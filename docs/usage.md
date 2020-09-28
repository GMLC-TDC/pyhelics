# Usage

This document will a simple 2 federate co-simulation in Python.

# Broker

```python
import helics as h

broker = h.helicsCreateBroker("zmq", "", "-f 2 --name=mainbroker")

while h.helicsBrokerIsConnected(broker):
    time.sleep(1)
```

# Federate 1

```python
import time
import helics as h
from math import pi

fedinfo = h.helicsCreateFederateInfo()

h.helicsFederateInfoSetCoreName(fedinfo, "Federate1")
h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")
h.helicsFederateInfoSetCoreInitString(fedinfo, "--broker=mainbroker --federates=1")
h.helicsFederateInfoSetTimeProperty(fedinfo, h.HELICS_PROPERTY_TIME_DELTA, 0.01)

vfed = h.helicsCreateValueFederate("Federate1", fedinfo)

pub = h.helicsFederateRegisterGlobalTypePublication(vfed, "topic_name", "double", "")

h.helicsFederateEnterExecutingMode(vfed)

this_time = 0.0

for t in range(5, 10):

    currenttime = h.helicsFederateRequestTime(vfed, t)

    h.helicsPublicationPublishDouble(pub, pi)
    print("SENDER: Sending value pi = {} at time {} to RECEIVER".format(pi, currenttime))

    time.sleep(1)

h.helicsFederateFinalize(vfed)

h.helicsFederateFree(vfed)
h.helicsCloseLibrary()
```

# Federate 2

```python
import helics as h

fedinfo = h.helicsCreateFederateInfo()
h.helicsFederateInfoSetCoreName(fedinfo, "Federate2")
h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")
h.helicsFederateInfoSetCoreInitString(fedinfo, "--federates=1")
h.helicsFederateInfoSetTimeProperty(fedinfo, h.HELICS_PROPERTY_TIME_DELTA, 0.01)

vfed = h.helicsCreateValueFederate("Federate2", fedinfo)

sub = h.helicsFederateRegisterSubscription(vfed, "topic_name", "")

h.helicsFederateEnterExecutingMode(vfed)

value = 0.0
currenttime = -1

while currenttime <= 100:

    currenttime = h.helicsFederateRequestTime(vfed, 100)

    value = h.helicsInputGetString(sub)
    print("RECEIVER: Received value = {} at time {} from SENDER".format(value, currenttime))

h.helicsFederateFinalize(vfed)

h.helicsFederateFree(vfed)
h.helicsCloseLibrary()
```
