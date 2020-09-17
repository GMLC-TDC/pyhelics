# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import time
import helics as h
import os
import pytest as pt

from test_init import createBroker, createValueFederate, destroyFederate, destroyBroker, createMessageFederate


CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def test_valuefederate_creation():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()
    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_state():

    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    state = h.helicsFederateGetState(vFed)
    assert state == 0

    h.helicsFederateEnterExecutingMode(vFed)

    state = h.helicsFederateGetState(vFed)
    assert state == 2

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_publication_registration():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    pubid1 = h.helicsFederateRegisterTypePublication(vFed, "pub1", "string", "")
    pubid2 = h.helicsFederateRegisterGlobalTypePublication(vFed, "pub2", "int", "")
    pubid3 = h.helicsFederateRegisterTypePublication(vFed, "pub3", "double", "V")

    h.helicsFederateEnterExecutingMode(vFed)

    assert h.helicsPublicationGetKey(pubid1) == "TestA Federate/pub1"
    assert h.helicsPublicationGetKey(pubid2) == "pub2"

    assert h.helicsPublicationGetKey(pubid3) == "TestA Federate/pub3"
    assert h.helicsPublicationGetType(pubid3) == "double"
    assert h.helicsPublicationGetUnits(pubid3) == "V"

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_named_point():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    defaultValue = "start of a longer string in place of the shorter one and now this should be very long"
    defVal = 5.3
    # testValue1 = "inside of the functional relationship of helics"
    testValue1 = "short string"
    testVal1 = 45.7823
    testValue2 = "I am a string"
    testVal2 = 0.0

    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_NAMED_POINT, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")

    h.helicsInputSetDefaultNamedPoint(subid, defaultValue, defVal)

    h.helicsFederateEnterExecutingMode(vFed)

    # publish string1 at time=0.0
    h.helicsPublicationPublishNamedPoint(pubid, testValue1, testVal1)

    assert h.helicsInputGetNamedPoint(subid) == (defaultValue, defVal)

    assert h.helicsFederateRequestTime(vFed, 1.0) == 0.01

    # # get the value
    assert h.helicsInputGetNamedPoint(subid) == (testValue1, testVal1)

    # publish a second string
    h.helicsPublicationPublishNamedPoint(pubid, testValue2, testVal2)

    # # make sure the value is still what we expect
    assert h.helicsInputGetNamedPoint(subid) == (testValue1, testVal1)
    # # make sure the string is what we expect
    # # assert value3 == testValue1
    # assert val3 == [testValue1, testVal1]

    # # advance time
    assert h.helicsFederateRequestTime(vFed, 2.0) == 0.02

    # # make sure the value was updated
    assert h.helicsInputGetNamedPoint(subid) == (testValue2, testVal2)

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_bool():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    defaultValue = True
    testValue1 = True
    testValue2 = False

    # register the publications
    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_BOOLEAN, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")

    h.helicsInputSetDefaultBoolean(subid, defaultValue)

    h.helicsFederateEnterExecutingMode(vFed)

    # publish string1 at time=0.0
    h.helicsPublicationPublishBoolean(pubid, testValue1)
    val = h.helicsInputGetBoolean(subid)

    assert val == defaultValue

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    # get the value
    val = h.helicsInputGetBoolean(subid)

    # make sure the string is what we expect
    assert val == testValue1

    # publish a second string
    h.helicsPublicationPublishBoolean(pubid, testValue2)

    # make sure the value is still what we expect
    val = h.helicsInputGetBoolean(subid)
    assert val == testValue1
    # advance time
    grantedtime = h.helicsFederateRequestTime(vFed, 2.0)
    # make sure the value was updated
    assert grantedtime == 0.02

    val = h.helicsInputGetBoolean(subid)
    assert val == testValue2

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_publisher_registration():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    pubid1 = h.helicsFederateRegisterPublication(vFed, "pub1", h.HELICS_DATA_TYPE_STRING, "")
    pubid2 = h.helicsFederateRegisterGlobalPublication(vFed, "pub2", h.HELICS_DATA_TYPE_INT, "")
    pubid3 = h.helicsFederateRegisterPublication(vFed, "pub3", h.HELICS_DATA_TYPE_DOUBLE, "V")
    h.helicsFederateEnterExecutingMode(vFed)

    publication_key = h.helicsPublicationGetKey(pubid1)
    assert publication_key == "TestA Federate/pub1"
    publication_type = h.helicsPublicationGetType(pubid1)
    assert publication_type == "string"
    publication_key = h.helicsPublicationGetKey(pubid2)
    assert publication_key == "pub2"
    publication_key = h.helicsPublicationGetKey(pubid3)
    assert publication_key == "TestA Federate/pub3"
    publication_type = h.helicsPublicationGetType(pubid3)
    assert publication_type == "double"
    publication_units = h.helicsPublicationGetUnits(pubid3)
    assert publication_units == "V"
    publication_type = h.helicsPublicationGetType(pubid2)
    assert publication_type == "int64"

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_subscription_and_publication_registration():

    broker = createBroker()
    vFed, fedinfo = createValueFederate(1, "fed0")

    pubid = h.helicsFederateRegisterPublication(vFed, "pub1", h.HELICS_DATA_TYPE_STRING, "")
    pubid2 = h.helicsFederateRegisterGlobalPublication(vFed, "pub2", h.HELICS_DATA_TYPE_INT, "volts")
    pubid3 = h.helicsFederateRegisterTypePublication(vFed, "pub3", "double", "V")

    subid1 = h.helicsFederateRegisterSubscription(vFed, "sub1", "")
    subid2 = h.helicsFederateRegisterSubscription(vFed, "sub2", "")
    subid3 = h.helicsFederateRegisterSubscription(vFed, "sub3", "V")

    h.helicsFederateEnterExecutingMode(vFed)

    publication_type = h.helicsPublicationGetType(pubid3)
    assert publication_type == "double"

    sub_key = h.helicsSubscriptionGetKey(subid1)
    assert sub_key == "sub1"
    sub_type = h.helicsInputGetType(subid1)
    assert sub_type == ""
    sub_key = h.helicsSubscriptionGetKey(subid2)
    assert sub_key == "sub2"
    sub_key = h.helicsSubscriptionGetKey(subid3)
    assert sub_key == "sub3"
    sub_type = h.helicsInputGetType(subid3)
    assert sub_type == ""
    sub_units = h.helicsInputGetUnits(subid3)
    assert sub_units == "V"
    sub_type = h.helicsInputGetType(subid2)
    assert sub_type == ""

    subid_b = h.helicsFederateGetSubscription(vFed, "sub1")
    tmp = h.helicsSubscriptionGetKey(subid_b)
    assert tmp == "sub1"
    # check the getSubscriptionByIndex function
    subid_c = h.helicsFederateGetInputByIndex(vFed, 2)
    tmp = h.helicsInputGetUnits(subid_c)
    assert tmp == "V"
    # check publications

    sv = h.helicsPublicationGetKey(pubid)
    sv2 = h.helicsPublicationGetKey(pubid2)
    assert sv == "Testfed0/pub1"
    assert sv2 == "pub2"
    pub3name = h.helicsPublicationGetKey(pubid3)
    assert pub3name == "Testfed0/pub3"

    type = h.helicsPublicationGetType(pubid3)
    assert type == "double"
    units = h.helicsPublicationGetUnits(pubid3)
    assert units == "V"

    # check the getSubscription function

    pubid_b = h.helicsFederateGetPublication(vFed, "Testfed0/pub1")
    tmp = h.helicsPublicationGetType(pubid_b)
    assert tmp == "string"
    # check the getSubscriptionByIndex function
    pubid_c = h.helicsFederateGetPublicationByIndex(vFed, 1)
    tmp = h.helicsPublicationGetUnits(pubid_c)
    assert tmp == "volts"

    # this one should be invalid
    # @test_throws h.HELICSErrorInvalidArgument pubid_d = h.helicsFederateGetPublicationByIndex(vFed, 5)

    h.helicsFederateFinalize(vFed)

    state = h.helicsFederateGetState(vFed)
    assert state == h.HELICS_STATE_FINALIZE

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_single_transfer():

    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_STRING, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")

    h.helicsFederateEnterExecutingMode(vFed)

    h.helicsPublicationPublishString(pubid, "string1")

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    s = h.helicsInputGetString(subid)
    assert s == "string1"

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_double():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    defaultValue = 1.0
    testValue = 2.0
    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_DOUBLE, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")
    h.helicsInputSetDefaultDouble(subid, defaultValue)

    h.helicsFederateEnterExecutingMode(vFed)

    # publish string1 at time=0.0
    h.helicsPublicationPublishDouble(pubid, testValue)

    value = h.helicsInputGetDouble(subid)
    assert value == defaultValue

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    value = h.helicsInputGetDouble(subid)
    assert value == testValue

    # publish string1 at time=0.0
    h.helicsPublicationPublishDouble(pubid, testValue + 1)

    grantedtime = h.helicsFederateRequestTime(vFed, 2.0)
    assert grantedtime == 0.02

    value = h.helicsInputGetDouble(subid)
    assert value == testValue + 1

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_complex():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    rDefaultValue = 1.0
    iDefaultValue = 1.0
    rTestValue = 2.0
    iTestValue = 2.0
    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_COMPLEX, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")
    h.helicsInputSetDefaultComplex(subid, complex(rDefaultValue, iDefaultValue))

    h.helicsFederateEnterExecutingMode(vFed)

    # publish string1 at time=0.0
    h.helicsPublicationPublishComplex(pubid, complex(rTestValue, iTestValue))

    assert (rDefaultValue, iDefaultValue) == h.helicsInputGetComplex(subid)

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    assert (rTestValue, iTestValue) == h.helicsInputGetComplex(subid)

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_integer():

    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    defaultValue = 1
    testValue = 2
    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_INT, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")
    h.helicsInputSetDefaultInteger(subid, defaultValue)

    h.helicsFederateEnterExecutingMode(vFed)

    h.helicsPublicationPublishInteger(pubid, testValue)

    value = h.helicsInputGetInteger(subid)
    assert value == defaultValue

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    value = h.helicsInputGetInteger(subid)
    assert value == testValue

    h.helicsPublicationPublishInteger(pubid, testValue + 1)

    grantedtime = h.helicsFederateRequestTime(vFed, 2.0)
    assert grantedtime == 0.02

    value = h.helicsInputGetInteger(subid)
    assert value == testValue + 1

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_string():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    defaultValue = "String1"
    testValue = "String2"
    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_STRING, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")
    h.helicsInputSetDefaultString(subid, defaultValue)

    h.helicsFederateEnterExecutingMode(vFed)

    h.helicsPublicationPublishString(pubid, testValue)

    value = h.helicsInputGetString(subid)
    assert value == defaultValue

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    value = h.helicsInputGetString(subid)
    assert value == testValue

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_vectord():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    defaultValue = [0.0, 1.0, 2.0]
    testValue = [3.0, 4.0, 5.0]
    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_VECTOR, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")
    h.helicsInputSetDefaultVector(subid, defaultValue)

    h.helicsFederateEnterExecutingMode(vFed)

    h.helicsPublicationPublishVector(pubid, testValue)

    assert h.helicsInputGetVector(subid) == defaultValue

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    value = h.helicsInputGetVector(subid)

    assert value == testValue

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_single_transfer():
    broker = createBroker()
    vFed, fedinfo = createValueFederate()

    s = "n2"

    pubid = h.helicsFederateRegisterGlobalPublication(vFed, "pub1", h.HELICS_DATA_TYPE_STRING, "")
    subid = h.helicsFederateRegisterSubscription(vFed, "pub1", "")

    h.helicsFederateEnterExecutingMode(vFed)

    h.helicsPublicationPublishString(pubid, "string1")

    grantedtime = h.helicsFederateRequestTime(vFed, 1.0)
    assert grantedtime == 0.01

    s = h.helicsInputGetString(subid)

    assert s == "string1"

    t = h.helicsInputLastUpdateTime(subid)
    assert t == 0.01

    h.helicsPublicationPublishString(pubid, "string2")

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_default_value_tests():
    broker = createBroker()
    vFed1, fedinfo = createValueFederate(1, "fed0")

    inp_raw1 = h.helicsFederateRegisterInput(vFed1, "key1", h.HELICS_DATA_TYPE_RAW, "raw")
    inp_raw2 = h.helicsFederateRegisterInput(vFed1, "key2", h.HELICS_DATA_TYPE_RAW, "raw")

    inp_bool = h.helicsFederateRegisterInput(vFed1, "key3", h.HELICS_DATA_TYPE_BOOLEAN, "")

    inp_time = h.helicsFederateRegisterInput(vFed1, "key4", h.HELICS_DATA_TYPE_TIME, "")

    inp_char = h.helicsFederateRegisterInput(vFed1, "key5", h.HELICS_DATA_TYPE_STRING, "")

    inp_vect = h.helicsFederateRegisterInput(vFed1, "key6", h.HELICS_DATA_TYPE_VECTOR, "V")

    inp_double = h.helicsFederateRegisterInput(vFed1, "key7", h.HELICS_DATA_TYPE_DOUBLE, "kW")

    inp_double2 = h.helicsFederateRegisterInput(vFed1, "key8", h.HELICS_DATA_TYPE_DOUBLE, "")

    inp_np = h.helicsFederateRegisterInput(vFed1, "key9", h.HELICS_DATA_TYPE_NAMED_POINT, "")

    h.helicsInputSetMinimumChange(inp_double, 1100.0)
    h.helicsInputSetDefaultDouble(inp_double, 10000.0)

    h.helicsInputSetOption(inp_double2, h.HELICS_HANDLE_OPTION_CONNECTION_REQUIRED, True)

    pub = h.helicsFederateRegisterPublication(vFed1, "", h.HELICS_DATA_TYPE_INT, "MW")
    h.helicsPublicationSetOption(pub, h.HELICS_HANDLE_OPTION_CONNECTION_REQUIRED, True)
    h.helicsPublicationAddTarget(pub, "Testfed0/key7")
    h.helicsPublicationAddTarget(pub, "Testfed0/key8")

    h.helicsInputSetDefaultRaw(inp_raw1, "")
    data = "this is a string"
    h.helicsInputSetDefaultRaw(inp_raw2, data)

    h.helicsInputSetDefaultBoolean(inp_bool, True)

    h.helicsInputSetDefaultTime(inp_time, 12.3)
    h.helicsInputSetDefaultChar(inp_char, "q")
    h.helicsInputSetDefaultVector(inp_vect, [])
    h.helicsInputSetDefaultNamedPoint(inp_np, data, 15.7)

    h.helicsFederateEnterExecutingMode(vFed1)
    assert h.helicsInputGetInjectionUnits(inp_double) == "MW"
    assert h.helicsInputGetInjectionUnits(inp_double2) == "MW"
    assert h.helicsInputGetType(inp_double) == "double"
    assert h.helicsInputGetPublicationType(inp_double) == "int64"

    c2 = h.helicsInputGetChar(inp_char)
    assert c2 == "q"
    h.helicsInputGetVector(inp_vect)

    optset = h.helicsInputGetOption(inp_double2, h.HELICS_HANDLE_OPTION_CONNECTION_REQUIRED)
    assert optset == 1

    optset = h.helicsPublicationGetOption(pub, h.HELICS_HANDLE_OPTION_CONNECTION_REQUIRED)
    assert optset == 1
    h.helicsPublicationPublishInteger(pub, 12)

    h.helicsFederateRequestNextStep(vFed1)
    assert h.helicsInputGetDouble(inp_double) == 12000.0
    assert h.helicsInputGetDouble(inp_double2) == 12.0

    h.helicsPublicationPublishInteger(pub, 13)

    h.helicsFederateRequestNextStep(vFed1)
    assert h.helicsInputIsUpdated(inp_double) is False
    assert h.helicsInputIsUpdated(inp_double2) is True

    assert h.helicsInputGetDouble(inp_double) == 12000.0
    assert h.helicsInputGetDouble(inp_double2) == 13.0

    h.helicsPublicationPublishInteger(pub, 15)

    h.helicsFederateRequestNextStep(vFed1)

    assert h.helicsInputIsUpdated(inp_double) is True
    assert h.helicsInputIsUpdated(inp_double2) is True

    h.helicsInputClearUpdate(inp_double)
    h.helicsInputClearUpdate(inp_double2)

    assert h.helicsInputIsUpdated(inp_double) is False
    assert h.helicsInputIsUpdated(inp_double2) is False

    _, rval = h.helicsInputGetNamedPoint(inp_np)
    assert rval == 15.7

    out, rval = h.helicsInputGetNamedPoint(inp_np)
    assert out == "this is a string"
    assert rval == 15.7

    h.helicsFederateFinalize(vFed1)

    destroyFederate(vFed1, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_info_filed():

    broker = createBroker()
    vFed, fedinfo = createValueFederate(1, "fed0")

    h.helicsFederateSetFlagOption(vFed, h.HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL, True)
    # register the publications/subscriptions

    subid1 = h.helicsFederateRegisterSubscription(vFed, "sub1", "")
    pubid1 = h.helicsFederateRegisterTypePublication(vFed, "pub1", "string", "")
    pubid2 = h.helicsFederateRegisterGlobalTypePublication(vFed, "pub2", "string", "")

    # Set info fields
    h.helicsInputSetInfo(subid1, "sub1_test")
    h.helicsPublicationSetInfo(pubid1, "pub1_test")
    h.helicsPublicationSetInfo(pubid2, "pub2_test")
    h.helicsFederateEnterExecutingMode(vFed)

    assert h.helicsInputGetInfo(subid1) == "sub1_test"
    assert h.helicsPublicationGetInfo(pubid1) == "pub1_test"
    assert h.helicsPublicationGetInfo(pubid2) == "pub2_test"

    cr = h.helicsFederateGetCoreObject(vFed)
    h.helicsFederateFinalize(vFed)

    wait = h.helicsCoreWaitForDisconnect(cr, 70)
    if wait is False:
        wait = h.helicsCoreWaitForDisconnect(cr, 500)
    assert wait is True

    destroyFederate(vFed, fedinfo)
    destroyBroker(broker)


def test_valuefederate_test_file_load():

    filename = os.path.join(CURRENT_DIRECTORY, "valuefederate.json")
    vFed = h.helicsCreateValueFederateFromConfig(filename)

    name = h.helicsFederateGetName(vFed)
    assert name == "valueFed"

    assert h.helicsFederateGetInputCount(vFed) == 3
    assert h.helicsFederateGetPublicationCount(vFed) == 2

    h.helicsFederateFinalize(vFed)
    h.helicsFederateFree(vFed)
    h.helicsCloseLibrary()
