# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import helics as h
import os
import pytest as pt

from test_init import createBroker, createValueFederate, destroyFederate, destroyBroker

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def test_combination_federate():

    broker = createBroker()

    cfed = h.helicsCreateCombinationFederateFromConfig(os.path.join(CURRENT_DIRECTORY, "combinationfederate.json"))

    assert h.helicsFederateIsValid(cfed)

    assert h.helicsFederateGetEndpointCount(cfed) == 2
    assert h.helicsFederateGetFilterCount(cfed) == 0
    assert h.helicsFederateGetInputCount(cfed) == 2

    ept = h.helicsFederateGetEndpointByIndex(cfed, 0)

    assert h.helicsEndpointGetName(ept) == "ept1"

    ipt = h.helicsFederateGetInputByIndex(cfed, 1)
    assert h.helicsInputGetExtractionUnits(ipt) == ""
    assert h.helicsSubscriptionGetKey(ipt) == "comboFed/pub2"

    h.helicsEndpointClearMessages(ept)

    h.helicsFederateDestroy(cfed)
    h.helicsBrokerDestroy(broker)
    h.helicsCloseLibrary()
