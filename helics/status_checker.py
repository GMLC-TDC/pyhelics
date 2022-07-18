# -*- coding: utf-8 -*-
import threading
import time
import logging
import json
import urllib.request

from .utils import error


class HELICSRuntimeError(RuntimeError):
    pass


logger = logging.getLogger(__name__)

API = "http://127.0.0.1:5000/api"


class CheckStatusThread(threading.Thread):
    def __init__(self, process_list, should_kill, helics_server_available):
        threading.Thread.__init__(self)
        self.should_kill = should_kill
        self._process_list = process_list
        self._status = {}
        self._helics_server_available = helics_server_available

    def run(self):
        logger.info("Starting checks logger")
        for p in self._process_list:
            self._status[p.name] = 0
        has_failed = False
        while True:
            time.sleep(1)
            for p in self._process_list:
                self.status(p)
                if has_failed is True and self.should_kill is True:
                    p.process.kill()
                if p.process.poll() is not None and p.process.returncode != 0:
                    self._status[p.name] = p.process.returncode
                    if has_failed is False and self.should_kill is True:
                        error("Process {} has failed, killing other processes".format(p.name))
                    has_failed = True

            all_p = [p.process.poll() for p in self._process_list if p.process.poll() is not None]
            if len(all_p) == len(self._process_list):
                if all(p == 0 for p in all_p):
                    return 0
                else:
                    return -1
            else:
                continue

    def status(self, p):
        if self._helics_server_available:
            if p.process.poll() is None:
                status = "running"
            elif p.process.returncode == 0:
                status = "success"
            elif p.process.returncode == -9:
                status = "terminated"
            elif p.process.returncode != 0:
                status = "failed"
            else:
                status = "unknown"
            r = urllib.request.Request("{}/runner/status".format(API))
            r.add_header("Content-Type", "application/json; charset=utf-8")
            body = {"name": p.name, "status": status}
            bytes = json.dumps(body).encode("utf-8")
            r.add_header("Content-Length", str(len(bytes)))
            try:
                with urllib.request.urlopen(r, bytes) as response:
                    json.loads(response.read().decode(response.info().get_param("charset") or "utf-8"))
            except Exception as e:
                logger.exception("Severing connection with helics-cli server: {}".format(e))
                self._helics_server_available = False
