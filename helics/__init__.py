# -*- coding: utf-8 -*-
from enum import IntEnum, unique
from typing import List

from . import _build

lib = _build.lib
ffi = _build.ffi


@unique
class HelicsCoreType(IntEnum):
    """
    * **DEFAULT**      = 0
    * **TEST**         = 3
    * **INTERPROCESS** = 4
    * **IPC**          = 5
    * **TCP**          = 6
    * **UDP**          = 7
    * **NNG**          = 9
    * **ZMQ_TEST**     = 10
    * **TCP_SS**       = 11
    * **HTTP**         = 12
    * **WEBSOCKET**    = 14
    * **INPROC**       = 18
    * **NULL**         = 66
    """

    DEFAULT = 0  # HelicsCoreType
    ZMQ = 1  # HelicsCoreType
    MPI = 2  # HelicsCoreType
    TEST = 3  # HelicsCoreType
    INTERPROCESS = 4  # HelicsCoreType
    IPC = 5  # HelicsCoreType
    TCP = 6  # HelicsCoreType
    UDP = 7  # HelicsCoreType
    NNG = 9  # HelicsCoreType
    ZMQ_TEST = 10  # HelicsCoreType
    TCP_SS = 11  # HelicsCoreType
    HTTP = 12  # HelicsCoreType
    WEBSOCKET = 14  # HelicsCoreType
    INPROC = 18  # HelicsCoreType
    NULL = 66  # HelicsCoreType


HELICS_CORE_TYPE_DEFAULT = HelicsCoreType.DEFAULT
HELICS_CORE_TYPE_ZMQ = HelicsCoreType.ZMQ
HELICS_CORE_TYPE_MPI = HelicsCoreType.MPI
HELICS_CORE_TYPE_TEST = HelicsCoreType.TEST
HELICS_CORE_TYPE_INTERPROCESS = HelicsCoreType.INTERPROCESS
HELICS_CORE_TYPE_IPC = HelicsCoreType.IPC
HELICS_CORE_TYPE_TCP = HelicsCoreType.TCP
HELICS_CORE_TYPE_UDP = HelicsCoreType.UDP
HELICS_CORE_TYPE_ZMQ_TEST = HelicsCoreType.ZMQ_TEST
HELICS_CORE_TYPE_NNG = HelicsCoreType.NNG
HELICS_CORE_TYPE_TCP_SS = HelicsCoreType.TCP_SS
HELICS_CORE_TYPE_HTTP = HelicsCoreType.HTTP
HELICS_CORE_TYPE_WEBSOCKET = HelicsCoreType.WEBSOCKET
HELICS_CORE_TYPE_INPROC = HelicsCoreType.INPROC
HELICS_CORE_TYPE_NULL = HelicsCoreType.NULL


@unique
class HelicsDataType(IntEnum):
    """
    * **STRING**         = 0
    * **DOUBLE**         = 1
    * **INT**            = 2
    * **COMPLEX**        = 3
    * **VECTOR**         = 4
    * **COMPLEX_VECTOR** = 5
    * **NAMED_POINT**    = 6
    * **BOOLEAN**        = 7
    * **TIME**           = 8
    * **RAW**            = 25
    * **MULTI**          = 33
    * **ANY**            = 25262
    """

    STRING = 0  # HelicsDataType
    DOUBLE = 1  # HelicsDataType
    INT = 2  # HelicsDataType
    COMPLEX = 3  # HelicsDataType
    VECTOR = 4  # HelicsDataType
    COMPLEX_VECTOR = 5  # HelicsDataType
    NAMED_POINT = 6  # HelicsDataType
    BOOLEAN = 7  # HelicsDataType
    TIME = 8  # HelicsDataType
    RAW = 25  # HelicsDataType
    MULTI = 33  # HelicsDataType
    ANY = 25262  # HelicsDataType


HELICS_DATA_TYPE_STRING = HelicsDataType.STRING
HELICS_DATA_TYPE_DOUBLE = HelicsDataType.DOUBLE
HELICS_DATA_TYPE_INT = HelicsDataType.INT
HELICS_DATA_TYPE_COMPLEX = HelicsDataType.COMPLEX
HELICS_DATA_TYPE_VECTOR = HelicsDataType.VECTOR
HELICS_DATA_TYPE_COMPLEX_VECTOR = HelicsDataType.COMPLEX_VECTOR
HELICS_DATA_TYPE_NAMED_POINT = HelicsDataType.NAMED_POINT
HELICS_DATA_TYPE_BOOLEAN = HelicsDataType.BOOLEAN
HELICS_DATA_TYPE_TIME = HelicsDataType.TIME
HELICS_DATA_TYPE_RAW = HelicsDataType.RAW
HELICS_DATA_TYPE_MULTI = HelicsDataType.MULTI
HELICS_DATA_TYPE_ANY = HelicsDataType.ANY


@unique
class HelicsFederateFlag(IntEnum):
    """
    * **OBSERVER**                      = 0
    * **UNINTERRUPTIBLE**               = 1
    * **INTERRUPTIBLE**                 = 2
    * **SOURCE_ONLY**                   = 4
    * **ONLY_TRANSMIT_ON_CHANGE**       = 6
    * **ONLY_UPDATE_ON_CHANGE**         = 8
    * **WAIT_FOR_CURRENT_TIME_UPDATE**  = 10
    * **RESTRICTIVE_TIME_POLICY**       = 11
    * **ROLLBACK**                      = 12
    * **FORWARD_COMPUTE**               = 14
    * **REALTIME**                      = 16
    * **SINGLE_THREAD_FEDERATE**        = 27
    * **SLOW_RESPONDING**               = 29
    * **DELAY_INIT_ENTRY**              = 45
    * **ENABLE_INIT_ENTRY**             = 47
    * **IGNORE_TIME_MISMATCH_WARNINGS** = 67
    * **TERMINATE_ON_ERROR**            = 72
    """

    OBSERVER = 0  # HelicsFederateFlags
    UNINTERRUPTIBLE = 1  # HelicsFederateFlags
    INTERRUPTIBLE = 2  # HelicsFederateFlags
    SOURCE_ONLY = 4  # HelicsFederateFlags
    ONLY_TRANSMIT_ON_CHANGE = 6  # HelicsFederateFlags
    ONLY_UPDATE_ON_CHANGE = 8  # HelicsFederateFlags
    WAIT_FOR_CURRENT_TIME_UPDATE = 10  # HelicsFederateFlags
    RESTRICTIVE_TIME_POLICY = 11  # HelicsFederateFlags
    ROLLBACK = 12  # HelicsFederateFlags
    FORWARD_COMPUTE = 14  # HelicsFederateFlags
    REALTIME = 16  # HelicsFederateFlags
    SINGLE_THREAD_FEDERATE = 27  # HelicsFederateFlags
    SLOW_RESPONDING = 29  # HelicsFederateFlags
    DELAY_INIT_ENTRY = 45  # HelicsFederateFlags
    ENABLE_INIT_ENTRY = 47  # HelicsFederateFlags
    IGNORE_TIME_MISMATCH_WARNINGS = 67  # HelicsFederateFlags
    TERMINATE_ON_ERROR = 72  # HelicsFederateFlags


HELICS_FLAG_OBSERVER = HelicsFederateFlag.OBSERVER
HELICS_FLAG_UNINTERRUPTIBLE = HelicsFederateFlag.UNINTERRUPTIBLE
HELICS_FLAG_INTERRUPTIBLE = HelicsFederateFlag.INTERRUPTIBLE
HELICS_FLAG_SOURCE_ONLY = HelicsFederateFlag.SOURCE_ONLY
HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE = HelicsFederateFlag.ONLY_TRANSMIT_ON_CHANGE
HELICS_FLAG_ONLY_UPDATE_ON_CHANGE = HelicsFederateFlag.ONLY_UPDATE_ON_CHANGE
HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE = HelicsFederateFlag.WAIT_FOR_CURRENT_TIME_UPDATE
HELICS_FLAG_RESTRICTIVE_TIME_POLICY = HelicsFederateFlag.RESTRICTIVE_TIME_POLICY
HELICS_FLAG_ROLLBACK = HelicsFederateFlag.ROLLBACK
HELICS_FLAG_FORWARD_COMPUTE = HelicsFederateFlag.FORWARD_COMPUTE
HELICS_FLAG_REALTIME = HelicsFederateFlag.REALTIME
HELICS_FLAG_SINGLE_THREAD_FEDERATE = HelicsFederateFlag.SINGLE_THREAD_FEDERATE
HELICS_FLAG_SLOW_RESPONDING = HelicsFederateFlag.SLOW_RESPONDING
HELICS_FLAG_DELAY_INIT_ENTRY = HelicsFederateFlag.DELAY_INIT_ENTRY
HELICS_FLAG_ENABLE_INIT_ENTRY = HelicsFederateFlag.ENABLE_INIT_ENTRY
HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS = HelicsFederateFlag.IGNORE_TIME_MISMATCH_WARNINGS
HELICS_FLAG_TERMINATE_ON_ERROR = HelicsFederateFlag.TERMINATE_ON_ERROR


@unique
class HelicsLogLevel(IntEnum):
    """
    * **NO_PRINT**    = -1
    * **ERROR**       = 0
    * **WARNING**     = 1
    * **SUMMARY**     = 2
    * **CONNECTIONS** = 3
    * **INTERFACES**  = 4
    * **TIMING**      = 5
    * **DATA**        = 6
    * **TRACE**       = 7
    """

    NO_PRINT = -1  # HelicsLogLevels
    ERROR = 0  # HelicsLogLevels
    WARNING = 1  # HelicsLogLevels
    SUMMARY = 2  # HelicsLogLevels
    CONNECTIONS = 3  # HelicsLogLevels
    INTERFACES = 4  # HelicsLogLevels
    TIMING = 5  # HelicsLogLevels
    DATA = 6  # HelicsLogLevels
    TRACE = 7  # HelicsLogLevels


HELICS_LOG_LEVEL_NO_PRINT = HelicsLogLevel.NO_PRINT
HELICS_LOG_LEVEL_ERROR = HelicsLogLevel.ERROR
HELICS_LOG_LEVEL_WARNING = HelicsLogLevel.WARNING
HELICS_LOG_LEVEL_SUMMARY = HelicsLogLevel.SUMMARY
HELICS_LOG_LEVEL_CONNECTIONS = HelicsLogLevel.CONNECTIONS
HELICS_LOG_LEVEL_INTERFACES = HelicsLogLevel.INTERFACES
HELICS_LOG_LEVEL_TIMING = HelicsLogLevel.TIMING
HELICS_LOG_LEVEL_DATA = HelicsLogLevel.DATA
HELICS_LOG_LEVEL_TRACE = HelicsLogLevel.TRACE


@unique
class HelicsError(IntEnum):
    """
    * **FATAL**                    = -404
    * **EXTERNAL_TYPE**            = -203
    * **OTHER**                    = -101
    * **INSUFFICIENT_SPACE**       = -18
    * **EXECUTION_FAILURE**        = -14
    * **INVALID_FUNCTION_CALL**    = -10
    * **INVALID_STATE_TRANSITION** = -9
    * **WARNING**                  = -8
    * **SYSTEM_FAILURE**           = -6
    * **DISCARD**                  = -5
    * **INVALID_ARGUMENT**         = -4
    * **INVALID_OBJECT**           = -3
    * **CONNECTION_FAILURE**       = -2
    * **REGISTRATION_FAILURE**     = -1
    * **OK**                       = 0
    """

    FATAL = -404  # HelicsErrorTypes
    EXTERNAL_TYPE = -203  # HelicsErrorTypes
    OTHER = -101  # HelicsErrorTypes
    INSUFFICIENT_SPACE = -18  # HelicsErrorTypes
    EXECUTION_FAILURE = -14  # HelicsErrorTypes
    INVALID_FUNCTION_CALL = -10  # HelicsErrorTypes
    INVALID_STATE_TRANSITION = -9  # HelicsErrorTypes
    WARNING = -8  # HelicsErrorTypes
    SYSTEM_FAILURE = -6  # HelicsErrorTypes
    DISCARD = -5  # HelicsErrorTypes
    INVALID_ARGUMENT = -4  # HelicsErrorTypes
    INVALID_OBJECT = -3  # HelicsErrorTypes
    CONNECTION_FAILURE = -2  # HelicsErrorTypes
    REGISTRATION_FAILURE = -1  # HelicsErrorTypes
    OK = 0  # HelicsErrorTypes


HELICS_ERROR_FATAL = HelicsError.FATAL
HELICS_ERROR_EXTERNAL_TYPE = HelicsError.EXTERNAL_TYPE
HELICS_ERROR_OTHER = HelicsError.OTHER
HELICS_ERROR_INSUFFICIENT_SPACE = HelicsError.INSUFFICIENT_SPACE
HELICS_ERROR_EXECUTION_FAILURE = HelicsError.EXECUTION_FAILURE
HELICS_ERROR_INVALID_FUNCTION_CALL = HelicsError.INVALID_FUNCTION_CALL
HELICS_ERROR_INVALID_STATE_TRANSITION = HelicsError.INVALID_STATE_TRANSITION
HELICS_WARNING = HelicsError.WARNING
HELICS_ERROR_SYSTEM_FAILURE = HelicsError.SYSTEM_FAILURE
HELICS_ERROR_DISCARD = HelicsError.DISCARD
HELICS_ERROR_INVALID_ARGUMENT = HelicsError.INVALID_ARGUMENT
HELICS_ERROR_INVALID_OBJECT = HelicsError.INVALID_OBJECT
HELICS_ERROR_CONNECTION_FAILURE = HelicsError.CONNECTION_FAILURE
HELICS_ERROR_REGISTRATION_FAILURE = HelicsError.REGISTRATION_FAILURE
HELICS_OK = HelicsError.OK


@unique
class HelicsProperty(IntEnum):
    """
    * **TIME_DELTA**            = 137
    * **TIME_PERIOD**           = 140
    * **TIME_OFFSET**           = 141
    * **TIME_RT_LAG**           = 143
    * **TIME_RT_LEAD**          = 144
    * **TIME_RT_TOLERANCE**     = 145
    * **TIME_INPUT_DELAY**      = 148
    * **TIME_OUTPUT_DELAY**     = 150
    * **INT_MAX_ITERATIONS**    = 259
    * **INT_LOG_LEVEL**         = 271
    * **INT_FILE_LOG_LEVEL**    = 272
    * **INT_CONSOLE_LOG_LEVEL** = 274
    """

    TIME_DELTA = 137  # HelicsProperties
    TIME_PERIOD = 140  # HelicsProperties
    TIME_OFFSET = 141  # HelicsProperties
    TIME_RT_LAG = 143  # HelicsProperties
    TIME_RT_LEAD = 144  # HelicsProperties
    TIME_RT_TOLERANCE = 145  # HelicsProperties
    TIME_INPUT_DELAY = 148  # HelicsProperties
    TIME_OUTPUT_DELAY = 150  # HelicsProperties
    INT_MAX_ITERATIONS = 259  # HelicsProperties
    INT_LOG_LEVEL = 271  # HelicsProperties
    INT_FILE_LOG_LEVEL = 272  # HelicsProperties
    INT_CONSOLE_LOG_LEVEL = 274  # HelicsProperties


HELICS_PROPERTY_TIME_DELTA = HelicsProperty.TIME_DELTA
HELICS_PROPERTY_TIME_PERIOD = HelicsProperty.TIME_PERIOD
HELICS_PROPERTY_TIME_OFFSET = HelicsProperty.TIME_OFFSET
HELICS_PROPERTY_TIME_RT_LAG = HelicsProperty.TIME_RT_LAG
HELICS_PROPERTY_TIME_RT_LEAD = HelicsProperty.TIME_RT_LEAD
HELICS_PROPERTY_TIME_RT_TOLERANCE = HelicsProperty.TIME_RT_TOLERANCE
HELICS_PROPERTY_TIME_INPUT_DELAY = HelicsProperty.TIME_INPUT_DELAY
HELICS_PROPERTY_TIME_OUTPUT_DELAY = HelicsProperty.TIME_OUTPUT_DELAY
HELICS_PROPERTY_INT_MAX_ITERATIONS = HelicsProperty.INT_MAX_ITERATIONS
HELICS_PROPERTY_INT_LOG_LEVEL = HelicsProperty.INT_LOG_LEVEL
HELICS_PROPERTY_INT_FILE_LOG_LEVEL = HelicsProperty.INT_FILE_LOG_LEVEL
HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL = HelicsProperty.INT_CONSOLE_LOG_LEVEL


@unique
class HelicsMultiInputMode(IntEnum):
    """
    * **NO_OP**               = 0
    * **VECTORIZE_OPERATION** = 1
    * **AND_OPERATION**       = 2
    * **OR_OPERATION**        = 3
    * **SUM_OPERATION**       = 4
    * **DIFF_OPERATION**      = 5
    * **MAX_OPERATION**       = 6
    * **MIN_OPERATION**       = 7
    * **AVERAGE_OPERATION**   = 8
    """

    NO_OP = 0  # HelicsMultiInputMode
    VECTORIZE_OPERATION = 1  # HelicsMultiInputMode
    AND_OPERATION = 2  # HelicsMultiInputMode
    OR_OPERATION = 3  # HelicsMultiInputMode
    SUM_OPERATION = 4  # HelicsMultiInputMode
    DIFF_OPERATION = 5  # HelicsMultiInputMode
    MAX_OPERATION = 6  # HelicsMultiInputMode
    MIN_OPERATION = 7  # HelicsMultiInputMode
    AVERAGE_OPERATION = 8  # HelicsMultiInputMode


HELICS_MULTI_INPUT_NO_OP = HelicsMultiInputMode.NO_OP
HELICS_MULTI_INPUT_VECTORIZE_OPERATION = HelicsMultiInputMode.VECTORIZE_OPERATION
HELICS_MULTI_INPUT_AND_OPERATION = HelicsMultiInputMode.AND_OPERATION
HELICS_MULTI_INPUT_OR_OPERATION = HelicsMultiInputMode.OR_OPERATION
HELICS_MULTI_INPUT_SUM_OPERATION = HelicsMultiInputMode.SUM_OPERATION
HELICS_MULTI_INPUT_DIFF_OPERATION = HelicsMultiInputMode.DIFF_OPERATION
HELICS_MULTI_INPUT_MAX_OPERATION = HelicsMultiInputMode.MAX_OPERATION
HELICS_MULTI_INPUT_MIN_OPERATION = HelicsMultiInputMode.MIN_OPERATION
HELICS_MULTI_INPUT_AVERAGE_OPERATION = HelicsMultiInputMode.AVERAGE_OPERATION


@unique
class HelicsHandleOption(IntEnum):
    """
    * **CONNECTION_REQUIRED**          = 397
    * **CONNECTION_OPTIONAL**          = 402
    * **SINGLE_CONNECTION_ONLY**       = 407
    * **MULTIPLE_CONNECTIONS_ALLOWED** = 409
    * **BUFFER_DATA**                  = 411
    * **STRICT_TYPE_CHECKING**         = 414
    * **IGNORE_UNIT_MISMATCH**         = 447
    * **ONLY_TRANSMIT_ON_CHANGE**      = 452
    * **ONLY_UPDATE_ON_CHANGE**        = 454
    * **IGNORE_INTERRUPTS**            = 475
    * **MULTI_INPUT_HANDLING_METHOD**  = 507
    * **INPUT_PRIORITY_LOCATION**      = 510
    * **CLEAR_PRIORITY_LIST**          = 512
    * **CONNECTIONS**                  = 522
    """

    CONNECTION_REQUIRED = 397  # HelicsHandleOptions
    CONNECTION_OPTIONAL = 402  # HelicsHandleOptions
    SINGLE_CONNECTION_ONLY = 407  # HelicsHandleOptions
    MULTIPLE_CONNECTIONS_ALLOWED = 409  # HelicsHandleOptions
    BUFFER_DATA = 411  # HelicsHandleOptions
    STRICT_TYPE_CHECKING = 414  # HelicsHandleOptions
    IGNORE_UNIT_MISMATCH = 447  # HelicsHandleOptions
    ONLY_TRANSMIT_ON_CHANGE = 452  # HelicsHandleOptions
    ONLY_UPDATE_ON_CHANGE = 454  # HelicsHandleOptions
    IGNORE_INTERRUPTS = 475  # HelicsHandleOptions
    MULTI_INPUT_HANDLING_METHOD = 507  # HelicsHandleOptions
    INPUT_PRIORITY_LOCATION = 510  # HelicsHandleOptions
    CLEAR_PRIORITY_LIST = 512  # HelicsHandleOptions
    CONNECTIONS = 522  # HelicsHandleOptions


HELICS_HANDLE_OPTION_CONNECTION_REQUIRED = HelicsHandleOption.CONNECTION_REQUIRED
HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL = HelicsHandleOption.CONNECTION_OPTIONAL
HELICS_HANDLE_OPTION_SINGLE_CONNECTION_ONLY = HelicsHandleOption.SINGLE_CONNECTION_ONLY
HELICS_HANDLE_OPTION_MULTIPLE_CONNECTIONS_ALLOWED = HelicsHandleOption.MULTIPLE_CONNECTIONS_ALLOWED
HELICS_HANDLE_OPTION_BUFFER_DATA = HelicsHandleOption.BUFFER_DATA
HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING = HelicsHandleOption.STRICT_TYPE_CHECKING
HELICS_HANDLE_OPTION_IGNORE_UNIT_MISMATCH = HelicsHandleOption.IGNORE_UNIT_MISMATCH
HELICS_HANDLE_OPTION_ONLY_TRANSMIT_ON_CHANGE = HelicsHandleOption.ONLY_TRANSMIT_ON_CHANGE
HELICS_HANDLE_OPTION_ONLY_UPDATE_ON_CHANGE = HelicsHandleOption.ONLY_UPDATE_ON_CHANGE
HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS = HelicsHandleOption.IGNORE_INTERRUPTS
HELICS_HANDLE_OPTION_MULTI_INPUT_HANDLING_METHOD = HelicsHandleOption.MULTI_INPUT_HANDLING_METHOD
HELICS_HANDLE_OPTION_INPUT_PRIORITY_LOCATION = HelicsHandleOption.INPUT_PRIORITY_LOCATION
HELICS_HANDLE_OPTION_CLEAR_PRIORITY_LIST = HelicsHandleOption.CLEAR_PRIORITY_LIST
HELICS_HANDLE_OPTION_CONNECTIONS = HelicsHandleOption.CONNECTIONS


@unique
class HelicsFilterType(IntEnum):
    """
    * **CUSTOM**       = 0
    * **DELAY**        = 1
    * **RANDOM_DELAY** = 2
    * **RANDOM_DROP**  = 3
    * **REROUTE**      = 4
    * **CLONE**        = 5
    * **FIREWALL**     = 6
    """

    CUSTOM = 0  # HelicsFilterType
    DELAY = 1  # HelicsFilterType
    RANDOM_DELAY = 2  # HelicsFilterType
    RANDOM_DROP = 3  # HelicsFilterType
    REROUTE = 4  # HelicsFilterType
    CLONE = 5  # HelicsFilterType
    FIREWALL = 6  # HelicsFilterType


HELICS_FILTER_TYPE_CUSTOM = HelicsFilterType.CUSTOM
HELICS_FILTER_TYPE_DELAY = HelicsFilterType.DELAY
HELICS_FILTER_TYPE_RANDOM_DELAY = HelicsFilterType.RANDOM_DELAY
HELICS_FILTER_TYPE_RANDOM_DROP = HelicsFilterType.RANDOM_DROP
HELICS_FILTER_TYPE_REROUTE = HelicsFilterType.REROUTE
HELICS_FILTER_TYPE_CLONE = HelicsFilterType.CLONE
HELICS_FILTER_TYPE_FIREWALL = HelicsFilterType.FIREWALL


@unique
class HelicsIterationRequest(IntEnum):
    """
    * **NO_ITERATION**      = 0
    * **FORCE_ITERATION**   = 1
    * **ITERATE_IF_NEEDED** = 2
    """

    NO_ITERATION = 0  # HelicsIterationRequest
    FORCE_ITERATION = 1  # HelicsIterationRequest
    ITERATE_IF_NEEDED = 2  # HelicsIterationRequest


HELICS_ITERATION_REQUEST_NO_ITERATION = HelicsIterationRequest.NO_ITERATION
HELICS_ITERATION_REQUEST_FORCE_ITERATION = HelicsIterationRequest.FORCE_ITERATION
HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED = HelicsIterationRequest.ITERATE_IF_NEEDED


@unique
class HelicsIterationResult(IntEnum):
    """
    * **NEXT_STEP** = 0
    * **ERROR**     = 1
    * **HALTED**    = 2
    * **ITERATING** = 3
    """

    NEXT_STEP = 0  # HelicsIterationResult
    ERROR = 1  # HelicsIterationResult
    HALTED = 2  # HelicsIterationResult
    ITERATING = 3  # HelicsIterationResult


HELICS_ITERATION_RESULT_NEXT_STEP = HelicsIterationResult.NEXT_STEP
HELICS_ITERATION_RESULT_ERROR = HelicsIterationResult.ERROR
HELICS_ITERATION_RESULT_HALTED = HelicsIterationResult.HALTED
HELICS_ITERATION_RESULT_ITERATING = HelicsIterationResult.ITERATING


@unique
class HelicsFederateState(IntEnum):
    """
    * **STARTUP**                = 0
    * **INITIALIZATION**         = 1
    * **EXECUTION**              = 2
    * **FINALIZE**               = 3
    * **ERROR**                  = 4
    * **PENDING_INIT**           = 5
    * **PENDING_EXEC**           = 6
    * **PENDING_TIME**           = 7
    * **PENDING_ITERATIVE_TIME** = 8
    * **PENDING_FINALIZE**       = 9
    """

    STARTUP = 0  # HelicsFederateState
    INITIALIZATION = 1  # HelicsFederateState
    EXECUTION = 2  # HelicsFederateState
    FINALIZE = 3  # HelicsFederateState
    ERROR = 4  # HelicsFederateState
    PENDING_INIT = 5  # HelicsFederateState
    PENDING_EXEC = 6  # HelicsFederateState
    PENDING_TIME = 7  # HelicsFederateState
    PENDING_ITERATIVE_TIME = 8  # HelicsFederateState
    PENDING_FINALIZE = 9  # HelicsFederateState


HELICS_STATE_STARTUP = HelicsFederateState.STARTUP
HELICS_STATE_INITIALIZATION = HelicsFederateState.INITIALIZATION
HELICS_STATE_EXECUTION = HelicsFederateState.EXECUTION
HELICS_STATE_FINALIZE = HelicsFederateState.FINALIZE
HELICS_STATE_ERROR = HelicsFederateState.ERROR
HELICS_STATE_PENDING_INIT = HelicsFederateState.PENDING_INIT
HELICS_STATE_PENDING_EXEC = HelicsFederateState.PENDING_EXEC
HELICS_STATE_PENDING_TIME = HelicsFederateState.PENDING_TIME
HELICS_STATE_PENDING_ITERATIVE_TIME = HelicsFederateState.PENDING_ITERATIVE_TIME
HELICS_STATE_PENDING_FINALIZE = HelicsFederateState.PENDING_FINALIZE


HelicsCore = object
HelicsBroker = object
HelicsFederate = object


class HelicsValueFederate(HelicsFederate):
    pass


class HelicsMessageFederate(HelicsFederate):
    pass


class HelicsCombinationFederate(HelicsFederate):
    pass


HelicsFederateInfo = object
HelicsTime = float
HelicsQuery = object
HelicsEndpoint = object
pointer = int
HelicsMessage = object
HelicsMessageObject = object
HelicsFilter = object
HelicsInput = object
HelicsPublication = object
HelicsComplex = object


class HelicsException(Exception):
    pass


def cstring(s: str) -> str:
    # Convert python string to cstring
    return ffi.new("char[]", s.encode())


def cdouble(d: float) -> float:
    # Convert python float to cfloat
    return d


def cchar(c: str) -> str:
    # Convert python str to cchar
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


def helicsIsCoreTypeAvailable(type: str) -> bool:
    """
    Returns `True` if core/broker type specified is available in current compilation.

    **Parameters**

    * **`type`** - A string representing a core type. Options include "zmq", "udp", "ipc", "interprocess", "tcp", "default", "mpi".

    **Returns**: `True` if `type` is available, `False` if `type` is not available.
    """
    f = loadSym("helicsIsCoreTypeAvailable")
    result = f(cstring(type))
    return result == 1


def helicsCreateCore(type: str, name: str, initString: str) -> HelicsCore:
    """
    Create a `helics.HelicsCore`.

    **Parameters**

    * **`type`** - The type of the core to create.
    * **`name`** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    * **`initString`** - An initialization string to send to the core. The format is similar to command line arguments. Typical options include a broker name, the broker address, the number of federates, etc.

    **Returns**: `helics.HelicsCore`.
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
    Create a `helics.HelicsCore` by passing command line arguments.

    **Parameters**

    * **`type`** - The type of the core to create.
    * **`name`** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    * **`arguments`** - The list of string values from a command line.

    **Returns**: `helics.HelicsCore`.
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
    Create a new reference to an existing core.
    This will create a new `helics.HelicsCore` that references the existing core.
    The new `helics.HelicsCore` must be freed as well.

    **Parameters**

    * **`core`** - An existing `helics.HelicsCore`.

    **Returns**: `helics.HelicsCore`.
    """
    f = loadSym("helicsCoreClone")
    err = helicsErrorInitialize()
    result = f(core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCoreIsValid(core: HelicsCore) -> bool:
    """
    Check if a `helics.HelicsCore` is a valid object.

    **Parameters**

    * **`core`** - The `helics.HelicsCore` object to test.

    **Returns**: `True` if valid, `False` if not valid.
    """
    f = loadSym("helicsCoreIsValid")
    result = f(core)
    return result == 1


def helicsCreateBroker(type: str, name: str, initString: str) -> HelicsBroker:
    """
    Create a broker object

    **Parameters**

    * **`type`** - The type of the broker to create.
    * **`name`** - The name of the broker. It can be a nullptr or empty string to have a name automatically assigned.
    * **`initString`** - An initialization string to send to the core-the format is similar to command line arguments. Typical options include a broker address such as --broker="XSSAF" if this is a subbroker, or the number of federates, or the address.

    **Returns**: `helics.HelicsBroker`.
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
    Create a `helics.HelicsCore` by passing command line arguments.

    **Parameters**

    * **`type`** - The type of the core to create.
    * **`name`** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    * **`arguments`** - The list of string values from a command line.

    **Returns**: `helics.HelicsBroker`.
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
    Create a new reference to an existing broker.
    This will create a new broker object that references the existing broker it must be freed as well.

    **Parameters**

    * **`broker`** - An existing `helics.HelicsBroker`.

    **Returns**: `helics.HelicsBroker`.
    """
    f = loadSym("helicsBrokerClone")
    err = helicsErrorInitialize()
    result = f(broker, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsBrokerIsValid(broker: HelicsBroker) -> bool:
    """
    Check if a broker object is a valid object.

    **Parameters**

    * **`broker`** - The `helics.HelicsBroker` object to test.

    **Returns**: `True` if valid, `False` if not valid.
    """
    f = loadSym("helicsBrokerIsValid")
    result = f(broker)
    return result == 1


def helicsBrokerIsConnected(broker: HelicsBroker) -> bool:
    """
    Check if a broker is connected.
    A connected broker implies it is attached to cores or cores could reach out to communicate.

    **Returns**: `True` if connected, `False` if not connected.
    """
    f = loadSym("helicsBrokerIsConnected")
    result = f(broker)
    return result == 1


def helicsBrokerDataLink(broker: HelicsBroker, source: str, target: str):
    """
    Link a named publication and named input using a broker.

    **Parameters**

    * **`broker`** - The broker to generate the connection from.
    * **`source`** - The name of the publication.
    * **`target`** - The name of the target to send the publication data.
    """
    f = loadSym("helicsBrokerDataLink")
    err = helicsErrorInitialize()
    f(broker, cstring(source), cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddSourceFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
    """
    Link a named filter to a source endpoint.

    **Parameters**

    * **`broker`** - The broker to generate the connection from.
    * **`filter`** - The name of the filter.
    * **`endpoint`** - The name of the endpoint to filter the data from.
    """
    f = loadSym("helicsBrokerAddSourceFilterToEndpoint")
    err = helicsErrorInitialize()
    f(broker, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddDestinationFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
    """
    Link a named filter to a destination endpoint.

    **Parameters**

    * **`broker`** - The broker to generate the connection from.
    * **`filter`** - The name of the filter.
    * **`endpoint`** - The name of the endpoint to filter the data going to.
    """
    f = loadSym("helicsBrokerAddDestinationFilterToEndpoint")
    err = helicsErrorInitialize()
    f(broker, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerMakeConnections(broker: HelicsBroker, file: str):
    """
    Load a file containing connection information.

    **Parameters**

    * **`broker`** - The broker to generate the connections from.
    * **`file`** - A JSON or TOML file containing connection information.
    """
    f = loadSym("helicsBrokerMakeConnections")
    err = helicsErrorInitialize()
    f(broker, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreWaitForDisconnect(core: HelicsCore, msToWait: int) -> bool:
    """
    Wait for the core to disconnect.

    **Parameters**

    * **`core`** - The core to wait for.
    * **`msToWait`** - The time out in millisecond (<0 for infinite timeout).
    """
    f = loadSym("helicsCoreWaitForDisconnect")
    err = helicsErrorInitialize()
    result = f(core, msToWait, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsBrokerWaitForDisconnect(broker: HelicsBroker, msToWait: int) -> bool:
    """
    Wait for the broker to disconnect.

    **Parameters**

    * **`broker`** - The broker to wait for.
    * **`msToWait`** - The time out in millisecond (<0 for infinite timeout).
    """
    f = loadSym("helicsBrokerWaitForDisconnect")
    err = helicsErrorInitialize()
    result = f(broker, msToWait, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsCoreIsConnected(core: HelicsCore) -> bool:
    """
    Check if a core is connected.
    A connected core implies it is attached to federates or federates could be attached to it.

    **Returns**: `True` if connected, `False` if not connected.
    """
    f = loadSym("helicsCoreIsConnected")
    result = f(core)
    return result == 1


def helicsCoreDataLink(core: HelicsCore, source: str, target: str):
    """
    Link a named publication and named input using a core.

    **Parameters**

    * **`core`** - The core to generate the connection from.
    * **`source`** - The name of the publication.
    * **`target`** - The name of the target to send the publication data.
    """
    f = loadSym("helicsCoreDataLink")
    err = helicsErrorInitialize()
    f(core, cstring(source), cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddSourceFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
    """
    Link a named filter to a source endpoint.

    **Parameters**

    * **`core`** - The core to generate the connection from.
    * **`filter`** - The name of the filter.
    * **`endpoint`** - The name of the endpoint to filter the data from.
    """
    f = loadSym("helicsCoreAddSourceFilterToEndpoint")
    err = helicsErrorInitialize()
    f(core, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddDestinationFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
    """
    Link a named filter to a destination endpoint.

    **Parameters**

    * **`core`** - The core to generate the connection from.
    * **`filter`** - The name of the filter.
    * **`endpoint`** - The name of the endpoint to filter the data going to.
    """
    f = loadSym("helicsCoreAddDestinationFilterToEndpoint")
    err = helicsErrorInitialize()
    f(core, cstring(filter), cstring(endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreMakeConnections(core: HelicsCore, file: str):
    """
    Load a file containing connection information.

    **Parameters**

    * **`core`** - The core to generate the connections from.
    * **`file`** - A JSON or TOML file containing connection information.
    """
    f = loadSym("helicsCoreMakeConnections")
    err = helicsErrorInitialize()
    f(core, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerGetIdentifier(broker: HelicsBroker) -> str:
    """
    Get an identifier for the broker.

    **Parameters**

    * **`broker`** - The broker to query.

    **Returns**: A string containing the identifier for the broker.
    """
    f = loadSym("helicsBrokerGetIdentifier")
    result = f(broker)
    return ffi.string(result).decode()


def helicsCoreGetIdentifier(core: HelicsCore) -> str:
    """
    Get an identifier for the core.

    **Parameters**

    * **`core`** - The core to query.

    **Returns**: A string with the identifier of the core.
    """
    f = loadSym("helicsCoreGetIdentifier")
    result = f(core)
    return ffi.string(result).decode()


def helicsBrokerGetAddress(broker: HelicsBroker) -> str:
    """
    Get the network address associated with a broker.

    **Parameters**

    * **`broker`** - The broker to query.

    **Returns**: A string with the network address of the broker.
    """
    f = loadSym("helicsBrokerGetAddress")
    result = f(broker)
    return ffi.string(result).decode()


def helicsCoreGetAddress(core: HelicsCore) -> str:
    """
    Get the network address associated with a core.

    **Parameters**

    * **`core`** - The core to query.

    **Returns**: A string with the network address of the broker.
    """
    f = loadSym("helicsCoreGetAddress")
    result = f(core)
    return ffi.string(result).decode()


def helicsCoreSetReadyToInit(core: HelicsCore):
    """
    Set the core to ready for init.
    This function is used for cores that have filters but no federates so there needs to be a direct signal to the core to trigger the federation initialization.

    **Parameters**

    * **`core`** - The `helics.HelicsCore` to enable init values for.
    """
    f = loadSym("helicsCoreSetReadyToInit")
    err = helicsErrorInitialize()
    f(core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreConnect(core: HelicsCore) -> bool:
    """
    Connect a core to the federate based on current configuration.

    **Parameters**

    * **`core`** - The core to connect.

    **Returns**: `True` if `core` is connected successfully, else `False`.
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
    Disconnect a core from the federation.

    **Parameters**

    * **`core`** - The core to query.
    """
    f = loadSym("helicsCoreDisconnect")
    err = helicsErrorInitialize()
    f(core, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetFederateByName(fedName: str) -> HelicsFederate:
    """
    Get an existing `helics.HelicsFederate` from a core by name.
    The federate must have been created by one of the other functions and at least one of the objects referencing the created federate must still be active in the process.

    **Parameters**

    * **`fedName`** - The name of the federate to retrieve.

    **Returns**: `helics.HelicsFederate`.
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
    Disconnect a broker.

    **Parameters**

    * **`broker`** - The broker to disconnect.
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


def helicsCreateValueFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsValueFederate:
    """
    Creation and destruction of Federates.
    Create `helics.HelicsValueFederate` from `helics.HelicsFederateInfo`.
    `helics.HelicsValueFederate` objects can be used in all functions that take a `helics.HelicsFederate` as an argument.

    **Parameters**

    * **`fedName`** - The name of the federate to create, can NULL or an empty string to use the default name from fi or an assigned name.
    * **`fi`** - The federate info object that contains details on the federate.

    **Returns**: `helics.HelicsValueFederate`.
    """
    f = loadSym("helicsCreateValueFederate")
    err = helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateValueFederateFromConfig(configFile: str) -> HelicsValueFederate:
    """
    Create `helics.HelicsValueFederate` from a JSON file, JSON string, or TOML file.
    `helics.HelicsValueFederate` objects can be used in all functions that take a `helics.HelicsFederate` as an argument.

    **Parameters**

    * **`configFile`** - A JSON file or a JSON string or TOML file that contains setup and configuration information.

    **Returns**: `helics.HelicsValueFederate`.
    """
    f = loadSym("helicsCreateValueFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateMessageFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsMessageFederate:
    """
    Create `helics.HelicsMessageFederate` from `helics.HelicsFederateInfo`.
    `helics.HelicsMessageFederate` objects can be used in all functions that take a `helics.HelicsFederate` as an argument.

    **Parameters**

    * **`fedName`** - The name of the federate to create.
    * **`fi`** - The federate info object that contains details on the federate.

    **Returns**: `helics.HelicsMessageFederate`.
    """
    f = loadSym("helicsCreateMessageFederate")
    err = helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateMessageFederateFromConfig(configFile: str) -> HelicsMessageFederate:
    """
    Create `helics.HelicsMessageFederate` from a JSON file or JSON string or TOML file.
    `helics.HelicsMessageFederate` objects can be used in all functions that take a `helics.HelicsFederate` object as an argument.

    **Parameters**

    * **`configFile`** - A config (JSON,TOML) file or a JSON string that contains setup and configuration information.

    **Returns**: `helics.HelicsMessageFederate`.
    """
    f = loadSym("helicsCreateMessageFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(configFile), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateCombinationFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsCombinationFederate:
    """
    Create a combination federate from `helics.HelicsFederateInfo`.
    Combination federates are both value federates and message federates, objects can be used in all functions
    that take a `helics.HelicsFederate` object as an argument.

    **Parameters**

    * **`fedName`** - A string with the name of the federate, can be NULL or an empty string to pull the default name from fi.
    * **`fi`** - The federate info object that contains details on the federate.

    **Returns**: `helics.HelicsCombinationFederate`.
    """
    f = loadSym("helicsCreateCombinationFederate")
    err = helicsErrorInitialize()
    result = f(cstring(fedName), fi, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCreateCombinationFederateFromConfig(configFile: str) -> HelicsCombinationFederate:
    """
    Create a combination federate from a JSON file or JSON string or TOML file.
    Combination federates are both value federates and message federates, objects can be used in all functions
    that take a `helics.HelicsFederate` object as an argument.

    **Parameters**

    * **`configFile`** - A JSON file or a JSON string or TOML file that contains setup and configuration information.

    **Returns**: `helics.HelicsCombinationFederate`.
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
    Create a new reference to an existing federate.
    This will create a new `helics.HelicsFederate` object that references the existing federate.
    The new object must be freed as well.

    **Parameters**

    * **`fed`** - An existing `helics.HelicsFederate`.

    **Returns**: `helics.HelicsFederate`.
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
    Create `helics.HelicsFederateInfo` for specifying federate information when constructing a federate.

    **Returns**: `helics.HelicsFederateInfo`.
    """
    f = loadSym("helicsCreateFederateInfo")
    result = f()
    return result


def helicsFederateInfoClone(fi: HelicsFederateInfo) -> HelicsFederateInfo:
    """
    Create `helics.HelicsFederateInfo` from an existing one and clone the information.

    **Parameters**

    * **`fi`** - A federateInfo object to duplicate.

    **Returns**: `helics.HelicsFederateInfo`.
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

    **Parameters**

    * **`fi`** - A federateInfo object.
    * **`argc`** - The number of command line arguments.
    * **`argv`** - An array of strings from the command line.
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
    Delete the memory associated with `helics.HelicsFederateInfo`.
    """
    f = loadSym("helicsFederateInfoFree")
    f(fi)


def helicsFederateIsValid(fed: HelicsFederate) -> bool:
    """
    Check if a `helics.HelicsFederate` is valid.

    **Returns**: `True` if the federate is a valid active federate, `False` otherwise.
    """
    f = loadSym("helicsFederateIsValid")
    result = f(fed)
    return result == 1


def helicsFederateInfoSetCoreName(fi: HelicsFederateInfo, corename: str):
    """
    Set the name of the core to link to for a federate.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`corename`** - The identifier for a core to link to.
    """
    f = loadSym("helicsFederateInfoSetCoreName")
    err = helicsErrorInitialize()
    f(fi, cstring(corename), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreInitString(fi: HelicsFederateInfo, coreInit: str):
    """
    Set the initialization string for the core usually in the form of command line arguments.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`coreInit`** - A string containing command line arguments to be passed to the core.
    """
    f = loadSym("helicsFederateInfoSetCoreInitString")
    err = helicsErrorInitialize()
    f(fi, cstring(coreInit), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerInitString(fi: HelicsFederateInfo, brokerInit: str):
    """
    Set the initialization string that a core will pass to a generated broker usually in the form of command line arguments.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`brokerInit`** - A string with command line arguments for a generated broker.
    """
    f = loadSym("helicsFederateInfoSetBrokerInitString")
    err = helicsErrorInitialize()
    f(fi, cstring(brokerInit), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreType(fi: HelicsFederateInfo, coretype: HelicsCoreType):
    """
    Set the core type by integer code.
    Valid values available by definitions in `api-data.h`.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`coretype`** - An numerical code for a core type see `helics.HelicsCoreType`.
    """
    f = loadSym("helicsFederateInfoSetCoreType")
    err = helicsErrorInitialize()
    f(fi, HelicsCoreType(coretype), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreTypeFromString(fi: HelicsFederateInfo, coretype: str):
    """
    Set the core type from a string.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`coretype`** - A string naming a core type.
    """
    f = loadSym("helicsFederateInfoSetCoreTypeFromString")
    err = helicsErrorInitialize()
    f(fi, cstring(coretype), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBroker(fi: HelicsFederateInfo, broker: str):
    """
    Set the name or connection information for a broker.
    This is only used if the core is automatically created, the broker information will be transferred to the core for connection.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`broker`** - A string which defines the connection information for a broker either a name or an address.
    """
    f = loadSym("helicsFederateInfoSetBroker")
    err = helicsErrorInitialize()
    f(fi, cstring(broker), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerKey(fi: HelicsFederateInfo, brokerkey: str):
    """
    Set the key for a broker connection.
    This is only used if the core is automatically created, the broker information will be transferred to the core for connection.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`brokerkey`** - A string containing a key for the broker to connect.
    """
    f = loadSym("helicsFederateInfoSetBrokerKey")
    err = helicsErrorInitialize()
    f(fi, cstring(brokerkey), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerPort(fi: HelicsFederateInfo, brokerPort: int):
    """
    Set the port to use for the broker.
    This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
    This will only be useful for network broker connections.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`brokerPort`** - The integer port number to use for connection with a broker.
    """
    f = loadSym("helicsFederateInfoSetBrokerPort")
    err = helicsErrorInitialize()
    f(fi, brokerPort, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetLocalPort(fi: HelicsFederateInfo, localPort: str):
    """
    Set the local port to use.
    This is only used if the core is automatically created, the port information will be transferred to the core for connection.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`localPort`** - A string with the port information to use as the local server port can be a number or "auto" or "os_local".
    """
    f = loadSym("helicsFederateInfoSetLocalPort")
    err = helicsErrorInitialize()
    f(fi, cstring(localPort), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetPropertyIndex(val: str) -> HelicsProperty:
    """
    Get a property index for use in `helics.helicsFederateInfoSetFlagOption`, `helics.helicsFederateInfoSetTimeProperty`, or `helics.helicsFederateInfoSetIntegerProperty`.

    **Parameters**

    * **`val`** - A string with the property name.

    **Returns**: An int with the property code or (-1) if not a valid property.
    """
    f = loadSym("helicsGetPropertyIndex")
    result = f(cstring(val))
    if result == -1:
        raise HelicsException(f"[-1] Unknown property index for flag `{val}`")
    else:
        return HelicsProperty(result)


def helicsGetFlagIndex(val: str) -> HelicsProperty:
    """
    Get a property index for use in `helics.helicsFederateInfoSetFlagOption`, `helics.helicsFederateSetFlagOption`.

    **Parameters**

    * **`val`** - A string with the option name.

    **Returns**: An int with the property code or (-1) if not a valid property.
    """
    f = loadSym("helicsGetFlagIndex")
    result = f(cstring(val))
    if result == -1:
        raise HelicsException(f"[-1] Unknown property index for flag `{val}`")
    else:
        return HelicsProperty(result)


def helicsGetOptionIndex(val: str) -> HelicsHandleOption:
    """
    Get an option index for use in `helics.helicsPublicationSetOption`, `helics.helicsInputSetOption`, `helics.helicsEndpointSetOption`,
    `helics.helicsFilterSetOption`, and the corresponding get functions

    **Parameters**

    * **`val`** - A string with the option name

    **Returns**: An int with the option index or (-1) if not a valid property.
    """
    f = loadSym("helicsGetOptionIndex")
    result = f(cstring(val))
    if result == -1:
        raise HelicsException(f"[-1] Unknown option index for flag `{val}`")
    else:
        return HelicsHandleOption(result)


def helicsGetOptionValue(val: str) -> int:
    """
    Get an option value for use in `helics.helicsPublicationSetOption`, `helics.helicsInputSetOption`, `helics.helicsEndpointSetOption`,
    `helics.helicsFilterSetOption`.

    **Parameters**

    * **`val`** - A string representing the value

    **Returns**: An int with the option value or (-1) if not a valid value.
    """
    f = loadSym("helicsGetOptionValue")
    result = f(cstring(val))
    if result == -1:
        raise HelicsException(f"[-1] Unknown option valud for flag `{val}`")
    else:
        return result


def helicsFederateInfoSetFlagOption(fi: HelicsFederateInfo, flag: HelicsFederateFlag, value: bool):
    """
    Set a flag in the info structure
    Valid flags are available `helics.HelicsFederateFlag`.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`flag`** - A numerical index for a flag.
    * **`value`** - The desired value of the flag `True` or `False`.
    """
    f = loadSym("helicsFederateInfoSetFlagOption")
    err = helicsErrorInitialize()
    f(fi, HelicsFederateFlag(flag), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetSeparator(fi: HelicsFederateInfo, separator: str):
    """
    Set the separator character in the info structure.
    The separator character is the separation character for local publications/endpoints in creating their global name.
    For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`separator`** - The character to use as a separator.
    """
    f = loadSym("helicsFederateInfoSetSeparator")
    err = helicsErrorInitialize()
    f(fi, cchar(separator), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetTimeProperty(fi: HelicsFederateInfo, timeProperty: HelicsProperty, propertyValue: HelicsTime):
    """
    Set the output delay for a federate.

    **Parameters**

    * **`fi`** - The federate info object to alter.
    * **`timeProperty`** - An integer representation of the time based property to set see `helics.HelicsProperty`.
    * **`propertyValue`** - The value of the property to set the timeProperty to.
    """
    f = loadSym("helicsFederateInfoSetTimeProperty")
    err = helicsErrorInitialize()
    f(fi, HelicsProperty(timeProperty), propertyValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetIntegerProperty(fi: HelicsFederateInfo, intProperty: HelicsProperty, propertyValue: int):
    """
    Set an integer property for a federate.
    Set known properties.

    **Parameters**

    * **`fi`** - The federateInfo object to alter.
    * **`intProperty`** - An int identifying the property.
    * **`propertyValue`** - The value to set the property to.
    """
    f = loadSym("helicsFederateInfoSetIntegerProperty")
    err = helicsErrorInitialize()
    f(fi, HelicsProperty(intProperty), propertyValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRegisterInterfaces(fed: HelicsFederate, file: str):
    """
    Load interfaces from a file.

    **Parameters**

    * **`fed`** - The federate to which to load interfaces.
    * **`file`** - The name of a file to load the interfaces from either JSON, or TOML.
    """
    f = loadSym("helicsFederateRegisterInterfaces")
    err = helicsErrorInitialize()
    f(fed, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGlobalError(fed: HelicsFederate, error_code: int, error_string: str):
    """
    Generate a global error from a federate.
    A global error halts the co-simulation completely.

    **Parameters**

    * **`fed`** - The federate to create an error in.
    * **`error_code`** - The integer code for the error.
    * **`error_string`** - A string describing the error.
    """
    f = loadSym("helicsFederateGlobalError")
    f(fed, error_code, cstring(error_string))


def helicsFederateLocalError(fed: HelicsFederate, error_code: int, error_string: str):
    """
    Generate a local error in a federate.
    This will propagate through the co-simulation but not necessarily halt the co-simulation, it has a similar effect to finalize but does allow some interaction with a core for a brief time.

    **Parameters**

    * **`fed`** - The federate to create an error in.
    * **`error_code`** - The integer code for the error.
    * **`error_string`** - A string describing the error.
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
    Enter the initialization state of a federate.
    The initialization state allows initial values to be set and received if the iteration is requested on entry to the execution state. This is a blocking call and will block until the core allows it to proceed.

    **Parameters**

    * **`fed`** - The federate to operate on.
    """
    f = loadSym("helicsFederateEnterInitializingMode")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterInitializingModeAsync(fed: HelicsFederate):
    """
    Non blocking alternative to `helics.helicsFederateEnterInitializingMode`.
    The function helicsFederateEnterInitializationModeFinalize must be called to finish the operation.

    **Parameters**

    * **`fed`** - The federate to operate on.
    """
    f = loadSym("helicsFederateEnterInitializingModeAsync")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateIsAsyncOperationCompleted(fed: HelicsFederate) -> bool:
    """
    Check if the current Asynchronous operation has completed.

    **Parameters**

    * **`fed`** - The federate to operate on.

    **Returns**: `True` if current operation has completed, else `False`.
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
    Finalize the entry to initialize mode that was initiated with `helics.helicsEnterInitializingModeAsync`.

    **Parameters**

    * **`fed`** - The federate desiring to complete the initialization step.
    """
    f = loadSym("helicsFederateEnterInitializingModeComplete")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingMode(fed: HelicsFederate):
    """
    Request that the federate enter the Execution mode.
    This call is blocking until granted entry by the `helics.HelicsCore`. On return from this call the federate will be at time 0. For an asynchronous alternative call see `helics.helicsFederateEnterExecutingModeAsync`

    **Parameters**

    * **`fed`** - A federate to change modes.
    """
    f = loadSym("helicsFederateEnterExecutingMode")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeAsync(fed: HelicsFederate):
    """
    Request that the federate enter the Execution mode.
    This call is non-blocking and will return immediately. Call `helics.helicsFederateEnterExecutingModeComplete` to finish the call sequence

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` to complete the call.
    """
    f = loadSym("helicsFederateEnterExecutingModeAsync")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeComplete(fed: HelicsFederate):
    """
    Complete the call to `helics.helicsFederateEnterExecutingModeAsync`.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` to complete the call.
    """
    f = loadSym("helicsFederateEnterExecutingModeComplete")
    err = helicsErrorInitialize()
    f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterative(fed: HelicsFederate, iterate: HelicsIterationRequest) -> HelicsIterationResult:
    """
    Request an iterative time.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status.

    **Parameters**

    * **`fed`** - The federate to make the request of.
    * **`iterate`** - The requested iteration mode.

    **Returns**: `helics.HelicsIterationResult`.
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
    Request an iterative entry to the execution mode.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status.

    **Parameters**

    * **`fed`** - The federate to make the request of.
    * **`iterate`** - The requested iteration mode.
    """
    f = loadSym("helicsFederateEnterExecutingModeIterativeAsync")
    err = helicsErrorInitialize()
    f(fed, iterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterativeComplete(fed: HelicsFederate,) -> HelicsIterationResult:
    """
    Complete the asynchronous iterative call into ExecutionMode.

    **Parameters**

    * **`fed`** - The federate to make the request of.

    **Returns**: `helics.HelicsIterationResult`.
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
    Get the current state of a federate.

    **Parameters**

    * **`fed`** - The federate to query.

    **Returns**: `helics.HelicsFederateState`.
    """
    f = loadSym("helicsFederateGetState")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFederateState(result)


def helicsFederateGetCoreObject(fed: HelicsFederate) -> HelicsCore:
    """
    Get the `helics.HelicsCore` associated with a federate.

    **Parameters**

    * **`fed`** - `helics.HelicsFederate`.

    **Returns**: `helics.HelicsCore`.
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
    Request the next time for federate execution.

    **Parameters**

    * **`fed`** - The federate to make the request of.
    * **`requestTime`** - The next requested time.

    **Returns**: `helics.HelicsTime`.
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
    Request the next time for federate execution.

    **Parameters**

    * **`fed`** - The federate to make the request of.
    * **`timeDelta`** - The requested amount of time to advance.

    **Returns**: `helics.HelicsTime`.
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
    Request the next time step for federate execution.
    Feds should have setup the period or `minDelta` for this to work well but it will request the next time step which is the current time plus the minimum time step.

    **Parameters**

    * **`fed`** - The federate to make the request of.

    **Returns**: `helics.HelicsTime`.
    """
    f = loadSym("helicsFederateRequestNextStep")
    err = helicsErrorInitialize()
    result = f(fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTimeIterative(
    fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest
) -> (HelicsTime, HelicsIterationResult):
    """
    Request an iterative time.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status.

    **Parameters**

    * **`fed`** - The federate to make the request of.
    * **`requestTime`** - The next desired time.
    * **`iterate`** - The requested iteration mode.

    **Returns**: `(helics.HelicsTime, helics.HelicsIterationResult)`.
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
    Request the next time for federate execution in an asynchronous call.
    Call `helics.helicsFederateRequestTimeComplete` to finish the call.

    **Parameters**

    * **`fed`** - The federate to make the request of.
    * **`requestTime`** - The next requested time.
    """
    f = loadSym("helicsFederateRequestTimeAsync")
    err = helicsErrorInitialize()
    f(fed, requestTime, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeComplete(fed: HelicsFederate) -> HelicsTime:
    """
    Complete an asynchronous requestTime call.

    **Parameters**

    * **`fed`** - The federate to make the request of.
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
    Request an iterative time through an asynchronous call.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status. Call `helics.helicsFederateRequestTimeIterativeComplete` to finish the process.

    **Parameters**

    * **`fed`** - The federate to make the request of.
    * **`requestTime`** - The next desired time.
    * **`iterate`** - The requested iteration mode.
    """
    f = loadSym("helicsFederateRequestTimeIterativeAsync")
    err = helicsErrorInitialize()
    f(fed, requestTime, iterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeIterativeComplete(fed: HelicsFederate) -> HelicsTime:
    """
    Complete an iterative time request asynchronous call.

    **Parameters**

    * **`fed`** - The federate to make the request of.

    **Returns**: The iteration specification of the result.
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
    Get the name of the federate.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` to query.

    **Returns**: A string with the name.
    """
    f = loadSym("helicsFederateGetName")
    result = f(fed)
    return ffi.string(result).decode()


def helicsFederateSetTimeProperty(fed: HelicsFederate, timeProperty: int, time: HelicsTime):
    """
    Set a time based property for a federate.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` to set the property for.
    * **`timeProperty`** - A integer code for a time property.
    * **`time`** - The requested value of the property.
    """
    f = loadSym("helicsFederateSetTimeProperty")
    err = helicsErrorInitialize()
    f(fed, timeProperty, time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetFlagOption(fed: HelicsFederate, flag: int, flagValue: bool):
    """
    Set a flag for the federate.

    **Parameters**

    * **`fed`** - The federate to alter a flag for.
    * **`flag`** - The flag to change.
    * **`flagValue`** - The new value of the flag. 0 for false, !=0 for true.
    """
    f = loadSym("helicsFederateSetFlagOption")
    err = helicsErrorInitialize()
    f(fed, flag, flagValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetSeparator(fed: HelicsFederate, separator: str):
    """
    Set the separator character in a federate.
    The separator character is the separation character for local publications/endpoints in creating their global name.
    For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.

    **Parameters**

    * **`fed`** - The federate info object to alter.
    * **`separator`** - The character to use as a separator.
    """
    f = loadSym("helicsFederateSetSeparator")
    err = helicsErrorInitialize()
    f(fed, cchar(separator), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetIntegerProperty(fed: HelicsFederate, intProperty: HelicsProperty, propertyVal: int):
    """
    Set an integer based property of a federate.

    **Parameters**

    * **`fed`** - The federate to change the property for.
    * **`intProperty`** - The property to set.
    * **`propertyVal`** - The value of the property.
    """
    f = loadSym("helicsFederateSetIntegerProperty")
    err = helicsErrorInitialize()
    f(fed, HelicsProperty(intProperty), propertyVal, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetTimeProperty(fed: HelicsFederate, timeProperty: int) -> HelicsTime:
    """
    Get the current value of a time based property in a federate.

    **Parameters**

    * **`fed`** - The federate query.
    * **`timeProperty`** - The property to query.

    **Returns**: `helics.HelicsTime`.
    """
    f = loadSym("helicsFederateGetTimeProperty")
    err = helicsErrorInitialize()
    result = f(fed, timeProperty, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetFlagOption(fed: HelicsFederate, flag: HelicsFederateFlag) -> bool:
    """
    Get a flag value for a federate.

    **Parameters**

    * **`fed`** - The federate to get the flag for.
    * **`flag`** - The `helics.HelicsFederateFlag` to query.
    """
    f = loadSym("helicsFederateGetFlagOption")
    err = helicsErrorInitialize()
    result = f(fed, flag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsFederateGetIntegerProperty(fed: HelicsFederate, intProperty: HelicsProperty) -> int:
    """
    Get the current value of an integer property (such as a logging level).

    **Parameters**

    * **`fed`** - The federate to get the flag for.
    * **`intProperty`** - A code for the property to set `helics.HelicsProperty`.
    """
    f = loadSym("helicsFederateGetIntegerProperty")
    err = helicsErrorInitialize()
    result = f(fed, HelicsProperty(intProperty), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetCurrentTime(fed: HelicsFederate) -> HelicsTime:
    """
    Get the current time of the federate.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` to query.

    **Returns**: `helics.HelicsTime`.
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
    Set a federation global value through a federate.
    This overwrites any previous value for this name.

    **Parameters**

    * **`fed`** - The federate to set the global through.
    * **`valueName`** - The name of the global to set.
    * **`value`** - The value of the global.
    """
    f = loadSym("helicsFederateSetGlobal")
    err = helicsErrorInitialize()
    f(fed, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateAddDependency(fed: HelicsFederate, fedName: str):
    """
    Add a time dependency for a federate. The federate will depend on the given named federate for time synchronization.

    **Parameters**

    * **`fed`** - The federate to add the dependency for.
    * **`fedName`** - The name of the federate to depend on.
    """
    f = loadSym("helicsFederateAddDependency")
    err = helicsErrorInitialize()
    f(fed, cstring(fedName), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetLogFile(fed: HelicsFederate, logFile: str):
    """
    Set the logging file for a federate (actually on the core associated with a federate).

    **Parameters**

    * **`fed`** - The federate to set the log file for.
    * **`logFile`** - The name of the log file.
    """
    f = loadSym("helicsFederateSetLogFile")
    err = helicsErrorInitialize()
    f(fed, cstring(logFile), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogErrorMessage(fed: HelicsFederate, logmessage: str):
    """
    Log an error message through a federate.

    **Parameters**

    * **`fed`** - The federate to log the error message through.
    * **`logmessage`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogErrorMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogWarningMessage(fed: HelicsFederate, logmessage: str):
    """
    Log a warning message through a federate.

    **Parameters**

    * **`fed`** - The federate to log the warning message through.
    * **`logmessage`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogWarningMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogInfoMessage(fed: HelicsFederate, logmessage: str):
    """
    Log an info message through a federate.

    **Parameters**

    * **`fed`** - The federate to log the info message through.
    * **`logmessage`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogInfoMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogDebugMessage(fed: HelicsFederate, logmessage: str):
    """
    Log a debug message through a federate.

    **Parameters**

    * **`fed`** - The federate to log the debug message through.
    * **`logmessage`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogDebugMessage")
    err = helicsErrorInitialize()
    f(fed, cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogLevelMessage(fed: HelicsFederate, loglevel: HelicsLogLevel, logmessage: str):
    """
    Log a message through a federate.

    **Parameters**

    * **`fed`** - The federate to log the message through.
    * **`loglevel`** - The level of the message to log see `helics.HelicsLogLevel`.
    * **`logmessage`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogLevelMessage")
    err = helicsErrorInitialize()
    f(fed, HelicsLogLevel(loglevel), cstring(logmessage), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetGlobal(core: HelicsCore, valueName: str, value: str):
    """
    Set a global value in a core.
    This overwrites any previous value for this name.

    **Parameters**

    * **`core`** - The core to set the global through.
    * **`valueName`** - The name of the global to set.
    * **`value`** - The value of the global.
    """
    f = loadSym("helicsCoreSetGlobal")
    err = helicsErrorInitialize()
    f(core, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetGlobal(broker: HelicsBroker, valueName: str, value: str):
    """
    Set a federation global value.
    This overwrites any previous value for this name.

    **Parameters**

    * **`broker`** - The broker to set the global through.
    * **`valueName`** - The name of the global to set.
    * **`value`** - The value of the global.
    """
    f = loadSym("helicsBrokerSetGlobal")
    err = helicsErrorInitialize()
    f(broker, cstring(valueName), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetLogFile(core: HelicsCore, logFileName: str):
    """
    Set the log file on a core.

    **Parameters**

    * **`core`** - The core to set the log file for.
    * **`logFileName`** - The name of the file to log to.
    """
    f = loadSym("helicsCoreSetLogFile")
    err = helicsErrorInitialize()
    f(core, cstring(logFileName), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetLogFile(broker: HelicsBroker, logFileName: str):
    """
    Set the log file on a broker.

    **Parameters**

    * **`broker`** - The broker to set the log file for.
    * **`logFileName`** - The name of the file to log to.
    """
    f = loadSym("helicsBrokerSetLogFile")
    err = helicsErrorInitialize()
    f(broker, cstring(logFileName), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCreateQuery(target: str, query: str) -> HelicsQuery:
    """
    Create a query object.
    A query object consists of a target and query string.

    **Parameters**

    * **`target`** - The name of the target to query.
    * **`query`** - The query to make of the target.

    **Returns**: `helics.HelicsQuery`.
    """
    f = loadSym("helicsCreateQuery")
    result = f(cstring(target), cstring(query))
    return result


def helicsQueryExecute(query: HelicsQuery, fed: HelicsFederate) -> str:
    """
    Execute a query.
    The call will block until the query finishes which may require communication or other delays.

    **Parameters**

    * **`query`** - The query object to use in the query.
    * **`fed`** - A federate to send the query through.

    **Returns**: String that contains the result of the query that was executed.
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
    Execute a query directly on a core.
    The call will block until the query finishes which may require communication or other delays.

    **Parameters**

    * **`query`** - The query object to use in the query.
    * **`core`** - The core to send the query to.

    **Returns**: String that contains the result of the query that was executed.
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
    Execute a query directly on a broker.
    The call will block until the query finishes which may require communication or other delays.

    **Parameters**

    * **`query`** - The query object to use in the query.
    * **`broker`** - The broker to send the query to.

    **Returns**: String that contains the result of the query that was executed.
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
    Execute a query in a non-blocking call.

    **Parameters**

    * **`query`** - The query object to use in the query.
    * **`fed`** - A federate to send the query through.
    """
    f = loadSym("helicsQueryExecuteAsync")
    err = helicsErrorInitialize()
    f(query, fed, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryExecuteComplete(query: HelicsQuery) -> str:
    """
    Complete the return from a query called with `helics.helicsExecuteQueryAsync`.
    The function will block until the query completes `isQueryComplete` can be called to determine if a query has completed or not.

    **Parameters**

    * **`query`** - The query object to complete execution of.

    **Returns**: String that contains the result of the query that was executed.
    """
    f = loadSym("helicsQueryExecuteComplete")
    err = helicsErrorInitialize()
    result = f(query, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsQueryIsCompleted(query: HelicsQuery) -> bool:
    """
    Check if an asynchronously executed query has completed.
    This function should usually be called after a QueryExecuteAsync function has been called.

    **Parameters**

    * **`query`** - The query object to check if completed

    **Returns**: Will return `True` if an asynchronous query has completed or a regular query call was made with a result, and false if an asynchronous query has not completed or is invalid.
    """
    f = loadSym("helicsQueryIsCompleted")
    result = f(query)
    return result == 1


def helicsQuerySetTarget(query: HelicsQuery, target: str):
    """
    Update the target of a query.

    **Parameters**

    * **`query`** - The query object to change the target of.
    * **`target`** - the name of the target to query.
    """
    f = loadSym("helicsQuerySetTarget")
    err = helicsErrorInitialize()
    f(query, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQuerySetQueryString(query: HelicsQuery, queryString: str):
    """
    Update the queryString of a query.

    **Parameters**

    * **`query`** - The query object to change the target of.
    * **`queryString`** - the new queryString.
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
    Function to do some housekeeping work.
    This runs some cleanup routines and tries to close out any residual thread that haven't been shutdown yet.
    """
    f = loadSym("helicsCleanupLibrary")
    f()


def helicsFederateRegisterEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
    """

    MessageFederate Calls.
    Create an endpoint.
    The endpoint becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for endpoints.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create an endpoint must have been created
              with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    * **`name`** - The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
    * **`type`** - A string describing the expected type of the publication (optional).

    **Returns**: `helics.HelicsEndpoint`.
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
    Create an endpoint.
    The endpoint becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for endpoints.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create an endpoint must have been created
           with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    * **`name`** - The identifier for the endpoint, the given name is the global identifier.
    * **`type`** - A string describing the expected type of the publication (optional).

    **Returns**: `helics.HelicsEndpoint`.
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
    Get an endpoint object from a name.

    **Parameters**

    * **`fed`** - The message `helics.HelicsFederate` to use to get the endpoint.
    * **`name`** - The name of the endpoint.

    **Returns**: `helics.HelicsEndpoint`.
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
    Get an endpoint by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsEndpoint`.
    """
    f = loadSym("helicsFederateGetEndpointByIndex")
    err = helicsErrorInitialize()
    result = f(fed, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsEndpointIsValid(endpoint: HelicsEndpoint) -> bool:
    """
    Check if an endpoint is valid.

    **Parameters**

    * **`endpoint`** - The endpoint object to check.

    **Returns**: `True` if the Endpoint object represents a valid endpoint.
    """
    f = loadSym("helicsEndpointIsValid")
    result = f(endpoint)
    return result == 1


def helicsEndpointSetDefaultDestination(endpoint: HelicsEndpoint, dest: str):
    """
    Set the default destination for an endpoint if no other endpoint is given.

    **Parameters**

    * **`endpoint`** - The endpoint to set the destination for.
    * **`dest`** - A string naming the desired default endpoint.
    """
    f = loadSym("helicsEndpointSetDefaultDestination")
    err = helicsErrorInitialize()
    f(endpoint, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetDefaultDestination(endpoint: HelicsEndpoint) -> str:
    """
    Get the default destination for an endpoint.

    **Parameters**

    * **`endpoint`** - The endpoint to set the destination for.

    **Returns**: A string with the default destination.
    """
    f = loadSym("helicsEndpointGetDefaultDestination")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsEndpointSendMessageRaw(endpoint: HelicsEndpoint, dest: str, data: bytes):
    """
    Send a message to the specified destination.

    **Parameters**

    * **`endpoint`** - The endpoint to send the data from.
    * **`dest`** - The target destination.
    * **`data`** - The data to send.
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
    Send a message at a specific time to the specified destination.

    **Parameters**

    * **`endpoint`** - The endpoint to send the data from.
    * **`dest`** - The target destination.
    * **`data`** - The data to send.
    * **`time`** - The time the message should be sent.
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

    _**Deprecated: Use `helics.helicsEndpointSendMessageObject` instead.**_

    **Parameters**

    * **`endpoint`** - The endpoint to send the data from.
    * **`message`** - The actual message to send.
    """
    f = loadSym("helicsEndpointSendMessage")
    err = helicsErrorInitialize()
    message = ffi.new("helics_message *", message)
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessageObject(endpoint: HelicsEndpoint, message: HelicsMessageObject):
    """
    Send a message object from a specific endpoint.

    **Parameters**

    * **`endpoint`** - The endpoint to send the data from.
    * **`message`** - The actual message to send which will be copied.
    """
    f = loadSym("helicsEndpointSendMessageObject")
    err = helicsErrorInitialize()
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessageObjectZeroCopy(endpoint: HelicsEndpoint, message: HelicsMessageObject):
    """
    Send a message object from a specific endpoint, the message will not be copied and the message object will no longer be valid after the call.

    **Parameters**

    * **`endpoint`** - The endpoint to send the data from.
    * **`message`** - The actual message to send which will be copied.
    """
    f = loadSym("helicsEndpointSendMessageObjectZeroCopy")
    err = helicsErrorInitialize()
    f(endpoint, message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSubscribe(endpoint: HelicsEndpoint, key: str):
    """
    Subscribe an endpoint to a publication.

    **Parameters**

    * **`endpoint`** - The endpoint to use.
    * **`key`** - The name of the publication.
    """
    f = loadSym("helicsEndpointSubscribe")
    err = helicsErrorInitialize()
    f(endpoint, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateHasMessage(fed: HelicsFederate) -> bool:
    """
    Check if the federate has any outstanding messages.

    **Parameters**

    * **`fed`** - The federate to check.

    **Returns**: `True` if the federate has a message waiting, `False` otherwise.
    """
    f = loadSym("helicsFederateHasMessage")
    result = f(fed)
    return result == 1


def helicsEndpointHasMessage(endpoint: HelicsEndpoint) -> bool:
    """
    Check if a given endpoint has any unread messages.

    **Parameters**

    * **`endpoint`** - The endpoint to check.

    **Returns**: `True` if the endpoint has a message, `False` otherwise.
    """
    f = loadSym("helicsEndpointHasMessage")
    result = f(endpoint)
    return result == 1


def helicsFederatePendingMessages(fed: HelicsFederate) -> int:
    """
    Returns the number of pending receives for the specified destination endpoint.

    **Parameters**

    * **`fed`** - The federate to get the number of waiting messages from.
    """
    f = loadSym("helicsFederatePendingMessages")
    return f(fed)


def helicsEndpointPendingMessages(endpoint: HelicsEndpoint) -> int:
    """
    Returns the number of pending receives for all endpoints of a particular federate.

    **Parameters**

    * **`endpoint`** - The endpoint to query.
    """
    f = loadSym("helicsEndpointPendingMessages")
    return f(endpoint)


def helicsEndpointGetMessage(endpoint: HelicsEndpoint) -> HelicsMessage:
    """
    Receive a packet from a particular endpoint.

    _**Deprecated: Use helicsEndpointGetMessageObject instead**_

    **Parameters**

    * **`endpoint`** - The identifier for the endpoint.

    **Returns**: A message object.
    """
    f = loadSym("helicsEndpointGetMessage")
    return f(endpoint)


def helicsEndpointGetMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject:
    """
    Receive a packet from a particular endpoint.

    **Parameters**

    * **`endpoint`** - The identifier for the endpoint.

    **Returns**: A message object.
    """
    f = loadSym("helicsEndpointGetMessageObject")
    return f(endpoint)


def helicsEndpointCreateMessageObject(endpoint: HelicsEndpoint) -> HelicsMessageObject:
    """
    Create a new empty message object.
    The message is empty and isValid will return false since there is no data associated with the message yet.

    **Parameters**

    * **`endpoint`** - The endpoint object to associate the message with.
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
    Receive a communication message for any endpoint in the federate.

    _**Deprecated: Use helicsFederateGetMessageObject instead**_

    The return order will be in order of endpoint creation. So all messages that are available for the first endpoint, then all for the second, and so on. Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival.

    **Returns**: A unique_ptr to a Message object containing the message data.
    """
    f = loadSym("helicsFederateGetMessage")
    result = f(fed)
    return result


def helicsFederateGetMessageObject(fed: HelicsFederate) -> HelicsMessageObject:
    """
    Receive a communication message for any endpoint in the federate.
    The return order will be in order of endpoint creation.
    So all messages that are available for the first endpoint, then all for the second, and so on.
    Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival.

    **Returns**: A `helics.HelicsMessageObject` which references the data in the message.
    """
    f = loadSym("helicsFederateGetMessageObject")
    result = f(fed)
    return result


def helicsFederateCreateMessageObject(fed: HelicsFederate) -> HelicsMessageObject:
    """
    Create a new empty message object.
    The message is empty and isValid will return false since there is no data associated with the message yet.

    **Parameters**

    * **`fed`** - the `helics.HelicsFederate` to associate the message with.
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
    Clear all stored messages from a federate.
    This clears messages retrieved through `helics.helicsFederateGetMessage` or `helics.helicsFederateGetMessageObject`.

    **Parameters**

    * **`fed`** - The federate to clear the message for.
    """
    f = loadSym("helicsFederateClearMessages")
    f(fed)


def helicsEndpointClearMessages(endpoint: HelicsEndpoint):
    """
    Clear all message from an endpoint.

    _**Deprecated: Use `helics.helicsFederateClearMessages` to free all messages, or `helics.helicsMessageFree` to clear an individual message.

    **Parameters**

    * **`endpoint`** - The endpoint object to operate on.
    """
    f = loadSym("helicsEndpointClearMessages")
    f(endpoint)


def helicsEndpointGetType(endpoint: HelicsEndpoint) -> str:
    """
    Get the type specified for an endpoint.

    **Parameters**

    * **`endpoint`** - The endpoint object in question.

    **Returns**: The defined type of the endpoint.
    """
    f = loadSym("helicsEndpointGetType")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsEndpointGetName(endpoint: HelicsEndpoint) -> str:
    """
    Get the name of an endpoint.

    **Parameters**

    * **`endpoint`** - The endpoint object in question.

    **Returns**: The name of the endpoint.
    """
    f = loadSym("helicsEndpointGetName")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsFederateGetEndpointCount(fed: HelicsFederate) -> int:
    """
    Get the number of endpoints in a federate.

    **Parameters**

    * **`fed`** - The message federate to query.

    **Returns**: (-1) if fed was not a valid federate, otherwise returns the number of endpoints.
    """
    f = loadSym("helicsFederateGetEndpointCount")
    result = f(fed)
    return result


def helicsEndpointGetInfo(endpoint: HelicsEndpoint) -> str:
    """
    Get the data in the info field of a filter.

    **Parameters**

    * **`end`** - The filter to query.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsEndpointGetInfo")
    result = f(endpoint)
    return ffi.string(result).decode()


def helicsEndpointSetInfo(endpoint: HelicsEndpoint, info: str):
    """
    Set the data in the info field for a filter.

    **Parameters**

    * **`end`** - The endpoint to query.
    * **`info`** - The string to set.
    """
    f = loadSym("helicsEndpointSetInfo")
    err = helicsErrorInitialize()
    f(endpoint, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSetOption(endpoint: HelicsEndpoint, option: HelicsHandleOption, value: int):
    """
    Set a handle option on an endpoint.

    **Parameters**

    * **`end`** - The endpoint to modify.
    * **`option`** - Integer code for the option to set `helics.HelicsHandleOption`.
    * **`value`** - The value to set the option to.
    """
    f = loadSym("helicsEndpointSetOption")
    err = helicsErrorInitialize()
    f(endpoint, HelicsHandleOption(option), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetOption(endpoint: HelicsEndpoint, option: HelicsHandleOption) -> int:
    """
    Get the value of handle option on an endpoint.

    **Parameters**

    * **`end`** - The endpoint to modify.
    * **`option`** - Integer code for the option to set `helics.HelicsHandleOption`.

    **Returns**: the value of the option, for boolean options will be 0 or 1.
    """
    f = loadSym("helicsEndpointGetOption")
    result = f(endpoint, HelicsHandleOption(option))
    return result


def helicsMessageGetSource(message: HelicsMessageObject) -> str:
    """
    Message operation functions.
    Functions for working with helics message envelopes.
    Get the source endpoint of a message.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: A string with the source endpoint.
    """
    f = loadSym("helicsMessageGetSource")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetDestination(message: HelicsMessageObject) -> str:
    """
    Get the destination endpoint of a message.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: A string with the destination endpoint.
    """
    f = loadSym("helicsMessageGetDestination")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetOriginalSource(message: HelicsMessageObject) -> str:
    """
    Get the original source endpoint of a message, the source may have been modified by filters or other actions.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: A string with the source of a message.
    """
    f = loadSym("helicsMessageGetOriginalSource")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetOriginalDestination(message: HelicsMessageObject) -> str:
    """
    Get the original destination endpoint of a message, the destination may have been modified by filters or other actions.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: A string with the original destination of a message.
    """
    f = loadSym("helicsMessageGetOriginalDestination")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetTime(message: HelicsMessageObject) -> HelicsTime:
    """
    Get the helics time associated with a message.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: The time associated with a message.
    """
    f = loadSym("helicsMessageGetTime")
    result = f(message)
    return result


def helicsMessageGetString(message: HelicsMessageObject) -> str:
    """
    Get the payload of a message as a string.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: A string representing the payload of a message.
    """
    f = loadSym("helicsMessageGetString")
    result = f(message)
    return ffi.string(result).decode()


def helicsMessageGetMessageID(message: HelicsMessageObject) -> int:
    """
    Get the messageID of a message.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: The messageID.
    """
    f = loadSym("helicsMessageGetMessageID")
    result = f(message)
    return result


def helicsMessageCheckFlag(message: HelicsMessageObject, flag: int) -> bool:
    """
    Check if a flag is set on a message.

    **Parameters**

    * **`message`** - The message object in question.
    * **`flag`** - The flag to check should be between [0,15].

    **Returns**: The flags associated with a message.
    """
    f = loadSym("helicsMessageCheckFlag")
    result = f(message, flag)
    return result == 1


def helicsMessageGetRawDataSize(message: HelicsMessageObject) -> int:
    """
    Get the size of the data payload in bytes.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: The size of the data payload.
    """
    f = loadSym("helicsMessageGetRawDataSize")
    result = f(message)
    return result


def helicsMessageGetRawData(message: HelicsMessageObject) -> bytes:
    """
    Get the raw data for a message object.

    **Parameters**

    * **`message`** - A message object to get the data for.

    **Returns**: Raw string data.
    """
    f = loadSym("helicsMessageGetRawData")
    err = helicsErrorInitialize()
    data = ffi.new("char *")
    maxMessageLen = helicsMessageGetRawDataSize(message)
    actualSize = ffi.new("int *")
    r = f(message, data, maxMessageLen, actualSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    return r


def helicsMessageGetRawDataPointer(message: HelicsMessageObject) -> pointer:
    """
    Get a pointer to the raw data of a message.

    **Parameters**

    * **`message`** - A message object to get the data for.

    **Returns**: A pointer to the raw data in memory, the pointer may be NULL if the message is not a valid message.
    """
    f = loadSym("helicsMessageGetRawDataPointer")
    result = f(message)
    return result


def helicsMessageIsValid(message: HelicsMessageObject) -> bool:
    """
    A check if the message contains a valid payload.

    **Parameters**

    * **`message`** - The message object in question.

    **Returns**: `True` if the message contains a payload.
    """
    f = loadSym("helicsMessageIsValid")
    result = f(message)
    return result == 1


def helicsMessageSetSource(message: HelicsMessageObject, src: str):
    """
    Set the source of a message.

    **Parameters**

    * **`message`** - The message object in question.
    * **`src`** - A string containing the source.
    """
    f = loadSym("helicsMessageSetSource")
    err = helicsErrorInitialize()
    f(message, cstring(src), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetDestination(message: HelicsMessageObject, dest: str):
    """
    Set the destination of a message.

    **Parameters**

    * **`message`** - The message object in question.
    * **`dest`** - A string containing the new destination.
    """
    f = loadSym("helicsMessageSetDestination")
    err = helicsErrorInitialize()
    f(message, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalSource(message: HelicsMessageObject, src: str):
    """
    Set the original source of a message.

    **Parameters**

    * **`message`** - The message object in question.
    * **`src`** - A string containing the new original source.
    """
    f = loadSym("helicsMessageSetOriginalSource")
    err = helicsErrorInitialize()
    f(message, cstring(src), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalDestination(message: HelicsMessageObject, dest: str):
    """
    Set the original destination of a message.

    **Parameters**

    * **`message`** - The message object in question.
    * **`dest`** - A string containing the new original source.
    """
    f = loadSym("helicsMessageSetOriginalDestination")
    err = helicsErrorInitialize()
    f(message, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetTime(message: HelicsMessageObject, time: HelicsTime):
    """
    Set the delivery time for a message.

    **Parameters**

    * **`message`** - The message object in question.
    * **`time`** - The time the message should be delivered.
    """
    f = loadSym("helicsMessageSetTime")
    err = helicsErrorInitialize()
    f(message, time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageResize(message: HelicsMessageObject, newSize: int):
    """
    Resize the data buffer for a message.
    The message data buffer will be resized. There are no guarantees on what is in the buffer in newly allocated space.
    If the allocated space is not sufficient new allocations will occur

    **Parameters**

    * **`message`** - The message object in question.
    * **`newSize`** - The new size in bytes of the buffer.
    """
    f = loadSym("helicsMessageResize")
    err = helicsErrorInitialize()
    f(message, newSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageReserve(message: HelicsMessageObject, reserveSize: int):
    """
    Reserve space in a buffer but don't actually resize.
    The message data buffer will be reserved but not resized.

    **Parameters**

    * **`message`** - The message object in question.
    * **`reserveSize`** - The number of bytes to reserve in the message object.
    """
    f = loadSym("helicsMessageReserve")
    err = helicsErrorInitialize()
    f(message, reserveSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetMessageID(message: HelicsMessageObject, messageID: int):
    """
    Set the message ID for the message.
    Normally this is not needed and the core of HELICS will adjust as needed.

    **Parameters**

    * **`message`** - The message object in question.
    * **`messageID`** - A new message ID.
    """
    f = loadSym("helicsMessageSetMessageID")
    err = helicsErrorInitialize()
    f(message, messageID, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClearFlags(message: HelicsMessageObject):
    """
    Clear the flags of a message.

    **Parameters**

    * **`message`** - The message object in question.
    """
    f = loadSym("helicsMessageClearFlags")
    f(message)


def helicsMessageSetFlagOption(message: HelicsMessageObject, flag: int, flagValue: bool):
    """
    Set a flag on a message.

    **Parameters**

    * **`message`** - The message object in question.
    * **`flag`** - An index of a flag to set on the message.
    * **`flagValue`** - The desired value of the flag.
    """
    f = loadSym("helicsMessageSetFlagOption")
    err = helicsErrorInitialize()
    f(message, flag, flagValue, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetString(message: HelicsMessageObject, string: str):
    """
    Set the data payload of a message as a string.

    **Parameters**

    * **`message`** - The message object in question.
    * **`str`** - A string containing the message data.
    """
    f = loadSym("helicsMessageSetString")
    err = helicsErrorInitialize()
    f(message, cstring(string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetData(message: HelicsMessageObject, data: str):
    """
    Set the data payload of a message as raw data.

    **Parameters**

    * **`message`** - The message object in question.
    * **`data`** - A string containing the message data.
    * **`inputDataLength`** - The length of the data to input.
    """
    f = loadSym("helicsMessageSetData")
    err = helicsErrorInitialize()
    inputDataLength = len(data)
    f(message, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageAppendData(message: HelicsMessageObject, data: pointer, inputDataLength: int):
    """
    Append data to the payload.

    **Parameters**

    * **`message`** - The message object in question.
    * **`data`** - A string containing the message data to append.
    * **`inputDataLength`** - The length of the data to input.
    """
    f = loadSym("helicsMessageAppendData")
    err = helicsErrorInitialize()
    f(message, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageCopy(source_message: HelicsMessageObject, dest_message: HelicsMessageObject):
    """
    Copy a message object.

    **Parameters**

    * **`source_message`** - The message object to copy from.
    * **`dest_message`** - The message object to copy to.
    """
    f = loadSym("helicsMessageCopy")
    err = helicsErrorInitialize()
    f(source_message, dest_message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClone(message: HelicsMessageObject) -> HelicsMessageObject:
    """
    Clone a message object.

    **Parameters**

    * **`message`** - The message object to copy from.

    **Returns**: `helics.HelicsMessageObject`.
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
    Free a message object from memory. Memory for message is managed so not using this function does not create memory leaks, this is an indication to the system that the memory for this message is done being used and can be reused for a new message.
    `helics.helicsFederateClearMessages` can also be used to clear up all stored messages at once.
    """
    f = loadSym("helicsMessageFree")
    f(message)


def helicsFederateRegisterFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a source Filter on the specified federate.
    Filters can be created through a federate or a core, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

    **Parameters**

    * **`fed`** - The federate to register through.
    * **`type`** - The type of filter to create `helics.HelicsFilterType`.
    * **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateRegisterFilter")
    err = helicsErrorInitialize()
    result = f(fed, HelicsFilterType(type), cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a global source filter through a federate.
    Filters can be created through a federate or a core, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

    **Parameters**

    * **`fed`** - The federate to register through.
    * **`type`** - The type of filter to create `helics.HelicsFilterType`.
    * **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateRegisterGlobalFilter")
    err = helicsErrorInitialize()
    result = f(fed, HelicsFilterType(type), cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Create a cloning Filter on the specified federate.
    Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

    **Parameters**

    * **`fed`** - The federate to register through.
    * **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
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
    Create a global cloning Filter on the specified federate.
    Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

    **Parameters**

    * **`fed`** - The federate to register through.
    * **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
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
    Create a source Filter on the specified core.
    Filters can be created through a federate or a core, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

    **Parameters**

    * **`core`** - The core to register through.
    * **`type`** - The type of filter to create `helics.HelicsFilterType`.
    * **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsCoreRegisterFilter")
    err = helicsErrorInitialize()
    result = f(core, HelicsFilterType(type), cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsCoreRegisterCloningFilter(core: HelicsCore, name: str) -> HelicsFilter:
    """
    Create a cloning Filter on the specified core.
    Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

    **Parameters**

    * **`core`** - The core to register through.
    * **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
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
    Get the number of filters registered through a federate.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` to use to get the filter.

    **Returns**: A count of the number of filters registered through a federate.
    """
    f = loadSym("helicsFederateGetFilterCount")
    result = f(fed)
    return result


def helicsFederateGetFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Get a filter by its name, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` to use to get the filter.
    * **`name`** - The name of the filter.

    **Returns**: `helics.HelicsFilter`.
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
    Get a filter by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateGetFilterByIndex")
    err = helicsErrorInitialize()
    result = f(fed, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFilterIsValid(filt: HelicsFilter) -> bool:
    """
    Check if a filter is valid.

    **Parameters**

    * **`filt`** - The filter object to check.

    **Returns**: `True` if the Filter object represents a valid filter.
    """
    f = loadSym("helicsFilterIsValid")
    result = f(filt)
    return result == 1


def helicsFilterGetName(filt: HelicsFilter) -> str:
    """
    Get the name of the filter and store in the given string.

    **Parameters**

    * **`filt`** - The given filter.

    **Returns**: A string with the name of the filter.
    """
    f = loadSym("helicsFilterGetName")
    result = f(filt)
    return ffi.string(result).decode()


def helicsFilterSet(filt: HelicsFilter, prop: str, val: float):
    """
    Set a property on a filter.

    **Parameters**

    * **`filt`** - The filter to modify.
    * **`prop`** - A string containing the property to set.
    * **`val`** - A numerical value for the property.
    """
    f = loadSym("helicsFilterSet")
    err = helicsErrorInitialize()
    f(filt, cstring(prop), cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetString(filt: HelicsFilter, prop: str, val: str):
    """
    Set a string property on a filter.

    **Parameters**

    * **`filt`** - The filter to modify.
    * **`prop`** - A string containing the property to set.
    * **`val`** - A string containing the new value.
    """
    f = loadSym("helicsFilterSetString")
    err = helicsErrorInitialize()
    f(filt, cstring(prop), cstring(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDestinationTarget(filt: HelicsFilter, dest: str):
    """
    Add a destination target to a filter.
    All messages going to a destination are copied to the delivery address(es).

    **Parameters**

    * **`filt`** - The given filter to add a destination target to.
    * **`dest`** - The name of the endpoint to add as a destination target.
    """
    f = loadSym("helicsFilterAddDestinationTarget")
    err = helicsErrorInitialize()
    f(filt, cstring(dest), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddSourceTarget(filt: HelicsFilter, source: str):
    """
    Add a source target to a filter.
    All messages coming from a source are copied to the delivery address(es).

    **Parameters**

    * **`filt`** - The given filter.
    * **`source`** - The name of the endpoint to add as a source target.
    """
    f = loadSym("helicsFilterAddSourceTarget")
    err = helicsErrorInitialize()
    f(filt, cstring(source), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
    """
    Clone filter functions.
    Functions that manipulate cloning filters in some way.
    Add a delivery endpoint to a cloning filter.
    All cloned messages are sent to the delivery address(es).

    **Parameters**

    * **`filt`** - The given filter.
    * **`deliveryEndpoint`** - The name of the endpoint to deliver messages to.
    """
    f = loadSym("helicsFilterAddDeliveryEndpoint")
    err = helicsErrorInitialize()
    f(filt, cstring(deliveryEndpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveTarget(filt: HelicsFilter, target: str):
    """
    Remove a destination target from a filter.

    **Parameters**

    * **`filt`** - The given filter.
    * **`target`** - The named endpoint to remove as a target.
    """
    f = loadSym("helicsFilterRemoveTarget")
    err = helicsErrorInitialize()
    f(filt, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
    """
    Remove a delivery destination from a cloning filter.

    **Parameters**

    * **`filt`** - The given filter (must be a cloning filter).
    * **`deliveryEndpoint`** - A string with the delivery endpoint to remove.
    """
    f = loadSym("helicsFilterRemoveDeliveryEndpoint")
    err = helicsErrorInitialize()
    f(filt, cstring(deliveryEndpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetInfo(filt: HelicsFilter) -> str:
    """
    Get the data in the info field of a filter.

    **Parameters**

    * **`filt`** - The given filter.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsFilterGetInfo")
    result = f(filt)
    return ffi.string(result).decode()


def helicsFilterSetInfo(filt: HelicsFilter, info: str):
    """
    Set the data in the info field for a filter

    **Parameters**

    * **`filt`** - The given filter.
    * **`info`** - The string to set.
    """
    f = loadSym("helicsFilterSetInfo")
    err = helicsErrorInitialize()
    f(filt, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetOption(filt: HelicsFilter, option: HelicsHandleOption, value: int):
    """
    Set the data in the info field for a filter.

    **Parameters**

    * **`filt`** - The given filter.
    * **`option`** - The option to set `helics.HelicsHandleOption`.
    * **`value`** - The value of the option commonly 0 for false 1 for true.
    """
    f = loadSym("helicsFilterSetOption")
    err = helicsErrorInitialize()
    f(filt, HelicsHandleOption(option), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetOption(filt: HelicsFilter, option: HelicsHandleOption) -> int:
    """
    Get a handle option for the filter.

    **Parameters**

    * **`filt`** - The given filter to query.
    * **`option`** - The option to query `helics.HelicsHandleOption`.

    **Returns**: `int`.
    """
    f = loadSym("helicsFilterGetOption")
    result = f(filt, HelicsHandleOption(option))
    return result


def helicsFederateRegisterSubscription(fed: HelicsFederate, key: str, units: str = "") -> HelicsInput:
    """
    Functions related to value federates for the C api.
    Create a subscription.
    The subscription becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a subscription, must have been created with `helics.helicsCreateValueFederate` or
    `helics.helicsCreateCombinationFederate`.
    * **`key`** - The identifier matching a publication to get a subscription for.
    * **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsSubscription`.
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
    Register a publication with a known type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`key`** - The identifier for the publication the global publication key will be prepended with the federate name.
    * **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    * **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterPublication")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a publication with a defined type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`key`** - The identifier for the publication.
    * **`type`** - A string labeling the type of the publication.
    * **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
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
    Register a global named publication with an arbitrary type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`key`** - The identifier for the publication.
    * **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    * **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterGlobalPublication")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a global publication with a defined type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`key`** - The identifier for the publication.
    * **`type`** - A string describing the expected type of the publication.
    * **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
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
    Register a named input.
    The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions, inputs, and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create an input.
    * **`key`** - The identifier for the publication the global input key will be prepended with the federate name.
    * **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    * **`units`** - A string listing the units of the input (optional).

    **Returns**: `helics.HelicsInput`.
    """
    f = loadSym("helicsFederateRegisterInput")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsInput:
    """
    Register an input with a defined type.
    The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions, inputs, and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create an input.
    * **`key`** - The identifier for the input.
    * **`type`** - A string describing the expected type of the input.
    * **`units`** - A string listing the units of the input maybe NULL.

    **Returns**: `helics.HelicsPublication`.
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
    Register a global named input.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`key`** - The identifier for the publication.
    * **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    * **`units`** - A string listing the units of the subscription maybe NULL.

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterGlobalInput")
    err = helicsErrorInitialize()
    result = f(fed, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRegisterGlobalTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a global publication with an arbitrary type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`key`** - The identifier for the publication.
    * **`type`** - A string defining the type of the input.
    * **`units`** - A string listing the units of the subscription maybe NULL.

    **Returns**: `helics.HelicsPublication`.
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
    Get a `helics.HelicsPublication` from a key.

    **Parameters**

    * **`fed`** - The value `helics.HelicsFederate` to use to get the publication.
    * **`key`** - The name of the publication.

    **Returns**: `helics.HelicsPublication`.
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
    Get a publication by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsPublication`.
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
    Get an input object from a key.

    **Parameters**

    * **`fed`** - The value `helics.HelicsFederate` to use to get the publication.
    * **`key`** - The name of the input.

    **Returns**: `helics.HelicsInput`.
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
    Get an input by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    * **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    * **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsInput`
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
    Get an input object from a subscription target.

    **Parameters**

    * **`fed`** - The value `helics.HelicsFederate` to use to get the publication.
    * **`key`** - The name of the publication that a subscription is targeting.

    **Returns**: `helics.HelicsInput`
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
    Clear all the update flags from a federates inputs.

    **Parameters**

    * **`fed`** - The value `helics.HelicsFederate` for which to clear update flags.
    """
    f = loadSym("helicsFederateClearUpdates")
    f(fed)


def helicsFederateRegisterFromPublicationJSON(fed: HelicsFederate, json: str):
    """
    Register the publications via JSON publication string.

    **Parameters**

    * **`fed`** - The value `helics.HelicsFederate` to use to register the publications.
    * **`json`** - The JSON publication string.
    """
    f = loadSym("helicsFederateRegisterFromPublicationJSON")
    err = helicsErrorInitialize()
    f(fed, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederatePublishJSON(fed: HelicsFederate, json: str):
    """
    Publish data contained in a JSON file or string.

    **Parameters**

    * **`fed`** - The value `helics.HelicsFederate` through which to publish the data.
    * **`json`** - The publication file name or literal JSON data string.
    """
    f = loadSym("helicsFederatePublishJSON")
    err = helicsErrorInitialize()
    f(fed, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationIsValid(pub: HelicsPublication) -> bool:
    """
    Publication functions.
    Functions for publishing data of various kinds.
    The data will get translated to the type specified when the publication was constructed automatically regardless of the function used to publish the data.
    Check if a publication is valid.

    **Parameters**

    * **`pub`** - The publication to check

    **Returns**: `True` if the publication is a valid publication.
    """
    f = loadSym("helicsPublicationIsValid")
    result = f(pub)
    return result == 1


def helicsPublicationPublishRaw(pub: HelicsPublication, data: pointer, inputDataLength: int):
    """
    Publish raw data from a char * and length.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`data`** - A pointer to the raw data.
    * **`inputDataLength`** - The size in bytes of the data to publish.
    """
    f = loadSym("helicsPublicationPublishRaw")
    err = helicsErrorInitialize()
    f(pub, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishString(pub: HelicsPublication, string: str):
    """
    Publish a string.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`str`** - The string to publish.
    """
    f = loadSym("helicsPublicationPublishString")
    err = helicsErrorInitialize()
    f(pub, cstring(string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishInteger(pub: HelicsPublication, val: int):
    """
    Publish an integer value.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`val`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishInteger")
    err = helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishBoolean(pub: HelicsPublication, val: bool):
    """
    Publish a Boolean Value.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`val`** - The boolean value to publish.
    """
    f = loadSym("helicsPublicationPublishBoolean")
    err = helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishDouble(pub: HelicsPublication, val: float):
    """
    Publish a double floating point value.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`val`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishDouble")
    err = helicsErrorInitialize()
    f(pub, cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishTime(pub: HelicsPublication, val: HelicsTime):
    """
    Publish a time value.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`val`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishTime")
    err = helicsErrorInitialize()
    f(pub, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishChar(pub: HelicsPublication, val: str):
    """
    Publish a single character.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`val`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishChar")
    err = helicsErrorInitialize()
    f(pub, cchar(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishComplex(pub: HelicsPublication, c: complex):
    """
    Publish a complex value (or pair of values).

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`c`** - `complex` number
    """
    f = loadSym("helicsPublicationPublishComplex")
    err = helicsErrorInitialize()
    f(pub, c.real, c.imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishVector(pub: HelicsPublication, vectorInput: List[float]):
    """
    Publish a vector of doubles.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`vectorInput`** - A pointer to an array of double data.
    """
    f = loadSym("helicsPublicationPublishVector")
    err = helicsErrorInitialize()
    vectorLength = len(vectorInput)
    f(pub, vectorInput, vectorLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishNamedPoint(pub: HelicsPublication, string: str, val: float):
    """
    Publish a named point.

    **Parameters**

    * **`pub`** - The publication to publish for.
    * **`str`** - A string for the name to publish.
    * **`val`** - A double for the value to publish.
    """
    f = loadSym("helicsPublicationPublishNamedPoint")
    err = helicsErrorInitialize()
    f(pub, cstring(string), cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationAddTarget(pub: HelicsPublication, target: str):
    """
    Add a named input to the list of targets a publication publishes to.

    **Parameters**

    * **`pub`** - The publication to add the target for.
    * **`target`** - The name of an input that the data should be sent to.
    """
    f = loadSym("helicsPublicationAddTarget")
    err = helicsErrorInitialize()
    f(pub, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsValid(ipt: HelicsInput) -> bool:
    """
    Check if an input is valid.

    **Parameters**

    * **`ipt`** - The input to check

    **Returns**: `True` if the Input object represents a valid input.
    """
    f = loadSym("helicsInputIsValid")
    result = f(ipt)
    return result == 1


def helicsInputAddTarget(ipt: HelicsInput, target: str):
    """
    Add a publication to the list of data that an input subscribes to.

    **Parameters**

    * **`ipt`** - The named input to modify.
    * **`target`** - The name of a publication that an input should subscribe to.
    """
    f = loadSym("helicsInputAddTarget")
    err = helicsErrorInitialize()
    f(ipt, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetRawValueSize(ipt: HelicsInput) -> int:
    """
    Data can be returned in a number of formats,  for instance if data is published as a double it can be returned as a string and vice versa,  not all translations make that much sense but they do work.
    Get the size of the raw value for subscription.

    **Returns**: The size of the raw data/string in bytes.
    """
    f = loadSym("helicsInputGetRawValueSize")
    result = f(ipt)
    return result


def helicsInputGetRawValue(ipt: HelicsInput) -> str:
    """
    Get the raw data for the latest value of a subscription.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: Raw string data.
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
    Get the size of a value for subscription assuming return as a string.

    **Returns**: The size of the string.
    """
    f = loadSym("helicsInputGetStringSize")
    result = f(ipt)
    return result


def helicsInputGetString(ipt: HelicsInput) -> str:
    """
    Get a string value from a subscription.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: A string data
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
    Get an integer value from a subscription.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: An int64_t value with the current value of the input.
    """
    f = loadSym("helicsInputGetInteger")
    err = helicsErrorInitialize()
    result = f(ipt, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsInputGetBoolean(ipt: HelicsInput) -> bool:
    """
    Get a boolean value from a subscription.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: A boolean value of current input value.
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
    Get a double value from a subscription..

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: The double value of the input.
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
    Get a time value from a subscription.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: The resulting time value.
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
    Get a single character value from an input.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: The resulting character value.
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
    Get a complex object from an input object.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: `complex`.
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
    Get a pair of double forming a complex number from a subscriptions.

    **Parameters**

    * **`ipt`** - The input to get the data for.

    **Returns**: a pair of floating point values that represent the real and imag values
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
    Get the size of a value for subscription assuming return as an array of doubles.

    **Returns**: The number of doubles in a returned vector.
    """
    f = loadSym("helicsInputGetVectorSize")
    result = f(ipt)
    return result


def helicsInputGetVector(ipt: HelicsInput) -> List[float]:
    """
    Get a vector from a subscription.

    **Parameters**

    * **`ipt`** - The input to get the result for.

    **Returns**: a list of floating point values
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
    Get a named point from a subscription.

    **Parameters**

    * **`ipt`** - The input to get the result for.

    **Returns**: a string and a double value for the named point
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

    Default Value functions.
    These functions set the default value for a subscription. That is the value returned if nothing was published from elsewhere.
    Set the default as a raw data array.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`data`** - A pointer to the raw data to use for the default.
    """
    f = loadSym("helicsInputSetDefaultRaw")
    err = helicsErrorInitialize()
    inputDataLength = len(data)
    f(ipt, cstring(data), inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultString(ipt: HelicsInput, string: str):
    """
    Set the default as a string.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`str`** - A pointer to the default string.
    """
    f = loadSym("helicsInputSetDefaultString")
    err = helicsErrorInitialize()
    f(ipt, cstring(string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultInteger(ipt: HelicsInput, val: int):
    """
    Set the default as an integer.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`val`** - The default integer.
    """
    f = loadSym("helicsInputSetDefaultInteger")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultBoolean(ipt: HelicsInput, val: bool):
    """
    Set the default as a boolean.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`val`** - The default boolean value.
    """
    f = loadSym("helicsInputSetDefaultBoolean")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultTime(ipt: HelicsInput, val: HelicsTime):
    """
    Set the default as a time.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`val`** - The default time value.
    """
    f = loadSym("helicsInputSetDefaultTime")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultChar(ipt: HelicsInput, val: str):
    """
    Set the default as a char.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`val`** - The default char value.
    """
    f = loadSym("helicsInputSetDefaultChar")
    err = helicsErrorInitialize()
    f(ipt, cchar(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultDouble(ipt: HelicsInput, val: float):
    """
    Set the default as a double.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`val`** - The default double value.
    """
    f = loadSym("helicsInputSetDefaultDouble")
    err = helicsErrorInitialize()
    f(ipt, val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultComplex(ipt: HelicsInput, c: complex):
    """
    Set the default as a complex number.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`real`** - The default real value.
    * **`imag`** - The default imaginary value.
    """
    f = loadSym("helicsInputSetDefaultComplex")
    err = helicsErrorInitialize()
    f(ipt, c.real, c.imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultVector(ipt: HelicsInput, vectorInput: List[float]):
    """
    Set the default as a vector of doubles.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`vectorInput`** - A pointer to an array of double data.
    * **`vectorLength`** - The number of points to publish.
    """
    f = loadSym("helicsInputSetDefaultVector")
    err = helicsErrorInitialize()
    vectorLength = len(vectorInput)
    f(ipt, vectorInput, vectorLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultNamedPoint(ipt: HelicsInput, string: str, val: float):
    """
    Set the default as a `NamedPoint`.

    **Parameters**

    * **`ipt`** - The input to set the default for.
    * **`str`** - A pointer to a string representing the name.
    * **`val`** - A double value for the value of the named point.
    """
    f = loadSym("helicsInputSetDefaultNamedPoint")
    err = helicsErrorInitialize()
    f(ipt, cstring(string), cdouble(val), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetType(ipt: HelicsInput) -> str:
    """
    Get the type of an input.

    **Parameters**

    * **`ipt`** - The input to query

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetType")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsInputGetPublicationType(ipt: HelicsInput) -> str:
    """
    Get the type the publisher to an input is sending.

    **Parameters**

    * **`ipt`** - The input to query

    **Returns**: A const char * with the type name.
    """
    f = loadSym("helicsInputGetPublicationType")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsPublicationGetType(pub: HelicsPublication) -> str:
    """
    Get the type of a publication.

    **Parameters**

    * **`pub`** - The publication to query

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsPublicationGetType")
    result = f(pub)
    return ffi.string(result).decode()


def helicsInputGetKey(ipt: HelicsInput) -> str:
    """
    Get the key of an input.

    **Parameters**

    * **`ipt`** - The input to query

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetKey")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsSubscriptionGetKey(ipt: HelicsInput) -> str:
    """
    Get the key of a subscription.

    **Returns**: A const char with the subscription key.
    """
    f = loadSym("helicsSubscriptionGetKey")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsPublicationGetKey(pub: HelicsPublication) -> str:
    """
    Get the key of a publication.
    This will be the global key used to identify the publication to the federation.

    **Parameters**

    * **`pub`** - The publication to query.

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsPublicationGetKey")
    result = f(pub)
    return ffi.string(result).decode()


def helicsInputGetUnits(ipt: HelicsInput) -> str:
    """
    Get the units of an input.

    **Parameters**

    * **`ipt`** - The input to query.

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetUnits")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsInputGetInjectionUnits(ipt: HelicsInput) -> str:
    """
    Get the units of the publication that an input is linked to.

    **Parameters**

    * **`ipt`** - The input to query.

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetInjectionUnits")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsInputGetExtractionUnits(ipt: HelicsInput) -> str:
    """
    Get the units of an input.
    The same as `helics.helicsInputGetUnits`.

    **Parameters**

    * **`ipt`** - The input to query.

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsInputGetExtractionUnits")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsPublicationGetUnits(pub: HelicsPublication) -> str:
    """
    Get the units of a publication.

    **Parameters**

    * **`pub`** - The publication to query.

    **Returns**: A void enumeration, helics_ok if everything worked.
    """
    f = loadSym("helicsPublicationGetUnits")
    result = f(pub)
    return ffi.string(result).decode()


def helicsInputGetInfo(ipt: HelicsInput) -> str:
    """
    Get the data in the info field of an input.

    **Parameters**

    * **`ipt`** - The input to query.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsInputGetInfo")
    result = f(ipt)
    return ffi.string(result).decode()


def helicsInputSetInfo(ipt: HelicsInput, info: str):
    """
    Set the data in the info field for an input.

    **Parameters**

    * **`ipt`** - The input to query.
    * **`info`** - The string to set.
    """
    f = loadSym("helicsInputSetInfo")
    err = helicsErrorInitialize()
    f(ipt, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetInfo(pub: HelicsPublication) -> str:
    """
    Get the data in the info field of an publication.

    **Parameters**

    * **`pub`** - The publication to query.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsPublicationGetInfo")
    result = f(pub)
    return ffi.string(result).decode()


def helicsPublicationSetInfo(pub: HelicsPublication, info: str):
    """
    Set the data in the info field for a publication.

    **Parameters**

    * **`pub`** - The publication to set the info field for.
    * **`info`** - The string to set.
    """
    f = loadSym("helicsPublicationSetInfo")
    err = helicsErrorInitialize()
    f(pub, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetOption(ipt: HelicsInput, option: HelicsHandleOption) -> int:
    """
    Get the current value of an input handle option.

    **Parameters**

    * **`ipt`** - The input to query.
    * **`option`** - Integer representation of the option in question see `helics.HelicsHandleOption`.

    **Returns**: An integer value with the current value of the given option.
    """
    f = loadSym("helicsInputGetOption")
    result = f(ipt, HelicsHandleOption(option))
    return result


def helicsInputSetOption(ipt: HelicsInput, option: HelicsHandleOption, value: int):
    """
    Set an option on an input.

    **Parameters**

    * **`ipt`** - The input to query.
    * **`option`** - The option to set for the input `helics.HelicsHandleOption`.
    * **`value`** - The value to set the option to.
    """
    f = loadSym("helicsInputSetOption")
    err = helicsErrorInitialize()
    f(ipt, HelicsHandleOption(option), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetOption(pub: HelicsPublication, option: HelicsHandleOption) -> int:
    """
    Get the value of an option for a publication.

    **Parameters**

    * **`pub`** - The publication to query.
    * **`option`** - The value to query see `helics.HelicsHandleOption`.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsPublicationGetOption")
    result = f(pub, HelicsHandleOption(option))
    return result


def helicsPublicationSetOption(pub: HelicsPublication, option: HelicsHandleOption, val: int):
    """
    Set the value of an option for a publication.

    **Parameters**

    * **`pub`** - The publication to query.
    * **`option`** - Integer code for the option to set `helics.HelicsHandleOption`.
    * **`val`** - The value to set the option to.
    """
    f = loadSym("helicsPublicationSetOption")
    err = helicsErrorInitialize()
    f(pub, HelicsHandleOption(option), val, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationSetMinimumChange(pub: HelicsPublication, tolerance: float):
    """
    Set the minimum change detection tolerance.

    **Parameters**

    * **`pub`** - The publication to modify.
    * **`tolerance`** - The tolerance level for publication, values changing less than this value will not be published.
    """
    f = loadSym("helicsPublicationSetMinimumChange")
    err = helicsErrorInitialize()
    f(pub, cdouble(tolerance), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetMinimumChange(ipt: HelicsInput, tolerance: float):
    """
    Set the minimum change detection tolerance.

    **Parameters**

    * **`ipt`** - The input to modify.
    * **`tolerance`** - The tolerance level for registering an update, values changing less than this value will not show asbeing updated.
    """
    f = loadSym("helicsInputSetMinimumChange")
    err = helicsErrorInitialize()
    f(ipt, cdouble(tolerance), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsUpdated(ipt: HelicsInput) -> bool:
    """
    Check if a particular subscription was updated.

    **Returns**: `True` if it has been updated since the last value retrieval.
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
    Get the number of publications in a federate.

    **Returns**: (-1) if fed was not a valid federate otherwise returns the number of publications.
    """
    f = loadSym("helicsFederateGetPublicationCount")
    result = f(fed)
    return result


def helicsFederateGetInputCount(fed: HelicsFederate) -> int:
    """
    Get the number of subscriptions in a federate.

    **Returns**: (-1) if fed was not a valid federate otherwise returns the number of subscriptions.
    """
    f = loadSym("helicsFederateGetInputCount")
    result = f(fed)
    return result


def helicsFederateSetLoggingCallback(fed: HelicsFederate, logger, userdata):
    """
    Set the logging callback for a `helics.HelicsFederate`

    Add a logging callback function for the C.
    The logging callback will be called when a message flows into a `helics.HelicsFederate` from the core or from a federate.

    # Parameters

    * **`fed`**: the `helics.HelicsFederate` that is created with `helics.helicsCreateValueFederate`, `helics.helicsCreateMessageFederate` or `helics.helicsCreateCombinationFederate`
    * **`logger`**: a callback with signature void(int, const char *, const char *, void *); the function arguments are loglevel, an identifier string, and a message string, and a pointer to user data
    * **`userdata`**: a pointer to user data that is passed to the function when executing
    """
    f = loadSym("helicsFederateSetLoggingCallback")
    err = helicsErrorInitialize()
    f(fed, logger, userdata, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
