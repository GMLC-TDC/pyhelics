# Usage

The following is simple example HELICS federation implemented in Python. The example files containing this code can be [found here](https://github.com/GMLC-TDC/pyhelics/tree/main/docs/examples/website_usage). The federation can be run from the command line with

```sh
$ helics run --path=runner.json
```

Many more Python-based HELICS examples can be found in the [HELICS Examples repository](https://github.com/GMLC-TDC/HELICS-Examples/user_guide_examples) with many of them having corresponding documentation in the [HELICS User Guide](https://docs.helics.org/en/latest/user-guide/examples/examples_index.html)

# Broker

```python
import helics as h
import time

broker = h.helicsCreateBroker("zmq", "", "-f 2 --loglevel=trace")

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
h.helicsFederateInfoSetCoreInitString(fedinfo, "--federates=1")
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

h.helicsFederateDisconnect(vfed)
h.helicsFederateDestroy(vfed)
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

h.helicsFederateDisconnect(vfed)
h.helicsFederateDestroy(vfed)
```
