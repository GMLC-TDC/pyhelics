# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import time
import pytest
import pytest as pt
import helics as h

from test_init import createBroker, createValueFederate, destroyFederate, destroyBroker


def test_misc_functions_api():
    print(h.helicsGetBuildFlags())
    assert len(h.helicsGetBuildFlags()) > 0
    assert len(h.helicsGetCompilerVersion()) > 0
    with pytest.raises(h.HelicsException):
        h.helicsCreateCore("something random", "here", "not an init string")


def test_broker_api():
    assert h.helicsIsCoreTypeAvailable("zmq") == 1
    broker1 = h.helicsCreateBroker("zmq", "broker1", "--federates 3 --loglevel=warning")
    broker2 = h.helicsBrokerClone(broker1)
    address_string = h.helicsBrokerGetAddress(broker1)
    assert "tcp://127.0.0.1:23404" in address_string
    assert "broker1" in h.helicsBrokerGetIdentifier(broker1)
    err = h.helicsErrorInitialize()
    h.helicsErrorClear(err)
    assert err.error_code == 0
    assert h.ffi.string(err.message).decode() == ""
    assert h.helicsBrokerIsValid(broker1) == 1
    assert h.helicsBrokerIsConnected(broker1) == 1
    h.helicsBrokerDisconnect(broker1)
    assert h.helicsBrokerIsConnected(broker1) == 0
    h.helicsBrokerDisconnect(broker2)
    # h.helicsBrokerFree(broker1)
    # h.helicsBrokerFree(broker2)
    h.helicsCloseLibrary()


def test_core_api():

    core1 = h.helicsCreateCore("inproc", "core1", "--autobroker")
    assert h.helicsCoreIsValid(core1) is True
    core2 = h.helicsCoreClone(core1)
    assert "core1" in h.helicsCoreGetIdentifier(core1)

    assert h.helicsCoreIsConnected(core1) == 0

    sourceFilter1 = h.helicsCoreRegisterFilter(core1, h.HELICS_FILTER_TYPE_DELAY, "core1SourceFilter")
    h.helicsFilterAddSourceTarget(sourceFilter1, "ep1")
    destinationFilter1 = h.helicsCoreRegisterFilter(core1, h.HELICS_FILTER_TYPE_DELAY, "core1DestinationFilter")
    h.helicsFilterAddDestinationTarget(destinationFilter1, "ep2")
    cloningFilter1 = h.helicsCoreRegisterCloningFilter(core1, "ep3")
    h.helicsFilterRemoveDeliveryEndpoint(cloningFilter1, "ep3")

    h.helicsCoreSetReadyToInit(core1)
    h.helicsCoreDisconnect(core1)
    h.helicsCoreDisconnect(core2)
    # h.helicsCoreFree(core1)
    # h.helicsCoreFree(core2)
    h.helicsCloseLibrary()


class UserData(object):
    def __init__(self, x):
        self.x = x


@h.ffi.callback("void logger(int loglevel, const char* identifier, const char* message, void* userData)")
def logger(loglevel: int, identifier: str, message: str, userData: object):
    userData = h.ffi.from_handle(userData)
    print(f"{loglevel}, {h.ffi.string(identifier).decode()}, {h.ffi.string(message).decode()}, {userData}")
    userData.x += 1


def test_logging_api():

    fi = h.helicsCreateFederateInfo()
    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1")
    h.helicsFederateInfoSetCoreInitString(fi, "--federates 1")

    h.helicsFederateInfoSetIntegerProperty(fi, h.HELICS_PROPERTY_INT_LOG_LEVEL, h.HELICS_LOG_LEVEL_TIMING)

    fed = h.helicsCreateValueFederate("test1", fi)

    userdata = UserData(5)

    handle = h.ffi.new_handle(userdata)
    h.helicsFederateSetLoggingCallback(fed, logger, handle)

    h.helicsFederateEnterExecutingMode(fed)
    h.helicsFederateLogInfoMessage(fed, "test MEXAGE")
    h.helicsFederateRequestNextStep(fed)
    h.helicsFederateLogInfoMessage(fed, "test MEXAGE")
    h.helicsFederateRequestNextStep(fed)
    h.helicsFederateLogInfoMessage(fed, "test MEXAGE")
    h.helicsFederateRequestNextStep(fed)
    h.helicsFederateLogInfoMessage(fed, "test MEXAGE")
    h.helicsFederateRequestNextStep(fed)

    h.helicsFederateDisconnect(fed)

    try:
        assert userdata.x == 19
    except:
        assert userdata.x == 9

    # h.helicsFederateFree(fed)
    # h.helicsFederateInfoFree(fi)

    h.helicsBrokerDisconnect(broker)
    # h.helicsBrokerFree(broker)

    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()


@pt.mark.skip()
def test_misc_api():
    fedInfo1 = h.helicsCreateFederateInfo()
    h.helicsFederateInfoSetCoreInitString(fedInfo1, "-f 1")
    h.helicsFederateInfoSetCoreName(fedInfo1, "core3")
    h.helicsFederateInfoSetCoreType(fedInfo1, 3)
    h.helicsFederateInfoSetCoreTypeFromString(fedInfo1, "zmq")
    h.helicsFederateInfoSetFlagOption(fedInfo1, 1, True)
    h.helicsFederateInfoSetTimeProperty(fedInfo1, h.HELICS_PROPERTY_TIME_INPUT_DELAY, 1.0)
    h.helicsFederateInfoSetIntegerProperty(fedInfo1, h.HELICS_PROPERTY_INT_LOG_LEVEL, 1)
    h.helicsFederateInfoSetIntegerProperty(fedInfo1, h.HELICS_PROPERTY_INT_MAX_ITERATIONS, 100)
    h.helicsFederateInfoSetTimeProperty(fedInfo1, h.HELICS_PROPERTY_TIME_OUTPUT_DELAY, 1.0)
    h.helicsFederateInfoSetTimeProperty(fedInfo1, h.HELICS_PROPERTY_TIME_PERIOD, 1.0)
    h.helicsFederateInfoSetTimeProperty(fedInfo1, h.HELICS_PROPERTY_TIME_DELTA, 1.0)
    h.helicsFederateInfoSetTimeProperty(fedInfo1, h.HELICS_PROPERTY_TIME_OFFSET, 0.1)
    # h.helicsFederateInfoFree(fedInfo1)

    broker3 = h.helicsCreateBroker("zmq", "broker3", "--federates 1")
    fedInfo2 = h.helicsCreateFederateInfo()
    coreInitString = "--federates 1"
    h.helicsFederateInfoSetCoreInitString(fedInfo2, coreInitString)
    h.helicsFederateInfoSetCoreTypeFromString(fedInfo2, "zmq")
    h.helicsFederateInfoSetIntegerProperty(fedInfo2, h.HELICS_PROPERTY_INT_LOG_LEVEL, h.HELICS_LOG_LEVEL_WARNING)
    h.helicsFederateInfoSetTimeProperty(fedInfo2, h.HELICS_PROPERTY_TIME_DELTA, 1.0)
    fed1 = h.helicsCreateCombinationFederate("fed1", fedInfo2)
    fed2 = h.helicsFederateClone(fed1)
    _ = h.helicsGetFederateByName("fed1")
    h.helicsFederateSetFlagOption(fed2, 1, False)

    h.helicsFederateSetTimeProperty(fed2, h.HELICS_PROPERTY_TIME_INPUT_DELAY, 1.0)
    h.helicsFederateSetIntegerProperty(fed1, h.HELICS_PROPERTY_INT_LOG_LEVEL, h.HELICS_LOG_LEVEL_WARNING)
    h.helicsFederateSetIntegerProperty(fed2, h.HELICS_PROPERTY_INT_MAX_ITERATIONS, 100)
    h.helicsFederateSetTimeProperty(fed2, h.HELICS_PROPERTY_TIME_OUTPUT_DELAY, 1.0)
    h.helicsFederateSetTimeProperty(fed2, h.HELICS_PROPERTY_TIME_PERIOD, 0.0)
    h.helicsFederateSetTimeProperty(fed2, h.HELICS_PROPERTY_TIME_DELTA, 1.0)

    _ = h.helicsFederateRegisterCloningFilter(fed1, "fed1/Ep1")
    fed1DestinationFilter = h.helicsFederateRegisterFilter(fed1, h.HELICS_FILTER_TYPE_DELAY, "fed1DestinationFilter")
    h.helicsFilterAddDestinationTarget(fed1DestinationFilter, "Ep2")

    ep1 = h.helicsFederateRegisterEndpoint(fed1, "Ep1", "string")
    ep2 = h.helicsFederateRegisterGlobalEndpoint(fed1, "Ep2", "string")
    pub1 = h.helicsFederateRegisterGlobalPublication(fed1, "pub1", h.HELICS_DATA_TYPE_DOUBLE, "")
    pub2 = h.helicsFederateRegisterGlobalTypePublication(fed1, "pub2", "complex", "")

    sub1 = h.helicsFederateRegisterSubscription(fed1, "pub1")
    sub2 = h.helicsFederateRegisterSubscription(fed1, "pub2")
    pub3 = h.helicsFederateRegisterPublication(fed1, "pub3", h.HELICS_DATA_TYPE_STRING, "")

    pub1KeyString = h.helicsPublicationGetKey(pub1)
    pub1TypeString = h.helicsPublicationGetType(pub1)
    pub1UnitsString = h.helicsPublicationGetUnits(pub1)
    sub1KeyString = h.helicsSubscriptionGetKey(sub1)
    sub1UnitsString = h.helicsInputGetUnits(sub1)
    assert "pub1" == pub1KeyString
    assert "double" == pub1TypeString
    assert "" == pub1UnitsString
    assert "pub1" == sub1KeyString
    assert "" == sub1UnitsString

    fed1SourceFilter = h.helicsFederateRegisterFilter(fed1, h.HELICS_FILTER_TYPE_DELAY, "fed1SourceFilter")
    h.helicsFilterAddSourceTarget(fed1SourceFilter, "Ep2")
    h.helicsFilterAddDestinationTarget(fed1SourceFilter, "fed1/Ep1")
    h.helicsFilterRemoveTarget(fed1SourceFilter, "fed1/Ep1")
    h.helicsFilterAddSourceTarget(fed1SourceFilter, "Ep2")
    h.helicsFilterRemoveTarget(fed1SourceFilter, "Ep2")

    fed1SourceFilterNameString = h.helicsFilterGetName(fed1SourceFilter)
    assert fed1SourceFilterNameString == "fed1/fed1SourceFilter"

    sub3 = h.helicsFederateRegisterSubscription(fed1, "fed1/pub3", "")
    pub4 = h.helicsFederateRegisterTypePublication(fed1, "pub4", "int", "")

    sub4 = h.helicsFederateRegisterSubscription(fed1, "fed1/pub4", "")
    pub5 = h.helicsFederateRegisterGlobalTypePublication(fed1, "pub5", "boolean", "")

    sub5 = h.helicsFederateRegisterSubscription(fed1, "pub5", "")
    pub6 = h.helicsFederateRegisterGlobalPublication(fed1, "pub6", h.HELICS_DATA_TYPE_VECTOR, "")
    sub6 = h.helicsFederateRegisterSubscription(fed1, "pub6", "")
    pub7 = h.helicsFederateRegisterGlobalPublication(fed1, "pub7", h.HELICS_DATA_TYPE_NAMED_POINT, "")
    sub7 = h.helicsFederateRegisterSubscription(fed1, "pub7", "")

    assert """helics.HelicsPublication(name = "pub1", type = "double", units = "", info = "")""" in repr(pub1)
    assert """helics.HelicsPublication(name = "pub2", type = "complex", units = "", info = "")""" in repr(pub2)
    assert """helics.HelicsPublication(name = "fed1/pub3", type = "string", units = "", info = "")""" in repr(pub3)
    assert """helics.HelicsPublication(name = "fed1/pub4", type = "int", units = "", info = "")""" in repr(pub4)
    assert """helics.HelicsPublication(name = "pub5", type = "boolean", units = "", info = "")""" in repr(pub5)
    assert """helics.HelicsPublication(name = "pub6", type = "double_vector", units = "", info = "")""" in repr(pub6)
    assert """helics.HelicsPublication(name = "pub7", type = "named_point", units = "", info = "")""" in repr(pub7)
    assert (
        """helics.HelicsInput(name = "_input_18", units = "", injection_units = "", publication_type = "", type = "", target = "pub7", info = "")"""
        in repr(sub7)
    )

    h.helicsInputSetDefaultBoolean(sub5, False)
    h.helicsInputSetDefaultComplex(sub2, -9.9 + 2.5j)
    h.helicsInputSetDefaultDouble(sub1, 3.4)
    h.helicsInputSetDefaultInteger(sub4, 6)
    h.helicsInputSetDefaultNamedPoint(sub7, "hollow", 20.0)
    h.helicsInputSetDefaultString(sub3, "default")
    sub6Default = [3.4, 90.9, 4.5]
    h.helicsInputSetDefaultVector(sub6, sub6Default)
    h.helicsEndpointSubscribe(ep2, "fed1/pub3")
    h.helicsFederateEnterInitializingModeAsync(fed1)
    rs = h.helicsFederateIsAsyncOperationCompleted(fed1)
    if rs == 0:
        time.sleep(0.500)
        rs = h.helicsFederateIsAsyncOperationCompleted(fed1)
        if rs == 0:
            time.sleep(0.500)
            rs = h.helicsFederateIsAsyncOperationCompleted(fed1)
            if rs == 0:
                assert True is False
    h.helicsFederateEnterInitializingModeComplete(fed1)
    h.helicsFederateEnterExecutingModeAsync(fed1)
    h.helicsFederateEnterExecutingModeComplete(fed1)

    assert (
        """helics.HelicsInput(name = "_input_18", units = "", injection_units = "", publication_type = "named_point", type = "", target = "pub7", info = "")"""
        in repr(sub7)
    )

    mesg1 = h.helicsFederateCreateMessage(fed1)
    h.helicsMessageSetString(mesg1, "Hello")
    h.helicsMessageSetSource(mesg1, "fed1/Ep1")
    h.helicsMessageSetOriginalSource(mesg1, "fed1/Ep1")
    h.helicsMessageSetDestination(mesg1, "Ep2")
    h.helicsMessageSetOriginalDestination(mesg1, "Ep2")

    h.helicsEndpointSendMessage(ep1, mesg1)
    mesg1 = h.helicsFederateCreateMessage(fed1)
    h.helicsMessageSetString(mesg1, "There")
    h.helicsMessageSetSource(mesg1, "fed1/Ep1")
    h.helicsMessageSetOriginalSource(mesg1, "fed1/Ep1")
    h.helicsMessageSetDestination(mesg1, "Ep2")
    h.helicsMessageSetOriginalDestination(mesg1, "Ep2")
    h.helicsEndpointSendMessage(ep1, mesg1)
    h.helicsEndpointSetDefaultDestination(ep2, "fed1/Ep1")

    ep1NameString = h.helicsEndpointGetName(ep1)
    ep1TypeString = h.helicsEndpointGetType(ep1)

    assert ep1NameString == "fed1/Ep1"
    assert ep1TypeString == "string"

    _ = h.helicsFederateGetCoreObject(fed1)

    fed1Time = h.helicsFederateGetCurrentTime(fed1)
    assert fed1Time == 0.0
    fed1EndpointCount = h.helicsFederateGetEndpointCount(fed1)
    assert fed1EndpointCount == 2

    fed1NameString = h.helicsFederateGetName(fed1)
    assert fed1NameString == "fed1"

    fed1State = h.helicsFederateGetState(fed1)
    assert fed1State == 2
    fed1PubCount = h.helicsFederateGetPublicationCount(fed1)
    assert fed1PubCount == 7
    fed1SubCount = h.helicsFederateGetInputCount(fed1)
    assert fed1SubCount == 7

    h.helicsPublicationPublishBoolean(pub5, True)
    h.helicsPublicationPublishComplex(pub2, 5.6 + -0.67j)
    h.helicsPublicationPublishDouble(pub1, 457.234)
    h.helicsPublicationPublishInteger(pub4, 1)
    h.helicsPublicationPublishNamedPoint(pub7, "Blah Blah", 20.0)
    h.helicsPublicationPublishString(pub3, "Mayhem")
    pub6Vector = [4.5, 56.5]
    h.helicsPublicationPublishVector(pub6, pub6Vector)
    time.sleep(0.500)
    h.helicsFederateRequestTimeAsync(fed1, 1.0)

    returnTime = h.helicsFederateRequestTimeComplete(fed1)
    assert returnTime == 1.0
    ep2MsgCount = h.helicsEndpointPendingMessages(ep2)
    assert ep2MsgCount == 0
    ep2HasMsg = h.helicsEndpointHasMessage(ep2)
    assert ep2HasMsg == 0

    ep2MsgCount = h.helicsEndpointPendingMessageCount(ep2)
    assert ep2MsgCount == 0

    returnTime = h.helicsFederateRequestTime(fed1, 3.0)
    assert returnTime == 3.0
    ep2MsgCount = h.helicsEndpointPendingMessageCount(ep2)
    try:
        assert ep2MsgCount == 2
    except:
        assert ep2MsgCount == 3

    msg2 = h.helicsEndpointGetMessage(ep2)
    assert h.helicsMessageGetTime(msg2) == 1.0
    assert h.helicsMessageGetString(msg2) == "Hello"
    assert h.helicsMessageGetOriginalSource(msg2) == "fed1/Ep1"
    assert h.helicsMessageGetSource(msg2) == "fed1/Ep1"
    assert h.helicsMessageGetDestination(msg2) == "Ep2"
    assert h.helicsMessageGetOriginalDestination(msg2) == "Ep2"

    fed1MsgCount = h.helicsFederatePendingMessages(fed1)
    assert fed1MsgCount == 1

    assert h.helicsFederateHasMessage(fed1) == 1

    msg3 = h.helicsFederateGetMessage(fed1)
    assert h.helicsMessageGetTime(msg3) == 1.0
    assert h.helicsMessageGetString(msg3) == "There"
    assert h.helicsMessageGetOriginalSource(msg3) == "fed1/Ep1"
    assert h.helicsMessageGetSource(msg3) == "fed1/Ep1"
    assert h.helicsMessageGetDestination(msg3) == "Ep2"
    assert h.helicsMessageGetOriginalDestination(msg3) == "Ep2"

    sub1Updated = h.helicsInputIsUpdated(sub1)
    assert sub1Updated is True

    assert h.helicsInputLastUpdateTime(sub2) == 3.0

    assert h.helicsInputGetComplex(sub2) == (5.6, -0.67)

    assert h.helicsInputGetDouble(sub1) == 457.234
    assert h.helicsInputGetInteger(sub4) == 1
    sub7PointString, sub7DoubleValue = h.helicsInputGetNamedPoint(sub7)
    assert sub7PointString == "Blah Blah"
    assert sub7DoubleValue == 20.0
    assert h.helicsInputGetBoolean(sub5) == True
    assert h.helicsInputGetString(sub3) == "Mayhem"

    # TODO: this test is failing in HELICS3
    # sub3ValueSize = h.helicsInputGetRawValueSize(sub3)
    # assert sub3ValueSize == 6

    assert h.helicsInputGetVector(sub6) == [4.5, 56.5]

    h.helicsFederateDisconnect(fed1)
    h.helicsFederateDisconnect(fed2)
    # h.helicsFederateFree(fed1)
    h.helicsFederateDisconnect(fed2)
    # h.helicsFederateFree(fed2)
    # h.helicsFederateInfoFree(fedInfo2)
    h.helicsBrokerDisconnect(broker3)

    # h.helicsBrokerFree(broker3)

    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()

# Exercise the Endpoint *Bytes* interfaces
def test_send_endpoint_bytes():
    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1")

    fedInfo = h.helicsCreateFederateInfo()
    coreInitString = "--federates 1"
    h.helicsFederateInfoSetCoreInitString(fedInfo, coreInitString)
    h.helicsFederateInfoSetCoreTypeFromString(fedInfo, "zmq")
    h.helicsFederateInfoSetIntegerProperty(fedInfo, h.HELICS_PROPERTY_INT_LOG_LEVEL, h.HELICS_LOG_LEVEL_WARNING)
    h.helicsFederateInfoSetTimeProperty(fedInfo, h.HELICS_PROPERTY_TIME_DELTA, 1.0)
    fed = h.helicsCreateMessageFederate("fed", fedInfo)

    ep1 = h.helicsFederateRegisterEndpoint(fed, "Ep1", "")
    ep2 = h.helicsFederateRegisterEndpoint(fed, "Ep2", "")

    h.helicsEndpointSetDefaultDestination(ep1, "fed/Ep2")

    h.helicsFederateEnterExecutingMode(fed)

    data1 = b'\0\0Hello,\0\0World!\0\0\0\0'
    data2 = bytes(x for x in range(256))
    data3 = b'\0' * 64

    msg = h.helicsFederateCreateMessage(fed)
    h.helicsMessageSetData(msg, data1)
    h.helicsEndpointSendMessage(ep1, msg)

    h.helicsEndpointSendBytesTo(ep1, data2, "fed/Ep2")

    h.helicsEndpointSendBytesToAt(ep1, data3, "fed/Ep2", 1.)

    h.helicsFederateRequestNextStep(fed)

    assert h.helicsEndpointPendingMessageCount(ep2) == 2
    assert h.helicsEndpointHasMessage(ep2)
    msg = h.helicsEndpointGetMessage(ep2)
    assert h.helicsMessageGetByteCount(msg) == len(data1)
    assert h.helicsMessageGetBytes(msg) == data1

    assert h.helicsEndpointPendingMessageCount(ep2) == 1
    assert h.helicsEndpointHasMessage(ep2)
    msg = h.helicsEndpointGetMessage(ep2)
    assert h.helicsMessageGetByteCount(msg) == len(data2)
    assert h.helicsMessageGetBytes(msg) == data2

    assert h.helicsEndpointPendingMessageCount(ep2) == 0
    assert not h.helicsEndpointHasMessage(ep2)

    h.helicsFederateRequestNextStep(fed)

    assert h.helicsEndpointPendingMessageCount(ep2) == 1
    assert h.helicsEndpointHasMessage(ep2)
    msg = h.helicsEndpointGetMessage(ep2)
    assert h.helicsMessageGetByteCount(msg) == len(data3)
    assert h.helicsMessageGetBytes(msg) == data3

    assert h.helicsEndpointPendingMessageCount(ep2) == 0
    assert not h.helicsEndpointHasMessage(ep2)

    h.helicsFederateDisconnect(fed)

    h.helicsBrokerDisconnect(broker)

    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()
