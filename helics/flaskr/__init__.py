# -*- coding: utf-8 -*-
import logging
import os
import sys
from dataclasses import dataclass

from flask import Flask, render_template, send_from_directory, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
import werkzeug

from .. import database as db

current_directory = os.path.realpath(os.path.dirname(__file__))

app = Flask(__name__.split(".")[0], static_url_path="", static_folder=os.path.join(current_directory, "../../client/build"))
api = Api(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["UPLOAD_FOLDER"] = "/tmp/uploads"

cache = {
    "path": os.path.join(app.config["UPLOAD_FOLDER"], "helics-cli.sqlite.db"),
    "profile-path": os.path.join(app.config["UPLOAD_FOLDER"], "profile.txt"),
}


class DatabaseManager:
    def __init__(self, path_to_helics_db=cache["path"]):
        self.path_to_helics_db = path_to_helics_db
        self.instaniate()

    def instaniate(self):
        self.engine = db.create_engine(f"sqlite:///{self.path_to_helics_db}")
        self.connection = self.engine.connect()
        self.session = db.Session(self.engine)


class Database(Resource):
    def get(self):
        return cache["path"]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location="files")
        args = parser.parse_args()
        file = args["file"]
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], "helics-cli.sqlite.db"))
        cache["path"] = os.path.join(app.config["UPLOAD_FOLDER"], "helics-cli.sqlite.db")
        dm = DatabaseManager()
        return {"filename": dm.path_to_helics_db}


api.add_resource(Database, "/api/database")


class SystemInfo(Resource):
    def get(self):
        dm = DatabaseManager()
        return dm.session.query(db.SystemInfo).one().data


api.add_resource(SystemInfo, "/api/systeminfo")


class Cores(Resource):
    def get(self):
        dm = DatabaseManager()
        cores = dm.session.query(db.Cores).all()
        return [{"id": e.id, "name": e.name, "address": e.address} for e in cores if not e.name.startswith("__observer__")]


api.add_resource(Cores, "/api/cores")


class Federates(Resource):
    def get(self):
        dm = DatabaseManager()
        federates = dm.session.query(db.Federates).all()
        return [{"id": f.id, "name": f.name, "parent": f.parent} for f in federates if f.name != "__observer__"]


api.add_resource(Federates, "/api/federates")


class Graph(Resource):
    def get(self):
        dm = DatabaseManager()
        federate = dm.session.query(db.FederateGraph).one().data
        data = dm.session.query(db.DataGraph).one().data
        return {"federate": federate, "data": data}


api.add_resource(Graph, "/api/graphs")


class Subscriptions(Resource):
    def get(self):
        dm = DatabaseManager()
        subscriptions = dm.session.query(db.Subscriptions).all()
        return [db.as_dict(i) for i in subscriptions]


api.add_resource(Subscriptions, "/api/subscriptions")


class Inputs(Resource):
    def get(self):
        dm = DatabaseManager()
        inputs = dm.session.query(db.Inputs).all()
        return [db.as_dict(i) for i in inputs]


api.add_resource(Inputs, "/api/inputs")


class Publications(Resource):
    def get(self):
        dm = DatabaseManager()
        publications = dm.session.query(db.Publications).all()
        return [db.as_dict(i) for i in publications]


api.add_resource(Publications, "/api/publications")


class DataTable(Resource):
    def get(self):
        dm = DatabaseManager()
        Base = automap_base()
        Base.prepare(dm.engine, reflect=True)
        return [db.as_dict(i) for i in dm.session.query(Base.classes.datatable).all()]


api.add_resource(DataTable, "/api/data")

import re


class Profile(Resource):

    # <PROFILING>SenderFederate2[131074](initializing)HELICS CODE ENTRY<4570827706580384>[t=-1000000]</PROFILING>
    PATTERN = re.compile(
        r"""
                (?P<name>\w+)                           # SenderFederate2
                \[(\d+)\]                               # [131074]
                \((?P<state>\w+)\)                      # (initializing)
                (?P<message>(?:\w|\s)+)                 # HELICS CODE ENTRY
                \<(?P<realtime>\d+(?:\|\d+)?)\>         # <4570827706580384|534534523453>
                \[t=(?P<simtime>-?\d*\.{0,1}\d+)\]      # [t=-1000000]
                """,
        re.X,
    )

    def get(self):
        with open(cache["profile-path"]) as f:
            data = f.read()
        data = data.replace(r"<PROFILING>", "").replace(r"</PROFILING>", "")
        names = []
        states = []
        messages = []
        simtimes = []
        realtimes = []
        time_marker = {}
        for line in data.splitlines():
            m = self.PATTERN.match(line)
            name = m.group("name")
            state = m.group("state")
            message = m.group("message")
            simtime = float(m.group("simtime"))
            try:
                realtime = float(m.group("realtime"))
            except:
                realtime, markertime = m.group("realtime").split("|")
                time_marker[name] = float(markertime)
                realtime = float(realtime)
            names.append(name)
            states.append(state)
            messages.append(message)
            simtimes.append(simtime)
            realtimes.append(realtime)

        profile = {}
        for name in set(names):
            profile[name] = []

        invert = True
        if invert:
            for name in set(names):
                profile[name].append({})

        for (name, state, message, simtime, realtime) in zip(names, states, messages, simtimes, realtimes):
            if state == "created":
                continue
            if "ENTRY" in message and not invert:
                profile[name].append({"s_enter": simtime, "r_enter": realtime})
            elif "EXIT" in message and not invert:
                profile[name][-1]["s_end"] = simtime
                profile[name][-1]["r_end"] = realtime
            elif "EXIT" in message and invert:
                profile[name].append({"s_enter": simtime, "r_enter": realtime})
            elif "ENTRY" in message and invert:
                profile[name][-1]["s_end"] = simtime
                profile[name][-1]["r_end"] = realtime
        profiles = []
        names = {k: i for i, k in enumerate(sorted(profile.keys()))}

        end = "r_end"
        enter = "r_enter"
        scaling = 1e9

        for k in profile.keys():
            for i in profile[k]:
                if end in i.keys() and enter in i.keys():
                    i["name"] = k
                    i[enter] = i[enter] / scaling
                    i[end] = i[end] / scaling
                    profiles.append(i)
        return profiles

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location="files")
        args = parser.parse_args()
        file = args["file"]
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], "profile.txt"))
        cache["profile-path"] = os.path.join(app.config["UPLOAD_FOLDER"], "profile.txt")


api.add_resource(Profile, "/api/profile")


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def index(path):
    return send_from_directory(os.path.join(current_directory, "..", "static"), path)


def run():
    app.run(debug=os.environ.get("PYHELICS_FLASK_DEBUG", False))
