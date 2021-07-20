# Migrating python code from HELICS v2.x.x to HELICS v3.x.x

This document will describe the path to migrate your python code from HELICS version 2.x.x to version 3.x.x.

**pyhelics** is backward and forward compatible. So you won't need to make any of these changes. The following document is for reference only.

[See this commit for a diff of all the changes](https://github.com/GMLC-TDC/pyhelics/commit/366a4c5cb7fdfe44e48a85acdde0be43d56df3a3).

You can also see the [tests](https://github.com/GMLC-TDC/pyhelics/tree/main/tests) folder on github for more examples on how to use the various functions.

See [the Pythonic Interface](./pythonic-interface.md) for all the new functionality that is available in pyhelics.

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

Functions named with `MessageObject` are renamed to use `Message`. This is all handled transparently in pyhelics, so you don't need to deal with it.

This function has been renamed: `helicsMessageCheckFlag` -> `helicsMessageGetFlagOption` to be consistent with `helicsMessageSetFlagOption`.

**Related to raw data**

Additionally, any function that takes `bytes` as an input must be passed in a python bytestring. If you have a regular python unicode string, as the user yoou are responsible for converting to a byte string with an encoding of your choice.

To convert a python unicode string to a byte string, you can do `"hello world".encode()`.
You can even specify the encoding: `"hello world".encode()`.

Similarly, any helics function that returns a byte string must be handled correctly on the user end. As a user, you are at the moment required to know the encoding of the message in order to convert it to the correct string.

All functions that have `Raw` in the name are replaced with functions that have `Bytes` in the name.

e.g.

`helicsMessageGetRawData` -> `helicsMessageGetBytes`

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

**Related to endpoints**

The following functions have been renamed and the argument order has been updated:

- `helicsEndpointSendMessageRaw` -> `helicsEndpointSendBytesTo`
- `helicsEndpointSendEventRaw` -> `helicsEndpointSendBytesToAt`

### Related to counting

The following functions have been renamed:

- `helicsFederatePendingMessages` -> `helicsFederatePendingMessageCount`
- `helicsEndpointPendingMessages` -> `helicsEndpointPendingMessageCount`

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

If you would like to use callbacks you can do the following in HELICS v3.x.x:

```python
@h.ffi.callback("void logger(HelicsMessage, void* userData)")
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

In HELICS v3,

```python
@h.ffi.callback("void logger(HelicsMessage, void* userData)")
```

In HELICS v2.x.x, use `helics_message_object` instead.

```python
@h.ffi.callback("void logger(helics_message_object, void* userData)")
```

Then, you can pass the variable that contains a reference to this C function to a helics callback function.
The user is responsible for managing memory with relation to these objects.
See [`cffi`'s documentation](https://cffi.readthedocs.io/en/latest/using.html#callbacks-old-style) for more information.
