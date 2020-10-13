# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import pytest as pt
import helics as h


def test_python_api():

    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1 --loglevel 1")

    fi = h.helicsCreateFederateInfo()
    h.helicsFederateInfoSetCoreInitString(fi, "--federates 1")
    h.helicsFederateInfoSetIntegerProperty(fi, h.HELICS_PROPERTY_INT_LOG_LEVEL, 5)
    fed = h.helicsCreateValueFederate("test1", fi)

    assert "publications = 0" in repr(fed)
    assert "inputs = 0" in repr(fed)
    assert "endpoints = 0" in repr(fed)
    assert "filters = 0" in repr(fed)

    assert fed.property["DELTA"] == 1e-09
    assert fed.property["PERIOD"] == 0.0
    assert fed.property["OFFSET"] == 0.0
    assert fed.property["RT_LAG"] == 0.0
    assert fed.property["RT_LEAD"] == 0.0
    assert fed.property["RT_TOLERANCE"] == 0.0
    assert fed.property["INPUT_DELAY"] == 0.0
    assert fed.property["OUTPUT_DELAY"] == 0.0
    assert fed.property["MAX_ITERATIONS"] == 50
    assert fed.property["LOG_LEVEL"] == 5
    # TODO: change this test when helics version is updated
    with pt.raises(h.HelicsException):
        assert fed.property["FILE_LOG_LEVEL"] == 1
    # TODO: change this test when helics version is updated
    with pt.raises(h.HelicsException):
        assert fed.property["CONSOLE_LOG_LEVEL"] == 1

    fed.property[h.HELICS_PROPERTY_INT_LOG_LEVEL] = 5

    assert fed.property[h.HelicsProperty.TIME_DELTA] == 1e-09
    assert fed.property[h.HelicsProperty.TIME_PERIOD] == 0.0
    assert fed.property[h.HelicsProperty.TIME_OFFSET] == 0.0
    assert fed.property[h.HelicsProperty.TIME_RT_LAG] == 0.0
    assert fed.property[h.HelicsProperty.TIME_RT_LEAD] == 0.0
    assert fed.property[h.HelicsProperty.TIME_RT_TOLERANCE] == 0.0
    assert fed.property[h.HelicsProperty.TIME_INPUT_DELAY] == 0.0
    assert fed.property[h.HelicsProperty.TIME_OUTPUT_DELAY] == 0.0
    assert fed.property[h.HelicsProperty.INT_MAX_ITERATIONS] == 50
    assert fed.property[h.HelicsProperty.INT_LOG_LEVEL] == 5
    assert fed.property[h.HelicsProperty.INT_FILE_LOG_LEVEL] == 5
    assert fed.property[h.HelicsProperty.INT_CONSOLE_LOG_LEVEL] == 5

    assert fed.property[h.HelicsProperty.TIME_DELTA.value] == 1e-09
    assert fed.property[h.HelicsProperty.TIME_PERIOD.value] == 0.0
    assert fed.property[h.HelicsProperty.TIME_OFFSET.value] == 0.0
    assert fed.property[h.HelicsProperty.TIME_RT_LAG.value] == 0.0
    assert fed.property[h.HelicsProperty.TIME_RT_LEAD.value] == 0.0
    assert fed.property[h.HelicsProperty.TIME_RT_TOLERANCE.value] == 0.0
    assert fed.property[h.HelicsProperty.TIME_INPUT_DELAY.value] == 0.0
    assert fed.property[h.HelicsProperty.TIME_OUTPUT_DELAY.value] == 0.0
    assert fed.property[h.HelicsProperty.INT_MAX_ITERATIONS.value] == 50
    assert fed.property[h.HelicsProperty.INT_LOG_LEVEL.value] == 5
    assert fed.property[h.HelicsProperty.INT_FILE_LOG_LEVEL.value] == 5
    assert fed.property[h.HelicsProperty.INT_CONSOLE_LOG_LEVEL.value] == 5

    assert fed.flag[h.HELICS_FLAG_OBSERVER] is False
    assert fed.flag[h.HELICS_FLAG_UNINTERRUPTIBLE] is False
    assert fed.flag[h.HELICS_FLAG_INTERRUPTIBLE] is True
    assert fed.flag[h.HELICS_FLAG_SOURCE_ONLY] is False
    assert fed.flag[h.HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE] is False
    assert fed.flag[h.HELICS_FLAG_ONLY_UPDATE_ON_CHANGE] is False
    assert fed.flag[h.HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE] is False
    assert fed.flag[h.HELICS_FLAG_RESTRICTIVE_TIME_POLICY] is False
    assert fed.flag[h.HELICS_FLAG_REALTIME] is False
    assert fed.flag[h.HELICS_FLAG_SLOW_RESPONDING] is False
    assert fed.flag[h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS] is False
    assert fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] is False

    fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] = True

    assert fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] is True

    del fed

    h.helicsBrokerDisconnect(broker)
    h.helicsBrokerFree(broker)

    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()
