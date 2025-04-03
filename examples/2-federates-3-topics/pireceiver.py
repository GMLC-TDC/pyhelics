# -*- coding: utf-8 -*-
import helics as h


def main(n):
    federate_name = f"ReceiverFederate{n}"

    print(f"{federate_name}: Helics version = {h.helicsGetVersion()}")

    fedinfo = h.helicsCreateFederateInfo()
    fedinfo.core_type = "zmq"
    fedinfo.property[h.HELICS_PROPERTY_TIME_DELTA] = 1.0
    fedinfo.property[h.HELICS_PROPERTY_TIME_PERIOD] = 1.0

    fed = h.helicsCreateCombinationFederate(federate_name, fedinfo)

    print(f"{federate_name}: Value federate created")

    fed.register_subscription(f"globaltopic{n}").set_default(0.0)
    fed.register_subscription(f"globaltopic{n+1}").set_default(0.0)
    fed.register_subscription(f"globaltopic{n+2}").set_default(0.0)

    fed.enter_executing_mode()
    print(f"{federate_name}: Entering execution mode")

    currenttime = -1
    while currenttime <= 10:

        currenttime = fed.request_time(10)

        value = fed.subscriptions[f"globaltopic{n}"].value
        print(f"{federate_name}: Received value = {value} at time {currenttime}")
        value = fed.subscriptions[f"globaltopic{n+1}"].value
        print(f"{federate_name}: Received value = {value} at time {currenttime}")
        value = fed.subscriptions[f"globaltopic{n+2}"].value
        print(f"{federate_name}: Received value = {value} at time {currenttime}")

    fed.disconnect()

    print(f"{federate_name}: Federate finalized")


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        n = 1
    else:
        n = int(sys.argv[1])
    main(n)
