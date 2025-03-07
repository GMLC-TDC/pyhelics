# -*- coding: utf-8 -*-
import os
import pytest as pt
import helics as h
import logging

from .utils import assert_attributes

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


DEFAULT_SUB_OPTION_SETTINGS = {
    h.HelicsHandleOption.CONNECTION_REQUIRED: 0,
    h.HelicsHandleOption.CONNECTION_OPTIONAL: 0,
    h.HelicsHandleOption.SINGLE_CONNECTION_ONLY: 0,
    h.HelicsHandleOption.MULTIPLE_CONNECTIONS_ALLOWED: 1,
    h.HelicsHandleOption.BUFFER_DATA: 0,
    h.HelicsHandleOption.RECONNECTABLE: 0,
    h.HelicsHandleOption.STRICT_TYPE_CHECKING: 0,
    h.HelicsHandleOption.RECEIVE_ONLY: 0,
    h.HelicsHandleOption.SOURCE_ONLY: 0,
    h.HelicsHandleOption.IGNORE_UNIT_MISMATCH: 0,
    h.HelicsHandleOption.ONLY_TRANSMIT_ON_CHANGE: 0,
    h.HelicsHandleOption.ONLY_UPDATE_ON_CHANGE: 0,
    h.HelicsHandleOption.IGNORE_INTERRUPTS: 0,
    h.HelicsHandleOption.MULTI_INPUT_HANDLING_METHOD: 0,
    h.HelicsHandleOption.INPUT_PRIORITY_LOCATION: -1,
    h.HelicsHandleOption.CLEAR_PRIORITY_LIST: 1,
    h.HelicsHandleOption.CONNECTIONS: 0,
}

DEFAULT_PUB_OPTION_SETTINGS = {
    h.HelicsHandleOption.CONNECTION_REQUIRED: 0,
    h.HelicsHandleOption.CONNECTION_OPTIONAL: 0,
    h.HelicsHandleOption.SINGLE_CONNECTION_ONLY: 0,
    h.HelicsHandleOption.MULTIPLE_CONNECTIONS_ALLOWED: 1,
    h.HelicsHandleOption.BUFFER_DATA: 0,
    h.HelicsHandleOption.RECONNECTABLE: 0,
    h.HelicsHandleOption.STRICT_TYPE_CHECKING: 0,
    h.HelicsHandleOption.RECEIVE_ONLY: 0,
    h.HelicsHandleOption.SOURCE_ONLY: 0,
    h.HelicsHandleOption.IGNORE_UNIT_MISMATCH: 0,
    h.HelicsHandleOption.ONLY_TRANSMIT_ON_CHANGE: 0,
    h.HelicsHandleOption.ONLY_UPDATE_ON_CHANGE: 0,
    h.HelicsHandleOption.IGNORE_INTERRUPTS: 0,
    h.HelicsHandleOption.MULTI_INPUT_HANDLING_METHOD: 0,
    h.HelicsHandleOption.INPUT_PRIORITY_LOCATION: 0,
    h.HelicsHandleOption.CLEAR_PRIORITY_LIST: 0,
    h.HelicsHandleOption.CONNECTIONS: 0,
}


def assert_entries(dict_like, expected: dict):
    for key, value in expected.items():
        assert dict_like[key] == value, f"{repr(dict_like)}.{repr(key)} is not {value}"


def test_python_api0():
    broker = h.helicsCreateBroker("zmq", "", "-f 1 --name=mainbroker0")
    fedinfo = h.helicsCreateFederateInfo()
    assert isinstance(fedinfo, h.HelicsFederateInfo)
    fedinfo.core_name = "TestFederate"
    fedinfo.core_type = "zmq"
    fedinfo.core_init = "-f 1 --broker=mainbroker0 --name=core0"
    mFed = h.helicsCreateCombinationFederate("TestFederate", fedinfo)

    assert_attributes(
        mFed,
        {
            "name": "TestFederate",
            "state": h.HelicsFederateState.STARTUP,
            "current_time": -9223372036.854776,
            "n_publications": 0,
            "n_subscriptions": 0,
            "n_endpoints": 0,
            "n_filters": 0,
            "n_pending_messages": 0,
        },
    )

    _ = mFed.register_endpoint("ep1")
    _ = mFed.register_global_endpoint("ep2")

    pub = mFed.register_publication(
        "publication", h.HELICS_DATA_TYPE_STRING, "custom-units"
    )
    assert_attributes(
        pub,
        {
            "name": "TestFederate/publication",
            "type": "string",
            "units": "custom-units",
            "info": "",
        },
    )

    sub = mFed.register_subscription("TestFederate/publication", "custom-units")
    assert_attributes(
        sub,
        {
            "name": "_input_3",
            "units": "custom-units",
            "injection_units": "",
            "publication_type": "",
            "type": "",
            "target": "TestFederate/publication",
            "info": "",
        },
    )
    assert_entries(sub.option, DEFAULT_SUB_OPTION_SETTINGS)
    sub.option["CONNECTION_REQUIRED"] = 1
    sub.option[h.HELICS_HANDLE_OPTION_CONNECTION_REQUIRED] = 1
    assert sub.option["CONNECTION_REQUIRED"] == 1

    mFed.property[h.HELICS_PROPERTY_TIME_DELTA] = 1.0
    assert mFed.property[h.HELICS_PROPERTY_TIME_DELTA] == 1.0

    mFed.property["TIME_DELTA"] = 1.0
    assert mFed.property["TIME_DELTA"] == 1.0

    mFed.enter_executing_mode()


def test_python_api1():
    broker = h.helicsCreateBroker("zmq", "", "-f 1 --name=mainbroker1")
    fedinfo = h.helicsCreateFederateInfo()
    assert isinstance(fedinfo, h.HelicsFederateInfo)
    fedinfo.core_name = "TestFederate"
    fedinfo.core_type = "zmq"
    fedinfo.core_init = "-f 1 --broker=mainbroker1  --name=core0"
    mFed = h.helicsCreateCombinationFederate("TestFederate", fedinfo)

    assert_attributes(
        mFed,
        {
            "name": "TestFederate",
            "state": h.HelicsFederateState.STARTUP,
            "current_time": -9223372036.854776,
            "n_publications": 0,
            "n_subscriptions": 0,
            "n_endpoints": 0,
            "n_filters": 0,
            "n_pending_messages": 0,
        },
    )

    _ = mFed.register_endpoint("ep1")
    _ = mFed.register_global_endpoint("ep2")

    pub = mFed.register_publication(
        "publication", h.HELICS_DATA_TYPE_STRING, "custom-units"
    )
    assert_attributes(
        pub,
        {
            "name": "TestFederate/publication",
            "type": "string",
            "units": "custom-units",
            "info": "",
        },
    )

    sub = mFed.register_subscription("TestFederate/publication", "custom-units")
    assert_attributes(
        sub,
        {
            "name": "_input_3",
            "units": "custom-units",
            "injection_units": "",
            "publication_type": "",
            "type": "",
            "target": "TestFederate/publication",
            "info": "",
        },
    )

    assert_entries(sub.option, DEFAULT_SUB_OPTION_SETTINGS)
    sub.option["CONNECTION_REQUIRED"] = 1
    assert sub.option["CONNECTION_REQUIRED"] == 1

    mFed.property[h.HELICS_PROPERTY_TIME_DELTA] = 1.0
    assert mFed.property[h.HELICS_PROPERTY_TIME_DELTA] == 1.0

    sub.set_default(b"hello")
    assert sub.bytes == b"hello"

    sub.set_default("world")
    assert sub.string == "world"

    sub.set_default(0)
    assert sub.integer == 0

    sub.set_default(True)
    assert sub.boolean is True

    sub.set_default(1.1)
    assert sub.double == 1.1

    sub.set_default(2 + 1.1j)
    assert sub.complex == 2 + 1.1j

    sub.set_default([1.0, 2.0, 3.0])
    assert sub.vector == [1.0, 2.0, 3.0]

    sub.set_default([complex(1.0, 2.0), complex(3.0, 4.0), complex(5.0, 6.0)])
    sub.info = "hello world"
    assert sub.info == "hello world"

    assert_entries(
        mFed.publications["TestFederate/publication"].option,
        DEFAULT_PUB_OPTION_SETTINGS,
    )
    mFed.publications["TestFederate/publication"].option["CONNECTION_REQUIRED"] = 1
    assert (
        mFed.publications["TestFederate/publication"].option["CONNECTION_REQUIRED"] == 1
    )

    mFed.enter_executing_mode()

    data = "random-data"

    mFed.endpoints["TestFederate/ep1"].default_destination = "ep2"
    mFed.endpoints["TestFederate/ep1"].info = "information"

    assert mFed.endpoints["TestFederate/ep1"].default_destination == "ep2"
    assert mFed.endpoints["TestFederate/ep1"].info == "information"

    mFed.endpoints["TestFederate/ep1"].send_data(data, "ep2", 1.0)

    mFed.publications["TestFederate/publication"].publish("first-time")

    assert mFed.request_time(2.0) == 1.0

    assert mFed.subscriptions["TestFederate/publication"].value == "first-time"
    try:
        assert mFed.subscriptions["TestFederate/publication"].bytes == b"first-time"
    except Exception:
        # TODO: this does not work as expected
        with pt.raises(AssertionError):
            assert mFed.subscriptions["TestFederate/publication"].bytes == b"first-time"

    assert mFed.has_message()

    assert mFed.endpoints["TestFederate/ep1"].has_message() is False

    assert mFed.endpoints["ep2"].has_message()

    message = mFed.endpoints["ep2"].get_message()

    assert message.is_valid() is True

    assert_attributes(
        message,
        {
            "source": "TestFederate/ep1",
            "destination": "ep2",
            "original_source": "TestFederate/ep1",
            "original_destination": "",
            "time": 1.0,
            "message_id": 55,
            "data": "random-data",
            "raw_data": b"random-data",
        },
    )

    message.append("-random")
    assert message.is_valid() is True
    assert message.data == "random-data-random"

    message.data = "random-data"
    assert message.raw_data == b"random-data"

    message.raw_data = b"random-data-random"
    assert message.data == "random-data-random"

    assert message.is_valid() is True
    message.message_id = 100
    message.source = "earth"
    message.destination = "moon"
    message.original_source = "hello-world"
    message.original_destination = "goodbye-world"
    message.time = 2.0

    assert message.is_valid() is True
    assert message.message_id == 100
    assert message.source == "earth"
    assert message.destination == "moon"
    assert message.original_source == "hello-world"
    assert message.original_destination == "goodbye-world"
    assert message.time == 2.0

    assert message.is_valid() is True
    # TODO(josephmckinsey): This will probably fail
    assert_entries(message.flag, {i: False for i in range(1, 16)})
    assert message.is_valid() is True
    message.flag[1] = True
    assert message.flag[1] is True

    mFed.publications["TestFederate/publication"].publish(1)

    assert mFed.request_next_step() == 2.0

    assert mFed.subscriptions["TestFederate/publication"].string == "1"

    mFed.endpoints["TestFederate/ep1"].send_data(message, "ep2")
    mFed.endpoints["TestFederate/ep1"].send_data(message, "ep2", 1.0)

    mFed.publications["TestFederate/publication"].publish(1 + 2j)

    assert mFed.request_next_step() == 3.0

    try:
        assert mFed.subscriptions["TestFederate/publication"].string == "1+2j"
    except AssertionError:
        assert mFed.subscriptions["TestFederate/publication"].string == "[1,2]"

    mFed.publications["TestFederate/publication"].publish([1, 2, 3, 4, 5])

    assert mFed.request_next_step() == 4.0

    assert mFed.subscriptions["TestFederate/publication"].vector == [
        1.0,
        2.0,
        3.0,
        4.0,
        5.0,
    ]

    mFed.publications["TestFederate/publication"].publish(False)

    assert mFed.request_next_step() == 5.0

    assert mFed.subscriptions["TestFederate/publication"].boolean is False
    m = mFed.create_message()
    assert_attributes(
        m,
        {
            "source": "",
            "destination": "",
            "original_source": "",
            "original_destination": "",
            "time": 0.0,
            "data": "",
            "message_id": 0,
        },
    )
    mFed.info = "hello-world"
    assert mFed.info == "hello-world"

    m = mFed.endpoints["ep2"].create_message()
    assert_attributes(
        m,
        {
            "source": "",
            "destination": "",
            "original_source": "",
            "original_destination": "",
            "time": 0.0,
            "data": "",
            "message_id": 0,
        },
    )
    mFed.disconnect()


def test_python_api2():
    broker = h.helicsCreateBroker(
        "zmq", "broker", "--federates 1 --loglevel=warning  --name=mainbroker2"
    )
    assert broker.is_connected()

    broker.set_global("hello", "world")

    broker.data_link("hello", "world")
    broker.add_destination_filter_to_endpoint("hello", "world")
    broker.add_source_filter_to_endpoint("hello", "world")
    try:
        assert broker.query("hello", "world") == "#invalid"
    except AssertionError:
        assert broker.query("hello", "world") == {
            "error": {"code": 404, "message": "query not valid"}
        }

    fi = h.helicsCreateFederateInfo()
    fi.core_init = "--federates 1 --brokername=mainbroker2 --name=core2"
    fi.property[h.HELICS_PROPERTY_INT_LOG_LEVEL] = 2

    fed = h.helicsCreateCombinationFederate("test1", fi)

    assert isinstance(fed.core, h.HelicsCore)
    # assert ignores port intentionally
    assert "tcp://127.0.0.1" in fed.core.address

    assert fed.core.is_connected()
    fed.core.set_ready_to_init()

    assert_attributes(
        fed,
        {"n_publications": 0, "n_subscriptions": 0, "n_endpoints": 0, "n_filters": 0},
    )

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
    assert fed.property["FILE_LOG_LEVEL"] == 2
    assert fed.property["CONSOLE_LOG_LEVEL"] == 2

    fed.property[h.HELICS_PROPERTY_INT_LOG_LEVEL] = 5

    fed.separator = "_"
    assert fed.separator == "_"

    fed.separator = "/"
    assert fed.separator == "/"

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

    assert fed.flag["TERMINATE_ON_ERROR"] is False
    fed.flag["TERMINATE_ON_ERROR"] = False

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

    fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] = True

    assert fed.flag[h.HELICS_FLAG_TERMINATE_ON_ERROR] is True

    fed.core.register_filter(h.HelicsFilterType.DELAY, "")
    fed.core.register_cloning_filter("")

    fed.register_filter(h.HelicsFilterType.DELAY, "")
    fed.register_cloning_filter("")

    fed.register_global_filter(h.HelicsFilterType.DELAY, "")
    fed.register_global_cloning_filter("")

    fed.core.set_global("hello", "world")

    try:
        assert fed.core.query("broker", "something") == "#invalid"
    except AssertionError:
        assert fed.core.query("broker", "something") == {
            "error": {"code": 400, "message": "unrecognized broker query"}
        }

    fed.add_dependency("hello")

    fed.core.disconnect()

    assert fed.core.wait_for_disconnect()

    broker.disconnect()
    assert broker.wait_for_disconnect()


def test_python_api3():
    core1 = h.helicsCreateCore("inproc", "core3", "--autobroker")

    assert_attributes(core1, {"identifier": "core3", "address": "core3"})

    core2 = core1.clone()

    assert core1.identifier == "core3"

    source_filter1 = core1.register_filter(
        h.HELICS_FILTER_TYPE_DELAY, "core3SourceFilter"
    )

    source_filter1.add_source_target("ep1")

    assert_entries(
        source_filter1.option,
        {
            **DEFAULT_PUB_OPTION_SETTINGS,
            h.HelicsHandleOption.MULTIPLE_CONNECTIONS_ALLOWED: 0,
        },
    )

    source_filter1.option["CONNECTION_REQUIRED"] = 1
    assert source_filter1.option["CONNECTION_REQUIRED"] == 1

    source_filter1.add_source_target("hello")
    source_filter1.add_destination_target("world")
    source_filter1.remove_destination_target("world")

    source_filter1.info = "hello world"
    assert source_filter1.info == "hello world"

    source_filter1.set("hello", 1)

    destination_filter1 = core1.register_filter(
        h.HELICS_FILTER_TYPE_DELAY, "core1DestinationFilter"
    )

    destination_filter1.add_destination_target("ep2")
    cloning_filter1 = core1.register_cloning_filter("ep3")

    cloning_filter1.remove_delivery_endpoint("ep3")
    cloning_filter1.add_delivery_endpoint("ep3")

    assert core1.is_valid()
    assert core1.is_connected()
    core1.set_ready_to_init()

    core1.disconnect()
    core2.disconnect()


def test_python_api4():
    fi = h.helicsCreateFederateInfo()
    fi.separator = "_"
    fi.broker = "broker test"

    fi.broker_key = "hello-world"

    fi.broker_port = 8929
    fi.local_port = 8229

    fi.broker_init = "-f 3"

    fi.flag[h.HelicsFlag.TERMINATE_ON_ERROR] = True
    fi.property[h.HelicsProperty.TIME_DELTA] = 1.0
    fi.property["TIME_DELTA"] = 1.0


def test_python_api5():
    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1 --name=mainbroker5")
    fi = h.helicsCreateFederateInfo()

    fed = h.helicsCreateCombinationFederate("test1", fi)
    with pt.raises(h.HelicsException):
        fed.register_interfaces("unknownfile.json")

    fed.core.disconnect()
    assert fed.core.wait_for_disconnect()

    broker.disconnect()
    assert broker.wait_for_disconnect()


def test_python_api6():
    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1 --name=mainbroker6")
    fi = h.helicsCreateFederateInfo()

    fed = h.helicsCreateCombinationFederate("test1", fi)

    fed.enter_initializing_mode()
    fed.enter_executing_mode()

    fed.core.disconnect()
    assert fed.core.wait_for_disconnect()

    broker.disconnect()
    assert broker.wait_for_disconnect()


@pt.mark.skip(reason="Fails to pass on windows and linux")
def test_python_api7():
    broker = h.helicsCreateBroker("zmq", "broker", "--federates 1 --name=mainbroker7")
    fi = h.helicsCreateFederateInfo()

    fed = h.helicsCreateCombinationFederate("test1", fi)

    _ = fed.register_filter(h.HELICS_FILTER_TYPE_DELAY, "core1SourceFilter")

    assert (
        fed.get_filter_by_name("core1SourceFilter").name
        == fed.get_filter_by_index(0).name
    )

    fed.set_global("hello", "world")

    # TODO: is_async_operation_completed
    assert fed.is_async_operation_completed() is False

    fed.enter_initializing_mode_async()
    fed.enter_initializing_mode_complete()

    assert fed.is_async_operation_completed() is False

    fed.enter_executing_mode_async()
    fed.enter_executing_mode_complete()

    assert fed.is_async_operation_completed() is False

    fed.request_time_advance(2.0)
    assert fed.current_time == 2.0

    fed.request_time_async(4.0)
    assert fed.current_time == 2.0
    fed.request_time_complete()
    assert fed.current_time == 4.0

    try:
        assert fed.query("hello", "world") == "#disconnected"
    except AssertionError:
        assert fed.query("hello", "world") == {
            "error": {"code": 404, "message": "query not valid"}
        }

    fed.local_error(0, "local")
    fed.global_error(0, "global")

    fed.log_message("error", logging.ERROR)
    fed.log_message("warn", logging.WARN)
    fed.log_message("info", logging.INFO)
    fed.log_message("debug", logging.DEBUG)
    fed.log_message("summary", h.HELICS_LOG_LEVEL_SUMMARY)

    fed.disconnect_async()
    fed.disconnect_complete()

    fed.core.disconnect()
    assert fed.core.wait_for_disconnect()

    broker.disconnect()
    assert broker.wait_for_disconnect()


def test_python_api8():
    broker = h.helicsCreateBroker("zmq", "", "-f 1 --name=mainbroker8")

    cfed = h.helicsCreateCombinationFederateFromConfig(
        os.path.join(CURRENT_DIRECTORY, "combinationfederate.json")
    )

    assert len(cfed.endpoints) == 2
    assert len(cfed.subscriptions) == 2

    h.helicsFederateDestroy(cfed)
    h.helicsFederateFree(cfed)
    h.helicsBrokerDestroy(broker)


def test_python_api9():
    broker = h.helicsCreateBroker("zmq", "", "-f 1 --name=mainbroker")
    fedinfo = h.helicsCreateFederateInfo()
    assert isinstance(fedinfo, h.HelicsFederateInfo)
    fedinfo.core_name = "TestFederate"
    fedinfo.core_type = "zmq"
    fedinfo.core_init = "-f 1 --broker=mainbroker"
    mFed = h.helicsCreateCombinationFederate("TestFederate", fedinfo)

    pub = mFed.register_publication(
        "publication", h.HELICS_DATA_TYPE_COMPLEX_VECTOR, "custom-units"
    )
    assert pub.type == "complex_vector"

    sub = mFed.register_subscription("TestFederate/publication", "custom-units")
    sub.set_default([complex(1.0, 2.0), complex(3.0, 4.0), complex(5.0, 6.0)])

    mFed.enter_executing_mode()

    assert sub.publication_type == "complex_vector"
    print(sub.value)

    mFed.disconnect()
