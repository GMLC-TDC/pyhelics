# -*- coding: utf-8 -*-
import logging
import json
import time
import os
import shlex
import subprocess
import sys
from dataclasses import dataclass
from typing import cast

from flask import Flask, render_template, send_from_directory, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
import werkzeug

import re

from .. import database as db

current_directory = os.path.realpath(os.path.dirname(__file__))

app = Flask(__name__.split(".")[0], static_url_path="", static_folder=os.path.join(current_directory, "../static"))
api = Api(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["UPLOAD_FOLDER"] = os.path.abspath(os.path.join(os.getcwd(), "__helics-server"))

cache = {
    "path": os.path.join(app.config["UPLOAD_FOLDER"], "helics-cli.sqlite.db"),
    "profile-path": os.path.join(app.config["UPLOAD_FOLDER"], "profile.txt"),
    "runner-path": os.path.join(app.config["UPLOAD_FOLDER"], "runner.json"),
    "runner-folder": app.config["UPLOAD_FOLDER"],
    "runner-file-name": "runner.json",
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


api.add_resource(Database, "/api/observer/database")


class SystemInfo(Resource):
    def get(self):
        dm = DatabaseManager()
        return dm.session.query(db.SystemInfo).one().data


api.add_resource(SystemInfo, "/api/observer/systeminfo")


class Cores(Resource):
    def get(self):
        dm = DatabaseManager()
        cores = dm.session.query(db.Cores).all()
        return [{"id": e.id, "name": e.name, "address": e.address} for e in cores if not e.name.startswith("__observer__")]


api.add_resource(Cores, "/api/observer/cores")


class Federates(Resource):
    def get(self):
        dm = DatabaseManager()
        federates = dm.session.query(db.Federates).all()
        return [{"id": f.id, "name": f.name, "parent": f.parent} for f in federates if f.name != "__observer__"]


api.add_resource(Federates, "/api/observer/federates")


class Graph(Resource):
    def get(self):
        dm = DatabaseManager()
        federate = dm.session.query(db.FederateGraph).one().data
        data = dm.session.query(db.DataGraph).one().data
        return {"federate": federate, "data": data}


api.add_resource(Graph, "/api/observer/graphs")


class Subscriptions(Resource):
    def get(self):
        dm = DatabaseManager()
        subscriptions = dm.session.query(db.Subscriptions).all()
        return [db.as_dict(i) for i in subscriptions]


api.add_resource(Subscriptions, "/api/observer/subscriptions")


class Inputs(Resource):
    def get(self):
        dm = DatabaseManager()
        inputs = dm.session.query(db.Inputs).all()
        return [db.as_dict(i) for i in inputs]


api.add_resource(Inputs, "/api/observer/inputs")


class Publications(Resource):
    def get(self):
        dm = DatabaseManager()
        publications = dm.session.query(db.Publications).all()
        return [db.as_dict(i) for i in publications]


api.add_resource(Publications, "/api/observer/publications")


class DataTable(Resource):
    def get(self):
        dm = DatabaseManager()
        Base = automap_base()
        Base.prepare(dm.engine, reflect=True)
        return [db.as_dict(i) for i in dm.session.query(Base.classes.datatable).all()]


api.add_resource(DataTable, "/api/observer/data")

status_tracker = {}


class RunnerFile(Resource):
    def get(self):
        if not os.path.exists(cache["runner-path"]):
            return {}
        with open(cache["runner-path"]) as f:
            data = json.loads(f.read())
        data["folder"] = cache["runner-folder"]
        data["path"] = cache["runner-path"]
        data["filename"] = cache["runner-file-name"]
        if data.get("broker", False) is True:
            data["federates"].append(
                {"directory": ".", "exec": "helics_broker -f{}".format(len(data["federates"])), "host": "localhost", "name": "broker"}
            )
        for federate in data["federates"]:
            if federate["directory"].startswith("."):
                federate["directory"] = os.path.abspath(os.path.join(data["folder"], federate["directory"]))
            federate["old_name"] = federate["name"]
            if os.path.exists(os.path.join(data["folder"], "{}.log".format(federate["name"]))):
                federate["log_available"] = True
            else:
                federate["log_available"] = False

            if federate["name"] in status_tracker:
                federate["status"] = status_tracker[federate["name"]]
            else:
                federate["status"] = None
        return data

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location="files")
        args = parser.parse_args()
        file = args["file"]
        path = cache["runner-folder"]
        name = cache["runner-file-name"]
        os.makedirs(path, exist_ok=True)
        file.save(os.path.join(path, name))
        cache["runner-path"] = os.path.join(path, name)


api.add_resource(RunnerFile, "/api/runner/file")


class RunnerFileName(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        args = parser.parse_args()
        name = args["name"]
        cache["runner-file-name"] = name
        cache["runner-path"] = os.path.join(cache["runner-folder"], cache["runner-file-name"])


api.add_resource(RunnerFileName, "/api/runner/file/name")


class RunnerFileFolder(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("folder", type=str)
        args = parser.parse_args()
        folder = args["folder"]
        cache["runner-folder"] = os.path.abspath(os.path.expanduser(folder))
        cache["runner-path"] = os.path.join(cache["runner-folder"], cache["runner-file-name"])


api.add_resource(RunnerFileFolder, "/api/runner/file/folder")


class RunnerFilePath(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("path", type=str)
        args = parser.parse_args()
        path = os.path.abspath(os.path.expanduser(args["path"]))
        cache["runner-path"] = path
        cache["runner-folder"] = os.path.dirname(path)
        cache["runner-file-name"] = os.path.basename(path)


api.add_resource(RunnerFilePath, "/api/runner/file/path")


class RunnerFileEdit(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("old_name", type=str)
        args = parser.parse_args()
        old_name = args["old_name"]
        with open(cache["runner-path"]) as f:
            data = json.loads(f.read())

        delete_index = None
        for i, f in enumerate(data["federates"]):
            if f["name"] == old_name:
                delete_index = i
                break
        data["federates"].pop(delete_index)
        with open(cache["runner-path"], "w") as f:
            f.write(json.dumps(data))
        return {"status": 200}

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("old_name", type=str)
        parser.add_argument("name", type=str)
        parser.add_argument("exec", type=str)
        parser.add_argument("directory", type=str)
        args = parser.parse_args()
        old_name = args["old_name"]
        name = args["name"]
        exec = args["exec"]
        directory = args["directory"]

        with open(cache["runner-path"]) as f:
            data = json.loads(f.read())

        for f in data["federates"]:
            if f["name"] == old_name:
                f["name"] = name
                f["exec"] = exec
                f["directory"] = directory
                break
        else:
            abort(417, description="Unknown name='{}'".format(old_name))

        with open(cache["runner-path"], "w") as f:
            f.write(json.dumps(data))

        return {"status": 200}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("exec", type=str)
        parser.add_argument("directory", type=str)
        args = parser.parse_args()
        name = args["name"]
        exec = args["exec"]
        directory = args["directory"]

        with open(cache["runner-path"]) as f:
            data = json.loads(f.read())

        for f in data["federates"]:
            if f["name"] == name:
                return abort(417, description="Name already exists {}".format(name))

        data["federates"].append(
            {
                "directory": directory,
                "exec": exec,
                "host": "localhost",
                "name": name,
            }
        )

        with open(cache["runner-path"], "w") as f:
            f.write(json.dumps(data))

        return {"status": 200}


api.add_resource(RunnerFileEdit, "/api/runner/file/edit")


class RunnerLog(Resource):
    def get(self, name):
        with open(cache["runner-path"]) as f:
            data = json.loads(f.read())
        with open(os.path.join(os.path.dirname(cache["runner-path"]), "{}.log".format(name))) as f:
            data = f.read()
        return {"log": data}


api.add_resource(RunnerLog, "/api/runner/log/<string:name>")


class RunnerRun(Resource):
    runner_server = {}

    def get(self):
        if self.runner_server.get("process", None) is not None:
            return {"status": True}
        else:
            return {"status": False}

    def post(self):
        if self.get()["status"]:
            self.delete()
        p = subprocess.Popen(shlex.split("helics run --path {} --connect-server".format(cache["runner-path"])))
        self.runner_server["process"] = p
        return {"status": True}

    def delete(self):
        self.runner_server["process"].terminate()
        self.runner_server["process"].kill()
        counter = 0
        while self.runner_server["process"].poll() is None or counter > 5:
            time.sleep(1)
            self.runner_server["process"].terminate()
            self.runner_server["process"].kill()
            counter += 1
        del self.runner_server["process"]
        global status_tracker
        status_tracker = {}
        return {"status": False}


api.add_resource(RunnerRun, "/api/runner/run")


class RunnerKillBroker(Resource):
    def post(self):
        name = "helics_broker"
        import platform

        if platform.system().lower().startswith("windows"):
            # windows OS
            if not name.endswith(".exe"):
                name = name + ".exe"
            os.system("taskkill /f /im {}".format(name))
            # os.system(r"start /b pcs.exe 2>&1")
            # with os.popen("tasklist | findstr \"pcs.exe\"") as f:
            #     temp_content = f.read()
            # if len(temp_content) == 0:
            #     pass
        else:
            if name.endswith(".exe"):
                name = name.replace(".exe", "")
            os.system("killall -9 {} 2>&1".format(name))


api.add_resource(RunnerKillBroker, "/api/runner/kill/broker")


class RunnerStatus(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name of federate")
        args = parser.parse_args()
        return {"status": status_tracker[args["name"]]}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name of federate")
        parser.add_argument("status", type=str, required=True, help="Status of federate")
        args = parser.parse_args()
        status_tracker[args["name"]] = args["status"]
        return {"status": status_tracker[args["name"]]}


api.add_resource(RunnerStatus, "/api/runner/status")


class Health(Resource):
    def get(self):
        return {"status": 200}


api.add_resource(Health, "/api/health")


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
            m = cast(re.Match[str], m)
            name = m.group("name")
            state = m.group("state")
            message = m.group("message")
            simtime = float(m.group("simtime"))
            try:
                realtime = float(m.group("realtime"))
            except ValueError:
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
        profiles = {}
        names = {k: i for i, k in enumerate(sorted(profile.keys()))}

        end = "r_end"
        enter = "r_enter"
        scaling = 1e9

        for k in profile.keys():
            profiles[k] = []
            for i in profile[k]:
                if end in i.keys() and enter in i.keys():
                    i["name"] = k
                    i[enter] = i[enter] / scaling
                    i[end] = i[end] / scaling
                    profiles[k].append(i)

        return profiles

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location="files")
        args = parser.parse_args()
        file = args["file"]
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], "profile.txt"))
        cache["profile-path"] = os.path.join(app.config["UPLOAD_FOLDER"], "profile.txt")
        return {"status": "success"}


api.add_resource(Profile, "/api/profiler/")


class APIException(Exception):
    def __init__(self, code, message):
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message

    def __str__(self):
        return self.__class__.__name__ + ": " + self.message


class BrokerServer(Resource):
    broker_server = {}

    def get(self):
        if self.broker_server.get("process", None) is not None:
            return {"status": True}
        else:
            return {"status": False}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("status", type=bool, required=True, help="requested status of broker server")
        args = parser.parse_args()
        status = args["status"]
        if status is True and self.broker_server.get("process", None) is not None:
            return abort(417, description="Unable to start server", status=True)
        elif status is False and self.broker_server.get("process", None) is None:
            return abort(417, description="Unable to stop server", status=False)
        elif status is True:
            p = subprocess.Popen(shlex.split("helics_broker_server --http"))
            self.broker_server["process"] = p
            return {"status": status}
        elif status is False:
            self.broker_server["process"].terminate()
            self.broker_server["process"].kill()
            counter = 0
            # TODO: Find out why broker server is not being terminated
            while self.broker_server["process"].poll() is None or counter > 5:
                time.sleep(1)
                self.broker_server["process"].terminate()
                self.broker_server["process"].kill()
                counter += 1
            del self.broker_server["process"]
            return {"status": status}


api.add_resource(BrokerServer, "/api/broker-server")


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def index(path):
    return send_from_directory(os.path.join(current_directory, "..", "static"), path)


def run():
    debug = bool(os.environ.get("PYHELICS_FLASK_DEBUG", False))
    if debug:
        host = None
    else:
        host = "0.0.0.0"
        cli = sys.modules["flask.cli"]
        cli.show_server_banner = lambda *x: None
        # os.environ["WERKZEUG_RUN_MAIN"] = "true"
    app.run(host=host, debug=debug)
