# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import time
import pytest
import helics as h
from helics.federate import Federate


def test_python_api():

    fi = h.helicsCreateFederateInfo()
    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1 --loglevel 1")
    h.helicsFederateInfoSetCoreInitString(fi, "--federates 1")

    h.helicsFederateInfoSetIntegerProperty(fi, h.HELICS_PROPERTY_INT_LOG_LEVEL, 5)

    fed = Federate(name="test1", federate_info=fi)

    assert "publications = 0" in repr(fed)
    assert "inputs = 0" in repr(fed)
    assert "endpoints = 0" in repr(fed)
    assert "filters = 0" in repr(fed)

    del fed

    h.helicsFederateInfoFree(fi)

    h.helicsBrokerDisconnect(broker)
    h.helicsBrokerFree(broker)

    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()
