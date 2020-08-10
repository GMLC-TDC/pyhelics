# Module helics


## Classes

### HelicsException {: #HelicsException }

```python
class HelicsException(self, *args, **kwargs)
```

Common base class for all non-exit exceptions.

Initialize self.  See help(type(self)) for accurate signature.


------

#### Base classes {: #HelicsException-bases }

* `builtins.Exception`


## Functions

### cchar {: #cchar }

```python
def cchar(c: str) -> str
```


------

### cdouble {: #cdouble }

```python
def cdouble(d: float) -> float
```


------

### cstring {: #cstring }

```python
def cstring(s: str) -> str
```


------

### helicsBrokerAddDestinationFilterToEndpoint {: #helicsBrokerAddDestinationFilterToEndpoint }

```python
def helicsBrokerAddDestinationFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str)
```

Link a named filter to a destination endpoint.

**Parameters**

* **broker** - The broker to generate the connection from.
* **filter** - The name of the filter (cannot be NULL).
* **endpoint** - The name of the endpoint to filter the data going to (cannot be NULL).

------

### helicsBrokerAddSourceFilterToEndpoint {: #helicsBrokerAddSourceFilterToEndpoint }

```python
def helicsBrokerAddSourceFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str)
```

Link a named filter to a source endpoint.

**Parameters**

* **broker** - The broker to generate the connection from.
* **filter** - The name of the filter (cannot be NULL).
* **endpoint** - The name of the endpoint to filter the data from (cannot be NULL).

------

### helicsBrokerClone {: #helicsBrokerClone }

```python
def helicsBrokerClone(broker: HelicsBroker) -> HelicsBroker
```

Create a new reference to an existing broker.
This will create a new broker object that references the existing broker it must be freed as well.

**Parameters**

* **broker** - An existing helics_broker.

------

### helicsBrokerDataLink {: #helicsBrokerDataLink }

```python
def helicsBrokerDataLink(broker: HelicsBroker, source: str, target: str)
```

Link a named publication and named input using a broker.

**Parameters**

* **broker** - The broker to generate the connection from.
* **source** - The name of the publication (cannot be NULL).
* **target** - The name of the target to send the publication data (cannot be NULL).

------

### helicsBrokerDestroy {: #helicsBrokerDestroy }

```python
def helicsBrokerDestroy(broker: HelicsBroker)
```

Disconnect and free a broker.

------

### helicsBrokerDisconnect {: #helicsBrokerDisconnect }

```python
def helicsBrokerDisconnect(broker: HelicsBroker)
```

Disconnect a broker.

**Parameters**

* **broker** - The broker to disconnect.

------

### helicsBrokerFree {: #helicsBrokerFree }

```python
def helicsBrokerFree(broker: HelicsBroker)
```

Release the memory associated with a broker.

------

### helicsBrokerGetAddress {: #helicsBrokerGetAddress }

```python
def helicsBrokerGetAddress(broker: HelicsBroker) -> str
```

Get the network address associated with a broker.

**Parameters**

* **broker** - The broker to query.

**Returns**: A string with the network address of the broker.

------

### helicsBrokerGetIdentifier {: #helicsBrokerGetIdentifier }

```python
def helicsBrokerGetIdentifier(broker: HelicsBroker) -> str
```

Get an identifier for the broker.

**Parameters**

* **broker** - The broker to query.

**Returns**: A string containing the identifier for the broker.

------

### helicsBrokerIsConnected {: #helicsBrokerIsConnected }

```python
def helicsBrokerIsConnected(broker: HelicsBroker) -> HelicsBool
```

Check if a broker is connected.
A connected broker implies it is attached to cores or cores could reach out to communicate.

**Returns**: `True` if connected, `False` if not connected.

------

### helicsBrokerIsValid {: #helicsBrokerIsValid }

```python
def helicsBrokerIsValid(broker: HelicsBroker) -> HelicsBool
```

Check if a broker object is a valid object.

**Parameters**

* **broker** - The helics_broker object to test.

------

### helicsBrokerMakeConnections {: #helicsBrokerMakeConnections }

```python
def helicsBrokerMakeConnections(broker: HelicsBroker, file: str)
```

Load a file containing connection information.

**Parameters**

* **broker** - The broker to generate the connections from.
* **file** - A JSON or TOML file containing connection information.

------

### helicsBrokerSetGlobal {: #helicsBrokerSetGlobal }

```python
def helicsBrokerSetGlobal(broker: HelicsBroker, valueName: str, value: str)
```

Set a federation global value.
This overwrites any previous value for this name.

**Parameters**

* **broker** - The broker to set the global through.
* **valueName** - The name of the global to set.
* **value** - The value of the global.

------

### helicsBrokerSetLogFile {: #helicsBrokerSetLogFile }

```python
def helicsBrokerSetLogFile(broker: HelicsBroker, logFileName: str)
```

Set the log file on a broker.

**Parameters**

* **broker** - The broker to set the log file for.
* **logFileName** - The name of the file to log to.

------

### helicsBrokerWaitForDisconnect {: #helicsBrokerWaitForDisconnect }

```python
def helicsBrokerWaitForDisconnect(broker: HelicsBroker, msToWait: int) -> HelicsBool
```

Wait for the broker to disconnect.

**Parameters**

* **broker** - The broker to wait for.
* **msToWait** - The time out in millisecond (<0 for infinite timeout).

------

### helicsCleanupLibrary {: #helicsCleanupLibrary }

```python
def helicsCleanupLibrary()
```

Function to do some housekeeping work.
This runs some cleanup routines and tries to close out any residual thread that haven't been shutdown yet.

------

### helicsCloseLibrary {: #helicsCloseLibrary }

```python
def helicsCloseLibrary()
```

Call when done using the helics library.
This function will ensure the threads are closed properly. If possible this should be the last call before exiting.

------

### helicsCoreAddDestinationFilterToEndpoint {: #helicsCoreAddDestinationFilterToEndpoint }

```python
def helicsCoreAddDestinationFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str)
```

Link a named filter to a destination endpoint.

**Parameters**

* **core** - The core to generate the connection from.
* **filter** - The name of the filter (cannot be NULL).
* **endpoint** - The name of the endpoint to filter the data going to (cannot be NULL).

------

### helicsCoreAddSourceFilterToEndpoint {: #helicsCoreAddSourceFilterToEndpoint }

```python
def helicsCoreAddSourceFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str)
```

Link a named filter to a source endpoint.

**Parameters**

* **core** - The core to generate the connection from.
* **filter** - The name of the filter (cannot be NULL).
* **endpoint** - The name of the endpoint to filter the data from (cannot be NULL).

------

### helicsCoreClone {: #helicsCoreClone }

```python
def helicsCoreClone(core: HelicsCore) -> HelicsCore
```

Create a new reference to an existing core.
This will create a new broker object that references the existing broker. The new broker object must be freed as well.

**Parameters**

* **core** - An existing helics_core.

------

### helicsCoreConnect {: #helicsCoreConnect }

```python
def helicsCoreConnect(core: HelicsCore) -> HelicsBool
```

Connect a core to the federate based on current configuration.

**Parameters**

* **core** - The core to connect.

------

### helicsCoreDataLink {: #helicsCoreDataLink }

```python
def helicsCoreDataLink(core: HelicsCore, source: str, target: str)
```

Link a named publication and named input using a core.

**Parameters**

* **core** - The core to generate the connection from.
* **source** - The name of the publication (cannot be NULL).
* **target** - The name of the target to send the publication data (cannot be NULL).

------

### helicsCoreDestroy {: #helicsCoreDestroy }

```python
def helicsCoreDestroy(core: HelicsCore)
```

Disconnect and free a core.

------

### helicsCoreDisconnect {: #helicsCoreDisconnect }

```python
def helicsCoreDisconnect(core: HelicsCore)
```

Disconnect a core from the federation.

**Parameters**

* **core** - The core to query.

------

### helicsCoreFree {: #helicsCoreFree }

```python
def helicsCoreFree(core: HelicsCore)
```

Release the memory associated with a core.

------

### helicsCoreGetAddress {: #helicsCoreGetAddress }

```python
def helicsCoreGetAddress(core: HelicsCore) -> str
```

Get the network address associated with a core.

**Parameters**

* **core** - The core to query.

**Returns**: A string with the network address of the broker.

------

### helicsCoreGetIdentifier {: #helicsCoreGetIdentifier }

```python
def helicsCoreGetIdentifier(core: HelicsCore) -> str
```

Get an identifier for the core.

**Parameters**

* **core** - The core to query.

**Returns**: A string with the identifier of the core.

------

### helicsCoreIsConnected {: #helicsCoreIsConnected }

```python
def helicsCoreIsConnected(core: HelicsCore) -> HelicsBool
```

Check if a core is connected.
A connected core implies it is attached to federates or federates could be attached to it.

**Returns**: `True` if connected, `False` if not connected.

------

### helicsCoreIsValid {: #helicsCoreIsValid }

```python
def helicsCoreIsValid(core: HelicsCore) -> HelicsBool
```

Check if a core object is a valid object.

**Parameters**

* **core** - The helics_core object to test.

------

### helicsCoreMakeConnections {: #helicsCoreMakeConnections }

```python
def helicsCoreMakeConnections(core: HelicsCore, file: str)
```

Load a file containing connection information.

**Parameters**

* **core** - The core to generate the connections from.
* **file** - A JSON or TOML file containing connection information.

------

### helicsCoreRegisterCloningFilter {: #helicsCoreRegisterCloningFilter }

```python
def helicsCoreRegisterCloningFilter(core: HelicsCore, name: str) -> HelicsFilter
```

Create a cloning Filter on the specified core.
Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

**Parameters**

* **core** - The core to register through.
* **name** - The name of the filter (can be NULL).

------

### helicsCoreRegisterFilter {: #helicsCoreRegisterFilter }

```python
def helicsCoreRegisterFilter(core: HelicsCore, type: HelicsFilterType, name: str) -> HelicsFilter
```

Create a source Filter on the specified core.
Filters can be created through a federate or a core, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

**Parameters**

* **core** - The core to register through.
* **type** - The type of filter to create `helics.helics_filter_type`.
* **name** - The name of the filter (can be NULL).

------

### helicsCoreSetGlobal {: #helicsCoreSetGlobal }

```python
def helicsCoreSetGlobal(core: HelicsCore, valueName: str, value: str)
```

Set a global value in a core.
This overwrites any previous value for this name.

**Parameters**

* **core** - The core to set the global through.
* **valueName** - The name of the global to set.
* **value** - The value of the global.

------

### helicsCoreSetLogFile {: #helicsCoreSetLogFile }

```python
def helicsCoreSetLogFile(core: HelicsCore, logFileName: str)
```

Set the log file on a core.

**Parameters**

* **core** - The core to set the log file for.
* **logFileName** - The name of the file to log to.

------

### helicsCoreSetReadyToInit {: #helicsCoreSetReadyToInit }

```python
def helicsCoreSetReadyToInit(core: HelicsCore)
```

Set the core to ready for init.
This function is used for cores that have filters but no federates so there needs to be a direct signal to the core to trigger the federation initialization.

**Parameters**

* **core** - The core object to enable init values for.

------

### helicsCoreWaitForDisconnect {: #helicsCoreWaitForDisconnect }

```python
def helicsCoreWaitForDisconnect(core: HelicsCore, msToWait: int) -> HelicsBool
```

Wait for the core to disconnect.

**Parameters**

* **core** - The core to wait for.
* **msToWait** - The time out in millisecond (<0 for infinite timeout).

------

### helicsCreateBroker {: #helicsCreateBroker }

```python
def helicsCreateBroker(type: str, name: str, initString: str) -> HelicsBroker
```

Create a broker object

**Parameters**

* **type** - The type of the broker to create.
* **name** - The name of the broker. It can be a nullptr or empty string to have a name automatically assigned.
* **initString** - An initialization string to send to the core-the format is similar to command line arguments. Typical options include a broker address such as --broker="XSSAF" if this is a subbroker, or the number of federates, or the address.

------

### helicsCreateBrokerFromArgs {: #helicsCreateBrokerFromArgs }

```python
def helicsCreateBrokerFromArgs(type: str, name: str, arguments: List[str]) -> HelicsBroker
```

Create a core object by passing command line arguments.

**Parameters**

* **type** - The type of the core to create.
* **name** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
* **arguments** - The list of string values from a command line.

------

### helicsCreateCombinationFederate {: #helicsCreateCombinationFederate }

```python
def helicsCreateCombinationFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate
```

Create a combination federate from a federate info object.
Combination federates are both value federates and message federates, objects can be used in all functions
that take a `helics.helics_federate`, `helics.helics_message_federate` or `helics.helics_federate` object as an argument

**Parameters**

* **fedName** - A string with the name of the federate, can be NULL or an empty string to pull the default name from fi.
* **fi** - The federate info object that contains details on the federate.

------

### helicsCreateCombinationFederateFromConfig {: #helicsCreateCombinationFederateFromConfig }

```python
def helicsCreateCombinationFederateFromConfig(configFile: str) -> HelicsFederate
```

Create a combination federate from a JSON file or JSON string or TOML file.
Combination federates are both value federates and message federates, objects can be used in all functions
         that take a `helics.helics_federate`, `helics.helics_message_federate` or `helics.helics_federate` object as an argument

**Parameters**

* **configFile** - A JSON file or a JSON string or TOML file that contains setup and configuration information.

------

### helicsCreateCore {: #helicsCreateCore }

```python
def helicsCreateCore(type: str, name: str, initString: str) -> HelicsCore
```

Create a core object

**Parameters**

* **type** - The type of the core to create.
* **name** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
* **initString** - An initialization string to send to the core. The format is similar to command line arguments. Typical options include a broker name, the broker address, the number of federates, etc.

------

### helicsCreateCoreFromArgs {: #helicsCreateCoreFromArgs }

```python
def helicsCreateCoreFromArgs(type: str, name: str, arguments: List[str]) -> HelicsCore
```

Create a core object by passing command line arguments.

**Parameters**

* **type** - The type of the core to create.
* **name** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
* **arguments** - The list of string values from a command line.

------

### helicsCreateFederateInfo {: #helicsCreateFederateInfo }

```python
def helicsCreateFederateInfo() -> HelicsFederateInfo
```

Create a federate info object for specifying federate information when constructing a federate.

**Returns**: A `helics.helics_federate_info` object which is a reference to the created object.

------

### helicsCreateMessageFederate {: #helicsCreateMessageFederate }

```python
def helicsCreateMessageFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate
```

Create a message federate from a federate info object.
`helics.helics_message_federate` objects can be used in all functions that take a `helics.helics_message_federate` or `helics.helics_federate` object as an argument.

**Parameters**

* **fedName** - The name of the federate to create.
* **fi** - The federate info object that contains details on the federate.

------

### helicsCreateMessageFederateFromConfig {: #helicsCreateMessageFederateFromConfig }

```python
def helicsCreateMessageFederateFromConfig(configFile: str) -> HelicsFederate
```

Create a message federate from a JSON file or JSON string or TOML file.
`helics.helics_message_federate` objects can be used in all functions that take a `helics.helics_message_federate` or `helics.helics_federate` object as an
argument

**Parameters**

* **configFile** - A config (JSON,TOML) file or a JSON string that contains setup and configuration information.

------

### helicsCreateQuery {: #helicsCreateQuery }

```python
def helicsCreateQuery(target: str, query: str) -> HelicsQuery
```

Create a query object.
A query object consists of a target and query string.

**Parameters**

* **target** - The name of the target to query.
* **query** - The query to make of the target.

------

### helicsCreateValueFederate {: #helicsCreateValueFederate }

```python
def helicsCreateValueFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate
```

Creation and destruction of Federates.
Create a value federate from a federate info object.
`helics.helics_federate` objects can be used in all functions that take a `helics.helics_federate` or `helics.helics_federate` object as an argument.

**Parameters**

* **fedName** - The name of the federate to create, can NULL or an empty string to use the default name from fi or an assigned name.
* **fi** - The federate info object that contains details on the federate.

------

### helicsCreateValueFederateFromConfig {: #helicsCreateValueFederateFromConfig }

```python
def helicsCreateValueFederateFromConfig(configFile: str) -> HelicsFederate
```

Create a value federate from a JSON file, JSON string, or TOML file.
`helics.helics_federate` objects can be used in all functions that take a `helics.helics_federate` or `helics.helics_federate` object as an argument.

**Parameters**

* **configFile** - A JSON file or a JSON string or TOML file that contains setup and configuration information.

------

### helicsEndpointClearMessages {: #helicsEndpointClearMessages }

```python
def helicsEndpointClearMessages(endpoint: HelicsEndpoint)
```

Clear all message from an endpoint.

_**Deprecated: Use [`helicsFederateClearMessages `](./#helicsFederateClearMessages) to free all messages, or [`helicsMessageFree `](./#helicsMessageFree) to clear an individual message.

**Parameters**

* **endpoint** - The endpoint object to operate on.

------

### helicsEndpointCreateMessageObject {: #helicsEndpointCreateMessageObject }

```python
def helicsEndpointCreateMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject
```

Create a new empty message object.
The message is empty and isValid will return false since there is no data associated with the message yet.

**Parameters**

* **endpoint** - The endpoint object to associate the message with.

------

### helicsEndpointGetDefaultDestination {: #helicsEndpointGetDefaultDestination }

```python
def helicsEndpointGetDefaultDestination(endpoint: HelicsEndpoint) -> str
```

Get the default destination for an endpoint.

**Parameters**

* **endpoint** - The endpoint to set the destination for.

**Returns**: A string with the default destination.

------

### helicsEndpointGetInfo {: #helicsEndpointGetInfo }

```python
def helicsEndpointGetInfo(endpoint: HelicsEndpoint) -> str
```

Get the data in the info field of a filter.

**Parameters**

* **end** - The filter to query.

**Returns**: A string with the info field string.

------

### helicsEndpointGetMessage {: #helicsEndpointGetMessage }

```python
def helicsEndpointGetMessage(endpoint: HelicsEndpoint) -> HelicsMessage
```

Receive a packet from a particular endpoint.

_**Deprecated: Use helicsEndpointGetMessageObject instead**_

**Parameters**

* **endpoint** - The identifier for the endpoint.

**Returns**: A message object.

------

### helicsEndpointGetMessageObject {: #helicsEndpointGetMessageObject }

```python
def helicsEndpointGetMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject
```

Receive a packet from a particular endpoint.

**Parameters**

* **endpoint** - The identifier for the endpoint.

**Returns**: A message object.

------

### helicsEndpointGetName {: #helicsEndpointGetName }

```python
def helicsEndpointGetName(endpoint: HelicsEndpoint) -> str
```

Get the name of an endpoint.

**Parameters**

* **endpoint** - The endpoint object in question.

**Returns**: The name of the endpoint.

------

### helicsEndpointGetOption {: #helicsEndpointGetOption }

```python
def helicsEndpointGetOption(endpoint: HelicsEndpoint, option: int) -> int
```

Set a handle option on an endpoint.

**Parameters**

* **end** - The endpoint to modify.
* **option** - Integer code for the option to set `helics.helics_handle_options`.

**Returns**: the value of the option, for boolean options will be 0 or 1.

------

### helicsEndpointGetType {: #helicsEndpointGetType }

```python
def helicsEndpointGetType(endpoint: HelicsEndpoint) -> str
```

Get the type specified for an endpoint.

**Parameters**

* **endpoint** - The endpoint object in question.

**Returns**: The defined type of the endpoint.

------

### helicsEndpointHasMessage {: #helicsEndpointHasMessage }

```python
def helicsEndpointHasMessage(endpoint: HelicsEndpoint) -> HelicsBool
```

Check if a given endpoint has any unread messages.

**Parameters**

* **endpoint** - The endpoint to check.

**Returns**: `True` if the endpoint has a message, `False` otherwise.

------

### helicsEndpointIsValid {: #helicsEndpointIsValid }

```python
def helicsEndpointIsValid(endpoint: HelicsEndpoint) -> HelicsBool
```

Check if an endpoint is valid.

**Parameters**

* **endpoint** - The endpoint object to check.

**Returns**: `True` if the Endpoint object represents a valid endpoint.

------

### helicsEndpointPendingMessages {: #helicsEndpointPendingMessages }

```python
def helicsEndpointPendingMessages(endpoint: HelicsEndpoint) -> int
```

Returns the number of pending receives for all endpoints of a particular federate.

**Parameters**

* **endpoint** - The endpoint to query.

------

### helicsEndpointSendEventRaw {: #helicsEndpointSendEventRaw }

```python
def helicsEndpointSendEventRaw(
    endpoint: HelicsEndpoint, dest: str, data: str, time: HelicsTime,
)
```

Send a message at a specific time to the specified destination.

**Parameters**

* **endpoint** - The endpoint to send the data from.
* **dest** - The target destination.
* **data** - The data to send.
* **time** - The time the message should be sent.

------

### helicsEndpointSendMessage {: #helicsEndpointSendMessage }

```python
def helicsEndpointSendMessage(endpoint: HelicsEndpoint, message: HelicsMessage)
```

Send a message object from a specific endpoint.

_**Deprecated: Use [`helicsEndpointSendMessageObject `](./#helicsEndpointSendMessageObject) instead.**_

**Parameters**

* **endpoint** - The endpoint to send the data from.
* **message** - The actual message to send.

------

### helicsEndpointSendMessageObject {: #helicsEndpointSendMessageObject }

```python
def helicsEndpointSendMessageObject(endpoint: HelicsEndpoint, message: HelicsMessageObject)
```

Send a message object from a specific endpoint.

**Parameters**

* **endpoint** - The endpoint to send the data from.
* **message** - The actual message to send which will be copied.

------

### helicsEndpointSendMessageObjectZeroCopy {: #helicsEndpointSendMessageObjectZeroCopy }

```python
def helicsEndpointSendMessageObjectZeroCopy(endpoint: HelicsEndpoint, message: HelicsMessageObject)
```

Send a message object from a specific endpoint, the message will not be copied and the message object will no longer be valid after the call.

**Parameters**

* **endpoint** - The endpoint to send the data from.
* **message** - The actual message to send which will be copied.

------

### helicsEndpointSendMessageRaw {: #helicsEndpointSendMessageRaw }

```python
def helicsEndpointSendMessageRaw(endpoint: HelicsEndpoint, dest: str, data: bytes)
```

Send a message to the specified destination.

**Parameters**

* **endpoint** - The endpoint to send the data from.
* **dest** - The target destination.
* **data** - The data to send.

------

### helicsEndpointSetDefaultDestination {: #helicsEndpointSetDefaultDestination }

```python
def helicsEndpointSetDefaultDestination(endpoint: HelicsEndpoint, dest: str)
```

Set the default destination for an endpoint if no other endpoint is given.

**Parameters**

* **endpoint** - The endpoint to set the destination for.
* **dest** - A string naming the desired default endpoint.

------

### helicsEndpointSetInfo {: #helicsEndpointSetInfo }

```python
def helicsEndpointSetInfo(endpoint: HelicsEndpoint, info: str)
```

Set the data in the info field for a filter.

**Parameters**

* **end** - The endpoint to query.
* **info** - The string to set.

------

### helicsEndpointSetOption {: #helicsEndpointSetOption }

```python
def helicsEndpointSetOption(endpoint: HelicsEndpoint, option: int, value: int)
```

Set a handle option on an endpoint.

**Parameters**

* **end** - The endpoint to modify.
* **option** - Integer code for the option to set `helics.helics_handle_options`.
* **value** - The value to set the option to.

------

### helicsEndpointSubscribe {: #helicsEndpointSubscribe }

```python
def helicsEndpointSubscribe(endpoint: HelicsEndpoint, key: str)
```

Subscribe an endpoint to a publication.

**Parameters**

* **endpoint** - The endpoint to use.
* **key** - The name of the publication.

------

### helicsErrorClear {: #helicsErrorClear }

```python
def helicsErrorClear(err: HelicsError)
```

Clear an error object.

------

### helicsErrorInitialize {: #helicsErrorInitialize }

```python
def helicsErrorInitialize() -> HelicsError
```

Return an initialized error object.

------

### helicsFederateAddDependency {: #helicsFederateAddDependency }

```python
def helicsFederateAddDependency(fed: HelicsFederate, fedName: str)
```

Add a time dependency for a federate. The federate will depend on the given named federate for time synchronization.

**Parameters**

* **fed** - The federate to add the dependency for.
* **fedName** - The name of the federate to depend on.

------

### helicsFederateClearMessages {: #helicsFederateClearMessages }

```python
def helicsFederateClearMessages(fed: HelicsFederate)
```

Clear all stored messages from a federate.
This clears messages retrieved through [`helicsFederateGetMessage `](./#helicsFederateGetMessage) or [`helicsFederateGetMessageObject `](./#helicsFederateGetMessageObject).

**Parameters**

* **fed** - The federate to clear the message for.

------

### helicsFederateClearUpdates {: #helicsFederateClearUpdates }

```python
def helicsFederateClearUpdates(fed: HelicsFederate)
```

Clear all the update flags from a federates inputs.

**Parameters**

* **fed** - The value federate object for which to clear update flags.

------

### helicsFederateClone {: #helicsFederateClone }

```python
def helicsFederateClone(fed: HelicsFederate) -> HelicsFederate
```

Create a new reference to an existing federate.
This will create a new `helics.helics_federate` object that references the existing federate. The new object must be freed as well.

**Parameters**

* **fed** - An existing helics_federate.

------

### helicsFederateCreateMessageObject {: #helicsFederateCreateMessageObject }

```python
def helicsFederateCreateMessageObject(fed: HelicsFederate) -> HelicsMessageObject
```

Create a new empty message object.
The message is empty and isValid will return false since there is no data associated with the message yet.

**Parameters**

* **fed** - the federate object to associate the message with.

------

### helicsFederateDestroy {: #helicsFederateDestroy }

```python
def helicsFederateDestroy(fed: HelicsFederate)
```

Disconnect and free a federate.

------

### helicsFederateEnterExecutingMode {: #helicsFederateEnterExecutingMode }

```python
def helicsFederateEnterExecutingMode(fed: HelicsFederate)
```

Request that the federate enter the Execution mode.
This call is blocking until granted entry by the core object. On return from this call the federate will be at time 0. For an asynchronous alternative call see [`helicsFederateEnterExecutingModeAsync `](./#helicsFederateEnterExecutingModeAsync)

**Parameters**

* **fed** - A federate to change modes.

------

### helicsFederateEnterExecutingModeAsync {: #helicsFederateEnterExecutingModeAsync }

```python
def helicsFederateEnterExecutingModeAsync(fed: HelicsFederate)
```

Request that the federate enter the Execution mode.
This call is non-blocking and will return immediately. Call [`helicsFederateEnterExecutingModeComplete `](./#helicsFederateEnterExecutingModeComplete) to finish the call sequence

**Parameters**

* **fed** - The federate object to complete the call.

------

### helicsFederateEnterExecutingModeComplete {: #helicsFederateEnterExecutingModeComplete }

```python
def helicsFederateEnterExecutingModeComplete(fed: HelicsFederate)
```

Complete the call to [`helicsFederateEnterExecutingModeAsync `](./#helicsFederateEnterExecutingModeAsync).

**Parameters**

* **fed** - The federate object to complete the call.

------

### helicsFederateEnterExecutingModeIterative {: #helicsFederateEnterExecutingModeIterative }

```python
def helicsFederateEnterExecutingModeIterative(fed: HelicsFederate, iterate: HelicsIterationRequest) -> HelicsIterationResult
```

Request an iterative time.
This call allows for finer grain control of the iterative process than [`helicsFederateRequestTime `](./#helicsFederateRequestTime). It takes a time and iteration request, and returns a time and iteration status.

**Parameters**

* **fed** - The federate to make the request of.
* **iterate** - The requested iteration mode.

------

### helicsFederateEnterExecutingModeIterativeAsync {: #helicsFederateEnterExecutingModeIterativeAsync }

```python
def helicsFederateEnterExecutingModeIterativeAsync(fed: HelicsFederate, iterate: HelicsIterationRequest)
```

Request an iterative entry to the execution mode.
This call allows for finer grain control of the iterative process than [`helicsFederateRequestTime `](./#helicsFederateRequestTime). It takes a time and iteration request, and returns a time and iteration status.

**Parameters**

* **fed** - The federate to make the request of.
* **iterate** - The requested iteration mode.

------

### helicsFederateEnterExecutingModeIterativeComplete {: #helicsFederateEnterExecutingModeIterativeComplete }

```python
def helicsFederateEnterExecutingModeIterativeComplete(fed: HelicsFederate,) -> HelicsIterationResult
```

Complete the asynchronous iterative call into ExecutionMode.

**Parameters**

* **fed** - The federate to make the request of.

------

### helicsFederateEnterInitializingMode {: #helicsFederateEnterInitializingMode }

```python
def helicsFederateEnterInitializingMode(fed: HelicsFederate)
```

Initialization, execution, and time requests.
Enter the initialization state of a federate.
The initialization state allows initial values to be set and received if the iteration is requested on entry to the execution state. This is a blocking call and will block until the core allows it to proceed.

**Parameters**

* **fed** - The federate to operate on.

------

### helicsFederateEnterInitializingModeAsync {: #helicsFederateEnterInitializingModeAsync }

```python
def helicsFederateEnterInitializingModeAsync(fed: HelicsFederate)
```

Non blocking alternative to `helics.helics.helicsFederateEnterInitializingMode`.
The function helicsFederateEnterInitializationModeFinalize must be called to finish the operation.

**Parameters**

* **fed** - The federate to operate on.

------

### helicsFederateEnterInitializingModeComplete {: #helicsFederateEnterInitializingModeComplete }

```python
def helicsFederateEnterInitializingModeComplete(fed: HelicsFederate)
```

Finalize the entry to initialize mode that was initiated with `helics.helicsEnterInitializingModeAsync`.

**Parameters**

* **fed** - The federate desiring to complete the initialization step.

------

### helicsFederateFinalize {: #helicsFederateFinalize }

```python
def helicsFederateFinalize(fed: HelicsFederate)
```

Finalize the federate. This function halts all communication in the federate and disconnects it from the core.

------

### helicsFederateFinalizeAsync {: #helicsFederateFinalizeAsync }

```python
def helicsFederateFinalizeAsync(fed: HelicsFederate)
```

Finalize the federate in an async call.

------

### helicsFederateFinalizeComplete {: #helicsFederateFinalizeComplete }

```python
def helicsFederateFinalizeComplete(fed: HelicsFederate)
```

Complete the asynchronous finalize call.

------

### helicsFederateFree {: #helicsFederateFree }

```python
def helicsFederateFree(fed: HelicsFederate)
```

Release the memory associated with a federate.

------

### helicsFederateGetCoreObject {: #helicsFederateGetCoreObject }

```python
def helicsFederateGetCoreObject(fed: HelicsFederate) -> HelicsCore
```

Get the core object associated with a federate.

**Parameters**

* **fed** - A federate object.

------

### helicsFederateGetCurrentTime {: #helicsFederateGetCurrentTime }

```python
def helicsFederateGetCurrentTime(fed: HelicsFederate) -> HelicsTime
```

Get the current time of the federate.

**Parameters**

* **fed** - The federate object to query.

------

### helicsFederateGetEndpoint {: #helicsFederateGetEndpoint }

```python
def helicsFederateGetEndpoint(fed: HelicsFederate, name: str) -> HelicsEndpoint
```

Get an endpoint object from a name.

**Parameters**

* **fed** - The message federate object to use to get the endpoint.
* **name** - The name of the endpoint.

------

### helicsFederateGetEndpointByIndex {: #helicsFederateGetEndpointByIndex }

```python
def helicsFederateGetEndpointByIndex(fed: HelicsFederate, index: int) -> HelicsEndpoint
```

Get an endpoint by its index, typically already created via registerInterfaces file or something of that nature.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **index** - The index of the publication to get.

------

### helicsFederateGetEndpointCount {: #helicsFederateGetEndpointCount }

```python
def helicsFederateGetEndpointCount(fed: HelicsFederate) -> int
```

Get the number of endpoints in a federate.

**Parameters**

* **fed** - The message federate to query.

**Returns**: (-1) if fed was not a valid federate, otherwise returns the number of endpoints.

------

### helicsFederateGetFilter {: #helicsFederateGetFilter }

```python
def helicsFederateGetFilter(fed: HelicsFederate, name: str) -> HelicsFilter
```

Get a filter by its name, typically already created via registerInterfaces file or something of that nature.

**Parameters**

* **fed** - The federate object to use to get the filter.
* **name** - The name of the filter.

**Returns**: A helics_filter object, the object will not be valid and err will contain an error code if no filter with the specified name exists.

------

### helicsFederateGetFilterByIndex {: #helicsFederateGetFilterByIndex }

```python
def helicsFederateGetFilterByIndex(fed: HelicsFederate, index: int) -> HelicsFilter
```

Get a filter by its index, typically already created via registerInterfaces file or something of that nature.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **index** - The index of the publication to get.

**Returns**: A helics_filter, which will be NULL if an invalid index is given.

------

### helicsFederateGetFilterCount {: #helicsFederateGetFilterCount }

```python
def helicsFederateGetFilterCount(fed: HelicsFederate) -> int
```

Get the number of filters registered through a federate.

**Parameters**

* **fed** - The federate object to use to get the filter.

**Returns**: A count of the number of filters registered through a federate.

------

### helicsFederateGetFlagOption {: #helicsFederateGetFlagOption }

```python
def helicsFederateGetFlagOption(fed: HelicsFederate, flag: int) -> HelicsBool
```

Get a flag value for a federate.

**Parameters**

* **fed** - The federate to get the flag for.
* **flag** - The flag to query.

------

### helicsFederateGetInput {: #helicsFederateGetInput }

```python
def helicsFederateGetInput(fed: HelicsFederate, key: str) -> HelicsInput
```

Get an input object from a key.

**Parameters**

* **fed** - The value federate object to use to get the publication.
* **key** - The name of the input.

**Returns**: A helics_input object, the object will not be valid and err will contain an error code if no input with the specified key exists.

------

### helicsFederateGetInputByIndex {: #helicsFederateGetInputByIndex }

```python
def helicsFederateGetInputByIndex(fed: HelicsFederate, index: int) -> HelicsInput
```

Get an input by its index, typically already created via registerInterfaces file or something of that nature.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **index** - The index of the publication to get.

**Returns**: A helics_input, which will be NULL if an invalid index.

------

### helicsFederateGetInputCount {: #helicsFederateGetInputCount }

```python
def helicsFederateGetInputCount(fed: HelicsFederate) -> int
```

Get the number of subscriptions in a federate.

**Returns**: (-1) if fed was not a valid federate otherwise returns the number of subscriptions.

------

### helicsFederateGetIntegerProperty {: #helicsFederateGetIntegerProperty }

```python
def helicsFederateGetIntegerProperty(fed: HelicsFederate, intProperty: int) -> int
```

Get the current value of an integer property (such as a logging level).

**Parameters**

* **fed** - The federate to get the flag for.
* **intProperty** - A code for the property to set `helics.helics_handle_options`.

------

### helicsFederateGetMessage {: #helicsFederateGetMessage }

```python
def helicsFederateGetMessage(fed: HelicsFederate) -> HelicsMessage
```

Receive a communication message for any endpoint in the federate.

_**Deprecated: Use helicsFederateGetMessageObject instead**_

The return order will be in order of endpoint creation. So all messages that are available for the first endpoint, then all for the second, and so on. Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival.

**Returns**: A unique_ptr to a Message object containing the message data.

------

### helicsFederateGetMessageObject {: #helicsFederateGetMessageObject }

```python
def helicsFederateGetMessageObject(fed: HelicsFederate) -> HelicsMessageObject
```

Receive a communication message for any endpoint in the federate.
The return order will be in order of endpoint creation.
So all messages that are available for the first endpoint, then all for the second, and so on.
Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival.

**Returns**: A `helics_message_object` which references the data in the message.

------

### helicsFederateGetName {: #helicsFederateGetName }

```python
def helicsFederateGetName(fed: HelicsFederate) -> str
```

Get the name of the federate.

**Parameters**

* **fed** - The federate object to query.

**Returns**: A pointer to a string with the name.

------

### helicsFederateGetPublication {: #helicsFederateGetPublication }

```python
def helicsFederateGetPublication(fed: HelicsFederate, key: str) -> HelicsPublication
```

Get a publication object from a key.

**Parameters**

* **fed** - The value federate object to use to get the publication.
* **key** - The name of the publication.

**Returns**: A helics_publication object, the object will not be valid and err will contain an error code if no publication with the specified key exists.

------

### helicsFederateGetPublicationByIndex {: #helicsFederateGetPublicationByIndex }

```python
def helicsFederateGetPublicationByIndex(fed: HelicsFederate, index: int) -> HelicsPublication
```

Get a publication by its index, typically already created via registerInterfaces file or something of that nature.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **index** - The index of the publication to get.

**Returns**: A helics_publication.

------

### helicsFederateGetPublicationCount {: #helicsFederateGetPublicationCount }

```python
def helicsFederateGetPublicationCount(fed: HelicsFederate) -> int
```

Get the number of publications in a federate.

**Returns**: (-1) if fed was not a valid federate otherwise returns the number of publications.

------

### helicsFederateGetState {: #helicsFederateGetState }

```python
def helicsFederateGetState(fed: HelicsFederate) -> HelicsFederateState
```

Get the current state of a federate.

**Parameters**

* **fed** - The federate to query.

------

### helicsFederateGetSubscription {: #helicsFederateGetSubscription }

```python
def helicsFederateGetSubscription(fed: HelicsFederate, key: str) -> HelicsInput
```

Get an input object from a subscription target.

**Parameters**

* **fed** - The value federate object to use to get the publication.
* **key** - The name of the publication that a subscription is targeting.

**Returns**: A helics_input object, the object will not be valid and err will contain an error code if no input with the specified key exists.

------

### helicsFederateGetTimeProperty {: #helicsFederateGetTimeProperty }

```python
def helicsFederateGetTimeProperty(fed: HelicsFederate, timeProperty: int) -> HelicsTime
```

Get the current value of a time based property in a federate.

**Parameters**

* **fed** - The federate query.
* **timeProperty** - The property to query.

------

### helicsFederateGlobalError {: #helicsFederateGlobalError }

```python
def helicsFederateGlobalError(fed: HelicsFederate, error_code: int, error_string: str)
```

Generate a global error from a federate.
A global error halts the co-simulation completely.

**Parameters**

* **fed** - The federate to create an error in.
* **error_code** - The integer code for the error.
* **error_string** - A string describing the error.

------

### helicsFederateHasMessage {: #helicsFederateHasMessage }

```python
def helicsFederateHasMessage(fed: HelicsFederate) -> HelicsBool
```

Check if the federate has any outstanding messages.

**Parameters**

* **fed** - The federate to check.

**Returns**: `True` if the federate has a message waiting, `False` otherwise.

------

### helicsFederateInfoClone {: #helicsFederateInfoClone }

```python
def helicsFederateInfoClone(fi: HelicsFederateInfo) -> HelicsFederateInfo
```

Create a federate info object from an existing one and clone the information.

**Parameters**

* **fi** - A federateInfo object to duplicate.

------

### helicsFederateInfoFree {: #helicsFederateInfoFree }

```python
def helicsFederateInfoFree(fi: HelicsFederateInfo)
```

Delete the memory associated with a federate info object.

------

### helicsFederateInfoLoadFromArgs {: #helicsFederateInfoLoadFromArgs }

```python
def helicsFederateInfoLoadFromArgs(fi: HelicsFederateInfo, arguments: List[str])
```

Load federate info from command line arguments.

**Parameters**

* **fi** - A federateInfo object.
* **argc** - The number of command line arguments.
* **argv** - An array of strings from the command line.

------

### helicsFederateInfoSetBroker {: #helicsFederateInfoSetBroker }

```python
def helicsFederateInfoSetBroker(fi: HelicsFederateInfo, broker: str)
```

Set the name or connection information for a broker.
This is only used if the core is automatically created, the broker information will be transferred to the core for connection.

**Parameters**

* **fi** - The federate info object to alter.
* **broker** - A string which defines the connection information for a broker either a name or an address.

------

### helicsFederateInfoSetBrokerInitString {: #helicsFederateInfoSetBrokerInitString }

```python
def helicsFederateInfoSetBrokerInitString(fi: HelicsFederateInfo, brokerInit: str)
```

Set the initialization string that a core will pass to a generated broker usually in the form of command line arguments.

**Parameters**

* **fi** - The federate info object to alter.
* **brokerInit** - A string with command line arguments for a generated broker.

------

### helicsFederateInfoSetBrokerKey {: #helicsFederateInfoSetBrokerKey }

```python
def helicsFederateInfoSetBrokerKey(fi: HelicsFederateInfo, brokerkey: str)
```

Set the key for a broker connection.
This is only used if the core is automatically created, the broker information will be transferred to the core for connection.

**Parameters**

* **fi** - The federate info object to alter.
* **brokerkey** - A string containing a key for the broker to connect.

------

### helicsFederateInfoSetBrokerPort {: #helicsFederateInfoSetBrokerPort }

```python
def helicsFederateInfoSetBrokerPort(fi: HelicsFederateInfo, brokerPort: int)
```

Set the port to use for the broker.
This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
This will only be useful for network broker connections.

**Parameters**

* **fi** - The federate info object to alter.
* **brokerPort** - The integer port number to use for connection with a broker.

------

### helicsFederateInfoSetCoreInitString {: #helicsFederateInfoSetCoreInitString }

```python
def helicsFederateInfoSetCoreInitString(fi: HelicsFederateInfo, coreInit: str)
```

Set the initialization string for the core usually in the form of command line arguments.

**Parameters**

* **fi** - The federate info object to alter.
* **coreInit** - A string containing command line arguments to be passed to the core.

------

### helicsFederateInfoSetCoreName {: #helicsFederateInfoSetCoreName }

```python
def helicsFederateInfoSetCoreName(fi: HelicsFederateInfo, corename: str)
```

Set the name of the core to link to for a federate.

**Parameters**

* **fi** - The federate info object to alter.
* **corename** - The identifier for a core to link to.

------

### helicsFederateInfoSetCoreType {: #helicsFederateInfoSetCoreType }

```python
def helicsFederateInfoSetCoreType(fi: HelicsFederateInfo, coretype: int)
```

Set the core type by integer code.
Valid values available by definitions in `api-data.h`.

**Parameters**

* **fi** - The federate info object to alter.
* **coretype** - An numerical code for a core type see `helics.helics_core_type`.

------

### helicsFederateInfoSetCoreTypeFromString {: #helicsFederateInfoSetCoreTypeFromString }

```python
def helicsFederateInfoSetCoreTypeFromString(fi: HelicsFederateInfo, coretype: str)
```

Set the core type from a string.

**Parameters**

* **fi** - The federate info object to alter.
* **coretype** - A string naming a core type.

------

### helicsFederateInfoSetFlagOption {: #helicsFederateInfoSetFlagOption }

```python
def helicsFederateInfoSetFlagOption(fi: HelicsFederateInfo, flag: int, value: HelicsBool)
```

Set a flag in the info structure
Valid flags are available `helics.helics.HELICS_FEDERATE_FLAGS`.

**Parameters**

* **fi** - The federate info object to alter.
* **flag** - A numerical index for a flag.
* **value** - The desired value of the flag `True` or `False`.

------

### helicsFederateInfoSetIntegerProperty {: #helicsFederateInfoSetIntegerProperty }

```python
def helicsFederateInfoSetIntegerProperty(fi: HelicsFederateInfo, intProperty: int, propertyValue: int)
```

Set an integer property for a federate.
Set known properties.

**Parameters**

* **fi** - The federateInfo object to alter.
* **intProperty** - An int identifying the property.
* **propertyValue** - The value to set the property to.

------

### helicsFederateInfoSetLocalPort {: #helicsFederateInfoSetLocalPort }

```python
def helicsFederateInfoSetLocalPort(fi: HelicsFederateInfo, localPort: str)
```

Set the local port to use.
This is only used if the core is automatically created, the port information will be transferred to the core for connection.

**Parameters**

* **fi** - The federate info object to alter.
* **localPort** - A string with the port information to use as the local server port can be a number or "auto" or "os_local".

------

### helicsFederateInfoSetSeparator {: #helicsFederateInfoSetSeparator }

```python
def helicsFederateInfoSetSeparator(fi: HelicsFederateInfo, separator: str)
```

Set the separator character in the info structure.
The separator character is the separation character for local publications/endpoints in creating their global name.
For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.

**Parameters**

* **fi** - The federate info object to alter.
* **separator** - The character to use as a separator.

------

### helicsFederateInfoSetTimeProperty {: #helicsFederateInfoSetTimeProperty }

```python
def helicsFederateInfoSetTimeProperty(fi: HelicsFederateInfo, timeProperty: int, propertyValue: HelicsTime)
```

Set the output delay for a federate.

**Parameters**

* **fi** - The federate info object to alter.
* **timeProperty** - An integer representation of the time based property to set see `helics.helics_properties`.
* **propertyValue** - The value of the property to set the timeProperty to.

------

### helicsFederateIsAsyncOperationCompleted {: #helicsFederateIsAsyncOperationCompleted }

```python
def helicsFederateIsAsyncOperationCompleted(fed: HelicsFederate) -> HelicsBool
```

Check if the current Asynchronous operation has completed.

**Parameters**

* **fed** - The federate to operate on.

------

### helicsFederateIsValid {: #helicsFederateIsValid }

```python
def helicsFederateIsValid(fed: HelicsFederate) -> HelicsBool
```

Check if a federate_object is valid.

**Returns**: `True` if the federate is a valid active federate, `False` otherwise.

------

### helicsFederateLocalError {: #helicsFederateLocalError }

```python
def helicsFederateLocalError(fed: HelicsFederate, error_code: int, error_string: str)
```

Generate a local error in a federate.
This will propagate through the co-simulation but not necessarily halt the co-simulation, it has a similar effect to finalize but does allow some interaction with a core for a brief time.

**Parameters**

* **fed** - The federate to create an error in.
* **error_code** - The integer code for the error.
* **error_string** - A string describing the error.

------

### helicsFederateLogDebugMessage {: #helicsFederateLogDebugMessage }

```python
def helicsFederateLogDebugMessage(fed: HelicsFederate, logmessage: str)
```

Log a debug message through a federate.

**Parameters**

* **fed** - The federate to log the debug message through.
* **logmessage** - The message to put in the log.

------

### helicsFederateLogErrorMessage {: #helicsFederateLogErrorMessage }

```python
def helicsFederateLogErrorMessage(fed: HelicsFederate, logmessage: str)
```

Log an error message through a federate.

**Parameters**

* **fed** - The federate to log the error message through.
* **logmessage** - The message to put in the log.

------

### helicsFederateLogInfoMessage {: #helicsFederateLogInfoMessage }

```python
def helicsFederateLogInfoMessage(fed: HelicsFederate, logmessage: str)
```

Log an info message through a federate.

**Parameters**

* **fed** - The federate to log the info message through.
* **logmessage** - The message to put in the log.

------

### helicsFederateLogLevelMessage {: #helicsFederateLogLevelMessage }

```python
def helicsFederateLogLevelMessage(fed: HelicsFederate, loglevel: int, logmessage: str)
```

Log a message through a federate.

**Parameters**

* **fed** - The federate to log the message through.
* **loglevel** - The level of the message to log see `helics.helics_log_levels`.
* **logmessage** - The message to put in the log.

------

### helicsFederateLogWarningMessage {: #helicsFederateLogWarningMessage }

```python
def helicsFederateLogWarningMessage(fed: HelicsFederate, logmessage: str)
```

Log a warning message through a federate.

**Parameters**

* **fed** - The federate to log the warning message through.
* **logmessage** - The message to put in the log.

------

### helicsFederatePendingMessages {: #helicsFederatePendingMessages }

```python
def helicsFederatePendingMessages(fed: HelicsFederate) -> int
```

Returns the number of pending receives for the specified destination endpoint.

**Parameters**

* **fed** - The federate to get the number of waiting messages from.

------

### helicsFederatePublishJSON {: #helicsFederatePublishJSON }

```python
def helicsFederatePublishJSON(fed: HelicsFederate, json: str)
```

Publish data contained in a JSON file or string.

**Parameters**

* **fed** - The value federate object through which to publish the data.
* **json** - The publication file name or literal JSON data string.

------

### helicsFederateRegisterCloningFilter {: #helicsFederateRegisterCloningFilter }

```python
def helicsFederateRegisterCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter
```

Create a cloning Filter on the specified federate.
Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

**Parameters**

* **fed** - The federate to register through.
* **name** - The name of the filter (can be NULL).

------

### helicsFederateRegisterEndpoint {: #helicsFederateRegisterEndpoint }

```python
def helicsFederateRegisterEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint
```

MessageFederate Calls.
Create an endpoint.
The endpoint becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for endpoints.

**Parameters**

* **fed** - The federate object in which to create an endpoint must have been created
          with helicsCreateMessageFederate or helicsCreateCombinationFederate.
* **name** - The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
* **type** - A string describing the expected type of the publication (may be NULL).

------

### helicsFederateRegisterFilter {: #helicsFederateRegisterFilter }

```python
def helicsFederateRegisterFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter
```

Create a source Filter on the specified federate.
Filters can be created through a federate or a core, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

**Parameters**

* **fed** - The federate to register through.
* **type** - The type of filter to create `helics.helics_filter_type`.
* **name** - The name of the filter (can be NULL).

------

### helicsFederateRegisterFromPublicationJSON {: #helicsFederateRegisterFromPublicationJSON }

```python
def helicsFederateRegisterFromPublicationJSON(fed: HelicsFederate, json: str)
```

Register the publications via JSON publication string.

**Parameters**

* **fed** - The value federate object to use to register the publications.
* **json** - The JSON publication string.

------

### helicsFederateRegisterGlobalCloningFilter {: #helicsFederateRegisterGlobalCloningFilter }

```python
def helicsFederateRegisterGlobalCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter
```

Create a global cloning Filter on the specified federate.
Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

**Parameters**

* **fed** - The federate to register through.
* **name** - The name of the filter (can be NULL).

------

### helicsFederateRegisterGlobalEndpoint {: #helicsFederateRegisterGlobalEndpoint }

```python
def helicsFederateRegisterGlobalEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint
```

Create an endpoint.
The endpoint becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for endpoints.

**Parameters**

* **fed** - The federate object in which to create an endpoint must have been created
       with helicsCreateMessageFederate or helicsCreateCombinationFederate.
* **name** - The identifier for the endpoint, the given name is the global identifier.
* **type** - A string describing the expected type of the publication (may be NULL).

**Returns**: An object containing the endpoint.

------

### helicsFederateRegisterGlobalFilter {: #helicsFederateRegisterGlobalFilter }

```python
def helicsFederateRegisterGlobalFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter
```

Create a global source filter through a federate.
Filters can be created through a federate or a core, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

**Parameters**

* **fed** - The federate to register through.
* **type** - The type of filter to create `helics.helics_filter_type`.
* **name** - The name of the filter (can be NULL).

------

### helicsFederateRegisterGlobalInput {: #helicsFederateRegisterGlobalInput }

```python
def helicsFederateRegisterGlobalInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication
```

Register a global named input.
The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **key** - The identifier for the publication.
* **type** - A code identifying the type of the input see `helics.helics_data_type` for available options.
* **units** - A string listing the units of the subscription maybe NULL.

**Returns**: An object containing the publication.

------

### helicsFederateRegisterGlobalPublication {: #helicsFederateRegisterGlobalPublication }

```python
def helicsFederateRegisterGlobalPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str = "") -> HelicsPublication
```

Register a global named publication with an arbitrary type.
The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **key** - The identifier for the publication.
* **type** - A code identifying the type of the input see `helics.helics_data_type` for available options.
* **units** - A string listing the units of the subscription (may be NULL).

**Returns**: An object containing the publication.

------

### helicsFederateRegisterGlobalTypeInput {: #helicsFederateRegisterGlobalTypeInput }

```python
def helicsFederateRegisterGlobalTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication
```

Register a global publication with an arbitrary type.
The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **key** - The identifier for the publication.
* **type** - A string defining the type of the input.
* **units** - A string listing the units of the subscription maybe NULL.

**Returns**: An object containing the publication.

------

### helicsFederateRegisterGlobalTypePublication {: #helicsFederateRegisterGlobalTypePublication }

```python
def helicsFederateRegisterGlobalTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication
```

Register a global publication with a defined type.
The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **key** - The identifier for the publication.
* **type** - A string describing the expected type of the publication.
* **units** - A string listing the units of the subscription (may be NULL).

**Returns**: An object containing the publication.

------

### helicsFederateRegisterInput {: #helicsFederateRegisterInput }

```python
def helicsFederateRegisterInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsInput
```

Register a named input.
The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
functions for subscriptions, inputs, and publications.

**Parameters**

* **fed** - The federate object in which to create an input.
* **key** - The identifier for the publication the global input key will be prepended with the federate name.
* **type** - A code identifying the type of the input see `helics.helics_data_type` for available options.
* **units** - A string listing the units of the input (may be NULL).

**Returns**: An object containing the input.

------

### helicsFederateRegisterInterfaces {: #helicsFederateRegisterInterfaces }

```python
def helicsFederateRegisterInterfaces(fed: HelicsFederate, file: str)
```

Load interfaces from a file.

**Parameters**

* **fed** - The federate to which to load interfaces.
* **file** - The name of a file to load the interfaces from either JSON, or TOML.

------

### helicsFederateRegisterPublication {: #helicsFederateRegisterPublication }

```python
def helicsFederateRegisterPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication
```

Register a publication with a known type.
The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **key** - The identifier for the publication the global publication key will be prepended with the federate name.
* **type** - A code identifying the type of the input see `helics.helics_data_type` for available options.
* **units** - A string listing the units of the subscription (may be NULL).

**Returns**: An object containing the publication.

------

### helicsFederateRegisterSubscription {: #helicsFederateRegisterSubscription }

```python
def helicsFederateRegisterSubscription(fed: HelicsFederate, key: str, units: str = "") -> HelicsInput
```

Functions related to value federates for the C api.
Create a subscription.
The subscription becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

**Parameters**

* **fed** - The federate object in which to create a subscription, must have been created with [`helicsCreateValueFederate `](./#helicsCreateValueFederate) or
[`helicsCreateCombinationFederate `](./#helicsCreateCombinationFederate).
* **key** - The identifier matching a publication to get a subscription for.
* **units** - A string listing the units of the subscription (may be NULL).

**Returns**: An object containing the subscription.

------

### helicsFederateRegisterTypeInput {: #helicsFederateRegisterTypeInput }

```python
def helicsFederateRegisterTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsInput
```

Register an input with a defined type.
The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
functions for subscriptions, inputs, and publications.

**Parameters**

* **fed** - The federate object in which to create an input.
* **key** - The identifier for the input.
* **type** - A string describing the expected type of the input.
* **units** - A string listing the units of the input maybe NULL.

**Returns**: An object containing the publication.

------

### helicsFederateRegisterTypePublication {: #helicsFederateRegisterTypePublication }

```python
def helicsFederateRegisterTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication
```

Register a publication with a defined type.
The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

**Parameters**

* **fed** - The federate object in which to create a publication.
* **key** - The identifier for the publication.
* **type** - A string labeling the type of the publication.
* **units** - A string listing the units of the subscription (may be NULL).

**Returns**: An object containing the publication.

------

### helicsFederateRequestNextStep {: #helicsFederateRequestNextStep }

```python
def helicsFederateRequestNextStep(fed: HelicsFederate) -> HelicsTime
```

Request the next time step for federate execution.
Feds should have setup the period or `minDelta` for this to work well but it will request the next time step which is the current time plus the minimum time step.

**Parameters**

* **fed** - The federate to make the request of.

------

### helicsFederateRequestTime {: #helicsFederateRequestTime }

```python
def helicsFederateRequestTime(fed: HelicsFederate, requestTime: HelicsTime) -> HelicsTime
```

Request the next time for federate execution.

**Parameters**

* **fed** - The federate to make the request of.
* **requestTime** - The next requested time.

------

### helicsFederateRequestTimeAdvance {: #helicsFederateRequestTimeAdvance }

```python
def helicsFederateRequestTimeAdvance(fed: HelicsFederate, timeDelta: HelicsTime) -> HelicsTime
```

Request the next time for federate execution.

**Parameters**

* **fed** - The federate to make the request of.
* **timeDelta** - The requested amount of time to advance.

------

### helicsFederateRequestTimeAsync {: #helicsFederateRequestTimeAsync }

```python
def helicsFederateRequestTimeAsync(fed: HelicsFederate, requestTime: HelicsTime)
```

Request the next time for federate execution in an asynchronous call.
Call [`helicsFederateRequestTimeComplete `](./#helicsFederateRequestTimeComplete) to finish the call.

**Parameters**

* **fed** - The federate to make the request of.
* **requestTime** - The next requested time.

------

### helicsFederateRequestTimeComplete {: #helicsFederateRequestTimeComplete }

```python
def helicsFederateRequestTimeComplete(fed: HelicsFederate) -> HelicsTime
```

Complete an asynchronous requestTime call.

**Parameters**

* **fed** - The federate to make the request of.

------

### helicsFederateRequestTimeIterative {: #helicsFederateRequestTimeIterative }

```python
def helicsFederateRequestTimeIterative(fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest) -> HelicsTime
```

Request an iterative time.
This call allows for finer grain control of the iterative process than [`helicsFederateRequestTime `](./#helicsFederateRequestTime). It takes a time and iteration request, and returns a time and iteration status.

**Parameters**

* **fed** - The federate to make the request of.
* **requestTime** - The next desired time.
* **iterate** - The requested iteration mode.

This function also returns the iteration specification of the result.

------

### helicsFederateRequestTimeIterativeAsync {: #helicsFederateRequestTimeIterativeAsync }

```python
def helicsFederateRequestTimeIterativeAsync(fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest)
```

Request an iterative time through an asynchronous call.
This call allows for finer grain control of the iterative process than [`helicsFederateRequestTime `](./#helicsFederateRequestTime). It takes a time and iteration request, and returns a time and iteration status. Call [`helicsFederateRequestTimeIterativeComplete `](./#helicsFederateRequestTimeIterativeComplete) to finish the process.

**Parameters**

* **fed** - The federate to make the request of.
* **requestTime** - The next desired time.
* **iterate** - The requested iteration mode.

------

### helicsFederateRequestTimeIterativeComplete {: #helicsFederateRequestTimeIterativeComplete }

```python
def helicsFederateRequestTimeIterativeComplete(fed: HelicsFederate) -> HelicsTime
```

Complete an iterative time request asynchronous call.

**Parameters**

* **fed** - The federate to make the request of.

**Returns**: The iteration specification of the result.

------

### helicsFederateSetFlagOption {: #helicsFederateSetFlagOption }

```python
def helicsFederateSetFlagOption(fed: HelicsFederate, flag: int, flagValue: HelicsBool)
```

Set a flag for the federate.

**Parameters**

* **fed** - The federate to alter a flag for.
* **flag** - The flag to change.
* **flagValue** - The new value of the flag. 0 for false, !=0 for true.

------

### helicsFederateSetGlobal {: #helicsFederateSetGlobal }

```python
def helicsFederateSetGlobal(fed: HelicsFederate, valueName: str, value: str)
```

Set a federation global value through a federate.
This overwrites any previous value for this name.

**Parameters**

* **fed** - The federate to set the global through.
* **valueName** - The name of the global to set.
* **value** - The value of the global.

------

### helicsFederateSetIntegerProperty {: #helicsFederateSetIntegerProperty }

```python
def helicsFederateSetIntegerProperty(fed: HelicsFederate, intProperty: int, propertyVal: int)
```

Set an integer based property of a federate.

**Parameters**

* **fed** - The federate to change the property for.
* **intProperty** - The property to set.
* **propertyVal** - The value of the property.

------

### helicsFederateSetLogFile {: #helicsFederateSetLogFile }

```python
def helicsFederateSetLogFile(fed: HelicsFederate, logFile: str)
```

Set the logging file for a federate (actually on the core associated with a federate).

**Parameters**

* **fed** - The federate to set the log file for.
* **logFile** - The name of the log file.

------

### helicsFederateSetSeparator {: #helicsFederateSetSeparator }

```python
def helicsFederateSetSeparator(fed: HelicsFederate, separator: str)
```

Set the separator character in a federate.
The separator character is the separation character for local publications/endpoints in creating their global name.
For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.

**Parameters**

* **fed** - The federate info object to alter.
* **separator** - The character to use as a separator.

------

### helicsFederateSetTimeProperty {: #helicsFederateSetTimeProperty }

```python
def helicsFederateSetTimeProperty(fed: HelicsFederate, timeProperty: int, time: HelicsTime)
```

Set a time based property for a federate.

**Parameters**

* **fed** - The federate object to set the property for.
* **timeProperty** - A integer code for a time property.
* **time** - The requested value of the property.

------

### helicsFilterAddDeliveryEndpoint {: #helicsFilterAddDeliveryEndpoint }

```python
def helicsFilterAddDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str)
```

Clone filter functions.
Functions that manipulate cloning filters in some way.
Add a delivery endpoint to a cloning filter.
All cloned messages are sent to the delivery address(es).

**Parameters**

* **filt** - The given filter.
* **deliveryEndpoint** - The name of the endpoint to deliver messages to.

------

### helicsFilterAddDestinationTarget {: #helicsFilterAddDestinationTarget }

```python
def helicsFilterAddDestinationTarget(filt: HelicsFilter, dest: str)
```

Add a destination target to a filter.
All messages going to a destination are copied to the delivery address(es).

**Parameters**

* **filt** - The given filter to add a destination target to.
* **dest** - The name of the endpoint to add as a destination target.

------

### helicsFilterAddSourceTarget {: #helicsFilterAddSourceTarget }

```python
def helicsFilterAddSourceTarget(filt: HelicsFilter, source: str)
```

Add a source target to a filter.
All messages coming from a source are copied to the delivery address(es).

**Parameters**

* **filt** - The given filter.
* **source** - The name of the endpoint to add as a source target.

------

### helicsFilterGetInfo {: #helicsFilterGetInfo }

```python
def helicsFilterGetInfo(filt: HelicsFilter) -> str
```

Get the data in the info field of a filter.

**Parameters**

* **filt** - The given filter.

**Returns**: A string with the info field string.

------

### helicsFilterGetName {: #helicsFilterGetName }

```python
def helicsFilterGetName(filt: HelicsFilter) -> str
```

Get the name of the filter and store in the given string.

**Parameters**

* **filt** - The given filter.

**Returns**: A string with the name of the filter.

------

### helicsFilterGetOption {: #helicsFilterGetOption }

```python
def helicsFilterGetOption(filt: HelicsFilter, option: int) -> int
```

Get a handle option for the filter

**Parameters**

* **filt** - The given filter to query.
* **option** - The option to query `helics.helics_handle_options`.

------

### helicsFilterIsValid {: #helicsFilterIsValid }

```python
def helicsFilterIsValid(filt: HelicsFilter) -> HelicsBool
```

Check if a filter is valid.

**Parameters**

* **filt** - The filter object to check.

**Returns**: `True` if the Filter object represents a valid filter.

------

### helicsFilterRemoveDeliveryEndpoint {: #helicsFilterRemoveDeliveryEndpoint }

```python
def helicsFilterRemoveDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str)
```

Remove a delivery destination from a cloning filter.

**Parameters**

* **filt** - The given filter (must be a cloning filter).
* **deliveryEndpoint** - A string with the delivery endpoint to remove.

------

### helicsFilterRemoveTarget {: #helicsFilterRemoveTarget }

```python
def helicsFilterRemoveTarget(filt: HelicsFilter, target: str)
```

Remove a destination target from a filter.

**Parameters**

* **filt** - The given filter.
* **target** - The named endpoint to remove as a target.

------

### helicsFilterSet {: #helicsFilterSet }

```python
def helicsFilterSet(filt: HelicsFilter, prop: str, val: float)
```

Set a property on a filter.

**Parameters**

* **filt** - The filter to modify.
* **prop** - A string containing the property to set.
* **val** - A numerical value for the property.

------

### helicsFilterSetInfo {: #helicsFilterSetInfo }

```python
def helicsFilterSetInfo(filt: HelicsFilter, info: str)
```

Set the data in the info field for a filter

**Parameters**

* **filt** - The given filter.
* **info** - The string to set.

------

### helicsFilterSetOption {: #helicsFilterSetOption }

```python
def helicsFilterSetOption(filt: HelicsFilter, option: int, value: int)
```

Set the data in the info field for a filter.

**Parameters**

* **filt** - The given filter.
* **option** - The option to set `helics.helics_handle_options`.
* **value** - The value of the option commonly 0 for false 1 for true.

------

### helicsFilterSetString {: #helicsFilterSetString }

```python
def helicsFilterSetString(filt: HelicsFilter, prop: str, val: str)
```

Set a string property on a filter.

**Parameters**

* **filt** - The filter to modify.
* **prop** - A string containing the property to set.
* **val** - A string containing the new value.

------

### helicsGetBuildFlags {: #helicsGetBuildFlags }

```python
def helicsGetBuildFlags() -> str
```

Get the build flags used to compile HELICS.

------

### helicsGetCompilerVersion {: #helicsGetCompilerVersion }

```python
def helicsGetCompilerVersion() -> str
```

Get the compiler version used to compile HELICS.

------

### helicsGetFederateByName {: #helicsGetFederateByName }

```python
def helicsGetFederateByName(fedName: str) -> HelicsFederate
```

Get an existing federate object from a core by name.
The federate must have been created by one of the other functions and at least one of the objects referencing the created federate must still be active in the process.

**Parameters**

* **fedName** - The name of the federate to retrieve.

------

### helicsGetFlagIndex {: #helicsGetFlagIndex }

```python
def helicsGetFlagIndex(val: str) -> int
```

Get a property index for use in [`helicsFederateInfoSetFlagOption `](./#helicsFederateInfoSetFlagOption), [`helicsFederateSetFlagOption `](./#helicsFederateSetFlagOption).

**Parameters**

* **val** - A string with the option name.

**Returns**: An int with the property code or (-1) if not a valid property.

------

### helicsGetOptionIndex {: #helicsGetOptionIndex }

```python
def helicsGetOptionIndex(val: str) -> int
```

Get an option index for use in [`helicsPublicationSetOption `](./#helicsPublicationSetOption), [`helicsInputSetOption `](./#helicsInputSetOption), [`helicsEndpointSetOption `](./#helicsEndpointSetOption),
[`helicsFilterSetOption `](./#helicsFilterSetOption), and the corresponding get functions

**Parameters**

* **val** - A string with the option name

**Returns**: An int with the option index or (-1) if not a valid property.

------

### helicsGetOptionValue {: #helicsGetOptionValue }

```python
def helicsGetOptionValue(val: str) -> int
```

Get an option value for use in [`helicsPublicationSetOption `](./#helicsPublicationSetOption), [`helicsInputSetOption `](./#helicsInputSetOption), [`helicsEndpointSetOption `](./#helicsEndpointSetOption),
[`helicsFilterSetOption `](./#helicsFilterSetOption).

**Parameters**

* **val** - A string representing the value

**Returns**: An int with the option value or (-1) if not a valid value.

------

### helicsGetPropertyIndex {: #helicsGetPropertyIndex }

```python
def helicsGetPropertyIndex(val: str) -> int
```

Get a property index for use in [`helicsFederateInfoSetFlagOption `](./#helicsFederateInfoSetFlagOption), [`helicsFederateInfoSetTimeProperty `](./#helicsFederateInfoSetTimeProperty),
or [`helicsFederateInfoSetIntegerProperty `](./#helicsFederateInfoSetIntegerProperty).

**Parameters**

* **val** - A string with the property name.

**Returns**: An int with the property code or (-1) if not a valid property.

------

### helicsGetVersion {: #helicsGetVersion }

```python
def helicsGetVersion() -> str
```

Get a version string for HELICS.

------

### helicsInputAddTarget {: #helicsInputAddTarget }

```python
def helicsInputAddTarget(ipt: HelicsInput, target: str)
```

Add a publication to the list of data that an input subscribes to.

**Parameters**

* **ipt** - The named input to modify.
* **target** - The name of a publication that an input should subscribe to.

------

### helicsInputClearUpdate {: #helicsInputClearUpdate }

```python
def helicsInputClearUpdate(ipt: HelicsInput)
```

Clear the updated flag from an input.

------

### helicsInputGetBoolean {: #helicsInputGetBoolean }

```python
def helicsInputGetBoolean(ipt: HelicsInput) -> HelicsBool
```

Get a boolean value from a subscription.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: A boolean value of current input value.

------

### helicsInputGetChar {: #helicsInputGetChar }

```python
def helicsInputGetChar(ipt: HelicsInput) -> str
```

Get a single character value from an input.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: The resulting character value.

------

### helicsInputGetComplex {: #helicsInputGetComplex }

```python
def helicsInputGetComplex(ipt: HelicsInput) -> complex
```

Get a pair of double forming a complex number from a subscriptions.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: a pair of floating point values that represent the real and imag values

------

### helicsInputGetComplexObject {: #helicsInputGetComplexObject }

```python
def helicsInputGetComplexObject(ipt: HelicsInput) -> complex
```

Get a complex object from an input object.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: A helics_complex structure with the value.

------

### helicsInputGetDouble {: #helicsInputGetDouble }

```python
def helicsInputGetDouble(ipt: HelicsInput) -> float
```

Get a double value from a subscription..

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: The double value of the input.

------

### helicsInputGetExtractionUnits {: #helicsInputGetExtractionUnits }

```python
def helicsInputGetExtractionUnits(ipt: HelicsInput) -> str
```

Get the units of an input.
The same as [`helicsInputGetUnits `](./#helicsInputGetUnits).

**Parameters**

* **ipt** - The input to query.

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsInputGetInfo {: #helicsInputGetInfo }

```python
def helicsInputGetInfo(inp: HelicsInput) -> str
```

Get the data in the info field of an input.

**Parameters**

* **inp** - The input to query.

**Returns**: A string with the info field string.

------

### helicsInputGetInjectionUnits {: #helicsInputGetInjectionUnits }

```python
def helicsInputGetInjectionUnits(ipt: HelicsInput) -> str
```

Get the units of the publication that an input is linked to.

**Parameters**

* **ipt** - The input to query.

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsInputGetInteger {: #helicsInputGetInteger }

```python
def helicsInputGetInteger(ipt: HelicsInput) -> int
```

Get an integer value from a subscription.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: An int64_t value with the current value of the input.

------

### helicsInputGetKey {: #helicsInputGetKey }

```python
def helicsInputGetKey(ipt: HelicsInput) -> str
```

Get the key of an input.

**Parameters**

* **ipt** - The input to query

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsInputGetNamedPoint {: #helicsInputGetNamedPoint }

```python
def helicsInputGetNamedPoint(ipt: HelicsInput)
```

Get a named point from a subscription.

**Parameters**

* **ipt** - The input to get the result for.

**Returns**: a string and a double value for the named point

------

### helicsInputGetOption {: #helicsInputGetOption }

```python
def helicsInputGetOption(inp: HelicsInput, option: int) -> int
```

Get the current value of an input handle option.

**Parameters**

* **inp** - The input to query.
* **option** - Integer representation of the option in question see `helics.helics_handle_options`.

**Returns**: An integer value with the current value of the given option.

------

### helicsInputGetPublicationType {: #helicsInputGetPublicationType }

```python
def helicsInputGetPublicationType(ipt: HelicsInput) -> str
```

Get the type the publisher to an input is sending.

**Parameters**

* **ipt** - The input to query

**Returns**: A const char * with the type name.

------

### helicsInputGetRawValue {: #helicsInputGetRawValue }

```python
def helicsInputGetRawValue(ipt: HelicsInput) -> str
```

Get the raw data for the latest value of a subscription.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: Raw string data.

------

### helicsInputGetRawValueSize {: #helicsInputGetRawValueSize }

```python
def helicsInputGetRawValueSize(ipt: HelicsInput) -> int
```

GetValue functions.
Data can be returned in a number of formats,  for instance if data is published as a double it can be returned as a string and vice versa,  not all translations make that much sense but they do work.
Get the size of the raw value for subscription.

**Returns**: The size of the raw data/string in bytes.

------

### helicsInputGetString {: #helicsInputGetString }

```python
def helicsInputGetString(ipt: HelicsInput) -> str
```

Get a string value from a subscription.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: A string data

------

### helicsInputGetStringSize {: #helicsInputGetStringSize }

```python
def helicsInputGetStringSize(ipt: HelicsInput) -> int
```

Get the size of a value for subscription assuming return as a string.

**Returns**: The size of the string.

------

### helicsInputGetTime {: #helicsInputGetTime }

```python
def helicsInputGetTime(ipt: HelicsInput) -> HelicsTime
```

Get a time value from a subscription.

**Parameters**

* **ipt** - The input to get the data for.

**Returns**: The resulting time value.

------

### helicsInputGetType {: #helicsInputGetType }

```python
def helicsInputGetType(ipt: HelicsInput) -> str
```

Get the type of an input.

**Parameters**

* **ipt** - The input to query

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsInputGetUnits {: #helicsInputGetUnits }

```python
def helicsInputGetUnits(ipt: HelicsInput) -> str
```

Get the units of an input.

**Parameters**

* **ipt** - The input to query.

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsInputGetVector {: #helicsInputGetVector }

```python
def helicsInputGetVector(ipt: HelicsInput) -> List[float]
```

Get a vector from a subscription.

**Parameters**

* **ipt** - The input to get the result for.

**Returns**: a list of floating point values

------

### helicsInputGetVectorSize {: #helicsInputGetVectorSize }

```python
def helicsInputGetVectorSize(ipt: HelicsInput) -> int
```

Get the size of a value for subscription assuming return as an array of doubles.

**Returns**: The number of doubles in a returned vector.

------

### helicsInputIsUpdated {: #helicsInputIsUpdated }

```python
def helicsInputIsUpdated(ipt: HelicsInput) -> HelicsBool
```

Check if a particular subscription was updated.

**Returns**: `True` if it has been updated since the last value retrieval.

------

### helicsInputIsValid {: #helicsInputIsValid }

```python
def helicsInputIsValid(ipt: HelicsInput) -> HelicsBool
```

Check if an input is valid.

**Parameters**

* **ipt** - The input to check

**Returns**: `True` if the Input object represents a valid input.

------

### helicsInputLastUpdateTime {: #helicsInputLastUpdateTime }

```python
def helicsInputLastUpdateTime(ipt: HelicsInput) -> HelicsTime
```

Get the last time a subscription was updated.

------

### helicsInputSetDefaultBoolean {: #helicsInputSetDefaultBoolean }

```python
def helicsInputSetDefaultBoolean(ipt: HelicsInput, val: HelicsBool)
```

Set the default as a boolean.

**Parameters**

* **ipt** - The input to set the default for.
* **val** - The default boolean value.

------

### helicsInputSetDefaultChar {: #helicsInputSetDefaultChar }

```python
def helicsInputSetDefaultChar(ipt: HelicsInput, val: str)
```

Set the default as a char.

**Parameters**

* **ipt** - The input to set the default for.
* **val** - The default char value.

------

### helicsInputSetDefaultComplex {: #helicsInputSetDefaultComplex }

```python
def helicsInputSetDefaultComplex(ipt: HelicsInput, c: complex)
```

Set the default as a complex number.

**Parameters**

* **ipt** - The input to set the default for.
* **real** - The default real value.
* **imag** - The default imaginary value.

------

### helicsInputSetDefaultDouble {: #helicsInputSetDefaultDouble }

```python
def helicsInputSetDefaultDouble(ipt: HelicsInput, val: float)
```

Set the default as a double.

**Parameters**

* **ipt** - The input to set the default for.
* **val** - The default double value.

------

### helicsInputSetDefaultInteger {: #helicsInputSetDefaultInteger }

```python
def helicsInputSetDefaultInteger(ipt: HelicsInput, val: int)
```

Set the default as an integer.

**Parameters**

* **ipt** - The input to set the default for.
* **val** - The default integer.

------

### helicsInputSetDefaultNamedPoint {: #helicsInputSetDefaultNamedPoint }

```python
def helicsInputSetDefaultNamedPoint(ipt: HelicsInput, str: str, val: float)
```

Set the default as a `NamedPoint`.

**Parameters**

* **ipt** - The input to set the default for.
* **str** - A pointer to a string representing the name.
* **val** - A double value for the value of the named point.

------

### helicsInputSetDefaultRaw {: #helicsInputSetDefaultRaw }

```python
def helicsInputSetDefaultRaw(ipt: HelicsInput, data: str)
```

Default Value functions.
These functions set the default value for a subscription. That is the value returned if nothing was published from elsewhere.
Set the default as a raw data array.

**Parameters**

* **ipt** - The input to set the default for.
* **data** - A pointer to the raw data to use for the default.

------

### helicsInputSetDefaultString {: #helicsInputSetDefaultString }

```python
def helicsInputSetDefaultString(ipt: HelicsInput, str: str)
```

Set the default as a string.

**Parameters**

* **ipt** - The input to set the default for.
* **str** - A pointer to the default string.

------

### helicsInputSetDefaultTime {: #helicsInputSetDefaultTime }

```python
def helicsInputSetDefaultTime(ipt: HelicsInput, val: HelicsTime)
```

Set the default as a time.

**Parameters**

* **ipt** - The input to set the default for.
* **val** - The default time value.

------

### helicsInputSetDefaultVector {: #helicsInputSetDefaultVector }

```python
def helicsInputSetDefaultVector(ipt: HelicsInput, vectorInput: List[float])
```

Set the default as a vector of doubles.

**Parameters**

* **ipt** - The input to set the default for.
* **vectorInput** - A pointer to an array of double data.
* **vectorLength** - The number of points to publish.

------

### helicsInputSetInfo {: #helicsInputSetInfo }

```python
def helicsInputSetInfo(inp: HelicsInput, info: str)
```

Set the data in the info field for an input.

**Parameters**

* **inp** - The input to query.
* **info** - The string to set.

------

### helicsInputSetMinimumChange {: #helicsInputSetMinimumChange }

```python
def helicsInputSetMinimumChange(inp: HelicsInput, tolerance: float)
```

Set the minimum change detection tolerance.

**Parameters**

* **inp** - The input to modify.
* **tolerance** - The tolerance level for registering an update, values changing less than this value will not show asbeing updated.

------

### helicsInputSetOption {: #helicsInputSetOption }

```python
def helicsInputSetOption(inp: HelicsInput, option: int, value: int)
```

Set an option on an input.

**Parameters**

* **inp** - The input to query.
* **option** - The option to set for the input `helics.helics_handle_options`.
* **value** - The value to set the option to.

------

### helicsIsCoreTypeAvailable {: #helicsIsCoreTypeAvailable }

```python
def helicsIsCoreTypeAvailable(type: str) -> HelicsBool
```

Returns true if core/broker type specified is available in current compilation.

**Parameters**

* **type** - A string representing a core type. Options include "zmq", "udp", "ipc", "interprocess", "tcp", "default", "mpi".

------

### helicsMessageAppendData {: #helicsMessageAppendData }

```python
def helicsMessageAppendData(message: HelicsMessageObject, data: pointer, inputDataLength: int)
```

Append data to the payload.

**Parameters**

* **message** - The message object in question.
* **data** - A string containing the message data to append.
* **inputDataLength** - The length of the data to input.

------

### helicsMessageCheckFlag {: #helicsMessageCheckFlag }

```python
def helicsMessageCheckFlag(message: HelicsMessageObject, flag: int) -> HelicsBool
```

Check if a flag is set on a message.

**Parameters**

* **message** - The message object in question.
* **flag** - The flag to check should be between [0,15].

**Returns**: The flags associated with a message.

------

### helicsMessageClearFlags {: #helicsMessageClearFlags }

```python
def helicsMessageClearFlags(message: HelicsMessageObject)
```

Clear the flags of a message.

**Parameters**

* **message** - The message object in question.

------

### helicsMessageClone {: #helicsMessageClone }

```python
def helicsMessageClone(message: HelicsMessageObject) -> HelicsMessageObject
```

Clone a message object.

**Parameters**

* **message** - The message object to copy from.

------

### helicsMessageCopy {: #helicsMessageCopy }

```python
def helicsMessageCopy(source_message: HelicsMessageObject, dest_message: HelicsMessageObject)
```

Copy a message object.

**Parameters**

* **source_message** - The message object to copy from.
* **dest_message** - The message object to copy to.

------

### helicsMessageFree {: #helicsMessageFree }

```python
def helicsMessageFree(message: HelicsMessageObject)
```

Free a message object from memory. Memory for message is managed so not using this function does not create memory leaks, this is an indication to the system that the memory for this message is done being used and can be reused for a new message.
[`helicsFederateClearMessages `](./#helicsFederateClearMessages) can also be used to clear up all stored messages at once.

------

### helicsMessageGetDestination {: #helicsMessageGetDestination }

```python
def helicsMessageGetDestination(message: HelicsMessageObject) -> str
```

Get the destination endpoint of a message.

**Parameters**

* **message** - The message object in question.

**Returns**: A string with the destination endpoint.

------

### helicsMessageGetMessageID {: #helicsMessageGetMessageID }

```python
def helicsMessageGetMessageID(message: HelicsMessageObject) -> int
```

Get the messageID of a message.

**Parameters**

* **message** - The message object in question.

**Returns**: The messageID.

------

### helicsMessageGetOriginalDestination {: #helicsMessageGetOriginalDestination }

```python
def helicsMessageGetOriginalDestination(message: HelicsMessageObject) -> str
```

Get the original destination endpoint of a message, the destination may have been modified by filters or other actions.

**Parameters**

* **message** - The message object in question.

**Returns**: A string with the original destination of a message.

------

### helicsMessageGetOriginalSource {: #helicsMessageGetOriginalSource }

```python
def helicsMessageGetOriginalSource(message: HelicsMessageObject) -> str
```

Get the original source endpoint of a message, the source may have been modified by filters or other actions.

**Parameters**

* **message** - The message object in question.

**Returns**: A string with the source of a message.

------

### helicsMessageGetRawData {: #helicsMessageGetRawData }

```python
def helicsMessageGetRawData(message: HelicsMessageObject)
```

Get the raw data for a message object.

**Parameters**

* **message** - A message object to get the data for.

**Returns**: Raw string data.

------

### helicsMessageGetRawDataPointer {: #helicsMessageGetRawDataPointer }

```python
def helicsMessageGetRawDataPointer(message: HelicsMessageObject) -> pointer
```

Get a pointer to the raw data of a message.

**Parameters**

* **message** - A message object to get the data for.

**Returns**: A pointer to the raw data in memory, the pointer may be NULL if the message is not a valid message.

------

### helicsMessageGetRawDataSize {: #helicsMessageGetRawDataSize }

```python
def helicsMessageGetRawDataSize(message: HelicsMessageObject) -> int
```

Get the size of the data payload in bytes.

**Parameters**

* **message** - The message object in question.

**Returns**: The size of the data payload.

------

### helicsMessageGetSource {: #helicsMessageGetSource }

```python
def helicsMessageGetSource(message: HelicsMessageObject) -> str
```

Message operation functions.
Functions for working with helics message envelopes.
Get the source endpoint of a message.

**Parameters**

* **message** - The message object in question.

**Returns**: A string with the source endpoint.

------

### helicsMessageGetString {: #helicsMessageGetString }

```python
def helicsMessageGetString(message: HelicsMessageObject) -> str
```

Get the payload of a message as a string.

**Parameters**

* **message** - The message object in question.

**Returns**: A string representing the payload of a message.

------

### helicsMessageGetTime {: #helicsMessageGetTime }

```python
def helicsMessageGetTime(message: HelicsMessageObject) -> HelicsTime
```

Get the helics time associated with a message.

**Parameters**

* **message** - The message object in question.

**Returns**: The time associated with a message.

------

### helicsMessageIsValid {: #helicsMessageIsValid }

```python
def helicsMessageIsValid(message: HelicsMessageObject) -> HelicsBool
```

A check if the message contains a valid payload.

**Parameters**

* **message** - The message object in question.

**Returns**: `True` if the message contains a payload.

------

### helicsMessageReserve {: #helicsMessageReserve }

```python
def helicsMessageReserve(message: HelicsMessageObject, reserveSize: int)
```

Reserve space in a buffer but don't actually resize.
The message data buffer will be reserved but not resized.

**Parameters**

* **message** - The message object in question.
* **reserveSize** - The number of bytes to reserve in the message object.

------

### helicsMessageResize {: #helicsMessageResize }

```python
def helicsMessageResize(message: HelicsMessageObject, newSize: int)
```

Resize the data buffer for a message.
The message data buffer will be resized. There are no guarantees on what is in the buffer in newly allocated space.
If the allocated space is not sufficient new allocations will occur

**Parameters**

* **message** - The message object in question.
* **newSize** - The new size in bytes of the buffer.

------

### helicsMessageSetData {: #helicsMessageSetData }

```python
def helicsMessageSetData(message: HelicsMessageObject, data: str)
```

Set the data payload of a message as raw data.

**Parameters**

* **message** - The message object in question.
* **data** - A string containing the message data.
* **inputDataLength** - The length of the data to input.

------

### helicsMessageSetDestination {: #helicsMessageSetDestination }

```python
def helicsMessageSetDestination(message: HelicsMessageObject, dest: str)
```

Set the destination of a message.

**Parameters**

* **message** - The message object in question.
* **dest** - A string containing the new destination.

------

### helicsMessageSetFlagOption {: #helicsMessageSetFlagOption }

```python
def helicsMessageSetFlagOption(message: HelicsMessageObject, flag: int, flagValue: HelicsBool)
```

Set a flag on a message.

**Parameters**

* **message** - The message object in question.
* **flag** - An index of a flag to set on the message.
* **flagValue** - The desired value of the flag.

------

### helicsMessageSetMessageID {: #helicsMessageSetMessageID }

```python
def helicsMessageSetMessageID(message: HelicsMessageObject, messageID: int)
```

Set the message ID for the message.
Normally this is not needed and the core of HELICS will adjust as needed.

**Parameters**

* **message** - The message object in question.
* **messageID** - A new message ID.

------

### helicsMessageSetOriginalDestination {: #helicsMessageSetOriginalDestination }

```python
def helicsMessageSetOriginalDestination(message: HelicsMessageObject, dest: str)
```

Set the original destination of a message.

**Parameters**

* **message** - The message object in question.
* **dest** - A string containing the new original source.

------

### helicsMessageSetOriginalSource {: #helicsMessageSetOriginalSource }

```python
def helicsMessageSetOriginalSource(message: HelicsMessageObject, src: str)
```

Set the original source of a message.

**Parameters**

* **message** - The message object in question.
* **src** - A string containing the new original source.

------

### helicsMessageSetSource {: #helicsMessageSetSource }

```python
def helicsMessageSetSource(message: HelicsMessageObject, src: str)
```

Set the source of a message.

**Parameters**

* **message** - The message object in question.
* **src** - A string containing the source.

------

### helicsMessageSetString {: #helicsMessageSetString }

```python
def helicsMessageSetString(message: HelicsMessageObject, str: str)
```

Set the data payload of a message as a string.

**Parameters**

* **message** - The message object in question.
* **str** - A string containing the message data.

------

### helicsMessageSetTime {: #helicsMessageSetTime }

```python
def helicsMessageSetTime(message: HelicsMessageObject, time: HelicsTime)
```

Set the delivery time for a message.

**Parameters**

* **message** - The message object in question.
* **time** - The time the message should be delivered.

------

### helicsPublicationAddTarget {: #helicsPublicationAddTarget }

```python
def helicsPublicationAddTarget(pub: HelicsPublication, target: str)
```

Add a named input to the list of targets a publication publishes to.

**Parameters**

* **pub** - The publication to add the target for.
* **target** - The name of an input that the data should be sent to.

------

### helicsPublicationGetInfo {: #helicsPublicationGetInfo }

```python
def helicsPublicationGetInfo(pub: HelicsPublication) -> str
```

Get the data in the info field of an publication.

**Parameters**

* **pub** - The publication to query.

**Returns**: A string with the info field string.

------

### helicsPublicationGetKey {: #helicsPublicationGetKey }

```python
def helicsPublicationGetKey(pub: HelicsPublication) -> str
```

Get the key of a publication.
This will be the global key used to identify the publication to the federation.

**Parameters**

* **pub** - The publication to query.

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsPublicationGetOption {: #helicsPublicationGetOption }

```python
def helicsPublicationGetOption(pub: HelicsPublication, option: int) -> int
```

Get the value of an option for a publication.

**Parameters**

* **pub** - The publication to query.
* **option** - The value to query see `helics.helics_handle_options`.

**Returns**: A string with the info field string.

------

### helicsPublicationGetType {: #helicsPublicationGetType }

```python
def helicsPublicationGetType(pub: HelicsPublication) -> str
```

Get the type of a publication.

**Parameters**

* **pub** - The publication to query

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsPublicationGetUnits {: #helicsPublicationGetUnits }

```python
def helicsPublicationGetUnits(pub: HelicsPublication) -> str
```

Get the units of a publication.

**Parameters**

* **pub** - The publication to query.

**Returns**: A void enumeration, helics_ok if everything worked.

------

### helicsPublicationIsValid {: #helicsPublicationIsValid }

```python
def helicsPublicationIsValid(pub: HelicsPublication) -> HelicsBool
```

Publication functions.
Functions for publishing data of various kinds.
The data will get translated to the type specified when the publication was constructed automatically regardless of the function used to publish the data.
Check if a publication is valid.

**Parameters**

* **pub** - The publication to check

**Returns**: `True` if the publication is a valid publication.

------

### helicsPublicationPublishBoolean {: #helicsPublicationPublishBoolean }

```python
def helicsPublicationPublishBoolean(pub: HelicsPublication, val: HelicsBool)
```

Publish a Boolean Value.

**Parameters**

* **pub** - The publication to publish for.
* **val** - The boolean value to publish.

------

### helicsPublicationPublishChar {: #helicsPublicationPublishChar }

```python
def helicsPublicationPublishChar(pub: HelicsPublication, val: str)
```

Publish a single character.

**Parameters**

* **pub** - The publication to publish for.
* **val** - The numerical value to publish.

------

### helicsPublicationPublishComplex {: #helicsPublicationPublishComplex }

```python
def helicsPublicationPublishComplex(pub: HelicsPublication, c: complex)
```

Publish a complex value (or pair of values).

**Parameters**

* **pub** - The publication to publish for.
* **real** - The real part of a complex number to publish.
* **imag** - The imaginary part of a complex number to publish.

------

### helicsPublicationPublishDouble {: #helicsPublicationPublishDouble }

```python
def helicsPublicationPublishDouble(pub: HelicsPublication, val: float)
```

Publish a double floating point value.

**Parameters**

* **pub** - The publication to publish for.
* **val** - The numerical value to publish.

------

### helicsPublicationPublishInteger {: #helicsPublicationPublishInteger }

```python
def helicsPublicationPublishInteger(pub: HelicsPublication, val: int)
```

Publish an integer value.

**Parameters**

* **pub** - The publication to publish for.
* **val** - The numerical value to publish.

------

### helicsPublicationPublishNamedPoint {: #helicsPublicationPublishNamedPoint }

```python
def helicsPublicationPublishNamedPoint(pub: HelicsPublication, str: str, val: float)
```

Publish a named point.

**Parameters**

* **pub** - The publication to publish for.
* **str** - A string for the name to publish.
* **val** - A double for the value to publish.

------

### helicsPublicationPublishRaw {: #helicsPublicationPublishRaw }

```python
def helicsPublicationPublishRaw(pub: HelicsPublication, data: pointer, inputDataLength: int)
```

Publish raw data from a char * and length.

**Parameters**

* **pub** - The publication to publish for.
* **data** - A pointer to the raw data.
* **inputDataLength** - The size in bytes of the data to publish.

------

### helicsPublicationPublishString {: #helicsPublicationPublishString }

```python
def helicsPublicationPublishString(pub: HelicsPublication, str: str)
```

Publish a string.

**Parameters**

* **pub** - The publication to publish for.
* **str** - The string to publish.

------

### helicsPublicationPublishTime {: #helicsPublicationPublishTime }

```python
def helicsPublicationPublishTime(pub: HelicsPublication, val: HelicsTime)
```

Publish a time value.

**Parameters**

* **pub** - The publication to publish for.
* **val** - The numerical value to publish.

------

### helicsPublicationPublishVector {: #helicsPublicationPublishVector }

```python
def helicsPublicationPublishVector(pub: HelicsPublication, vectorInput: List[float])
```

Publish a vector of doubles.

**Parameters**

* **pub** - The publication to publish for.
* **vectorInput** - A pointer to an array of double data.

------

### helicsPublicationSetInfo {: #helicsPublicationSetInfo }

```python
def helicsPublicationSetInfo(pub: HelicsPublication, info: str)
```

Set the data in the info field for a publication.

**Parameters**

* **pub** - The publication to set the info field for.
* **info** - The string to set.

------

### helicsPublicationSetMinimumChange {: #helicsPublicationSetMinimumChange }

```python
def helicsPublicationSetMinimumChange(pub: HelicsPublication, tolerance: float)
```

Set the minimum change detection tolerance.

**Parameters**

* **pub** - The publication to modify.
* **tolerance** - The tolerance level for publication, values changing less than this value will not be published.

------

### helicsPublicationSetOption {: #helicsPublicationSetOption }

```python
def helicsPublicationSetOption(pub: HelicsPublication, option: int, val: int)
```

Set the value of an option for a publication.

**Parameters**

* **pub** - The publication to query.
* **option** - Integer code for the option to set `helics.helics_handle_options`.
* **val** - The value to set the option to.

------

### helicsQueryBrokerExecute {: #helicsQueryBrokerExecute }

```python
def helicsQueryBrokerExecute(query: HelicsQuery, broker: HelicsBroker) -> str
```

Execute a query directly on a broker.
The call will block until the query finishes which may require communication or other delays.

**Parameters**

* **query** - The query object to use in the query.
* **broker** - The broker to send the query to.

------

### helicsQueryCoreExecute {: #helicsQueryCoreExecute }

```python
def helicsQueryCoreExecute(query: HelicsQuery, core: HelicsCore) -> str
```

Execute a query directly on a core.
The call will block until the query finishes which may require communication or other delays.

**Parameters**

* **query** - The query object to use in the query.
* **core** - The core to send the query to.

------

### helicsQueryExecute {: #helicsQueryExecute }

```python
def helicsQueryExecute(query: HelicsQuery, fed: HelicsFederate) -> str
```

Execute a query.
The call will block until the query finishes which may require communication or other delays.

**Parameters**

* **query** - The query object to use in the query.
* **fed** - A federate to send the query through.

------

### helicsQueryExecuteAsync {: #helicsQueryExecuteAsync }

```python
def helicsQueryExecuteAsync(query: HelicsQuery, fed: HelicsFederate)
```

Execute a query in a non-blocking call.

**Parameters**

* **query** - The query object to use in the query.
* **fed** - A federate to send the query through.

------

### helicsQueryExecuteComplete {: #helicsQueryExecuteComplete }

```python
def helicsQueryExecuteComplete(query: HelicsQuery) -> str
```

Complete the return from a query called with `helics.helicsExecuteQueryAsync`.
The function will block until the query completes `isQueryComplete` can be called to determine if a query has completed or not.

**Parameters**

* **query** - The query object to complete execution of.

------

### helicsQueryFree {: #helicsQueryFree }

```python
def helicsQueryFree(query: HelicsQuery)
```

Free the memory associated with a query object.

------

### helicsQueryIsCompleted {: #helicsQueryIsCompleted }

```python
def helicsQueryIsCompleted(query: HelicsQuery) -> HelicsBool
```

Check if an asynchronously executed query has completed.
This function should usually be called after a QueryExecuteAsync function has been called.

**Parameters**

* **query** - The query object to check if completed

**Returns**: Will return `True` if an asynchronous query has completed or a regular query call was made with a result, and false if an asynchronous query has not completed or is invalid.

------

### helicsQuerySetQueryString {: #helicsQuerySetQueryString }

```python
def helicsQuerySetQueryString(query: HelicsQuery, queryString: str)
```

Update the queryString of a query.

**Parameters**

* **query** - The query object to change the target of.
* **queryString** - the new queryString.

------

### helicsQuerySetTarget {: #helicsQuerySetTarget }

```python
def helicsQuerySetTarget(query: HelicsQuery, target: str)
```

Update the target of a query.

**Parameters**

* **query** - The query object to change the target of.
* **target** - the name of the target to query.

------

### helicsSubscriptionGetKey {: #helicsSubscriptionGetKey }

```python
def helicsSubscriptionGetKey(ipt: HelicsInput) -> str
```

Get the key of a subscription.

**Returns**: A const char with the subscription key.

------

### loadSym {: #loadSym }

```python
def loadSym(s)
```
