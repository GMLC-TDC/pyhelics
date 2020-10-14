# -*- coding: utf-8 -*-
import os
import sys

CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(CURRENT_DIRECTORY)
sys.path.append(os.path.dirname(CURRENT_DIRECTORY))

import pytest as pt
import helics as h


def test_python_api1():
    broker = h.helicsCreateBroker("zmq", "", "-f2")
    fedinfo = h.helicsCreateFederateInfo()
    fedinfo.core_name = "TestFilter"
    fFed = h.helicsCreateMessageFederate("TestFilter", fedinfo)
    fedinfo = h.helicsCreateFederateInfo()
    fedinfo.core_name = "TestMessage"
    mFed = h.helicsCreateMessageFederate("TestMessage", fedinfo)

    p1 = mFed.register_global_endpoint("port1")
    p2 = mFed.register_global_endpoint("port2", "random")

    assert """HelicsEndpoint(name = "port1", type = "", info = "", is_valid = True, default_destination = "", n_pending_messages = 0)""" in repr(p1)
    assert (
        """HelicsEndpoint(name = "port2", type = "random", info = "", is_valid = True, default_destination = "", n_pending_messages = 0)"""
        in repr(p2)
    )

    f1 = fFed.register_global_filter(h.HELICS_FILTER_TYPE_CUSTOM, "filter1")
    f1.add_source_target("port1")
    assert """HelicsFilter(name = "filter1", info = "")""" in repr(f1)

    f2 = fFed.register_global_filter(h.HELICS_FILTER_TYPE_DELAY, "filter2")
    f2.add_source_target("port1")
    assert """HelicsFilter(name = "filter2", info = "")""" in repr(f2)

    ep1 = fFed.register_endpoint("fout")
    assert (
        """HelicsEndpoint(name = "TestFilter/fout", type = "", info = "", is_valid = True, default_destination = "", n_pending_messages = 0)"""
        in repr(ep1)
    )

    f3 = fFed.register_filter(h.HELICS_FILTER_TYPE_RANDOM_DELAY, "filter3")
    f3.add_source_target("TestFilter/fout")

    f2.set("delay", 2.5)
    assert f2.option["CONNECTION_REQUIRED"] == 0
    assert f2.option["CONNECTION_OPTIONAL"] == 0
    assert f2.option["SINGLE_CONNECTION_ONLY"] == 0
    assert f2.option["MULTIPLE_CONNECTIONS_ALLOWED"] == 0
    assert f2.option["BUFFER_DATA"] == 0
    assert f2.option["STRICT_TYPE_CHECKING"] == 0
    assert f2.option["IGNORE_UNIT_MISMATCH"] == 0
    assert f2.option["ONLY_TRANSMIT_ON_CHANGE"] == 0
    assert f2.option["ONLY_UPDATE_ON_CHANGE"] == 0
    assert f2.option["IGNORE_INTERRUPTS"] == 0
    assert f2.option["MULTI_INPUT_HANDLING_METHOD"] == 0
    assert f2.option["INPUT_PRIORITY_LOCATION"] == 0
    assert f2.option["CLEAR_PRIORITY_LIST"] == 0
    assert f2.option["CONNECTIONS"] == 0

    f2.option["CONNECTION_REQUIRED"] = 1

    assert f2.option["CONNECTION_REQUIRED"] == 1

    fFed.enter_executing_mode_async()
    mFed.enter_executing_mode()
    fFed.enter_executing_mode_complete()

    assert fFed.state == 2
    assert fFed.state == h.HelicsFederateState.EXECUTION
    data = "hello world"

    filt_key = h.helicsFilterGetName(f1)
    assert filt_key == "filter1"

    filt_key = h.helicsFilterGetName(f2)
    assert filt_key == "filter2"

    h.helicsEndpointSendMessageRaw(p1, "port2", data.encode())
    h.helicsFederateRequestTimeAsync(mFed, 1.0)
    grantedtime = h.helicsFederateRequestTime(fFed, 1.0)
    assert grantedtime == 1.0
    grantedtime = h.helicsFederateRequestTimeComplete(mFed)
    assert grantedtime == 1.0
    res = h.helicsFederateHasMessage(mFed)
    assert res == 0
    res = h.helicsEndpointHasMessage(p2)
    assert res == 0
    # grantedtime = h.helicsFederateRequestTime(fFed, 3.0)
    # assert res==h.helics_true

    h.helicsFederateFinalize(mFed)
    h.helicsFederateFinalize(fFed)
    # f2 = h.helicsFederateRegisterDestinationFilter(fFed, h.helics_custom_filter, "filter2", "port2")
    # ep1 = h.helicsFederateRegisterEndpoint(fFed, "fout", "")
    # f3 = h.helicsFederateRegisterSourceFilter(fFed, h.helics_custom_filter, "", "filter0/fout")

    del fFed
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
