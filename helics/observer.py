# -*- coding: utf-8 -*-

import logging
import os
import time
import tempfile
from typing import Dict, List, cast
from datetime import datetime

import helics as h

from . import database as db

logger = logging.getLogger(__name__)
hdlr = logging.StreamHandler()
fmt = logging.Formatter("%(asctime)s %(name)-35s %(levelname)-8s %(message)s")
hdlr.setFormatter(fmt)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


class HelicsObserverFederate:
    """
    HelicsObserverFederate
    """

    def __init__(self, folder=None, core_type="zmq"):
        if folder is None:
            self._folder = tempfile.gettempdir()
        else:
            self._folder = folder
        self._core_type = core_type
        self._setup_engine()
        self._setup_federate()

    def _setup_engine(self):
        db_file = os.path.abspath(os.path.join(self._folder, "helics-cli.sqlite.db"))
        if os.path.exists(db_file):
            os.remove(db_file)
        self.engine = db.create_engine("sqlite+pysqlite:///{}".format(db_file), echo=False, future=True)
        db.Base.metadata.create_all(self.engine)
        self.session = db.Session(bind=self.engine)
        self.session.add(db.MetaData(name="helics_version", value=h.helicsGetVersion()))
        self.session.add(db.MetaData(name="created", value=datetime.now().isoformat()))
        self.session.add(db.SystemInfo(data=h.helicsGetSystemInfo()))

    def _setup_federate(self):
        self.name = "__observer__"
        self.fedinfo = h.helicsCreateFederateInfo()
        self.fedinfo.core_type = self._core_type
        self.fedinfo.property[h.HELICS_PROPERTY_TIME_DELTA] = 1.0
        self.fedinfo.property[h.HELICS_PROPERTY_TIME_PERIOD] = 1.0
        self.fedinfo.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] = True
        self.fedinfo.flag[h.HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING] = True
        self.fedinfo.flag[h.HELICS_FLAG_OBSERVER] = True
        logger.info("Creating observer")
        self.federate = h.helicsCreateCombinationFederate(self.name, self.fedinfo)
        logger.info("Entering initialization mode")
        self.federate.enter_initializing_mode()
        logger.info("Waiting for other federates")
        self.wait()
        self.get_data()
        self.hook()

    @property
    def federates(self) -> List[str]:
        return [cast(str, name) for name in self.federate.query("root", "federates")]

    @property
    def brokers(self) -> List[str]:
        return [cast(str, name) for name in self.federate.query("root", "brokers")]

    @property
    def publications(self) -> List[str]:
        return [cast(str, name) for name in self.federate.query("root", "publications")]

    @property
    def subscriptions(self) -> List[str]:
        return [cast(str, name) for name in self.federate.query("root", "subscriptions")]

    @property
    def inputs(self) -> List[str]:
        return [cast(str, name) for name in self.federate.query("root", "inputs")]

    def get_data(self):
        data = self.federate.query("root", "federate_map")
        data = cast(Dict, data)
        logger.info("Adding federategraph")
        self.session.add(db.FederateGraph(data=data))

        data = self.federate.query("root", "data_flow_graph")
        data = cast(Dict, data)
        logger.info("Adding datagraph")
        self.session.add(db.DataGraph(data=data))

        for core in data["cores"]:
            logger.info(f"Adding core {core}")
            self.session.add(
                db.Cores(
                    id=core["attributes"]["id"],
                    name=core["attributes"]["name"],
                    parent=core["attributes"]["parent"],
                    address=self.federate.query(core["attributes"]["name"], "address"),
                )
            )
            for federate in core["federates"]:
                assert federate["attributes"]["parent"] == core["attributes"]["id"]
                logger.info(f"Adding federate {federate}")
                self.session.add(db.Federates(id=federate["attributes"]["id"], name=federate["attributes"]["name"], parent=core["attributes"]["id"]))

                if "inputs" in federate.keys():
                    for input in federate["inputs"]:
                        logger.info(f"Adding input {input}")
                        if "sources" not in input.keys():
                            self.session.add(db.Inputs(source=input["federate"]))
                        else:
                            for s in input["sources"]:
                                self.session.add(db.Inputs(source=input["federate"], target=s["federate"]))

                if "publications" in federate.keys():
                    for publication in federate["publications"]:
                        logger.info(f"Adding publication {publication}")
                        if "targets" not in publication.keys():
                            self.session.add(db.Publications(source=publication["federate"]))
                        else:
                            for t in publication["targets"]:
                                self.session.add(db.Publications(name=publication["key"], target=publication["federate"], source=t["federate"]))

        self.session.commit()

        # Create a data table
        columns = [
            db.Column(col_name, col_type)
            for (col_name, col_type) in zip(
                self.federate.query("root", "publications"),
                [db.Float for _ in self.federate.query("root", "publications")],
            )
        ]
        columns.insert(0, db.Column("simulation_time", db.Float))
        columns.insert(0, db.Column("updated_at", db.Float))
        columns.insert(0, db.Column("id", db.Integer, db.Sequence("id"), primary_key=True, nullable=False))
        datatable = db.Table("datatable", db.Base.metadata, *columns)

        class DataTable(db.Base):
            __table__ = datatable

        self.DataTable = DataTable
        db.Base.metadata.create_all(self.engine)

    def hook(self):
        for pub in self.publications:
            s = self.federate.register_subscription(pub)
            s.set_default(0.0)

    def wait(self):
        federates = self.federates
        while not all(self.federate.query(name, "isinit") is True for name in federates):
            for name in federates:
                logger.debug(f"{name} isinit = {self.federate.query(name, 'isinit')}")
            time.sleep(1)

    def run(self):
        self.federate.enter_executing_mode()
        while True:
            for name in self.federates:
                if self.federate.query(name, "state") == "disconnected":
                    self.session.add(
                        db.FederateEventLogs(
                            name=name,
                            updated_at=time.time(),
                            state="disconnected",
                        )
                    )
                    continue
                data = cast(dict, self.federate.query(name, "current_time"))
                self.session.add(
                    db.FederateEventLogs(
                        name=name,
                        updated_at=time.time(),
                        granted_time=data["granted_time"],
                        requested_time=data["requested_time"],
                        state="executing",
                    )
                )
            simulation_time = self.federate.request_next_step()
            d = {"simulation_time": simulation_time}
            logger.info(self.federate.subscriptions)
            for k, sub in self.federate.subscriptions.items():
                d[k] = sub.value
            self.session.add(self.DataTable(updated_at=time.time(), **d))
            self.session.commit()

            if (
                all(self.federate.query(name, "state") == "disconnected" for name in self.federates if name != "__observer__")
                or simulation_time >= 9223372036.3
            ):
                break


if __name__ == "__main__":
    o = HelicsObserverFederate()
    o.run()
