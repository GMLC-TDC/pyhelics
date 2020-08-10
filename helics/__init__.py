# -*- coding: utf-8 -*-
from typing import List

from . import _build

lib = _build.lib
ffi = _build.ffi

HELICS_CORE_TYPE_DEFAULT = 0  # HelicsCoreType
HELICS_CORE_TYPE_ZMQ = 1  # HelicsCoreType
HELICS_CORE_TYPE_MPI = 2  # HelicsCoreType
HELICS_CORE_TYPE_TEST = 3  # HelicsCoreType
HELICS_CORE_TYPE_INTERPROCESS = 4  # HelicsCoreType
HELICS_CORE_TYPE_IPC = 5  # HelicsCoreType
HELICS_CORE_TYPE_TCP = 6  # HelicsCoreType
HELICS_CORE_TYPE_UDP = 7  # HelicsCoreType
HELICS_CORE_TYPE_ZMQ_TEST = 10  # HelicsCoreType
HELICS_CORE_TYPE_NNG = 9  # HelicsCoreType
HELICS_CORE_TYPE_TCP_SS = 11  # HelicsCoreType
HELICS_CORE_TYPE_HTTP = 12  # HelicsCoreType
HELICS_CORE_TYPE_WEBSOCKET = 14  # HelicsCoreType
HELICS_CORE_TYPE_INPROC = 18  # HelicsCoreType
HELICS_CORE_TYPE_NULL = 66  # HelicsCoreType
HELICS_DATA_TYPE_STRING = 0  # HelicsDataType
HELICS_DATA_TYPE_DOUBLE = 1  # HelicsDataType
HELICS_DATA_TYPE_INT = 2  # HelicsDataType
HELICS_DATA_TYPE_COMPLEX = 3  # HelicsDataType
HELICS_DATA_TYPE_VECTOR = 4  # HelicsDataType
HELICS_DATA_TYPE_COMPLEX_VECTOR = 5  # HelicsDataType
HELICS_DATA_TYPE_NAMED_POINT = 6  # HelicsDataType
HELICS_DATA_TYPE_BOOLEAN = 7  # HelicsDataType
HELICS_DATA_TYPE_TIME = 8  # HelicsDataType
HELICS_DATA_TYPE_RAW = 25  # HelicsDataType
HELICS_DATA_TYPE_MULTI = 33  # HelicsDataType
HELICS_DATA_TYPE_ANY = 25262  # HelicsDataType
HELICS_FLAG_OBSERVER = 0  # HelicsFederateFlags
HELICS_FLAG_UNINTERRUPTIBLE = 1  # HelicsFederateFlags
HELICS_FLAG_INTERRUPTIBLE = 2  # HelicsFederateFlags
HELICS_FLAG_SOURCE_ONLY = 4  # HelicsFederateFlags
HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE = 6  # HelicsFederateFlags
HELICS_FLAG_ONLY_UPDATE_ON_CHANGE = 8  # HelicsFederateFlags
HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE = 10  # HelicsFederateFlags
HELICS_FLAG_RESTRICTIVE_TIME_POLICY = 11  # HelicsFederateFlags
HELICS_FLAG_ROLLBACK = 12  # HelicsFederateFlags
HELICS_FLAG_FORWARD_COMPUTE = 14  # HelicsFederateFlags
HELICS_FLAG_REALTIME = 16  # HelicsFederateFlags
HELICS_FLAG_SINGLE_THREAD_FEDERATE = 27  # HelicsFederateFlags
HELICS_FLAG_SLOW_RESPONDING = 29  # HelicsFederateFlags
HELICS_FLAG_DELAY_INIT_ENTRY = 45  # HelicsFederateFlags
HELICS_FLAG_ENABLE_INIT_ENTRY = 47  # HelicsFederateFlags
HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS = 67  # HelicsFederateFlags
HELICS_FLAG_TERMINATE_ON_ERROR = 72  # HelicsFederateFlags
HELICS_LOG_LEVEL_NO_PRINT = -1  # HelicsLogLevels
HELICS_LOG_LEVEL_ERROR = 0  # HelicsLogLevels
HELICS_LOG_LEVEL_WARNING = 1  # HelicsLogLevels
HELICS_LOG_LEVEL_SUMMARY = 2  # HelicsLogLevels
HELICS_LOG_LEVEL_CONNECTIONS = 3  # HelicsLogLevels
HELICS_LOG_LEVEL_INTERFACES = 4  # HelicsLogLevels
HELICS_LOG_LEVEL_TIMING = 5  # HelicsLogLevels
HELICS_LOG_LEVEL_DATA = 6  # HelicsLogLevels
HELICS_LOG_LEVEL_TRACE = 7  # HelicsLogLevels
HELICS_ERROR_FATAL = -404  # HelicsErrorTypes
HELICS_ERROR_EXTERNAL_TYPE = -203  # HelicsErrorTypes
HELICS_ERROR_OTHER = -101  # HelicsErrorTypes
HELICS_ERROR_INSUFFICIENT_SPACE = -18  # HelicsErrorTypes
HELICS_ERROR_EXECUTION_FAILURE = -14  # HelicsErrorTypes
HELICS_ERROR_INVALID_FUNCTION_CALL = -10  # HelicsErrorTypes
HELICS_ERROR_INVALID_STATE_TRANSITION = -9  # HelicsErrorTypes
HELICS_WARNING = -8  # HelicsErrorTypes
HELICS_ERROR_SYSTEM_FAILURE = -6  # HelicsErrorTypes
HELICS_ERROR_DISCARD = -5  # HelicsErrorTypes
HELICS_ERROR_INVALID_ARGUMENT = -4  # HelicsErrorTypes
HELICS_ERROR_INVALID_OBJECT = -3  # HelicsErrorTypes
HELICS_ERROR_CONNECTION_FAILURE = -2  # HelicsErrorTypes
HELICS_ERROR_REGISTRATION_FAILURE = -1  # HelicsErrorTypes
HELICS_OK = 0  # HelicsErrorTypes
HELICS_PROPERTY_TIME_DELTA = 137  # HelicsProperties
HELICS_PROPERTY_TIME_PERIOD = 140  # HelicsProperties
HELICS_PROPERTY_TIME_OFFSET = 141  # HelicsProperties
HELICS_PROPERTY_TIME_RT_LAG = 143  # HelicsProperties
HELICS_PROPERTY_TIME_RT_LEAD = 144  # HelicsProperties
HELICS_PROPERTY_TIME_RT_TOLERANCE = 145  # HelicsProperties
HELICS_PROPERTY_TIME_INPUT_DELAY = 148  # HelicsProperties
HELICS_PROPERTY_TIME_OUTPUT_DELAY = 150  # HelicsProperties
HELICS_PROPERTY_INT_MAX_ITERATIONS = 259  # HelicsProperties
HELICS_PROPERTY_INT_LOG_LEVEL = 271  # HelicsProperties
HELICS_PROPERTY_INT_FILE_LOG_LEVEL = 272  # HelicsProperties
HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL = 274  # HelicsProperties
HELICS_MULTI_INPUT_NO_OP = 0  # HelicsMultiInputMode
HELICS_MULTI_INPUT_VECTORIZE_OPERATION = 1  # HelicsMultiInputMode
HELICS_MULTI_INPUT_AND_OPERATION = 2  # HelicsMultiInputMode
HELICS_MULTI_INPUT_OR_OPERATION = 3  # HelicsMultiInputMode
HELICS_MULTI_INPUT_SUM_OPERATION = 4  # HelicsMultiInputMode
HELICS_MULTI_INPUT_DIFF_OPERATION = 5  # HelicsMultiInputMode
HELICS_MULTI_INPUT_MAX_OPERATION = 6  # HelicsMultiInputMode
HELICS_MULTI_INPUT_MIN_OPERATION = 7  # HelicsMultiInputMode
HELICS_MULTI_INPUT_AVERAGE_OPERATION = 8  # HelicsMultiInputMode
HELICS_HANDLE_OPTION_CONNECTION_REQUIRED = 397  # HelicsHandleOptions
HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL = 402  # HelicsHandleOptions
HELICS_HANDLE_OPTION_SINGLE_CONNECTION_ONLY = 407  # HelicsHandleOptions
HELICS_HANDLE_OPTION_MULTIPLE_CONNECTIONS_ALLOWED = 409  # HelicsHandleOptions
HELICS_HANDLE_OPTION_BUFFER_DATA = 411  # HelicsHandleOptions
HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING = 414  # HelicsHandleOptions
HELICS_HANDLE_OPTION_IGNORE_UNIT_MISMATCH = 447  # HelicsHandleOptions
HELICS_HANDLE_OPTION_ONLY_TRANSMIT_ON_CHANGE = 452  # HelicsHandleOptions
HELICS_HANDLE_OPTION_ONLY_UPDATE_ON_CHANGE = 454  # HelicsHandleOptions
HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS = 475  # HelicsHandleOptions
HELICS_HANDLE_OPTION_MULTI_INPUT_HANDLING_METHOD = 507  # HelicsHandleOptions
HELICS_HANDLE_OPTION_INPUT_PRIORITY_LOCATION = 510  # HelicsHandleOptions
HELICS_HANDLE_OPTION_CLEAR_PRIORITY_LIST = 512  # HelicsHandleOptions
HELICS_HANDLE_OPTION_CONNECTIONS = 522  # HelicsHandleOptions
HELICS_FILTER_TYPE_CUSTOM = 0  # HelicsFilterType
HELICS_FILTER_TYPE_DELAY = 1  # HelicsFilterType
HELICS_FILTER_TYPE_RANDOM_DELAY = 2  # HelicsFilterType
HELICS_FILTER_TYPE_RANDOM_DROP = 3  # HelicsFilterType
HELICS_FILTER_TYPE_REROUTE = 4  # HelicsFilterType
HELICS_FILTER_TYPE_CLONE = 5  # HelicsFilterType
HELICS_FILTER_TYPE_FIREWALL = 6  # HelicsFilterType
HELICS_ITERATION_REQUEST_NO_ITERATION = 0  # HelicsIterationRequest
HELICS_ITERATION_REQUEST_FORCE_ITERATION = 1  # HelicsIterationRequest
HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED = 2  # HelicsIterationRequest
HELICS_ITERATION_RESULT_NEXT_STEP = 0  # HelicsIterationResult
HELICS_ITERATION_RESULT_ERROR = 1  # HelicsIterationResult
HELICS_ITERATION_RESULT_HALTED = 2  # HelicsIterationResult
HELICS_ITERATION_RESULT_ITERATING = 3  # HelicsIterationResult
HELICS_STATE_STARTUP = 0  # HelicsFederateState
HELICS_STATE_INITIALIZATION = 1  # HelicsFederateState
HELICS_STATE_EXECUTION = 2  # HelicsFederateState
HELICS_STATE_FINALIZE = 3  # HelicsFederateState
HELICS_STATE_ERROR = 4  # HelicsFederateState
HELICS_STATE_PENDING_INIT = 5  # HelicsFederateState
HELICS_STATE_PENDING_EXEC = 6  # HelicsFederateState
HELICS_STATE_PENDING_TIME = 7  # HelicsFederateState
HELICS_STATE_PENDING_ITERATIVE_TIME = 8  # HelicsFederateState
HELICS_STATE_PENDING_FINALIZE = 9  # HelicsFederateState


HelicsBool = bool
HelicsError = bool
HelicsCore = object
HelicsBroker = object
HelicsFederate = object
HelicsFederateInfo = object
HelicsTime = float
HelicsIterationRequest = object
HelicsIterationResult = object
HelicsFederateState = object
HelicsQuery = object
HelicsEndpoint = object
pointer = float
HelicsMessage = object
HelicsMessageObject = object
HelicsFilterType = object
HelicsFilter = object
HelicsInput = object
HelicsDataType = object
HelicsPublication = object
HelicsComplex = object

"""
HELICS_CLOSE_ON_EXCEPTION: Global flag to close HELICS library when a Python HELICS exception occurs.

If you wish to manually handle closing the HELICS library, you can do the following:

>>> import helics as h
>>> h.HELICS_CLOSE_ON_EXCEPTION = False
"""
HELICS_CLOSE_ON_EXCEPTION = True


class HelicsException(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, *args, **kwargs):
        if HELICS_CLOSE_ON_EXCEPTION is True:
            helicsCloseLibrary()
        super(*args, **kwargs)


def cstring(s: str) -> str:
    """Convert python string to cstring"""
    return ffi.new("char[]", s.encode())


def cdouble(d: float) -> float:
    """Convert python float to cfloat"""
    return d


def cchar(c: str) -> str:
    """Convert python str to cchar"""
    return c.encode()


def loadSym(s):
    return getattr(lib, s)


def helicsGetVersion() -> str:
    """
    Get a version string for HELICS.
    """
    f = loadSym("helicsGetVersion")
    result = f()
    return ffi.string(result).decode()


def helicsGetBuildFlags() -> str:
    """
    Get the build flags used to compile HELICS.
    """
    f = loadSym("helicsGetBuildFlags")
    result = f()
    return ffi.string(result).decode()


def helicsGetCompilerVersion() -> str:
    """
    Get the compiler version used to compile HELICS.
    """
    f = loadSym("helicsGetCompilerVersion")
    result = f()
    return ffi.string(result).decode()


def helicsErrorInitialize() -> HelicsError:
    """
    Return an initialized error object.
    """
    f = loadSym("helicsErrorInitialize")
    result = f()
    return ffi.new("helics_error *", result)


def helicsErrorClear(err: HelicsError):
    """
    Clear an error object.
    """
    f = loadSym("helicsErrorClear")
    f(err)


def helicsIsCoreTypeAvailable(type: str) -> HelicsBool:
    """
    Returns true if core/broker type specified is available in current compilation
    @param type A string representing a core type
    @details Options include "zmq", "udp", "ipc", "interprocess", "tcp", "default", "mpi".
    """
    f = loadSym("helicsIsCoreTypeAvailable")
    result = f(cstring(type))
    return result == 1


def helicsCreateCore(type: str, name: str, initString: str) -> HelicsCore:
    """
    Create a core object
    @param type The type of the core to create.
    @param name The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    @param initString An initialization string to send to the core. The format is similar to command line arguments.
                      Typical options include a broker name, the broker address, the number of federates, etc.
    """
    f = loadSym("helicsCreateCore")
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), cstring(initString), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateCoreFromArgs(type: str, name: str, arguments: List[str]) -> HelicsCore:
    """
    Create a core object by passing command line arguments
    @param type The type of the core to create.
    @param name The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    @param arguments The list of string values from a command line.
    """
    f = loadSym("helicsCreateCoreFromArgs")
    argc = len(arguments)
    argv = ffi.new(f"char*[{argc}]")
    for i, s in enumerate(arguments):
        argv[i] = cstring(s)
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), argc, argv, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCoreClone(core: HelicsCore) -> HelicsCore:
    """
    Create a new reference to an existing core
    @details This will create a new broker object that references the existing broker. The new broker object must be freed as well
    @param core An existing helics_core.
    """
    f = loadSym("helicsCoreClone")
    err = helicsErrorInitialize()
    result = f(core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCoreIsValid(core: HelicsCore) -> HelicsBool:
    """
    Check if a core object is a valid object
    @param core The helics_core object to test.
    """
    f = loadSym("helicsCoreIsValid")
    result = f(core)
    return result == 1


def helicsCreateBroker(type: str, name: str, initString: str) -> HelicsBroker:
    """
    Create a broker object
    @param type The type of the broker to create.
    @param name The name of the broker. It can be a nullptr or empty string to have a name automatically assigned.
    @param initString An initialization string to send to the core-the format is similar to command line arguments.
                      Typical options include a broker address such as --broker="XSSAF" if this is a subbroker, or the number of federates,
    or the address.
    """
    f = loadSym("helicsCreateBroker")
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), cstring(initString), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateBrokerFromArgs(type: str, name: str, arguments: List[str]) -> HelicsBroker:
    """
    Create a core object by passing command line arguments
    @param type The type of the core to create.
    @param name The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    @param arguments The list of string values from a command line.
    """
    f = loadSym("helicsCreateBrokerFromArgs")
    argc = len(arguments)
    argv = ffi.new(f"char*[{argc}]")
    for i, s in enumerate(arguments):
        argv[i] = cstring(s)
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), argc, argv, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsBrokerClone(broker: HelicsBroker) -> HelicsBroker:
    """
    Create a new reference to an existing broker
    @details This will create a new broker object that references the existing broker it must be freed as well
    @param broker An existing helics_broker.
    """
    f = loadSym("helicsBrokerClone")
    err = helicsErrorInitialize()
    result = f(broker, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsBrokerIsValid(broker: HelicsBroker) -> HelicsBool:
    """
    Check if a broker object is a valid object
    @param broker The helics_broker object to test.
    """
    f = loadSym("helicsBrokerIsValid")
    result = f(broker)
    return result == 1


def helicsBrokerIsConnected(broker: HelicsBroker) -> HelicsBool:
    """
    Check if a broker is connected
    @details A connected broker implies it is attached to cores or cores could reach out to communicate
    @return helics_false if not connected.
    """
    f = loadSym("helicsBrokerIsConnected")
    result = f(broker)
    return result == 1


def helicsBrokerDataLink(broker: HelicsBroker, source: str, target: str):
    """
    Link a named publication and named input using a broker
    @param broker The broker to generate the connection from.
    @param source The name of the publication (cannot be NULL).
    @param target The name of the target to send the publication data (cannot be NULL).
    """
    f = loadSym("helicsBrokerDataLink")
    err = helicsErrorInitialize()
    f(broker, cstring(source), cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddSourceFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
    """
    Link a named filter to a source endpoint
    @param broker The broker to generate the connection from.
    @param filter The name of the filter (cannot be NULL).
    @param endpoint The name of the endpoint to filter the data from (cannot be NULL).
    """
    f = loadSym("helicsBrokerAddSourceFilterToEndpoint")
    err = helicsErrorInitialize()
    f(broker, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddDestinationFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
    """
    Link a named filter to a destination endpoint
    @param broker The broker to generate the connection from.
    @param filter The name of the filter (cannot be NULL).
    @param endpoint The name of the endpoint to filter the data going to (cannot be NULL).
    """
    f = loadSym("helicsBrokerAddDestinationFilterToEndpoint")
    err = helicsErrorInitialize()
    f(broker, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerMakeConnections(broker: HelicsBroker, file: str):
    """
    Load a file containing connection information
    @param broker The broker to generate the connections from.
    @param file A JSON or TOML file containing connection information.
    """
    f = loadSym("helicsBrokerMakeConnections")
    err = helicsErrorInitialize()
    f(broker, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreWaitForDisconnect(core: HelicsCore, msToWait: int) -> HelicsBool:
    """
    Wait for the core to disconnect
    @param core The core to wait for.
    @param msToWait The time out in millisecond (<0 for infinite timeout).
    """
    f = loadSym("helicsCoreWaitForDisconnect")
    err = helicsErrorInitialize()
    result = f(core, msToWait, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsBrokerWaitForDisconnect(broker: HelicsBroker, msToWait: int) -> HelicsBool:
    """
    Wait for the broker to disconnect
    @param broker The broker to wait for.
    @param msToWait The time out in millisecond (<0 for infinite timeout).
    """
    f = loadSym("helicsBrokerWaitForDisconnect")
    err = helicsErrorInitialize()
    result = f(broker, msToWait, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsCoreIsConnected(core: HelicsCore) -> HelicsBool:
    """
    Check if a core is connected
    @details A connected core implies it is attached to federates or federates could be attached to it    @return helics_false if not connected, helics_true if it is connected.
    """
    f = loadSym("helicsCoreIsConnected")
    result = f(core)
    return result == 1


def helicsCoreDataLink(core: HelicsCore, source: str, target: str):
    """
    Link a named publication and named input using a core
    @param core The core to generate the connection from.
    @param source The name of the publication (cannot be NULL).
    @param target The name of the target to send the publication data (cannot be NULL).
    """
    f = loadSym("helicsCoreDataLink")
    err = helicsErrorInitialize()
    f(core, cstring(source), cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddSourceFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
    """
    Link a named filter to a source endpoint
    @param core The core to generate the connection from.
    @param filter The name of the filter (cannot be NULL).
    @param endpoint The name of the endpoint to filter the data from (cannot be NULL).
    """
    f = loadSym("helicsCoreAddSourceFilterToEndpoint")
    err = helicsErrorInitialize()
    f(core, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddDestinationFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
    """
    Link a named filter to a destination endpoint
    @param core The core to generate the connection from.
    @param filter The name of the filter (cannot be NULL).
    @param endpoint The name of the endpoint to filter the data going to (cannot be NULL).
    """
    f = loadSym("helicsCoreAddDestinationFilterToEndpoint")
    err = helicsErrorInitialize()
    f(core, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreMakeConnections(core: HelicsCore, file: str):
    """
    Load a file containing connection information
    @param core The core to generate the connections from.
    @param file A JSON or TOML file containing connection information.
    """
    f = loadSym("helicsCoreMakeConnections")
    err = helicsErrorInitialize()
    f(core, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerGetIdentifier(broker: HelicsBroker) -> str:
    """
    Get an identifier for the broker
    @param broker The broker to query
    @return A string containing the identifier for the broker.
    """
    f = loadSym("helicsBrokerGetIdentifier")
    result = f(broker)
    return ffi.string(result).decode()


def helicsCoreGetIdentifier(core: HelicsCore) -> str:
    """
    Get an identifier for the core
    @param core The core to query
    @return A string with the identifier of the core.
    """
    f = loadSym("helicsCoreGetIdentifier")
    result = f(core)
    return ffi.string(result).decode()


def helicsBrokerGetAddress(broker: HelicsBroker) -> str:
    """
    Get the network address associated with a broker
    @param broker The broker to query
    @return A string with the network address of the broker.
    """
    f = loadSym("helicsBrokerGetAddress")
    result = f(broker)
    return ffi.string(result).decode()


def helicsCoreGetAddress(core: HelicsCore) -> str:
    """
    Get the network address associated with a core
    @param core The core to query
    @return A string with the network address of the broker.
    """
    f = loadSym("helicsCoreGetAddress")
    result = f(core)
    return ffi.string(result).decode()


def helicsCoreSetReadyToInit(core: HelicsCore):
    """
    Set the core to ready for init
    @details This function is used for cores that have filters but no federates so there needs to be
             a direct signal to the core to trigger the federation initialization
    @param core The core object to enable init values for.
    """
    f = loadSym("helicsCoreSetReadyToInit")
    err = helicsErrorInitialize()
    f(core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreConnect(core: HelicsCore) -> HelicsBool:
    """
    Connect a core to the federate based on current configuration
    @param core The core to connect.
    """
    f = loadSym("helicsCoreConnect")
    err = helicsErrorInitialize()
    result = f(core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsCoreDisconnect(core: HelicsCore):
    """
    Disconnect a core from the federation
    @param core The core to query.
    """
    f = loadSym("helicsCoreDisconnect")
    err = helicsErrorInitialize()
    f(core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetFederateByName(fedName: str) -> HelicsFederate:
    """
    Get an existing federate object from a core by name
    @details The federate must have been created by one of the other functions and at least one of the objects referencing the created
             federate must still be active in the process
    @param fedName The name of the federate to retrieve.
    """
    f = loadSym("helicsGetFederateByName")
    err = helicsErrorInitialize()
    result = f(cstring(fedName), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsBrokerDisconnect(broker: HelicsBroker):
    """
    Disconnect a broker
    @param broker The broker to disconnect.
    """
    f = loadSym("helicsBrokerDisconnect")
    err = helicsErrorInitialize()
    f(broker, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateDestroy(fed: HelicsFederate):
    """
    Disconnect and free a federate.
    """
    f = loadSym("helicsFederateDestroy")
    f(fed)


def helicsBrokerDestroy(broker: HelicsBroker):
    """
    Disconnect and free a broker.
    """
    f = loadSym("helicsBrokerDestroy")
    f(broker)


def helicsCoreDestroy(core: HelicsCore):
    """
    Disconnect and free a core.
    """
    f = loadSym("helicsCoreDestroy")
    f(core)


def helicsCoreFree(core: HelicsCore):
    """
    Release the memory associated with a core.
    """
    f = loadSym("helicsCoreFree")
    f(core)


def helicsBrokerFree(broker: HelicsBroker):
    """
    Release the memory associated with a broker.
    """
    f = loadSym("helicsBrokerFree")
    f(broker)


def helicsCreateValueFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
    """
    Creation and destruction of Federates.
    Create a value federate from a federate info object
    @details helics_federate objects can be used in all functions that take a helics_federate or helics_federate object as an argument
    @param fedName The name of the federate to create, can NULL or an empty string to use the default name from fi or an assigned name.
    @param fi The federate info object that contains details on the federate.
    """
    f = loadSym("helicsCreateValueFederate")
    err = helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateValueFederateFromConfig(configFile: str) -> HelicsFederate:
    """
    Create a value federate from a JSON file, JSON string, or TOML file
    @details helics_federate objects can be used in all functions that take a helics_federate or helics_federate object as an argument
    @param configFile A JSON file or a JSON string or TOML file that contains setup and configuration information.
    """
    f = loadSym("helicsCreateValueFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateMessageFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
    """
    Create a message federate from a federate info object
    @details helics_message_federate objects can be used in all functions that take a helics_message_federate or helics_federate object as an
    argument
    @param fedName The name of the federate to create.
    @param fi The federate info object that contains details on the federate.
    """
    f = loadSym("helicsCreateMessageFederate")
    err = helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateMessageFederateFromConfig(configFile: str) -> HelicsFederate:
    """
    Create a message federate from a JSON file or JSON string or TOML file
    @details helics_message_federate objects can be used in all functions that take a helics_message_federate or helics_federate object as an
    argument
    @param configFile A Config(JSON,TOML) file or a JSON string that contains setup and configuration information.
    """
    f = loadSym("helicsCreateMessageFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateCombinationFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
    """
    Create a combination federate from a federate info object
    @details Combination federates are both value federates and message federates, objects can be used in all functions
                         that take a helics_federate, helics_message_federate or helics_federate object as an argument    @param fedName A string with the name of the federate, can be NULL or an empty string to pull the default name from fi.
    @param fi The federate info object that contains details on the federate.
    """
    f = loadSym("helicsCreateCombinationFederate")
    err = helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateCombinationFederateFromConfig(configFile: str) -> HelicsFederate:
    """
    Create a combination federate from a JSON file or JSON string or TOML file
    @details Combination federates are both value federates and message federates, objects can be used in all functions
             that take a helics_federate, helics_message_federate or helics_federate object as an argument    @param configFile A JSON file or a JSON string or TOML file that contains setup and configuration information.
    """
    f = loadSym("helicsCreateCombinationFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateClone(fed: HelicsFederate) -> HelicsFederate:
    """
    Create a new reference to an existing federate
    @details This will create a new helics_federate object that references the existing federate. The new object must be freed as well
    @param fed An existing helics_federate.
    """
    f = loadSym("helicsFederateClone")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateFederateInfo() -> HelicsFederateInfo:
    """
    Create a federate info object for specifying federate information when constructing a federate
    @return A helics_federate_info object which is a reference to the created object.
    """
    f = loadSym("helicsCreateFederateInfo")
    result = f()
    return result


def helicsFederateInfoClone(fi: HelicsFederateInfo) -> HelicsFederateInfo:
    """
    Create a federate info object from an existing one and clone the information
    @param fi A federateInfo object to duplicate.
    """
    f = loadSym("helicsFederateInfoClone")
    err = helicsErrorInitialize()
    result = f(fi, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateInfoLoadFromArgs(fi: HelicsFederateInfo, arguments: List[str]):
    """
    Load federate info from command line arguments.
    @param fi A federateInfo object.
    @param argc The number of command line arguments.
    @param argv An array of strings from the command line.
    """
    f = loadSym("helicsFederateInfoLoadFromArgs")
    err = helicsErrorInitialize()
    argc = len(arguments)
    argv = ffi.new(f"char*[{argc}]")
    for i, s in enumerate(arguments):
        argv[i] = cstring(s)
    f(fi, argc, argv, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoFree(fi: HelicsFederateInfo):
    """
    Delete the memory associated with a federate info object.
    """
    f = loadSym("helicsFederateInfoFree")
    f(fi)


def helicsFederateIsValid(fed: HelicsFederate) -> HelicsBool:
    """
    Check if a federate_object is valid
    @return helics_true if the federate is a valid active federate, helics_false otherwise
    """
    f = loadSym("helicsFederateIsValid")
    result = f(fed)
    return result == 1


def helicsFederateInfoSetCoreName(fi: HelicsFederateInfo, corename: str):
    """
    Set the name of the core to link to for a federate
    @param fi The federate info object to alter.
    @param corename The identifier for a core to link to.
    """
    f = loadSym("helicsFederateInfoSetCoreName")
    err = helicsErrorInitialize()
    f(fi, cstring(corename), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreInitString(fi: HelicsFederateInfo, coreInit: str):
    """
    Set the initialization string for the core usually in the form of command line arguments
    @param fi The federate info object to alter.
    @param coreInit A string containing command line arguments to be passed to the core.
    """
    f = loadSym("helicsFederateInfoSetCoreInitString")
    err = helicsErrorInitialize()
    f(fi, cstring(coreInit), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerInitString(fi: HelicsFederateInfo, brokerInit: str):
    """
    Set the initialization string that a core will pass to a generated broker usually in the form of command line arguments
    @param fi The federate info object to alter.
    @param brokerInit A string with command line arguments for a generated broker.
    """
    f = loadSym("helicsFederateInfoSetBrokerInitString")
    err = helicsErrorInitialize()
    f(fi, cstring(brokerInit), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreType(fi: HelicsFederateInfo, coretype: int):
    """
    Set the core type by integer code
    @details Valid values available by definitions in api-data.h.
    @param fi The federate info object to alter.
    @param coretype An numerical code for a core type see /ref helics_core_type.
    """
    f = loadSym("helicsFederateInfoSetCoreType")
    err = helicsErrorInitialize()
    f(fi, coretype, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreTypeFromString(fi: HelicsFederateInfo, coretype: str):
    """
    Set the core type from a string
    @param fi The federate info object to alter.
    @param coretype A string naming a core type.
    """
    f = loadSym("helicsFederateInfoSetCoreTypeFromString")
    err = helicsErrorInitialize()
    f(fi, cstring(coretype), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBroker(fi: HelicsFederateInfo, broker: str):
    """
    Set the name or connection information for a broker
    @details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
    @param fi The federate info object to alter.
    @param broker A string which defines the connection information for a broker either a name or an address.
    """
    f = loadSym("helicsFederateInfoSetBroker")
    err = helicsErrorInitialize()
    f(fi, cstring(broker), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerKey(fi: HelicsFederateInfo, brokerkey: str):
    """
    Set the key for a broker connection
    @details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
    @param fi The federate info object to alter.
    @param brokerkey A string containing a key for the broker to connect.
    """
    f = loadSym("helicsFederateInfoSetBrokerKey")
    err = helicsErrorInitialize()
    f(fi, cstring(brokerkey), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerPort(fi: HelicsFederateInfo, brokerPort: int):
    """
    Set the port to use for the broker
    @details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
    This will only be useful for network broker connections.
    @param fi The federate info object to alter.
    @param brokerPort The integer port number to use for connection with a broker.
    """
    f = loadSym("helicsFederateInfoSetBrokerPort")
    err = helicsErrorInitialize()
    f(fi, brokerPort, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetLocalPort(fi: HelicsFederateInfo, localPort: str):
    """
    Set the local port to use
    @details This is only used if the core is automatically created, the port information will be transferred to the core for connection.
    @param fi The federate info object to alter.
    @param localPort A string with the port information to use as the local server port can be a number or "auto" or "os_local".
    """
    f = loadSym("helicsFederateInfoSetLocalPort")
    err = helicsErrorInitialize()
    f(fi, cstring(localPort), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetPropertyIndex(val: str) -> int:
    """
    Get a property index for use in /ref helicsFederateInfoSetFlagOption, /ref helicsFederateInfoSetTimeProperty,
    or /ref helicsFederateInfoSetIntegerProperty
    @param val A string with the property name.
    @return An int with the property code or (-1) if not a valid property.
    """
    f = loadSym("helicsGetPropertyIndex")
    return f(cstring(val))


def helicsGetFlagIndex(val: str) -> int:
    """
    Get a property index for use in /ref helicsFederateInfoSetFlagOption, /ref helicsFederateSetFlagOption,
    @param val A string with the option name.
    @return An int with the property code or (-1) if not a valid property.
    """
    f = loadSym("helicsGetFlagIndex")
    return f(cstring(val))


def helicsGetOptionIndex(val: str) -> int:
    """
    Get an option index for use in /ref helicsPublicationSetOption, /ref helicsInputSetOption, /ref helicsEndpointSetOption,
    /ref helicsFilterSetOption, and the corresponding get functions
    @param val A string with the option name
    @return An int with the option index or (-1) if not a valid property.
    """
    f = loadSym("helicsGetOptionIndex")
    return f(cstring(val))


def helicsGetOptionValue(val: str) -> int:
    """
    Get an option value for use in /ref helicsPublicationSetOption, /ref helicsInputSetOption, /ref helicsEndpointSetOption,
    /ref helicsFilterSetOption
    @param val A string representing the value
    @return An int with the option value or (-1) if not a valid value.
    """
    f = loadSym("helicsGetOptionValue")
    return f(cstring(val))


def helicsFederateInfoSetFlagOption(fi: HelicsFederateInfo, flag: int, value: HelicsBool):
    """
    Set a flag in the info structure
    @details Valid flags are available /ref helics_federate_flags.
    @param fi The federate info object to alter.
    @param flag A numerical index for a flag.
    @param value The desired value of the flag helics_true or helics_false.
    """
    f = loadSym("helicsFederateInfoSetFlagOption")
    err = helicsErrorInitialize()
    f(fi, flag, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetSeparator(fi: HelicsFederateInfo, separator: str):
    """
    Set the separator character in the info structure
    @details The separator character is the separation character for local publications/endpoints in creating their global name.
    For example if the separator character is '/'  then a local endpoint would have a globally reachable name of fedName/localName.
    @param fi The federate info object to alter.
    @param separator The character to use as a separator.
    """
    f = loadSym("helicsFederateInfoSetSeparator")
    err = helicsErrorInitialize()
    f(fi, cchar(separator), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetTimeProperty(fi: HelicsFederateInfo, timeProperty: int, propertyValue: HelicsTime):
    """
    Set the output delay for a federate
    @param fi The federate info object to alter.
    @param timeProperty An integer representation of the time based property to set see /ref helics_properties.
    @param propertyValue The value of the property to set the timeProperty to.
    """
    f = loadSym("helicsFederateInfoSetTimeProperty")
    err = helicsErrorInitialize()
    f(fi, timeProperty, propertyValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetIntegerProperty(fi: HelicsFederateInfo, intProperty: int, propertyValue: int):
    """
    Set an integer property for a federate
    @details Set known properties
    @param fi The federateInfo object to alter.
    @param intProperty An int identifying the property.
    @param propertyValue The value to set the property to.
    """
    f = loadSym("helicsFederateInfoSetIntegerProperty")
    err = helicsErrorInitialize()
    f(fi, intProperty, propertyValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRegisterInterfaces(fed: HelicsFederate, file: str):
    """
    Load interfaces from a file
    @param fed The federate to which to load interfaces.
    @param file The name of a file to load the interfaces from either JSON, or TOML.
    """
    f = loadSym("helicsFederateRegisterInterfaces")
    err = helicsErrorInitialize()
    f(fed, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGlobalError(fed: HelicsFederate, error_code: int, error_string: str):
    """
    Generate a global error from a federate
    @details A global error halts the co-simulation completely
    @param fed The federate to create an error in.
    @param error_code The integer code for the error.
    @param error_string A string describing the error.
    """
    f = loadSym("helicsFederateGlobalError")
    f(fed, error_code, cstring(error_string))


def helicsFederateLocalError(fed: HelicsFederate, error_code: int, error_string: str):
    """
    Generate a local error in a federate
    @details This will propagate through the co-simulation but not necessarily halt the co-simulation, it has a similar effect to finalize
    but does allow some interaction with a core for a brief time.
    @param fed The federate to create an error in.
    @param error_code The integer code for the error.
    @param error_string A string describing the error.
    """
    f = loadSym("helicsFederateLocalError")
    f(fed, error_code, cstring(error_string))


def helicsFederateFinalize(fed: HelicsFederate):
    """
    Finalize the federate. This function halts all communication in the federate and disconnects it from the core.
    """
    f = loadSym("helicsFederateFinalize")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFinalizeAsync(fed: HelicsFederate):
    """
    Finalize the federate in an async call.
    """
    f = loadSym("helicsFederateFinalizeAsync")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFinalizeComplete(fed: HelicsFederate):
    """
    Complete the asynchronous finalize call.
    """
    f = loadSym("helicsFederateFinalizeComplete")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFree(fed: HelicsFederate):
    """
    Release the memory associated with a federate.
    """
    f = loadSym("helicsFederateFree")
    f(fed)


def helicsCloseLibrary():
    """
    Call when done using the helics library.
    This function will ensure the threads are closed properly. If possible this should be the last call before exiting.
    """
    f = loadSym("helicsCloseLibrary")
    f()


def helicsFederateEnterInitializingMode(fed: HelicsFederate):
    """
    Initialization, execution, and time requests.
    Enter the initialization state of a federate
    @details The initialization state allows initial values to be set and received if the iteration is requested on entry to the execution
    state. This is a blocking call and will block until the core allows it to proceed
    @param fed The federate to operate on.
    """
    f = loadSym("helicsFederateEnterInitializingMode")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterInitializingModeAsync(fed: HelicsFederate):
    """
    Non blocking alternative to \ref helicsFederateEnterInitializingMode
    @details The function helicsFederateEnterInitializationModeFinalize must be called to finish the operation
    @param fed The federate to operate on.
    """
    f = loadSym("helicsFederateEnterInitializingModeAsync")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateIsAsyncOperationCompleted(fed: HelicsFederate) -> HelicsBool:
    """
    Check if the current Asynchronous operation has completed
    @param fed The federate to operate on.
    """
    f = loadSym("helicsFederateIsAsyncOperationCompleted")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsFederateEnterInitializingModeComplete(fed: HelicsFederate):
    """
    Finalize the entry to initialize mode that was initiated with /ref heliceEnterInitializingModeAsync
    @param fed The federate desiring to complete the initialization step.
    """
    f = loadSym("helicsFederateEnterInitializingModeComplete")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingMode(fed: HelicsFederate):
    """
    Request that the federate enter the Execution mode
    @details This call is blocking until granted entry by the core object. On return from this call the federate will be at time 0.
             For an asynchronous alternative call see /ref helicsFederateEnterExecutingModeAsync
    @param fed A federate to change modes.
    """
    f = loadSym("helicsFederateEnterExecutingMode")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeAsync(fed: HelicsFederate):
    """
    Request that the federate enter the Execution mode
    @details This call is non-blocking and will return immediately. Call /ref helicsFederateEnterExecutingModeComplete to finish the call
    sequence
    @param fed The federate object to complete the call.
    """
    f = loadSym("helicsFederateEnterExecutingModeAsync")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeComplete(fed: HelicsFederate):
    """
    Complete the call to /ref helicsFederateEnterExecutingModeAsync
    @param fed The federate object to complete the call.
    """
    f = loadSym("helicsFederateEnterExecutingModeComplete")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterative(fed: HelicsFederate, iterate: HelicsIterationRequest) -> HelicsIterationResult:
    """
    Request an iterative time
    @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
             iteration request, and returns a time and iteration status
    @param fed The federate to make the request of.
    @param iterate The requested iteration mode.
    """
    f = loadSym("helicsFederateEnterExecutingModeIterative")
    err = helicsErrorInitialize()
    result = f(fed, iterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateEnterExecutingModeIterativeAsync(fed: HelicsFederate, iterate: HelicsIterationRequest):
    """
    Request an iterative entry to the execution mode
    @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
             iteration request, and returns a time and iteration status    @param fed The federate to make the request of.
    @param iterate The requested iteration mode.
    """
    f = loadSym("helicsFederateEnterExecutingModeIterativeAsync")
    err = helicsErrorInitialize()
    f(fed, iterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterativeComplete(fed: HelicsFederate,) -> HelicsIterationResult:
    """
    Complete the asynchronous iterative call into ExecutionMode
    @param fed The federate to make the request of.
    """
    f = loadSym("helicsFederateEnterExecutingModeIterativeComplete")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetState(fed: HelicsFederate) -> HelicsFederateState:
    """
    Get the current state of a federate
    @param fed The federate to query.
    """
    f = loadSym("helicsFederateGetState")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetCoreObject(fed: HelicsFederate) -> HelicsCore:
    """
    Get the core object associated with a federate
    @param fed A federate object.
    """
    f = loadSym("helicsFederateGetCoreObject")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTime(fed: HelicsFederate, requestTime: HelicsTime) -> HelicsTime:
    """
    Request the next time for federate execution
    @param fed The federate to make the request of.
    @param requestTime The next requested time.
    """
    f = loadSym("helicsFederateRequestTime")
    err = helicsErrorInitialize()
    result = f(fed, requestTime, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTimeAdvance(fed: HelicsFederate, timeDelta: HelicsTime) -> HelicsTime:
    """
    Request the next time for federate execution
    @param fed The federate to make the request of.
    @param timeDelta The requested amount of time to advance.
    """
    f = loadSym("helicsFederateRequestTimeAdvance")
    err = helicsErrorInitialize()
    result = f(fed, timeDelta, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestNextStep(fed: HelicsFederate) -> HelicsTime:
    """
    Request the next time step for federate execution
    @details Feds should have setup the period or minDelta for this to work well but it will request the next time step which is the current
    time plus the minimum time step
    @param fed The federate to make the request of.
    """
    f = loadSym("helicsFederateRequestNextStep")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTimeIterative(fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest) -> HelicsTime:
    """
    Request an iterative time
    @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
    iteration request, and returns a time and iteration status
    @param fed The federate to make the request of.
    @param requestTime The next desired time.
    @param iterate The requested iteration mode.
    @beginPythonOnly
    This function also returns the iteration specification of the result.
    @endPythonOnly
    """
    f = loadSym("helicsFederateRequestTimeIterative")
    err = helicsErrorInitialize()
    outIteration = ffi.new("helics_iteration_result *")
    result = f(fed, requestTime, iterate, outIteration, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result, outIteration


def helicsFederateRequestTimeAsync(fed: HelicsFederate, requestTime: HelicsTime):
    """
    Request the next time for federate execution in an asynchronous call
    @details Call /ref helicsFederateRequestTimeComplete to finish the call
    @param fed The federate to make the request of.
    @param requestTime The next requested time.
    """
    f = loadSym("helicsFederateRequestTimeAsync")
    err = helicsErrorInitialize()
    f(fed, requestTime, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeComplete(fed: HelicsFederate) -> HelicsTime:
    """
    Complete an asynchronous requestTime call
    @param fed The federate to make the request of.
    """
    f = loadSym("helicsFederateRequestTimeComplete")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTimeIterativeAsync(fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest):
    """
    Request an iterative time through an asynchronous call
    @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
    iteration request, and returns a time and iteration status. Call /ref helicsFederateRequestTimeIterativeComplete to finish the process
    @param fed The federate to make the request of.
    @param requestTime The next desired time.
    @param iterate The requested iteration mode.
    """
    f = loadSym("helicsFederateRequestTimeIterativeAsync")
    err = helicsErrorInitialize()
    f(fed, requestTime, iterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeIterativeComplete(fed: HelicsFederate) -> HelicsTime:
    """
    Complete an iterative time request asynchronous call
    @param fed The federate to make the request of.
    @return The iteration specification of the result.
    """
    f = loadSym("helicsFederateRequestTimeIterativeComplete")
    err = helicsErrorInitialize()
    outIterate = ffi.new("helics_iteration_result *")
    result = f(fed, outIterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result, outIterate


def helicsFederateGetName(fed: HelicsFederate) -> str:
    """
    Get the name of the federate
    @param fed The federate object to query
    @return A pointer to a string with the name.
    """
    f = loadSym("helicsFederateGetName")
    result = f(fed)
    return ffi.string(result).decode()


def helicsFederateSetTimeProperty(fed: HelicsFederate, timeProperty: int, time: HelicsTime):
    """
    Set a time based property for a federate
    @param fed The federate object to set the property for.
    @param timeProperty A integer code for a time property.
    @param time The requested value of the property.
    """
    f = loadSym("helicsFederateSetTimeProperty")
    err = helicsErrorInitialize()
    f(fed, timeProperty, time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetFlagOption(fed: HelicsFederate, flag: int, flagValue: HelicsBool):
    """
    Set a flag for the federate
    @param fed The federate to alter a flag for.
    @param flag The flag to change.
    @param flagValue The new value of the flag. 0 for false, !=0 for true.
    """
    f = loadSym("helicsFederateSetFlagOption")
    err = helicsErrorInitialize()
    f(fed, flag, flagValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetSeparator(fed: HelicsFederate, separator: str):
    """
    Set the separator character in a federate
    @details The separator character is the separation character for local publications/endpoints in creating their global name.
             For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName
    @param fed The federate info object to alter.
    @param separator The character to use as a separator.
    """
    f = loadSym("helicsFederateSetSeparator")
    err = helicsErrorInitialize()
    f(fed, cchar(separator), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetIntegerProperty(fed: HelicsFederate, intProperty: int, propertyVal: int):
    """
    Set an integer based property of a federate
    @param fed The federate to change the property for.
    @param intProperty The property to set.
    @param propertyVal The value of the property.
    """
    f = loadSym("helicsFederateSetIntegerProperty")
    err = helicsErrorInitialize()
    f(fed, intProperty, propertyVal, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetTimeProperty(fed: HelicsFederate, timeProperty: int) -> HelicsTime:
    """
    Get the current value of a time based property in a federate
    @param fed The federate query.
    @param timeProperty The property to query.
    """
    f = loadSym("helicsFederateGetTimeProperty")
    err = helicsErrorInitialize()
    result = f(fed, timeProperty, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetFlagOption(fed: HelicsFederate, flag: int) -> HelicsBool:
    """
    Get a flag value for a federate
    @param fed The federate to get the flag for.
    @param flag The flag to query.
    """
    f = loadSym("helicsFederateGetFlagOption")
    err = helicsErrorInitialize()
    result = f(fed, flag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsFederateGetIntegerProperty(fed: HelicsFederate, intProperty: int) -> int:
    """
    Get the current value of an integer property (such as a logging level)
    @param fed The federate to get the flag for.
    @param intProperty A code for the property to set /ref helics_handle_options.
    """
    f = loadSym("helicsFederateGetIntegerProperty")
    err = helicsErrorInitialize()
    result = f(fed, intProperty, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetCurrentTime(fed: HelicsFederate) -> HelicsTime:
    """
    Get the current time of the federate
    @param fed The federate object to query.
    """
    f = loadSym("helicsFederateGetCurrentTime")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateSetGlobal(fed: HelicsFederate, valueName: str, value: str):
    """
    Set a federation global value through a federate
    @details This overwrites any previous value for this name.
    @param fed The federate to set the global through.
    @param valueName The name of the global to set.
    @param value The value of the global.
    """
    f = loadSym("helicsFederateSetGlobal")
    err = helicsErrorInitialize()
    f(fed, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateAddDependency(fed: HelicsFederate, fedName: str):
    """
    Add a time dependency for a federate. The federate will depend on the given named federate for time synchronization
    @param fed The federate to add the dependency for.
    @param fedName The name of the federate to depend on.
    """
    f = loadSym("helicsFederateAddDependency")
    err = helicsErrorInitialize()
    f(fed, cstring(fedName), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetLogFile(fed: HelicsFederate, logFile: str):
    """
    Set the logging file for a federate (actually on the core associated with a federate)
    @param fed The federate to set the log file for.
    @param logFile The name of the log file.
    """
    f = loadSym("helicsFederateSetLogFile")
    err = helicsErrorInitialize()
    f(fed, cstring(logFile), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogErrorMessage(fed: HelicsFederate, logmessage: str):
    """
    Log an error message through a federate
    @param fed The federate to log the error message through.
    @param logmessage The message to put in the log.
    """
    f = loadSym("helicsFederateLogErrorMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogWarningMessage(fed: HelicsFederate, logmessage: str):
    """
    Log a warning message through a federate
    @param fed The federate to log the warning message through.
    @param logmessage The message to put in the log.
    """
    f = loadSym("helicsFederateLogWarningMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogInfoMessage(fed: HelicsFederate, logmessage: str):
    """
    Log an info message through a federate
    @param fed The federate to log the info message through.
    @param logmessage The message to put in the log.
    """
    f = loadSym("helicsFederateLogInfoMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogDebugMessage(fed: HelicsFederate, logmessage: str):
    """
    Log a debug message through a federate
    @param fed The federate to log the debug message through.
    @param logmessage The message to put in the log.
    """
    f = loadSym("helicsFederateLogDebugMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogLevelMessage(fed: HelicsFederate, loglevel: int, logmessage: str):
    """
    Log a message through a federate
    @param fed The federate to log the message through.
    @param loglevel The level of the message to log see /ref helics_log_levels.
    @param logmessage The message to put in the log.
    """
    f = loadSym("helicsFederateLogLevelMessage")
    err = helicsErrorInitialize()
    f(fed, loglevel, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetGlobal(core: HelicsCore, valueName: str, value: str):
    """
    Set a global value in a core
    @details This overwrites any previous value for this name
    @param core The core to set the global through.
    @param valueName The name of the global to set.
    @param value The value of the global.
    """
    f = loadSym("helicsCoreSetGlobal")
    err = helicsErrorInitialize()
    f(core, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetGlobal(broker: HelicsBroker, valueName: str, value: str):
    """
    Set a federation global value
    @details This overwrites any previous value for this name
    @param broker The broker to set the global through.
    @param valueName The name of the global to set.
    @param value The value of the global.
    """
    f = loadSym("helicsBrokerSetGlobal")
    err = helicsErrorInitialize()
    f(broker, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetLogFile(core: HelicsCore, logFileName: str):
    """
    Set the log file on a core
    @param core The core to set the log file for.
    @param logFileName The name of the file to log to.
    """
    f = loadSym("helicsCoreSetLogFile")
    err = helicsErrorInitialize()
    f(core, cstring(logFileName), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetLogFile(broker: HelicsBroker, logFileName: str):
    """
    Set the log file on a broker
    @param broker The broker to set the log file for.
    @param logFileName The name of the file to log to.
    """
    f = loadSym("helicsBrokerSetLogFile")
    err = helicsErrorInitialize()
    f(broker, cstring(logFileName), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCreateQuery(target: str, query: str) -> HelicsQuery:
    """
    Create a query object
    @details A query object consists of a target and query string
    @param target The name of the target to query.
    @param query The query to make of the target.
    """
    f = loadSym("helicsCreateQuery")
    result = f(cstring(target), cstring(query))
    return result


def helicsQueryExecute(query: HelicsQuery, fed: HelicsFederate) -> str:
    """
    Execute a query
    @details The call will block until the query finishes which may require communication or other delays
    @param query The query object to use in the query.
    @param fed A federate to send the query through.
    """
    f = loadSym("helicsQueryExecute")
    err = helicsErrorInitialize()
    result = f(query, fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsQueryCoreExecute(query: HelicsQuery, core: HelicsCore) -> str:
    """
    Execute a query directly on a core
    @details The call will block until the query finishes which may require communication or other delays
    @param query The query object to use in the query.
    @param core The core to send the query to.
    """
    f = loadSym("helicsQueryCoreExecute")
    err = helicsErrorInitialize()
    result = f(query, core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsQueryBrokerExecute(query: HelicsQuery, broker: HelicsBroker) -> str:
    """
    Execute a query directly on a broker
    @details The call will block until the query finishes which may require communication or other delays
    @param query The query object to use in the query.
    @param broker The broker to send the query to.
    """
    f = loadSym("helicsQueryBrokerExecute")
    err = helicsErrorInitialize()
    result = f(query, broker, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsQueryExecuteAsync(query: HelicsQuery, fed: HelicsFederate):
    """
    Execute a query in a non-blocking call
    @param query The query object to use in the query.
    @param fed A federate to send the query through.
    """
    f = loadSym("helicsQueryExecuteAsync")
    err = helicsErrorInitialize()
    f(query, fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryExecuteComplete(query: HelicsQuery) -> str:
    """
    Complete the return from a query called with /ref helicsExecuteQueryAsync
    @details The function will block until the query completes /ref isQueryComplete can be called to determine if a query has completed or
    not
    @param query The query object to complete execution of.
    """
    f = loadSym("helicsQueryExecuteComplete")
    err = helicsErrorInitialize()
    result = f(query, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsQueryIsCompleted(query: HelicsQuery) -> HelicsBool:
    """
    Check if an asynchronously executed query has completed
    @details This function should usually be called after a QueryExecuteAsync function has been called
    @param query The query object to check if completed
    @return Will return helics_true if an asynchronous query has completed or a regular query call was made with a result,
            and false if an asynchronous query has not completed or is invalid
    """
    f = loadSym("helicsQueryIsCompleted")
    result = f(query)
    return result == 1


def helicsQuerySetTarget(query: HelicsQuery, target: str):
    """
    Update the target of a query
    @param query The query object to change the target of.
    @param target the name of the target to query
    """
    f = loadSym("helicsQuerySetTarget")
    err = helicsErrorInitialize()
    f(query, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQuerySetQueryString(query: HelicsQuery, queryString: str):
    """
    Update the queryString of a query
    @param query The query object to change the target of.
    @param queryString the new queryString
    """
    f = loadSym("helicsQuerySetQueryString")
    err = helicsErrorInitialize()
    f(query, cstring(queryString), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryFree(query: HelicsQuery):
    """
    Free the memory associated with a query object.
    """
    f = loadSym("helicsQueryFree")
    f(query)


def helicsCleanupLibrary():
    """
    Function to do some housekeeping work
    @details This runs some cleanup routines and tries to close out any residual thread that haven't been shutdown yet.
    """
    f = loadSym("helicsCleanupLibrary")
    f()


def helicsFederateRegisterEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
    """

    MessageFederate Calls
    Create an endpoint
    @details The endpoint becomes part of the federate and is destroyed when the federate is freed
             so there are no separate free functions for endpoints
    @param fed The federate object in which to create an endpoint must have been created
              with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    @param name The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
    @param type A string describing the expected type of the publication (may be NULL).
    """
    f = loadSym("helicsFederateRegisterEndpoint")
    err = helicsErrorInitialize()
    result = f(fed, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
    """
    Create an endpoint
    @details The endpoint becomes part of the federate and is destroyed when the federate is freed
             so there are no separate free functions for endpoints
    @param fed The federate object in which to create an endpoint must have been created
           with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    @param name The identifier for the endpoint, the given name is the global identifier.
    @param type A string describing the expected type of the publication (may be NULL).
    @return An object containing the endpoint.
    """
    f = loadSym("helicsFederateRegisterGlobalEndpoint")
    err = helicsErrorInitialize()
    result = f(fed, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetEndpoint(fed: HelicsFederate, name: str) -> HelicsEndpoint:
    """
    Get an endpoint object from a name
    @param fed The message federate object to use to get the endpoint.
    @param name The name of the endpoint.
    """
    f = loadSym("helicsFederateGetEndpoint")
    err = helicsErrorInitialize()
    result = f(fed, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetEndpointByIndex(fed: HelicsFederate, index: int) -> HelicsEndpoint:
    """
    Get an endpoint by its index, typically already created via registerInterfaces file or something of that nature
    @param fed The federate object in which to create a publication.
    @param index The index of the publication to get.
    """
    f = loadSym("helicsFederateGetEndpointByIndex")
    err = helicsErrorInitialize()
    result = f(fed, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsEndpointIsValid(endpoint: HelicsEndpoint) -> HelicsBool:
    """
    Check if an endpoint is valid
    @param endpoint The endpoint object to check
    @return helics_true if the Endpoint object represents a valid endpoint.
    """
    f = loadSym("helicsEndpointIsValid")
    result = f(endpoint)
    return result == 1


def helicsEndpointSetDefaultDestination(endpoint: HelicsEndpoint, dest: str):
    """
    Set the default destination for an endpoint if no other endpoint is given
    @param endpoint The endpoint to set the destination for.
    @param dest A string naming the desired default endpoint.
    """
    f = loadSym("helicsEndpointSetDefaultDestination")
    err = helicsErrorInitialize()
    f(endpoint, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetDefaultDestination(endpoint: HelicsEndpoint) -> str:
    """
    Get the default destination for an endpoint
    @param endpoint The endpoint to set the destination for
    @return A string with the default destination.
    """
    f = loadSym("helicsEndpointGetDefaultDestination")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsEndpointSendMessageRaw(endpoint: HelicsEndpoint, dest: str, data: bytes):
    """
    Send a message to the specified destination
    @param endpoint The endpoint to send the data from.
    @param dest The target destination.
    @param data The data to send.
    """
    f = loadSym("helicsEndpointSendMessageRaw")
    err = helicsErrorInitialize()
    inputDataLength = len(data)
    f(endpoint, cstring(dest), data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendEventRaw(
    endpoint: HelicsEndpoint, dest: str, data: str, time: HelicsTime,
):
    """
    Send a message at a specific time to the specified destination
    @param endpoint The endpoint to send the data from.
    @param dest The target destination.
    @param data The data to send.
    @param time The time the message should be sent.
    """
    f = loadSym("helicsEndpointSendEventRaw")
    err = helicsErrorInitialize()
    inputDataLength = len(data)
    f(endpoint, cstring(dest), cstring(data), inputDataLength, time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessage(endpoint: HelicsEndpoint, message: HelicsMessage):
    """
    Send a message object from a specific endpoint.
    @deprecated Use helicsEndpointSendMessageObject instead.
    @param endpoint The endpoint to send the data from.
    @param message The actual message to send.
    """
    f = loadSym("helicsEndpointSendMessage")
    err = helicsErrorInitialize()
    message = ffi.new("helics_message *", message)
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessageObject(endpoint: HelicsEndpoint, message: HelicsMessageObject):
    """
    Send a message object from a specific endpoint
    @param endpoint The endpoint to send the data from.
    @param message The actual message to send which will be copied.
    """
    f = loadSym("helicsEndpointSendMessageObject")
    err = helicsErrorInitialize()
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessageObjectZeroCopy(endpoint: HelicsEndpoint, message: HelicsMessageObject):
    """
    Send a message object from a specific endpoint, the message will not be copied and the message object will no longer be valid
    after the call
    @param endpoint The endpoint to send the data from.
    @param message The actual message to send which will be copied.
    """
    f = loadSym("helicsEndpointSendMessageObjectZeroCopy")
    err = helicsErrorInitialize()
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSubscribe(endpoint: HelicsEndpoint, key: str):
    """
    Subscribe an endpoint to a publication
    @param endpoint The endpoint to use.
    @param key The name of the publication.
    """
    f = loadSym("helicsEndpointSubscribe")
    err = helicsErrorInitialize()
    f(endpoint, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateHasMessage(fed: HelicsFederate) -> HelicsBool:
    """
    Check if the federate has any outstanding messages
    @param fed The federate to check
    @return helics_true if the federate has a message waiting, helics_false otherwise.
    """
    f = loadSym("helicsFederateHasMessage")
    result = f(fed)
    return result == 1


def helicsEndpointHasMessage(endpoint: HelicsEndpoint) -> HelicsBool:
    """
    Check if a given endpoint has any unread messages
    @param endpoint The endpoint to check
    @return helics_true if the endpoint has a message, helics_false otherwise.
    """
    f = loadSym("helicsEndpointHasMessage")
    result = f(endpoint)
    return result == 1


def helicsFederatePendingMessages(fed: HelicsFederate) -> int:
    """
    Returns the number of pending receives for the specified destination endpoint
    @param fed The federate to get the number of waiting messages from.
    """
    f = loadSym("helicsFederatePendingMessages")
    return f(fed)


def helicsEndpointPendingMessages(endpoint: HelicsEndpoint) -> int:
    """
    Returns the number of pending receives for all endpoints of a particular federate
    @param endpoint The endpoint to query.
    """
    f = loadSym("helicsEndpointPendingMessages")
    return f(endpoint)


def helicsEndpointGetMessage(endpoint: HelicsEndpoint) -> HelicsMessage:
    """
    Receive a packet from a particular endpoint
    @deprecated This function is deprecated and will be removed in Helics 3.0.
                Use helicsEndpointGetMessageObject instead
    @param[in] endpoint The identifier for the endpoint
    @return A message object.
    """
    f = loadSym("helicsEndpointGetMessage")
    return f(endpoint)


def helicsEndpointGetMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject:
    """
    Receive a packet from a particular endpoint
    @param[in] endpoint The identifier for the endpoint
    @return A message object.
    """
    f = loadSym("helicsEndpointGetMessageObject")
    return f(endpoint)


def helicsEndpointCreateMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject:
    """
    Create a new empty message object
    @details The message is empty and isValid will return false since there is no data associated with the message yet
    @param endpoint The endpoint object to associate the message with.
    """
    f = loadSym("helicsEndpointCreateMessageObject")
    err = helicsErrorInitialize()
    result = f(endpoint, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetMessage(fed: HelicsFederate) -> HelicsMessage:
    """
    Receive a communication message for any endpoint in the federate
    @deprecated This function is deprecated and will be removed in Helics 3.0.
                Use helicsFederateGetMessageObject instead
    @details The return order will be in order of endpoint creation.
             So all messages that are available for the first endpoint, then all for the second, and so on.
             Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival
    @return A unique_ptr to a Message object containing the message data.
    """
    f = loadSym("helicsFederateGetMessage")
    result = f(fed)
    return result


def helicsFederateGetMessageObject(fed: HelicsFederate) -> HelicsMessageObject:
    """
    Receive a communication message for any endpoint in the federate
    @details The return order will be in order of endpoint creation.
             So all messages that are available for the first endpoint, then all for the second, and so on.
             Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival
    @return A helics_message_object which references the data in the message.
    """
    f = loadSym("helicsFederateGetMessageObject")
    result = f(fed)
    return result


def helicsFederateCreateMessageObject(fed: HelicsFederate) -> HelicsMessageObject:
    """
    Create a new empty message object
    @details The message is empty and isValid will return false since there is no data associated with the message yet
    @param fed the federate object to associate the message with
    """
    f = loadSym("helicsFederateCreateMessageObject")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateClearMessages(fed: HelicsFederate):
    """
    Clear all stored messages from a federate
    @details This clears messages retrieved through helicsFederateGetMessage or helicsFederateGetMessageObject    @param fed The federate to clear the message for.
    """
    f = loadSym("helicsFederateClearMessages")
    f(fed)


def helicsEndpointClearMessages(endpoint: HelicsEndpoint):
    """
    Clear all message from an endpoint
    @deprecated This function does nothing and will be removed.
                Use helicsFederateClearMessages to free all messages,
                or helicsMessageFree to clear an individual message
    @param endpoint The endpoint object to operate on.
    """
    f = loadSym("helicsEndpointClearMessages")
    f(endpoint)


def helicsEndpointGetType(endpoint: HelicsEndpoint) -> str:
    """
    Get the type specified for an endpoint
    @param endpoint The endpoint object in question
    @return The defined type of the endpoint.
    """
    f = loadSym("helicsEndpointGetType")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsEndpointGetName(endpoint: HelicsEndpoint) -> str:
    """
    Get the name of an endpoint
    @param endpoint The endpoint object in question
    @return The name of the endpoint.
    """
    f = loadSym("helicsEndpointGetName")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsFederateGetEndpointCount(fed: HelicsFederate) -> int:
    """
    Get the number of endpoints in a federate
    @param fed The message federate to query
    @return (-1) if fed was not a valid federate, otherwise returns the number of endpoints.
    """
    f = loadSym("helicsFederateGetEndpointCount")
    result = f(fed)
    return result


def helicsEndpointGetInfo(endpoint: HelicsEndpoint) -> str:
    """
    Get the data in the info field of a filter
    @param end The filter to query
    @return A string with the info field string.
    """
    f = loadSym("helicsEndpointGetInfo")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsEndpointSetInfo(endpoint: HelicsEndpoint, info: str):
    """
    Set the data in the info field for a filter
    @param end The endpoint to query.
    @param info The string to set.
    """
    f = loadSym("helicsEndpointSetInfo")
    err = helicsErrorInitialize()
    f(endpoint, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSetOption(endpoint: HelicsEndpoint, option: int, value: int):
    """
    Set a handle option on an endpoint
    @param end The endpoint to modify.
    @param option Integer code for the option to set /ref helics_handle_options.
    @param value The value to set the option to.
    """
    f = loadSym("helicsEndpointSetOption")
    err = helicsErrorInitialize()
    f(endpoint, option, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetOption(endpoint: HelicsEndpoint, option: int) -> int:
    """
    Set a handle option on an endpoint
    @param end The endpoint to modify.
    @param option Integer code for the option to set /ref helics_handle_options.
    @return the value of the option, for boolean options will be 0 or 1
    """
    f = loadSym("helicsEndpointGetOption")
    result = f(endpoint, option)
    return result


def helicsMessageGetSource(message: HelicsMessageObject) -> str:
    """
    Message operation functions
    @details Functions for working with helics message envelopes.
    Get the source endpoint of a message
    @param message The message object in question
    @return A string with the source endpoint.
    """
    f = loadSym("helicsMessageGetSource")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetDestination(message: HelicsMessageObject) -> str:
    """
    Get the destination endpoint of a message
    @param message The message object in question
    @return A string with the destination endpoint.
    """
    f = loadSym("helicsMessageGetDestination")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetOriginalSource(message: HelicsMessageObject) -> str:
    """
    Get the original source endpoint of a message, the source may have been modified by filters or other actions
    @param message The message object in question
    @return A string with the source of a message.
    """
    f = loadSym("helicsMessageGetOriginalSource")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetOriginalDestination(message: HelicsMessageObject) -> str:
    """
    Get the original destination endpoint of a message, the destination may have been modified by filters or other actions
    @param message The message object in question
    @return A string with the original destination of a message.
    """
    f = loadSym("helicsMessageGetOriginalDestination")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetTime(message: HelicsMessageObject) -> HelicsTime:
    """
    Get the helics time associated with a message
    @param message The message object in question
    @return The time associated with a message.
    """
    f = loadSym("helicsMessageGetTime")
    result = f(message)
    return result


def helicsMessageGetString(message: HelicsMessageObject) -> str:
    """
    Get the payload of a message as a string
    @param message The message object in question
    @return A string representing the payload of a message.
    """
    f = loadSym("helicsMessageGetString")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetMessageID(message: HelicsMessageObject) -> int:
    """
    Get the messageID of a message
    @param message The message object in question
    @return The messageID.
    """
    f = loadSym("helicsMessageGetMessageID")
    result = f(message)
    return result


def helicsMessageCheckFlag(message: HelicsMessageObject, flag: int) -> HelicsBool:
    """
    Check if a flag is set on a message
    @param message The message object in question.
    @param flag The flag to check should be between [0,15]
    @return The flags associated with a message.
    """
    f = loadSym("helicsMessageCheckFlag")
    result = f(message, flag)
    return result == 1


def helicsMessageGetRawDataSize(message: HelicsMessageObject) -> int:
    """
    Get the size of the data payload in bytes
    @param message The message object in question
    @return The size of the data payload.
    """
    f = loadSym("helicsMessageGetRawDataSize")
    result = f(message)
    return result


def helicsMessageGetRawData(message: HelicsMessageObject):
    """
    Get the raw data for a message object
    @param message A message object to get the data for.
    @return Raw string data.
    """
    f = loadSym("helicsMessageGetRawData")
    err = helicsErrorInitialize()
    data = ffi.new("char *")
    maxMessageLen = helicsMessageGetRawDataSize(message)
    actualSize = ffi.new("int *")
    f(message, data, maxMessageLen, actualSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageGetRawDataPointer(message: HelicsMessageObject) -> pointer:
    """
    Get a pointer to the raw data of a message
    @param message A message object to get the data for
    @return A pointer to the raw data in memory, the pointer may be NULL if the message is not a valid message.
    """
    f = loadSym("helicsMessageGetRawDataPointer")
    result = f(message)
    return result


def helicsMessageIsValid(message: HelicsMessageObject) -> HelicsBool:
    """
    A check if the message contains a valid payload
    @param message The message object in question
    @return helics_true if the message contains a payload.
    """
    f = loadSym("helicsMessageIsValid")
    result = f(message)
    return result == 1


def helicsMessageSetSource(message: HelicsMessageObject, src: str):
    """
    Set the source of a message
    @param message The message object in question.
    @param src A string containing the source.
    """
    f = loadSym("helicsMessageSetSource")
    err = helicsErrorInitialize()
    f(message, cstring(src), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetDestination(message: HelicsMessageObject, dest: str):
    """
    Set the destination of a message
    @param message The message object in question.
    @param dest A string containing the new destination.
    """
    f = loadSym("helicsMessageSetDestination")
    err = helicsErrorInitialize()
    f(message, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalSource(message: HelicsMessageObject, src: str):
    """
    Set the original source of a message
    @param message The message object in question.
    @param src A string containing the new original source.
    """
    f = loadSym("helicsMessageSetOriginalSource")
    err = helicsErrorInitialize()
    f(message, cstring(src), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalDestination(message: HelicsMessageObject, dest: str):
    """
    Set the original destination of a message
    @param message The message object in question.
    @param dest A string containing the new original source.
    """
    f = loadSym("helicsMessageSetOriginalDestination")
    err = helicsErrorInitialize()
    f(message, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetTime(message: HelicsMessageObject, time: HelicsTime):
    """
    Set the delivery time for a message
    @param message The message object in question.
    @param time The time the message should be delivered.
    """
    f = loadSym("helicsMessageSetTime")
    err = helicsErrorInitialize()
    f(message, time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageResize(message: HelicsMessageObject, newSize: int):
    """
    Resize the data buffer for a message
    @details The message data buffer will be resized. There are no guarantees on what is in the buffer in newly allocated space.
             If the allocated space is not sufficient new allocations will occur
    @param message The message object in question.
    @param newSize The new size in bytes of the buffer.
    """
    f = loadSym("helicsMessageResize")
    err = helicsErrorInitialize()
    f(message, newSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageReserve(message: HelicsMessageObject, reserveSize: int):
    """
    Reserve space in a buffer but don't actually resize
    @details The message data buffer will be reserved but not resized
    @param message The message object in question.
    @param reserveSize The number of bytes to reserve in the message object.
    """
    f = loadSym("helicsMessageReserve")
    err = helicsErrorInitialize()
    f(message, reserveSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetMessageID(message: HelicsMessageObject, messageID: int):
    """
    Set the message ID for the message
    @details Normally this is not needed and the core of HELICS will adjust as needed
    @param message The message object in question.
    @param messageID A new message ID.
    """
    f = loadSym("helicsMessageSetMessageID")
    err = helicsErrorInitialize()
    f(message, messageID, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClearFlags(message: HelicsMessageObject):
    """
    Clear the flags of a message
    @param message The message object in question
    """
    f = loadSym("helicsMessageClearFlags")
    f(message)


def helicsMessageSetFlagOption(message: HelicsMessageObject, flag: int, flagValue: HelicsBool):
    """
    Set a flag on a message
    @param message The message object in question.
    @param flag An index of a flag to set on the message.
    @param flagValue The desired value of the flag.
    """
    f = loadSym("helicsMessageSetFlagOption")
    err = helicsErrorInitialize()
    f(message, flag, flagValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetString(message: HelicsMessageObject, str: str):
    """
    Set the data payload of a message as a string
    @param message The message object in question.
    @param str A string containing the message data.
    """
    f = loadSym("helicsMessageSetString")
    err = helicsErrorInitialize()
    f(message, cstring(str), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetData(message: HelicsMessageObject, data: str):
    """
    Set the data payload of a message as raw data
    @param message The message object in question.
    @param data A string containing the message data.
    @param inputDataLength The length of the data to input.
    """
    f = loadSym("helicsMessageSetData")
    err = helicsErrorInitialize()
    inputDataLength = len(data)
    f(message, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageAppendData(message: HelicsMessageObject, data: pointer, inputDataLength: int):
    """
    Append data to the payload
    @param message The message object in question.
    @param data A string containing the message data to append.
    @param inputDataLength The length of the data to input.
    """
    f = loadSym("helicsMessageAppendData")
    err = helicsErrorInitialize()
    f(message, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageCopy(source_message: HelicsMessageObject, dest_message: HelicsMessageObject):
    """
    Copy a message object
    @param source_message The message object to copy from.
    @param dest_message The message object to copy to.
    """
    f = loadSym("helicsMessageCopy")
    err = helicsErrorInitialize()
    f(source_message, dest_message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClone(message: HelicsMessageObject) -> HelicsMessageObject:
    """
    Clone a message object
    @param message The message object to copy from.
    """
    f = loadSym("helicsMessageClone")
    err = helicsErrorInitialize()
    result = f(message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsMessageFree(message: HelicsMessageObject):
    """
    Free a message object from memory
    @details memory for message is managed so not using this function does not create memory leaks, this is an indication
    to the system that the memory for this message is done being used and can be reused for a new message.
    helicsFederateClearMessages() can also be used to clear up all stored messages at once
    """
    f = loadSym("helicsMessageFree")
    f(message)


def helicsFederateRegisterFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a source Filter on the specified federate
    @details Filters can be created through a federate or a core, linking through a federate allows
             a few extra features of name matching to function on the federate interface but otherwise equivalent behavior
    @param fed The federate to register through.
    @param type The type of filter to create /ref helics_filter_type.
    @param name The name of the filter (can be NULL).
    """
    f = loadSym("helicsFederateRegisterFilter")
    err = helicsErrorInitialize()
    result = f(fed, type, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a global source filter through a federate
    @details Filters can be created through a federate or a core, linking through a federate allows
             a few extra features of name matching to function on the federate interface but otherwise equivalent behavior
    @param fed The federate to register through.
    @param type The type of filter to create /ref helics_filter_type.
    @param name The name of the filter (can be NULL).
    """
    f = loadSym("helicsFederateRegisterGlobalFilter")
    err = helicsErrorInitialize()
    result = f(fed, type, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Create a cloning Filter on the specified federate
    @details Cloning filters copy a message and send it to multiple locations, source and destination can be added
             through other functions
    @param fed The federate to register through.
    @param name The name of the filter (can be NULL).
    """
    f = loadSym("helicsFederateRegisterCloningFilter")
    err = helicsErrorInitialize()
    result = f(fed, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Create a global cloning Filter on the specified federate
    @details Cloning filters copy a message and send it to multiple locations, source and destination can be added
             through other functions
    @param fed The federate to register through.
    @param name The name of the filter (can be NULL).
    """
    f = loadSym("helicsFederateRegisterGlobalCloningFilter")
    err = helicsErrorInitialize()
    result = f(fed, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCoreRegisterFilter(core: HelicsCore, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a source Filter on the specified core
    @details Filters can be created through a federate or a core, linking through a federate allows
             a few extra features of name matching to function on the federate interface but otherwise equivalent behavior
    @param core The core to register through.
    @param type The type of filter to create /ref helics_filter_type.
    @param name The name of the filter (can be NULL).
    """
    f = loadSym("helicsCoreRegisterFilter")
    err = helicsErrorInitialize()
    result = f(core, type, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCoreRegisterCloningFilter(core: HelicsCore, name: str) -> HelicsFilter:
    """
    Create a cloning Filter on the specified core
    @details Cloning filters copy a message and send it to multiple locations, source and destination can be added
             through other functions
    @param core The core to register through.
    @param name The name of the filter (can be NULL).
    """
    f = loadSym("helicsCoreRegisterCloningFilter")
    err = helicsErrorInitialize()
    result = f(core, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetFilterCount(fed: HelicsFederate) -> int:
    """
    Get the number of filters registered through a federate
    @param fed The federate object to use to get the filter
    @return A count of the number of filters registered through a federate.
    """
    f = loadSym("helicsFederateGetFilterCount")
    result = f(fed)
    return result


def helicsFederateGetFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Get a filter by its name, typically already created via registerInterfaces file or something of that nature
    @param fed The federate object to use to get the filter.
    @param name The name of the filter.
    @return A helics_filter object, the object will not be valid and err will contain an error code if no filter with the specified name
    exists.
    """
    f = loadSym("helicsFederateGetFilter")
    err = helicsErrorInitialize()
    result = f(fed, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetFilterByIndex(fed: HelicsFederate, index: int) -> HelicsFilter:
    """
    Get a filter by its index, typically already created via registerInterfaces file or something of that nature
    @param fed The federate object in which to create a publication.
    @param index The index of the publication to get.
    @return A helics_filter, which will be NULL if an invalid index is given.
    """
    f = loadSym("helicsFederateGetFilterByIndex")
    err = helicsErrorInitialize()
    result = f(fed, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFilterIsValid(filt: HelicsFilter) -> HelicsBool:
    """
    Check if a filter is valid
    @param filt The filter object to check
    @return helics_true if the Filter object represents a valid filter.
    """
    f = loadSym("helicsFilterIsValid")
    result = f(filt)
    return result == 1


def helicsFilterGetName(filt: HelicsFilter) -> str:
    """
    Get the name of the filter and store in the given string
    @param filt The given filter
    @return A string with the name of the filter.
    """
    f = loadSym("helicsFilterGetName")
    result = f(filt)
    return ffi.string(result).decode()


def helicsFilterSet(filt: HelicsFilter, prop: str, val: float):
    """
    Set a property on a filter
    @param filt The filter to modify.
    @param prop A string containing the property to set.
    @param val A numerical value for the property.
    """
    f = loadSym("helicsFilterSet")
    err = helicsErrorInitialize()
    f(filt, cstring(prop), cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetString(filt: HelicsFilter, prop: str, val: str):
    """
    Set a string property on a filter
    @param filt The filter to modify.
    @param prop A string containing the property to set.
    @param val A string containing the new value.
    """
    f = loadSym("helicsFilterSetString")
    err = helicsErrorInitialize()
    f(filt, cstring(prop), cstring(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDestinationTarget(filt: HelicsFilter, dest: str):
    """
    Add a destination target to a filter
    @details All messages going to a destination are copied to the delivery address(es).
    @param filt The given filter to add a destination target to.
    @param dest The name of the endpoint to add as a destination target.
    """
    f = loadSym("helicsFilterAddDestinationTarget")
    err = helicsErrorInitialize()
    f(filt, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddSourceTarget(filt: HelicsFilter, source: str):
    """
    Add a source target to a filter
    @details All messages coming from a source are copied to the delivery address(es)
    @param filt The given filter.
    @param source The name of the endpoint to add as a source target.
    """
    f = loadSym("helicsFilterAddSourceTarget")
    err = helicsErrorInitialize()
    f(filt, cstring(source), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
    """
    Clone filter functions
    @details Functions that manipulate cloning filters in some way.
    Add a delivery endpoint to a cloning filter
    @details All cloned messages are sent to the delivery address(es)
    @param filt The given filter.
    @param deliveryEndpoint The name of the endpoint to deliver messages to.
    """
    f = loadSym("helicsFilterAddDeliveryEndpoint")
    err = helicsErrorInitialize()
    f(filt, cstring(deliveryEndpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveTarget(filt: HelicsFilter, target: str):
    """
    Remove a destination target from a filter
    @param filt The given filter.
    @param target The named endpoint to remove as a target.
    """
    f = loadSym("helicsFilterRemoveTarget")
    err = helicsErrorInitialize()
    f(filt, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
    """
    Remove a delivery destination from a cloning filter
    @param filt The given filter (must be a cloning filter).
    @param deliveryEndpoint A string with the delivery endpoint to remove.
    """
    f = loadSym("helicsFilterRemoveDeliveryEndpoint")
    err = helicsErrorInitialize()
    f(filt, cstring(deliveryEndpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetInfo(filt: HelicsFilter) -> str:
    """
    Get the data in the info field of a filter
    @param filt The given filter
    @return A string with the info field string.
    """
    f = loadSym("helicsFilterGetInfo")
    result = f(filt)
    return ffi.string(result).decode()


def helicsFilterSetInfo(filt: HelicsFilter, info: str):
    """
    Set the data in the info field for a filter
    @param filt The given filter.
    @param info The string to set.
    """
    f = loadSym("helicsFilterSetInfo")
    err = helicsErrorInitialize()
    f(filt, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetOption(filt: HelicsFilter, option: int, value: int):
    """
    Set the data in the info field for a filter
    @param filt The given filter.
    @param option The option to set /ref helics_handle_options.
    @param value The value of the option commonly 0 for false 1 for true.
    """
    f = loadSym("helicsFilterSetOption")
    err = helicsErrorInitialize()
    f(filt, option, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetOption(filt: HelicsFilter, option: int) -> int:
    """
    Get a handle option for the filter
    @param filt The given filter to query.
    @param option The option to query /ref helics_handle_options.
    """
    f = loadSym("helicsFilterGetOption")
    result = f(filt, option)
    return result


def helicsFederateRegisterSubscription(fed: HelicsFederate, key: str, units: str = "") -> HelicsInput:
    """
    Functions related to value federates for the C api
    Create a subscription
    @details The subscription becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions and publications
    @param fed The federate object in which to create a subscription, must have been created with /ref helicsCreateValueFederate or
    /ref helicsCreateCombinationFederate.
    @param key The identifier matching a publication to get a subscription for.
    @param units A string listing the units of the subscription (may be NULL).
    @return An object containing the subscription.
    """
    f = loadSym("helicsFederateRegisterSubscription")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication:
    """
    Register a publication with a known type
    @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions and publications
    @param fed The federate object in which to create a publication.
    @param key The identifier for the publication the global publication key will be prepended with the federate name.
    @param type A code identifying the type of the input see /ref helics_data_type for available options.
    @param units A string listing the units of the subscription (may be NULL).
    @return An object containing the publication.
    """
    f = loadSym("helicsFederateRegisterPublication")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a publication with a defined type
    @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions and publications
    @param fed The federate object in which to create a publication.
    @param key The identifier for the publication.
    @param type A string labeling the type of the publication.
    @param units A string listing the units of the subscription (may be NULL).
    @return An object containing the publication.
    """
    f = loadSym("helicsFederateRegisterTypePublication")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str = "") -> HelicsPublication:
    """
    Register a global named publication with an arbitrary type
    @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions and publications
    @param fed The federate object in which to create a publication.
    @param key The identifier for the publication.
    @param type A code identifying the type of the input see /ref helics_data_type for available options.
    @param units A string listing the units of the subscription (may be NULL).
    @return An object containing the publication.
    """
    f = loadSym("helicsFederateRegisterGlobalPublication")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a global publication with a defined type
    @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions and publications
    @param fed The federate object in which to create a publication.
    @param key The identifier for the publication.
    @param type A string describing the expected type of the publication.
    @param units A string listing the units of the subscription (may be NULL).
    @return An object containing the publication.
    """
    f = loadSym("helicsFederateRegisterGlobalTypePublication")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsInput:
    """
    Register a named input
    @details The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions, inputs, and publications
    @param fed The federate object in which to create an input.
    @param key The identifier for the publication the global input key will be prepended with the federate name.
    @param type A code identifying the type of the input see /ref helics_data_type for available options.
    @param units A string listing the units of the input (may be NULL).
    @return An object containing the input.
    """
    f = loadSym("helicsFederateRegisterInput")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsInput:
    """
    Register an input with a defined type
    @details The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions, inputs, and publications
    @param fed The federate object in which to create an input.
    @param key The identifier for the input.
    @param type A string describing the expected type of the input.
    @param units A string listing the units of the input maybe NULL.
    @return An object containing the publication.
    """
    f = loadSym("helicsFederateRegisterTypeInput")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication:
    """
    Register a global named input
    @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions and publications
    @param fed The federate object in which to create a publication.
    @param key The identifier for the publication.
    @param type A code identifying the type of the input see /ref helics_data_type for available options.
    @param units A string listing the units of the subscription maybe NULL.
    @return An object containing the publication.
    """
    f = loadSym("helicsFederateRegisterGlobalInput")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a global publication with an arbitrary type
    @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions and publications
    @param fed The federate object in which to create a publication.
    @param key The identifier for the publication.
    @param type A string defining the type of the input.
    @param units A string listing the units of the subscription maybe NULL.
    @return An object containing the publication.
    """
    f = loadSym("helicsFederateRegisterGlobalTypeInput")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetPublication(fed: HelicsFederate, key: str) -> HelicsPublication:
    """
    Get a publication object from a key
    @param fed The value federate object to use to get the publication.
    @param key The name of the publication.
    @return A helics_publication object, the object will not be valid and err will contain an error code if no publication with the specified key exists.
    """
    f = loadSym("helicsFederateGetPublication")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetPublicationByIndex(fed: HelicsFederate, index: int) -> HelicsPublication:
    """
    Get a publication by its index, typically already created via registerInterfaces file or something of that nature
    @param fed The federate object in which to create a publication.
    @param index The index of the publication to get.
    @return A helics_publication.
    """
    f = loadSym("helicsFederateGetPublicationByIndex")
    err = helicsErrorInitialize()
    result = f(fed, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetInput(fed: HelicsFederate, key: str) -> HelicsInput:
    """
    Get an input object from a key
    @param fed The value federate object to use to get the publication.
    @param key The name of the input.
    @return A helics_input object, the object will not be valid and err will contain an error code if no input with the specified key exists.
    """
    f = loadSym("helicsFederateGetInput")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetInputByIndex(fed: HelicsFederate, index: int) -> HelicsInput:
    """
    Get an input by its index, typically already created via registerInterfaces file or something of that nature
    @param fed The federate object in which to create a publication.
    @param index The index of the publication to get.
    @return A helics_input, which will be NULL if an invalid index.
    """
    f = loadSym("helicsFederateGetInputByIndex")
    err = helicsErrorInitialize()
    result = f(fed, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetSubscription(fed: HelicsFederate, key: str) -> HelicsInput:
    """
    Get an input object from a subscription target
    @param fed The value federate object to use to get the publication.
    @param key The name of the publication that a subscription is targeting.
    @return A helics_input object, the object will not be valid and err will contain an error code if no input with the specified key exists.
    """
    f = loadSym("helicsFederateGetSubscription")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateClearUpdates(fed: HelicsFederate):
    """
    Clear all the update flags from a federates inputs
    @param fed The value federate object for which to clear update flags.
    """
    f = loadSym("helicsFederateClearUpdates")
    f(fed)


def helicsFederateRegisterFromPublicationJSON(fed: HelicsFederate, json: str):
    """
    Register the publications via JSON publication string
    @param fed The value federate object to use to register the publications.
    @param json The JSON publication string.
    """
    f = loadSym("helicsFederateRegisterFromPublicationJSON")
    err = helicsErrorInitialize()
    f(fed, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederatePublishJSON(fed: HelicsFederate, json: str):
    """
    Publish data contained in a JSON file or string
    @param fed The value federate object through which to publish the data.
    @param json The publication file name or literal JSON data string.
    """
    f = loadSym("helicsFederatePublishJSON")
    err = helicsErrorInitialize()
    f(fed, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationIsValid(pub: HelicsPublication) -> HelicsBool:
    """
    Publication functions
    @details Functions for publishing data of various kinds.
    The data will get translated to the type specified when the publication was constructed automatically
    regardless of the function used to publish the data.
    Check if a publication is valid
    @param pub The publication to check
    @return helics_true if the publication is a valid publication.
    """
    f = loadSym("helicsPublicationIsValid")
    result = f(pub)
    return result == 1


def helicsPublicationPublishRaw(pub: HelicsPublication, data: pointer, inputDataLength: int):
    """
    Publish raw data from a char * and length
    @param pub The publication to publish for.
    @param data A pointer to the raw data.
    @param inputDataLength The size in bytes of the data to publish.
    """
    f = loadSym("helicsPublicationPublishRaw")
    err = helicsErrorInitialize()
    f(pub, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishString(pub: HelicsPublication, str: str):
    """
    Publish a string
    @param pub The publication to publish for.
    @param str The string to publish.
    """
    f = loadSym("helicsPublicationPublishString")
    err = helicsErrorInitialize()
    f(pub, cstring(str), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishInteger(pub: HelicsPublication, val: int):
    """
    Publish an integer value
    @param pub The publication to publish for.
    @param val The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishInteger")
    err = helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishBoolean(pub: HelicsPublication, val: HelicsBool):
    """
    Publish a Boolean Value
    @param pub The publication to publish for.
    @param val The boolean value to publish.
    """
    f = loadSym("helicsPublicationPublishBoolean")
    err = helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishDouble(pub: HelicsPublication, val: float):
    """
    Publish a double floating point value
    @param pub The publication to publish for.
    @param val The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishDouble")
    err = helicsErrorInitialize()
    f(pub, cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishTime(pub: HelicsPublication, val: HelicsTime):
    """
    Publish a time value
    @param pub The publication to publish for.
    @param val The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishTime")
    err = helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishChar(pub: HelicsPublication, val: str):
    """
    Publish a single character
    @param pub The publication to publish for.
    @param val The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishChar")
    err = helicsErrorInitialize()
    f(pub, cchar(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishComplex(pub: HelicsPublication, c: complex):
    """
    Publish a complex value (or pair of values)
    @param pub The publication to publish for.
    @param real The real part of a complex number to publish.
    @param imag The imaginary part of a complex number to publish.
    """
    f = loadSym("helicsPublicationPublishComplex")
    err = helicsErrorInitialize()
    f(pub, c.real, c.imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishVector(pub: HelicsPublication, vectorInput: List[float]):
    """
    Publish a vector of doubles
    @param pub The publication to publish for.
    @param vectorInput A pointer to an array of double data.
    """
    f = loadSym("helicsPublicationPublishVector")
    err = helicsErrorInitialize()
    vectorLength = len(vectorInput)
    f(pub, vectorInput, vectorLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishNamedPoint(pub: HelicsPublication, str: str, val: float):
    """
    Publish a named point
    @param pub The publication to publish for.
    @param str A string for the name to publish.
    @param val A double for the value to publish.
    """
    f = loadSym("helicsPublicationPublishNamedPoint")
    err = helicsErrorInitialize()
    f(pub, cstring(str), cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationAddTarget(pub: HelicsPublication, target: str):
    """
    Add a named input to the list of targets a publication publishes to
    @param pub The publication to add the target for.
    @param target The name of an input that the data should be sent to.
    """
    f = loadSym("helicsPublicationAddTarget")
    err = helicsErrorInitialize()
    f(pub, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsValid(ipt: HelicsInput) -> HelicsBool:
    """
    Check if an input is valid
    @param ipt The input to check
    @return helics_true if the Input object represents a valid input.
    """
    f = loadSym("helicsInputIsValid")
    result = f(ipt)
    return result == 1


def helicsInputAddTarget(ipt: HelicsInput, target: str):
    """
    Add a publication to the list of data that an input subscribes to
    @param ipt The named input to modify.
    @param target The name of a publication that an input should subscribe to.
    """
    f = loadSym("helicsInputAddTarget")
    err = helicsErrorInitialize()
    f(ipt, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetRawValueSize(ipt: HelicsInput) -> int:
    """

    GetValue functions
    @details Data can be returned in a number of formats,  for instance if data is published as a double it can be returned as a string and
    vice versa,  not all translations make that much sense but they do work.
    Get the size of the raw value for subscription
    @return The size of the raw data/string in bytes.
    """
    f = loadSym("helicsInputGetRawValueSize")
    result = f(ipt)
    return result


def helicsInputGetRawValue(ipt: HelicsInput) -> str:
    """
    Get the raw data for the latest value of a subscription
    @param ipt The input to get the data for.
    @return Raw string data.
    """
    f = loadSym("helicsInputGetRawValue")
    err = helicsErrorInitialize()
    data = ffi.new("char *")
    maxDatalen = helicsInputGetRawValueSize(ipt)
    actualSize = ffi.new("int *")
    f(ipt, data, maxDatalen, actualSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(data).decode()


def helicsInputGetStringSize(ipt: HelicsInput) -> int:
    """
    Get the size of a value for subscription assuming return as a string
    @return The size of the string.
    """
    f = loadSym("helicsInputGetStringSize")
    result = f(ipt)
    return result


def helicsInputGetString(ipt: HelicsInput) -> str:
    """
    Get a string value from a subscription
    @param ipt The input to get the data for.
    @return A string data
    """
    f = loadSym("helicsInputGetString")
    err = helicsErrorInitialize()
    outputString = ffi.new("char[500]")
    maxStringLen = 500
    actualLength = ffi.new("int *")
    f(ipt, outputString, maxStringLen, actualLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(outputString).decode()


def helicsInputGetInteger(ipt: HelicsInput) -> int:
    """
    Get an integer value from a subscription
    @param ipt The input to get the data for.
    @return An int64_t value with the current value of the input.
    """
    f = loadSym("helicsInputGetInteger")
    err = helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsInputGetBoolean(ipt: HelicsInput) -> HelicsBool:
    """
    Get a boolean value from a subscription
    @param ipt The input to get the data for.
    @return A boolean value of current input value.
    """
    f = loadSym("helicsInputGetBoolean")
    err = helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsInputGetDouble(ipt: HelicsInput) -> float:
    """
    Get a double value from a subscription
    @param ipt The input to get the data for.
    @return The double value of the input.
    """
    f = loadSym("helicsInputGetDouble")
    err = helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsInputGetTime(ipt: HelicsInput) -> HelicsTime:
    """
    Get a time value from a subscription
    @param ipt The input to get the data for.
    @return The resulting time value.
    """
    f = loadSym("helicsInputGetTime")
    err = helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsInputGetChar(ipt: HelicsInput) -> str:
    """
    Get a single character value from an input
    @param ipt The input to get the data for.
    @return The resulting character value.
    """
    f = loadSym("helicsInputGetChar")
    err = helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        # TODO: this is a char, will ffi.string conversion work?
        return result.decode()


def helicsInputGetComplexObject(ipt: HelicsInput) -> complex:
    """
    Get a complex object from an input object
    @param ipt The input to get the data for.
    @return A helics_complex structure with the value.
    """
    f = loadSym("helicsInputGetComplexObject")
    err = helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return complex(result.real, result.imag)


def helicsInputGetComplex(ipt: HelicsInput) -> complex:
    """
    Get a pair of double forming a complex number from a subscriptions
    @param ipt The input to get the data for.
    @return a pair of floating point values that represent the real and imag values
    """
    f = loadSym("helicsInputGetComplex")
    err = helicsErrorInitialize()
    real = ffi.new("double *")
    imag = ffi.new("double *")
    f(ipt, real, imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return complex(real[0], imag[0])


def helicsInputGetVectorSize(ipt: HelicsInput) -> int:
    """
    Get the size of a value for subscription assuming return as an array of doubles
    @return The number of doubles in a returned vector.
    """
    f = loadSym("helicsInputGetVectorSize")
    result = f(ipt)
    return result


def helicsInputGetVector(ipt: HelicsInput) -> List[float]:
    """
    Get a vector from a subscription
    @param ipt The input to get the result for.
    @return a list of floating point values
    """
    f = loadSym("helicsInputGetVector")
    err = helicsErrorInitialize()
    maxlen = helicsInputGetVectorSize(ipt)
    data = ffi.new(f"double[{maxlen}]")
    actualSize = ffi.new("int *")
    f(ipt, data, maxlen, actualSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return [x for x in data]


def helicsInputGetNamedPoint(ipt: HelicsInput):
    """
    Get a named point from a subscription
    @param ipt The input to get the result for.
    @return a string and a double value for the named point
    """
    f = loadSym("helicsInputGetNamedPoint")
    err = helicsErrorInitialize()
    outputString = ffi.new("char[500]")
    maxStringLen = 500
    actualLength = ffi.new("int *")
    val = ffi.new("double *")
    f(ipt, outputString, maxStringLen, actualLength, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(outputString).decode(), val[0]


def helicsInputSetDefaultRaw(ipt: HelicsInput, data: str):
    """

    Default Value functions
    @details These functions set the default value for a subscription. That is the value returned if nothing was published from elsewhere.
    Set the default as a raw data array
    @param ipt The input to set the default for.
    @param data A pointer to the raw data to use for the default.
    """
    f = loadSym("helicsInputSetDefaultRaw")
    err = helicsErrorInitialize()
    inputDataLength = len(data)
    f(ipt, cstring(data), inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultString(ipt: HelicsInput, str: str):
    """
    Set the default as a string
    @param ipt The input to set the default for.
    @param str A pointer to the default string.
    """
    f = loadSym("helicsInputSetDefaultString")
    err = helicsErrorInitialize()
    f(ipt, cstring(str), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultInteger(ipt: HelicsInput, val: int):
    """
    Set the default as an integer
    @param ipt The input to set the default for.
    @param val The default integer.
    """
    f = loadSym("helicsInputSetDefaultInteger")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultBoolean(ipt: HelicsInput, val: HelicsBool):
    """
    Set the default as a boolean
    @param ipt The input to set the default for.
    @param val The default boolean value.
    """
    f = loadSym("helicsInputSetDefaultBoolean")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultTime(ipt: HelicsInput, val: HelicsTime):
    """
    Set the default as a time
    @param ipt The input to set the default for.
    @param val The default time value.
    """
    f = loadSym("helicsInputSetDefaultTime")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultChar(ipt: HelicsInput, val: str):
    """
    Set the default as a char
    @param ipt The input to set the default for.
    @param val The default char value.
    """
    f = loadSym("helicsInputSetDefaultChar")
    err = helicsErrorInitialize()
    f(ipt, cchar(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultDouble(ipt: HelicsInput, val: float):
    """
    Set the default as a double
    @param ipt The input to set the default for.
    @param val The default double value.
    """
    f = loadSym("helicsInputSetDefaultDouble")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultComplex(ipt: HelicsInput, c: complex):
    """
    Set the default as a complex number
    @param ipt The input to set the default for.
    @param real The default real value.
    @param imag The default imaginary value.
    """
    f = loadSym("helicsInputSetDefaultComplex")
    err = helicsErrorInitialize()
    f(ipt, c.real, c.imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultVector(ipt: HelicsInput, vectorInput: List[float]):
    """
    Set the default as a vector of doubles
    @param ipt The input to set the default for.
    @param vectorInput A pointer to an array of double data.
    @param vectorLength The number of points to publish.
    """
    f = loadSym("helicsInputSetDefaultVector")
    err = helicsErrorInitialize()
    vectorLength = len(vectorInput)
    f(ipt, vectorInput, vectorLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultNamedPoint(ipt: HelicsInput, str: str, val: float):
    """
    Set the default as a NamedPoint
    @param ipt The input to set the default for.
    @param str A pointer to a string representing the name.
    @param val A double value for the value of the named point.
    """
    f = loadSym("helicsInputSetDefaultNamedPoint")
    err = helicsErrorInitialize()
    f(ipt, cstring(str), cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetType(ipt: HelicsInput) -> str:
    """
    Get the type of an input
    @param ipt The input to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetType")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsInputGetPublicationType(ipt: HelicsInput) -> str:
    """
    Get the type the publisher to an input is sending
    @param ipt The input to query
    @return A const char * with the type name.
    """
    f = loadSym("helicsInputGetPublicationType")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsPublicationGetType(pub: HelicsPublication) -> str:
    """
    Get the type of a publication
    @param pub The publication to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsPublicationGetType")
    result = f(pub)
    return ffi.string(result).decode()


def helicsInputGetKey(ipt: HelicsInput) -> str:
    """
    Get the key of an input
    @param ipt The input to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetKey")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsSubscriptionGetKey(ipt: HelicsInput) -> str:
    """
    Get the key of a subscription
    @return A const char with the subscription key.
    """
    f = loadSym("helicsSubscriptionGetKey")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsPublicationGetKey(pub: HelicsPublication) -> str:
    """
    Get the key of a publication
    @details This will be the global key used to identify the publication to the federation
    @param pub The publication to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsPublicationGetKey")
    result = f(pub)
    return ffi.string(result).decode()


def helicsInputGetUnits(ipt: HelicsInput) -> str:
    """
    Get the units of an input
    @param ipt The input to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetUnits")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsInputGetInjectionUnits(ipt: HelicsInput) -> str:
    """
    Get the units of the publication that an input is linked to
    @param ipt The input to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetInjectionUnits")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsInputGetExtractionUnits(ipt: HelicsInput) -> str:
    """
    Get the units of an input
    @details The same as helicsInputGetUnits
    @param ipt The input to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetExtractionUnits")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsPublicationGetUnits(pub: HelicsPublication) -> str:
    """
    Get the units of a publication
    @param pub The publication to query
    @return A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsPublicationGetUnits")
    result = f(pub)
    return ffi.string(result).decode()


def helicsInputGetInfo(inp: HelicsInput) -> str:
    """
    Get the data in the info field of an input
    @param inp The input to query
    @return A string with the info field string.
    """
    f = loadSym("helicsInputGetInfo")
    result = f(inp)
    return ffi.string(result).decode()


def helicsInputSetInfo(inp: HelicsInput, info: str):
    """
    Set the data in the info field for an input
    @param inp The input to query.
    @param info The string to set.
    """
    f = loadSym("helicsInputSetInfo")
    err = helicsErrorInitialize()
    f(inp, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetInfo(pub: HelicsPublication) -> str:
    """
    Get the data in the info field of an publication
    @param pub The publication to query
    @return A string with the info field string.
    """
    f = loadSym("helicsPublicationGetInfo")
    result = f(pub)
    return ffi.string(result).decode()


def helicsPublicationSetInfo(pub: HelicsPublication, info: str):
    """
    Set the data in the info field for a publication
    @param pub The publication to set the info field for.
    @param info The string to set.
    """
    f = loadSym("helicsPublicationSetInfo")
    err = helicsErrorInitialize()
    f(pub, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetOption(inp: HelicsInput, option: int) -> int:
    """
    Get the current value of an input handle option    @param inp The input to query.
    @param option Integer representation of the option in question see /ref helics_handle_options
    @return An integer value with the current value of the given option.
    """
    f = loadSym("helicsInputGetOption")
    result = f(inp, option)
    return result


def helicsInputSetOption(inp: HelicsInput, option: int, value: int):
    """
    Set an option on an input    @param inp The input to query.
    @param option The option to set for the input /ref helics_handle_options.
    @param value The value to set the option to.
    """
    f = loadSym("helicsInputSetOption")
    err = helicsErrorInitialize()
    f(inp, option, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetOption(pub: HelicsPublication, option: int) -> int:
    """
    Get the value of an option for a publication    @param pub The publication to query.
    @param option The value to query see /ref helics_handle_options
    @return A string with the info field string.
    """
    f = loadSym("helicsPublicationGetOption")
    result = f(pub, option)
    return result


def helicsPublicationSetOption(pub: HelicsPublication, option: int, val: int):
    """
    Set the value of an option for a publication    @param pub The publication to query.
    @param option Integer code for the option to set /ref helics_handle_options.
    @param val The value to set the option to.
    """
    f = loadSym("helicsPublicationSetOption")
    err = helicsErrorInitialize()
    f(pub, option, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationSetMinimumChange(pub: HelicsPublication, tolerance: float):
    """
    Set the minimum change detection tolerance
    @param pub The publication to modify.
    @param tolerance The tolerance level for publication, values changing less than this value will not be published.
    """
    f = loadSym("helicsPublicationSetMinimumChange")
    err = helicsErrorInitialize()
    f(pub, cdouble(tolerance), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetMinimumChange(inp: HelicsInput, tolerance: float):
    """
    Set the minimum change detection tolerance
    @param inp The input to modify.
    @param tolerance The tolerance level for registering an update, values changing less than this value will not show asbeing updated.
    """
    f = loadSym("helicsInputSetMinimumChange")
    err = helicsErrorInitialize()
    f(inp, cdouble(tolerance), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsUpdated(ipt: HelicsInput) -> HelicsBool:
    """
    Check if a particular subscription was updated
    @return helics_true if it has been updated since the last value retrieval.
    """
    f = loadSym("helicsInputIsUpdated")
    result = f(ipt)
    return result == 1


def helicsInputLastUpdateTime(ipt: HelicsInput) -> HelicsTime:
    """
    Get the last time a subscription was updated.
    """
    f = loadSym("helicsInputLastUpdateTime")
    result = f(ipt)
    return result


def helicsInputClearUpdate(ipt: HelicsInput):
    """
    Clear the updated flag from an input.
    """
    f = loadSym("helicsInputClearUpdate")
    f(ipt)


def helicsFederateGetPublicationCount(fed: HelicsFederate) -> int:
    """
    Get the number of publications in a federate
    @return (-1) if fed was not a valid federate otherwise returns the number of publications.
    """
    f = loadSym("helicsFederateGetPublicationCount")
    result = f(fed)
    return result


def helicsFederateGetInputCount(fed: HelicsFederate) -> int:
    """
    Get the number of subscriptions in a federate
    @return (-1) if fed was not a valid federate otherwise returns the number of subscriptions.
    """
    f = loadSym("helicsFederateGetInputCount")
    result = f(fed)
    return result
