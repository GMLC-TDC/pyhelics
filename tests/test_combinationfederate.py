# -*- coding: utf-8 -*-
import helics as h
import os

from .init import createBroker, createValueFederate, destroyFederate, destroyBroker

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def test_combination_federate():

    broker = createBroker()

    cfed = h.helicsCreateCombinationFederateFromConfig(os.path.join(CURRENT_DIRECTORY, "combinationfederate.json"))

    assert h.helicsFederateIsValid(cfed)

    assert h.helicsFederateGetEndpointCount(cfed) == 6
    assert h.helicsFederateGetFilterCount(cfed) == 6
    assert h.helicsFederateGetInputCount(cfed) == 7

    ept = h.helicsFederateGetEndpointByIndex(cfed, 0)

    assert h.helicsEndpointGetName(ept) == "EV_Controller/EV6"

    filt = h.helicsFederateGetFilterByIndex(cfed, 3)

    assert h.helicsFilterGetName(filt) == "EV_Controller/filterEV3"

    f = h.helicsFederateGetFilter(cfed, "EV_Controller/filterEV3")
    assert h.helicsFilterGetName(f) == "EV_Controller/filterEV3"

    ipt = h.helicsFederateGetInputByIndex(cfed, 4)
    assert h.helicsInputGetExtractionUnits(ipt) == ""
    assert h.helicsSubscriptionGetKey(ipt) == "IEEE_123_feeder_0/charge_EV3"

    h.helicsEndpointClearMessages(ept)

    h.helicsFederateDestroy(cfed)
    h.helicsBrokerDestroy(broker)
