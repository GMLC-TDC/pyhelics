# Pythonic interface

Example of what it looks like to use the Pythonic interface:

```python
import helics as h

broker = h.helicsCreateBroker("zmq", "", "-f 1 --name=mainbroker")

fedinfo = h.helicsCreateFederateInfo()

fedinfo.core_name = "TestFederate"
fedinfo.core_type = "zmq"
fedinfo.core_init = "-f 1 --broker=mainbroker"

mFed = h.helicsCreateCombinationFederate("TestFederate", fedinfo)
mFed.register_endpoint("ep1")
mFed.register_global_endpoint("ep2")
mFed.property[h.HELICS_PROPERTY_TIME_DELTA] = 1.0

pub = mFed.register_publication("publication", h.HELICS_DATA_TYPE_STRING, "custom-units")

sub = mFed.register_subscription("TestFederate/publication", "custom-units")
sub.option["CONNECTION_REQUIRED"] = 1
sub.set_default(b"hello")
sub.set_default("world")
sub.set_default(0)
sub.set_default(True)
sub.set_default(1.1)
sub.set_default(2 + 1.1j)
sub.set_default([1.0, 2.0, 3.0])

sub.info = "hello world"

mFed.publications["TestFederate/publication"].option["CONNECTION_REQUIRED"] = 1

mFed.enter_executing_mode()

data = "random-data"

mFed.endpoints["TestFederate/ep1"].default_destination = "ep2"
mFed.endpoints["TestFederate/ep1"].info = "information"

mFed.endpoints["TestFederate/ep1"].send_data(data, "ep2", 1.0)

mFed.publications["TestFederate/publication"].publish("first-time")

assert mFed.request_time(2.0) == 1.0

print("""mFed.subscriptions["TestFederate/publication"].bytes: """, mFed.subscriptions["TestFederate/publication"].bytes)

assert mFed.subscriptions["TestFederate/publication"].bytes == b"first-time"

print("Exiting...")
```