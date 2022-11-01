# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import helics as h
import os

import pytest
import pytest as pt

from test_init import createBroker, createValueFederate, destroyFederate, destroyBroker, createMessageFederate

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def test_filter_type_tests_registration():

    broker = createBroker(2)
    fFed, fedinfo1 = createMessageFederate(1, "filter")
    mFed, fedinfo2 = createMessageFederate(1, "message")

    h.helicsFederateRegisterGlobalEndpoint(mFed, "port1", "")
    h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "")

    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "filter1")
    h.helicsFilterAddSourceTarget(f1, "port1")

    f2 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "filter2")
    h.helicsFilterAddDestinationTarget(f2, "port2")

    assert f1 != f2

    _ = h.helicsFederateRegisterEndpoint(fFed, "fout", "")

    f3 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "c4")
    h.helicsFilterAddSourceTarget(f3, "Testfilter/fout")

    f1_b = h.helicsFederateGetFilter(fFed, "filter1")
    tmp = h.helicsFilterGetName(f1_b)
    assert tmp == "Testfilter/filter1"

    f1_c = h.helicsFederateGetFilterByIndex(fFed, 2)
    tmp = h.helicsFilterGetName(f1_c)
    assert tmp == "Testfilter/c4"

    # @test_throws h.HELICSErrorInvalidArgument f1_n = h.helicsFederateGetFilterByIndex(fFed, -2)

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)
    h.helicsFederateDisconnectAsync(mFed)
    h.helicsFederateDisconnect(fFed)
    h.helicsFederateDisconnectComplete(mFed)

    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(fFed, fedinfo1)
    destroyFederate(mFed, fedinfo2)
    destroyBroker(broker)


def test_filter_type_tests_info():

    broker = createBroker(2)
    fFed, fedinfo1 = createMessageFederate(1, "filter")
    mFed, fedinfo2 = createMessageFederate(1, "message")

    p1 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port1", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "")

    h.helicsEndpointSetInfo(p1, "p1_test")
    h.helicsEndpointSetInfo(p2, "p2_test")

    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "filter1")
    h.helicsFilterAddSourceTarget(f1, "port1")
    h.helicsFilterSetInfo(f1, "f1_test")

    f2 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "filter2")
    h.helicsFilterAddDestinationTarget(f2, "port2")
    h.helicsFilterSetInfo(f2, "f2_test")

    ep1 = h.helicsFederateRegisterEndpoint(fFed, "fout", "")
    h.helicsEndpointSetInfo(ep1, "ep1_test")
    f3 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "c4")
    h.helicsFilterAddSourceTarget(f3, "filter0/fout")
    h.helicsFilterSetInfo(f3, "f3_test")

    assert h.helicsEndpointGetInfo(p1) == "p1_test"
    assert h.helicsEndpointGetInfo(p2) == "p2_test"
    assert h.helicsEndpointGetInfo(ep1) == "ep1_test"

    assert h.helicsFilterGetInfo(f1) == "f1_test"
    assert h.helicsFilterGetInfo(f2) == "f2_test"
    assert h.helicsFilterGetInfo(f3) == "f3_test"

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)

    h.helicsFederateDisconnectAsync(mFed)
    h.helicsFederateDisconnect(fFed)
    h.helicsFederateDisconnectComplete(mFed)

    destroyFederate(fFed, fedinfo1)
    destroyFederate(mFed, fedinfo2)
    destroyBroker(broker)


def test_filter_types_tests_core_filter_registration():

    core1 = h.helicsCreateCore("inproc", "core1", "--autobroker")

    core2 = h.helicsCoreClone(core1)

    core1IdentifierString = h.helicsCoreGetIdentifier(core1)

    assert core1IdentifierString == "core1"

    sourceFilter1 = h.helicsCoreRegisterFilter(core1, h.HELICS_FILTER_TYPE_DELAY, "core1SourceFilter")

    h.helicsFilterAddSourceTarget(sourceFilter1, "ep1")
    destinationFilter1 = h.helicsCoreRegisterFilter(core1, h.HELICS_FILTER_TYPE_DELAY, "core1DestinationFilter")

    h.helicsFilterAddDestinationTarget(destinationFilter1, "ep2")
    cloningFilter1 = h.helicsCoreRegisterCloningFilter(core1, "ep3")

    h.helicsFilterRemoveDeliveryEndpoint(cloningFilter1, "ep3")
    core1IsConnected = h.helicsCoreIsConnected(core1)
    assert core1IsConnected != 0
    h.helicsCoreSetReadyToInit(core1)
    h.helicsCoreDisconnect(core1)
    h.helicsCoreDisconnect(core2)
    # h.helicsCoreFree(core1)
    # h.helicsCoreFree(core2)
    h.helicsCloseLibrary()


def test_filter_type_tests_message_filter_function():

    broker = createBroker(2)
    fFed, fedinfo1 = createMessageFederate(1, "filter")
    mFed, fedinfo2 = createMessageFederate(1, "message")

    h.helicsFederateSetFlagOption(mFed, h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS, True)
    p1 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port1", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "")

    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_DELAY, "filter1")
    h.helicsFilterAddSourceTarget(f1, "port1")
    h.helicsFilterSet(f1, "delay", 2.5)

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)

    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_EXECUTION
    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "port2")

    h.helicsFederateRequestTimeAsync(mFed, 1.0)
    h.helicsFederateRequestTime(fFed, 1.0)
    h.helicsFederateRequestTimeComplete(mFed)

    assert h.helicsFederateHasMessage(mFed) is False

    h.helicsFederateRequestTimeAsync(mFed, 2.0)
    h.helicsFederateRequestTime(fFed, 2.0)
    h.helicsFederateRequestTimeComplete(mFed)
    assert h.helicsEndpointHasMessage(p2) is False

    h.helicsFederateRequestTimeAsync(fFed, 3.0)
    h.helicsFederateRequestTime(mFed, 3.0)

    assert h.helicsEndpointHasMessage(p2) is True

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "port1"
    assert h.helicsMessageGetOriginalSource(m2) == "port1"
    assert h.helicsMessageGetDestination(m2) == "port2"
    assert h.helicsMessageGetByteCount(m2) == len(data)
    assert h.helicsMessageGetTime(m2) == 2.5

    h.helicsFederateRequestTime(mFed, 3.0)
    h.helicsFederateRequestTimeComplete(fFed)
    h.helicsFederateDisconnectAsync(mFed)
    h.helicsFederateDisconnect(fFed)
    h.helicsFederateDisconnectComplete(mFed)
    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(fFed, fedinfo1)
    destroyFederate(mFed, fedinfo2)
    destroyBroker(broker)


def test_filter_test_types_function_mobj():

    broker = createBroker(2)
    fFed, fedinfo1 = createMessageFederate(1, "filter")
    mFed, fedinfo2 = createMessageFederate(1, "message")

    h.helicsFederateSetFlagOption(mFed, h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS, True)
    p1 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port1", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "")

    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_DELAY, "filter1")
    h.helicsFilterAddSourceTarget(f1, "port1")
    h.helicsFilterSet(
        f1, "delay", 2.5,
    )

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)

    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_EXECUTION

    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "port2")

    h.helicsFederateRequestTimeAsync(mFed, 1.0)
    h.helicsFederateRequestTime(fFed, 1.0)
    h.helicsFederateRequestTimeComplete(mFed)

    res = h.helicsFederateHasMessage(mFed)
    assert res is False

    h.helicsFederateRequestTimeAsync(mFed, 2.0)
    h.helicsFederateRequestTime(fFed, 2.0)
    h.helicsFederateRequestTimeComplete(mFed)
    assert h.helicsEndpointHasMessage(p2) is False

    h.helicsFederateRequestTimeAsync(fFed, 3.0)
    h.helicsFederateRequestTime(mFed, 3.0)

    assert h.helicsEndpointHasMessage(p2) is True

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "port1"
    assert h.helicsMessageGetOriginalSource(m2) == "port1"
    assert h.helicsMessageGetDestination(m2) == "port2"
    assert h.helicsMessageGetByteCount(m2) == len(data)
    assert h.helicsMessageGetTime(m2) == 2.5

    h.helicsFederateRequestTime(mFed, 3.0)
    h.helicsFederateRequestTimeComplete(fFed)
    h.helicsFederateDisconnectAsync(mFed)
    h.helicsFederateDisconnect(fFed)
    h.helicsFederateDisconnectComplete(mFed)
    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(fFed, fedinfo1)
    destroyFederate(mFed, fedinfo2)
    destroyBroker(broker)


def test_filter_test_types_function_two_stage():

    broker = createBroker(3)
    fFed, fedinfo1 = createMessageFederate(1, "filter")
    fFed2, fedinfo2 = createMessageFederate(1, "filter2")
    mFed, fedinfo3 = createMessageFederate(1, "message")

    p1 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port1", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "")

    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_DELAY, "filter1")
    h.helicsFilterAddSourceTarget(f1, "port1")
    h.helicsFilterSet(f1, "delay", 1.25)

    f2 = h.helicsFederateRegisterFilter(fFed2, h.HELICS_FILTER_TYPE_DELAY, "filter2")
    h.helicsFilterAddSourceTarget(f2, "port1")
    h.helicsFilterSet(f2, "delay", 1.25)

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingModeAsync(fFed2)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)
    h.helicsFederateEnterExecutingModeComplete(fFed2)

    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_EXECUTION
    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "port2")

    h.helicsFederateRequestTimeAsync(mFed, 0.0)
    h.helicsFederateRequestTimeAsync(fFed, 1.0)
    h.helicsFederateRequestTime(fFed2, 1.0)
    h.helicsFederateRequestTimeComplete(mFed)
    h.helicsFederateRequestTimeComplete(fFed)
    assert h.helicsFederateHasMessage(mFed) is False

    h.helicsFederateRequestTimeAsync(mFed, 0.0)
    h.helicsFederateRequestTimeAsync(fFed2, 2.0)
    h.helicsFederateRequestTime(fFed, 2.0)
    h.helicsFederateRequestTimeComplete(mFed)
    h.helicsFederateRequestTimeComplete(fFed2)
    assert h.helicsEndpointHasMessage(p2) is False

    h.helicsFederateRequestTimeAsync(fFed, 3.0)
    h.helicsFederateRequestTimeAsync(fFed2, 3.0)
    h.helicsFederateRequestTime(mFed, 3.0)
    assert h.helicsEndpointHasMessage(p2) is True

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "port1"
    assert h.helicsMessageGetOriginalSource(m2) == "port1"
    assert h.helicsMessageGetDestination(m2) == "port2"
    assert h.helicsMessageGetByteCount(m2) == len(data)
    assert h.helicsMessageGetTime(m2) == 2.5

    h.helicsFederateRequestTimeComplete(fFed)
    h.helicsFederateRequestTimeComplete(fFed2)
    h.helicsFederateDisconnectAsync(mFed)
    h.helicsFederateDisconnectAsync(fFed)
    h.helicsFederateDisconnect(fFed2)
    h.helicsFederateDisconnectComplete(mFed)
    h.helicsFederateDisconnectComplete(fFed)
    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(fFed, fedinfo1)
    destroyFederate(fFed2, fedinfo2)
    destroyFederate(mFed, fedinfo3)
    destroyBroker(broker)


def test_filter_test_types_function2():

    broker = createBroker(2)
    fFed, fedinfo1 = createMessageFederate(1, "filter")
    mFed, fedinfo2 = createMessageFederate(1, "message")

    p1 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port1", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "")

    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_DELAY, "filter1")
    h.helicsFilterAddSourceTarget(f1, "port1")
    h.helicsFilterSet(f1, "delay", 2.5)

    f2 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_DELAY, "filter2")
    h.helicsFilterAddSourceTarget(f2, "port2")
    h.helicsFilterSet(f2, "delay", 2.5)
    # this is expected to fail since a regular filter doesn't have a delivery endpoint
    # @test_throws h.HELICSErrorInvalidObject h.helicsFilterAddDeliveryEndpoint(f2, "port1")

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)

    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_EXECUTION

    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "port2")

    h.helicsFederateRequestTimeAsync(mFed, 1.0)
    h.helicsFederateRequestTime(fFed, 1.0)
    h.helicsFederateRequestTimeComplete(mFed)

    res = h.helicsFederateHasMessage(mFed)
    assert res is False

    h.helicsEndpointSendBytesTo(p2, data, "port1")
    h.helicsFederateRequestTimeAsync(mFed, 2.0)
    h.helicsFederateRequestTime(fFed, 2.0)
    h.helicsFederateRequestTimeComplete(mFed)
    assert h.helicsEndpointHasMessage(p2) is False
    # there may be something wrong here yet but this test isn't the one to find it and
    # this may prevent spurious errors for now.
    # std::this_thread::yield()
    h.helicsFederateRequestTime(mFed, 3.0)

    assert h.helicsEndpointHasMessage(p2) is True

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "port1"
    assert h.helicsMessageGetOriginalSource(m2) == "port1"
    assert h.helicsMessageGetDestination(m2) == "port2"
    assert h.helicsMessageGetByteCount(m2) == len(data)
    assert h.helicsMessageGetTime(m2) == 2.5

    assert h.helicsEndpointHasMessage(p1) is False

    h.helicsFederateRequestTime(mFed, 4.0)
    assert h.helicsEndpointHasMessage(p1) is True
    h.helicsFederateDisconnectAsync(mFed)
    h.helicsFederateDisconnect(fFed)
    h.helicsFederateDisconnectComplete(mFed)
    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(fFed, fedinfo1)
    destroyFederate(mFed, fedinfo2)
    destroyBroker(broker)


def test_filter_test_types_message_filter_function3():

    broker = createBroker(2)
    fFed, fedinfo1 = createMessageFederate(1, "filter", 1)
    mFed, fedinfo2 = createMessageFederate(1, "message", 1)

    p1 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port1", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "random")

    f1 = h.helicsFederateRegisterGlobalFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "filter1")
    h.helicsFilterAddSourceTarget(f1, "port1")
    f2 = h.helicsFederateRegisterGlobalFilter(fFed, h.HELICS_FILTER_TYPE_DELAY, "filter2")
    h.helicsFilterAddSourceTarget(f2, "port1")

    h.helicsFederateRegisterEndpoint(fFed, "fout", "")
    f3 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_RANDOM_DELAY, "filter3")
    h.helicsFilterAddSourceTarget(f3, "filter0/fout")

    h.helicsFilterSet(f2, "delay", 2.5)

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)

    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_EXECUTION

    data = "hello world".encode()
    h.helicsEndpointSendBytesTo(p1, data, "port2")

    h.helicsFederateRequestTimeAsync(mFed, 1.0)
    h.helicsFederateRequestTime(fFed, 1.0)
    h.helicsFederateRequestTimeComplete(mFed)

    assert h.helicsFederateHasMessage(mFed) is False

    h.helicsEndpointSendBytesTo(p2, data, "port1")
    h.helicsFederateRequestTimeAsync(mFed, 2.0)
    h.helicsFederateRequestTime(fFed, 2.0)
    h.helicsFederateRequestTimeComplete(mFed)
    assert h.helicsEndpointHasMessage(p2) is False
    # there may be something wrong here yet but this test isn't the one to find it and
    # this may prevent spurious errors for now.
    # std::this_thread::yield()
    h.helicsFederateRequestTimeAsync(mFed, 3.0)
    h.helicsFederateRequestTime(fFed, 3.0)
    h.helicsFederateRequestTimeComplete(mFed)

    assert h.helicsEndpointHasMessage(p2)

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "port1"
    assert h.helicsMessageGetOriginalSource(m2) == "port1"
    assert h.helicsMessageGetDestination(m2) == "port2"
    assert h.helicsMessageGetByteCount(m2) == len(data)
    assert h.helicsMessageGetTime(m2) == 2.5

    assert h.helicsEndpointHasMessage(p1) is True
    h.helicsFederateDisconnect(mFed)
    h.helicsFederateDisconnect(fFed)
    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(mFed, fedinfo1)
    destroyFederate(fFed, fedinfo2)
    destroyBroker(broker)


def test_filter_test_types_clone_test():

    broker = createBroker(3)
    sFed, fedinfo1 = createMessageFederate(1, "source", 1)
    dFed, fedinfo2 = createMessageFederate(1, "dest", 1)
    dcFed, fedinfo3 = createMessageFederate(1, "dest_clone", 1)

    p1 = h.helicsFederateRegisterGlobalEndpoint(sFed, "src", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(dFed, "dest", "")
    p3 = h.helicsFederateRegisterGlobalEndpoint(dcFed, "cm", "")

    f1 = h.helicsFederateRegisterCloningFilter(dcFed, "")
    h.helicsFilterAddDeliveryEndpoint(f1, "cm")
    h.helicsFilterAddSourceTarget(f1, "src")

    h.helicsFederateEnterExecutingModeAsync(sFed)
    h.helicsFederateEnterExecutingModeAsync(dcFed)
    h.helicsFederateEnterExecutingMode(dFed)
    h.helicsFederateEnterExecutingModeComplete(sFed)
    h.helicsFederateEnterExecutingModeComplete(dcFed)

    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_EXECUTION
    state = h.helicsFederateGetState(dcFed)
    assert state == h.HELICS_STATE_EXECUTION
    state = h.helicsFederateGetState(dFed)
    assert state == h.HELICS_STATE_EXECUTION

    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "dest")

    h.helicsFederateRequestTimeAsync(sFed, 1.0)
    h.helicsFederateRequestTimeAsync(dcFed, 1.0)
    h.helicsFederateRequestTime(dFed, 1.0)
    h.helicsFederateRequestTimeComplete(sFed)
    h.helicsFederateRequestTimeComplete(dcFed)

    assert h.helicsFederateHasMessage(dFed)

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "src"
    assert h.helicsMessageGetOriginalSource(m2) == "src"
    assert h.helicsMessageGetDestination(m2) == "dest"
    assert h.helicsMessageGetByteCount(m2) == len(data)

    assert h.helicsFederateHasMessage(dcFed)

    m2 = h.helicsEndpointGetMessage(p3)
    assert h.helicsMessageGetSource(m2) == "src"
    assert h.helicsMessageGetOriginalSource(m2) == "src"
    assert h.helicsMessageGetDestination(m2) == "cm"
    assert h.helicsMessageGetOriginalDestination(m2) == "dest"
    assert h.helicsMessageGetByteCount(m2) == len(data)

    h.helicsFederateDisconnectAsync(sFed)
    h.helicsFederateDisconnectAsync(dFed)
    h.helicsFederateDisconnect(dcFed)
    h.helicsFederateDisconnectComplete(sFed)
    h.helicsFederateDisconnectComplete(dFed)
    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(sFed, fedinfo1)
    destroyFederate(dFed, fedinfo2)
    destroyFederate(dcFed, fedinfo3)
    destroyBroker(broker)


def test_filter_test_types_clone_test_connections():

    broker = createBroker(3)
    sFed, fedinfo1 = createMessageFederate(1, "source", 1.0,)
    dFed, fedinfo2 = createMessageFederate(1, "dest", 1.0)
    dcFed, fedinfo3 = createMessageFederate(1, "dest_clone", 1.0)

    p1 = h.helicsFederateRegisterGlobalEndpoint(sFed, "src", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(dFed, "dest", "")
    p3 = h.helicsFederateRegisterGlobalEndpoint(dcFed, "cm", "")

    f1 = h.helicsFederateRegisterGlobalCloningFilter(dcFed, "filt1")
    h.helicsFilterAddDeliveryEndpoint(f1, "cm")
    cr = h.helicsFederateGetCore(sFed)

    h.helicsCoreAddSourceFilterToEndpoint(cr, "filt1", "src")
    # h.helicsCoreAddSourceFilterToEndpoint(cr, "", "src")

    h.helicsFederateEnterExecutingModeAsync(sFed)
    h.helicsFederateEnterExecutingModeAsync(dcFed)
    h.helicsFederateEnterExecutingMode(dFed)
    h.helicsFederateEnterExecutingModeComplete(sFed)
    h.helicsFederateEnterExecutingModeComplete(dcFed)

    q = h.helicsCreateQuery("", "filtered_endpoints")
    filteredEndpoints = h.helicsQueryExecute(q, sFed)
    # assert "srcFilters" in str(filteredEndpoints)
    # assert "(cloning)" in str(filteredEndpoints)
    # h.helicsQueryFree(q)

    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_EXECUTION
    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "dest")

    h.helicsFederateRequestTimeAsync(sFed, 1.0)
    h.helicsFederateRequestTimeAsync(dcFed, 1.0)
    h.helicsFederateRequestTime(dFed, 1.0)
    h.helicsFederateRequestTimeComplete(sFed)
    h.helicsFederateRequestTimeComplete(dcFed)

    assert h.helicsFederateHasMessage(dFed) is True

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "src"
    assert h.helicsMessageGetOriginalSource(m2) == "src"
    assert h.helicsMessageGetDestination(m2) == "dest"
    assert h.helicsMessageGetByteCount(m2) == len(data)

    assert h.helicsFederateHasMessage(dcFed) is True

    m2 = h.helicsEndpointGetMessage(p3)
    assert h.helicsMessageGetSource(m2) == "src"
    assert h.helicsMessageGetOriginalSource(m2) == "src"
    assert h.helicsMessageGetDestination(m2) == "cm"
    assert h.helicsMessageGetOriginalDestination(m2) == "dest"
    assert h.helicsMessageGetByteCount(m2) == len(data)

    h.helicsFederateDisconnectAsync(sFed)
    h.helicsFederateDisconnectAsync(dFed)
    h.helicsFederateDisconnect(dcFed)
    h.helicsFederateDisconnectComplete(sFed)
    h.helicsFederateDisconnectComplete(dFed)
    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(sFed, fedinfo1)
    destroyFederate(dFed, fedinfo2)
    destroyFederate(dcFed, fedinfo3)
    destroyBroker(broker)


def test_filter_test_types_clone_test_broker_connections():
    broker = createBroker(3)
    sFed, fedinfo1 = createMessageFederate(1, "source", 1.0)
    dFed, fedinfo2 = createMessageFederate(1, "dest", 1.0)
    dcFed, fedinfo3 = createMessageFederate(1, "dest_clone", 1.0)

    p1 = h.helicsFederateRegisterGlobalEndpoint(sFed, "src", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(dFed, "dest", "")
    p3 = h.helicsFederateRegisterGlobalEndpoint(dcFed, "cm", "")

    f1 = h.helicsFederateRegisterGlobalCloningFilter(dcFed, "filt1")
    h.helicsFilterAddDeliveryEndpoint(f1, "cm")

    h.helicsBrokerAddSourceFilterToEndpoint(broker, "filt1", "src")
    h.helicsBrokerAddSourceFilterToEndpoint(broker, "", "src")

    h.helicsFederateEnterExecutingModeAsync(sFed)
    h.helicsFederateEnterExecutingModeAsync(dcFed)
    h.helicsFederateEnterExecutingMode(dFed)
    h.helicsFederateEnterExecutingModeComplete(sFed)
    h.helicsFederateEnterExecutingModeComplete(dcFed)

    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_EXECUTION
    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "dest")

    h.helicsFederateRequestTimeAsync(sFed, 1.0)
    h.helicsFederateRequestTimeAsync(dcFed, 1.0)
    h.helicsFederateRequestTime(dFed, 1.0)
    h.helicsFederateRequestTimeComplete(sFed)
    h.helicsFederateRequestTimeComplete(dcFed)

    assert h.helicsFederateHasMessage(dFed) is True

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "src"
    assert h.helicsMessageGetOriginalSource(m2) == "src"
    assert h.helicsMessageGetDestination(m2) == "dest"
    assert h.helicsMessageGetByteCount(m2) == len(data)

    assert h.helicsFederateHasMessage(dcFed) is True

    m2 = h.helicsEndpointGetMessage(p3)
    assert h.helicsMessageGetSource(m2) == "src"
    assert h.helicsMessageGetOriginalSource(m2) == "src"
    assert h.helicsMessageGetDestination(m2) == "cm"
    assert h.helicsMessageGetOriginalDestination(m2) == "dest"
    assert h.helicsMessageGetByteCount(m2) == len(data)

    h.helicsFederateDisconnectAsync(sFed)
    h.helicsFederateDisconnectAsync(dFed)
    h.helicsFederateDisconnect(dcFed)
    h.helicsFederateDisconnectComplete(sFed)
    h.helicsFederateDisconnectComplete(dFed)
    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(sFed, fedinfo1)
    destroyFederate(dFed, fedinfo2)
    destroyFederate(dcFed, fedinfo3)
    destroyBroker(broker)


@pt.mark.skip(reason="Fails to run on Windows")
def test_filter_test_types_clone_test_dest_connections():
    broker = createBroker(3)
    sFed, fedinfo1 = createMessageFederate(1, "source", 1.0)
    dFed, fedinfo2 = createMessageFederate(1, "dest", 1.0)
    dcFed, fedinfo3 = createMessageFederate(1, "dest_clone", 2.0)

    p1 = h.helicsFederateRegisterGlobalEndpoint(sFed, "src", "")
    _ = h.helicsFederateRegisterGlobalEndpoint(dFed, "dest", "")
    _ = h.helicsFederateRegisterGlobalEndpoint(dcFed, "cm", "")

    f1 = h.helicsFederateRegisterGlobalCloningFilter(dcFed, "filt1")
    h.helicsFilterAddDeliveryEndpoint(f1, "cm")

    cr = h.helicsFederateGetCore(sFed)

    h.helicsCoreAddDestinationFilterToEndpoint(cr, "filt1", "dest")

    h.helicsCoreAddDestinationFilterToEndpoint(cr, "", "dest")

    # h.helicsCoreFree(cr)

    h.helicsFederateEnterExecutingModeAsync(sFed)
    h.helicsFederateEnterExecutingModeAsync(dcFed)
    h.helicsFederateEnterExecutingMode(dFed)
    h.helicsFederateEnterExecutingModeComplete(sFed)
    h.helicsFederateEnterExecutingModeComplete(dcFed)

    q = h.helicsCreateQuery("", "filtered_endpoints")
    filteredEndpoints = h.helicsQueryExecute(q, dFed)
    assert "cloningdestFilter" in str(filteredEndpoints)
    # h.helicsQueryFree(q)

    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_EXECUTION
    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "dest")

    h.helicsFederateDisconnect(sFed)

    # TODO: implement threading

    # auto dFedExec = [&]() {
    #     h.helicsFederateRequestTime(dFed, 1.0)
    #     m2 = h.helicsEndpointGetMessage(p2)
    #     h.helicsFederateDisconnect(dFed, "")
    # }

    # h.helics_message m3
    # auto dcFedExec = [&]() {
    #     h.helicsFederateRequestTime(dcFed, 2.0)
    #     auto res = h.helicsFederateHasMessage(dcFed)
    #     if (res == h.helics_False) {
    #         std::this_thread::sleep_for(std::chrono::milliseconds(50))
    #         h.helicsFederateRequestTime(dcFed, 4.0)
    #     }
    #     m3 = h.helicsEndpointGetMessage(p3)
    #     h.helicsFederateDisconnect(dcFed)
    # }

    # auto threaddFed = std::thread(dFedExec)
    # auto threaddcFed = std::thread(dcFedExec)

    # threaddFed.join()
    # (m2.source, "src")
    # (m2.original_source, "src")
    # (m2.dest, "dest")
    # (m2.length, static_cast<int64_t>(data.size()))

    # threaddcFed.join()

    # (m3.source, "src")
    # (m3.original_source, "src")
    # (m3.dest, "cm")
    # (m3.original_dest, "dest")
    # (m3.length, static_cast<int64_t>(data.size()))

    # (state = h.helicsFederateGetState(sFed))
    # (state == h.helics_state_finalize)

    destroyFederate(sFed, fedinfo1)
    destroyFederate(dFed, fedinfo2)
    destroyFederate(dcFed, fedinfo3)
    destroyBroker(broker)


try:

    @h.ffi.callback("void logger(helics_message_object, void* userData)")
    def filterFunc1(mess, userData):
        m = h.HelicsMessage(mess)
        time = h.helicsMessageGetTime(m)
        h.helicsMessageSetTime(m, time + 2.5)


except:

    @h.ffi.callback("void logger(HelicsMessage, void* userData)")
    def filterFunc1(mess, userData):
        m = h.HelicsMessage(mess)
        time = h.helicsMessageGetTime(m)
        h.helicsMessageSetTime(m, time + 2.5)


class UserData(object):
    def __init__(self, x):
        self.x = x


@pt.mark.skip(reason="Fails to pass on CI")
def test_filter_callback_test():

    broker = createBroker(2)

    assert """helics.HelicsBroker(identifier = "mainbroker", address = "tcp://127.0.0.1:23404")""" in repr(broker)

    fFed, fedinfo1 = createMessageFederate(1, "filter", 1.0)
    mFed, fedinfo2 = createMessageFederate(1, "message", 1.0)

    h.helicsFederateSetFlagOption(mFed, h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS, True)

    p1 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port1")
    p2 = h.helicsFederateRegisterGlobalEndpoint(mFed, "port2", "")

    assert (
        """helics.HelicsEndpoint(name = "port1", type = "", info = "", is_valid = True, default_destination = "", n_pending_messages = 0)"""
        in repr(p1)
    )
    assert (
        """helics.HelicsEndpoint(name = "port2", type = "", info = "", is_valid = True, default_destination = "", n_pending_messages = 0)"""
        in repr(p2)
    )

    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "filter1")
    f2 = h.helicsFederateRegisterFilter(mFed, h.HELICS_FILTER_TYPE_DELAY, "dfilter")

    h.helicsFilterAddSourceTarget(f1, "port1")

    assert 'name = "Testfilter/filter1"' in repr(f1)

    userdata = UserData(5)

    handle = h.ffi.new_handle(userdata)
    h.helicsFilterSetCustomCallback(f1, filterFunc1, handle)

    with pt.raises(h.HelicsException):
        h.helicsFilterSetCustomCallback(f2, filterFunc1, handle)

    assert (
        """helics.HelicsMessageFederate(name = "Testfilter", state = HelicsFederateState.STARTUP, current_time = -9223372036.854776, n_publications = 0, n_subscriptions = 0, n_endpoints = 0, n_filters = 1, n_pending_messages = 0)"""
        in repr(fFed)
    )
    assert (
        """helics.HelicsMessageFederate(name = "Testmessage", state = HelicsFederateState.STARTUP, current_time = -9223372036.854776, n_publications = 0, n_subscriptions = 0, n_endpoints = 2, n_filters = 1, n_pending_messages = 0)"""
        in repr(mFed)
    )

    h.helicsFederateEnterExecutingModeAsync(fFed)
    h.helicsFederateEnterExecutingMode(mFed)
    h.helicsFederateEnterExecutingModeComplete(fFed)

    assert (
        """helics.HelicsMessageFederate(name = "Testfilter", state = HelicsFederateState.EXECUTION, current_time = 0.0, n_publications = 0, n_subscriptions = 0, n_endpoints = 0, n_filters = 1, n_pending_messages = 0)"""
        in repr(fFed)
    )
    assert (
        """helics.HelicsMessageFederate(name = "Testmessage", state = HelicsFederateState.EXECUTION, current_time = 0.0, n_publications = 0, n_subscriptions = 0, n_endpoints = 2, n_filters = 1, n_pending_messages = 0)"""
        in repr(mFed)
    )

    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_EXECUTION
    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "port2")

    h.helicsFederateRequestTimeAsync(mFed, 1.0)
    h.helicsFederateRequestTime(fFed, 1.0)
    h.helicsFederateRequestTimeComplete(mFed)

    assert h.helicsFederateHasMessage(mFed) is False

    h.helicsFederateRequestTimeAsync(mFed, 2.0)
    h.helicsFederateRequestTime(fFed, 2.0)
    h.helicsFederateRequestTimeComplete(mFed)
    assert h.helicsEndpointHasMessage(p2) is False

    h.helicsFederateRequestTimeAsync(fFed, 3.0)
    h.helicsFederateRequestTime(mFed, 3.0)

    assert h.helicsEndpointHasMessage(p2)

    m2 = h.helicsEndpointGetMessage(p2)
    assert h.helicsMessageGetSource(m2) == "port1"
    assert h.helicsMessageGetOriginalSource(m2) == "port1"
    assert h.helicsMessageGetDestination(m2) == "port2"
    assert h.helicsMessageGetByteCount(m2) == len(data)
    assert h.helicsMessageGetTime(m2) == 2.5

    h.helicsFederateRequestTime(mFed, 3.0)
    h.helicsFederateRequestTimeComplete(fFed)
    h.helicsFederateDisconnectAsync(mFed)
    h.helicsFederateDisconnect(fFed)
    h.helicsFederateDisconnectComplete(mFed)
    state = h.helicsFederateGetState(fFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(fFed, fedinfo1)
    destroyFederate(mFed, fedinfo2)
    destroyBroker(broker)


@pt.mark.skip(reason="Fails to pass on CI")
def test_filter_test_types_clone_test_broker_dest_connections():

    broker = createBroker(3)
    sFed, fedinfo1 = createMessageFederate(1, "source", 1.0)
    dFed, fedinfo2 = createMessageFederate(1, "dest", 1.0)
    dcFed, fedinfo3 = createMessageFederate(1, "dest_clone", 1.0)

    p1 = h.helicsFederateRegisterGlobalEndpoint(sFed, "src", "")
    p2 = h.helicsFederateRegisterGlobalEndpoint(dFed, "dest", "")
    p3 = h.helicsFederateRegisterGlobalEndpoint(dcFed, "cm", "")

    f1 = h.helicsFederateRegisterGlobalCloningFilter(dcFed, "filt1")
    h.helicsFilterAddDeliveryEndpoint(f1, "cm")
    h.helicsBrokerAddDestinationFilterToEndpoint(broker, "filt1", "dest")

    h.helicsBrokerAddDestinationFilterToEndpoint(broker, "", "dest")

    h.helicsFederateEnterExecutingModeAsync(sFed)
    h.helicsFederateEnterExecutingModeAsync(dcFed)
    h.helicsFederateEnterExecutingMode(dFed)
    h.helicsFederateEnterExecutingModeComplete(sFed)
    h.helicsFederateEnterExecutingModeComplete(dcFed)

    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_EXECUTION
    data = "".join(["a" for _ in range(0, 500)]).encode()
    h.helicsEndpointSendBytesTo(p1, data, "dest")

    h.helicsFederateRequestTimeAsync(sFed, 1.0)
    h.helicsFederateRequestTimeAsync(dcFed, 1.0)
    h.helicsFederateRequestTime(dFed, 1.0)
    h.helicsFederateRequestTimeComplete(sFed)
    h.helicsFederateRequestTimeComplete(dcFed)

    assert h.helicsFederateHasMessage(dFed) is True

    m2 = h.helicsEndpointGetMessage(p2)

    assert h.helicsMessageGetSource(m2) == "src"
    assert h.helicsMessageGetOriginalSource(m2) == "src"
    assert h.helicsMessageGetDestination(m2) == "dest"
    assert h.helicsMessageGetByteCount(m2) == len(data)

    h.helicsFederateDisconnectAsync(sFed)
    h.helicsFederateDisconnectAsync(dFed)

    # TODO: figure out why this test fails on CI
    # @test_broken False
    # assert h.helicsFederateHasMessage(dcFed) is False

    # h.helicsFederateRequestTime(dcFed, 2.0)

    # assert h.helicsFederateHasMessage(dcFed) is True

    # m2 = h.helicsEndpointGetMessage(p3)
    # assert h.helicsMessageGetSource(m2) == "src"
    # assert h.helicsMessageGetOriginalSource(m2) == "src"
    # assert h.helicsMessageGetDestination(m2) == "cm"
    # assert h.helicsMessageGetOriginalDestination(m2) == "dest"
    # assert h.helicsMessageGetByteCount(m2) == len(data)

    # _ = h.helicsFederateHasMessage(dcFed)

    h.helicsFederateDisconnect(dcFed)
    h.helicsFederateDisconnectComplete(sFed)
    h.helicsFederateDisconnectComplete(dFed)
    state = h.helicsFederateGetState(sFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(sFed, fedinfo1)
    destroyFederate(dFed, fedinfo2)
    destroyFederate(dcFed, fedinfo3)
    destroyBroker(broker)


def test_filter_test_file_load():

    filename = os.path.join(CURRENT_DIRECTORY, "filters.json")
    mFed = h.helicsCreateMessageFederateFromConfig(filename)

    name = h.helicsFederateGetName(mFed)
    assert name == "filterFed"

    assert h.helicsFederateGetEndpointCount(mFed) == 3
    h.helicsFederateDisconnect(mFed)
    h.helicsCloseLibrary()
