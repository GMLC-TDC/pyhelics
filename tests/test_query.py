# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import time
import helics as h

from test_init import createBroker, createValueFederate, destroyFederate, destroyBroker, createMessageFederate


def test_query_federate_tests():

    broker = createBroker(2)
    vFed1, fedinfo1 = createValueFederate(1, "fed0")
    vFed2, fedinfo2 = createValueFederate(1, "fed1")

    h.helicsFederateRegisterGlobalTypePublication(vFed1, "pub1", "double", "")
    h.helicsFederateRegisterTypePublication(vFed1, "pub2", "double", "")
    h.helicsFederateRegisterTypePublication(vFed2, "pub3", "double", "")
    h.helicsFederateEnterInitializingModeAsync(vFed1)
    h.helicsFederateEnterInitializingMode(vFed2)
    h.helicsFederateEnterInitializingModeComplete(vFed1)

    core = h.helicsFederateGetCoreObject(vFed1)

    q1 = h.helicsCreateQuery("Testfed0", "publications")
    res = h.helicsQueryCoreExecute(q1, core)
    try:
        assert res == "[pub1;Testfed0/pub2]"
    except:
        assert res == ["pub1", "Testfed0/pub2"]
    # res = h.helicsQueryExecute(q1, vFed2)
    # assert res == "[pub1;Testfed0/pub2]"
    h.helicsQueryFree(q1)

    # q1 = h.helicsCreateQuery("Testfed1", "isinit")
    # res = h.helicsQueryExecute(q1, vFed1)
    # assert res, "True"
    # h.helicsQueryFree(q1)

    # q1 = h.helicsCreateQuery("Testfed1", "publications")
    # res = h.helicsQueryExecute(q1, vFed1)
    # assert res == "[Testfed1/pub3]"
    # h.helicsQueryFree(q1)

    h.helicsCoreFree(core)
    h.helicsFederateFinalizeAsync(vFed1)
    h.helicsFederateFinalize(vFed2)
    h.helicsFederateFinalizeComplete(vFed1)

    destroyFederate(vFed1, fedinfo1)
    destroyFederate(vFed2, fedinfo2)
    destroyBroker(broker)


def test_query_broker_tests():

    broker = createBroker(2)
    vFed1, fedinfo1 = createValueFederate(1, "fed0")
    vFed2, fedinfo2 = createValueFederate(1, "fed1")
    core = h.helicsFederateGetCoreObject(vFed1)

    q1 = h.helicsCreateQuery("root", "federates")
    res = h.helicsQueryCoreExecute(q1, core)
    name1 = h.helicsFederateGetName(vFed1)
    name2 = h.helicsFederateGetName(vFed2)

    try:
        assert f"[{name1};{name2}]" == res
    except AssertionError:
        assert [name1, name2] == res

    res = h.helicsQueryExecute(q1, vFed1)
    try:
        assert f"[{name1};{name2}]" == res
    except AssertionError:
        assert [name1, name2] == res

    h.helicsFederateEnterInitializingModeAsync(vFed1)
    h.helicsFederateEnterInitializingMode(vFed2)
    h.helicsFederateEnterInitializingModeComplete(vFed1)
    h.helicsQueryFree(q1)
    h.helicsCoreFree(core)
    h.helicsFederateFinalizeAsync(vFed1)
    h.helicsFederateFinalize(vFed2)
    h.helicsFederateFinalizeComplete(vFed1)

    destroyFederate(vFed1, fedinfo1)
    destroyFederate(vFed2, fedinfo2)
    destroyBroker(broker)
