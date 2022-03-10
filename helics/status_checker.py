# -*- coding: utf-8 -*-
import threading
import time
import logging


class HELICSRuntimeError(RuntimeError):
    pass


logger = logging.getLogger(__name__)


class CheckStatusThread(threading.Thread):
    def __init__(self, process_list, should_kill):
        threading.Thread.__init__(self)
        self.should_kill = should_kill
        self._process_list = process_list
        self._status = {}

    def run(self):
        logger.info("Starting checks logger")
        for p in self._process_list:
            self._status[p.name] = 0
        has_failed = False
        while True:
            time.sleep(1)
            for p in self._process_list:
                if has_failed is True and self.should_kill is True:
                    p.process.kill()
                if p.process.poll() is not None and p.process.returncode != 0:
                    self._status[p.name] = p.process.returncode
                    if has_failed is False and self.should_kill is True:
                        print("Error: Process {} has failed, killing other processes".format(p.name))
                    has_failed = True

            all_p = [p.process.poll() for p in self._process_list if p.process.poll() is not None]
            if len(all_p) == len(self._process_list):
                if all(p == 0 for p in all_p):
                    return 0
                else:
                    raise HELICSRuntimeError("Error has occurred")
            else:
                continue
