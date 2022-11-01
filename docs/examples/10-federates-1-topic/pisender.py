# -*- coding: utf-8 -*-
import time

from math import pi
import helics as h
import random


def main(n):

    federate_name = f"SenderFederate{n}"

    print(f"{federate_name}: Helics version = {h.helicsGetVersion()}")

    fedinfo = h.helicsCreateFederateInfo()
    fedinfo.core_type = "zmq"
    fedinfo.property[h.HELICS_PROPERTY_TIME_DELTA] = 1.0
    fedinfo.property[h.HELICS_PROPERTY_TIME_PERIOD] = 1.0

    fed = h.helicsCreateCombinationFederate(federate_name, fedinfo)

    print(f"{federate_name}: Combination federate created")

    fed.register_global_publication(f"globaltopic", h.HELICS_DATA_TYPE_DOUBLE)

    print(f"{federate_name}: Publication registered")

    fed.enter_executing_mode()
    print(f"{federate_name}: Entering execution mode")

    for t in range(0, 10):
        value = pi * t

        fed.request_next_step()

        fed.publications[f"globaltopic"].publish(value)
        print(f"{federate_name}: Sending value pi = {value} at time {fed.current_time} on globaltopic")

        # Computing user needs
        time.sleep(float(n) * (1 + (0.5 - random.random()) / 10))

    fed.disconnect()
    print(f"{federate_name}: Federate finalized")
    del fed

    h.helicsCloseLibrary()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        n = 1
    else:
        n = int(sys.argv[1])
    main(n)
