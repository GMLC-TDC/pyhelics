# -*- coding: utf-8 -*-
import time
import sys

from math import pi
import helics as h
import random

federate_name = f"SenderFederate{sys.argv[1]}"

print(f"{federate_name}: Helics version = {h.helicsGetVersion()}")

fedinfo = h.helicsCreateFederateInfo()

h.helicsFederateInfoSetCoreName(fedinfo, federate_name + "Core")
h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")
h.helicsFederateInfoSetCoreInitString(fedinfo, "--federates=1")
h.helicsFederateInfoSetTimeProperty(fedinfo, h.helics_property_time_delta, 1.0)
h.helicsFederateInfoSetTimeProperty(fedinfo, h.helics_property_time_period, 1.0)

fed = h.helicsCreateCombinationFederate(federate_name, fedinfo)

print(f"{federate_name}: Combination federate created")

pub = h.helicsFederateRegisterGlobalTypePublication(fed, f"globaltopic{sys.argv[1]}", "double", "")

print(f"{federate_name}: Publication registered")

h.helicsFederateEnterExecutingMode(fed)

print(f"{federate_name}: Entering execution mode")

this_time = 0.0
grantedtime = -1

for t in range(1, 10):
    value = pi * t

    while grantedtime < t:
        grantedtime = h.helicsFederateRequestTime(fed, t)

    h.helicsPublicationPublishDouble(pub, value)

    print(f"{federate_name}: Sending value pi = {value} at time {grantedtime}")

    # Computing user needs
    time.sleep(float(sys.argv[1]) * (1 + (0.5 - random.random()) / 10))

h.helicsFederateFinalize(fed)
print(f"{federate_name}: Federate finalized")

h.helicsFederateFree(fed)
h.helicsCloseLibrary()
