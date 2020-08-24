# Migrating python code from HELICS v2.x.x to HELICS v3.x.x

This document will describe the path to migrate your python code from HELICS version 2.x.x to version 3.x.x.

You can also see the [tests](https://github.com/GMLC-TDC/pyhelics/tree/master/tests) folder on github for more examples on how to use the various functions.

### Functions

**Related to `HelicsMessage`**

Previously you may have add code to deal with `message`s like this:

```python
# helics v2
m = h.helicsEndpointGetMessage(endpoint)
assert m.source == "port1"
assert m.original_source == "port1"
assert m.destination == "port2"
assert m.data == len(data)
assert m.time == 2.5
```

The return object of `helicsEndpointGetMessage(endpoint)` is now a opaque object and you will have to use `helics*` functions to get the various attributes of that object.

```python
# helics v3
m = h.helicsEndpointGetMessage(endpoint)
assert h.helicsMessageGetSource(m) == "port1"
assert h.helicsMessageGetOriginalSource(m) == "port1"
assert h.helicsMessageGetDestination(m) == "port2"
assert h.helicsMessageGetRawDataSize(m) == len(data)
assert h.helicsMessageGetTime(m) == 2.5
```

**Related to raw data**

Additionally, any function that takes `bytes` as an input must be passed in a python bytestring. If you have a regular python unicode string, as the user yoou are responsible for converting to a byte string with an encoding of your choice.

To convert a python unicode string to a byte string, you can do `"hello world".encode()`.
You can even specify the encoding: `"hello world".encode()`.

Similarly, any helics function that returns a byte string must be handled correctly on the user end. As a user, you are at the moment required to know the encoding of the message in order to convert it to the correct string.

**Related to complex numbers**

Previously, you would need to pass real and imaginary components of complex numbers as separate floating point values.

```python
# helics v2
h.helicsInputSetDefaultComplex(sub, -9.9, 2.5)
```

Now you can pass them as a complex number.

```python
# helics v3
h.helicsInputSetDefaultComplex(sub, -9.9 + 2.5j)
```

These are the full list of functions:

- `helicsInputGetComplex`
- `helicsPublicationPublishComplex`
- `helicsInputSetDefaultComplex`

that are affected by this change.

### Enumerations

Enumerations are constants now, and are represented by upper case variables:

```python
# helics v2
h.helicsFederateInfoSetIntegerProperty(fedInfo1, h.helics_property_int_log_level, 1)
h.helicsFederateInfoSetIntegerProperty(fedInfo1, h.helics_property_int_max_iterations, 100)
```

```python
# helics v3
h.helicsFederateInfoSetIntegerProperty(fedInfo1, h.HELICS_PROPERTY_INT_LOG_LEVEL, 1)
h.helicsFederateInfoSetIntegerProperty(fedInfo1, h.HELICS_PROPERTY_INT_MAX_ITERATIONS, 100)
```

### New functionality

If you would like to use callbacks you can:

```python
@h.ffi.callback("void logger(helics_message_object, void* userData)")
def filterFunc1(mess, user_data):
    time = h.helicsMessageGetTime(mess)
    user_data = h.ffi.from_handle(user_data)

    h.helicsMessageSetTime(mess, time + 2.5)
    user_data += 1


class UserData(object):
    def __init__(self, x):
        self.x = x


...

user_data = UserData(5)
handle = h.ffi.new_handle(user_data)
h.helicsFilterSetCustomCallback(f1, filterFunc1, handle)

...
```

Find the signature of the function that you'd like to call, use `h.ffi.callback` as a python decorator for that function.

```python
@h.ffi.callback("void logger(helics_message_object, void* userData)")
```

Then, you can pass the variable that contains a reference to this C function to a helics callback function.
The user is responsible for managing memory with relation to these objects.
See [`cffi`'s documentation](https://cffi.readthedocs.io/en/latest/using.html#callbacks-old-style) for more information.
