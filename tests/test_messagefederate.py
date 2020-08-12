# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import time
import helics as h
import pytest as pt

from test_init import createBroker, createValueFederate, destroyFederate, destroyBroker, createMessageFederate


@pt.fixture
def mFed():
    initstring = "-f 1 --name=mainbroker"
    fedinitstring = "--broker=mainbroker --federates=1"
    deltat = 0.01

    h.helicsGetVersion()

    # Create broker #
    broker = h.helicsCreateBroker("zmq", "", initstring)

    isconnected = h.helicsBrokerIsConnected(broker)

    if isconnected == 1:
        pass

    # Create Federate Info object that describes the federate properties #
    fedinfo = h.helicsCreateFederateInfo()

    # Set Federate name #
    h.helicsFederateInfoSetCoreName(fedinfo, "CoreA Federate")

    # Set core type from string #
    h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")

    # Federate init string #
    h.helicsFederateInfoSetCoreInitString(fedinfo, fedinitstring)

    # Set the message interval (timedelta) for federate. Note th#
    # HELICS minimum message time interval is 1 ns and by default
    # it uses a time delta of 1 second. What is provided to the
    # setTimedelta routine is a multiplier for the default timedelta.

    # Set one second message interval #
    h.helicsFederateInfoSetTimeProperty(fedinfo, h.HELICS_PROPERTY_TIME_DELTA, deltat)

    h.helicsFederateInfoSetIntegerProperty(fedinfo, h.HELICS_PROPERTY_INT_LOG_LEVEL, 1)

    mFed = h.helicsCreateMessageFederate("TestA Federate", fedinfo)

    yield mFed

    h.helicsFederateFinalize(mFed)
    state = h.helicsFederateGetState(mFed)
    assert state == 3
    while h.helicsBrokerIsConnected(broker):
        time.sleep(1)

    h.helicsFederateInfoFree(fedinfo)
    h.helicsFederateFree(mFed)
    h.helicsCloseLibrary()


def test_message_federate_initialize(mFed):
    state = h.helicsFederateGetState(mFed)
    assert state == 0
    h.helicsFederateEnterExecutingMode(mFed)

    state = h.helicsFederateGetState(mFed)
    assert state == 2


def test_message_federate_endpoint_registration(mFed):
    epid1 = h.helicsFederateRegisterEndpoint(mFed, "ep1", "")
    epid2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "ep2", "random")

    h.helicsFederateEnterExecutingMode(mFed)

    endpoint_name = h.helicsEndpointGetName(epid1)
    assert endpoint_name == "TestA Federate/ep1"

    endpoint_name = h.helicsEndpointGetName(epid2)
    assert endpoint_name == "ep2"

    endpoint_name = h.helicsEndpointGetType(epid1)
    assert endpoint_name == ""

    endpoint_name = h.helicsEndpointGetType(epid2)
    assert endpoint_name == "random"


def test_message_federate_send(mFed):
    epid1 = h.helicsFederateRegisterEndpoint(mFed, "ep1", "")
    epid2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "ep2", "random")

    h.helicsFederateSetTimeProperty(mFed, h.HELICS_PROPERTY_TIME_DELTA, 1.0)
    h.helicsFederateEnterExecutingMode(mFed)

    data = "random-data"

    h.helicsEndpointSendEventRaw(epid1, "ep2", data, 1.0)

    granted_time = h.helicsFederateRequestTime(mFed, 2.0)
    assert granted_time == 1.0

    res = h.helicsFederateHasMessage(mFed)
    assert res == 1

    res = h.helicsEndpointHasMessage(epid1)
    assert res == 0

    res = h.helicsEndpointHasMessage(epid2)
    assert res == 1

    message = h.helicsEndpointGetMessage(epid2)

    assert h.helicsMessageGetMessageID(message) == 55
    assert h.helicsMessageIsValid(message) is True
    assert h.helicsMessageGetString(message) == "random-data"
    assert h.helicsMessageGetRawDataSize(message) == 11
    assert h.helicsMessageGetOriginalDestination(message) == ""
    assert h.helicsMessageGetOriginalSource(message) == "TestA Federate/ep1"
    assert h.helicsMessageGetSource(message) == "TestA Federate/ep1"
    assert h.helicsMessageGetTime(message) == 1.0


def test_messagefederate_test_message_federate_initialize(mFed):

    state = h.helicsFederateGetState(mFed)
    assert state == 0
    h.helicsFederateEnterExecutingMode(mFed)

    state = h.helicsFederateGetState(mFed)
    assert state == 2


def test_messagefederate_test_message_federate_endpoint_registration(mFed):

    epid1 = h.helicsFederateRegisterEndpoint(mFed, "ep1", "")
    epid2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "ep2", "random")

    h.helicsFederateEnterExecutingMode(mFed)

    assert h.HELICS_STATE_EXECUTION == h.helicsFederateGetState(mFed)

    endpoint_name = h.helicsEndpointGetName(epid1)
    assert endpoint_name == "TestA Federate/ep1"

    endpoint_name = h.helicsEndpointGetName(epid2)
    assert endpoint_name == "ep2"

    endpoint_name = h.helicsEndpointGetType(epid1)
    assert endpoint_name == ""

    endpoint_name = h.helicsEndpointGetType(epid2)
    assert endpoint_name == "random"

    epid_b = h.helicsFederateGetEndpoint(mFed, "ep2")
    type = h.helicsEndpointGetType(epid_b)
    assert type == "random"

    epid_c = h.helicsFederateGetEndpointByIndex(mFed, 0)
    name = h.helicsEndpointGetName(epid_c)
    assert name == "TestA Federate/ep1"


def test_messagefederate_test_message_federate_send(mFed):

    epid1 = h.helicsFederateRegisterEndpoint(mFed, "ep1", "")
    epid2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "ep2", "random")

    h.helicsFederateSetTimeProperty(mFed, h.HELICS_PROPERTY_TIME_DELTA, 1.0)
    h.helicsFederateEnterExecutingMode(mFed)

    data = "random-data"

    h.helicsEndpointSendEventRaw(epid1, "ep2", data, 1.0)

    granted_time = h.helicsFederateRequestTime(mFed, 2.0)
    assert granted_time == 1.0

    res = h.helicsFederateHasMessage(mFed)
    assert res is True

    res = h.helicsEndpointHasMessage(epid1)
    assert res is False

    res = h.helicsEndpointHasMessage(epid2)
    assert res is True

    message = h.helicsEndpointGetMessage(epid2)

    assert h.helicsMessageGetMessageID(message) == 55
    assert h.helicsMessageIsValid(message) is True
    assert h.helicsMessageGetString(message) == "random-data"
    assert h.helicsMessageGetRawDataSize(message) == 11
    assert h.helicsMessageGetOriginalDestination(message) == ""
    assert h.helicsMessageGetOriginalSource(message) == "TestA Federate/ep1"
    assert h.helicsMessageGetSource(message) == "TestA Federate/ep1"
    assert h.helicsMessageGetTime(message) == 1.0
    # @test_broken False
    # assert h.helicsMessageGetRawData(message) == None


def test_messagefederate_send_receive_2fed_multisend():

    broker = createBroker(2)
    mFed1, fedinfo1 = createMessageFederate(1, "A Federate")
    mFed2, fedinfo2 = createMessageFederate(1, "B Federate")

    epid1 = h.helicsFederateRegisterEndpoint(mFed1, "ep1", "")
    epid2 = h.helicsFederateRegisterGlobalEndpoint(mFed2, "ep2", "random")

    h.helicsEndpointSetOption(epid1, h.HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS, True)

    h.helicsFederateSetTimeProperty(mFed1, h.HELICS_PROPERTY_TIME_DELTA, 1.0)
    h.helicsFederateSetTimeProperty(mFed2, h.HELICS_PROPERTY_TIME_DELTA, 1.0)

    h.helicsFederateEnterExecutingModeAsync(mFed1)
    h.helicsFederateEnterExecutingMode(mFed2)
    h.helicsFederateEnterExecutingModeComplete(mFed1)

    assert h.HELICS_STATE_EXECUTION == h.helicsFederateGetState(mFed1)
    assert h.HELICS_STATE_EXECUTION == h.helicsFederateGetState(mFed2)

    h.helicsEndpointSetDefaultDestination(epid1, "ep2")

    h.helicsEndpointSendMessageRaw(epid1, "", "a".encode())
    h.helicsEndpointSendMessageRaw(epid1, "", "a".encode())
    h.helicsEndpointSendMessageRaw(epid1, "", "a".encode())

    h.helicsFederateRequestTimeAsync(mFed1, 1.0)
    granted_time = h.helicsFederateRequestTime(mFed2, 1.0)
    complete_time = h.helicsFederateRequestTimeComplete(mFed1)

    assert granted_time == 1.0
    assert complete_time == 1.0

    res = h.helicsEndpointPendingMessages(epid2)
    assert res == 3

    res = h.helicsFederatePendingMessages(mFed2)
    assert res == 3

    assert h.helicsEndpointGetDefaultDestination(epid1) == "ep2"

    # FIXME: Someday this will be implemented.
    # @test_broken h.helicsEndpointGetOption(epid1, h.HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS) is True

    destroyFederate(mFed1, fedinfo1)
    destroyFederate(mFed2, fedinfo2)
    destroyBroker(broker)


def test_messagefederate_message_object_tests(mFed):

    epid1 = h.helicsFederateRegisterEndpoint(mFed, "ep1", "")
    epid2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "ep2", "random")

    h.helicsFederateSetTimeProperty(mFed, h.HELICS_PROPERTY_TIME_DELTA, 1.0)

    h.helicsFederateEnterExecutingMode(mFed)

    assert h.helicsFederateGetState(mFed) == h.HELICS_STATE_EXECUTION

    msg = h.helicsFederateCreateMessage(mFed)
    h.helicsMessageSetDestination(msg, "ep2")
    h.helicsMessageGetDestination(msg) == "ep2"
    h.helicsMessageSetData(msg, "".join(["a" for _ in range(0, 500)]).encode())
    h.helicsMessageSetTime(msg, 0.0)

    h.helicsEndpointSendMessage(epid1, msg)
    t = h.helicsFederateRequestTime(mFed, 1.0)
    assert t == 1.0

    assert h.helicsFederateHasMessage(mFed) is True
    assert h.helicsEndpointHasMessage(epid1) is False
    assert h.helicsEndpointHasMessage(epid2) is True

    msg = h.helicsEndpointGetMessage(epid2)
    assert h.helicsMessageGetRawDataSize(msg) == 500
    # TODO: segfaults
    # print(h.helicsMessageGetRawData(msg))
    # @test_broken False
    # segfaults
    # rawdata = h.helicsMessageGetRawDataPointer(msg)
    # assert Char(unsafe_load(Ptr{Cchar}(rdata), 245)) == 'a'

    h.helicsFederateFinalize(mFed)

    assert h.helicsFederateGetState(mFed) == h.HELICS_STATE_FINALIZE

    h.helicsMessageSetFlagOption(msg, 7, True)
    assert h.helicsMessageCheckFlag(msg, 7) is True
    h.helicsMessageClearFlags(msg)
    assert h.helicsMessageCheckFlag(msg, 7) is False

    h.helicsEndpointSetDefaultDestination(epid1, "ep2")


def test_messagefederate_timing_tests():

    broker = createBroker(1)
    vFed1, fedinfo1 = createMessageFederate(1, "fed0")
    vFed2, fedinfo2 = createMessageFederate(1, "fed1")

    h.helicsFederateSetTimeProperty(vFed1, h.HELICS_PROPERTY_TIME_PERIOD, 0.1)
    h.helicsFederateSetTimeProperty(vFed2, h.HELICS_PROPERTY_TIME_PERIOD, 0.1)

    h.helicsFederateSetTimeProperty(vFed2, h.HELICS_PROPERTY_TIME_INPUT_DELAY, 0.1)

    h.helicsFederateSetFlagOption(vFed1, h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS, True)
    h.helicsFederateSetFlagOption(vFed2, h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS, True)

    ept1 = h.helicsFederateRegisterGlobalEndpoint(vFed1, "e1", "")
    h.helicsFederateRegisterGlobalEndpoint(vFed2, "e2", "")

    h.helicsFederateEnterExecutingModeAsync(vFed1)
    h.helicsFederateEnterExecutingMode(vFed2)
    h.helicsFederateEnterExecutingModeComplete(vFed1)
    h.helicsFederateRequestTimeAsync(vFed2, 2.0)
    gtime = h.helicsFederateRequestTime(vFed1, 1.0)
    # check that the request is only granted at the appropriate period
    assert gtime == 1.0

    assert h.helicsFederateGetIntegerProperty(vFed1, h.HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL) == -1
    assert h.helicsFederateGetIntegerProperty(vFed2, h.HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL) == -1

    assert h.helicsFederateGetFlagOption(vFed1, h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS) is True
    assert h.helicsFederateGetFlagOption(vFed2, h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS) is True

    h.helicsEndpointSendMessageRaw(ept1, "e2", "test1".encode())
    h.helicsFederateRequestTimeAsync(vFed1, 1.9)
    gtime = h.helicsFederateRequestTimeComplete(vFed2)
    assert gtime >= 1.1  # the message should show up at the next available time point after the impact window
    h.helicsFederateRequestTimeAsync(vFed2, 2.0)
    gtime = h.helicsFederateRequestTimeComplete(vFed1)
    assert gtime >= 1.9

    tres = h.helicsFederateGetTimeProperty(vFed1, h.HELICS_PROPERTY_TIME_PERIOD)
    assert tres == 0.1

    # m = h.helicsEndpointGetMessage(ept1)
    # @show h.helicsMessageGetRawData(m)
    # TODO: null pointer received from C

    gtime = h.helicsFederateRequestTimeComplete(vFed2)
    assert gtime == 2.0
    h.helicsFederateFinalize(vFed1)
    h.helicsFederateFinalize(vFed2)

    destroyFederate(vFed1, fedinfo1)
    destroyFederate(vFed2, fedinfo2)
    destroyBroker(broker)
