# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import pytest as pt
import helics as h
import time


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


def test_python_api1():

    broker = h.helicsCreateBroker("zmq", "", "-f 1 --name=mainbroker")
    fedinfo = h.helicsCreateFederateInfo()
    fedinfo.core_name = "TestFilter"
    fedinfo.core_type = "zmq"
    fedinfo.core_init = "-f 1 --broker=mainbroker"
    mFed = h.helicsCreateCombinationFederate("TestFilter", fedinfo)

    assert (
        """HelicsCombinationFederate(name = "TestFilter", state = HelicsFederateState.STARTUP, current_time = -9223372036.854776, n_publications = 0, n_inputs = 0, n_endpoints = 0, n_filters = 0, n_pending_messages = 0)"""
        in repr(mFed)
    )

    _ = mFed.register_endpoint("ep1")
    _ = mFed.register_global_endpoint("ep2")

    mFed.property[h.HELICS_PROPERTY_TIME_DELTA] = 1.0
    assert mFed.property[h.HELICS_PROPERTY_TIME_DELTA] == 1.0

    mFed.enter_executing_mode()

    data = "random-data"

    mFed.endpoints["TestFilter/ep1"].send_data(data, "ep2", 1.0)

    assert mFed.request_time(2.0) == 1.0

    assert mFed.has_message()

    assert mFed.endpoints["TestFilter/ep1"].has_message() is False

    assert mFed.endpoints["ep2"].has_message()

    message = mFed.endpoints["ep2"].message

    assert message.message_id == 55
    assert message.is_valid() is True
    assert message.data == "random-data"
    assert message.raw_data == b"random-data"
    assert len(message.raw_data) == 11
    assert message.original_destination == ""
    assert message.original_source == "TestFilter/ep1"
    assert message.source == "TestFilter/ep1"
    assert message.time == 1.0

    assert (
        """<{ 1 = False, 2 = False, 3 = False, 4 = False, 5 = False, 6 = False, 7 = False, 8 = False, 9 = False, 10 = False, 11 = False, 12 = False, 13 = False, 14 = False, 15 = False }>"""
        in repr(message.flag)
    )
    message.flag[1] = True
    assert message.flag[1] is True

    mFed.finalize()

    del mFed
    del broker


def test_python_api2():

    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1 --loglevel 1")
    assert broker.is_connected()

    broker.set_global("hello", "world")

    broker.data_link("hello", "world")
    broker.add_destination_filter_to_endpoint("hello", "world")
    broker.add_source_filter_to_endpoint("hello", "world")
    assert broker.query("hello", "world") == "#invalid"

    fi = h.helicsCreateFederateInfo()
    fi.core_init = "--federates 1"
    fi.set_property(h.HELICS_PROPERTY_INT_LOG_LEVEL, 2)

    fed = h.helicsCreateCombinationFederate("test1", fi)

    assert "HelicsCore" in repr(fed.core)
    assert 'address = "tcp://127.0.0.1' in repr(fed.core)

    assert fed.core.is_connected()
    fed.core.set_ready_to_init()

    assert "n_publications = 0" in repr(fed)
    assert "n_inputs = 0" in repr(fed)
    assert "n_endpoints = 0" in repr(fed)
    assert "n_filters = 0" in repr(fed)

    assert fed.property["DELTA"] == 1e-09
    assert fed.property["PERIOD"] == 0.0
    assert fed.property["OFFSET"] == 0.0
    assert fed.property["RT_LAG"] == 0.0
    assert fed.property["RT_LEAD"] == 0.0
    assert fed.property["RT_TOLERANCE"] == 0.0
    assert fed.property["INPUT_DELAY"] == 0.0
    assert fed.property["OUTPUT_DELAY"] == 0.0
    assert fed.property["MAX_ITERATIONS"] == 50
    assert fed.property["LOG_LEVEL"] == 2
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

    assert "'TIME_DELTA' = 1e-09" in repr(fed.property)
    assert "'TIME_PERIOD' = 0.0" in repr(fed.property)
    assert "'TIME_OFFSET' = 0.0" in repr(fed.property)
    assert "'TIME_RT_LAG' = 0.0" in repr(fed.property)
    assert "'TIME_RT_LEAD' = 0.0" in repr(fed.property)
    assert "'TIME_RT_TOLERANCE' = 0.0" in repr(fed.property)
    assert "'TIME_INPUT_DELAY' = 0.0" in repr(fed.property)
    assert "'TIME_OUTPUT_DELAY' = 0.0" in repr(fed.property)
    assert "'INT_MAX_ITERATIONS' = 50" in repr(fed.property)
    assert "'INT_LOG_LEVEL' = 5" in repr(fed.property)
    assert "'INT_FILE_LOG_LEVEL' = 5" in repr(fed.property)
    assert "'INT_CONSOLE_LOG_LEVEL' = 5" in repr(fed.property)

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

    assert fed.flag[h.HELICS_FLAG_OBSERVER.value] is False
    assert fed.flag[h.HELICS_FLAG_UNINTERRUPTIBLE.value] is False
    assert fed.flag[h.HELICS_FLAG_INTERRUPTIBLE.value] is True
    assert fed.flag[h.HELICS_FLAG_SOURCE_ONLY.value] is False
    assert fed.flag[h.HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE.value] is False
    assert fed.flag[h.HELICS_FLAG_ONLY_UPDATE_ON_CHANGE.value] is False
    assert fed.flag[h.HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE.value] is False
    assert fed.flag[h.HELICS_FLAG_RESTRICTIVE_TIME_POLICY.value] is False
    assert fed.flag[h.HELICS_FLAG_REALTIME.value] is False
    assert fed.flag[h.HELICS_FLAG_SLOW_RESPONDING.value] is False
    assert fed.flag[h.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS.value] is False
    assert fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR.value] is False

    assert "'OBSERVER' = False" in repr(fed.flag)
    assert "'UNINTERRUPTIBLE' = False" in repr(fed.flag)
    assert "'INTERRUPTIBLE' = True" in repr(fed.flag)
    assert "'SOURCE_ONLY' = False" in repr(fed.flag)
    assert "'ONLY_TRANSMIT_ON_CHANGE' = False" in repr(fed.flag)
    assert "'ONLY_UPDATE_ON_CHANGE' = False" in repr(fed.flag)
    assert "'WAIT_FOR_CURRENT_TIME_UPDATE' = False" in repr(fed.flag)
    assert "'RESTRICTIVE_TIME_POLICY' = False" in repr(fed.flag)
    assert "'REALTIME' = False" in repr(fed.flag)
    assert "'SLOW_RESPONDING' = False," in repr(fed.flag)
    assert "'IGNORE_TIME_MISMATCH_WARNINGS' = False," in repr(fed.flag)
    assert "'TERMINATE_ON_ERROR' = False" in repr(fed.flag)

    fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] = True

    assert fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] is True

    fed.core.register_filter(h.HelicsFilterType.DELAY, "")
    fed.core.register_cloning_filter("")

    fed.register_filter(h.HelicsFilterType.DELAY, "")
    fed.register_cloning_filter("")

    fed.core.set_global("hello", "world")

    assert fed.core.query("broker", "something") == "#invalid"

    fed.core.disconnect()

    assert fed.core.wait_for_disconnect()

    del fed

    broker.disconnect()
    assert broker.wait_for_disconnect()

    del broker

    h.helicsCleanupLibrary()
    h.helicsCloseLibrary()


def test_python_api3():
    core1 = h.helicsCreateCore("inproc", "core1", "--autobroker")

    assert """HelicsCore(identifier = "core1", address = "core1")""" in repr(core1)

    core2 = core1.clone()

    assert core1.identifier == "core1"

    source_filter1 = core1.register_filter(h.HELICS_FILTER_TYPE_DELAY, "core1SourceFilter")

    source_filter1.add_source_target("ep1")

    assert (
        """<{ 'CONNECTION_REQUIRED' = 0, 'CONNECTION_OPTIONAL' = 0, 'SINGLE_CONNECTION_ONLY' = 0, 'MULTIPLE_CONNECTIONS_ALLOWED' = 0, 'BUFFER_DATA' = 0, 'STRICT_TYPE_CHECKING' = 0, 'IGNORE_UNIT_MISMATCH' = 0, 'ONLY_TRANSMIT_ON_CHANGE' = 0, 'ONLY_UPDATE_ON_CHANGE' = 0, 'IGNORE_INTERRUPTS' = 0, 'MULTI_INPUT_HANDLING_METHOD' = 0, 'INPUT_PRIORITY_LOCATION' = 0, 'CLEAR_PRIORITY_LIST' = 0, 'CONNECTIONS' = 0 }>"""
        in repr(source_filter1.option)
    )

    source_filter1.option["CONNECTION_REQUIRED"] = 1
    assert source_filter1.option["CONNECTION_REQUIRED"] == 1

    source_filter1.add_source_target("hello")
    source_filter1.add_destination_target("world")
    source_filter1.remove_destination_target("world")

    source_filter1.info = "hello world"
    assert source_filter1.info == "hello world"

    source_filter1.set("hello", 1)

    destination_filter1 = core1.register_filter(h.HELICS_FILTER_TYPE_DELAY, "core1DestinationFilter")

    destination_filter1.add_destination_target("ep2")
    cloning_filter1 = core1.register_cloning_filter("ep3")

    cloning_filter1.remove_delivery_endpoint("ep3")

    assert core1.is_connected()
    core1.set_ready_to_init()

    core1.disconnect()
    core2.disconnect()

    del core1
    del core2

    h.helicsCloseLibrary()
