# -*- coding: utf-8 -*-
import time
import helics as h


def assert_attributes(obj, attributes: dict[str, any]):
    for key, value in attributes.items():
        assert hasattr(obj, key), f"{repr(obj)} does not have attribute {key}"
        assert getattr(obj, key) == value, f"{repr(obj)}.{key} is not {value}"


def create_broker(number=1):
    initstring = f"-f {number} --name=mainbroker"
    # @test_throws h.HELICSErrorInvalidArgument broker = h.helicsCreateBroker("mq", "", initstring)
    broker = h.helicsCreateBroker("zmq", "", initstring)
    # assert broker is h.Broker
    assert h.helicsBrokerIsConnected(broker) is True
    return broker


def setup_federate_info(name="A Core", number=1, deltat=0.01):
    fedinitstring = f"--broker=mainbroker --federates={number}"

    # Create Federate Info object that describes the federate properties
    fedinfo = h.helicsCreateFederateInfo()
    # assert fedinfo isa h.FederateInfo

    # # Set Federate name
    h.helicsFederateInfoSetCoreName(fedinfo, f"Test{name}")

    # # Set core type from string
    h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")

    # # Federate init string
    h.helicsFederateInfoSetCoreInitString(fedinfo, fedinitstring)

    # # Set the message interval (timedelta) for federate. Note th#
    # # HELICS minimum message time interval is 1 ns and by default
    # # it uses a time delta of 1 second. What is provided to the
    # # setTimedelta routine is a multiplier for the default timedelta.

    # # Set one second message interval
    h.helicsFederateInfoSetTimeProperty(fedinfo, h.HELICS_PROPERTY_TIME_DELTA, deltat)
    h.helicsFederateInfoSetIntegerProperty(fedinfo, h.HELICS_PROPERTY_INT_LOG_LEVEL, -1)
    return fedinfo


def create_value_federate(federates=1, name="A Federate", deltat=0.01):
    fedinfo = setup_federate_info(name, federates, deltat)
    vFed = h.helicsCreateValueFederate(f"Test{name}", fedinfo)
    # assert vFed isa h.ValueFederate
    return vFed, fedinfo


def create_message_federate(federates=1, name="A Federate", deltat=0.01):
    fedinfo = setup_federate_info(name, federates, deltat)
    mFed = h.helicsCreateMessageFederate(f"Test{name}", fedinfo)
    # assert mFed isa h.MessageFederate
    return mFed, fedinfo


def destroy_broker(broker):
    h.helicsBrokerDisconnect(broker)


def destroy_federate(fed, fedinfo, broker=None):
    h.helicsFederateDisconnect(fed)
    _ = h.helicsFederateGetState(fed)
    if broker is not None:
        while h.helicsBrokerIsConnected(broker):
            time.sleep(1)
    h.helicsFederateInfoFree(fedinfo)
    h.helicsFederateFree(fed)
    if broker is not None:
        destroy_broker(broker)
