# Implementing HELICS Callbacks in Python

There are several HELICS functionalities that allow for the definition of custom behavior through the use of custom callback functions. Two specific examples are the definition of the filter behavior when implementing a filter federate and the other is the response to a custom query. In both cases custom code needs to be written to define behavior when HELICS needs to perform a specific action (filter a message, respond to a query). There are a few steps to implement callbacks in PyHELICS

## Define User Data
The callback function generally exists outside the scope of other code and thus, if the functionality defined in the callback needs data from, say, the federate, that data has to be carried into the callback through a custom class generically called "user data". This user data is defined as a class that is instantiated and filled as a part of federate operation.  

```python
# Store what ever data you'd like. 
# A reference to this object is passed to the filter callback. 
# You don't need to use this if you don't want to.
class UserData(object):
    def __init__(self, iteration_count = None):
        self.pi = 3.14
        self.e = 2.718
        self.interation_count = iteration_count
```

## Define the Callback
This is where the real C-to-Python magic happens, using the "cffi" library. As the HELICS library being used is C-based, there are several things that look weird in the Python world that we have to do to properly hook into that library. The biggest of these is adding a Python decorator to the callback in the form of a string that contains the C signature of the callback being implemented. For example:

```python
# Filter callback
@h.ffi.callback("void logger(HelicsMessage, void* userData)")
def filter_callback(mess, userData):
    # Filter operation code here

# Query callback
@h.ffi.callback("void query(const char *query, int querySize, HelicsQueryBuffer buffer, void *user_data)")
def query_callback(query_ptr, size:int, query_buffer_ptr, user_data):
    query_str = h.ffi.string(query_ptr,size).decode()
    query_buffer = h.HelicsQueryBuffer(query_buffer_ptr)
    # Query operation code here
    
```

In the case of the query callback, you can see there are two other bits that need to be added in.
  
  1 - The query string is passed in as a C pointer. If you've only worked in Python, you might wonder what a "pointer" is. So does Python; the "cffi" library is used to translate the data the pointer is referencing into something Python recognizes as a string. 
  2 - The query response that will be created by the callback function must be put into a pre-constructed databuffer that is passed in when the callback is made ("HelicsQueryBuffer buffer" in the above C signature). HELICS will read this buffer to get the response of the callback. Again, pointers are involved so we use the "cffi" library to make them something Python can deal with.

## Register the Callback
Last step, with the callback defined we need to "register" it so that HELICS knows which function to call when its time to execute the callback. This is done as part of setting up your federate and should be done as early as possible so that the federate is able to respond to any callbacks that come in early in the life of a federate.



```python
# Filter callback federate code
def main():
    ...
    f1 = h.helicsFederateRegisterFilter(fFed, h.HELICS_FILTER_TYPE_CUSTOM, "filter1")
    userdata = UserData(iteration_count = 10)
    user_data_handle = h.ffi.new_handle(userdata)
    h.helicsFilterSetCustomCallback(f1, filter_callback, user_data_handle)


# Query callback federate code
def main():
    ...
    fed = h.helicsCreateValueFederateFromConfig("math_fed.json")
    user_data = UserData(iteration_count = 10)
    user_data_handle = h.ffi.new_handle(user_data)
    h.helicsFederateSetQueryCallback(fed, query_callback, user_data_handle)

```

In both cases, the user data is defined, a "handle" to the user data is created, and the callback functions are registered using specific HELICS APIs.

## Complete Examples
Here are the full code for completeness sake. As of this writing, there is not a running example for the filter callback but there is one for the [query callback](https://github.com/GMLC-TDC/HELICS-Examples/blob/53bece298f9be952002e2f9201f24922fabc73b4/user_guide_examples/advanced/advanced_connector/interface_creation/Charger.py) in the [HELICS Examples repository](https://github.com/GMLC-TDC/HELICS-Examples).


### Filter Federate Code
``` python

class UserData(object):
    def __init__(self, iteration_count = None):
        self.pi = 3.14
        self.e = 2.718
        self.interation_count = iteration_count
        
@h.ffi.callback("void logger(HelicsMessage, void* userData)")
def filter_callback(mess, userData):
    # Filter operation code here
    

def main():
    fed = h.helicsCreateValueFederateFromConfig("math_fed.json")
    f1 = h.helicsFederateRegisterFilter(fed, h.HELICS_FILTER_TYPE_CUSTOM, "filter1")
    userdata = UserData(iteration_count = 10)
    user_data_handle = h.ffi.new_handle(userdata)
    h.helicsFilterSetCustomCallback(f1, filter_callback, user_data_handle)
```

### Query Response Code
```Python
class UserData(object):
    def __init__(self, iteration_count = None):
        self.pi = 3.14
        self.e = 2.718
        self.interation_count = iteration_count

@h.ffi.callback("void query(const char *query, int querySize, HelicsQueryBuffer buffer, void *user_data)")
def query_callback(query_ptr, size:int, query_buffer_ptr, user_data):
    query_str = h.ffi.string(query_ptr,size).decode()
    query_buffer = h.HelicsQueryBuffer(query_buffer_ptr)
    # Query operation code here
    

def main():
    fed = h.helicsCreateValueFederateFromConfig("math_fed.json")
    user_data = UserData(iteration_count = 10)
    user_data_handle = h.ffi.new_handle(user_data)
    h.helicsFederateSetQueryCallback(fed, query_callback, user_data_handle)

```