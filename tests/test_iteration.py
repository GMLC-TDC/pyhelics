# -*- coding: utf-8 -*-
import sys

import helics as h
import pytest as pt

from .utils import (
    create_broker,
    create_value_federate,
    destroy_federate,
    destroy_broker,
)


@pt.mark.skipif(sys.platform == "win32", reason="Fails to pass on windows")
def test_iteration_execution_iteration_test():
    broker = create_broker(1)
    vFed1, fedinfo = create_value_federate(1, "fed0")
    # register the publications

    pubid = h.helicsFederateRegisterGlobalPublication(
        vFed1, "pub1", h.HELICS_DATA_TYPE_DOUBLE, ""
    )

    subid = h.helicsFederateRegisterSubscription(vFed1, "pub1", "")
    h.helicsFederateSetTimeProperty(vFed1, h.HELICS_PROPERTY_TIME_DELTA, 1.0)

    h.helicsFederateEnterInitializingMode(vFed1)
    h.helicsPublicationPublishDouble(pubid, 27.0)

    comp = h.helicsFederateEnterExecutingModeIterative(
        vFed1, h.HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED
    )
    assert comp == h.HELICS_ITERATION_RESULT_ITERATING
    val = h.helicsInputGetDouble(subid)
    assert val == 27.0

    comp = h.helicsFederateEnterExecutingModeIterative(
        vFed1, h.HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED
    )

    assert comp == h.HELICS_ITERATION_RESULT_NEXT_STEP

    val2 = h.helicsInputGetDouble(subid)

    assert val2 == val

    h.helicsFederateDisconnect(vFed1)
    destroy_federate(vFed1, fedinfo)
    destroy_broker(broker)


@pt.mark.skipif(sys.platform == "win32", reason="Fails to pass on windows")
def test_iteration_async_test():
    broker = create_broker(1)
    vFed1, fedinfo1 = create_value_federate(1, "fed0")
    vFed2, fedinfo2 = create_value_federate(1, "fed1")

    # register the publications
    pub1 = h.helicsFederateRegisterGlobalPublication(
        vFed1, "pub1", h.HELICS_DATA_TYPE_INT
    )

    sub1 = h.helicsFederateRegisterSubscription(vFed2, "pub1")
    pub2 = h.helicsFederateRegisterGlobalPublication(
        vFed2, "pub2", h.HELICS_DATA_TYPE_INT
    )

    sub2 = h.helicsFederateRegisterSubscription(vFed1, "pub2")
    h.helicsFederateSetTimeProperty(vFed1, h.HELICS_PROPERTY_TIME_PERIOD, 1.0)
    h.helicsFederateSetTimeProperty(vFed2, h.HELICS_PROPERTY_TIME_PERIOD, 1.0)
    # vFed1->setLoggingLevel(5)
    # vFed2->setLoggingLevel(5)

    h.helicsFederateEnterInitializingModeAsync(vFed1)
    h.helicsFederateEnterInitializingMode(vFed2)
    h.helicsFederateEnterInitializingModeComplete(vFed1)

    c1 = 0
    c2 = 0

    h.helicsPublicationPublishInteger(pub1, c1)
    h.helicsPublicationPublishInteger(pub2, c2)

    h.helicsFederateEnterExecutingModeAsync(vFed1)
    h.helicsFederateEnterExecutingMode(vFed2)
    h.helicsFederateEnterExecutingModeComplete(vFed1)

    while c1 <= 10:
        h.helicsInputGetInteger(sub1), c1
        h.helicsInputGetInteger(sub2), c2
        c1 += 1
        c2 += 1

        if c1 <= 10:
            h.helicsPublicationPublishInteger(pub1, c1)
            h.helicsPublicationPublishInteger(pub2, c2)

        h.helicsFederateRequestTimeIterativeAsync(
            vFed1, 1.0, h.HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED
        )

        grantedTime, state = h.helicsFederateRequestTimeIterative(
            vFed2, 1.0, h.HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED
        )
        if c1 <= 10:
            # assert state == h.HELICS_ITERATION_RESULT_ITERATING
            assert grantedTime == 0.0
        else:
            # assert state == h.HELICS_ITERATION_RESULT_NEXT_STEP
            assert grantedTime == 1.0

        grantedTime, state = h.helicsFederateRequestTimeIterativeComplete(vFed1)
        if c1 <= 10:
            # assert state == h.HELICS_ITERATION_RESULT_ITERATING
            assert grantedTime == 0.0
            # assert state == h.HELICS_ITERATION_RESULT_NEXT_STEP
            # assert grantedTime == 1.0

    destroy_federate(vFed1, fedinfo1)
    destroy_federate(vFed2, fedinfo2)
    destroy_broker(broker)
