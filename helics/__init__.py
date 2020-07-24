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


class HelicsException(Exception):
    """Base class for exceptions in this module."""

    pass


def cstring(s: str) -> str:
    """Convert python string to cstring"""
    return ffi.new("char[]", s.decode())


def loadSym(s):
    return getattr(lib, s)


# **************************************************
# * Common Functions
# **************************************************
# *
# * Get a version string for HELICS.
#
def helicsGetVersion() -> str:
    f = loadSym("helicsGetVersion")
    result = f()
    return ffi.string(result).decode()


# *
# * Get the build flags used to compile HELICS.
#
def helicsGetBuildFlags() -> str:
    f = loadSym("helicsGetBuildFlags")
    result = f()
    return ffi.string(result).decode()


# *
# * Get the compiler version used to compile HELICS.
#
def helicsGetCompilerVersion() -> str:
    f = loadSym("helicsGetCompilerVersion")
    result = f()
    return ffi.string(result).decode()


# *
# * Return an initialized error object.
#
def helicsErrorInitialize() -> HelicsError:
    f = loadSym("helicsErrorInitialize")
    result = f()
    return result


# *
# * Clear an error object.
#
def helicsErrorClear(err: HelicsError):
    f = loadSym("helicsErrorClear")
    f(err)


# *
# * Returns true if core/broker type specified is available in current compilation.
# *
# * @param type A string representing a core type.
# *
# * @details Options include "zmq", "udp", "ipc", "interprocess", "tcp", "default", "mpi".
#
def helicsIsCoreTypeAvailable(type: str) -> HelicsBool:
    f = loadSym("helicsIsCoreTypeAvailable")
    result = f(cstring(type))
    return result == 1


# *
# * Create a core object.
# *
# * @param type The type of the core to create.
# * @param name The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
# * @param initString An initialization string to send to the core. The format is similar to command line arguments.
# *                   Typical options include a broker name, the broker address, the number of federates, etc.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A helics_core object.
# * @forcpponly
# * If the core is invalid, err will contain the corresponding error message and the returned object will be NULL.
# * @endforcpponly
#
def helicsCreateCore(type: str, name: str, initString: str) -> HelicsCore:
    f = loadSym("helicsCreateCore")
    err = lib.helicsErrorInitialize()
    result = f(cstring(type), cstring(name), cstring(initString), err)
    if err.error_code != 0:
        raise HelicsException(ffi.string(err.message))
    else:
        return result


# *
# * Create a core object by passing command line arguments.
# *
# * @param type The type of the core to create.
# * @param name The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
# * @forcpponly
# * @param argc The number of arguments.
# * @endforcpponly
# * @param argv The list of string values from a command line.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string
# *                    if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A helics_core object.
#
def helicsCreateCoreFromArgs(type: str, name: str, arguments: List[str]) -> HelicsCore:
    f = loadSym("helicsCreateCoreFromArgs")
    argc = len(arguments)
    argv = ffi.new(f"char*[{argc}]")
    for i, s in enumerate(arguments):
        argv[i] = s
    err = lib.helicsErrorInitialize()
    result = f(cstring(type), cstring(name), argc, argv, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result


# *
# * Create a new reference to an existing core.
# *
# * @details This will create a new broker object that references the existing broker. The new broker object must be freed as well.
# *
# * @param core An existing helics_core.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A new reference to the same broker.
#
def helicsCoreClone(core: HelicsCore) -> HelicsCore:
    f = loadSym("helicsCoreClone")
    err = lib.helicsErrorInitialize()
    result = f(core, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result


# *
# * Check if a core object is a valid object.
# *
# * @param core The helics_core object to test.
#
def helicsCoreIsValid(core: HelicsCore) -> HelicsBool:
    f = loadSym("helicsCoreIsValid")
    result = f(core)
    return result == 1


# *
# * Create a broker object.
# *
# * @param type The type of the broker to create.
# * @param name The name of the broker. It can be a nullptr or empty string to have a name automatically assigned.
# * @param initString An initialization string to send to the core-the format is similar to command line arguments.
# *                   Typical options include a broker address such as --broker="XSSAF" if this is a subbroker, or the number of federates,
# * or the address.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A helics_broker object.
# * @forcpponly
# * It will be NULL if there was an error indicated in the err object.
# * @endforcpponly
#
def helicsCreateBroker(type: str, name: str, initString: str) -> HelicsBroker:
    f = loadSym("helicsCreateBroker")
    err = lib.helicsErrorInitialize()
    result = f(cstring(type), cstring(name), cstring(initString), err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result


# *
# * Create a core object by passing command line arguments.
# *
# * @param type The type of the core to create.
# * @param name The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
# * @forcpponly
# * @param argc The number of arguments.
# * @endforcpponly
# * @param argv The list of string values from a command line.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A helics_core object.
#
def helicsCreateBrokerFromArgs(type: str, name: str, arguments: List[str]) -> HelicsBroker:
    f = loadSym("helicsCreateBrokerFromArgs")
    argc = len(arguments)
    argv = ffi.new(f"char*[{argc}]")
    for i, s in enumerate(arguments):
        argv[i] = s
    err = lib.helicsErrorInitialize()
    result = f(cstring(type), cstring(name), argc, argv, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result


# *
# * Create a new reference to an existing broker.
# *
# * @details This will create a new broker object that references the existing broker it must be freed as well.
# *
# * @param broker An existing helics_broker.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A new reference to the same broker.
#
def helicsBrokerClone(broker: HelicsBroker) -> HelicsBroker:
    f = loadSym("helicsBrokerClone")
    err = lib.helicsErrorInitialize()
    result = f(broker, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result


# *
# * Check if a broker object is a valid object.
# *
# * @param broker The helics_broker object to test.
#
def helicsBrokerIsValid(broker: HelicsBroker) -> HelicsBool:
    f = loadSym("helicsBrokerIsValid")
    result = f(broker)
    return result == 1


# *
# * Check if a broker is connected.
# *
# * @details A connected broker implies it is attached to cores or cores could reach out to communicate.
# *
# * @return helics_false if not connected.
#
def helicsBrokerIsConnected(broker: HelicsBroker) -> HelicsBool:
    f = loadSym("helicsBrokerIsConnected")
    result = f(broker)
    return result == 1


# *
# * Link a named publication and named input using a broker.
# *
# * @param broker The broker to generate the connection from.
# * @param source The name of the publication (cannot be NULL).
# * @param target The name of the target to send the publication data (cannot be NULL).
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsBrokerDataLink(broker: HelicsBroker, source: str, target: str):
    f = loadSym("helicsBrokerDataLink")
    err = lib.helicsErrorInitialize()
    f(broker, cstring(source), cstring(target), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Link a named filter to a source endpoint.
# *
# * @param broker The broker to generate the connection from.
# * @param filter The name of the filter (cannot be NULL).
# * @param endpoint The name of the endpoint to filter the data from (cannot be NULL).
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsBrokerAddSourceFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
    f = loadSym("helicsBrokerAddSourceFilterToEndpoint")
    err = lib.helicsErrorInitialize()
    f(broker, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Link a named filter to a destination endpoint.
# *
# * @param broker The broker to generate the connection from.
# * @param filter The name of the filter (cannot be NULL).
# * @param endpoint The name of the endpoint to filter the data going to (cannot be NULL).
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsBrokerAddDestinationFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
    f = loadSym("helicsBrokerAddDestinationFilterToEndpoint")
    err = lib.helicsErrorInitialize()
    f(broker, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Load a file containing connection information.
# *
# * @param broker The broker to generate the connections from.
# * @param file A JSON or TOML file containing connection information.
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsBrokerMakeConnections(broker: HelicsBroker, file: str):
    f = loadSym("helicsBrokerMakeConnections")
    err = lib.helicsErrorInitialize()
    f(broker, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Wait for the core to disconnect.
# *
# * @param core The core to wait for.
# * @param msToWait The time out in millisecond (<0 for infinite timeout).
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return helics_true if the disconnect was successful, helics_false if there was a timeout.
#
def helicsCoreWaitForDisconnect(core: HelicsCore, msToWait: int) -> HelicsBool:
    f = loadSym("helicsCoreWaitForDisconnect")
    err = lib.helicsErrorInitialize()
    result = f(core, msToWait.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result == 1


# *
# * Wait for the broker to disconnect.
# *
# * @param broker The broker to wait for.
# * @param msToWait The time out in millisecond (<0 for infinite timeout).
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return helics_true if the disconnect was successful, helics_false if there was a timeout.
#
def helicsBrokerWaitForDisconnect(broker: HelicsBroker, msToWait: int) -> HelicsBool:
    f = loadSym("helicsBrokerWaitForDisconnect")
    err = lib.helicsErrorInitialize()
    result = f(broker, msToWait.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result == 1


# *
# * Check if a core is connected.
# *
# * @details A connected core implies it is attached to federates or federates could be attached to it
# *
# * @return helics_false if not connected, helics_true if it is connected.
#
def helicsCoreIsConnected(core: HelicsCore) -> HelicsBool:
    f = loadSym("helicsCoreIsConnected")
    result = f(core)
    return result == 1


# *
# * Link a named publication and named input using a core.
# *
# * @param core The core to generate the connection from.
# * @param source The name of the publication (cannot be NULL).
# * @param target The name of the target to send the publication data (cannot be NULL).
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsCoreDataLink(core: HelicsCore, source: str, target: str):
    f = loadSym("helicsCoreDataLink")
    err = lib.helicsErrorInitialize()
    f(core, cstring(source), cstring(target), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Link a named filter to a source endpoint.
# *
# * @param core The core to generate the connection from.
# * @param filter The name of the filter (cannot be NULL).
# * @param endpoint The name of the endpoint to filter the data from (cannot be NULL).
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsCoreAddSourceFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
    f = loadSym("helicsCoreAddSourceFilterToEndpoint")
    err = lib.helicsErrorInitialize()
    f(core, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Link a named filter to a destination endpoint.
# *
# * @param core The core to generate the connection from.
# * @param filter The name of the filter (cannot be NULL).
# * @param endpoint The name of the endpoint to filter the data going to (cannot be NULL).
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsCoreAddDestinationFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
    f = loadSym("helicsCoreAddDestinationFilterToEndpoint")
    err = lib.helicsErrorInitialize()
    f(core, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Load a file containing connection information.
# *
# * @param core The core to generate the connections from.
# * @param file A JSON or TOML file containing connection information.
# * @forcpponly
# * @param[in,out] err A helics_error object, can be NULL if the errors are to be ignored.
# * @endforcpponly
#
def helicsCoreMakeConnections(core: HelicsCore, file: str):
    f = loadSym("helicsCoreMakeConnections")
    err = lib.helicsErrorInitialize()
    f(core, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an identifier for the broker.
# *
# * @param broker The broker to query.
# *
# * @return A string containing the identifier for the broker.
#
def helicsBrokerGetIdentifier(broker: HelicsBroker) -> str:
    f = loadSym("helicsBrokerGetIdentifier")
    result = f(broker)
    return ffi.string(result).decode()


# *
# * Get an identifier for the core.
# *
# * @param core The core to query.
# *
# * @return A string with the identifier of the core.
#
def helicsCoreGetIdentifier(core: HelicsCore) -> str:
    f = loadSym("helicsCoreGetIdentifier")
    result = f(core)
    return ffi.string(result).decode()


# *
# * Get the network address associated with a broker.
# *
# * @param broker The broker to query.
# *
# * @return A string with the network address of the broker.
#
def helicsBrokerGetAddress(broker: HelicsBroker) -> str:
    f = loadSym("helicsBrokerGetAddress")
    result = f(broker)
    return ffi.string(result).decode()


# *
# * Get the network address associated with a core.
# *
# * @param core The core to query.
# *
# * @return A string with the network address of the broker.
#
def helicsCoreGetAddress(core: HelicsCore) -> str:
    f = loadSym("helicsCoreGetAddress")
    result = f(core)
    return ffi.string(result).decode()


# *
# * Set the core to ready for init.
# *
# * @details This function is used for cores that have filters but no federates so there needs to be
# *          a direct signal to the core to trigger the federation initialization.
# *
# * @param core The core object to enable init values for.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsCoreSetReadyToInit(core: HelicsCore):
    f = loadSym("helicsCoreSetReadyToInit")
    err = lib.helicsErrorInitialize()
    f(core, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Connect a core to the federate based on current configuration.
# *
# * @param core The core to connect.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return helics_false if not connected, helics_true if it is connected.
#
def helicsCoreConnect(core: HelicsCore) -> HelicsBool:
    f = loadSym("helicsCoreConnect")
    err = lib.helicsErrorInitialize()
    result = f(core, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result == 1


# *
# * Disconnect a core from the federation.
# *
# * @param core The core to query.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsCoreDisconnect(core: HelicsCore):
    f = loadSym("helicsCoreDisconnect")
    err = lib.helicsErrorInitialize()
    f(core, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an existing federate object from a core by name.
# *
# * @details The federate must have been created by one of the other functions and at least one of the objects referencing the created
# *          federate must still be active in the process.
# *
# * @param fedName The name of the federate to retrieve.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return NULL if no fed is available by that name otherwise a helics_federate with that name.
#
def helicsGetFederateByName(fedName: str) -> HelicsFederate:
    f = loadSym("helicsGetFederateByName")
    err = lib.helicsErrorInitialize()
    result = f(cstring(fedName), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Disconnect a broker.
# *
# * @param broker The broker to disconnect.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsBrokerDisconnect(broker: HelicsBroker):
    f = loadSym("helicsBrokerDisconnect")
    err = lib.helicsErrorInitialize()
    f(broker, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Disconnect and free a federate.
#
def helicsFederateDestroy(fed: HelicsFederate):
    f = loadSym("helicsFederateDestroy")
    f(fed)


# *
# * Disconnect and free a broker.
#
def helicsBrokerDestroy(broker: HelicsBroker):
    f = loadSym("helicsBrokerDestroy")
    f(broker)


# *
# * Disconnect and free a core.
#
def helicsCoreDestroy(core: HelicsCore):
    f = loadSym("helicsCoreDestroy")
    f(core)


# *
# * Release the memory associated with a core.
#
def helicsCoreFree(core: HelicsCore):
    f = loadSym("helicsCoreFree")
    f(core)


# *
# * Release the memory associated with a broker.
#
def helicsBrokerFree(broker: HelicsBroker):
    f = loadSym("helicsBrokerFree")
    f(broker)


#
# * Creation and destruction of Federates.
#
# *
# * Create a value federate from a federate info object.
# *
# * @details helics_federate objects can be used in all functions that take a helics_federate or helics_federate object as an argument.
# *
# * @param fedName The name of the federate to create, can NULL or an empty string to use the default name from fi or an assigned name.
# * @param fi The federate info object that contains details on the federate.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An opaque value federate object.
#
def helicsCreateValueFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
    f = loadSym("helicsCreateValueFederate")
    err = lib.helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a value federate from a JSON file, JSON string, or TOML file.
# *
# * @details helics_federate objects can be used in all functions that take a helics_federate or helics_federate object as an argument.
# *
# * @param configFile A JSON file or a JSON string or TOML file that contains setup and configuration information.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An opaque value federate object.
#
def helicsCreateValueFederateFromConfig(configFile: str) -> HelicsFederate:
    f = loadSym("helicsCreateValueFederateFromConfig")
    err = lib.helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a message federate from a federate info object.
# *
# * @details helics_message_federate objects can be used in all functions that take a helics_message_federate or helics_federate object as an
# * argument.
# *
# * @param fedName The name of the federate to create.
# * @param fi The federate info object that contains details on the federate.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An opaque message federate object.
#
def helicsCreateMessageFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
    f = loadSym("helicsCreateMessageFederate")
    err = lib.helicsErrorInitialize()
    result = f(fedName, fi, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a message federate from a JSON file or JSON string or TOML file.
# *
# * @details helics_message_federate objects can be used in all functions that take a helics_message_federate or helics_federate object as an
# * argument.
# *
# * @param configFile A Config(JSON,TOML) file or a JSON string that contains setup and configuration information.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An opaque message federate object.
#
def helicsCreateMessageFederateFromConfig(configFile: str) -> HelicsFederate:
    f = loadSym("helicsCreateMessageFederateFromConfig")
    err = lib.helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a combination federate from a federate info object.
# *
# * @details Combination federates are both value federates and message federates, objects can be used in all functions
# *                      that take a helics_federate, helics_message_federate or helics_federate object as an argument
# *
# * @param fedName A string with the name of the federate, can be NULL or an empty string to pull the default name from fi.
# * @param fi The federate info object that contains details on the federate.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An opaque value federate object nullptr if the object creation failed.
#
def helicsCreateCombinationFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
    f = loadSym("helicsCreateCombinationFederate")
    err = lib.helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a combination federate from a JSON file or JSON string or TOML file.
# *
# * @details Combination federates are both value federates and message federates, objects can be used in all functions
# *          that take a helics_federate, helics_message_federate or helics_federate object as an argument
# *
# * @param configFile A JSON file or a JSON string or TOML file that contains setup and configuration information.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An opaque combination federate object.
#
def helicsCreateCombinationFederateFromConfig(configFile: str) -> HelicsFederate:
    f = loadSym("helicsCreateCombinationFederateFromConfig")
    err = lib.helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a new reference to an existing federate.
# *
# * @details This will create a new helics_federate object that references the existing federate. The new object must be freed as well.
# *
# * @param fed An existing helics_federate.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A new reference to the same federate.
#
def helicsFederateClone(fed: HelicsFederate) -> HelicsFederate:
    f = loadSym("helicsFederateClone")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a federate info object for specifying federate information when constructing a federate.
# *
# * @return A helics_federate_info object which is a reference to the created object.
#
def helicsCreateFederateInfo() -> HelicsFederateInfo:
    f = loadSym("helicsCreateFederateInfo")
    result = f()


# *
# * Create a federate info object from an existing one and clone the information.
# *
# * @param fi A federateInfo object to duplicate.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# *  @return A helics_federate_info object which is a reference to the created object.
#
def helicsFederateInfoClone(fi: HelicsFederateInfo) -> HelicsFederateInfo:
    f = loadSym("helicsFederateInfoClone")
    err = lib.helicsErrorInitialize()
    result = f(fi, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Load federate info from command line arguments.
# *
# * @param fi A federateInfo object.
# * @param argc The number of command line arguments.
# * @param argv An array of strings from the command line.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoLoadFromArgs(fi: HelicsFederateInfo, arguments: List[str]):
    f = loadSym("helicsFederateInfoLoadFromArgs")
    err = lib.helicsErrorInitialize()
    argc = arguments.len
    argv = allocCStringArray([])
    for i, s in arguments.pairs():
        argv[i] = s
    f(fi, argc.cint, argv, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Delete the memory associated with a federate info object.
#
def helicsFederateInfoFree(fi: HelicsFederateInfo):
    f = loadSym("helicsFederateInfoFree")
    f(fi)


# *
# * Check if a federate_object is valid.
# *
# * @return helics_true if the federate is a valid active federate, helics_false otherwise
#
def helicsFederateIsValid(fed: HelicsFederate) -> HelicsBool:
    f = loadSym("helicsFederateIsValid")
    result = f(fed)
    return result == 1


# *
# * Set the name of the core to link to for a federate.
# *
# * @param fi The federate info object to alter.
# * @param corename The identifier for a core to link to.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetCoreName(fi: HelicsFederateInfo, corename: str):
    f = loadSym("helicsFederateInfoSetCoreName")
    err = lib.helicsErrorInitialize()
    f(fi, cstring(corename), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the initialization string for the core usually in the form of command line arguments.
# *
# * @param fi The federate info object to alter.
# * @param coreInit A string containing command line arguments to be passed to the core.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetCoreInitString(fi: HelicsFederateInfo, coreInit: str):
    f = loadSym("helicsFederateInfoSetCoreInitString")
    err = lib.helicsErrorInitialize()
    f(fi, cstring(coreInit), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the initialization string that a core will pass to a generated broker usually in the form of command line arguments.
# *
# * @param fi The federate info object to alter.
# * @param brokerInit A string with command line arguments for a generated broker.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetBrokerInitString(fi: HelicsFederateInfo, brokerInit: str):
    f = loadSym("helicsFederateInfoSetBrokerInitString")
    err = lib.helicsErrorInitialize()
    f(fi, cstring(brokerInit), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the core type by integer code.
# *
# * @details Valid values available by definitions in api-data.h.
# * @param fi The federate info object to alter.
# * @param coretype An numerical code for a core type see /ref helics_core_type.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetCoreType(fi: HelicsFederateInfo, coretype: int):
    f = loadSym("helicsFederateInfoSetCoreType")
    err = lib.helicsErrorInitialize()
    f(fi, coretype.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the core type from a string.
# *
# * @param fi The federate info object to alter.
# * @param coretype A string naming a core type.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetCoreTypeFromString(fi: HelicsFederateInfo, coretype: str):
    f = loadSym("helicsFederateInfoSetCoreTypeFromString")
    err = lib.helicsErrorInitialize()
    f(fi, cstring(coretype), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the name or connection information for a broker.
# *
# * @details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
# * @param fi The federate info object to alter.
# * @param broker A string which defines the connection information for a broker either a name or an address.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetBroker(fi: HelicsFederateInfo, broker: str):
    f = loadSym("helicsFederateInfoSetBroker")
    err = lib.helicsErrorInitialize()
    f(fi, cstring(broker), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the key for a broker connection.
# *
# * @details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
# * @param fi The federate info object to alter.
# * @param brokerkey A string containing a key for the broker to connect.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetBrokerKey(fi: HelicsFederateInfo, brokerkey: str):
    f = loadSym("helicsFederateInfoSetBrokerKey")
    err = lib.helicsErrorInitialize()
    f(fi, cstring(brokerkey), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the port to use for the broker.
# *
# * @details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
# * This will only be useful for network broker connections.
# * @param fi The federate info object to alter.
# * @param brokerPort The integer port number to use for connection with a broker.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetBrokerPort(fi: HelicsFederateInfo, brokerPort: int):
    f = loadSym("helicsFederateInfoSetBrokerPort")
    err = lib.helicsErrorInitialize()
    f(fi, brokerPort.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the local port to use.
# *
# * @details This is only used if the core is automatically created, the port information will be transferred to the core for connection.
# * @param fi The federate info object to alter.
# * @param localPort A string with the port information to use as the local server port can be a number or "auto" or "os_local".
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetLocalPort(fi: HelicsFederateInfo, localPort: str):
    f = loadSym("helicsFederateInfoSetLocalPort")
    err = lib.helicsErrorInitialize()
    f(fi, cstring(localPort), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a property index for use in /ref helicsFederateInfoSetFlagOption, /ref helicsFederateInfoSetTimeProperty,
# * or /ref helicsFederateInfoSetIntegerProperty
# * @param val A string with the property name.
# * @return An int with the property code or (-1) if not a valid property.
#
def helicsGetPropertyIndex(val: str) -> int:
    f = loadSym("helicsGetPropertyIndex")
    f(cstring(val))


# *
# * Get a property index for use in /ref helicsFederateInfoSetFlagOption, /ref helicsFederateSetFlagOption,
# * @param val A string with the option name.
# * @return An int with the property code or (-1) if not a valid property.
#
def helicsGetFlagIndex(val: str) -> int:
    f = loadSym("helicsGetFlagIndex")
    f(cstring(val))


# *
# * Get an option index for use in /ref helicsPublicationSetOption, /ref helicsInputSetOption, /ref helicsEndpointSetOption,
# * /ref helicsFilterSetOption, and the corresponding get functions.
# *
# * @param val A string with the option name.
# *
# * @return An int with the option index or (-1) if not a valid property.
#
def helicsGetOptionIndex(val: str) -> int:
    f = loadSym("helicsGetOptionIndex")
    f(cstring(val))


# *
# * Get an option value for use in /ref helicsPublicationSetOption, /ref helicsInputSetOption, /ref helicsEndpointSetOption,
# * /ref helicsFilterSetOption.
# *
# * @param val A string representing the value.
# *
# * @return An int with the option value or (-1) if not a valid value.
#
def helicsGetOptionValue(val: str) -> int:
    f = loadSym("helicsGetOptionValue")
    f(cstring(val))


# *
# * Set a flag in the info structure.
# *
# * @details Valid flags are available /ref helics_federate_flags.
# * @param fi The federate info object to alter.
# * @param flag A numerical index for a flag.
# * @param value The desired value of the flag helics_true or helics_false.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetFlagOption(fi: HelicsFederateInfo, flag: int, value: HelicsBool):
    f = loadSym("helicsFederateInfoSetFlagOption")
    err = lib.helicsErrorInitialize()
    f(fi, flag.cint, value, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the separator character in the info structure.
# *
# * @details The separator character is the separation character for local publications/endpoints in creating their global name.
# * For example if the separator character is '/'  then a local endpoint would have a globally reachable name of fedName/localName.
# * @param fi The federate info object to alter.
# * @param separator The character to use as a separator.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetSeparator(fi: HelicsFederateInfo, separator: str):
    f = loadSym("helicsFederateInfoSetSeparator")
    err = lib.helicsErrorInitialize()
    f(fi, separator.cchar, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the output delay for a federate.
# *
# * @param fi The federate info object to alter.
# * @param timeProperty An integer representation of the time based property to set see /ref helics_properties.
# * @param propertyValue The value of the property to set the timeProperty to.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetTimeProperty(fi: HelicsFederateInfo, timeProperty: int, propertyValue: HelicsTime):
    f = loadSym("helicsFederateInfoSetTimeProperty")
    err = lib.helicsErrorInitialize()
    f(fi, timeProperty.cint, propertyValue, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set an integer property for a federate.
# *
# * @details Set known properties.
# *
# * @param fi The federateInfo object to alter.
# * @param intProperty An int identifying the property.
# * @param propertyValue The value to set the property to.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateInfoSetIntegerProperty(fi: HelicsFederateInfo, intProperty: int, propertyValue: int):
    f = loadSym("helicsFederateInfoSetIntegerProperty")
    err = lib.helicsErrorInitialize()
    f(fi, intProperty.cint, propertyValue.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Load interfaces from a file.
# *
# * @param fed The federate to which to load interfaces.
# * @param file The name of a file to load the interfaces from either JSON, or TOML.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateRegisterInterfaces(fed: HelicsFederate, file: str):
    f = loadSym("helicsFederateRegisterInterfaces")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Generate a global error from a federate.
# *
# * @details A global error halts the co-simulation completely.
# *
# * @param fed The federate to create an error in.
# * @param error_code The integer code for the error.
# * @param error_string A string describing the error.
#
def helicsFederateGlobalError(fed: HelicsFederate, error_code: int, error_string: str):
    f = loadSym("helicsFederateGlobalError")
    f(fed, error_code.cint, cstring(error_string))


# *
# * Generate a local error in a federate.
# *
# * @details This will propagate through the co-simulation but not necessarily halt the co-simulation, it has a similar effect to finalize
# * but does allow some interaction with a core for a brief time.
# * @param fed The federate to create an error in.
# * @param error_code The integer code for the error.
# * @param error_string A string describing the error.
#
def helicsFederateLocalError(fed: HelicsFederate, error_code: int, error_string: str):
    f = loadSym("helicsFederateLocalError")
    f(fed, error_code.cint, cstring(error_string))


# *
# * Finalize the federate. This function halts all communication in the federate and disconnects it from the core.
#
def helicsFederateFinalize(fed: HelicsFederate):
    f = loadSym("helicsFederateFinalize")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Finalize the federate in an async call.
#
def helicsFederateFinalizeAsync(fed: HelicsFederate):
    f = loadSym("helicsFederateFinalizeAsync")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Complete the asynchronous finalize call.
#
def helicsFederateFinalizeComplete(fed: HelicsFederate):
    f = loadSym("helicsFederateFinalizeComplete")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Release the memory associated with a federate.
#
def helicsFederateFree(fed: HelicsFederate):
    f = loadSym("helicsFederateFree")
    f(fed)


# *
# * Call when done using the helics library.
# * This function will ensure the threads are closed properly. If possible this should be the last call before exiting.
#
def helicsCloseLibrary():
    f = loadSym("helicsCloseLibrary")
    f()


#
# * Initialization, execution, and time requests.
#
# *
# * Enter the initialization state of a federate.
# *
# * @details The initialization state allows initial values to be set and received if the iteration is requested on entry to the execution
# * state. This is a blocking call and will block until the core allows it to proceed.
# *
# * @param fed The federate to operate on.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateEnterInitializingMode(fed: HelicsFederate):
    f = loadSym("helicsFederateEnterInitializingMode")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Non blocking alternative to \ref helicsFederateEnterInitializingMode.
# *
# * @details The function helicsFederateEnterInitializationModeFinalize must be called to finish the operation.
# *
# * @param fed The federate to operate on.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateEnterInitializingModeAsync(fed: HelicsFederate):
    f = loadSym("helicsFederateEnterInitializingModeAsync")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Check if the current Asynchronous operation has completed.
# *
# * @param fed The federate to operate on.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return helics_false if not completed, helics_true if completed.
#
def helicsFederateIsAsyncOperationCompleted(fed: HelicsFederate) -> HelicsBool:
    f = loadSym("helicsFederateIsAsyncOperationCompleted")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result == 1


# *
# * Finalize the entry to initialize mode that was initiated with /ref heliceEnterInitializingModeAsync.
# *
# * @param fed The federate desiring to complete the initialization step.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateEnterInitializingModeComplete(fed: HelicsFederate):
    f = loadSym("helicsFederateEnterInitializingModeComplete")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request that the federate enter the Execution mode.
# *
# * @details This call is blocking until granted entry by the core object. On return from this call the federate will be at time 0.
# *          For an asynchronous alternative call see /ref helicsFederateEnterExecutingModeAsync.
# *
# * @param fed A federate to change modes.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateEnterExecutingMode(fed: HelicsFederate):
    f = loadSym("helicsFederateEnterExecutingMode")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request that the federate enter the Execution mode.
# *
# * @details This call is non-blocking and will return immediately. Call /ref helicsFederateEnterExecutingModeComplete to finish the call
# * sequence.
# *
# * @param fed The federate object to complete the call.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateEnterExecutingModeAsync(fed: HelicsFederate):
    f = loadSym("helicsFederateEnterExecutingModeAsync")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Complete the call to /ref helicsFederateEnterExecutingModeAsync.
# *
# * @param fed The federate object to complete the call.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateEnterExecutingModeComplete(fed: HelicsFederate):
    f = loadSym("helicsFederateEnterExecutingModeComplete")
    err = lib.helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request an iterative time.
# *
# * @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
# *          iteration request, and returns a time and iteration status.
# *
# * @param fed The federate to make the request of.
# * @param iterate The requested iteration mode.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An iteration structure with field containing the time and iteration status.
#
def helicsFederateEnterExecutingModeIterative(fed: HelicsFederate, iterate: HelicsIterationRequest) -> HelicsIterationResult:
    f = loadSym("helicsFederateEnterExecutingModeIterative")
    err = lib.helicsErrorInitialize()
    result = f(fed, iterate, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request an iterative entry to the execution mode.
# *
# * @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
# *          iteration request, and returns a time and iteration status
# *
# * @param fed The federate to make the request of.
# * @param iterate The requested iteration mode.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateEnterExecutingModeIterativeAsync(fed: HelicsFederate, iterate: HelicsIterationRequest):
    f = loadSym("helicsFederateEnterExecutingModeIterativeAsync")
    err = lib.helicsErrorInitialize()
    f(fed, iterate, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Complete the asynchronous iterative call into ExecutionMode.
# *
# * @param fed The federate to make the request of.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return An iteration object containing the iteration time and iteration_status.
#
def helicsFederateEnterExecutingModeIterativeComplete(fed: HelicsFederate,) -> HelicsIterationResult:
    f = loadSym("helicsFederateEnterExecutingModeIterativeComplete")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the current state of a federate.
# *
# * @param fed The federate to query.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return State the resulting state if void return helics_ok.
#
def helicsFederateGetState(fed: HelicsFederate) -> HelicsFederateState:
    f = loadSym("helicsFederateGetState")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the core object associated with a federate.
# *
# * @param fed A federate object.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A core object, nullptr if invalid.
#
def helicsFederateGetCoreObject(fed: HelicsFederate) -> HelicsCore:
    f = loadSym("helicsFederateGetCoreObject")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request the next time for federate execution.
# *
# * @param fed The federate to make the request of.
# * @param requestTime The next requested time.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return The time granted to the federate, will return helics_time_maxtime if the simulation has terminated or is invalid.
#
def helicsFederateRequestTime(fed: HelicsFederate, requestTime: HelicsTime) -> HelicsTime:
    f = loadSym("helicsFederateRequestTime")
    err = lib.helicsErrorInitialize()
    result = f(fed, requestTime, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request the next time for federate execution.
# *
# * @param fed The federate to make the request of.
# * @param timeDelta The requested amount of time to advance.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return The time granted to the federate, will return helics_time_maxtime if the simulation has terminated or is invalid
#
def helicsFederateRequestTimeAdvance(fed: HelicsFederate, timeDelta: HelicsTime) -> HelicsTime:
    f = loadSym("helicsFederateRequestTimeAdvance")
    err = lib.helicsErrorInitialize()
    result = f(fed, timeDelta, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request the next time step for federate execution.
# *
# * @details Feds should have setup the period or minDelta for this to work well but it will request the next time step which is the current
# * time plus the minimum time step.
# *
# * @param fed The federate to make the request of.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return The time granted to the federate, will return helics_time_maxtime if the simulation has terminated or is invalid
#
def helicsFederateRequestNextStep(fed: HelicsFederate) -> HelicsTime:
    f = loadSym("helicsFederateRequestNextStep")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request an iterative time.
# *
# * @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
# * iteration request, and returns a time and iteration status.
# *
# * @param fed The federate to make the request of.
# * @param requestTime The next desired time.
# * @param iterate The requested iteration mode.
# * @forcpponly
# * @param[out] outIteration  The iteration specification of the result.
# * @endforcpponly
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return The granted time, will return helics_time_maxtime if the simulation has terminated along with the appropriate iteration result.
# * @beginPythonOnly
# * This function also returns the iteration specification of the result.
# * @endPythonOnly
#
def helicsFederateRequestTimeIterative(
    fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest, outIteration: HelicsIterationResult,
) -> HelicsTime:
    f = loadSym("helicsFederateRequestTimeIterative")
    err = lib.helicsErrorInitialize()
    result = f(fed, requestTime, iterate, outIteration, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request the next time for federate execution in an asynchronous call.
# *
# * @details Call /ref helicsFederateRequestTimeComplete to finish the call.
# *
# * @param fed The federate to make the request of.
# * @param requestTime The next requested time.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateRequestTimeAsync(fed: HelicsFederate, requestTime: HelicsTime):
    f = loadSym("helicsFederateRequestTimeAsync")
    err = lib.helicsErrorInitialize()
    f(fed, requestTime, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Complete an asynchronous requestTime call.
# *
# * @param fed The federate to make the request of.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return The time granted to the federate, will return helics_time_maxtime if the simulation has terminated.
#
def helicsFederateRequestTimeComplete(fed: HelicsFederate) -> HelicsTime:
    f = loadSym("helicsFederateRequestTimeComplete")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Request an iterative time through an asynchronous call.
# *
# * @details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
# * iteration request, and returns a time and iteration status. Call /ref helicsFederateRequestTimeIterativeComplete to finish the process.
# *
# * @param fed The federate to make the request of.
# * @param requestTime The next desired time.
# * @param iterate The requested iteration mode.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateRequestTimeIterativeAsync(fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest):
    f = loadSym("helicsFederateRequestTimeIterativeAsync")
    err = lib.helicsErrorInitialize()
    f(fed, requestTime, iterate, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Complete an iterative time request asynchronous call.
# *
# * @param fed The federate to make the request of.
# * @forcpponly
# * @param[out] outIterate The iteration specification of the result.
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return The granted time, will return helics_time_maxtime if the simulation has terminated.
# * @beginPythonOnly
# * This function also returns the iteration specification of the result.
# * @endPythonOnly
#
def helicsFederateRequestTimeIterativeComplete(fed: HelicsFederate, outIterate: HelicsIterationResult) -> HelicsTime:
    f = loadSym("helicsFederateRequestTimeIterativeComplete")
    err = lib.helicsErrorInitialize()
    result = f(fed, outIterate, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the name of the federate.
# *
# * @param fed The federate object to query.
# *
# * @return A pointer to a string with the name.
#
def helicsFederateGetName(fed: HelicsFederate) -> str:
    f = loadSym("helicsFederateGetName")
    result = f(fed)
    return ffi.string(result).decode()


# *
# * Set a time based property for a federate.
# *
# * @param fed The federate object to set the property for.
# * @param timeProperty A integer code for a time property.
# * @param time The requested value of the property.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateSetTimeProperty(fed: HelicsFederate, timeProperty: int, time: HelicsTime):
    f = loadSym("helicsFederateSetTimeProperty")
    err = lib.helicsErrorInitialize()
    f(fed, timeProperty.cint, time, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set a flag for the federate.
# *
# * @param fed The federate to alter a flag for.
# * @param flag The flag to change.
# * @param flagValue The new value of the flag. 0 for false, !=0 for true.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateSetFlagOption(fed: HelicsFederate, flag: int, flagValue: HelicsBool):
    f = loadSym("helicsFederateSetFlagOption")
    err = lib.helicsErrorInitialize()
    f(fed, flag.cint, flagValue, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the separator character in a federate.
# *
# * @details The separator character is the separation character for local publications/endpoints in creating their global name.
# *          For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.
# *
# * @param fed The federate info object to alter.
# * @param separator The character to use as a separator.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateSetSeparator(fed: HelicsFederate, separator: str):
    f = loadSym("helicsFederateSetSeparator")
    err = lib.helicsErrorInitialize()
    f(fed, separator.cchar, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set an integer based property of a federate.
# *
# * @param fed The federate to change the property for.
# * @param intProperty The property to set.
# * @param propertyVal The value of the property.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateSetIntegerProperty(fed: HelicsFederate, intProperty: int, propertyVal: int):
    f = loadSym("helicsFederateSetIntegerProperty")
    err = lib.helicsErrorInitialize()
    f(fed, intProperty.cint, propertyVal.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the current value of a time based property in a federate.
# *
# * @param fed The federate query.
# * @param timeProperty The property to query.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsFederateGetTimeProperty(fed: HelicsFederate, timeProperty: int) -> HelicsTime:
    f = loadSym("helicsFederateGetTimeProperty")
    err = lib.helicsErrorInitialize()
    result = f(fed, timeProperty.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a flag value for a federate.
# *
# * @param fed The federate to get the flag for.
# * @param flag The flag to query.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return The value of the flag.
#
def helicsFederateGetFlagOption(fed: HelicsFederate, flag: int) -> HelicsBool:
    f = loadSym("helicsFederateGetFlagOption")
    err = lib.helicsErrorInitialize()
    result = f(fed, flag.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result == 1


# *
# * Get the current value of an integer property (such as a logging level).
# *
# * @param fed The federate to get the flag for.
# * @param intProperty A code for the property to set /ref helics_handle_options.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return The value of the property.
#
def helicsFederateGetIntegerProperty(fed: HelicsFederate, intProperty: int) -> int:
    f = loadSym("helicsFederateGetIntegerProperty")
    err = lib.helicsErrorInitialize()
    result = f(fed, intProperty.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the current time of the federate.
# *
# * @param fed The federate object to query.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return The current time of the federate.
#
def helicsFederateGetCurrentTime(fed: HelicsFederate) -> HelicsTime:
    f = loadSym("helicsFederateGetCurrentTime")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set a federation global value through a federate.
# *
# * @details This overwrites any previous value for this name.
# * @param fed The federate to set the global through.
# * @param valueName The name of the global to set.
# * @param value The value of the global.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateSetGlobal(fed: HelicsFederate, valueName: str, value: str):
    f = loadSym("helicsFederateSetGlobal")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Add a time dependency for a federate. The federate will depend on the given named federate for time synchronization.
# *
# * @param fed The federate to add the dependency for.
# * @param fedName The name of the federate to depend on.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateAddDependency(fed: HelicsFederate, fedName: str):
    f = loadSym("helicsFederateAddDependency")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(fedName), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the logging file for a federate (actually on the core associated with a federate).
# *
# * @param fed The federate to set the log file for.
# * @param logFile The name of the log file.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateSetLogFile(fed: HelicsFederate, logFile: str):
    f = loadSym("helicsFederateSetLogFile")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(logFile), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Log an error message through a federate.
# *
# * @param fed The federate to log the error message through.
# * @param logmessage The message to put in the log.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateLogErrorMessage(fed: HelicsFederate, logmessage: str):
    f = loadSym("helicsFederateLogErrorMessage")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Log a warning message through a federate.
# *
# * @param fed The federate to log the warning message through.
# * @param logmessage The message to put in the log.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateLogWarningMessage(fed: HelicsFederate, logmessage: str):
    f = loadSym("helicsFederateLogWarningMessage")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Log an info message through a federate.
# *
# * @param fed The federate to log the info message through.
# * @param logmessage The message to put in the log.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateLogInfoMessage(fed: HelicsFederate, logmessage: str):
    f = loadSym("helicsFederateLogInfoMessage")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Log a debug message through a federate.
# *
# * @param fed The federate to log the debug message through.
# * @param logmessage The message to put in the log.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateLogDebugMessage(fed: HelicsFederate, logmessage: str):
    f = loadSym("helicsFederateLogDebugMessage")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Log a message through a federate.
# *
# * @param fed The federate to log the message through.
# * @param loglevel The level of the message to log see /ref helics_log_levels.
# * @param logmessage The message to put in the log.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFederateLogLevelMessage(fed: HelicsFederate, loglevel: int, logmessage: str):
    f = loadSym("helicsFederateLogLevelMessage")
    err = lib.helicsErrorInitialize()
    f(fed, loglevel.cint, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set a global value in a core.
# *
# * @details This overwrites any previous value for this name.
# *
# * @param core The core to set the global through.
# * @param valueName The name of the global to set.
# * @param value The value of the global.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsCoreSetGlobal(core: HelicsCore, valueName: str, value: str):
    f = loadSym("helicsCoreSetGlobal")
    err = lib.helicsErrorInitialize()
    f(core, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set a federation global value.
# *
# * @details This overwrites any previous value for this name.
# *
# * @param broker The broker to set the global through.
# * @param valueName The name of the global to set.
# * @param value The value of the global.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsBrokerSetGlobal(broker: HelicsBroker, valueName: str, value: str):
    f = loadSym("helicsBrokerSetGlobal")
    err = lib.helicsErrorInitialize()
    f(broker, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the log file on a core.
# *
# * @param core The core to set the log file for.
# * @param logFileName The name of the file to log to.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsCoreSetLogFile(core: HelicsCore, logFileName: str):
    f = loadSym("helicsCoreSetLogFile")
    err = lib.helicsErrorInitialize()
    f(core, cstring(logFileName), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the log file on a broker.
# *
# * @param broker The broker to set the log file for.
# * @param logFileName The name of the file to log to.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsBrokerSetLogFile(broker: HelicsBroker, logFileName: str):
    f = loadSym("helicsBrokerSetLogFile")
    err = lib.helicsErrorInitialize()
    f(broker, cstring(logFileName), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a query object.
# *
# * @details A query object consists of a target and query string.
# *
# * @param target The name of the target to query.
# * @param query The query to make of the target.
#
def helicsCreateQuery(target: str, query: str) -> HelicsQuery:
    f = loadSym("helicsCreateQuery")
    f(cstring(target), cstring(query))


# *
# * Execute a query.
# *
# * @details The call will block until the query finishes which may require communication or other delays.
# *
# * @param query The query object to use in the query.
# * @param fed A federate to send the query through.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A pointer to a string.  The string will remain valid until the query is freed or executed again.
# * @forcpponly
# *         The return will be nullptr if fed or query is an invalid object, the return string will be "#invalid" if the query itself was
# * invalid.
# * @endforcpponly
#
def helicsQueryExecute(query: HelicsQuery, fed: HelicsFederate) -> str:
    f = loadSym("helicsQueryExecute")
    err = lib.helicsErrorInitialize()
    result = f(query, fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return ffi.string(result).decode()


# *
# * Execute a query directly on a core.
# *
# * @details The call will block until the query finishes which may require communication or other delays.
# *
# * @param query The query object to use in the query.
# * @param core The core to send the query to.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A pointer to a string.  The string will remain valid until the query is freed or executed again.
# * @forcpponly
# *         The return will be nullptr if core or query is an invalid object, the return string will be "#invalid" if the query itself was
# * invalid.
# * @endforcpponly
#
def helicsQueryCoreExecute(query: HelicsQuery, core: HelicsCore) -> str:
    f = loadSym("helicsQueryCoreExecute")
    err = lib.helicsErrorInitialize()
    result = f(query, core, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return ffi.string(result).decode()


# *
# * Execute a query directly on a broker.
# *
# * @details The call will block until the query finishes which may require communication or other delays.
# *
# * @param query The query object to use in the query.
# * @param broker The broker to send the query to.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A pointer to a string.  The string will remain valid until the query is freed or executed again.
# * @forcpponly
# *         The return will be nullptr if broker or query is an invalid object, the return string will be "#invalid" if the query itself was
# * invalid
# * @endforcpponly
#
def helicsQueryBrokerExecute(query: HelicsQuery, broker: HelicsBroker) -> str:
    f = loadSym("helicsQueryBrokerExecute")
    err = lib.helicsErrorInitialize()
    result = f(query, broker, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return ffi.string(result).decode()


# *
# * Execute a query in a non-blocking call.
# *
# * @param query The query object to use in the query.
# * @param fed A federate to send the query through.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsQueryExecuteAsync(query: HelicsQuery, fed: HelicsFederate):
    f = loadSym("helicsQueryExecuteAsync")
    err = lib.helicsErrorInitialize()
    f(query, fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Complete the return from a query called with /ref helicsExecuteQueryAsync.
# *
# * @details The function will block until the query completes /ref isQueryComplete can be called to determine if a query has completed or
# * not.
# *
# * @param query The query object to complete execution of.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @return A pointer to a string. The string will remain valid until the query is freed or executed again.
# * @forcpponly
# *         The return will be nullptr if query is an invalid object
# * @endforcpponly
#
def helicsQueryExecuteComplete(query: HelicsQuery) -> str:
    f = loadSym("helicsQueryExecuteComplete")
    err = lib.helicsErrorInitialize()
    result = f(query, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return ffi.string(result).decode()


# *
# * Check if an asynchronously executed query has completed.
# *
# * @details This function should usually be called after a QueryExecuteAsync function has been called.
# *
# * @param query The query object to check if completed.
# *
# * @return Will return helics_true if an asynchronous query has completed or a regular query call was made with a result,
# *         and false if an asynchronous query has not completed or is invalid
#
def helicsQueryIsCompleted(query: HelicsQuery) -> HelicsBool:
    f = loadSym("helicsQueryIsCompleted")
    result = f(query)
    return result == 1


# *
# * Update the target of a query.
# *
# * @param query The query object to change the target of.
# * @param target the name of the target to query
# *
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsQuerySetTarget(query: HelicsQuery, target: str):
    f = loadSym("helicsQuerySetTarget")
    err = lib.helicsErrorInitialize()
    f(query, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Update the queryString of a query.
# *
# * @param query The query object to change the target of.
# * @param queryString the new queryString
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsQuerySetQueryString(query: HelicsQuery, queryString: str):
    f = loadSym("helicsQuerySetQueryString")
    err = lib.helicsErrorInitialize()
    f(query, cstring(queryString), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Free the memory associated with a query object.
#
def helicsQueryFree(query: HelicsQuery):
    f = loadSym("helicsQueryFree")
    f(query)


# *
# * Function to do some housekeeping work.
# *
# * @details This runs some cleanup routines and tries to close out any residual thread that haven't been shutdown yet.
#
def helicsCleanupLibrary():
    f = loadSym("helicsCleanupLibrary")
    f()


#  MessageFederate Calls
# *
# * Create an endpoint.
# *
# * @details The endpoint becomes part of the federate and is destroyed when the federate is freed
# *          so there are no separate free functions for endpoints.
# *
# * @param fed The federate object in which to create an endpoint must have been created
# *           with helicsCreateMessageFederate or helicsCreateCombinationFederate.
# * @param name The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
# * @param type A string describing the expected type of the publication (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the endpoint.
# * @forcpponly
# *         nullptr on failure.
# * @endforcpponly
#
def helicsFederateRegisterEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
    f = loadSym("helicsFederateRegisterEndpoint")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create an endpoint.
# *
# * @details The endpoint becomes part of the federate and is destroyed when the federate is freed
# *          so there are no separate free functions for endpoints.
# *
# * @param fed The federate object in which to create an endpoint must have been created
#               with helicsCreateMessageFederate or helicsCreateCombinationFederate.
# * @param name The identifier for the endpoint, the given name is the global identifier.
# * @param type A string describing the expected type of the publication (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# * @return An object containing the endpoint.
# * @forcpponly
# *         nullptr on failure.
# * @endforcpponly
#
def helicsFederateRegisterGlobalEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
    f = loadSym("helicsFederateRegisterGlobalEndpoint")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an endpoint object from a name.
# *
# * @param fed The message federate object to use to get the endpoint.
# * @param name The name of the endpoint.
# * @forcpponly
# * @param[in,out] err The error object to complete if there is an error.
# * @endforcpponly
# *
# * @return A helics_endpoint object.
# * @forcpponly
# *         The object will not be valid and err will contain an error code if no endpoint with the specified name exists.
# * @endforcpponly
#
def helicsFederateGetEndpoint(fed: HelicsFederate, name: str) -> HelicsEndpoint:
    f = loadSym("helicsFederateGetEndpoint")
    err = lib.helicsErrorInitialize()
    result = f(fed, name, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an endpoint by its index, typically already created via registerInterfaces file or something of that nature.
# *
# * @param fed The federate object in which to create a publication.
# * @param index The index of the publication to get.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_endpoint.
# * @forcpponly
# *         It will be NULL if given an invalid index.
# * @endforcpponly
#
def helicsFederateGetEndpointByIndex(fed: HelicsFederate, index: int) -> HelicsEndpoint:
    f = loadSym("helicsFederateGetEndpointByIndex")
    err = lib.helicsErrorInitialize()
    result = f(fed, index.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Check if an endpoint is valid.
# *
# * @param endpoint The endpoint object to check.
# *
# * @return helics_true if the Endpoint object represents a valid endpoint.
#
def helicsEndpointIsValid(endpoint: HelicsEndpoint) -> HelicsBool:
    f = loadSym("helicsEndpointIsValid")
    result = f(endpoint)
    return result == 1


# *
# * Set the default destination for an endpoint if no other endpoint is given.
# *
# * @param endpoint The endpoint to set the destination for.
# * @param dest A string naming the desired default endpoint.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsEndpointSetDefaultDestination(endpoint: HelicsEndpoint, dest: str):
    f = loadSym("helicsEndpointSetDefaultDestination")
    err = lib.helicsErrorInitialize()
    f(endpoint, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the default destination for an endpoint.
# *
# * @param endpoint The endpoint to set the destination for.
# *
# * @return A string with the default destination.
#
def helicsEndpointGetDefaultDestination(endpoint: HelicsEndpoint) -> str:
    f = loadSym("helicsEndpointGetDefaultDestination")
    result = f(endpoint)
    return ffi.string(result).decode()


# *
# * Send a message to the specified destination.
# *
# * @param endpoint The endpoint to send the data from.
# * @param dest The target destination.
# * @forcpponly
# *             nullptr to use the default destination.
# * @endforcpponly
# * @beginpythononly
# *             "" to use the default destination.
# * @endpythononly
# * @param data The data to send.
# * @forcpponly
# * @param inputDataLength The length of the data to send.
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsEndpointSendMessageRaw(endpoint: HelicsEndpoint, dest: str, data: pointer, inputDataLength: int):
    f = loadSym("helicsEndpointSendMessageRaw")
    err = lib.helicsErrorInitialize()
    f(endpoint, cstring(dest), data, inputDataLength.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Send a message at a specific time to the specified destination.
# *
# * @param endpoint The endpoint to send the data from.
# * @param dest The target destination.
# * @forcpponly
# *             nullptr to use the default destination.
# * @endforcpponly
# * @beginpythononly
# *             "" to use the default destination.
# * @endpythononly
# * @param data The data to send.
# * @forcpponly
# * @param inputDataLength The length of the data to send.
# * @endforcpponly
# * @param time The time the message should be sent.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsEndpointSendEventRaw(
    endpoint: HelicsEndpoint, dest: str, data: pointer, inputDataLength: int, time: HelicsTime,
):
    f = loadSym("helicsEndpointSendEventRaw")
    err = lib.helicsErrorInitialize()
    f(endpoint, cstring(dest), data, inputDataLength.cint, time, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Send a message object from a specific endpoint.
# * @deprecated Use helicsEndpointSendMessageObject instead.
# * @param endpoint The endpoint to send the data from.
# * @param message The actual message to send.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsEndpointSendMessage(endpoint: HelicsEndpoint, message: HelicsMessage):
    f = loadSym("helicsEndpointSendMessage")
    err = lib.helicsErrorInitialize()
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Send a message object from a specific endpoint.
# *
# * @param endpoint The endpoint to send the data from.
# * @param message The actual message to send which will be copied.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsEndpointSendMessageObject(endpoint: HelicsEndpoint, message: HelicsMessageObject):
    f = loadSym("helicsEndpointSendMessageObject")
    err = lib.helicsErrorInitialize()
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Send a message object from a specific endpoint, the message will not be copied and the message object will no longer be valid
# * after the call.
# *
# * @param endpoint The endpoint to send the data from.
# * @param message The actual message to send which will be copied.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsEndpointSendMessageObjectZeroCopy(endpoint: HelicsEndpoint, message: HelicsMessageObject):
    f = loadSym("helicsEndpointSendMessageObjectZeroCopy")
    err = lib.helicsErrorInitialize()
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Subscribe an endpoint to a publication.
# *
# * @param endpoint The endpoint to use.
# * @param key The name of the publication.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsEndpointSubscribe(endpoint: HelicsEndpoint, key: str):
    f = loadSym("helicsEndpointSubscribe")
    err = lib.helicsErrorInitialize()
    f(endpoint, key, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Check if the federate has any outstanding messages.
# *
# * @param fed The federate to check.
# *
# * @return helics_true if the federate has a message waiting, helics_false otherwise.
#
def helicsFederateHasMessage(fed: HelicsFederate) -> HelicsBool:
    f = loadSym("helicsFederateHasMessage")
    f(fed)
    return result == 1


# *
# * Check if a given endpoint has any unread messages.
# *
# * @param endpoint The endpoint to check.
# *
# * @return helics_true if the endpoint has a message, helics_false otherwise.
#
def helicsEndpointHasMessage(endpoint: HelicsEndpoint) -> HelicsBool:
    f = loadSym("helicsEndpointHasMessage")
    f(endpoint)
    return result == 1


# *
# * Returns the number of pending receives for the specified destination endpoint.
# *
# * @param fed The federate to get the number of waiting messages from.
#
def helicsFederatePendingMessages(fed: HelicsFederate) -> int:
    f = loadSym("helicsFederatePendingMessages")
    f(fed)


# *
# * Returns the number of pending receives for all endpoints of a particular federate.
# *
# * @param endpoint The endpoint to query.
#
def helicsEndpointPendingMessages(endpoint: HelicsEndpoint) -> int:
    f = loadSym("helicsEndpointPendingMessages")
    f(endpoint)


# *
# * Receive a packet from a particular endpoint.
# *
# * @deprecated This function is deprecated and will be removed in Helics 3.0.
# *             Use helicsEndpointGetMessageObject instead.
# *
# * @param[in] endpoint The identifier for the endpoint.
# *
# * @return A message object.
#
def helicsEndpointGetMessage(endpoint: HelicsEndpoint) -> HelicsMessage:
    f = loadSym("helicsEndpointGetMessage")
    f(endpoint)


# *
# * Receive a packet from a particular endpoint.
# *
# * @param[in] endpoint The identifier for the endpoint.
# *
# * @return A message object.
#
def helicsEndpointGetMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject:
    f = loadSym("helicsEndpointGetMessageObject")
    f(endpoint)


# *
# * Create a new empty message object.
# *
# * @details The message is empty and isValid will return false since there is no data associated with the message yet.
# *
# * @param endpoint The endpoint object to associate the message with.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
# *
# * @return A new helics_message_object.
#
def helicsEndpointCreateMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject:
    f = loadSym("helicsEndpointCreateMessageObject")
    err = lib.helicsErrorInitialize()
    result = f(endpoint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Receive a communication message for any endpoint in the federate.
# *
# * @deprecated This function is deprecated and will be removed in Helics 3.0.
# *             Use helicsFederateGetMessageObject instead.
# *
# * @details The return order will be in order of endpoint creation.
# *          So all messages that are available for the first endpoint, then all for the second, and so on.
# *          Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival.
# *
# * @return A unique_ptr to a Message object containing the message data.
#
def helicsFederateGetMessage(fed: HelicsFederate) -> HelicsMessage:
    f = loadSym("helicsFederateGetMessage")
    f(fed)


# *
# * Receive a communication message for any endpoint in the federate.
# *
# * @details The return order will be in order of endpoint creation.
# *          So all messages that are available for the first endpoint, then all for the second, and so on.
# *          Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival.
# *
# * @return A helics_message_object which references the data in the message.
#
def helicsFederateGetMessageObject(fed: HelicsFederate) -> HelicsMessageObject:
    f = loadSym("helicsFederateGetMessageObject")
    f(fed)


# *
# * Create a new empty message object.
# *
# * @details The message is empty and isValid will return false since there is no data associated with the message yet.
# *
# * @param fed the federate object to associate the message with
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
# *
# * @return A helics_message_object containing the message data.
#
def helicsFederateCreateMessageObject(fed: HelicsFederate) -> HelicsMessageObject:
    f = loadSym("helicsFederateCreateMessageObject")
    err = lib.helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Clear all stored messages from a federate.
# *
# * @details This clears messages retrieved through helicsFederateGetMessage or helicsFederateGetMessageObject
# *
# * @param fed The federate to clear the message for.
#
def helicsFederateClearMessages(fed: HelicsFederate):
    f = loadSym("helicsFederateClearMessages")
    f(fed)


# *
# * Clear all message from an endpoint.
# *
# * @deprecated This function does nothing and will be removed.
# *             Use helicsFederateClearMessages to free all messages,
# *             or helicsMessageFree to clear an individual message.
# *
# * @param endpoint The endpoint object to operate on.
#
def helicsEndpointClearMessages(endpoint: HelicsEndpoint):
    f = loadSym("helicsEndpointClearMessages")
    f(endpoint)


# *
# * Get the type specified for an endpoint.
# *
# * @param endpoint The endpoint object in question.
# *
# * @return The defined type of the endpoint.
#
def helicsEndpointGetType(endpoint: HelicsEndpoint) -> str:
    f = loadSym("helicsEndpointGetType")
    result = f(endpoint)
    return ffi.string(result).decode()


# *
# * Get the name of an endpoint.
# *
# * @param endpoint The endpoint object in question.
# *
# * @return The name of the endpoint.
#
def helicsEndpointGetName(endpoint: HelicsEndpoint) -> str:
    f = loadSym("helicsEndpointGetName")
    result = f(endpoint)
    return ffi.string(result).decode()


# *
# * Get the number of endpoints in a federate.
# *
# * @param fed The message federate to query.
# *
# * @return (-1) if fed was not a valid federate, otherwise returns the number of endpoints.
#
def helicsFederateGetEndpointCount(fed: HelicsFederate) -> int:
    f = loadSym("helicsFederateGetEndpointCount")
    result = f(fed).int


# *
# * Get the data in the info field of a filter.
# *
# * @param end The filter to query.
# *
# * @return A string with the info field string.
#
def helicsEndpointGetInfo(endpoint: HelicsEndpoint) -> str:
    f = loadSym("helicsEndpointGetInfo")
    result = f(endpoint)
    return ffi.string(result).decode()


# *
# * Set the data in the info field for a filter.
# *
# * @param end The endpoint to query.
# * @param info The string to set.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsEndpointSetInfo(endpoint: HelicsEndpoint, info: str):
    f = loadSym("helicsEndpointSetInfo")
    err = lib.helicsErrorInitialize()
    f(endpoint, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set a handle option on an endpoint.
# *
# * @param end The endpoint to modify.
# * @param option Integer code for the option to set /ref helics_handle_options.
# * @param value The value to set the option to.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsEndpointSetOption(endpoint: HelicsEndpoint, option: int, value: int):
    f = loadSym("helicsEndpointSetOption")
    err = lib.helicsErrorInitialize()
    f(endpoint, option.cint, value.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set a handle option on an endpoint.
# *
# * @param end The endpoint to modify.
# * @param option Integer code for the option to set /ref helics_handle_options.
# * @return the value of the option, for boolean options will be 0 or 1
#
def helicsEndpointGetOption(endpoint: HelicsEndpoint, option: int) -> int:
    f = loadSym("helicsEndpointGetOption")
    result = f(endpoint, option.cint).int


# *
# * \defgroup Message operation functions
# * @details Functions for working with helics message envelopes.
# * @{
#
# *
# * Get the source endpoint of a message.
# *
# * @param message The message object in question.
# *
# * @return A string with the source endpoint.
#
def helicsMessageGetSource(message: HelicsMessageObject) -> str:
    f = loadSym("helicsMessageGetSource")
    result = f(message)
    return ffi.string(result).decode()


# *
# * Get the destination endpoint of a message.
# *
# * @param message The message object in question.
# *
# * @return A string with the destination endpoint.
#
def helicsMessageGetDestination(message: HelicsMessageObject) -> str:
    f = loadSym("helicsMessageGetDestination")
    result = f(message)
    return ffi.string(result).decode()


# *
# * Get the original source endpoint of a message, the source may have been modified by filters or other actions.
# *
# * @param message The message object in question.
# *
# * @return A string with the source of a message.
#
def helicsMessageGetOriginalSource(message: HelicsMessageObject) -> str:
    f = loadSym("helicsMessageGetOriginalSource")
    result = f(message)
    return ffi.string(result).decode()


# *
# * Get the original destination endpoint of a message, the destination may have been modified by filters or other actions.
# *
# * @param message The message object in question.
# *
# * @return A string with the original destination of a message.
#
def helicsMessageGetOriginalDestination(message: HelicsMessageObject) -> str:
    f = loadSym("helicsMessageGetOriginalDestination")
    result = f(message)
    return ffi.string(result).decode()


# *
# * Get the helics time associated with a message.
# *
# * @param message The message object in question.
# *
# * @return The time associated with a message.
#
def helicsMessageGetTime(message: HelicsMessageObject) -> HelicsTime:
    f = loadSym("helicsMessageGetTime")
    result = f(message)


# *
# * Get the payload of a message as a string.
# *
# * @param message The message object in question.
# *
# * @return A string representing the payload of a message.
#
def helicsMessageGetString(message: HelicsMessageObject) -> str:
    f = loadSym("helicsMessageGetString")
    result = f(message)
    return ffi.string(result).decode()


# *
# * Get the messageID of a message.
# *
# * @param message The message object in question.
# *
# * @return The messageID.
#
def helicsMessageGetMessageID(message: HelicsMessageObject) -> int:
    f = loadSym("helicsMessageGetMessageID")
    result = f(message).int


# *
# * Check if a flag is set on a message.
# *
# * @param message The message object in question.
# * @param flag The flag to check should be between [0,15].
# *
# * @return The flags associated with a message.
#
def helicsMessageCheckFlag(message: HelicsMessageObject, flag: int) -> HelicsBool:
    f = loadSym("helicsMessageCheckFlag")
    result = f(message, flag.cint)
    return result == 1


# *
# * Get the size of the data payload in bytes.
# *
# * @param message The message object in question.
# *
# * @return The size of the data payload.
#
def helicsMessageGetRawDataSize(message: HelicsMessageObject) -> int:
    f = loadSym("helicsMessageGetRawDataSize")
    result = f(message).int


# *
# * Get the raw data for a message object.
# *
# * @param message A message object to get the data for.
# * @forcpponly
# * @param[out] data The memory location of the data.
# * @param maxMessagelen The maximum size of information that data can hold.
# * @param[out] actualSize The actual length of data copied to data.
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @beginPythonOnly
# * @return Raw string data.
# * @endPythonOnly
#
def helicsMessageGetRawData(
    message: HelicsMessageObject, data: pointer, maxMessagelen: int, actualSize: int, err: HelicsError,
):
    f = loadSym("helicsMessageGetRawData")
    err = lib.helicsErrorInitialize()
    f(message, data, maxMessagelen.cint, actualSize, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a pointer to the raw data of a message.
# *
# * @param message A message object to get the data for.
# *
# * @return A pointer to the raw data in memory, the pointer may be NULL if the message is not a valid message.
#
def helicsMessageGetRawDataPointer(message: HelicsMessageObject) -> pointer:
    f = loadSym("helicsMessageGetRawDataPointer")
    result = f(message)


# *
# * A check if the message contains a valid payload.
# *
# * @param message The message object in question.
# *
# * @return helics_true if the message contains a payload.
#
def helicsMessageIsValid(message: HelicsMessageObject) -> HelicsBool:
    f = loadSym("helicsMessageIsValid")
    result = f(message)
    return result == 1


# *
# * Set the source of a message.
# *
# * @param message The message object in question.
# * @param src A string containing the source.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetSource(message: HelicsMessageObject, src: str):
    f = loadSym("helicsMessageSetSource")
    err = lib.helicsErrorInitialize()
    f(message, cstring(src), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the destination of a message.
# *
# * @param message The message object in question.
# * @param dest A string containing the new destination.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetDestination(message: HelicsMessageObject, dest: str):
    f = loadSym("helicsMessageSetDestination")
    err = lib.helicsErrorInitialize()
    f(message, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the original source of a message.
# *
# * @param message The message object in question.
# * @param src A string containing the new original source.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetOriginalSource(message: HelicsMessageObject, src: str):
    f = loadSym("helicsMessageSetOriginalSource")
    err = lib.helicsErrorInitialize()
    f(message, cstring(src), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the original destination of a message.
# *
# * @param message The message object in question.
# * @param dest A string containing the new original source.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetOriginalDestination(message: HelicsMessageObject, dest: str):
    f = loadSym("helicsMessageSetOriginalDestination")
    err = lib.helicsErrorInitialize()
    f(message, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the delivery time for a message.
# *
# * @param message The message object in question.
# * @param time The time the message should be delivered.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetTime(message: HelicsMessageObject, time: HelicsTime):
    f = loadSym("helicsMessageSetTime")
    err = lib.helicsErrorInitialize()
    f(message, time, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Resize the data buffer for a message.
# *
# * @details The message data buffer will be resized. There are no guarantees on what is in the buffer in newly allocated space.
# *          If the allocated space is not sufficient new allocations will occur.
# *
# * @param message The message object in question.
# * @param newSize The new size in bytes of the buffer.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageResize(message: HelicsMessageObject, newSize: int):
    f = loadSym("helicsMessageResize")
    err = lib.helicsErrorInitialize()
    f(message, newSize.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Reserve space in a buffer but don't actually resize.
# *
# * @details The message data buffer will be reserved but not resized.
# *
# * @param message The message object in question.
# * @param reserveSize The number of bytes to reserve in the message object.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageReserve(message: HelicsMessageObject, reserveSize: int):
    f = loadSym("helicsMessageReserve")
    err = lib.helicsErrorInitialize()
    f(message, reserveSize.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the message ID for the message.
# *
# * @details Normally this is not needed and the core of HELICS will adjust as needed.
# *
# * @param message The message object in question.
# * @param messageID A new message ID.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetMessageID(message: HelicsMessageObject, messageID: int):
    f = loadSym("helicsMessageSetMessageID")
    err = lib.helicsErrorInitialize()
    f(message, messageID.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Clear the flags of a message.
# *
# * @param message The message object in question
#
def helicsMessageClearFlags(message: HelicsMessageObject):
    f = loadSym("helicsMessageClearFlags")
    f(message)


# *
# * Set a flag on a message.
# *
# * @param message The message object in question.
# * @param flag An index of a flag to set on the message.
# * @param flagValue The desired value of the flag.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetFlagOption(message: HelicsMessageObject, flag: int, flagValue: HelicsBool):
    f = loadSym("helicsMessageSetFlagOption")
    err = lib.helicsErrorInitialize()
    f(message, flag.cint, flagValue, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the data payload of a message as a string.
# *
# * @param message The message object in question.
# * @param str A string containing the message data.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetString(message: HelicsMessageObject, str: str):
    f = loadSym("helicsMessageSetString")
    err = lib.helicsErrorInitialize()
    f(message, cstring(str), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the data payload of a message as raw data.
# *
# * @param message The message object in question.
# * @param data A string containing the message data.
# * @param inputDataLength The length of the data to input.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageSetData(message: HelicsMessageObject, data: pointer, inputDataLength: int):
    f = loadSym("helicsMessageSetData")
    err = lib.helicsErrorInitialize()
    f(message, data, inputDataLength.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Append data to the payload.
# *
# * @param message The message object in question.
# * @param data A string containing the message data to append.
# * @param inputDataLength The length of the data to input.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageAppendData(message: HelicsMessageObject, data: pointer, inputDataLength: int):
    f = loadSym("helicsMessageAppendData")
    err = lib.helicsErrorInitialize()
    f(message, data, inputDataLength.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Copy a message object.
# *
# * @param source_message The message object to copy from.
# * @param dest_message The message object to copy to.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageCopy(source_message: HelicsMessageObject, dest_message: HelicsMessageObject):
    f = loadSym("helicsMessageCopy")
    err = lib.helicsErrorInitialize()
    f(source_message, dest_message, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Clone a message object.
# *
# * @param message The message object to copy from.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsMessageClone(message: HelicsMessageObject) -> HelicsMessageObject:
    f = loadSym("helicsMessageClone")
    err = lib.helicsErrorInitialize()
    result = f(message, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Free a message object from memory
# * @details memory for message is managed so not using this function does not create memory leaks, this is an indication
# * to the system that the memory for this message is done being used and can be reused for a new message.
# * helicsFederateClearMessages() can also be used to clear up all stored messages at once
#
def helicsMessageFree(message: HelicsMessageObject):
    f = loadSym("helicsMessageFree")
    f(message)


# *@}
#
# Copyright (c) 2017-2020,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable Energy, LLC.  See the top-level NOTICE for
# additional details. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
#
# *
# * @file
# *
# @brief Functions related to message filters for the C api
#
# *
# * Create a source Filter on the specified federate.
# *
# * @details Filters can be created through a federate or a core, linking through a federate allows
# *          a few extra features of name matching to function on the federate interface but otherwise equivalent behavior
# *
# * @param fed The federate to register through.
# * @param type The type of filter to create /ref helics_filter_type.
# * @param name The name of the filter (can be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_filter object.
#
def helicsFederateRegisterFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    f = loadSym("helicsFederateRegisterFilter")
    err = lib.helicsErrorInitialize()
    result = f(fed, type, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a global source filter through a federate.
# *
# * @details Filters can be created through a federate or a core, linking through a federate allows
# *          a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.
# *
# * @param fed The federate to register through.
# * @param type The type of filter to create /ref helics_filter_type.
# * @param name The name of the filter (can be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_filter object.
#
def helicsFederateRegisterGlobalFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    f = loadSym("helicsFederateRegisterGlobalFilter")
    err = lib.helicsErrorInitialize()
    result = f(fed, type, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a cloning Filter on the specified federate.
# *
# * @details Cloning filters copy a message and send it to multiple locations, source and destination can be added
# *          through other functions.
# *
# * @param fed The federate to register through.
# * @param name The name of the filter (can be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_filter object.
#
def helicsFederateRegisterCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    f = loadSym("helicsFederateRegisterCloningFilter")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a global cloning Filter on the specified federate.
# *
# * @details Cloning filters copy a message and send it to multiple locations, source and destination can be added
# *          through other functions.
# *
# * @param fed The federate to register through.
# * @param name The name of the filter (can be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_filter object.
#
def helicsFederateRegisterGlobalCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    f = loadSym("helicsFederateRegisterGlobalCloningFilter")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a source Filter on the specified core.
# *
# * @details Filters can be created through a federate or a core, linking through a federate allows
# *          a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.
# *
# * @param core The core to register through.
# * @param type The type of filter to create /ref helics_filter_type.
# * @param name The name of the filter (can be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_filter object.
#
def helicsCoreRegisterFilter(core: HelicsCore, type: HelicsFilterType, name: str) -> HelicsFilter:
    f = loadSym("helicsCoreRegisterFilter")
    err = lib.helicsErrorInitialize()
    result = f(core, type, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Create a cloning Filter on the specified core.
# *
# * @details Cloning filters copy a message and send it to multiple locations, source and destination can be added
# *          through other functions.
# *
# * @param core The core to register through.
# * @param name The name of the filter (can be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_filter object.
#
def helicsCoreRegisterCloningFilter(core: HelicsCore, name: str) -> HelicsFilter:
    f = loadSym("helicsCoreRegisterCloningFilter")
    err = lib.helicsErrorInitialize()
    result = f(core, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the number of filters registered through a federate.
# *
# * @param fed The federate object to use to get the filter.
# *
# * @return A count of the number of filters registered through a federate.
#
def helicsFederateGetFilterCount(fed: HelicsFederate) -> int:
    f = loadSym("helicsFederateGetFilterCount")
    f(fed)


# *
# * Get a filter by its name, typically already created via registerInterfaces file or something of that nature.
# *
# * @param fed The federate object to use to get the filter.
# * @param name The name of the filter.
# * @forcpponly
# * @param[in,out] err The error object to complete if there is an error.
# * @endforcpponly
# *
# * @return A helics_filter object, the object will not be valid and err will contain an error code if no filter with the specified name
# * exists.
#
def helicsFederateGetFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    f = loadSym("helicsFederateGetFilter")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a filter by its index, typically already created via registerInterfaces file or something of that nature.
# *
# * @param fed The federate object in which to create a publication.
# * @param index The index of the publication to get.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_filter, which will be NULL if an invalid index is given.
#
def helicsFederateGetFilterByIndex(fed: HelicsFederate, index: int) -> HelicsFilter:
    f = loadSym("helicsFederateGetFilterByIndex")
    err = lib.helicsErrorInitialize()
    result = f(fed, index.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Check if a filter is valid.
# *
# * @param filt The filter object to check.
# *
# * @return helics_true if the Filter object represents a valid filter.
#
def helicsFilterIsValid(filt: HelicsFilter) -> HelicsBool:
    f = loadSym("helicsFilterIsValid")
    result = f(filt)
    return result == 1


# *
# * Get the name of the filter and store in the given string.
# *
# * @param filt The given filter.
# *
# * @return A string with the name of the filter.
#
def helicsFilterGetName(filt: HelicsFilter) -> str:
    f = loadSym("helicsFilterGetName")
    result = f(filt)
    return ffi.string(result).decode()


# *
# * Set a property on a filter.
# *
# * @param filt The filter to modify.
# * @param prop A string containing the property to set.
# * @param val A numerical value for the property.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFilterSet(filt: HelicsFilter, prop: str, val: float):
    f = loadSym("helicsFilterSet")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(prop), val.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set a string property on a filter.
# *
# * @param filt The filter to modify.
# * @param prop A string containing the property to set.
# * @param val A string containing the new value.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFilterSetString(filt: HelicsFilter, prop: str, val: str):
    f = loadSym("helicsFilterSetString")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(prop), cstring(val), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Add a destination target to a filter.
# *
# * @details All messages going to a destination are copied to the delivery address(es).
# * @param filt The given filter to add a destination target to.
# * @param dest The name of the endpoint to add as a destination target.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFilterAddDestinationTarget(filt: HelicsFilter, dest: str):
    f = loadSym("helicsFilterAddDestinationTarget")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Add a source target to a filter.
# *
# * @details All messages coming from a source are copied to the delivery address(es).
# *
# * @param filt The given filter.
# * @param source The name of the endpoint to add as a source target.
# * @forcpponly.
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFilterAddSourceTarget(filt: HelicsFilter, source: str):
    f = loadSym("helicsFilterAddSourceTarget")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(source), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * \defgroup Clone filter functions
# * @details Functions that manipulate cloning filters in some way.
# * @{
#
# *
# * Add a delivery endpoint to a cloning filter.
# *
# * @details All cloned messages are sent to the delivery address(es).
# *
# * @param filt The given filter.
# * @param deliveryEndpoint The name of the endpoint to deliver messages to.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFilterAddDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
    f = loadSym("helicsFilterAddDeliveryEndpoint")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(deliveryEndpoint), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Remove a destination target from a filter.
# *
# * @param filt The given filter.
# * @param target The named endpoint to remove as a target.
# * @forcpponly
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFilterRemoveTarget(filt: HelicsFilter, target: str):
    f = loadSym("helicsFilterRemoveTarget")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Remove a delivery destination from a cloning filter.
# *
# * @param filt The given filter (must be a cloning filter).
# * @param deliveryEndpoint A string with the delivery endpoint to remove.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsFilterRemoveDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
    f = loadSym("helicsFilterRemoveDeliveryEndpoint")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(deliveryEndpoint), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the data in the info field of a filter.
# *
# * @param filt The given filter.
# *
# * @return A string with the info field string.
#
def helicsFilterGetInfo(filt: HelicsFilter) -> str:
    f = loadSym("helicsFilterGetInfo")
    result = f(filt)
    return ffi.string(result).decode()


# *
# * Set the data in the info field for a filter.
# *
# * @param filt The given filter.
# * @param info The string to set.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsFilterSetInfo(filt: HelicsFilter, info: str):
    f = loadSym("helicsFilterSetInfo")
    err = lib.helicsErrorInitialize()
    f(filt, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the data in the info field for a filter.
# *
# * @param filt The given filter.
# * @param option The option to set /ref helics_handle_options.
# * @param value The value of the option commonly 0 for false 1 for true.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsFilterSetOption(filt: HelicsFilter, option: int, value: int):
    f = loadSym("helicsFilterSetOption")
    err = lib.helicsErrorInitialize()
    f(filt, option.cint, value.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a handle option for the filter.
# *
# * @param filt The given filter to query.
# * @param option The option to query /ref helics_handle_options.
#
def helicsFilterGetOption(filt: HelicsFilter, option: int) -> int:
    f = loadSym("helicsFilterGetOption")
    result = f(filt, option.cint).int


# *
# * @}
#
#
# Copyright (c) 2017-2020,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable Energy, LLC.  See the top-level NOTICE for
# additional details. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
#
# *
# * @file
# *
# * @brief Functions related to value federates for the C api
#
# *
# * sub/pub registration
#
# *
# * Create a subscription.
# *
# * @details The subscription becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions and publications.
# *
# * @param fed The federate object in which to create a subscription, must have been created with /ref helicsCreateValueFederate or
# * /ref helicsCreateCombinationFederate.
# * @param key The identifier matching a publication to get a subscription for.
# * @param units A string listing the units of the subscription (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the subscription.
#
def helicsFederateRegisterSubscription(fed: HelicsFederate, key: str, units: str) -> HelicsInput:
    f = loadSym("helicsFederateRegisterSubscription")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register a publication with a known type.
# *
# * @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions and publications.
# *
# * @param fed The federate object in which to create a publication.
# * @param key The identifier for the publication the global publication key will be prepended with the federate name.
# * @param type A code identifying the type of the input see /ref helics_data_type for available options.
# * @param units A string listing the units of the subscription (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the publication.
#
def helicsFederateRegisterPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication:
    f = loadSym("helicsFederateRegisterPublication")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register a publication with a defined type.
# *
# * @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions and publications.
# *
# * @param fed The federate object in which to create a publication.
# * @param key The identifier for the publication.
# * @param type A string labeling the type of the publication.
# * @param units A string listing the units of the subscription (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the publication.
#
def helicsFederateRegisterTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    f = loadSym("helicsFederateRegisterTypePublication")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register a global named publication with an arbitrary type.
# *
# * @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions and publications.
# *
# * @param fed The federate object in which to create a publication.
# * @param key The identifier for the publication.
# * @param type A code identifying the type of the input see /ref helics_data_type for available options.
# * @param units A string listing the units of the subscription (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the publication.
#
def helicsFederateRegisterGlobalPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication:
    f = loadSym("helicsFederateRegisterGlobalPublication")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register a global publication with a defined type.
# *
# * @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions and publications.
# *
# * @param fed The federate object in which to create a publication.
# * @param key The identifier for the publication.
# * @param type A string describing the expected type of the publication.
# * @param units A string listing the units of the subscription (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the publication.
#
def helicsFederateRegisterGlobalTypePublication(fed: HelicsFederate, key: str, type: str, units: str, err: HelicsError) -> HelicsPublication:
    f = loadSym("helicsFederateRegisterGlobalTypePublication")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register a named input.
# *
# * @details The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions, inputs, and publications.
# *
# * @param fed The federate object in which to create an input.
# * @param key The identifier for the publication the global input key will be prepended with the federate name.
# * @param type A code identifying the type of the input see /ref helics_data_type for available options.
# * @param units A string listing the units of the input (may be NULL).
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the input.
#
def helicsFederateRegisterInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsInput:
    f = loadSym("helicsFederateRegisterInput")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register an input with a defined type.
# *
# * @details The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions, inputs, and publications.
# *
# * @param fed The federate object in which to create an input.
# * @param key The identifier for the input.
# * @param type A string describing the expected type of the input.
# * @param units A string listing the units of the input maybe NULL.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the publication.
#
def helicsFederateRegisterTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsInput:
    f = loadSym("helicsFederateRegisterTypeInput")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register a global named input.
# *
# * @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions and publications.
# *
# * @param fed The federate object in which to create a publication.
# * @param key The identifier for the publication.
# * @param type A code identifying the type of the input see /ref helics_data_type for available options.
# * @param units A string listing the units of the subscription maybe NULL.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the publication.
#
def helicsFederateRegisterGlobalInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication:
    f = loadSym("helicsFederateRegisterGlobalInput")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), type, cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Register a global publication with an arbitrary type.
# *
# * @details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
# * functions for subscriptions and publications.
# *
# * @param fed The federate object in which to create a publication.
# * @param key The identifier for the publication.
# * @param type A string defining the type of the input.
# * @param units A string listing the units of the subscription maybe NULL.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An object containing the publication.
#
def helicsFederateRegisterGlobalTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    f = loadSym("helicsFederateRegisterGlobalTypeInput")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a publication object from a key.
# *
# * @param fed The value federate object to use to get the publication.
# * @param key The name of the publication.
# * @forcpponly
# * @param[in,out] err The error object to complete if there is an error.
# * @endforcpponly
# *
# * @return A helics_publication object, the object will not be valid and err will contain an error code if no publication with the
# * specified key exists.
#
def helicsFederateGetPublication(fed: HelicsFederate, key: str) -> HelicsPublication:
    f = loadSym("helicsFederateGetPublication")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a publication by its index, typically already created via registerInterfaces file or something of that nature.
# *
# * @param fed The federate object in which to create a publication.
# * @param index The index of the publication to get.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_publication.
#
def helicsFederateGetPublicationByIndex(fed: HelicsFederate, index: int) -> HelicsPublication:
    f = loadSym("helicsFederateGetPublicationByIndex")
    err = lib.helicsErrorInitialize()
    result = f(fed, index.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an input object from a key.
# *
# * @param fed The value federate object to use to get the publication.
# * @param key The name of the input.
# * @forcpponly
# * @param[in,out] err The error object to complete if there is an error.
# * @endforcpponly
# *
# * @return A helics_input object, the object will not be valid and err will contain an error code if no input with the specified
# * key exists.
#
def helicsFederateGetInput(fed: HelicsFederate, key: str) -> HelicsInput:
    f = loadSym("helicsFederateGetInput")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an input by its index, typically already created via registerInterfaces file or something of that nature.
# *
# * @param fed The federate object in which to create a publication.
# * @param index The index of the publication to get.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A helics_input, which will be NULL if an invalid index.
#
def helicsFederateGetInputByIndex(fed: HelicsFederate, index: int) -> HelicsInput:
    f = loadSym("helicsFederateGetInputByIndex")
    err = lib.helicsErrorInitialize()
    result = f(fed, index.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an input object from a subscription target.
# *
# * @param fed The value federate object to use to get the publication.
# * @param key The name of the publication that a subscription is targeting.
# * @forcpponly
# * @param[in,out] err The error object to complete if there is an error.
# * @endforcpponly
# *
# * @return A helics_input object, the object will not be valid and err will contain an error code if no input with the specified
# * key exists.
#
def helicsFederateGetSubscription(fed: HelicsFederate, key: str) -> HelicsInput:
    f = loadSym("helicsFederateGetSubscription")
    err = lib.helicsErrorInitialize()
    result = f(fed, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Clear all the update flags from a federates inputs.
# *
# * @param fed The value federate object for which to clear update flags.
#
def helicsFederateClearUpdates(fed: HelicsFederate):
    f = loadSym("helicsFederateClearUpdates")
    f(fed)


# *
# * Register the publications via JSON publication string.
# *
# * @param fed The value federate object to use to register the publications.
# * @param json The JSON publication string.
# * @forcpponly
# * @param[in,out] err The error object to complete if there is an error.
# * @endforcpponly
# *
# * @details This would be the same JSON that would be used to publish data.
#
def helicsFederateRegisterFromPublicationJSON(fed: HelicsFederate, json: str):
    f = loadSym("helicsFederateRegisterFromPublicationJSON")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish data contained in a JSON file or string.
# *
# * @param fed The value federate object through which to publish the data.
# * @param json The publication file name or literal JSON data string.
# * @forcpponly
# * @param[in,out] err The error object to complete if there is an error.
# * @endforcpponly
#
def helicsFederatePublishJSON(fed: HelicsFederate, json: str):
    f = loadSym("helicsFederatePublishJSON")
    err = lib.helicsErrorInitialize()
    f(fed, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * \defgroup publications Publication functions
# * @details Functions for publishing data of various kinds.
# * The data will get translated to the type specified when the publication was constructed automatically
# * regardless of the function used to publish the data.
# * @{
#
# *
# * Check if a publication is valid.
# *
# * @param pub The publication to check.
# *
# * @return helics_true if the publication is a valid publication.
#
def helicsPublicationIsValid(pub: HelicsPublication) -> HelicsBool:
    f = loadSym("helicsPublicationIsValid")
    result = f(pub)
    return result == 1


# *
# * Publish raw data from a char * and length.
# *
# * @param pub The publication to publish for.
# * @param data A pointer to the raw data.
# * @param inputDataLength The size in bytes of the data to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishRaw(pub: HelicsPublication, data: pointer, inputDataLength: int):
    f = loadSym("helicsPublicationPublishRaw")
    err = lib.helicsErrorInitialize()
    f(pub, data, inputDataLength.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a string.
# *
# * @param pub The publication to publish for.
# * @param str The string to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishString(pub: HelicsPublication, str: str):
    f = loadSym("helicsPublicationPublishString")
    err = lib.helicsErrorInitialize()
    f(pub, cstring(str), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish an integer value.
# *
# * @param pub The publication to publish for.
# * @param val The numerical value to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishInteger(pub: HelicsPublication, val: int):
    f = loadSym("helicsPublicationPublishInteger")
    err = lib.helicsErrorInitialize()
    f(pub, val.int64, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a Boolean Value.
# *
# * @param pub The publication to publish for.
# * @param val The boolean value to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishBoolean(pub: HelicsPublication, val: HelicsBool):
    f = loadSym("helicsPublicationPublishBoolean")
    err = lib.helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a double floating point value.
# *
# * @param pub The publication to publish for.
# * @param val The numerical value to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishDouble(pub: HelicsPublication, val: float):
    f = loadSym("helicsPublicationPublishDouble")
    err = lib.helicsErrorInitialize()
    f(pub, val.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a time value.
# *
# * @param pub The publication to publish for.
# * @param val The numerical value to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishTime(pub: HelicsPublication, val: HelicsTime):
    f = loadSym("helicsPublicationPublishTime")
    err = lib.helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a single character.
# *
# * @param pub The publication to publish for.
# * @param val The numerical value to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishChar(pub: HelicsPublication, val: str):
    f = loadSym("helicsPublicationPublishChar")
    err = lib.helicsErrorInitialize()
    f(pub, val.cchar, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a complex value (or pair of values).
# *
# * @param pub The publication to publish for.
# * @param real The real part of a complex number to publish.
# * @param imag The imaginary part of a complex number to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishComplex(pub: HelicsPublication, real: float, imag: float):
    f = loadSym("helicsPublicationPublishComplex")
    err = lib.helicsErrorInitialize()
    f(pub, real.cdouble, imag.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a vector of doubles.
# *
# * @param pub The publication to publish for.
# * @param vectorInput A pointer to an array of double data.
# * @forcpponly
# * @param vectorLength The number of points to publish.
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishVector(pub: HelicsPublication, vectorInput: float, vectorLength: int):
    f = loadSym("helicsPublicationPublishVector")
    err = lib.helicsErrorInitialize()
    f(pub, vectorInput, vectorLength.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Publish a named point.
# *
# * @param pub The publication to publish for.
# * @param str A string for the name to publish.
# * @param val A double for the value to publish.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationPublishNamedPoint(pub: HelicsPublication, str: str, val: float):
    f = loadSym("helicsPublicationPublishNamedPoint")
    err = lib.helicsErrorInitialize()
    f(pub, cstring(str), val.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Add a named input to the list of targets a publication publishes to.
# *
# * @param pub The publication to add the target for.
# * @param target The name of an input that the data should be sent to.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsPublicationAddTarget(pub: HelicsPublication, target: str):
    f = loadSym("helicsPublicationAddTarget")
    err = lib.helicsErrorInitialize()
    f(pub, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Check if an input is valid.
# *
# * @param ipt The input to check.
# *
# * @return helics_true if the Input object represents a valid input.
#
def helicsInputIsValid(ipt: HelicsInput) -> HelicsBool:
    f = loadSym("helicsInputIsValid")
    result = f(ipt)
    return result == 1


# *
# * Add a publication to the list of data that an input subscribes to.
# *
# * @param ipt The named input to modify.
# * @param target The name of a publication that an input should subscribe to.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
#
def helicsInputAddTarget(ipt: HelicsInput, target: str):
    f = loadSym("helicsInputAddTarget")
    err = lib.helicsErrorInitialize()
    f(ipt, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *@}
# *
# * \defgroup getValue GetValue functions
# * @details Data can be returned in a number of formats,  for instance if data is published as a double it can be returned as a string and
# * vice versa,  not all translations make that much sense but they do work.
# * @{
#
# *
# * Get the size of the raw value for subscription.
# *
# * @return The size of the raw data/string in bytes.
#
def helicsInputGetRawValueSize(ipt: HelicsInput) -> int:
    f = loadSym("helicsInputGetRawValueSize")
    result = f(ipt).int


# *
# * Get the raw data for the latest value of a subscription.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[out] data The memory location of the data
# * @param maxDatalen The maximum size of information that data can hold.
# * @param[out] actualSize The actual length of data copied to data.
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @beginPythonOnly
# * @return Raw string data.
# * @endPythonOnly
#
def helicsInputGetRawValue(ipt: HelicsInput, data: pointer, maxDatalen: int, actualSize: int):
    f = loadSym("helicsInputGetRawValue")
    err = lib.helicsErrorInitialize()
    f(ipt, data, maxDatalen.cint, actualSize, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the size of a value for subscription assuming return as a string.
# *
# * @return The size of the string.
#
def helicsInputGetStringSize(ipt: HelicsInput) -> int:
    f = loadSym("helicsInputGetStringSize")
    result = f(ipt).int


# *
# * Get a string value from a subscription.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[out] outputString Storage for copying a null terminated string.
# * @param maxStringLen The maximum size of information that str can hold.
# * @param[out] actualLength The actual length of the string.
# * @param[in,out] err Error term for capturing errors.
# * @endforcpponly
# *
# * @beginPythonOnly
# * @return A string data
# * @endPythonOnly
#
def helicsInputGetString(ipt: HelicsInput, outputString: str, maxStringLen: int, actualLength: int):
    f = loadSym("helicsInputGetString")
    err = lib.helicsErrorInitialize()
    f(ipt, outputString, maxStringLen.cint, actualLength, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get an integer value from a subscription.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return An int64_t value with the current value of the input.
#
def helicsInputGetInteger(ipt: HelicsInput) -> int:
    f = loadSym("helicsInputGetInteger")
    err = lib.helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a boolean value from a subscription.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return A boolean value of current input value.
#
def helicsInputGetBoolean(ipt: HelicsInput) -> HelicsBool:
    f = loadSym("helicsInputGetBoolean")
    err = lib.helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return result == 1


# *
# * Get a double value from a subscription.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return The double value of the input.
#
def helicsInputGetDouble(ipt: HelicsInput) -> float:
    f = loadSym("helicsInputGetDouble")
    err = lib.helicsErrorInitialize()
    result = f(ipt, err).float
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a time value from a subscription.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return The resulting time value.
#
def helicsInputGetTime(ipt: HelicsInput) -> HelicsTime:
    f = loadSym("helicsInputGetTime")
    err = lib.helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a single character value from an input.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[in,out] err A pointer to an error object for catching errors.
# * @endforcpponly
# *
# * @return The resulting character value.
# * @forcpponly
# *         NAK (negative acknowledgment) symbol returned on error
# * @endforcpponly
#
def helicsInputGetChar(ipt: HelicsInput) -> str:
    f = loadSym("helicsInputGetChar")
    err = lib.helicsErrorInitialize()
    result = f(ipt, err).char
    if err.error_code != 0:
        raise HelicsException(err.message)
    else:
        return ffi.string(result).decode()


# *
# * Get a complex object from an input object.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[in,out] err A helics error object, if the object is not empty the function is bypassed otherwise it is filled in if there is an
# * error.
# * @endforcpponly
# *
# * @return A helics_complex structure with the value.
#
def helicsInputGetComplexObject(ipt: HelicsInput) -> HelicsComplex:
    f = loadSym("helicsInputGetComplexObject")
    err = lib.helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get a pair of double forming a complex number from a subscriptions.
# *
# * @param ipt The input to get the data for.
# * @forcpponly
# * @param[out] real Memory location to place the real part of a value.
# * @param[out] imag Memory location to place the imaginary part of a value.
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * On error the values will not be altered.
# * @endforcpponly
# *
# * @beginPythonOnly
# * @return a pair of floating point values that represent the real and imag values
# * @endPythonOnly
#
def helicsInputGetComplex(ipt: HelicsInput, real: float, imag: float):
    f = loadSym("helicsInputGetComplex")
    err = lib.helicsErrorInitialize()
    f(ipt, real, imag, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the size of a value for subscription assuming return as an array of doubles.
# *
# * @return The number of doubles in a returned vector.
#
def helicsInputGetVectorSize(ipt: HelicsInput) -> int:
    f = loadSym("helicsInputGetVectorSize")
    f(ipt)


# *
# * Get a vector from a subscription.
# *
# * @param ipt The input to get the result for.
# * @forcpponly
# * @param[out] data The location to store the data.
# * @param maxlen The maximum size of the vector.
# * @param[out] actualSize Location to place the actual length of the resulting vector.
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @beginPythonOnly
# * @return a list of floating point values
# * @endPythonOnly
#
# Declaration 'helicsInputGetVector' skipped
# Declaration 'ipt' skipped
# Declaration 'helicsInputGetVector' skipped
# Declaration 'ipt' skipped
# Declaration 'data' skipped
# Declaration 'maxlen' skipped
# Declaration 'actualSize' skipped
# Declaration 'err' skipped

# *
# * Get a named point from a subscription.
# *
# * @param ipt The input to get the result for.
# * @forcpponly
# * @param[out] outputString Storage for copying a null terminated string.
# * @param maxStringLen The maximum size of information that str can hold.
# * @param[out] actualLength The actual length of the string
# * @param[out] val The double value for the named point.
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
# *
# * @beginPythonOnly
# * @return a string and a double value for the named point
# * @endPythonOnly
#
def helicsInputGetNamedPoint(
    ipt: HelicsInput, outputString: str, maxStringLen: int, actualLength: int, val: float,
):
    f = loadSym("helicsInputGetNamedPoint")
    err = lib.helicsErrorInitialize()
    f(ipt, cstring(outputString), maxStringLen.cint, actualLength, val, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *@}
# *
# * \defgroup default_values Default Value functions
# * @details These functions set the default value for a subscription. That is the value returned if nothing was published from elsewhere.
# * @{
#
# *
# * Set the default as a raw data array.
# *
# * @param ipt The input to set the default for.
# * @param data A pointer to the raw data to use for the default.
# * @forcpponly
# * @param inputDataLength The size of the raw data.
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultRaw(ipt: HelicsInput, data: pointer, inputDataLength: int):
    f = loadSym("helicsInputSetDefaultRaw")
    err = lib.helicsErrorInitialize()
    f(ipt, data, inputDataLength.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a string.
# *
# * @param ipt The input to set the default for.
# * @param str A pointer to the default string.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultString(ipt: HelicsInput, str: str):
    f = loadSym("helicsInputSetDefaultString")
    err = lib.helicsErrorInitialize()
    f(ipt, cstring(str), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as an integer.
# *
# * @param ipt The input to set the default for.
# * @param val The default integer.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultInteger(ipt: HelicsInput, val: int):
    f = loadSym("helicsInputSetDefaultInteger")
    err = lib.helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a boolean.
# *
# * @param ipt The input to set the default for.
# * @param val The default boolean value.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultBoolean(ipt: HelicsInput, val: HelicsBool):
    f = loadSym("helicsInputSetDefaultBoolean")
    err = lib.helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a time.
# *
# * @param ipt The input to set the default for.
# * @param val The default time value.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultTime(ipt: HelicsInput, val: HelicsTime):
    f = loadSym("helicsInputSetDefaultTime")
    err = lib.helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a char.
# *
# * @param ipt The input to set the default for.
# * @param val The default char value.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultChar(ipt: HelicsInput, val: str):
    f = loadSym("helicsInputSetDefaultChar")
    err = lib.helicsErrorInitialize()
    f(ipt, val.cchar, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a double.
# *
# * @param ipt The input to set the default for.
# * @param val The default double value.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultDouble(ipt: HelicsInput, val: float):
    f = loadSym("helicsInputSetDefaultDouble")
    err = lib.helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a complex number.
# *
# * @param ipt The input to set the default for.
# * @param real The default real value.
# * @param imag The default imaginary value.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultComplex(ipt: HelicsInput, real: float, imag: float):
    f = loadSym("helicsInputSetDefaultComplex")
    err = lib.helicsErrorInitialize()
    f(ipt, real.cdouble, imag.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a vector of doubles.
# *
# * @param ipt The input to set the default for.
# * @param vectorInput A pointer to an array of double data.
# * @param vectorLength The number of points to publish.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultVector(ipt: HelicsInput, vectorInput: float, vectorLength: int):
    f = loadSym("helicsInputSetDefaultVector")
    err = lib.helicsErrorInitialize()
    f(ipt, vectorInput, vectorLength.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the default as a NamedPoint.
# *
# * @param ipt The input to set the default for.
# * @param str A pointer to a string representing the name.
# * @param val A double value for the value of the named point.
# * @forcpponly
# * @param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
# * @endforcpponly
#
def helicsInputSetDefaultNamedPoint(ipt: HelicsInput, str: str, val: float):
    f = loadSym("helicsInputSetDefaultNamedPoint")
    err = lib.helicsErrorInitialize()
    f(ipt, cstring(str), val.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *@}
# *
# * \defgroup Information retrieval
# * @{
#
# *
# * Get the type of an input.
# *
# * @param ipt The input to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsInputGetType(ipt: HelicsInput) -> str:
    f = loadSym("helicsInputGetType")
    result = f(ipt)
    return ffi.string(result).decode()


# *
# * Get the type the publisher to an input is sending.
# *
# * @param ipt The input to query.
# *
# * @return A const char * with the type name.
#
def helicsInputGetPublicationType(ipt: HelicsInput) -> str:
    f = loadSym("helicsInputGetPublicationType")
    result = f(ipt)
    return ffi.string(result).decode()


# *
# * Get the type of a publication.
# *
# * @param pub The publication to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsPublicationGetType(pub: HelicsPublication) -> str:
    f = loadSym("helicsPublicationGetType")
    result = f(pub)
    return ffi.string(result).decode()


# *
# * Get the key of an input.
# *
# * @param ipt The input to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsInputGetKey(ipt: HelicsInput) -> str:
    f = loadSym("helicsInputGetKey")
    result = f(ipt)
    return ffi.string(result).decode()


# *
# * Get the key of a subscription.
# *
# * @return A const char with the subscription key.
#
def helicsSubscriptionGetKey(ipt: HelicsInput) -> str:
    f = loadSym("helicsSubscriptionGetKey")
    result = f(ipt)
    return ffi.string(result).decode()


# *
# * Get the key of a publication.
# *
# * @details This will be the global key used to identify the publication to the federation.
# *
# * @param pub The publication to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsPublicationGetKey(pub: HelicsPublication) -> str:
    f = loadSym("helicsPublicationGetKey")
    result = f(pub)
    return ffi.string(result).decode()


# *
# * Get the units of an input.
# *
# * @param ipt The input to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsInputGetUnits(ipt: HelicsInput) -> str:
    f = loadSym("helicsInputGetUnits")
    result = f(ipt)
    return ffi.string(result).decode()


# *
# * Get the units of the publication that an input is linked to.
# *
# * @param ipt The input to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsInputGetInjectionUnits(ipt: HelicsInput) -> str:
    f = loadSym("helicsInputGetInjectionUnits")
    result = f(ipt)
    return ffi.string(result).decode()


# *
# * Get the units of an input.
# *
# * @details The same as helicsInputGetUnits.
# *
# * @param ipt The input to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsInputGetExtractionUnits(ipt: HelicsInput) -> str:
    f = loadSym("helicsInputGetExtractionUnits")
    result = f(ipt)
    return ffi.string(result).decode()


# *
# * Get the units of a publication.
# *
# * @param pub The publication to query.
# *
# * @return A void enumeration, helics_ok if everything worked.
#
def helicsPublicationGetUnits(pub: HelicsPublication) -> str:
    f = loadSym("helicsPublicationGetUnits")
    result = f(pub)
    return ffi.string(result).decode()


# *
# * Get the data in the info field of an input.
# *
# * @param inp The input to query.
# *
# * @return A string with the info field string.
#
def helicsInputGetInfo(inp: HelicsInput) -> str:
    f = loadSym("helicsInputGetInfo")
    result = f(inp)
    return ffi.string(result).decode()


# *
# * Set the data in the info field for an input.
# *
# * @param inp The input to query.
# * @param info The string to set.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsInputSetInfo(inp: HelicsInput, info: str):
    f = loadSym("helicsInputSetInfo")
    err = lib.helicsErrorInitialize()
    f(inp, info, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the data in the info field of an publication.
# *
# * @param pub The publication to query.
# *
# * @return A string with the info field string.
#
def helicsPublicationGetInfo(pub: HelicsPublication) -> str:
    f = loadSym("helicsPublicationGetInfo")
    result = f(pub)
    return ffi.string(result).decode()


# *
# * Set the data in the info field for a publication.
# *
# * @param pub The publication to set the info field for.
# * @param info The string to set.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsPublicationSetInfo(pub: HelicsPublication, info: str):
    f = loadSym("helicsPublicationSetInfo")
    err = lib.helicsErrorInitialize()
    f(pub, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the current value of an input handle option
# *
# * @param inp The input to query.
# * @param option Integer representation of the option in question see /ref helics_handle_options.
# *
# * @return An integer value with the current value of the given option.
#
def helicsInputGetOption(inp: HelicsInput, option: int) -> int:
    f = loadSym("helicsInputGetOption")
    result = f(inp, option.cint).int


# *
# * Set an option on an input
# *
# * @param inp The input to query.
# * @param option The option to set for the input /ref helics_handle_options.
# * @param value The value to set the option to.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsInputSetOption(inp: HelicsInput, option: int, value: int):
    f = loadSym("helicsInputSetOption")
    err = lib.helicsErrorInitialize()
    f(inp, option.cint, value.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Get the value of an option for a publication
# *
# * @param pub The publication to query.
# * @param option The value to query see /ref helics_handle_options.
# *
# * @return A string with the info field string.
#
def helicsPublicationGetOption(pub: HelicsPublication, option: int) -> int:
    f = loadSym("helicsPublicationGetOption")
    result = f(pub, option.cint).int


# *
# * Set the value of an option for a publication
# *
# * @param pub The publication to query.
# * @param option Integer code for the option to set /ref helics_handle_options.
# * @param val The value to set the option to.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsPublicationSetOption(pub: HelicsPublication, option: int, val: int):
    f = loadSym("helicsPublicationSetOption")
    err = lib.helicsErrorInitialize()
    f(pub, option.cint, val.cint, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the minimum change detection tolerance.
# *
# * @param pub The publication to modify.
# * @param tolerance The tolerance level for publication, values changing less than this value will not be published.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsPublicationSetMinimumChange(pub: HelicsPublication, tolerance: float):
    f = loadSym("helicsPublicationSetMinimumChange")
    err = lib.helicsErrorInitialize()
    f(pub, tolerance.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *
# * Set the minimum change detection tolerance.
# *
# * @param inp The input to modify.
# * @param tolerance The tolerance level for registering an update, values changing less than this value will not show asbeing updated.
# * @forcpponly
# * @param[in,out] err An error object to fill out in case of an error.
# * @endforcpponly
#
def helicsInputSetMinimumChange(inp: HelicsInput, tolerance: float):
    f = loadSym("helicsInputSetMinimumChange")
    err = lib.helicsErrorInitialize()
    f(inp, tolerance.cdouble, err)
    if err.error_code != 0:
        raise HelicsException(err.message)


# *@}
# *
# * Check if a particular subscription was updated.
# *
# * @return helics_true if it has been updated since the last value retrieval.
#
def helicsInputIsUpdated(ipt: HelicsInput) -> HelicsBool:
    f = loadSym("helicsInputIsUpdated")
    result = f(ipt)
    return result == 1


# *
# * Get the last time a subscription was updated.
#
def helicsInputLastUpdateTime(ipt: HelicsInput) -> HelicsTime:
    f = loadSym("helicsInputLastUpdateTime")
    result = f(ipt)


# *
# * Clear the updated flag from an input.
#
def helicsInputClearUpdate(ipt: HelicsInput):
    f = loadSym("helicsInputClearUpdate")
    f(ipt)


# *
# * Get the number of publications in a federate.
# *
# * @return (-1) if fed was not a valid federate otherwise returns the number of publications.
#
def helicsFederateGetPublicationCount(fed: HelicsFederate) -> int:
    f = loadSym("helicsFederateGetPublicationCount")
    result = f(fed).int


# *
# * Get the number of subscriptions in a federate.
# *
# * @return (-1) if fed was not a valid federate otherwise returns the number of subscriptions.
#
def helicsFederateGetInputCount(fed: HelicsFederate) -> int:
    f = loadSym("helicsFederateGetInputCount")
    result = f(fed).int
