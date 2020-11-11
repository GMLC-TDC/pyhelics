# -*- coding: utf-8 -*-
import logging
import warnings
import json

from enum import IntEnum, unique

try:
    from typing import List, Tuple, Union
except ImportError:
    pass

from . import _build

lib = _build.lib
ffi = _build.ffi

import signal
import sys


def signal_handler(sig, frame):
    helicsCloseLibrary()
    print("User pressed 'CTRL-C'. Exiting ...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

HELICS_TIME_ZERO = 0.0  # definition of time zero-the beginning of simulation
HELICS_TIME_EPSILON = 1.0e-9  # definition of the minimum time resolution
HELICS_TIME_INVALID = -1.785e39  # definition of an invalid time that has no meaning
HELICS_TIME_MAXTIME = 9223372036.854774

helics_time_zero = HELICS_TIME_ZERO
helics_time_epsilon = HELICS_TIME_EPSILON
helics_time_invalid = HELICS_TIME_INVALID
helics_time_maxtime = HELICS_TIME_MAXTIME

HelicsTime = float
pointer = int


@unique
class HelicsCoreType(IntEnum):
    """
    - **DEFAULT**      = 0
    - **TEST**         = 3
    - **INTERPROCESS** = 4
    - **IPC**          = 5
    - **TCP**          = 6
    - **UDP**          = 7
    - **NNG**          = 9
    - **ZMQ_TEST**     = 10
    - **TCP_SS**       = 11
    - **HTTP**         = 12
    - **WEBSOCKET**    = 14
    - **INPROC**       = 18
    - **NULL**         = 66
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

helics_core_type_default = HelicsCoreType.DEFAULT
helics_core_type_zmq = HelicsCoreType.ZMQ
helics_core_type_mpi = HelicsCoreType.MPI
helics_core_type_test = HelicsCoreType.TEST
helics_core_type_interprocess = HelicsCoreType.INTERPROCESS
helics_core_type_ipc = HelicsCoreType.IPC
helics_core_type_tcp = HelicsCoreType.TCP
helics_core_type_udp = HelicsCoreType.UDP
helics_core_type_zmq_test = HelicsCoreType.ZMQ_TEST
helics_core_type_nng = HelicsCoreType.NNG
helics_core_type_tcp_ss = HelicsCoreType.TCP_SS
helics_core_type_http = HelicsCoreType.HTTP
helics_core_type_websocket = HelicsCoreType.WEBSOCKET
helics_core_type_inproc = HelicsCoreType.INPROC
helics_core_type_null = HelicsCoreType.NULL


@unique
class HelicsDataType(IntEnum):
    """
    - **STRING**         = 0
    - **DOUBLE**         = 1
    - **INT**            = 2
    - **COMPLEX**        = 3
    - **VECTOR**         = 4
    - **COMPLEX_VECTOR** = 5
    - **NAMED_POINT**    = 6
    - **BOOLEAN**        = 7
    - **TIME**           = 8
    - **RAW**            = 25
    - **MULTI**          = 33
    - **ANY**            = 25262
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

helics_data_type_string = HelicsDataType.STRING
helics_data_type_double = HelicsDataType.DOUBLE
helics_data_type_int = HelicsDataType.INT
helics_data_type_complex = HelicsDataType.COMPLEX
helics_data_type_vector = HelicsDataType.VECTOR
helics_data_type_complex_vector = HelicsDataType.COMPLEX_VECTOR
helics_data_type_named_point = HelicsDataType.NAMED_POINT
helics_data_type_boolean = HelicsDataType.BOOLEAN
helics_data_type_time = HelicsDataType.TIME
helics_data_type_raw = HelicsDataType.RAW
helics_data_type_multi = HelicsDataType.MULTI
helics_data_type_any = HelicsDataType.ANY


@unique
class HelicsFederateFlag(IntEnum):
    """
    - **OBSERVER**                      = 0
    - **UNINTERRUPTIBLE**               = 1
    - **INTERRUPTIBLE**                 = 2
    - **SOURCE_ONLY**                   = 4
    - **ONLY_TRANSMIT_ON_CHANGE**       = 6
    - **ONLY_UPDATE_ON_CHANGE**         = 8
    - **WAIT_FOR_CURRENT_TIME_UPDATE**  = 10
    - **RESTRICTIVE_TIME_POLICY**       = 11
    - **REALTIME**                      = 16
    - **SLOW_RESPONDING**               = 29
    - **DELAY_INIT_ENTRY**              = 45
    - **ENABLE_INIT_ENTRY**             = 47
    - **IGNORE_TIME_MISMATCH_WARNINGS** = 67
    - **TERMINATE_ON_ERROR**            = 72
    """

    OBSERVER = 0  # HelicsFederateFlags
    UNINTERRUPTIBLE = 1  # HelicsFederateFlags
    INTERRUPTIBLE = 2  # HelicsFederateFlags
    SOURCE_ONLY = 4  # HelicsFederateFlags
    ONLY_TRANSMIT_ON_CHANGE = 6  # HelicsFederateFlags
    ONLY_UPDATE_ON_CHANGE = 8  # HelicsFederateFlags
    WAIT_FOR_CURRENT_TIME_UPDATE = 10  # HelicsFederateFlags
    RESTRICTIVE_TIME_POLICY = 11  # HelicsFederateFlags
    # ROLLBACK = 12  # HelicsFederateFlags
    # FORWARD_COMPUTE = 14  # HelicsFederateFlags
    REALTIME = 16  # HelicsFederateFlags
    # SINGLE_THREAD_FEDERATE = 27  # HelicsFederateFlags
    SLOW_RESPONDING = 29  # HelicsFederateFlags
    DELAY_INIT_ENTRY = 45  # HelicsFederateFlags
    ENABLE_INIT_ENTRY = 47  # HelicsFederateFlags
    IGNORE_TIME_MISMATCH_WARNINGS = 67  # HelicsFederateFlags
    TERMINATE_ON_ERROR = 72  # HelicsFederateFlags
    FORCE_LOGGING_FLUSH = 88  # HelicsFederateFlags
    DUMPLOG = 89  # HelicsFederateFlags


HELICS_FLAG_OBSERVER = HelicsFederateFlag.OBSERVER
HELICS_FLAG_UNINTERRUPTIBLE = HelicsFederateFlag.UNINTERRUPTIBLE
HELICS_FLAG_INTERRUPTIBLE = HelicsFederateFlag.INTERRUPTIBLE
HELICS_FLAG_SOURCE_ONLY = HelicsFederateFlag.SOURCE_ONLY
HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE = HelicsFederateFlag.ONLY_TRANSMIT_ON_CHANGE
HELICS_FLAG_ONLY_UPDATE_ON_CHANGE = HelicsFederateFlag.ONLY_UPDATE_ON_CHANGE
HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE = HelicsFederateFlag.WAIT_FOR_CURRENT_TIME_UPDATE
HELICS_FLAG_RESTRICTIVE_TIME_POLICY = HelicsFederateFlag.RESTRICTIVE_TIME_POLICY
# HELICS_FLAG_ROLLBACK = HelicsFederateFlag.ROLLBACK
# HELICS_FLAG_FORWARD_COMPUTE = HelicsFederateFlag.FORWARD_COMPUTE
HELICS_FLAG_REALTIME = HelicsFederateFlag.REALTIME
# HELICS_FLAG_SINGLE_THREAD_FEDERATE = HelicsFederateFlag.SINGLE_THREAD_FEDERATE
HELICS_FLAG_SLOW_RESPONDING = HelicsFederateFlag.SLOW_RESPONDING
HELICS_FLAG_DELAY_INIT_ENTRY = HelicsFederateFlag.DELAY_INIT_ENTRY
HELICS_FLAG_ENABLE_INIT_ENTRY = HelicsFederateFlag.ENABLE_INIT_ENTRY
HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS = HelicsFederateFlag.IGNORE_TIME_MISMATCH_WARNINGS
HELICS_FLAG_TERMINATE_ON_ERROR = HelicsFederateFlag.TERMINATE_ON_ERROR
HELICS_FLAG_FORCE_LOGGING_FLUSH = HelicsFederateFlag.FORCE_LOGGING_FLUSH
HELICS_FLAG_DUMPLOG = HelicsFederateFlag.DUMPLOG

helics_flag_observer = HelicsFederateFlag.OBSERVER
helics_flag_uninterruptible = HelicsFederateFlag.UNINTERRUPTIBLE
helics_flag_interruptible = HelicsFederateFlag.INTERRUPTIBLE
helics_flag_source_only = HelicsFederateFlag.SOURCE_ONLY
helics_flag_only_transmit_on_change = HelicsFederateFlag.ONLY_TRANSMIT_ON_CHANGE
helics_flag_only_update_on_change = HelicsFederateFlag.ONLY_UPDATE_ON_CHANGE
helics_flag_wait_for_current_time_update = HelicsFederateFlag.WAIT_FOR_CURRENT_TIME_UPDATE
helics_flag_restrictive_time_policy = HelicsFederateFlag.RESTRICTIVE_TIME_POLICY
# helics_flag_rollback = HelicsFederateFlag.ROLLBACK
# helics_flag_forward_compute = HelicsFederateFlag.FORWARD_COMPUTE
helics_flag_realtime = HelicsFederateFlag.REALTIME
# helics_flag_single_thread_federate = HelicsFederateFlag.SINGLE_THREAD_FEDERATE
helics_flag_slow_responding = HelicsFederateFlag.SLOW_RESPONDING
helics_flag_delay_init_entry = HelicsFederateFlag.DELAY_INIT_ENTRY
helics_flag_enable_init_entry = HelicsFederateFlag.ENABLE_INIT_ENTRY
helics_flag_ignore_time_mismatch_warnings = HelicsFederateFlag.IGNORE_TIME_MISMATCH_WARNINGS
helics_flag_terminate_on_error = HelicsFederateFlag.TERMINATE_ON_ERROR
helics_flag_force_logging_flush = HelicsFederateFlag.FORCE_LOGGING_FLUSH
helics_flag_dumplog = HelicsFederateFlag.DUMPLOG


@unique
class HelicsLogLevel(IntEnum):
    """
    - **NO_PRINT**    = -1
    - **ERROR**       = 0
    - **WARNING**     = 1
    - **SUMMARY**     = 2
    - **CONNECTIONS** = 3
    - **INTERFACES**  = 4
    - **TIMING**      = 5
    - **DATA**        = 6
    - **TRACE**       = 7
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

helics_log_level_no_print = HelicsLogLevel.NO_PRINT
helics_log_level_error = HelicsLogLevel.ERROR
helics_log_level_warning = HelicsLogLevel.WARNING
helics_log_level_summary = HelicsLogLevel.SUMMARY
helics_log_level_connections = HelicsLogLevel.CONNECTIONS
helics_log_level_interfaces = HelicsLogLevel.INTERFACES
helics_log_level_timing = HelicsLogLevel.TIMING
helics_log_level_data = HelicsLogLevel.DATA
helics_log_level_trace = HelicsLogLevel.TRACE


@unique
class HelicsError(IntEnum):
    """
    - **FATAL**                    = -404
    - **EXTERNAL_TYPE**            = -203
    - **OTHER**                    = -101
    - **INSUFFICIENT_SPACE**       = -18
    - **EXECUTION_FAILURE**        = -14
    - **INVALID_FUNCTION_CALL**    = -10
    - **INVALID_STATE_TRANSITION** = -9
    - **WARNING**                  = -8
    - **SYSTEM_FAILURE**           = -6
    - **DISCARD**                  = -5
    - **INVALID_ARGUMENT**         = -4
    - **INVALID_OBJECT**           = -3
    - **CONNECTION_FAILURE**       = -2
    - **REGISTRATION_FAILURE**     = -1
    - **OK**                       = 0
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

helics_error_fatal = HelicsError.FATAL
helics_error_external_type = HelicsError.EXTERNAL_TYPE
helics_error_other = HelicsError.OTHER
helics_error_insufficient_space = HelicsError.INSUFFICIENT_SPACE
helics_error_execution_failure = HelicsError.EXECUTION_FAILURE
helics_error_invalid_function_call = HelicsError.INVALID_FUNCTION_CALL
helics_error_invalid_state_transition = HelicsError.INVALID_STATE_TRANSITION
helics_warning = HelicsError.WARNING
helics_error_system_failure = HelicsError.SYSTEM_FAILURE
helics_error_discard = HelicsError.DISCARD
helics_error_invalid_argument = HelicsError.INVALID_ARGUMENT
helics_error_invalid_object = HelicsError.INVALID_OBJECT
helics_error_connection_failure = HelicsError.CONNECTION_FAILURE
helics_error_registration_failure = HelicsError.REGISTRATION_FAILURE
helics_ok = HelicsError.OK


@unique
class HelicsProperty(IntEnum):
    """
    - **TIME_DELTA**            = 137
    - **TIME_PERIOD**           = 140
    - **TIME_OFFSET**           = 141
    - **TIME_RT_LAG**           = 143
    - **TIME_RT_LEAD**          = 144
    - **TIME_RT_TOLERANCE**     = 145
    - **TIME_INPUT_DELAY**      = 148
    - **TIME_OUTPUT_DELAY**     = 150
    - **INT_MAX_ITERATIONS**    = 259
    - **INT_LOG_LEVEL**         = 271
    - **INT_FILE_LOG_LEVEL**    = 272
    - **INT_CONSOLE_LOG_LEVEL** = 274
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

helics_property_time_delta = HelicsProperty.TIME_DELTA
helics_property_time_period = HelicsProperty.TIME_PERIOD
helics_property_time_offset = HelicsProperty.TIME_OFFSET
helics_property_time_rt_lag = HelicsProperty.TIME_RT_LAG
helics_property_time_rt_lead = HelicsProperty.TIME_RT_LEAD
helics_property_time_rt_tolerance = HelicsProperty.TIME_RT_TOLERANCE
helics_property_time_input_delay = HelicsProperty.TIME_INPUT_DELAY
helics_property_time_output_delay = HelicsProperty.TIME_OUTPUT_DELAY
helics_property_int_max_iterations = HelicsProperty.INT_MAX_ITERATIONS
helics_property_int_log_level = HelicsProperty.INT_LOG_LEVEL
helics_property_int_file_log_level = HelicsProperty.INT_FILE_LOG_LEVEL
helics_property_int_console_log_level = HelicsProperty.INT_CONSOLE_LOG_LEVEL


@unique
class HelicsMultiInputMode(IntEnum):
    """
    - **NO_OP**               = 0
    - **VECTORIZE_OPERATION** = 1
    - **AND_OPERATION**       = 2
    - **OR_OPERATION**        = 3
    - **SUM_OPERATION**       = 4
    - **DIFF_OPERATION**      = 5
    - **MAX_OPERATION**       = 6
    - **MIN_OPERATION**       = 7
    - **AVERAGE_OPERATION**   = 8
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

helics_multi_input_no_op = HelicsMultiInputMode.NO_OP
helics_multi_input_vectorize_operation = HelicsMultiInputMode.VECTORIZE_OPERATION
helics_multi_input_and_operation = HelicsMultiInputMode.AND_OPERATION
helics_multi_input_or_operation = HelicsMultiInputMode.OR_OPERATION
helics_multi_input_sum_operation = HelicsMultiInputMode.SUM_OPERATION
helics_multi_input_diff_operation = HelicsMultiInputMode.DIFF_OPERATION
helics_multi_input_max_operation = HelicsMultiInputMode.MAX_OPERATION
helics_multi_input_min_operation = HelicsMultiInputMode.MIN_OPERATION
helics_multi_input_average_operation = HelicsMultiInputMode.AVERAGE_OPERATION


@unique
class HelicsHandleOption(IntEnum):
    """
    - **CONNECTION_REQUIRED**          = 397
    - **CONNECTION_OPTIONAL**          = 402
    - **SINGLE_CONNECTION_ONLY**       = 407
    - **MULTIPLE_CONNECTIONS_ALLOWED** = 409
    - **BUFFER_DATA**                  = 411
    - **STRICT_TYPE_CHECKING**         = 414
    - **IGNORE_UNIT_MISMATCH**         = 447
    - **ONLY_TRANSMIT_ON_CHANGE**      = 452
    - **ONLY_UPDATE_ON_CHANGE**        = 454
    - **IGNORE_INTERRUPTS**            = 475
    - **MULTI_INPUT_HANDLING_METHOD**  = 507
    - **INPUT_PRIORITY_LOCATION**      = 510
    - **CLEAR_PRIORITY_LIST**          = 512
    - **CONNECTIONS**                  = 522
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

helics_handle_option_connection_required = HelicsHandleOption.CONNECTION_REQUIRED
helics_handle_option_connection_optional = HelicsHandleOption.CONNECTION_OPTIONAL
helics_handle_option_single_connection_only = HelicsHandleOption.SINGLE_CONNECTION_ONLY
helics_handle_option_multiple_connections_allowed = HelicsHandleOption.MULTIPLE_CONNECTIONS_ALLOWED
helics_handle_option_buffer_data = HelicsHandleOption.BUFFER_DATA
helics_handle_option_strict_type_checking = HelicsHandleOption.STRICT_TYPE_CHECKING
helics_handle_option_ignore_unit_mismatch = HelicsHandleOption.IGNORE_UNIT_MISMATCH
helics_handle_option_only_transmit_on_change = HelicsHandleOption.ONLY_TRANSMIT_ON_CHANGE
helics_handle_option_only_update_on_change = HelicsHandleOption.ONLY_UPDATE_ON_CHANGE
helics_handle_option_ignore_interrupts = HelicsHandleOption.IGNORE_INTERRUPTS
helics_handle_option_multi_input_handling_method = HelicsHandleOption.MULTI_INPUT_HANDLING_METHOD
helics_handle_option_input_priority_location = HelicsHandleOption.INPUT_PRIORITY_LOCATION
helics_handle_option_clear_priority_list = HelicsHandleOption.CLEAR_PRIORITY_LIST
helics_handle_option_connections = HelicsHandleOption.CONNECTIONS


@unique
class HelicsFilterType(IntEnum):
    """
    - **CUSTOM**       = 0
    - **DELAY**        = 1
    - **RANDOM_DELAY** = 2
    - **RANDOM_DROP**  = 3
    - **REROUTE**      = 4
    - **CLONE**        = 5
    - **FIREWALL**     = 6
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

helics_filter_type_custom = HelicsFilterType.CUSTOM
helics_filter_type_delay = HelicsFilterType.DELAY
helics_filter_type_random_delay = HelicsFilterType.RANDOM_DELAY
helics_filter_type_random_drop = HelicsFilterType.RANDOM_DROP
helics_filter_type_reroute = HelicsFilterType.REROUTE
helics_filter_type_clone = HelicsFilterType.CLONE
helics_filter_type_firewall = HelicsFilterType.FIREWALL


@unique
class HelicsIterationRequest(IntEnum):
    """
    - **NO_ITERATION**      = 0
    - **FORCE_ITERATION**   = 1
    - **ITERATE_IF_NEEDED** = 2
    """

    NO_ITERATION = 0  # HelicsIterationRequest
    FORCE_ITERATION = 1  # HelicsIterationRequest
    ITERATE_IF_NEEDED = 2  # HelicsIterationRequest


HELICS_ITERATION_REQUEST_NO_ITERATION = HelicsIterationRequest.NO_ITERATION
HELICS_ITERATION_REQUEST_FORCE_ITERATION = HelicsIterationRequest.FORCE_ITERATION
HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED = HelicsIterationRequest.ITERATE_IF_NEEDED

helics_iteration_request_no_iteration = HelicsIterationRequest.NO_ITERATION
helics_iteration_request_force_iteration = HelicsIterationRequest.FORCE_ITERATION
helics_iteration_request_iterate_if_needed = HelicsIterationRequest.ITERATE_IF_NEEDED


@unique
class HelicsIterationResult(IntEnum):
    """
    - **NEXT_STEP** = 0
    - **ERROR**     = 1
    - **HALTED**    = 2
    - **ITERATING** = 3
    """

    NEXT_STEP = 0  # HelicsIterationResult
    ERROR = 1  # HelicsIterationResult
    HALTED = 2  # HelicsIterationResult
    ITERATING = 3  # HelicsIterationResult


HELICS_ITERATION_RESULT_NEXT_STEP = HelicsIterationResult.NEXT_STEP
HELICS_ITERATION_RESULT_ERROR = HelicsIterationResult.ERROR
HELICS_ITERATION_RESULT_HALTED = HelicsIterationResult.HALTED
HELICS_ITERATION_RESULT_ITERATING = HelicsIterationResult.ITERATING

helics_iteration_result_next_step = HelicsIterationResult.NEXT_STEP
helics_iteration_result_error = HelicsIterationResult.ERROR
helics_iteration_result_halted = HelicsIterationResult.HALTED
helics_iteration_result_iterating = HelicsIterationResult.ITERATING


@unique
class HelicsFederateState(IntEnum):
    """
    - **STARTUP**                = 0
    - **INITIALIZATION**         = 1
    - **EXECUTION**              = 2
    - **FINALIZE**               = 3
    - **ERROR**                  = 4
    - **PENDING_INIT**           = 5
    - **PENDING_EXEC**           = 6
    - **PENDING_TIME**           = 7
    - **PENDING_ITERATIVE_TIME** = 8
    - **PENDING_FINALIZE**       = 9
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

helics_state_startup = HelicsFederateState.STARTUP
helics_state_initialization = HelicsFederateState.INITIALIZATION
helics_state_execution = HelicsFederateState.EXECUTION
helics_state_finalize = HelicsFederateState.FINALIZE
helics_state_error = HelicsFederateState.ERROR
helics_state_pending_init = HelicsFederateState.PENDING_INIT
helics_state_pending_exec = HelicsFederateState.PENDING_EXEC
helics_state_pending_time = HelicsFederateState.PENDING_TIME
helics_state_pending_iterative_time = HelicsFederateState.PENDING_ITERATIVE_TIME
helics_state_pending_finalize = HelicsFederateState.PENDING_FINALIZE


class _HelicsCHandle:
    def __init__(self, handle):
        self.handle = handle


class _FilterOptionAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        if type(index) == str:
            idx = helicsGetOptionIndex(index)
        else:
            idx = HelicsHandleOption(index)
        return helicsFilterGetOption(self, idx)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = helicsGetOptionIndex(index)
        else:
            idx = HelicsHandleOption(index)
        return helicsFilterSetOption(self, idx, value)

    def __repr__(self):
        lst = []
        for o in HelicsHandleOption:
            lst.append("'{}' = {}".format(o.name, self[o]))
        return "<{{ {} }}>".format(", ".join(lst))

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class HelicsFilter(_HelicsCHandle):
    def __init__(self, handle):
        super(HelicsFilter, self).__init__(handle)
        self.option = _FilterOptionAccessor(self.handle)

    def __repr__(self):
        name = self.name
        info = self.info
        return """<helics.{class_name}(name = "{name}", info = "{info}") at {id}>""".format(
            class_name=self.__class__.__name__, name=name, info=info, id=hex(id(self))
        )

    def add_destination_target(self, destination: str):
        """
        Add a destination target to a cloning filter.
        All messages going to a destination are copied to the delivery address(es).
        """
        helicsFilterAddDestinationTarget(self, destination)

    def add_source_target(self, source: str):
        """
        Add a source target to a cloning filter.
        All messages coming from a source are copied to the delivery address(es).
        """
        helicsFilterAddSourceTarget(self, source)

    def remove_destination_target(self, destination: str):
        """remove a destination target from a cloning filter."""
        helicsFilterRemoveTarget(self, destination)

    def add_delivery_endpoint(self, delivery_endpoint: str):
        """
        Add a delivery destination from a filter.

        **Parameters**

        - **`delivery_endpoint`** - A string with the delivery endpoint to add.
        """
        helicsFilterAddDeliveryEndpoint(self, delivery_endpoint)

    def remove_delivery_endpoint(self, delivery_endpoint: str):
        """
        Remove a delivery destination from a filter.

        **Parameters**

        - **`delivery_endpoint`** - A string with the delivery endpoint to remove.
        """
        helicsFilterRemoveDeliveryEndpoint(self, delivery_endpoint)

    @property
    def name(self) -> str:
        return helicsFilterGetName(self)

    @property
    def info(self) -> str:
        """Get the interface information field of the filter."""
        return helicsFilterGetInfo(self)

    @info.setter
    def info(self, info: str):
        """Set the interface information field of the filter."""
        helicsFilterSetInfo(self, info)

    def set(self, property: str, value: float):
        """Set a property on a filter."""
        helicsFilterSet(self, property, value)


class HelicsCloningFilter(HelicsFilter):
    pass


class HelicsCore(_HelicsCHandle):
    def __repr__(self):
        identifier = self.identifier
        address = self.address
        return """<helics.{class_name}(identifier = "{identifier}", address = "{address}") at {id}>""".format(
            class_name=self.__class__.__name__, identifier=identifier, address=address, id=hex(id(self)),
        )

    def __del__(self):
        helicsCoreFree(self)

    @property
    def identifier(self) -> str:
        """Get an identifier string for the core."""
        return helicsCoreGetIdentifier(self)

    @property
    def address(self) -> str:
        """Get the connection network or connection address for the core."""
        return helicsCoreGetAddress(self)

    def is_valid(self) -> bool:
        """Check if the core is valid."""
        return helicsCoreIsValid(self)

    def is_connected(self) -> bool:
        """Check if the core is connected to the broker."""
        return helicsCoreIsConnected(self)

    def clone(self):
        return helicsCoreClone(self)

    def set_ready_to_init(self):
        """Set the core to ready to enter init.

        This function only needs to be called for cores that don't have any federates but may have filters for cores with federates it won't do anything.
        """
        helicsCoreSetReadyToInit(self)

    def disconnect(self):
        """
        Disconnect the core from its broker.
        """
        helicsCoreDisconnect(self)

    def wait_for_disconnect(self, ms_to_wait: int = -1) -> bool:
        """Waits in the current thread until the broker is disconnected

        **Parameters**

        **`ms_to_wait`**:  the timeout to wait for disconnect (-1) implies no timeout

        Returns: true if the disconnect was successful false if it timed out.
        """
        return helicsCoreWaitForDisconnect(self, ms_to_wait)

    def register_filter(self, kind: HelicsFilterType, name: str = "") -> HelicsFilter:
        """
        Create a destination Filter on the specified federate.

        Filters can be created through a federate or a core , linking through a federate allows
        a few extra features of name matching to function on the federate interface but otherwise
        equivalent behavior

        **`kind`**: the type of filter to create
        **`name`**: the name of the filter (can be NULL)

        Returns: a `helics.HelicsFilter` object.
        """
        return helicsCoreRegisterFilter(self, kind, name)

    def register_cloning_filter(self, delivery_endpoint: str) -> HelicsCloningFilter:
        """
        Create a cloning Filter on the specified federate.

        Cloning filters copy a message and send it to multiple locations source and destination can be added through other functions

        **Parameters**

        **`delivery_endpoint`**: the specified endpoint to deliver the message

        Returns: a `helics.HelicsFilter` object.
        """
        return helicsCoreRegisterCloningFilter(self, delivery_endpoint)

    def set_global(self, name: str, value: str):
        """
        Set a global federation value.

        **Parameters**

        **`name`**: the name of the global value to set
        **`value`**: actual value of the global variable
        """
        helicsCoreSetGlobal(self, name, value)

    def query(self, target: str, query: str) -> str:
        """
        Make a query of the core.

        This call is blocking until the value is returned which may take some time depending
        on the size of the federation and the specific string being queried

        **`target`**:  the target of the query can be "federation", "federate", "broker", "core", or a specific name of a federate, core, or broker
        **`query`**: a string with the query, see other documentation for specific properties to query, can be defined by the federate

        Returns: a string with the value requested.  this is either going to be a vector of strings value
        or a JSON string stored in the first element of the vector.  The string "#invalid" is returned
        if the query was not valid
        """
        q = helicsCreateQuery(target, query)
        result = helicsQueryCoreExecute(q, self)
        helicsQueryFree(q)
        return result


class HelicsBroker(_HelicsCHandle):
    def __repr__(self):
        identifier = self.identifier
        address = self.address
        return """<helics.{class_name}(identifier = "{identifier}", address = "{address}") at {id}>""".format(
            class_name=self.__class__.__name__, identifier=identifier, address=address, id=hex(id(self)),
        )

    def __del__(self):
        helicsBrokerFree(self)

    def is_connected(self):
        """Check if the broker is connected."""
        return helicsBrokerIsConnected(self) is True

    def wait_for_disconnect(self, ms_to_wait: int = -1):
        """
        Waits in the current thread until the broker is disconnected.

        **Parameters**

        - **`ms_to_wait`**: the timeout to wait for disconnect (-1) implies no timeout

        Returns: `True` if the disconnect was successful false if it timed out
        """
        return helicsBrokerWaitForDisconnect(self, ms_to_wait)

    def disconnect(self):
        """
        Disconnect the broker from any other brokers and communications.
        """
        return helicsBrokerDisconnect(self)

    @property
    def identifier(self):
        """
        Get the local identification for the broker.
        """
        return helicsBrokerGetIdentifier(self)

    @property
    def address(self):
        """
        Get the connection address for the broker.
        """
        return helicsBrokerGetAddress(self)

    def set_global(self, name: str, value: str):
        """
        Set a federation global value.

        This overwrites any previous value for this name. globals can be queried with a target of "global" and query of the value to Query.

        **Parameters**

        - **`name`**: the name of the global to set.
        - **`value`**: the value of the global.
        """
        helicsBrokerSetGlobal(self, name, value)

    def data_link(self, source: str, target: str):
        """
        Create a data link between a named publication and a named input.

        **Parameters**

        - **`source`**: the name of the publication.
        - **`target`**: the name of the input.
        """
        helicsBrokerDataLink(self, source, target)

    def add_source_filter_to_endpoint(self, filter: str, target: str):
        """
        Create a filter connection between a named filter and a named endpoint for messages coming from that endpoint.

        **Parameters**

        **`filter`**: the name of the filter.
        **`target`**: the name of the source target.
        """
        helicsBrokerAddSourceFilterToEndpoint(self, filter, target)

    def add_destination_filter_to_endpoint(self, filter: str, target: str):
        """
        Create a filter connection between a named filter and a named endpoint for destination processing.

        **Parameters**

        - **`filter`**: the name of the filter.
        - **`target`**: the name of the source target.
        """
        helicsBrokerAddDestinationFilterToEndpoint(self, filter, target)

    def query(self, target: str, query: str) -> str:
        """
        Make a query of the broker.

        This call is blocking until the value is returned which may take some time depending on the size of the federation and the specific string being queried.

        **Parameters**

        - **`target`**:  the target of the query can be "federation", "federate", "broker", "core", or a specific name of a federate, core, or broker.
        - **`query`**: a string with the query, see other documentation for specific properties to query, can be defined by the federate.

        Returns: a string with the value requested. This is either going to be a vector of strings value or a JSON string stored in the first element of the vector. The string "#invalid" is returned if the query was not valid.
        """
        q = helicsCreateQuery(target, query)
        result = helicsQueryBrokerExecute(q, self)
        helicsQueryFree(q)
        return result


class _MessageFlagAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        return helicsMessageCheckFlag(self, index)

    def __setitem__(self, index: int, value: bool):
        return helicsMessageSetFlagOption(self, index, value)

    def __repr__(self):
        lst = []
        for f in range(1, 16):
            try:
                lst.append("{} = {}".format(f, self[f]))
            except Exception:
                pass
        return "<{{ {} }}>".format(", ".join(lst))

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class HelicsMessage(_HelicsCHandle):
    def __init__(self, handle):
        super(HelicsMessage, self).__init__(handle)
        self.flag = _MessageFlagAccessor(self.handle)

    def __repr__(self):
        source = self.source
        destination = self.destination
        original_source = self.original_source
        original_destination = self.original_destination
        time = self.time
        message_id = self.message_id
        message = self.data
        return """<helics.{class_name}(source = "{source}", destination = "{destination}", original_source = "{original_source}", original_destination = "{original_destination}", time = {time}, id = {message_id}, message = "{message}") at {id}>""".format(
            class_name=self.__class__.__name__,
            source=source,
            destination=destination,
            original_source=original_source,
            original_destination=original_destination,
            time=time,
            message_id=message_id,
            message=message,
            id=hex(id(self)),
        )

    def append(self, data: bytes):
        helicsMessageAppendData(self, data)

    def is_valid(self) -> bool:
        return helicsMessageIsValid(self)

    @property
    def source(self):
        return helicsMessageGetSource(self)

    @source.setter
    def source(self, v):
        return helicsMessageSetSource(self, v)

    @property
    def destination(self):
        return helicsMessageGetDestination(self)

    @destination.setter
    def destination(self, v):
        return helicsMessageSetDestination(self, v)

    @property
    def original_source(self):
        return helicsMessageGetOriginalSource(self)

    @original_source.setter
    def original_source(self, v):
        return helicsMessageSetOriginalSource(self, v)

    @property
    def original_dest(self):
        warnings.warn("This is deprecated. Use `original_destination` instead.")
        return self.original_destination

    @original_dest.setter
    def original_dest(self, v):
        warnings.warn("This is deprecated. Use `original_destination` instead.")
        self.original_destination = v

    @property
    def original_destination(self):
        return helicsMessageGetOriginalDestination(self)

    @original_destination.setter
    def original_destination(self, v):
        return helicsMessageSetOriginalDestination(self, v)

    @property
    def time(self):
        return helicsMessageGetTime(self)

    @time.setter
    def time(self, v):
        return helicsMessageSetTime(self, v)

    @property
    def data(self):
        return helicsMessageGetString(self)

    @data.setter
    def data(self, v: str):
        return helicsMessageSetString(self, v)

    @property
    def raw_data(self) -> bytes:
        return helicsMessageGetRawData(self)

    @raw_data.setter
    def raw_data(self, v: bytes):
        return helicsMessageSetData(self, v)

    @property
    def message_id(self):
        return helicsMessageGetMessageID(self)

    @message_id.setter
    def message_id(self, v):
        return helicsMessageSetMessageID(self, v)


class HelicsQuery(_HelicsCHandle):
    pass


class HelicsEndpoint(_HelicsCHandle):
    def __repr__(self):
        name = self.name
        type = self.type
        info = self.info
        is_valid = self.is_valid()
        default_destination = self.default_destination
        n_pending_messages = self.n_pending_messages
        return """<helics.{class_name}(name = "{name}", type = "{type}", info = "{info}", is_valid = {is_valid}, default_destination = "{default_destination}", n_pending_messages = {n_pending_messages}) at {id}>""".format(
            class_name=self.__class__.__name__,
            name=name,
            type=type,
            info=info,
            is_valid=is_valid,
            default_destination=default_destination,
            n_pending_messages=n_pending_messages,
            id=hex(id(self)),
        )

    @property
    def default_destination(self) -> str:
        """Get the default destination for an endpoint."""
        return helicsEndpointGetDefaultDestination(self)

    @default_destination.setter
    def default_destination(self, destination: str):
        """set the default destination for an endpoint."""
        helicsEndpointSetDefaultDestination(self, destination)

    @property
    def n_pending_messages(self) -> int:
        """Returns the number of pending receives for endpoint."""
        return helicsEndpointPendingMessages(self)

    @property
    def name(self) -> str:
        """Get the name of the endpoint."""
        return helicsEndpointGetName(self)

    @property
    def type(self) -> str:
        """Get the specified type of the endpoint."""
        return helicsEndpointGetType(self)

    @property
    def info(self) -> str:
        """Get the interface information field of the filter."""
        return helicsEndpointGetInfo(self)

    @info.setter
    def info(self, info: str):
        """Set the interface information field of the filter."""
        helicsEndpointSetInfo(self, info)

    def is_valid(self) -> bool:
        """Check if the input is valid."""
        return helicsEndpointIsValid(self)

    def has_message(self) -> bool:
        """Checks if endpoint has unread messages."""
        return helicsEndpointHasMessage(self)

    def get_message(self) -> HelicsMessage:
        """Get a packet from an endpoint."""
        return helicsEndpointGetMessage(self)

    def create_message(self) -> HelicsMessage:
        """Create a message object."""
        return helicsEndpointCreateMessage(self)

    def send_data(self, data: Union[bytes, HelicsMessage], destination: str = None, time=None):
        if type(data) == HelicsMessage:
            helicsEndpointSendMessage(self, data)
        elif time is None:
            helicsEndpointSendBytesTo(self, data, destination)
        else:
            helicsEndpointSendBytesToAt(self, data, destination, time)


class _FederateInfoFlagAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        raise AttributeError("Unable to get {index}".format(index=index))

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = helicsGetFlagIndex(index)
        else:
            idx = HelicsFederateFlag(index)
        return helicsFederateInfoSetFlagOption(self, idx, value)

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class _FederateInfoPropertyAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        raise AttributeError("Unable to get {index}".format(index=index))

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = helicsGetPropertyIndex(index)
        else:
            idx = HelicsProperty(index)
        if "TIME_" in idx.name:
            return helicsFederateInfoSetTimeProperty(self, idx, value)
        elif "INT_" in idx.name:
            return helicsFederateInfoSetIntegerProperty(self, index, value)

    def __repr__(self):
        lst = []
        for p in HelicsProperty:
            lst.append("'{}' = {}".format(p.name, self[p]))
        return "<{{ {} }}>".format(", ".join(lst))

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class HelicsFederateInfo(_HelicsCHandle):
    def __init__(self, handle):
        # Python2 compatible super
        super(HelicsFederateInfo, self).__init__(handle)

        self.property = _FederateInfoPropertyAccessor(self.handle)
        self.flag = _FederateInfoFlagAccessor(self.handle)

    def __repr__(self):
        return """<helics.{class_name}() at {id}>""".format(class_name=self.__class__.__name__, id=hex(id(self)),)

    @property
    def core_name(self):
        raise AttributeError("Unreadable attribute `core_name`")

    @core_name.setter
    def core_name(self, core_name: str):
        helicsFederateInfoSetCoreName(self, core_name)

    @property
    def separator(self):
        raise AttributeError("Unreadable attribute `separator`")

    @separator.setter
    def separator(self, separator: str):
        """
        Specify a separator to use for naming separation between the federate name and the interface name.

        `self.separator = '.'` will result in future registrations of local endpoints such as `"fedName.endpoint"`.
        `self.separator = '/'` will result in `"fedName/endpoint"`.

        The default is `'/'`.
        Any character can be used though many will not make that much sense.
        This call is not thread safe and should be called before any local interfaces are created otherwise it may not be possible to retrieve them without using the full name.
        Recommended: ['/', '.', ':', '-', '_']
        """
        helicsFederateInfoSetSeparator(self, separator)

    @property
    def core_init(self):
        raise AttributeError("Unreadable attribute `core_init`")

    @core_init.setter
    def core_init(self, core_init: str):
        """
        Set the core init string to use in the FederateInfo.

        **`core_init`**: core init string to use.
        """
        helicsFederateInfoSetCoreInitString(self, core_init)

    @property
    def broker_init(self):
        raise AttributeError("Unreadable attribute `broker_init`")

    @broker_init.setter
    def broker_init(self, broker_init: str):
        """Set a string for the broker initialization in command line argument format."""
        helicsFederateInfoSetBrokerInitString(self, broker_init)

    @property
    def core_type(self):
        raise AttributeError("Unreadable attribute `broker_init`")

    @core_type.setter
    def core_type(self, core_type):
        """
        Set the core type with the core type.

        **`coretype`**: A core type.
        """
        if type(core_type) == str:
            helicsFederateInfoSetCoreTypeFromString(self, core_type)
        else:
            helicsFederateInfoSetCoreType(self, HelicsCoreType(core_type))

    @property
    def broker(self):
        raise AttributeError("Unreadable attribute `broker`.")

    @broker.setter
    def broker(self, broker: str):
        """
        Set the broker to connect with.

        **`broker`**: a string with the broker connection information or name.
        """
        helicsFederateInfoSetBroker(self, broker)

    @property
    def broker_key(self):
        raise AttributeError("Unreadable attribute `broker_key`.")

    @broker_key.setter
    def broker_key(self, broker_key):
        """Set the broker key to use.

        **`broker_key`**: a string with the broker key information
        """
        helicsFederateInfoSetBrokerKey(self, broker_key)

    @property
    def local_port(self):
        raise AttributeError("Unreadable attribute `local_port`.")

    @local_port.setter
    def local_port(self, broker_port: int):
        helicsFederateInfoSetLocalPort(self, broker_port)

    @property
    def broker_port(self):
        raise AttributeError("Unreadable attribute `broker_port`.")

    @broker_port.setter
    def broker_port(self, broker_port: int):
        helicsFederateInfoSetBrokerPort(self, broker_port)


class _PublicationOptionAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        if type(index) == str:
            idx = helicsGetOptionIndex(index)
        else:
            idx = HelicsHandleOption(index)
        return helicsPublicationGetOption(self, idx)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = helicsGetOptionIndex(index)
        else:
            idx = HelicsHandleOption(index)
        return helicsPublicationSetOption(self, idx, value)

    def __repr__(self):
        lst = []
        for o in HelicsHandleOption:
            lst.append("'{}' = {}".format(o.name, self[o]))
        return "<{{ {} }}>".format(", ".join(lst))

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class _FederateFlagAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        if type(index) == str:
            idx = helicsGetFlagIndex(index)
        else:
            idx = HelicsFederateFlag(index)
        return helicsFederateGetFlagOption(self, idx)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = helicsGetFlagIndex(index)
        else:
            idx = HelicsFederateFlag(index)
        return helicsFederateSetFlagOption(self, idx, value)

    def __repr__(self):
        lst = []
        for f in HelicsFederateFlag:
            # TODO: remove this try except
            # See https://github.com/GMLC-TDC/HELICS/issues/1549
            try:
                lst.append("'{}' = {}".format(f.name, self[f]))
            except Exception:
                pass
        return "<{{ {} }}>".format(", ".join(lst))

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class _FederatePropertyAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        if type(index) == str:
            idx = helicsGetPropertyIndex(index)
        else:
            idx = HelicsProperty(index)
        if "TIME_" in idx.name:
            return helicsFederateGetTimeProperty(self, idx)
        elif "INT_" in idx.name:
            return helicsFederateGetIntegerProperty(self, idx)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = helicsGetPropertyIndex(index)
        else:
            idx = HelicsProperty(index)
        if "TIME_" in idx.name:
            return helicsFederateSetTimeProperty(self, idx, value)
        elif "INT_" in idx.name:
            return helicsFederateSetIntegerProperty(self, index, value)

    def __repr__(self):
        lst = []
        for p in HelicsProperty:
            lst.append("'{}' = {}".format(p.name, self[p]))
        return "<{{ {} }}>".format(", ".join(lst))

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class HelicsFederate(_HelicsCHandle):
    def __init__(self, handle):
        # Python2 compatible super
        super(HelicsFederate, self).__init__(handle)

        self._exec_async_iterate = False
        self.property = _FederatePropertyAccessor(self.handle)
        self.flag = _FederateFlagAccessor(self.handle)
        self._separator = "/"

        self.publications = {}
        self.subscriptions = {}
        self.endpoints = {}
        self.filters = {}

    def __repr__(self):
        name = self.name
        state = str(self.state)
        current_time = self.current_time
        n_publications = self.n_publications
        n_endpoints = self.n_endpoints
        n_filters = self.n_filters
        n_subscriptions = self.n_inputs
        n_pending_messages = self.n_pending_messages
        return """<helics.{class_name}(name = "{name}", state = {state}, current_time = {current_time}, n_publications = {n_publications}, n_subscriptions = {n_subscriptions}, n_endpoints = {n_endpoints}, n_filters = {n_filters}, n_pending_messages = {n_pending_messages}) at {id}>""".format(
            class_name=self.__class__.__name__,
            name=name,
            state=state,
            current_time=current_time,
            n_publications=n_publications,
            n_endpoints=n_endpoints,
            n_filters=n_filters,
            n_subscriptions=n_subscriptions,
            n_pending_messages=n_pending_messages,
            id=hex(id(self)),
        )

    def __del__(self):
        helicsFederateFree(self)

    @property
    def name(self) -> str:
        return helicsFederateGetName(self)

    @property
    def state(self) -> HelicsFederateState:
        return helicsFederateGetState(self)

    @property
    def current_time(self) -> HelicsTime:
        return helicsFederateGetCurrentTime(self)

    @property
    def core(self) -> HelicsCore:
        return helicsFederateGetCoreObject(self)

    @property
    def n_publications(self) -> int:
        return helicsFederateGetPublicationCount(self)

    @property
    def n_endpoints(self) -> int:
        return helicsFederateGetEndpointCount(self)

    @property
    def n_filters(self) -> int:
        return helicsFederateGetFilterCount(self)

    @property
    def n_inputs(self) -> int:
        return helicsFederateGetInputCount(self)

    @property
    def n_pending_messages(self):
        """Returns the number of pending receives for all endpoints."""
        return helicsFederatePendingMessages(self)

    @property
    def separator(self):
        return self._separator

    @separator.setter
    def separator(self, separator: str):
        """
        Specify a separator to use for naming separation between the federate name and the interface name.

        `self.separator = '.'` will result in future registrations of local endpoints such as `"fedName.endpoint"`.
        `self.separator = '/'` will result in `"fedName/endpoint"`.

        The default is `'/'`.
        Any character can be used though many will not make that much sense.
        This call is not thread safe and should be called before any local interfaces are created otherwise it may not be possible to retrieve them without using the full name.
        Recommended: ['/', '.', ':', '-', '_']

        **Parameters**

        - **separator**: str to use as separator.
        """
        helicsFederateSetSeparator(self, separator)
        self._separator = separator

    def register_interfaces(self, config):
        """
        Register a set of interfaces defined in a file.

        Call is only valid in startup mode

        **Parameters**

        - **`configString`**: the location of the file or config String to load to generate the interfaces
        """
        helicsFederateRegisterInterfaces(self, config)

    def enter_initializing_mode(self):
        """
        Enter the initialization mode after all interfaces have been defined.

        The call will block until all federates have entered initialization mode.
        """
        helicsFederateEnterInitializingMode(self)

    def enter_initializing_mode_async(self):
        """
        Enter the initialization mode after all interfaces have been defined.

        The call will not block but a call to `enter_initializing_mode_complete` should be made to complete the call sequence.
        """
        helicsFederateEnterInitializingModeAsync(self)

    def is_async_operation_completed(self):
        """
        Called after one of the async calls and will indicate true if an async operation has completed.
        Only call from the same thread as the one that called the initial async call and will return false if called when no aysnc operation is in flight
        """
        return helicsFederateIsAsyncOperationCompleted(self)

    def enter_initializing_mode_complete(self):
        """
        Second part of the async process for entering initializationState call after a call to `enter_initializing_mode_async` if call any other time it will throw an `InvalidFunctionCall` exception
        """
        helicsFederateEnterInitializingModeComplete(self)

    def enter_executing_mode(self, iterate: HelicsIterationRequest = HelicsIterationRequest.NO_ITERATION):
        """
        Enter the normal execution mode.

        Call will block until all federates have entered this mode.

        **Parameters**

        - **`iterate`**: An optional flag indicating the desired iteration mode.
        """
        iterate = HelicsIterationRequest(iterate)
        if iterate == HelicsIterationRequest.NO_ITERATION:
            helicsFederateEnterExecutingMode(self)
            out_iterate = HelicsIterationResult.NEXT_STEP
        else:
            out_iterate = helicsFederateEnterExecutingModeIterative(self, iterate)
        return out_iterate

    def enter_executing_mode_async(self, iterate: HelicsIterationRequest = HelicsIterationRequest.NO_ITERATION):
        """
        Enter the normal execution mode.

        Call will return immediately but `enter_executing_mode_complete` should be called to complete the operation.

        **Parameters**

        - **`iterate`**: An optional flag indicating the desired iteration mode.
        """
        iterate = HelicsIterationRequest(iterate)
        if iterate == HelicsIterationRequest.NO_ITERATION:
            helicsFederateEnterExecutingModeAsync(self)
            self._exec_async_iterate = False
        else:
            helicsFederateEnterExecutingModeIterativeAsync(self, iterate)
            self._exec_async_iterate = True

    def enter_executing_mode_complete(self):
        """
        Complete the async call for entering Execution state.

        Call will not block but will return quickly.
        The `enter_initializing_mode_complete` must be called before doing other operations.
        """
        out_iterate = HelicsIterationResult.NEXT_STEP
        if self._exec_async_iterate:
            out_iterate = helicsFederateEnterExecutingModeIterativeComplete(self)
        else:
            helicsFederateEnterExecutingModeComplete(self)
        return out_iterate

    def finalize(self):
        """
        Terminate the simulation.

        Call is will block until the finalize has been acknowledged, no commands that interact with the core may be called after this function function.
        """
        helicsFederateFinalize(self)

    def finalize_async(self):
        """
        Terminate the simulation in a non-blocking call.
        `self.finalize_complete()` must be called after this call to complete the finalize procedure.
        """
        helicsFederateFinalizeAsync(self)

    def finalize_complete(self):
        """
        Complete the asynchronous terminate pair.
        """
        helicsFederateFinalizeComplete(self)

    def request_time(self, time: HelicsTime) -> HelicsTime:
        """
        **Parameters**

        - **`time`**: the next requested time step.

        Returns: The granted time step.
        """
        return helicsFederateRequestTime(self, time)

    def request_next_step(self) -> HelicsTime:
        """
        Request a time advancement to the next allowed time.

        Returns: The granted time step.
        """
        return helicsFederateRequestNextStep(self)

    def request_time_advance(self, time_delta: HelicsTime) -> HelicsTime:
        """
        Request a time advancement to the next allowed time.

        **Parameters**

        - **`timeDelta`**: The amount of time requested to advance.

        Returns: The granted time step.
        """
        return helicsFederateRequestTimeAdvance(self, time_delta)

    def request_time_iterative(self, time: float, iterate: HelicsIterationRequest) -> Tuple[HelicsTime, HelicsIterationResult]:
        """
        Request a time advancement.

        **Parameters**

        - **`time`**: the next requested time step.
        - **`iterate`**: a requested iteration mode.

        Returns: The granted time step in a structure containing a return time and an iteration_result.
        """
        grantedTime, status = helicsFederateRequestTimeIterative(self, time, iterate)
        return grantedTime, status

    def request_time_async(self, time: HelicsTime):
        """
        Request a time advancement and return immediately for asynchronous function.
        `self.request_time_complete()` should be called to finish the operation and get the result.

        **Parameters**

        - **`time`**: the next requested time step
        """
        helicsFederateRequestTimeAsync(self, time)

    def request_time_iterative_async(self, time: float, iterate: HelicsIterationRequest):
        """
        Request a time advancement with iterative call and return for asynchronous function.
        `self.request_time_iterative_complete()` should be called to finish the operation and get the result.

        **Parameters**

        - **`time`**: the next requested time step.
        - **`iterate`**: a requested iteration level (none, require, optional).
        """
        helicsFederateRequestTimeIterativeAsync(self, time, iterate)

    def request_time_complete(self) -> HelicsTime:
        """
        Request a time advancement.

        Returns: the granted time step.
        """
        return helicsFederateRequestTimeComplete(self)

    def request_time_iterative_complete(self) -> Tuple[HelicsTime, HelicsIterationResult]:
        """
        Finalize the time advancement request.

        Returns: the granted time step and iteration result.
        """
        granted_time, status = helicsFederateRequestTimeIterativeComplete(self)
        return granted_time, status

    def query(self, target: str, query: str) -> str:
        """
        Make a query of the federate.

        This call is blocking until the value is returned which make take some time depending on the size of the federation and the specific string being queried.

        **Parameters**

        - **`target`**: the target of the query can be "federation", "federate", "broker", "core", or a specific name of a federate, core, or broker.
        - **`query`**: a string with the query see other documentation for specific properties to query, can be defined by the federate.

        Returns: a string with the value requested.
        this is either going to be a vector of strings value or a JSON string stored in the first element of the vector. The string "#invalid" is returned if the query was not valid.
        """
        q = helicsCreateQuery(target, query)
        result = helicsQueryExecute(q, self)
        helicsQueryFree(q)
        return result

    def register_filter(self, kind: HelicsFilterType, filter_name: str) -> HelicsFilter:
        """
        Define a filter interface.

        A filter will modify messages coming from or going to target endpoints.

        **Parameters**

        - **`kind`**: the type of the filter to register.
        - **`filter_name`**: the name of the filter.
        """
        filter = helicsFederateRegisterFilter(self, kind, filter_name)
        self.filters[filter.name] = filter
        return filter

    def register_cloning_filter(self, delivery_endpoint: str) -> HelicsCloningFilter:
        """
        Create a `HelicsCloningFilter` on the specified federate.

        Cloning filters copy a message and send it to multiple locations source and destination can be added through other functions.

        **Parameters**

        - **`delivery_endpoint`**: the specified endpoint to deliver the message.

        Returns: A `HelicsCloningFilter` object.
        """
        filter = helicsFederateRegisterCloningFilter(self, delivery_endpoint)
        self.filters[filter.name] = filter
        return filter

    def register_global_filter(self, kind: HelicsFilterType, filter_name: str) -> HelicsFilter:
        """
        Define a filter interface.

        A filter will modify messages coming from or going to target endpoints.

        **Parameters**

        - **`kind`**: the type of the filter to register.
        - **`filter_name`**: the name of the filter.
        """
        filter = helicsFederateRegisterGlobalFilter(self, kind, filter_name)
        self.filters[filter.name] = filter
        return filter

    def register_global_cloning_filter(self, delivery_endpoint: str) -> HelicsCloningFilter:
        """
        Create a cloning Filter on the specified federate

        Cloning filters copy a message and send it to multiple locations source and destination can be added through other functions.

        **Parameters**

        - **`delivery_endpoint`**: the specified endpoint to deliver the message.

        Returns: A CloningFilter object.
        """
        filter = helicsFederateRegisterGlobalCloningFilter(self, delivery_endpoint)
        self.filters[filter.name] = filter
        return filter

    def get_filter_by_name(self, filter_name):
        """
        Get the id of a source filter from the name of the endpoint.

        **Parameters**

        - **`filter_name`**: the name of the filter.

        Returns: a reference to a filter object which could be invalid if `filter_name` is not valid.
        """
        return helicsFederateGetFilter(self, filter_name)

    def get_filter_by_index(self, filter_index):
        """
        Get a filter by index.

        **Parameters**

        - **`index`**: the index of a filter.

        Returns: A reference to a filter object which could be invalid if `filter_name` is not valid.
        """
        return helicsFederateGetFilterByIndex(self, filter_index)

    def set_global(self, name: str, value: str):
        """
        Set a federation global value.

        This overwrites any previous value for this name.

        **Parameters**

        - **`name`**: the name of the global to set.
        - **`value`**: the value of the global.
        """
        helicsFederateSetGlobal(self, name, value)

    def add_dependency(self, federate_name):
        """
        Add a dependency for this federate.

        Adds an additional internal time dependency for the federate.

        **Parameters**

        - **`fed_name`**: the name of the federate to add a dependency on.
        """
        helicsFederateAddDependency(self, federate_name)

    def local_error(self, error_code: int, error_string: str):
        """
        Generate a local federate error.

        **Parameters**

        - **`error_code`**: an error code to give to the error.
        - **`error_string`**: a string message associated with the error.
        """
        helicsFederateLocalError(self, error_code, error_string)

    def global_error(self, error_code: int, error_string: str):
        """
        Generate a global error to terminate the federation.

        **Parameters**

        - **`error_code`**: an error code to give to the error.
        - **`error_string`**: a string message associated with the error.
        """
        helicsFederateGlobalError(self, error_code, error_string)

    def log_message(self, message: str, level: HelicsLogLevel):
        """Log an message."""
        if level == logging.ERROR:
            helicsFederateLogErrorMessage(self, message)
        elif level == logging.WARN:
            helicsFederateLogWarningMessage(self, message)
        elif level == logging.INFO:
            helicsFederateLogInfoMessage(self, message)
        elif level == logging.DEBUG:
            helicsFederateLogDebugMessage(self, message)
        else:
            helicsFederateLogLevelMessage(self, HelicsLogLevel(level), message)


class _InputOptionAccessor(_HelicsCHandle):
    def __getitem__(self, index):
        if type(index) == str:
            idx = helicsGetOptionIndex(index)
        else:
            idx = HelicsHandleOption(index)
        return helicsInputGetOption(self, idx)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = helicsGetOptionIndex(index)
        else:
            idx = HelicsHandleOption(index)
        return helicsInputSetOption(self, idx, value)

    def __repr__(self):
        lst = []
        for o in HelicsHandleOption:
            lst.append("'{}' = {}".format(o.name, self[o]))
        return "<{{ {} }}>".format(", ".join(lst))

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class HelicsInput(_HelicsCHandle):
    def __init__(self, handle):
        super(HelicsInput, self).__init__(handle)
        self.option = _InputOptionAccessor(self.handle)

    def __repr__(self):
        key = self.key
        units = self.units
        injection_units = self.injection_units
        publication_type = self.publication_type
        type = self.type
        target = self.target
        info = self.info
        return """<helics.{class_name}(key = "{key}", units = "{units}", injection_units = "{injection_units}", publication_type = "{publication_type}", type = "{type}", target = "{target}", info = "{info}") at {id}>""".format(
            class_name=self.__class__.__name__,
            key=key,
            units=units,
            injection_units=injection_units,
            publication_type=publication_type,
            type=type,
            target=target,
            info=info,
            id=hex(id(self)),
        )

    def is_valid(self) -> bool:
        """Check if the input is valid."""
        return helicsInputIsValid(self)

    def add_target(self, target: str):
        """Add a publication target to the input."""
        helicsInputAddTarget(self, target)

    def set_default(self, data: Union[bytes, str, int, bool, float, complex, List[float]]):
        """
        Set the default value as a raw data
        Set the default value as a string
        Set the default value as an integer
        Set the default value as a bool
        Set the default value as a double
        Set the default value as a vector of doubles
        """
        if isinstance(data, bytes):
            helicsInputSetDefaultBytes(self, data)
        elif isinstance(data, str):
            helicsInputSetDefaultString(self, data)
        elif isinstance(data, int):
            helicsInputSetDefaultInteger(self, data)
        elif isinstance(data, bool):
            helicsInputSetDefaultBoolean(self, data)
        elif isinstance(data, float):
            helicsInputSetDefaultDouble(self, data)
        elif isinstance(data, complex):
            helicsInputSetDefaultComplex(self, data)
        elif isinstance(data, list):
            helicsInputSetDefaultVector(self, data)
        else:
            raise NotImplementedError("Unknown type `{}`".format(type(data)))

    @property
    def bytes(self) -> bytes:
        """Get a raw value as a character vector."""
        return helicsInputGetRawValue(self)

    @property
    def string(self) -> str:
        """Get the current value as a string."""
        return helicsInputGetString(self)

    @property
    def named_point(self) -> Tuple[str, float]:
        """Get the current value as a named point."""
        return helicsInputGetNamedPoint(self)

    @property
    def integer(self) -> int:
        """Get the current value as a 64 bit integer."""
        return helicsInputGetInteger(self)

    @property
    def boolean(self) -> bool:
        """Get the value as a boolean."""
        return helicsInputGetBoolean(self)

    @property
    def double(self) -> float:
        """Get the value as a double."""
        return helicsInputGetDouble(self)

    @property
    def complex(self) -> complex:
        """Get the value as a complex number."""
        r, i = helicsInputGetComplex(self)
        return complex(r, i)

    @property
    def vector(self) -> List[float]:
        """get the current value as a vector of doubles."""
        return helicsInputGetVector(self)

    def is_updated(self) -> bool:
        """Check if an input is updated."""
        return helicsInputIsUpdated(self)

    def get_last_update_time(self) -> HelicsTime:
        """Get the last time an input was updated."""
        return helicsInputLastUpdateTime(self)

    def clear_update(self):
        """Clear the updated flag."""
        helicsInputClearUpdate(self)

    @property
    def key(self) -> str:
        """get the Name/Key for the input
        the name is the local name if given, key is the full key name."""
        return helicsInputGetKey(self)

    @property
    def units(self) -> str:
        """Get the units associated with a input."""
        return helicsInputGetExtractionUnits(self)

    @property
    def injection_units(self) -> str:
        """Get the units associated with an inputs publication."""
        return helicsInputGetInjectionUnits(self)

    @property
    def publication_type(self) -> str:
        """Get the units associated with a publication of an input."""
        return helicsInputGetPublicationType(self)

    @property
    def type(self) -> str:
        """Get the type of the input."""
        return helicsInputGetType(self)

    @property
    def target(self) -> str:
        """Get an associated target."""
        return helicsSubscriptionGetKey(self)

    @property
    def info(self) -> str:
        """Get the interface information field of the filter."""
        return helicsInputGetInfo(self)

    @info.setter
    def info(self, info: str):
        """Set the interface information field of the publication."""
        helicsInputSetInfo(self, info)


class HelicsPublication(_HelicsCHandle):
    def __init__(self, handle):
        super(HelicsPublication, self).__init__(handle)
        self.option = _PublicationOptionAccessor(self.handle)

    def __repr__(self):
        key = self.key
        type = self.type
        info = self.info
        units = self.units
        return """<helics.{class_name}(key = "{key}", type = "{type}", units = "{units}", info = "{info}") at {id}>""".format(
            class_name=self.__class__.__name__, key=key, type=type, units=units, info=info, id=hex(id(self))
        )

    def is_valid(self) -> bool:
        """Check if the publication is valid."""
        return helicsPublicationIsValid(self)

    def publish(self, data: Union[bytes, str, int, complex, float, List[float], Tuple[str, float], bool]):
        """
        publish raw bytes
        publish a string
        publish an int value
        publish a double
        publish a complex number
        publish a vector of doubles
        publish a named point with a string and double
        publish a boolean value
        """
        if isinstance(data, bytes):
            helicsPublicationPublishBytes(self, data)
        elif isinstance(data, str):
            helicsPublicationPublishString(self, data)
        elif isinstance(data, int):
            helicsPublicationPublishInteger(self, data)
        elif isinstance(data, float):
            helicsPublicationPublishDouble(self, data)
        elif isinstance(data, complex):
            helicsPublicationPublishComplex(self, data)
        elif isinstance(data, list):
            helicsPublicationPublishVector(self, data)
        elif isinstance(data, tuple):
            helicsPublicationPublishNamedPoint(self, data[0], data[1])
        elif isinstance(data, bool):
            helicsPublicationPublishBoolean(self, data)
        else:
            raise NotImplementedError("Unknown type `{}`".format(type(data)))

    @property
    def key(self) -> str:
        """Get the key for the publication."""
        return helicsPublicationGetKey(self)

    @property
    def units(self) -> str:
        """Get the units of the publication."""
        return helicsPublicationGetUnits(self)

    @property
    def type(self) -> str:
        """Get the type for the publication."""
        return helicsPublicationGetType(self)

    @property
    def info(self) -> str:
        """Get the interface information field of the publication."""
        return helicsPublicationGetInfo(self)

    @info.setter
    def info(self, info: str):
        """Set the interface information field of the publication."""
        helicsPublicationSetInfo(self, info)


class HelicsValueFederate(HelicsFederate):
    def register_publication(self, name: str, kind: Union[str, HelicsDataType], units: str = "") -> HelicsPublication:
        """
        Register a publication.

        Call is only valid in startup mode.

        **Parameters**

        - **`name`**: the name of the publication.
        - **`kind`**: the type of the publication.
        - **`units`**: a string defining the units of the publication [optional]

        Returns: a publication id object for use as an identifier
        """
        if type(kind) == str:
            pub = helicsFederateRegisterTypePublication(self, name, kind, units)
        else:
            pub = helicsFederateRegisterPublication(self, name, HelicsDataType(kind), units)
        self.publications[pub.key] = pub
        return pub

    def register_global_publication(self, name: str, kind: Union[str, HelicsDataType], units: str = "") -> HelicsPublication:
        """
        Register a publication

        Call is only valid in startup mode

        **Parameters**

        - **`name`**: the name of the publication
        - **`kind`**: the type of the publication
        - **`units`**: a string defining the units of the publication [optional]

        Returns: a publication object for use as an identifier
        """
        if type(kind) == str:
            pub = helicsFederateRegisterGlobalTypePublication(self, name, kind, units)
        else:
            pub = helicsFederateRegisterGlobalPublication(self, name, HelicsDataType(kind), units)
        self.publications[pub.key] = pub
        return pub

    def register_from_publication_json(self, data: Union[dict, str]) -> HelicsPublication:
        """
        Register publications from a JSON output file or string.

        Generates interface based on the data contained in a JSON file or string.
        """
        if type(data) == str:
            try:
                with open(data) as f:
                    data = json.load(f)
            except Exception:
                data = json.loads(data)
        else:
            data = json.dumps(data)
        pub = helicsFederateRegisterFromPublicationJSON(self, data)
        self.publications["{}".format(pub.key)] = pub
        return pub

    def get_publication_by_name(self, name: str) -> HelicsPublication:
        """Get publication by name."""
        return helicsFederateGetPublication(self, name)

    def get_publication_by_index(self, index: int) -> HelicsPublication:
        """
        Get a publication by index.

        **Parameters**

        - **`index`**: a 0 based index of the publication to retrieve

        Returns: a Publication object
        """
        return helicsFederateGetPublicationByIndex(self, index)

    def register_subscription(self, name: str, units: str = "") -> HelicsInput:
        sub = helicsFederateRegisterSubscription(self, name, units)
        self.subscriptions[sub.target] = sub
        return sub

    def register_input(self, name: str, kind: Union[str, HelicsDataType], units: str = "") -> HelicsInput:
        """
        Register an input.

        Call is only valid in startup mode.

        **Parameters**

        - **`name`**: the name of the input
        - **`kind`**: the type of input to register
        - **`units`**: a string defining the units of the input [optional]

        Returns: an input id object for use as an identifier
        """
        if type(kind) == str:
            ipt = helicsFederateRegisterTypeInput(self, name, kind, units)
        else:
            ipt = helicsFederateRegisterTypeInput(self, name, HelicsDataType(kind), units)
        self.subscriptions[ipt.target] = ipt
        return ipt

    def register_global_input(self, name: str, kind: Union[str, HelicsDataType], units: str = "") -> HelicsInput:
        """
        Register an input.

        Call is only valid in startup mode.

        **Parameters**

        - **`name`**: the name of the input
        - **`kind`**: a string defining the type of the input
        - **`units`**: a string defining the units of the input [optional]

        Returns: an input object for use as an identifier.
        """
        if type(kind) == str:
            ipt = helicsFederateRegisterGlobalTypeInput(self, name, kind, units)
        else:
            ipt = helicsFederateRegisterGlobalTypeInput(self, name, HelicsDataType(kind), units)
        self.subscriptions[ipt.target] = ipt
        return ipt

    def get_subscription_by_name(self, name: str) -> HelicsInput:
        """Get an input by index."""
        return helicsFederateGetInput(self, name)

    def get_subscription_by_index(self, index: int) -> HelicsInput:
        """Get a subscription by index."""
        return helicsFederateGetInputByIndex(self, index)

    @property
    def n_subscriptions(self) -> int:
        """Get the number of inputs in this federate."""
        return helicsFederateGetInputCount(self)

    @property
    def n_publications(self) -> int:
        """Get the number of publications in this federate."""
        return helicsFederateGetPublicationCount(self)

    def clear_updates(self):
        """Clear all the update flags from all federate inputs."""
        helicsFederateClearUpdates(self)

    def publish_json(self, data: Union[dict, str]):
        """Publish data contained in a JSON file."""
        if type(data) == str:
            try:
                with open(data) as f:
                    data = json.load(f)
            except Exception:
                data = json.loads(data)
        else:
            data = json.dumps(data)
        helicsFederatePublishJSON(self, data)


class HelicsMessageFederate(HelicsFederate):
    def __init__(self, handle):
        super(HelicsMessageFederate, self).__init__(handle)

    def register_endpoint(self, name: str, kind: str = "") -> HelicsEndpoint:
        """
        Register an endpoint.

        Call is only valid in startup mode

        - **`name`**: the name of the endpoint
        - **`kind`**: the defined type of the interface for endpoint checking if requested

        Returns: an Endpoint Object
        """
        ep = helicsFederateRegisterEndpoint(self, name, kind)
        self.endpoints[ep.name] = ep
        return ep

    def register_global_endpoint(self, name: str, kind: str = "") -> HelicsEndpoint:
        """
        Register an endpoint directly without prepending the federate name.

        - **`name`**: the name of the endpoint
        - **`kind`**: the defined type of the interface for endpoint checking if requested

        Returns: an Endpoint Object
        """
        ep = helicsFederateRegisterGlobalEndpoint(self, name, kind)
        self.endpoints[ep.name] = ep
        return ep

    def get_endpoint_by_name(self, name: str) -> HelicsEndpoint:
        """
        Get an Endpoint from its name.

        **Parameters**

        - **`name`**: the name of the endpoint to retrieve.

        Returns: an Endpoint
        """
        return helicsFederateGetEndpoint(self, name)

    def get_endpoint_by_index(self, index: int) -> HelicsEndpoint:
        """
        Get an Endpoint from an index.

        **Parameters**

        - **`index`**: the index of the endpoint to retrieve index is 0 based

        Return an Endpoint
        """
        return helicsFederateGetEndpointByIndex(self, index)

    def has_message(self) -> bool:
        """Checks if federate has any messages."""
        return helicsFederateHasMessage(self)

    def get_message(self) -> HelicsMessage:
        """Get a packet for any endpoints in the federate."""
        return helicsFederateGetMessage(self)

    def create_message(self) -> HelicsMessage:
        """Create a message object."""
        return helicsFederateCreateMessage(self)


class HelicsCombinationFederate(HelicsValueFederate, HelicsMessageFederate):
    pass


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

    - **`type`** - A string representing a core type. Options include "zmq", "udp", "ipc", "interprocess", "tcp", "default", "mpi".

    **Returns**: `True` if `type` is available, `False` if `type` is not available.
    """
    f = loadSym("helicsIsCoreTypeAvailable")
    result = f(cstring(type))
    return result == 1


def helicsCreateCore(type: str, name: str, init_string: str) -> HelicsCore:
    """
    Create a `helics.HelicsCore`.

    **Parameters**

    - **`type`** - The type of the core to create.
    - **`name`** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    - **`init_string`** - An initialization string to send to the core. The format is similar to command line arguments. Typical options include a broker name, the broker address, the number of federates, etc.

    **Returns**: `helics.HelicsCore`.
    """
    f = loadSym("helicsCreateCore")
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), cstring(init_string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCore(result)


def helicsCreateCoreFromArgs(type: str, name: str, arguments: List[str]) -> HelicsCore:
    """
    Create a `helics.HelicsCore` by passing command line arguments.

    **Parameters**

    - **`type`** - The type of the core to create.
    - **`name`** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    - **`arguments`** - The list of string values from a command line.

    **Returns**: `helics.HelicsCore`.
    """
    f = loadSym("helicsCreateCoreFromArgs")
    argc = len(arguments)
    argv = ffi.new("char*[{argc}]".format(argc=argc))
    for i, s in enumerate(arguments):
        argv[i] = cstring(s)
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), argc, argv, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCore(result)


def helicsCoreClone(core: HelicsCore) -> HelicsCore:
    """
    Create a new reference to an existing core.
    This will create a new `helics.HelicsCore` that references the existing core.
    The new `helics.HelicsCore` must be freed as well.

    **Parameters**

    - **`core`** - An existing `helics.HelicsCore`.

    **Returns**: `helics.HelicsCore`.
    """
    f = loadSym("helicsCoreClone")
    err = helicsErrorInitialize()
    result = f(core.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCore(result)


def helicsCoreIsValid(core: HelicsCore) -> bool:
    """
    Check if a `helics.HelicsCore` is a valid object.

    **Parameters**

    - **`core`** - The `helics.HelicsCore` object to test.

    **Returns**: `True` if valid, `False` if not valid.
    """
    f = loadSym("helicsCoreIsValid")
    result = f(core.handle)
    return result == 1


def helicsCreateBroker(type: str, name: str, init_string: str) -> HelicsBroker:
    """
    Create a broker object

    **Parameters**

    - **`type`** - The type of the broker to create.
    - **`name`** - The name of the broker. It can be a nullptr or empty string to have a name automatically assigned.
    - **`init_string`** - An initialization string to send to the core-the format is similar to command line arguments. Typical options include a broker address such as --broker="XSSAF" if this is a subbroker, or the number of federates, or the address.

    **Returns**: `helics.HelicsBroker`.
    """
    f = loadSym("helicsCreateBroker")
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), cstring(init_string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsBroker(result)


def helicsCreateBrokerFromArgs(type: str, name: str, arguments: List[str]) -> HelicsBroker:
    """
    Create a `helics.HelicsCore` by passing command line arguments.

    **Parameters**

    - **`type`** - The type of the core to create.
    - **`name`** - The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
    - **`arguments`** - The list of string values from a command line.

    **Returns**: `helics.HelicsBroker`.
    """
    f = loadSym("helicsCreateBrokerFromArgs")
    argc = len(arguments)
    argv = ffi.new("char*[{argc}]".format(argc=argc))
    for i, s in enumerate(arguments):
        argv[i] = cstring(s)
    err = helicsErrorInitialize()
    result = f(cstring(type), cstring(name), argc, argv, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsBroker(result)


def helicsBrokerClone(broker: HelicsBroker) -> HelicsBroker:
    """
    Create a new reference to an existing broker.
    This will create a new broker object that references the existing broker it must be freed as well.

    **Parameters**

    - **`broker`** - An existing `helics.HelicsBroker`.

    **Returns**: `helics.HelicsBroker`.
    """
    f = loadSym("helicsBrokerClone")
    err = helicsErrorInitialize()
    result = f(broker.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsBroker(result)


def helicsBrokerIsValid(broker: HelicsBroker) -> bool:
    """
    Check if a broker object is a valid object.

    **Parameters**

    - **`broker`** - The `helics.HelicsBroker` object to test.

    **Returns**: `True` if valid, `False` if not valid.
    """
    f = loadSym("helicsBrokerIsValid")
    result = f(broker.handle)
    return result == 1


def helicsBrokerIsConnected(broker: HelicsBroker) -> bool:
    """
    Check if a broker is connected.
    A connected broker implies it is attached to cores or cores could reach out to communicate.

    **Returns**: `True` if connected, `False` if not connected.
    """
    f = loadSym("helicsBrokerIsConnected")
    result = f(broker.handle)
    return result == 1


def helicsBrokerDataLink(broker: HelicsBroker, source_name: str, target_name: str):
    """
    Link a named publication and named input using a broker.

    **Parameters**

    - **`broker`** - The broker to generate the connection from.
    - **`source_name`** - The name of the publication.
    - **`target_name`** - The name of the target to send the publication data.
    """
    f = loadSym("helicsBrokerDataLink")
    err = helicsErrorInitialize()
    f(broker.handle, cstring(source_name), cstring(target_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddSourceFilterToEndpoint(broker: HelicsBroker, filter_name: str, endpoint_name: str):
    """
    Link a named filter to a source endpoint.

    **Parameters**

    - **`broker`** - The broker to generate the connection from.
    - **`filter`** - The name of the filter.
    - **`endpoint`** - The name of the endpoint to filter the data from.
    """
    f = loadSym("helicsBrokerAddSourceFilterToEndpoint")
    err = helicsErrorInitialize()
    f(broker.handle, cstring(filter_name), cstring(endpoint_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddDestinationFilterToEndpoint(broker: HelicsBroker, filter_name: str, endpoint_name: str):
    """
    Link a named filter to a destination endpoint.

    **Parameters**

    - **`broker`** - The broker to generate the connection from.
    - **`filter`** - The name of the filter.
    - **`endpoint`** - The name of the endpoint to filter the data going to.
    """
    f = loadSym("helicsBrokerAddDestinationFilterToEndpoint")
    err = helicsErrorInitialize()
    f(broker.handle, cstring(filter_name), cstring(endpoint_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerMakeConnections(broker: HelicsBroker, file: str):
    """
    Load a file containing connection information.

    **Parameters**

    - **`broker`** - The broker to generate the connections from.
    - **`file`** - A JSON or TOML file containing connection information.
    """
    f = loadSym("helicsBrokerMakeConnections")
    err = helicsErrorInitialize()
    f(broker.handle, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreWaitForDisconnect(core: HelicsCore, ms_to_wait: int) -> bool:
    """
    Wait for the core to disconnect.

    **Parameters**

    - **`core`** - The core to wait for.
    - **`ms_to_wait`** - The time out in millisecond (<0 for infinite timeout).
    """
    f = loadSym("helicsCoreWaitForDisconnect")
    err = helicsErrorInitialize()
    result = f(core.handle, ms_to_wait, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsBrokerWaitForDisconnect(broker: HelicsBroker, ms_to_wait: int) -> bool:
    """
    Wait for the broker to disconnect.

    **Parameters**

    - **`broker`** - The broker to wait for.
    - **`ms_to_wait`** - The time out in millisecond (<0 for infinite timeout).
    """
    f = loadSym("helicsBrokerWaitForDisconnect")
    err = helicsErrorInitialize()
    result = f(broker.handle, ms_to_wait, err)
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
    result = f(core.handle)
    return result == 1


def helicsCoreDataLink(core: HelicsCore, source_name: str, target_name: str):
    """
    Link a named publication and named input using a core.

    **Parameters**

    - **`core`** - The core to generate the connection from.
    - **`source_name`** - The name of the publication.
    - **`target_name`** - The name of the target to send the publication data.
    """
    f = loadSym("helicsCoreDataLink")
    err = helicsErrorInitialize()
    f(core.handle, cstring(source_name), cstring(target_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddSourceFilterToEndpoint(core: HelicsCore, filter_name: str, endpoint_name: str):
    """
    Link a named filter to a source endpoint.

    **Parameters**

    - **`core`** - The core to generate the connection from.
    - **`filter`** - The name of the filter.
    - **`endpoint`** - The name of the endpoint to filter the data from.
    """
    f = loadSym("helicsCoreAddSourceFilterToEndpoint")
    err = helicsErrorInitialize()
    f(core.handle, cstring(filter_name), cstring(endpoint_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddDestinationFilterToEndpoint(core: HelicsCore, filter_name: str, endpoint_name: str):
    """
    Link a named filter to a destination endpoint.

    **Parameters**

    - **`core`** - The core to generate the connection from.
    - **`filter`** - The name of the filter.
    - **`endpoint`** - The name of the endpoint to filter the data going to.
    """
    f = loadSym("helicsCoreAddDestinationFilterToEndpoint")
    err = helicsErrorInitialize()
    f(core.handle, cstring(filter_name), cstring(endpoint_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreMakeConnections(core: HelicsCore, file: str):
    """
    Load a file containing connection information.

    **Parameters**

    - **`core`** - The core to generate the connections from.
    - **`file`** - A JSON or TOML file containing connection information.
    """
    f = loadSym("helicsCoreMakeConnections")
    err = helicsErrorInitialize()
    f(core.handle, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerGetIdentifier(broker: HelicsBroker) -> str:
    """
    Get an identifier for the broker.

    **Parameters**

    - **`broker`** - The broker to query.

    **Returns**: A string containing the identifier for the broker.
    """
    f = loadSym("helicsBrokerGetIdentifier")
    result = f(broker.handle)
    return ffi.string(result).decode()


def helicsCoreGetIdentifier(core: HelicsCore) -> str:
    """
    Get an identifier for the core.

    **Parameters**

    - **`core`** - The core to query.

    **Returns**: A string with the identifier of the core.
    """
    f = loadSym("helicsCoreGetIdentifier")
    result = f(core.handle)
    return ffi.string(result).decode()


def helicsBrokerGetAddress(broker: HelicsBroker) -> str:
    """
    Get the network address associated with a broker.

    **Parameters**

    - **`broker`** - The broker to query.

    **Returns**: A string with the network address of the broker.
    """
    f = loadSym("helicsBrokerGetAddress")
    result = f(broker.handle)
    return ffi.string(result).decode()


def helicsCoreGetAddress(core: HelicsCore) -> str:
    """
    Get the network address associated with a core.

    **Parameters**

    - **`core`** - The core to query.

    **Returns**: A string with the network address of the broker.
    """
    f = loadSym("helicsCoreGetAddress")
    result = f(core.handle)
    return ffi.string(result).decode()


def helicsCoreSetReadyToInit(core: HelicsCore):
    """
    Set the core to ready for init.
    This function is used for cores that have filters but no federates so there needs to be a direct signal to the core to trigger the federation initialization.

    **Parameters**

    - **`core`** - The `helics.HelicsCore` to enable init values for.
    """
    f = loadSym("helicsCoreSetReadyToInit")
    err = helicsErrorInitialize()
    f(core.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreConnect(core: HelicsCore) -> bool:
    """
    Connect a core to the federate based on current configuration.

    **Parameters**

    - **`core`** - The core to connect.

    **Returns**: `True` if `core` is connected successfully, else `False`.
    """
    f = loadSym("helicsCoreConnect")
    err = helicsErrorInitialize()
    result = f(core.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsCoreDisconnect(core: HelicsCore):
    """
    Disconnect a core from the federation.

    **Parameters**

    - **`core`** - The core to query.
    """
    f = loadSym("helicsCoreDisconnect")
    err = helicsErrorInitialize()
    f(core.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetFederateByName(fed_name: str) -> HelicsFederate:
    """
    Get an existing `helics.HelicsFederate` from a core by name.
    The federate must have been created by one of the other functions and at least one of the objects referencing the created federate must still be active in the process.

    **Parameters**

    - **`fed_name`** - The name of the federate to retrieve.

    **Returns**: `helics.HelicsFederate`.
    """
    f = loadSym("helicsGetFederateByName")
    err = helicsErrorInitialize()
    result = f(cstring(fed_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFederate(result)


def helicsBrokerDisconnect(broker: HelicsBroker):
    """
    Disconnect a broker.

    **Parameters**

    - **`broker`** - The broker to disconnect.
    """
    f = loadSym("helicsBrokerDisconnect")
    err = helicsErrorInitialize()
    f(broker.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateDestroy(fed: HelicsFederate):
    """
    Disconnect and free a federate.
    """
    f = loadSym("helicsFederateDestroy")
    f(fed.handle)


def helicsBrokerDestroy(broker: HelicsBroker):
    """
    Disconnect and free a broker.
    """
    f = loadSym("helicsBrokerDestroy")
    f(broker.handle)


def helicsCoreDestroy(core: HelicsCore):
    """
    Disconnect and free a core.
    """
    f = loadSym("helicsCoreDestroy")
    f(core.handle)


def helicsCoreFree(core: HelicsCore):
    """
    Release the memory associated with a core.
    """
    f = loadSym("helicsCoreFree")
    f(core.handle)


def helicsBrokerFree(broker: HelicsBroker):
    """
    Release the memory associated with a broker.
    """
    f = loadSym("helicsBrokerFree")
    f(broker.handle)


def helicsCreateValueFederate(fed_name: str, fi: HelicsFederateInfo = None) -> HelicsValueFederate:
    """
    Creation and destruction of Federates.
    Create `helics.HelicsValueFederate` from `helics.HelicsFederateInfo`.
    `helics.HelicsValueFederate` objects can be used in all functions that take a `helics.HelicsFederate` as an argument.

    **Parameters**

    - **`fed_name`** - The name of the federate to create, can NULL or an empty string to use the default name from fi or an assigned name.
    - **`fi`** - The federate info object that contains details on the federate.

    **Returns**: `helics.HelicsValueFederate`.
    """
    f = loadSym("helicsCreateValueFederate")
    err = helicsErrorInitialize()
    if fi is None:
        fi = helicsCreateFederateInfo()
    result = f(cstring(fed_name), fi.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsValueFederate(result)


def helicsCreateValueFederateFromConfig(config_file: str) -> HelicsValueFederate:
    """
    Create `helics.HelicsValueFederate` from a JSON file, JSON string, or TOML file.
    `helics.HelicsValueFederate` objects can be used in all functions that take a `helics.HelicsFederate` as an argument.

    **Parameters**

    - **`config_file`** - A JSON file or a JSON string or TOML file that contains setup and configuration information.

    **Returns**: `helics.HelicsValueFederate`.
    """
    f = loadSym("helicsCreateValueFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(config_file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsValueFederate(result)


def helicsCreateMessageFederate(fed_name: str, fi: HelicsFederateInfo = None) -> HelicsMessageFederate:
    """
    Create `helics.HelicsMessageFederate` from `helics.HelicsFederateInfo`.
    `helics.HelicsMessageFederate` objects can be used in all functions that take a `helics.HelicsFederate` as an argument.

    **Parameters**

    - **`fed_name`** - The name of the federate to create.
    - **`fi`** - The federate info object that contains details on the federate.

    **Returns**: `helics.HelicsMessageFederate`.
    """
    f = loadSym("helicsCreateMessageFederate")
    err = helicsErrorInitialize()
    if fi is None:
        fi = helicsCreateFederateInfo()
    result = f(cstring(fed_name), fi.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsMessageFederate(result)


def helicsCreateMessageFederateFromConfig(config_file: str) -> HelicsMessageFederate:
    """
    Create `helics.HelicsMessageFederate` from a JSON file or JSON string or TOML file.
    `helics.HelicsMessageFederate` objects can be used in all functions that take a `helics.HelicsFederate` object as an argument.

    **Parameters**

    - **`config_file`** - A config (JSON,TOML) file or a JSON string that contains setup and configuration information.

    **Returns**: `helics.HelicsMessageFederate`.
    """
    f = loadSym("helicsCreateMessageFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(config_file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsMessageFederate(result)


def helicsCreateCombinationFederate(fed_name: str, fi: HelicsFederateInfo = None) -> HelicsCombinationFederate:
    """
    Create a combination federate from `helics.HelicsFederateInfo`.
    Combination federates are both value federates and message federates, objects can be used in all functions
    that take a `helics.HelicsFederate` object as an argument.

    **Parameters**

    - **`fed_name`** - A string with the name of the federate, can be NULL or an empty string to pull the default name from fi.
    - **`fi`** - The federate info object that contains details on the federate.

    **Returns**: `helics.HelicsCombinationFederate`.
    """
    f = loadSym("helicsCreateCombinationFederate")
    err = helicsErrorInitialize()
    if fi is None:
        fi = helicsCreateFederateInfo()
    result = f(cstring(fed_name), fi.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCombinationFederate(result)


def helicsCreateCombinationFederateFromConfig(config_file: str) -> HelicsCombinationFederate:
    """
    Create a combination federate from a JSON file or JSON string or TOML file.
    Combination federates are both value federates and message federates, objects can be used in all functions
    that take a `helics.HelicsFederate` object as an argument.

    **Parameters**

    - **`config_file`** - A JSON file or a JSON string or TOML file that contains setup and configuration information.

    **Returns**: `helics.HelicsCombinationFederate`.
    """
    f = loadSym("helicsCreateCombinationFederateFromConfig")
    err = helicsErrorInitialize()
    result = f(cstring(config_file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCombinationFederate(result)


def helicsFederateClone(fed: HelicsFederate) -> HelicsFederate:
    """
    Create a new reference to an existing federate.
    This will create a new `helics.HelicsFederate` object that references the existing federate.
    The new object must be freed as well.

    **Parameters**

    - **`fed`** - An existing `helics.HelicsFederate`.

    **Returns**: `helics.HelicsFederate`.
    """
    f = loadSym("helicsFederateClone")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFederate(result)


def helicsCreateFederateInfo() -> HelicsFederateInfo:
    """
    Create `helics.HelicsFederateInfo` for specifying federate information when constructing a federate.

    **Returns**: `helics.HelicsFederateInfo`.
    """
    f = loadSym("helicsCreateFederateInfo")
    result = f()
    return HelicsFederateInfo(result)


def helicsFederateInfoClone(fi: HelicsFederateInfo) -> HelicsFederateInfo:
    """
    Create `helics.HelicsFederateInfo` from an existing one and clone the information.

    **Parameters**

    - **`fi`** - A federateInfo object to duplicate.

    **Returns**: `helics.HelicsFederateInfo`.
    """
    f = loadSym("helicsFederateInfoClone")
    err = helicsErrorInitialize()
    result = f(fi.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFederateInfo(result)


def helicsFederateInfoLoadFromArgs(fi: HelicsFederateInfo, arguments: List[str]):
    """
    Load federate info from command line arguments.

    **Parameters**

    - **`fi`** - A federateInfo object.
    - **`argc`** - The number of command line arguments.
    - **`argv`** - An array of strings from the command line.
    """
    f = loadSym("helicsFederateInfoLoadFromArgs")
    err = helicsErrorInitialize()
    argc = len(arguments)
    argv = ffi.new("char*[{argc}]".format(argc=argc))
    for i, s in enumerate(arguments):
        argv[i] = cstring(s)
    f(fi.handle, argc, argv, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoFree(fi: HelicsFederateInfo):
    """
    Delete the memory associated with `helics.HelicsFederateInfo`.
    """
    f = loadSym("helicsFederateInfoFree")
    f(fi.handle)


def helicsFederateIsValid(fed: HelicsFederate) -> bool:
    """
    Check if a `helics.HelicsFederate` is valid.

    **Returns**: `True` if the federate is a valid active federate, `False` otherwise.
    """
    f = loadSym("helicsFederateIsValid")
    result = f(fed.handle)
    return result == 1


def helicsFederateInfoSetCoreName(fi: HelicsFederateInfo, core_name: str):
    """
    Set the name of the core to link to for a federate.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`core_name`** - The identifier for a core to link to.
    """
    f = loadSym("helicsFederateInfoSetCoreName")
    err = helicsErrorInitialize()
    f(fi.handle, cstring(core_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreInitString(fi: HelicsFederateInfo, core_init_string: str):
    """
    Set the initialization string for the core usually in the form of command line arguments.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`core_init_string`** - A string containing command line arguments to be passed to the core.
    """
    f = loadSym("helicsFederateInfoSetCoreInitString")
    err = helicsErrorInitialize()
    f(fi.handle, cstring(core_init_string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerInitString(fi: HelicsFederateInfo, broker_init_string: str):
    """
    Set the initialization string that a core will pass to a generated broker usually in the form of command line arguments.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`broker_init_string`** - A string with command line arguments for a generated broker.
    """
    f = loadSym("helicsFederateInfoSetBrokerInitString")
    err = helicsErrorInitialize()
    f(fi.handle, cstring(broker_init_string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreType(fi: HelicsFederateInfo, core_type: HelicsCoreType):
    """
    Set the core type by integer code.
    Valid values available by definitions in `api-data.h`.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`core_type`** - An numerical code for a core type see `helics.HelicsCoreType`.
    """
    f = loadSym("helicsFederateInfoSetCoreType")
    err = helicsErrorInitialize()
    f(fi.handle, HelicsCoreType(core_type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreTypeFromString(fi: HelicsFederateInfo, core_type: str):
    """
    Set the core type from a string.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`core_type`** - A string naming a core type.
    """
    f = loadSym("helicsFederateInfoSetCoreTypeFromString")
    err = helicsErrorInitialize()
    f(fi.handle, cstring(core_type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBroker(fi: HelicsFederateInfo, broker_string: str):
    """
    Set the name or connection information for a broker.
    This is only used if the core is automatically created, the broker information will be transferred to the core for connection.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`broker_string`** - A string which defines the connection information for a broker either a name or an address.
    """
    f = loadSym("helicsFederateInfoSetBroker")
    err = helicsErrorInitialize()
    f(fi.handle, cstring(broker_string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerKey(fi: HelicsFederateInfo, broker_key: str):
    """
    Set the key for a broker connection.
    This is only used if the core is automatically created, the broker information will be transferred to the core for connection.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`broker_key`** - A string containing a key for the broker to connect.
    """
    f = loadSym("helicsFederateInfoSetBrokerKey")
    err = helicsErrorInitialize()
    f(fi.handle, cstring(broker_key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerPort(fi: HelicsFederateInfo, broker_port: Union[int, str]):
    """
    Set the port to use for the broker.
    This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
    This will only be useful for network broker connections.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`broker_port`** - The integer port number to use for connection with a broker.
    """
    f = loadSym("helicsFederateInfoSetBrokerPort")
    err = helicsErrorInitialize()
    broker_port = int(broker_port)
    f(fi.handle, broker_port, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetLocalPort(fi: HelicsFederateInfo, local_port: Union[int, str]):
    """
    Set the local port to use.
    This is only used if the core is automatically created, the port information will be transferred to the core for connection.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`local_port`** - A string with the port information to use as the local server port can be a number or "auto" or "os_local".
    """
    f = loadSym("helicsFederateInfoSetLocalPort")
    err = helicsErrorInitialize()
    local_port = str(local_port)
    f(fi.handle, cstring(local_port), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetPropertyIndex(value: str) -> HelicsProperty:
    """
    Get a property index for use in `helics.helicsFederateInfoSetFlagOption`, `helics.helicsFederateInfoSetTimeProperty`, or `helics.helicsFederateInfoSetIntegerProperty`.

    **Parameters**

    - **`value`** - A string with the property name.

    **Returns**: An int with the property code or (-1) if not a valid property.
    """
    f = loadSym("helicsGetPropertyIndex")
    result = f(cstring(value))
    if result == -1:
        raise HelicsException("[-1] Unknown property index for flag `{value}`".format(value=value))
    else:
        return HelicsProperty(result)


def helicsGetFlagIndex(value: str) -> HelicsFederateFlag:
    """
    Get a property index for use in `helics.helicsFederateInfoSetFlagOption`, `helics.helicsFederateSetFlagOption`.

    **Parameters**

    - **`value`** - A string with the option name.

    **Returns**: An int with the property code or (-1) if not a valid property.
    """
    f = loadSym("helicsGetFlagIndex")
    result = f(cstring(value))
    if result == -1:
        raise HelicsException("[-1] Unknown property index for flag `{value}`".format(value=value))
    else:
        return HelicsFederateFlag(result)


def helicsGetOptionIndex(value: str) -> HelicsHandleOption:
    """
    Get an option index for use in `helics.helicsPublicationSetOption`, `helics.helicsInputSetOption`, `helics.helicsEndpointSetOption`,
    `helics.helicsFilterSetOption`, and the corresponding get functions

    **Parameters**

    - **`value`** - A string with the option name

    **Returns**: An int with the option index or (-1) if not a valid property.
    """
    f = loadSym("helicsGetOptionIndex")
    result = f(cstring(value))
    if result == -1:
        raise HelicsException("[-1] Unknown option index for flag `{value}`".format(value=value))
    else:
        return HelicsHandleOption(result)


def helicsGetOptionValue(value: str) -> int:
    """
    Get an option value for use in `helics.helicsPublicationSetOption`, `helics.helicsInputSetOption`, `helics.helicsEndpointSetOption`,
    `helics.helicsFilterSetOption`.

    **Parameters**

    - **`value`** - A string representing the value

    **Returns**: An int with the option value or (-1) if not a valid value.
    """
    f = loadSym("helicsGetOptionValue")
    result = f(cstring(value))
    if result == -1:
        raise HelicsException("[-1] Unknown option valud for flag `{value}`".format(value=value))
    else:
        return result


def helicsFederateInfoSetFlagOption(fi: HelicsFederateInfo, flag: HelicsFederateFlag, value: bool):
    """
    Set a flag in the info structure
    Valid flags are available `helics.HelicsFederateFlag`.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`flag`** - A numerical index for a flag.
    - **`value`** - The desired value of the flag `True` or `False`.
    """
    f = loadSym("helicsFederateInfoSetFlagOption")
    err = helicsErrorInitialize()
    f(fi.handle, flag, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetSeparator(fi: HelicsFederateInfo, separator: str):
    """
    Set the separator character in the info structure.
    The separator character is the separation character for local publications/endpoints in creating their global name.
    For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`separator`** - The character to use as a separator.
    """
    f = loadSym("helicsFederateInfoSetSeparator")
    err = helicsErrorInitialize()
    f(fi.handle, cchar(separator), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetTimeProperty(fi: HelicsFederateInfo, time_property: HelicsProperty, value: HelicsTime):
    """
    Set the output delay for a federate.

    **Parameters**

    - **`fi`** - The federate info object to alter.
    - **`time_property`** - An integer representation of the time based property to set see `helics.HelicsProperty`.
    - **`propertyValue`** - The value of the property to set the timeProperty to.
    """
    f = loadSym("helicsFederateInfoSetTimeProperty")
    err = helicsErrorInitialize()
    f(fi.handle, HelicsProperty(time_property), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetIntegerProperty(fi: HelicsFederateInfo, property: HelicsProperty, value: int):
    """
    Set an integer property for a federate.
    Set known properties.

    **Parameters**

    - **`fi`** - The federateInfo object to alter.
    - **`property`** - `helics.HelicsProperty`.
    - **`value`** - The value to set the property to.
    """
    f = loadSym("helicsFederateInfoSetIntegerProperty")
    err = helicsErrorInitialize()
    f(fi.handle, HelicsProperty(property), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRegisterInterfaces(fed: HelicsFederate, file: str):
    """
    Load interfaces from a file.

    **Parameters**

    - **`fed`** - The federate to which to load interfaces.
    - **`file`** - The name of a file to load the interfaces from either JSON, or TOML.
    """
    f = loadSym("helicsFederateRegisterInterfaces")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGlobalError(fed: HelicsFederate, error_code: int, error_string: str):
    """
    Generate a global error from a federate.
    A global error halts the co-simulation completely.

    **Parameters**

    - **`fed`** - The federate to create an error in.
    - **`error_code`** - The integer code for the error.
    - **`error_string`** - A string describing the error.
    """
    f = loadSym("helicsFederateGlobalError")
    f(fed.handle, error_code, cstring(error_string))


def helicsFederateLocalError(fed: HelicsFederate, error_code: int, error_string: str):
    """
    Generate a local error in a federate.
    This will propagate through the co-simulation but not necessarily halt the co-simulation, it has a similar effect to finalize but does allow some interaction with a core for a brief time.

    **Parameters**

    - **`fed`** - The federate to create an error in.
    - **`error_code`** - The integer code for the error.
    - **`error_string`** - A string describing the error.
    """
    f = loadSym("helicsFederateLocalError")
    f(fed.handle, error_code, cstring(error_string))


def helicsFederateFinalize(fed: HelicsFederate):
    """
    Finalize the federate. This function halts all communication in the federate and disconnects it from the core.
    """
    f = loadSym("helicsFederateFinalize")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFinalizeAsync(fed: HelicsFederate):
    """
    Finalize the federate in an async call.
    """
    f = loadSym("helicsFederateFinalizeAsync")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFinalizeComplete(fed: HelicsFederate):
    """
    Complete the asynchronous finalize call.
    """
    f = loadSym("helicsFederateFinalizeComplete")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFree(fed: HelicsFederate):
    """
    Release the memory associated with a federate.
    """
    f = loadSym("helicsFederateFree")
    f(fed.handle)


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

    - **`fed`** - The federate to operate on.
    """
    f = loadSym("helicsFederateEnterInitializingMode")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterInitializingModeAsync(fed: HelicsFederate):
    """
    Non blocking alternative to `helics.helicsFederateEnterInitializingMode`.
    The function helicsFederateEnterInitializationModeFinalize must be called to finish the operation.

    **Parameters**

    - **`fed`** - The federate to operate on.
    """
    f = loadSym("helicsFederateEnterInitializingModeAsync")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateIsAsyncOperationCompleted(fed: HelicsFederate) -> bool:
    """
    Check if the current Asynchronous operation has completed.

    **Parameters**

    - **`fed`** - The federate to operate on.

    **Returns**: `True` if current operation has completed, else `False`.
    """
    f = loadSym("helicsFederateIsAsyncOperationCompleted")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsFederateEnterInitializingModeComplete(fed: HelicsFederate):
    """
    Finalize the entry to initialize mode that was initiated with `helics.helicsEnterInitializingModeAsync`.

    **Parameters**

    - **`fed`** - The federate desiring to complete the initialization step.
    """
    f = loadSym("helicsFederateEnterInitializingModeComplete")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingMode(fed: HelicsFederate):
    """
    Request that the federate enter the Execution mode.
    This call is blocking until granted entry by the `helics.HelicsCore`. On return from this call the federate will be at time 0. For an asynchronous alternative call see `helics.helicsFederateEnterExecutingModeAsync`

    **Parameters**

    - **`fed`** - A federate to change modes.
    """
    f = loadSym("helicsFederateEnterExecutingMode")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeAsync(fed: HelicsFederate):
    """
    Request that the federate enter the Execution mode.
    This call is non-blocking and will return immediately. Call `helics.helicsFederateEnterExecutingModeComplete` to finish the call sequence

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` to complete the call.
    """
    f = loadSym("helicsFederateEnterExecutingModeAsync")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeComplete(fed: HelicsFederate):
    """
    Complete the call to `helics.helicsFederateEnterExecutingModeAsync`.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` to complete the call.
    """
    f = loadSym("helicsFederateEnterExecutingModeComplete")
    err = helicsErrorInitialize()
    f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterative(fed: HelicsFederate, iterate: HelicsIterationRequest) -> HelicsIterationResult:
    """
    Request an iterative time.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    - **`iterate`** - `helics.HelicsIterationRequest`, i.e. the requested iteration mode.

    **Returns**: `helics.HelicsIterationResult`.
    """
    f = loadSym("helicsFederateEnterExecutingModeIterative")
    err = helicsErrorInitialize()
    result = f(fed.handle, HelicsIterationRequest(iterate), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsIterationResult(result)


def helicsFederateEnterExecutingModeIterativeAsync(fed: HelicsFederate, iterate: HelicsIterationRequest):
    """
    Request an iterative entry to the execution mode.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    - **`iterate`** - `helics.HelicsIterationRequest`, i.e. the requested iteration mode.
    """
    f = loadSym("helicsFederateEnterExecutingModeIterativeAsync")
    err = helicsErrorInitialize()
    f(fed.handle, HelicsIterationRequest(iterate), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterativeComplete(fed: HelicsFederate,) -> HelicsIterationResult:
    """
    Complete the asynchronous iterative call into ExecutionMode.

    **Parameters**

    - **`fed`** - The federate to make the request of.

    **Returns**: `helics.HelicsIterationResult`.
    """
    f = loadSym("helicsFederateEnterExecutingModeIterativeComplete")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsIterationResult(result)


def helicsFederateGetState(fed: HelicsFederate) -> HelicsFederateState:
    """
    Get the current state of a federate.

    **Parameters**

    - **`fed`** - The federate to query.

    **Returns**: `helics.HelicsFederateState`.
    """
    f = loadSym("helicsFederateGetState")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFederateState(result)


def helicsFederateGetCoreObject(fed: HelicsFederate) -> HelicsCore:
    """
    Get the `helics.HelicsCore` associated with a federate.

    **Parameters**

    - **`fed`** - `helics.HelicsFederate`.

    **Returns**: `helics.HelicsCore`.
    """
    warnings.warn("This function is deprecated. Use `helicsFederateGetCore` instead.")
    return helicsFederateGetCore(fed)


def helicsFederateGetCore(fed: HelicsFederate) -> HelicsCore:
    """
    Get the `helics.HelicsCore` associated with a federate.

    **Parameters**

    - **`fed`** - `helics.HelicsFederate`.

    **Returns**: `helics.HelicsCore`.
    """
    try:
        f = loadSym("helicsFederateGetCoreObject")
    except AttributeError:
        f = loadSym("helicsFederateGetCore")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCore(result)


def helicsFederateRequestTime(fed: HelicsFederate, request_time: HelicsTime) -> HelicsTime:
    """
    Request the next time for federate execution.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    - **`request_time`** - The next requested time.

    **Returns**: `helics.HelicsTime`.
    """
    f = loadSym("helicsFederateRequestTime")
    err = helicsErrorInitialize()
    result = f(fed.handle, request_time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTimeAdvance(fed: HelicsFederate, time_delta: HelicsTime) -> HelicsTime:
    """
    Request the next time for federate execution.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    - **`time_delta`** - The requested amount of time to advance.

    **Returns**: `helics.HelicsTime`.
    """
    f = loadSym("helicsFederateRequestTimeAdvance")
    err = helicsErrorInitialize()
    result = f(fed.handle, time_delta, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestNextStep(fed: HelicsFederate) -> HelicsTime:
    """
    Request the next time step for federate execution.
    Feds should have setup the period or `minDelta` for this to work well but it will request the next time step which is the current time plus the minimum time step.

    **Parameters**

    - **`fed`** - The federate to make the request of.

    **Returns**: `helics.HelicsTime`.
    """
    f = loadSym("helicsFederateRequestNextStep")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTimeIterative(
    fed: HelicsFederate, request_time: HelicsTime, iterate: HelicsIterationRequest
) -> Tuple[HelicsTime, HelicsIterationResult]:
    """
    Request an iterative time.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    - **`request_time`** - The next desired time.
    - **`iterate`** - `helics.HelicsIterationRequest`, i.e. the requested iteration mode.

    **Returns**: `(helics.HelicsTime, helics.HelicsIterationResult)`.
    """
    f = loadSym("helicsFederateRequestTimeIterative")
    err = helicsErrorInitialize()
    out_iterate = ffi.new("helics_iteration_result *")
    result = f(fed.handle, request_time, HelicsIterationRequest(iterate), out_iterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result, HelicsIterationResult(out_iterate[0])


def helicsFederateRequestTimeAsync(fed: HelicsFederate, request_time: HelicsTime):
    """
    Request the next time for federate execution in an asynchronous call.
    Call `helics.helicsFederateRequestTimeComplete` to finish the call.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    - **`request_time`** - The next requested time.
    """
    f = loadSym("helicsFederateRequestTimeAsync")
    err = helicsErrorInitialize()
    f(fed.handle, request_time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeComplete(fed: HelicsFederate) -> HelicsTime:
    """
    Complete an asynchronous requestTime call.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    """
    f = loadSym("helicsFederateRequestTimeComplete")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateRequestTimeIterativeAsync(fed: HelicsFederate, request_time: HelicsTime, iterate: HelicsIterationRequest):
    """
    Request an iterative time through an asynchronous call.
    This call allows for finer grain control of the iterative process than `helics.helicsFederateRequestTime`. It takes a time and iteration request, and returns a time and iteration status. Call `helics.helicsFederateRequestTimeIterativeComplete` to finish the process.

    **Parameters**

    - **`fed`** - The federate to make the request of.
    - **`request_time`** - The next desired time.
    - **`iterate`** - `helics.HelicsIterationRequest`, i.e. the requested iteration mode.
    """
    f = loadSym("helicsFederateRequestTimeIterativeAsync")
    err = helicsErrorInitialize()
    f(fed.handle, request_time, HelicsIterationRequest(iterate), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeIterativeComplete(fed: HelicsFederate) -> Tuple[HelicsTime, HelicsIterationResult]:
    """
    Complete an iterative time request asynchronous call.

    **Parameters**

    - **`fed`** - The federate to make the request of.

    **Returns**: The iteration specification of the result.
    """
    f = loadSym("helicsFederateRequestTimeIterativeComplete")
    err = helicsErrorInitialize()
    out_iterate = ffi.new("helics_iteration_result *")
    result = f(fed.handle, out_iterate, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result, out_iterate


def helicsFederateGetName(fed: HelicsFederate) -> str:
    """
    Get the name of the federate.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` to query.

    **Returns**: A string with the name.
    """
    f = loadSym("helicsFederateGetName")
    result = f(fed.handle)
    return ffi.string(result).decode()


def helicsFederateSetTimeProperty(fed: HelicsFederate, time_property: int, time: HelicsTime):
    """
    Set a time based property for a federate.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` to set the property for.
    - **`time_property`** - A integer code for a time property.
    - **`time`** - The requested value of the property.
    """
    f = loadSym("helicsFederateSetTimeProperty")
    err = helicsErrorInitialize()
    f(fed.handle, time_property, time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetFlagOption(fed: HelicsFederate, flag: int, value: bool):
    """
    Set a flag for the federate.

    **Parameters**

    - **`fed`** - The federate to alter a flag for.
    - **`flag`** - The flag to change.
    - **`value`** - The new value of the flag. 0 for false, !=0 for true.
    """
    f = loadSym("helicsFederateSetFlagOption")
    err = helicsErrorInitialize()
    f(fed.handle, flag, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetSeparator(fed: HelicsFederate, separator: str):
    """
    Set the separator character in a federate.
    The separator character is the separation character for local publications/endpoints in creating their global name.
    For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.

    **Parameters**

    - **`fed`** - The federate info object to alter.
    - **`separator`** - The character to use as a separator.
    """
    f = loadSym("helicsFederateSetSeparator")
    err = helicsErrorInitialize()
    f(fed.handle, cchar(separator), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetIntegerProperty(fed: HelicsFederate, property: HelicsProperty, value: int):
    """
    Set an integer based property of a federate.

    **Parameters**

    - **`fed`** - The federate to change the property for.
    - **`property`** - `helics.HelicsProperty`.
    - **`value`** - The value of the property.
    """
    f = loadSym("helicsFederateSetIntegerProperty")
    err = helicsErrorInitialize()
    f(fed.handle, HelicsProperty(property), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetTimeProperty(fed: HelicsFederate, time_property: int) -> HelicsTime:
    """
    Get the current value of a time based property in a federate.

    **Parameters**

    - **`fed`** - The federate query.
    - **`time_property`** - The property to query.

    **Returns**: `helics.HelicsTime`.
    """
    f = loadSym("helicsFederateGetTimeProperty")
    err = helicsErrorInitialize()
    result = f(fed.handle, time_property, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetFlagOption(fed: HelicsFederate, flag: HelicsFederateFlag) -> bool:
    """
    Get a flag value for a federate.

    **Parameters**

    - **`fed`** - The federate to get the flag for.
    - **`flag`** - The `helics.HelicsFederateFlag` to query.
    """
    f = loadSym("helicsFederateGetFlagOption")
    err = helicsErrorInitialize()
    result = f(fed.handle, HelicsFederateFlag(flag), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsFederateGetIntegerProperty(fed: HelicsFederate, property: HelicsProperty) -> int:
    """
    Get the current value of an integer property (such as a logging level).

    **Parameters**

    - **`fed`** - The federate to get the flag for.
    - **`property`** - A code for the property to set `helics.HelicsProperty`.
    """
    f = loadSym("helicsFederateGetIntegerProperty")
    err = helicsErrorInitialize()
    result = f(fed.handle, HelicsProperty(property), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateGetCurrentTime(fed: HelicsFederate) -> HelicsTime:
    """
    Get the current time of the federate.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` to query.

    **Returns**: `helics.HelicsTime`.
    """
    f = loadSym("helicsFederateGetCurrentTime")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsFederateSetGlobal(fed: HelicsFederate, name: str, value: str):
    """
    Set a federation global value through a federate.
    This overwrites any previous value for this name.

    **Parameters**

    - **`fed`** - The federate to set the global through.
    - **`name`** - The name of the global to set.
    - **`value`** - The value of the global.
    """
    f = loadSym("helicsFederateSetGlobal")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(name), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateAddDependency(fed: HelicsFederate, name: str):
    """
    Add a time dependency for a federate. The federate will depend on the given named federate for time synchronization.

    **Parameters**

    - **`fed`** - The federate to add the dependency for.
    - **`name`** - The name of the federate to depend on.
    """
    f = loadSym("helicsFederateAddDependency")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetLogFile(fed: HelicsFederate, log_file: str):
    """
    Set the logging file for a federate (actually on the core associated with a federate).

    **Parameters**

    - **`fed`** - The federate to set the log file for.
    - **`log_file`** - The name of the log file.
    """
    f = loadSym("helicsFederateSetLogFile")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(log_file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogErrorMessage(fed: HelicsFederate, log_message: str):
    """
    Log an error message through a federate.

    **Parameters**

    - **`fed`** - The federate to log the error message through.
    - **`log_message`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogErrorMessage")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(log_message), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogWarningMessage(fed: HelicsFederate, log_message: str):
    """
    Log a warning message through a federate.

    **Parameters**

    - **`fed`** - The federate to log the warning message through.
    - **`log_message`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogWarningMessage")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(log_message), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogInfoMessage(fed: HelicsFederate, log_message: str):
    """
    Log an info message through a federate.

    **Parameters**

    - **`fed`** - The federate to log the info message through.
    - **`log_message`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogInfoMessage")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(log_message), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogDebugMessage(fed: HelicsFederate, log_message: str):
    """
    Log a debug message through a federate.

    **Parameters**

    - **`fed`** - The federate to log the debug message through.
    - **`log_message`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogDebugMessage")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(log_message), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogLevelMessage(fed: HelicsFederate, log_level: HelicsLogLevel, log_message: str):
    """
    Log a message through a federate.

    **Parameters**

    - **`fed`** - The federate to log the message through.
    - **`log_level`** - The level of the message to log see `helics.HelicsLogLevel`.
    - **`log_message`** - The message to put in the log.
    """
    f = loadSym("helicsFederateLogLevelMessage")
    err = helicsErrorInitialize()
    f(fed.handle, HelicsLogLevel(log_level), cstring(log_message), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetGlobal(core: HelicsCore, name: str, value: str):
    """
    Set a global value in a core.
    This overwrites any previous value for this name.

    **Parameters**

    - **`core`** - The core to set the global through.
    - **`name`** - The name of the global to set.
    - **`value`** - The value of the global.
    """
    f = loadSym("helicsCoreSetGlobal")
    err = helicsErrorInitialize()
    f(core.handle, cstring(name), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetGlobal(broker: HelicsBroker, name: str, value: str):
    """
    Set a federation global value.
    This overwrites any previous value for this name.

    **Parameters**

    - **`broker`** - The broker to set the global through.
    - **`name`** - The name of the global to set.
    - **`value`** - The value of the global.
    """
    f = loadSym("helicsBrokerSetGlobal")
    err = helicsErrorInitialize()
    f(broker.handle, cstring(name), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetLogFile(core: HelicsCore, log_file: str):
    """
    Set the log file on a core.

    **Parameters**

    - **`core`** - The core to set the log file for.
    - **`log_file`** - The name of the file to log to.
    """
    f = loadSym("helicsCoreSetLogFile")
    err = helicsErrorInitialize()
    f(core.handle, cstring(log_file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetLogFile(broker: HelicsBroker, log_file: str):
    """
    Set the log file on a broker.

    **Parameters**

    - **`broker`** - The broker to set the log file for.
    - **`log_file`** - The name of the file to log to.
    """
    f = loadSym("helicsBrokerSetLogFile")
    err = helicsErrorInitialize()
    f(broker.handle, cstring(log_file), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCreateQuery(target_name: str, query_string: str) -> HelicsQuery:
    """
    Create a query object.
    A query object consists of a target and query string.

    **Parameters**

    - **`target_name`** - The name of the target to query.
    - **`query_string`** - The query to make of the target.

    **Returns**: `helics.HelicsQuery`.
    """
    f = loadSym("helicsCreateQuery")
    result = f(cstring(target_name), cstring(query_string))
    return HelicsQuery(result)


def helicsQueryExecute(query: HelicsQuery, fed: HelicsFederate) -> str:
    """
    Execute a query.
    The call will block until the query finishes which may require communication or other delays.

    **Parameters**

    - **`query`** - The query object to use in the query.
    - **`fed`** - A federate to send the query through.

    **Returns**: String that contains the result of the query that was executed.
    """
    f = loadSym("helicsQueryExecute")
    err = helicsErrorInitialize()
    result = f(query.handle, fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        s = ffi.string(result).decode()
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return s


def helicsQueryCoreExecute(query: HelicsQuery, core: HelicsCore) -> Union[str, dict]:
    """
    Execute a query directly on a core.
    The call will block until the query finishes which may require communication or other delays.

    **Parameters**

    - **`query`** - The query object to use in the query.
    - **`core`** - The core to send the query to.

    **Returns**: String that contains the result of the query that was executed.
    """
    f = loadSym("helicsQueryCoreExecute")
    err = helicsErrorInitialize()
    result = f(query.handle, core.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        s = ffi.string(result).decode()
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return s


def helicsQueryBrokerExecute(query: HelicsQuery, broker: HelicsBroker) -> str:
    """
    Execute a query directly on a broker.
    The call will block until the query finishes which may require communication or other delays.

    **Parameters**

    - **`query`** - The query object to use in the query.
    - **`broker`** - The broker to send the query to.

    **Returns**: String that contains the result of the query that was executed.
    """
    f = loadSym("helicsQueryBrokerExecute")
    err = helicsErrorInitialize()
    result = f(query.handle, broker.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        s = ffi.string(result).decode()
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return s


def helicsQueryExecuteAsync(query: HelicsQuery, fed: HelicsFederate):
    """
    Execute a query in a non-blocking call.

    **Parameters**

    - **`query`** - The query object to use in the query.
    - **`fed`** - A federate to send the query through.
    """
    f = loadSym("helicsQueryExecuteAsync")
    err = helicsErrorInitialize()
    f(query.handle, fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryExecuteComplete(query: HelicsQuery) -> str:
    """
    Complete the return from a query called with `helics.helicsExecuteQueryAsync`.
    The function will block until the query completes `isQueryComplete` can be called to determine if a query has completed or not.

    **Parameters**

    - **`query`** - The query object to complete execution of.

    **Returns**: String that contains the result of the query that was executed.
    """
    f = loadSym("helicsQueryExecuteComplete")
    err = helicsErrorInitialize()
    result = f(query.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        s = ffi.string(result).decode()
        try:
            return json.loads(s)
        except json.JSONDecodeError:
            return s


def helicsQueryIsCompleted(query: HelicsQuery) -> bool:
    """
    Check if an asynchronously executed query has completed.
    This function should usually be called after a QueryExecuteAsync function has been called.

    **Parameters**

    - **`query`** - The query object to check if completed

    **Returns**: Will return `True` if an asynchronous query has completed or a regular query call was made with a result, and false if an asynchronous query has not completed or is invalid.
    """
    f = loadSym("helicsQueryIsCompleted")
    result = f(query.handle)
    return result == 1


def helicsQuerySetTarget(query: HelicsQuery, target_name: str):
    """
    Update the target of a query.

    **Parameters**

    - **`query`** - The query object to change the target of.
    - **`target_name`** - the name of the target to query.
    """
    f = loadSym("helicsQuerySetTarget")
    err = helicsErrorInitialize()
    f(query.handle, cstring(target_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQuerySetQueryString(query: HelicsQuery, query_string: str):
    """
    Update the queryString of a query.

    **Parameters**

    - **`query`** - The query object to change the target of.
    - **`query_string`** - the new queryString.
    """
    f = loadSym("helicsQuerySetQueryString")
    err = helicsErrorInitialize()
    f(query.handle, cstring(query_string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryFree(query: HelicsQuery):
    """
    Free the memory associated with a query object.
    """
    f = loadSym("helicsQueryFree")
    f(query.handle)


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

    - **`fed`** - The `helics.HelicsFederate` in which to create an endpoint must have been created with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    - **`name`** - The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
    - **`type`** - A string describing the expected type of the publication (optional).

    **Returns**: `helics.HelicsEndpoint`.
    """
    f = loadSym("helicsFederateRegisterEndpoint")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsEndpoint(result)


def helicsFederateRegisterGlobalEndpoint(fed: HelicsFederate, name: str, type: str = "") -> HelicsEndpoint:
    """
    Create an endpoint.
    The endpoint becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for endpoints.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create an endpoint must have been created with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    - **`name`** - The identifier for the endpoint.handle, the given name is the global identifier.
    - **`type`** - A string describing the expected type of the publication (optional).

    **Returns**: `helics.HelicsEndpoint`.
    """
    f = loadSym("helicsFederateRegisterGlobalEndpoint")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsEndpoint(result)


def helicsFederateGetEndpoint(fed: HelicsFederate, name: str) -> HelicsEndpoint:
    """
    Get an endpoint object from a name.

    **Parameters**

    - **`fed`** - The message `helics.HelicsFederate` to use to get the endpoint.
    - **`name`** - The name of the endpoint.

    **Returns**: `helics.HelicsEndpoint`.
    """
    f = loadSym("helicsFederateGetEndpoint")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsEndpoint(result)


def helicsFederateGetEndpointByIndex(fed: HelicsFederate, index: int) -> HelicsEndpoint:
    """
    Get an endpoint by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsEndpoint`.
    """
    f = loadSym("helicsFederateGetEndpointByIndex")
    err = helicsErrorInitialize()
    result = f(fed.handle, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsEndpoint(result)


def helicsEndpointIsValid(endpoint: HelicsEndpoint) -> bool:
    """
    Check if an endpoint is valid.

    **Parameters**

    - **`endpoint`** - The endpoint object to check.

    **Returns**: `True` if the Endpoint object represents a valid endpoint.
    """
    f = loadSym("helicsEndpointIsValid")
    result = f(endpoint.handle)
    return result == 1


def helicsEndpointSetDefaultDestination(endpoint: HelicsEndpoint, destination: str):
    """
    Set the default destination for an endpoint if no other endpoint is given.

    **Parameters**

    - **`endpoint`** - The endpoint to set the destination for.
    - **`destination`** - A string naming the desired default endpoint.
    """
    f = loadSym("helicsEndpointSetDefaultDestination")
    err = helicsErrorInitialize()
    f(endpoint.handle, cstring(destination), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetDefaultDestination(endpoint: HelicsEndpoint) -> str:
    """
    Get the default destination for an endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint to set the destination for.

    **Returns**: A string with the default destination.
    """
    f = loadSym("helicsEndpointGetDefaultDestination")
    result = f(endpoint.handle)
    return ffi.string(result).decode()


def helicsEndpointSendBytesTo(endpoint: HelicsEndpoint, data: bytes, destination: str):
    """
    Send a message to the specified destination.

    **Parameters**

    - **`endpoint`** - The endpoint to send the data from.
    - **`data`** - The data to send.
    - **`destination`** - The target destination.
    """
    try:
        f = loadSym("helicsEndpointSendBytesTo")
        err = helicsErrorInitialize()
        if isinstance(data, str):
            data = data.encode()
        if not isinstance(data, bytes):
            raise HelicsException(
                """Raw data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(
                    t=type(data)
                )
            )
        inputDataLength = len(data)
        f(endpoint.handle, data, inputDataLength, cstring(destination), err)
        if err.error_code != 0:
            raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    except AttributeError:
        f = loadSym("helicsEndpointSendMessageRaw")
        err = helicsErrorInitialize()
        if isinstance(data, str):
            data = data.encode()
        if not isinstance(data, bytes):
            raise HelicsException(
                """Raw data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(
                    t=type(data)
                )
            )
        inputDataLength = len(data)
        f(endpoint.handle, cstring(destination), data, inputDataLength, err)
        if err.error_code != 0:
            raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessageRaw(endpoint: HelicsEndpoint, destination: str, data: bytes):
    """
    Send a message to the specified destination.

    **Parameters**

    - **`endpoint`** - The endpoint to send the data from.
    - **`destination`** - The target destination.
    - **`data`** - The data to send.

    **DEPRECATED**

    Use `helicsEndpointSendBytesTo` instead
    """
    warnings.warn("This function is deprecated. Use `helicsEndpointSendBytesTo` instead.")
    helicsEndpointSendBytesTo(endpoint, data, destination)


def helicsEndpointSendBytesToAt(endpoint: HelicsEndpoint, data: bytes, destination: str, time: HelicsTime):
    """
    Send a message at a specific time to the specified destination.

    **Parameters**

    - **`endpoint`** - The endpoint to send the data from.
    - **`data`** - The data to send.
    - **`destination`** - The target destination.
    - **`time`** - The time the message should be sent.
    """
    try:
        f = loadSym("helicsEndpointSendBytesToAt")
        err = helicsErrorInitialize()
        inputDataLength = len(data)
        f(endpoint.handle, cstring(data), inputDataLength, cstring(destination), time, err)
        if err.error_code != 0:
            raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    except AttributeError:
        f = loadSym("helicsEndpointSendEventRaw")
        err = helicsErrorInitialize()
        inputDataLength = len(data)
        f(endpoint.handle, cstring(destination), cstring(data), inputDataLength, time, err)
        if err.error_code != 0:
            raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendEventRaw(
    endpoint: HelicsEndpoint, destination: str, data: bytes, time: HelicsTime,
):
    """
    Send a message at a specific time to the specified destination.

    **Parameters**

    - **`endpoint`** - The endpoint to send the data from.
    - **`destination`** - The target destination.
    - **`data`** - The data to send.
    - **`time`** - The time the message should be sent.

    **DEPRECATED**

    Use `helicsEndpointSendBytesToAt` instead.
    """
    warnings.warn("This function is deprecated. Use `helicsEndpointSendBytesToAt` instead.")
    helicsEndpointSendBytesToAt(endpoint, data, destination, time)


def helicsEndpointSendMessageObject(endpoint: HelicsEndpoint, message: HelicsMessage):
    """
    Send a message object from a specific endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint to send the data from.
    - **`message`** - The actual message to send which will be copied.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use `helicsEndpointSendMessage` instead.")
    return helicsEndpointSendMessage(endpoint)


def helicsEndpointSendMessageObjectZeroCopy(endpoint: HelicsEndpoint, message: HelicsMessage):
    """
    Send a message object from a specific endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint to send the data from.
    - **`message`** - The actual message to send which will be copied.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use `helicsEndpointSendMessage` instead.")
    return helicsEndpointSendMessage(endpoint)


def helicsEndpointSendMessage(endpoint: HelicsEndpoint, message: HelicsMessage):
    """
    Send a message object from a specific endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint to send the data from.
    - **`message`** - The actual message to send which will be copied.
    """
    try:
        f = loadSym("helicsEndpointSendMessageObject")
    except AttributeError:
        f = loadSym("helicsEndpointSendMessage")
    err = helicsErrorInitialize()
    f(endpoint.handle, message.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSubscribe(endpoint: HelicsEndpoint, key: str):
    """
    Subscribe an endpoint to a publication.

    **Parameters**

    - **`endpoint`** - The endpoint to use.
    - **`key`** - The name of the publication.
    """
    f = loadSym("helicsEndpointSubscribe")
    err = helicsErrorInitialize()
    f(endpoint.handle, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateHasMessage(fed: HelicsFederate) -> bool:
    """
    Check if the federate has any outstanding messages.

    **Parameters**

    - **`fed`** - The federate to check.

    **Returns**: `True` if the federate has a message waiting, `False` otherwise.
    """
    f = loadSym("helicsFederateHasMessage")
    result = f(fed.handle)
    return result == 1


def helicsEndpointHasMessage(endpoint: HelicsEndpoint) -> bool:
    """
    Check if a given endpoint has any unread messages.

    **Parameters**

    - **`endpoint`** - The endpoint to check.

    **Returns**: `True` if the endpoint has a message, `False` otherwise.
    """
    f = loadSym("helicsEndpointHasMessage")
    result = f(endpoint.handle)
    return result == 1


def helicsFederatePendingMessagesCount(fed: HelicsFederate) -> int:
    """
    Returns the number of pending receives for the specified destination endpoint.

    **Parameters**

    - **`fed`** - The federate to get the number of waiting messages from.
    """
    try:
        f = loadSym("helicsFederatePendingMessagesCount")
    except AttributeError:
        f = loadSym("helicsFederatePendingMessages")
    return f(fed.handle)


def helicsFederatePendingMessages(fed: HelicsFederate) -> int:
    """
    Returns the number of pending receives for the specified destination endpoint.

    **Parameters**

    - **`fed`** - The federate to get the number of waiting messages from.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use `helicsFederatePendingMessagesCount` instead.")
    return helicsFederatePendingMessagesCount(fed)


def helicsEndpointPendingMessages(endpoint: HelicsEndpoint) -> int:
    """
    Returns the number of pending receives for all endpoints of a particular federate.

    **Parameters**

    - **`endpoint`** - The endpoint to query.
    """
    warnings.warn("This function has been deprecated. Use `helicsEndpointPendingMessagesCount` instead.")
    return helicsEndpointPendingMessagesCount(endpoint)


def helicsEndpointPendingMessagesCount(endpoint: HelicsEndpoint) -> int:
    """
    Returns the number of pending receives for all endpoints of a particular federate.

    **Parameters**

    - **`endpoint`** - The endpoint to query.
    """
    try:
        f = loadSym("helicsEndpointPendingMessagesCount")
    except AttributeError:
        f = loadSym("helicsEndpointPendingMessages")
    return f(endpoint.handle)


def helicsEndpointGetMessageObject(endpoint: HelicsEndpoint) -> HelicsMessage:
    """
    Receive a packet from a particular endpoint.

    **Parameters**

    - **`endpoint`** - The identifier for the endpoint.

    **Returns**: A message.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use `helicsEndpointGetMessage` instead.")
    return helicsEndpointGetMessage(endpoint)


def helicsEndpointGetMessage(endpoint: HelicsEndpoint) -> HelicsMessage:
    """
    Receive a packet from a particular endpoint.

    **Parameters**

    - **`endpoint`** - The identifier for the endpoint.

    **Returns**: A message object.
    """
    try:
        f = loadSym("helicsEndpointGetMessageObject")
    except AttributeError:
        f = loadSym("helicsEndpointGetMessage")
    return HelicsMessage(f(endpoint.handle))


def helicsEndpointCreateMessageObject(endpoint: HelicsEndpoint) -> HelicsMessage:
    """
    Create a new empty message.
    The message is empty and isValid will return false since there is no data associated with the message yet.

    **Parameters**

    - **`endpoint`** - The endpoint object to associate the message with.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use `helicsEndpointCreateMessage` instead")
    return helicsEndpointCreateMessage(endpoint)


def helicsEndpointCreateMessage(endpoint: HelicsEndpoint) -> HelicsMessage:
    """
    Create a new empty message object.
    The message is empty and isValid will return false since there is no data associated with the message yet.

    **Parameters**

    - **`endpoint`** - The endpoint object to associate the message with.
    """
    try:
        f = loadSym("helicsEndpointCreateMessageObject")
    except AttributeError:
        f = loadSym("helicsEndpointCreateMessage")
    err = helicsErrorInitialize()
    result = f(endpoint.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsMessage(result)


def helicsFederateGetMessageObject(fed: HelicsFederate) -> HelicsMessage:
    """
    Receive a communication message for any endpoint in the federate.
    The return order will be in order of endpoint creation.
    So all messages that are available for the first endpoint.handle, then all for the second, and so on.
    Within a single endpoint.handle, the messages are ordered by time, then source_id, then order of arrival.

    **Returns**: A `helics.HelicsMessage` which references the data in the message.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use helicsFederateGetMessage instead")
    return helicsFederateGetMessage(fed)


def helicsFederateGetMessage(fed: HelicsFederate) -> HelicsMessage:
    """
    Receive a communication message for any endpoint in the federate.
    The return order will be in order of endpoint creation.
    So all messages that are available for the first endpoint.handle, then all for the second, and so on.
    Within a single endpoint.handle, the messages are ordered by time, then source_id, then order of arrival.

    **Returns**: A `helics.HelicsMessage` which references the data in the message.
    """
    try:
        f = loadSym("helicsFederateGetMessageObject")
    except AttributeError:
        f = loadSym("helicsFederateGetMessage")
    result = f(fed.handle)
    return HelicsMessage(result)


def helicsFederateCreateMessageObject(fed: HelicsFederate) -> HelicsMessage:
    """
    Create a new empty message object.
    The message is empty and isValid will return false since there is no data associated with the message yet.

    **Parameters**

    - **`fed`** - the `helics.HelicsFederate` to associate the message with.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use helicsFederateCreateMessage instead")
    return helicsFederateCreateMessage(fed)


def helicsFederateCreateMessage(fed: HelicsFederate) -> HelicsMessage:
    """
    Create a new empty message object.
    The message is empty and isValid will return false since there is no data associated with the message yet.

    **Parameters**

    - **`fed`** - the `helics.HelicsFederate` to associate the message with.
    """
    try:
        f = loadSym("helicsFederateCreateMessageObject")
    except AttributeError:
        f = loadSym("helicsFederateCreateMessage")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsMessage(result)


def helicsFederateClearMessages(fed: HelicsFederate):
    """
    Clear all stored messages from a federate.
    This clears messages retrieved through `helics.helicsFederateGetMessage` or `helics.helicsFederateGetMessageObject`.

    **Parameters**

    - **`fed`** - The federate to clear the message for.
    """
    f = loadSym("helicsFederateClearMessages")
    f(fed.handle)


def helicsEndpointClearMessages(endpoint: HelicsEndpoint):
    """
    Clear all message from an endpoint.

    _**Deprecated: Use `helics.helicsFederateClearMessages` to free all messages, or `helics.helicsMessageFree` to clear an individual message.

    **Parameters**

    - **`endpoint`** - The endpoint object to operate on.

    **DEPRECATED**
    """
    try:
        f = loadSym("helicsEndpointClearMessages")
        f(endpoint.handle)
    except AttributeError:
        warnings.warn("This function is deprecated. Clearing is handled at the federate level.")


def helicsEndpointGetType(endpoint: HelicsEndpoint) -> str:
    """
    Get the type specified for an endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint object in question.

    **Returns**: The defined type of the endpoint.
    """
    f = loadSym("helicsEndpointGetType")
    result = f(endpoint.handle)
    return ffi.string(result).decode()


def helicsEndpointGetName(endpoint: HelicsEndpoint) -> str:
    """
    Get the name of an endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint object in question.

    **Returns**: The name of the endpoint.
    """
    f = loadSym("helicsEndpointGetName")
    result = f(endpoint.handle)
    return ffi.string(result).decode()


def helicsFederateGetEndpointCount(fed: HelicsFederate) -> int:
    """
    Get the number of endpoints in a federate.

    **Parameters**

    - **`fed`** - The message federate to query.

    **Returns**: (-1) if fed was not a valid federate, otherwise returns the number of endpoints.
    """
    f = loadSym("helicsFederateGetEndpointCount")
    result = f(fed.handle)
    return result


def helicsEndpointGetInfo(endpoint: HelicsEndpoint) -> str:
    """
    Get the data in the info field of a filter.

    **Parameters**

    - **`end`** - The filter to query.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsEndpointGetInfo")
    result = f(endpoint.handle)
    return ffi.string(result).decode()


def helicsEndpointSetInfo(endpoint: HelicsEndpoint, info: str):
    """
    Set the data in the info field for a filter.

    **Parameters**

    - **`endpoint`** - The endpoint to query.
    - **`info`** - The string to set.
    """
    f = loadSym("helicsEndpointSetInfo")
    err = helicsErrorInitialize()
    f(endpoint.handle, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSetOption(endpoint: HelicsEndpoint, option: HelicsHandleOption, value: int):
    """
    Set a handle option on an endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint to modify.
    - **`option`** - Integer code for the option to set `helics.HelicsHandleOption`.
    - **`value`** - The value to set the option to.
    """
    f = loadSym("helicsEndpointSetOption")
    err = helicsErrorInitialize()
    f(endpoint.handle, HelicsHandleOption(option), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetOption(endpoint: HelicsEndpoint, option: HelicsHandleOption) -> int:
    """
    Get the value of handle option on an endpoint.

    **Parameters**

    - **`endpoint`** - The endpoint to modify.
    - **`option`** - Integer code for the option to set `helics.HelicsHandleOption`.

    **Returns**: the value of the option, for boolean options will be 0 or 1.
    """
    f = loadSym("helicsEndpointGetOption")
    result = f(endpoint.handle, HelicsHandleOption(option))
    return result


def helicsMessageGetSource(message: HelicsMessage) -> str:
    """
    Message operation functions.
    Functions for working with helics message envelopes.
    Get the source endpoint of a message.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: A string with the source endpoint.
    """
    f = loadSym("helicsMessageGetSource")
    result = f(message.handle)
    return ffi.string(result).decode()


def helicsMessageGetDestination(message: HelicsMessage) -> str:
    """
    Get the destination endpoint of a message.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: A string with the destination endpoint.
    """
    f = loadSym("helicsMessageGetDestination")
    result = f(message.handle)
    return ffi.string(result).decode()


def helicsMessageGetOriginalSource(message: HelicsMessage) -> str:
    """
    Get the original source endpoint of a message, the source may have been modified by filters or other actions.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: A string with the source of a message.
    """
    f = loadSym("helicsMessageGetOriginalSource")
    result = f(message.handle)
    return ffi.string(result).decode()


def helicsMessageGetOriginalDestination(message: HelicsMessage) -> str:
    """
    Get the original destination endpoint of a message, the destination may have been modified by filters or other actions.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: A string with the original destination of a message.
    """
    f = loadSym("helicsMessageGetOriginalDestination")
    result = f(message.handle)
    return ffi.string(result).decode()


def helicsMessageGetTime(message: HelicsMessage) -> HelicsTime:
    """
    Get the helics time associated with a message.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: The time associated with a message.
    """
    f = loadSym("helicsMessageGetTime")
    result = f(message.handle)
    return result


def helicsMessageGetString(message: HelicsMessage) -> str:
    """
    Get the payload of a message as a string.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: A string representing the payload of a message.
    """
    f = loadSym("helicsMessageGetString")
    result = f(message.handle)
    return ffi.string(result).decode()


def helicsMessageGetMessageID(message: HelicsMessage) -> int:
    """
    Get the messageID of a message.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: The messageID.
    """
    f = loadSym("helicsMessageGetMessageID")
    result = f(message.handle)
    return result


def helicsMessageGetFlagOption(message: HelicsMessage, flag: int) -> bool:
    """
    Get flag on a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`flag`** - The flag to check should be between [0,15].

    **Returns**: The flags associated with a message.
    """
    try:
        f = loadSym("helicsMessageGetFlagOption")
    except AttributeError:
        f = loadSym("helicsMessageCheckFlag")
    result = f(message.handle, flag)
    return result == 1


def helicsMessageCheckFlag(message: HelicsMessage, flag: int) -> bool:
    """
    Check if a flag is set on a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`flag`** - The flag to check should be between [0,15].

    **Returns**: The flags associated with a message.

    **DEPRECATED**
    """
    warnings.warn("This function is deprecated. Use `helicsMessageGetFlagOption` instead.")
    return helicsMessageGetFlagOption(message, flag)


def helicsMessageGetByteCount(message: HelicsMessage) -> int:
    """
    Get the size of the data payload in bytes.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: The size of the data payload.
    """
    try:
        f = loadSym("helicsMessageGetByteCount")
    except AttributeError:
        f = loadSym("helicsMessageGetRawDataSize")
    result = f(message.handle)
    return result


def helicsMessageGetRawDataSize(message: HelicsMessage) -> int:
    """
    Get the size of the data payload in bytes.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: The size of the data payload.

    **DEPRECATED**
    """
    warnings.warn("This function is deprecated. Use `helicsMessageGetByteCount` instead.")
    return helicsMessageGetByteCount(message)


def helicsMessageGetRawData(message: HelicsMessage) -> bytes:
    """
    Get the raw data for a message object.

    **Parameters**

    - **`message`** - A message object to get the data for.

    **Returns**: Raw string data.

    **DEPRECATED**
    """
    warnings.warn("This function is deprecated. Use `helicsMessageGetBytes` instead.")
    return helicsMessageGetBytes(message)


def helicsMessageGetBytes(message: HelicsMessage) -> bytes:
    """
    Get the raw data for a message object.

    **Parameters**

    - **`message`** - A message object to get the data for.

    **Returns**: Raw string data.
    """
    try:
        f = loadSym("helicsMessageGetBytes")
    except AttributeError:
        f = loadSym("helicsMessageGetRawData")
    err = helicsErrorInitialize()
    maxMessageLen = helicsMessageGetByteCount(message) + 1024
    data = ffi.new("char[{maxMessageLen}]".format(maxMessageLen=maxMessageLen))
    actualSize = ffi.new("int[1]")
    f(message.handle, data, maxMessageLen, actualSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    return ffi.string(data, maxlen=actualSize[0])


def helicsMessageGetRawDataPointer(message: HelicsMessage) -> pointer:
    """
    Get a pointer to the raw data of a message.

    **Parameters**

    - **`message`** - A message object to get the data for.

    **Returns**: A pointer to the raw data in memory, the pointer may be NULL if the message is not a valid message.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use `helicsMessageGetBytesPointer` instead.")
    return helicsMessageGetBytesPointer(message)


def helicsMessageGetBytesPointer(message: HelicsMessage) -> pointer:
    """
    Get a pointer to the raw data of a message.

    **Parameters**

    - **`message`** - A message object to get the data for.

    **Returns**: A pointer to the raw data in memory, the pointer may be NULL if the message is not a valid message.
    """
    try:
        f = loadSym("helicsMessageGetBytesPointer")
    except AttributeError:
        f = loadSym("helicsMessageGetRawDataPointer")
    result = f(message.handle)
    return result


def helicsMessageIsValid(message: HelicsMessage) -> bool:
    """
    A check if the message contains a valid payload.

    **Parameters**

    - **`message`** - The message object in question.

    **Returns**: `True` if the message contains a payload.
    """
    f = loadSym("helicsMessageIsValid")
    result = f(message.handle)
    return result == 1


def helicsMessageSetSource(message: HelicsMessage, source: str):
    """
    Set the source of a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`source`** - A string containing the source.
    """
    f = loadSym("helicsMessageSetSource")
    err = helicsErrorInitialize()
    f(message.handle, cstring(source), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetDestination(message: HelicsMessage, destination: str):
    """
    Set the destination of a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`destination`** - A string containing the new destination.
    """
    f = loadSym("helicsMessageSetDestination")
    err = helicsErrorInitialize()
    f(message.handle, cstring(destination), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalSource(message: HelicsMessage, source: str):
    """
    Set the original source of a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`source`** - A string containing the new original source.
    """
    f = loadSym("helicsMessageSetOriginalSource")
    err = helicsErrorInitialize()
    f(message.handle, cstring(source), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalDestination(message: HelicsMessage, destination: str):
    """
    Set the original destination of a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`destination`** - A string containing the new original source.
    """
    f = loadSym("helicsMessageSetOriginalDestination")
    err = helicsErrorInitialize()
    f(message.handle, cstring(destination), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetTime(message: HelicsMessage, time: HelicsTime):
    """
    Set the delivery time for a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`time`** - The time the message should be delivered.
    """
    f = loadSym("helicsMessageSetTime")
    err = helicsErrorInitialize()
    f(message.handle, time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageResize(message: HelicsMessage, new_size: int):
    """
    Resize the data buffer for a message.
    The message data buffer will be resized. There are no guarantees on what is in the buffer in newly allocated space.
    If the allocated space is not sufficient new allocations will occur

    **Parameters**

    - **`message`** - The message object in question.
    - **`new_size`** - The new size in bytes of the buffer.
    """
    f = loadSym("helicsMessageResize")
    err = helicsErrorInitialize()
    f(message.handle, new_size, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageReserve(message: HelicsMessage, reserve_size: int):
    """
    Reserve space in a buffer but don't actually resize.
    The message data buffer will be reserved but not resized.

    **Parameters**

    - **`message`** - The message object in question.
    - **`reserve_size`** - The number of bytes to reserve in the message object.
    """
    f = loadSym("helicsMessageReserve")
    err = helicsErrorInitialize()
    f(message.handle, reserve_size, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetMessageID(message: HelicsMessage, message_id: int):
    """
    Set the message ID for the message.
    Normally this is not needed and the core of HELICS will adjust as needed.

    **Parameters**

    - **`message`** - The message object in question.
    - **`message_id`** - A new message ID.
    """
    f = loadSym("helicsMessageSetMessageID")
    err = helicsErrorInitialize()
    f(message.handle, message_id, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClearFlags(message: HelicsMessage):
    """
    Clear the flags of a message.

    **Parameters**

    - **`message`** - The message object in question.
    """
    f = loadSym("helicsMessageClearFlags")
    f(message.handle)


def helicsMessageSetFlagOption(message: HelicsMessage, flag: int, value: bool):
    """
    Set a flag on a message.

    **Parameters**

    - **`message`** - The message object in question.
    - **`flag`** - An index of a flag to set on the message.
    - **`value`** - The desired value of the flag.
    """
    f = loadSym("helicsMessageSetFlagOption")
    err = helicsErrorInitialize()
    f(message.handle, flag, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetString(message: HelicsMessage, string: str):
    """
    Set the data payload of a message as a string.

    **Parameters**

    - **`message`** - The message object in question.
    - **`string`** - A string containing the message data.
    """
    f = loadSym("helicsMessageSetString")
    err = helicsErrorInitialize()
    f(message.handle, cstring(string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetData(message: HelicsMessage, data: bytes):
    """
    Set the data payload of a message as raw data.

    **Parameters**

    - **`message`** - The message object in question.
    - **`data`** - A string containing the message data.
    """
    f = loadSym("helicsMessageSetData")
    err = helicsErrorInitialize()
    if isinstance(data, str):
        data = data.encode()
    if not isinstance(data, bytes):
        raise HelicsException(
            """Raw data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data))
        )
    inputDataLength = len(data)
    f(message.handle, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageAppendData(message: HelicsMessage, data: bytes):
    """
    Append data to the payload.

    **Parameters**

    - **`message`** - The message object in question.
    - **`data`** - A string containing the message data to append.
    """
    f = loadSym("helicsMessageAppendData")
    err = helicsErrorInitialize()
    if isinstance(data, str):
        data = data.encode()
    if not isinstance(data, bytes):
        raise HelicsException(
            """Raw data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data))
        )
    inputDataLength = len(data)
    f(message.handle, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageCopy(source_message: HelicsMessage, destination_message: HelicsMessage):
    """
    Copy a message object.

    **Parameters**

    - **`source_message`** - The message object to copy from.
    - **`destination_message`** - The message object to copy to.
    """
    f = loadSym("helicsMessageCopy")
    err = helicsErrorInitialize()
    f(source_message, destination_message, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClone(message: HelicsMessage) -> HelicsMessage:
    """
    Clone a message object.

    **Parameters**

    - **`message`** - The message object to copy from.

    **Returns**: `helics.HelicsMessage`.
    """
    f = loadSym("helicsMessageClone")
    err = helicsErrorInitialize()
    result = f(message.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsMessage(result)


def helicsMessageFree(message: HelicsMessage):
    """
    Free a message object from memory. Memory for message is managed so not using this function does not create memory leaks, this is an indication to the system that the memory for this message is done being used and can be reused for a new message.
    `helics.helicsFederateClearMessages` can also be used to clear up all stored messages at once.
    """
    f = loadSym("helicsMessageFree")
    f(message.handle)


def helicsFederateRegisterFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a source Filter on the specified federate.
    Filters can be created through a federate or a core.handle, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

    **Parameters**

    - **`fed`** - The federate to register through.
    - **`type`** - The type of filter to create `helics.HelicsFilterType`.
    - **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateRegisterFilter")
    err = helicsErrorInitialize()
    result = f(fed.handle, HelicsFilterType(type), cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFilter(result)


def helicsFederateRegisterGlobalFilter(fed: HelicsFederate, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a global source filter through a federate.
    Filters can be created through a federate or a core.handle, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

    **Parameters**

    - **`fed`** - The federate to register through.
    - **`type`** - The type of filter to create `helics.HelicsFilterType`.
    - **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateRegisterGlobalFilter")
    err = helicsErrorInitialize()
    result = f(fed.handle, HelicsFilterType(type), cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFilter(result)


def helicsFederateRegisterCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Create a cloning Filter on the specified federate.
    Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

    **Parameters**

    - **`fed`** - The federate to register through.
    - **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateRegisterCloningFilter")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCloningFilter(result)


def helicsFederateRegisterGlobalCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Create a global cloning Filter on the specified federate.
    Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

    **Parameters**

    - **`fed`** - The federate to register through.
    - **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateRegisterGlobalCloningFilter")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsCloningFilter(result)


def helicsCoreRegisterFilter(core: HelicsCore, type: HelicsFilterType, name: str) -> HelicsFilter:
    """
    Create a source Filter on the specified core.
    Filters can be created through a federate or a core.handle, linking through a federate allows a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

    **Parameters**

    - **`core`** - The core to register through.
    - **`type`** - The type of filter to create `helics.HelicsFilterType`.
    - **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsCoreRegisterFilter")
    err = helicsErrorInitialize()
    result = f(core.handle, HelicsFilterType(type), cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFilter(result)


def helicsCoreRegisterCloningFilter(core: HelicsCore, name: str) -> HelicsFilter:
    """
    Create a cloning Filter on the specified core.
    Cloning filters copy a message and send it to multiple locations, source and destination can be added through other functions.

    **Parameters**

    - **`core`** - The core to register through.
    - **`name`** - The name of the filter (can be NULL).

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsCoreRegisterCloningFilter")
    err = helicsErrorInitialize()
    result = f(core.handle, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFilter(result)


def helicsFederateGetFilterCount(fed: HelicsFederate) -> int:
    """
    Get the number of filters registered through a federate.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` to use to get the filter.

    **Returns**: A count of the number of filters registered through a federate.
    """
    f = loadSym("helicsFederateGetFilterCount")
    result = f(fed.handle)
    return result


def helicsFederateGetFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
    """
    Get a filter by its name, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` to use to get the filter.
    - **`name`** - The name of the filter.

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateGetFilter")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFilter(result)


def helicsFederateGetFilterByIndex(fed: HelicsFederate, index: int) -> HelicsFilter:
    """
    Get a filter by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsFilter`.
    """
    f = loadSym("helicsFederateGetFilterByIndex")
    err = helicsErrorInitialize()
    result = f(fed.handle, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsFilter(result)


def helicsFilterIsValid(filter: HelicsFilter) -> bool:
    """
    Check if a filter is valid.

    **Parameters**

    - **`filter`** - The filter object to check.

    **Returns**: `True` if the Filter object represents a valid filter.
    """
    f = loadSym("helicsFilterIsValid")
    result = f(filter.handle)
    return result == 1


def helicsFilterGetName(filter: HelicsFilter) -> str:
    """
    Get the name of the filter and store in the given string.

    **Parameters**

    - **`filter`** - The given filter.

    **Returns**: A string with the name of the filter.
    """
    f = loadSym("helicsFilterGetName")
    result = f(filter.handle)
    return ffi.string(result).decode()


def helicsFilterSet(filter: HelicsFilter, property: str, value: float):
    """
    Set a property on a filter.

    **Parameters**

    - **`filter`** - The filter to modify.
    - **`property`** - A string containing the property to set.
    - **`value`** - A numerical value for the property.
    """
    f = loadSym("helicsFilterSet")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(property), cdouble(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetString(filter: HelicsFilter, property: str, value: str):
    """
    Set a string property on a filter.

    **Parameters**

    - **`filter`** - The filter to modify.
    - **`property`** - A string containing the property to set.
    - **`value`** - A string containing the new value.
    """
    f = loadSym("helicsFilterSetString")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(property), cstring(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDestinationTarget(filter: HelicsFilter, destination: str):
    """
    Add a destination target to a filter.
    All messages going to a destination are copied to the delivery address(es).

    **Parameters**

    - **`filter`** - The given filter to add a destination target to.
    - **`destination`** - The name of the endpoint to add as a destination target.
    """
    f = loadSym("helicsFilterAddDestinationTarget")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(destination), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddSourceTarget(filter: HelicsFilter, source_name: str):
    """
    Add a source target to a filter.
    All messages coming from a source are copied to the delivery address(es).

    **Parameters**

    - **`filter`** - The given filter.
    - **`source_name`** - The name of the endpoint to add as a source target.
    """
    f = loadSym("helicsFilterAddSourceTarget")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(source_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDeliveryEndpoint(filter: HelicsFilter, delivery_endpoint: str):
    """
    Clone filter functions.
    Functions that manipulate cloning filters in some way.
    Add a delivery endpoint to a cloning filter.
    All cloned messages are sent to the delivery address(es).

    **Parameters**

    - **`filter`** - The given filter.
    - **`delivery_endpoint`** - The name of the endpoint to deliver messages to.
    """
    f = loadSym("helicsFilterAddDeliveryEndpoint")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(delivery_endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveTarget(filter: HelicsFilter, target_name: str):
    """
    Remove a destination target from a filter.

    **Parameters**

    - **`filter`** - The given filter.
    - **`target_name`** - The named endpoint to remove as a target.
    """
    f = loadSym("helicsFilterRemoveTarget")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(target_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveDeliveryEndpoint(filter: HelicsFilter, delivery_endpoint: str):
    """
    Remove a delivery destination from a cloning filter.

    **Parameters**

    - **`filter`** - The given filter (must be a cloning filter).
    - **`delivery_endpoint`** - A string with the delivery endpoint to remove.
    """
    f = loadSym("helicsFilterRemoveDeliveryEndpoint")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(delivery_endpoint), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetInfo(filter: HelicsFilter) -> str:
    """
    Get the data in the info field of a filter.

    **Parameters**

    - **`filter`** - The given filter.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsFilterGetInfo")
    result = f(filter.handle)
    return ffi.string(result).decode()


def helicsFilterSetInfo(filter: HelicsFilter, info: str):
    """
    Set the data in the info field for a filter

    **Parameters**

    - **`filter`** - The given filter.
    - **`info`** - The string to set.
    """
    f = loadSym("helicsFilterSetInfo")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetOption(filter: HelicsFilter, option: HelicsHandleOption, value: int):
    """
    Set the data in the info field for a filter.

    **Parameters**

    - **`filter`** - The given filter.
    - **`option`** - The option to set `helics.HelicsHandleOption`.
    - **`value`** - The value of the option commonly 0 for false 1 for true.
    """
    f = loadSym("helicsFilterSetOption")
    err = helicsErrorInitialize()
    f(filter.handle, HelicsHandleOption(option), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetOption(filter: HelicsFilter, option: HelicsHandleOption) -> int:
    """
    Get a handle option for the filter.

    **Parameters**

    - **`filter`** - The given filter to query.
    - **`option`** - The option to query `helics.HelicsHandleOption`.

    **Returns**: `int`.
    """
    f = loadSym("helicsFilterGetOption")
    result = f(filter.handle, HelicsHandleOption(option))
    return result


def helicsFederateRegisterSubscription(fed: HelicsFederate, key: str, units: str = "") -> HelicsInput:
    """
    Functions related to value federates for the C api.
    Create a subscription.
    The subscription becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a subscription, must have been created with `helics.helicsCreateValueFederate` or
    `helics.helicsCreateCombinationFederate`.
    - **`key`** - The identifier matching a publication to get a subscription for.
    - **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsSubscription`.
    """
    f = loadSym("helicsFederateRegisterSubscription")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsInput(result)


def helicsFederateRegisterPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication:
    """
    Register a publication with a known type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`key`** - The identifier for the publication the global publication key will be prepended with the federate name.
    - **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    - **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterPublication")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsPublication(result)


def helicsFederateRegisterTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a publication with a defined type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`key`** - The identifier for the publication.
    - **`type`** - A string labeling the type of the publication.
    - **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterTypePublication")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsPublication(result)


def helicsFederateRegisterGlobalPublication(fed: HelicsFederate, key: str, type: HelicsDataType, units: str = "") -> HelicsPublication:
    """
    Register a global named publication with an arbitrary type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`key`** - The identifier for the publication.
    - **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    - **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterGlobalPublication")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsPublication(result)


def helicsFederateRegisterGlobalTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
    """
    Register a global publication with a defined type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`key`** - The identifier for the publication.
    - **`type`** - A string describing the expected type of the publication.
    - **`units`** - A string listing the units of the subscription (optional).

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterGlobalTypePublication")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsPublication(result)


def helicsFederateRegisterInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsInput:
    """
    Register a named input.
    The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions, inputs, and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create an input.
    - **`key`** - The identifier for the publication the global input key will be prepended with the federate name.
    - **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    - **`units`** - A string listing the units of the input (optional).

    **Returns**: `helics.HelicsInput`.
    """
    f = loadSym("helicsFederateRegisterInput")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsInput(result)


def helicsFederateRegisterTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsInput:
    """
    Register an input with a defined type.
    The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
    functions for subscriptions, inputs, and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create an input.
    - **`key`** - The identifier for the input.
    - **`type`** - A string describing the expected type of the input.
    - **`units`** - A string listing the units of the input maybe NULL.

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterTypeInput")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsInput(result)


def helicsFederateRegisterGlobalInput(fed: HelicsFederate, key: str, type: HelicsDataType, units: str) -> HelicsPublication:
    """
    Register a global named input.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`key`** - The identifier for the publication.
    - **`type`** - A code identifying the type of the input see `helics.HelicsDataType` for available options.
    - **`units`** - A string listing the units of the subscription maybe NULL.

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterGlobalInput")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), HelicsDataType(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsPublication(result)


def helicsFederateRegisterGlobalTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsInput:
    """
    Register a global publication with an arbitrary type.
    The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for subscriptions and publications.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`key`** - The identifier for the publication.
    - **`type`** - A string defining the type of the input.
    - **`units`** - A string listing the units of the subscription maybe NULL.

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateRegisterGlobalTypeInput")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), cstring(type), cstring(units), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsInput(result)


def helicsFederateGetPublication(fed: HelicsFederate, key: str) -> HelicsPublication:
    """
    Get a `helics.HelicsPublication` from a key.

    **Parameters**

    - **`fed`** - The value `helics.HelicsFederate` to use to get the publication.
    - **`key`** - The name of the publication.

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateGetPublication")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsPublication(result)


def helicsFederateGetPublicationByIndex(fed: HelicsFederate, index: int) -> HelicsPublication:
    """
    Get a publication by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsPublication`.
    """
    f = loadSym("helicsFederateGetPublicationByIndex")
    err = helicsErrorInitialize()
    result = f(fed.handle, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsPublication(result)


def helicsFederateGetInput(fed: HelicsFederate, key: str) -> HelicsInput:
    """
    Get an input object from a key.

    **Parameters**

    - **`fed`** - The value `helics.HelicsFederate` to use to get the publication.
    - **`key`** - The name of the input.

    **Returns**: `helics.HelicsInput`.
    """
    f = loadSym("helicsFederateGetInput")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsInput(result)


def helicsFederateGetInputByIndex(fed: HelicsFederate, index: int) -> HelicsInput:
    """
    Get an input by its index, typically already created via registerInterfaces file or something of that nature.

    **Parameters**

    - **`fed`** - The `helics.HelicsFederate` in which to create a publication.
    - **`index`** - The index of the publication to get.

    **Returns**: `helics.HelicsInput`
    """
    f = loadSym("helicsFederateGetInputByIndex")
    err = helicsErrorInitialize()
    result = f(fed.handle, index, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsInput(result)


def helicsFederateGetSubscription(fed: HelicsFederate, key: str) -> HelicsInput:
    """
    Get an input object from a subscription target.

    **Parameters**

    - **`fed`** - The value `helics.HelicsFederate` to use to get the publication.
    - **`key`** - The name of the publication that a subscription is targeting.

    **Returns**: `helics.HelicsInput`
    """
    f = loadSym("helicsFederateGetSubscription")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(key), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsInput(result)


def helicsFederateClearUpdates(fed: HelicsFederate):
    """
    Clear all the update flags from a federates inputs.

    **Parameters**

    - **`fed`** - The value `helics.HelicsFederate` for which to clear update flags.
    """
    f = loadSym("helicsFederateClearUpdates")
    f(fed.handle)


def helicsFederateRegisterFromPublicationJSON(fed: HelicsFederate, json: str):
    """
    Register the publications via JSON publication string.

    **Parameters**

    - **`fed`** - The value `helics.HelicsFederate` to use to register the publications.
    - **`json`** - The JSON publication string.
    """
    f = loadSym("helicsFederateRegisterFromPublicationJSON")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederatePublishJSON(fed: HelicsFederate, json: str):
    """
    Publish data contained in a JSON file or string.

    **Parameters**

    - **`fed`** - The value `helics.HelicsFederate` through which to publish the data.
    - **`json`** - The publication file name or literal JSON data string.
    """
    f = loadSym("helicsFederatePublishJSON")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(json), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationIsValid(pub: HelicsPublication) -> bool:
    """
    Publication functions.
    Functions for publishing data of various kinds.
    The data will get translated to the type specified when the publication was constructed automatically regardless of the function used to publish the data.
    Check if a publication is valid.

    **Parameters**

    - **`pub`** - The publication to check

    **Returns**: `True` if the publication is a valid publication.
    """
    f = loadSym("helicsPublicationIsValid")
    result = f(pub.handle)
    return result == 1


def helicsPublicationPublishRaw(pub: HelicsPublication, data: bytes):
    """
    Publish raw data from a char * and length.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`data`** - A pointer to the raw data.

    **DEPRECATED**
    """
    warnings.warn("This function is deprecated. Use `helicsPublicationPublishBytes` instead.")
    helicsPublicationPublishBytes(pub, data)


def helicsPublicationPublishBytes(pub: HelicsPublication, data: bytes):
    """
    Publish raw data from a char * and length.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`data`** - A pointer to the raw data.
    """
    try:
        f = loadSym("helicsPublicationPublishBytes")
    except AttributeError:
        f = loadSym("helicsPublicationPublishRaw")
    err = helicsErrorInitialize()
    if isinstance(data, str):
        data = data.encode()
    if not isinstance(data, bytes):
        raise HelicsException(
            """Raw data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data))
        )
    inputDataLength = len(data)
    f(pub.handle, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishString(pub: HelicsPublication, string: str):
    """
    Publish a string.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`string`** - The string to publish.
    """
    f = loadSym("helicsPublicationPublishString")
    err = helicsErrorInitialize()
    f(pub.handle, cstring(string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishInteger(pub: HelicsPublication, value: int):
    """
    Publish an integer value.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`value`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishInteger")
    err = helicsErrorInitialize()
    f(pub.handle, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishBoolean(pub: HelicsPublication, value: bool):
    """
    Publish a Boolean Value.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`value`** - The boolean value to publish.
    """
    f = loadSym("helicsPublicationPublishBoolean")
    err = helicsErrorInitialize()
    f(pub.handle, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishDouble(pub: HelicsPublication, value: float):
    """
    Publish a double floating point value.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`value`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishDouble")
    err = helicsErrorInitialize()
    f(pub.handle, cdouble(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishTime(pub: HelicsPublication, value: HelicsTime):
    """
    Publish a time value.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`value`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishTime")
    err = helicsErrorInitialize()
    f(pub.handle, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishChar(pub: HelicsPublication, value: str):
    """
    Publish a single character.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`value`** - The numerical value to publish.
    """
    f = loadSym("helicsPublicationPublishChar")
    err = helicsErrorInitialize()
    f(pub.handle, cchar(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishComplex(pub: HelicsPublication, real: float, imag: float = 0):
    """
    Publish a complex value (or pair of values).

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`real`** - `float` number or `complex` number
    - **`imag`** - `float` number
    """
    c = complex(real, imag)
    f = loadSym("helicsPublicationPublishComplex")
    err = helicsErrorInitialize()
    f(pub.handle, c.real, c.imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishVector(pub: HelicsPublication, vectorInput: List[float]):
    """
    Publish a vector of doubles.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`vectorInput`** - A pointer to an array of double data.
    """
    f = loadSym("helicsPublicationPublishVector")
    err = helicsErrorInitialize()
    vectorLength = len(vectorInput)
    f(pub.handle, vectorInput, vectorLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishNamedPoint(pub: HelicsPublication, string: str, value: float):
    """
    Publish a named point.

    **Parameters**

    - **`pub`** - The publication to publish for.
    - **`string`** - A string for the name to publish.
    - **`value`** - A double for the value to publish.
    """
    f = loadSym("helicsPublicationPublishNamedPoint")
    err = helicsErrorInitialize()
    f(pub.handle, cstring(string), cdouble(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationAddTarget(pub: HelicsPublication, target_name: str):
    """
    Add a named input to the list of targets a publication publishes to.

    **Parameters**

    - **`pub`** - The publication to add the target for.
    - **`target_name`** - The name of an input that the data should be sent to.
    """
    f = loadSym("helicsPublicationAddTarget")
    err = helicsErrorInitialize()
    f(pub.handle, cstring(target_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsValid(ipt: HelicsInput) -> bool:
    """
    Check if an input is valid.

    **Parameters**

    - **`ipt`** - The input to check

    **Returns**: `True` if the Input object represents a valid input.
    """
    f = loadSym("helicsInputIsValid")
    result = f(ipt.handle)
    return result == 1


def helicsInputAddTarget(ipt: HelicsInput, target_name: str):
    """
    Add a publication to the list of data that an input subscribes to.

    **Parameters**

    - **`ipt`** - The named input to modify.
    - **`target_name`** - The name of a publication that an input should subscribe to.
    """
    f = loadSym("helicsInputAddTarget")
    err = helicsErrorInitialize()
    f(ipt.handle, cstring(target_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetRawValueSize(ipt: HelicsInput) -> int:
    """
    Data can be returned in a number of formats,  for instance if data is published as a double it can be returned as a string and vice versa,  not all translations make that much sense but they do work.
    Get the size of the raw value for subscription.

    **Returns**: The size of the raw data/string in bytes.

    **DEPRECATED**
    """
    warnings.warn("This function is deprecated. Use `helicsInputGetByteCount` instead.")
    return helicsInputGetByteCount(ipt)


def helicsInputGetByteCount(ipt: HelicsInput) -> int:
    """
    Data can be returned in a number of formats,  for instance if data is published as a double it can be returned as a string and vice versa,  not all translations make that much sense but they do work.
    Get the size of the raw value for subscription.

    **Returns**: The size of the raw data/string in bytes.
    """
    try:
        f = loadSym("helicsInputGetByteCount")
    except AttributeError:
        f = loadSym("helicsInputGetRawValueSize")
    result = f(ipt.handle)
    return result


def helicsInputGetRawValue(ipt: HelicsInput) -> bytes:
    """
    Get the raw data for the latest value of a subscription.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: Raw string data.

    **DEPRECATED**
    """
    warnings.warn("This function is deprecated. Use `helicsInputGetBytes` instead.")
    return helicsInputGetBytes(ipt)


def helicsInputGetBytes(ipt: HelicsInput) -> bytes:
    """
    Get the raw data for the latest value of a subscription.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: Raw string data.
    """
    try:
        f = loadSym("helicsInputGetBytes")
    except AttributeError:
        f = loadSym("helicsInputGetRawValue")
    err = helicsErrorInitialize()
    maxDataLen = helicsInputGetByteCount(ipt) + 1024
    data = ffi.new("char[{maxDataLen}]".format(maxDataLen=maxDataLen))
    actualSize = ffi.new("int[1]")
    f(ipt.handle, data, maxDataLen, actualSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(data, maxlen=actualSize[0])


def helicsInputGetStringSize(ipt: HelicsInput) -> int:
    """
    Get the size of a value for subscription assuming return as a string.

    **Returns**: The size of the string.
    """
    f = loadSym("helicsInputGetStringSize")
    result = f(ipt.handle)
    return result


def helicsInputGetString(ipt: HelicsInput) -> str:
    """
    Get a string value from a subscription.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: A string data
    """
    f = loadSym("helicsInputGetString")
    err = helicsErrorInitialize()
    maxStringLen = helicsInputGetStringSize(ipt) + 1024
    outputString = ffi.new("char[{maxStringLen}]".format(maxStringLen=maxStringLen))
    actualLength = ffi.new("int[1]")
    f(ipt.handle, outputString, maxStringLen, actualLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(outputString, maxlen=actualLength[0]).decode()


def helicsInputGetInteger(ipt: HelicsInput) -> int:
    """
    Get an integer value from a subscription.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: An int64_t value with the current value of the input.
    """
    f = loadSym("helicsInputGetInteger")
    err = helicsErrorInitialize()
    result = f(ipt.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsInputGetBoolean(ipt: HelicsInput) -> bool:
    """
    Get a boolean value from a subscription.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: A boolean value of current input value.
    """
    f = loadSym("helicsInputGetBoolean")
    err = helicsErrorInitialize()
    result = f(ipt.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result == 1


def helicsInputGetDouble(ipt: HelicsInput) -> float:
    """
    Get a double value from a subscription..

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: The double value of the input.
    """
    f = loadSym("helicsInputGetDouble")
    err = helicsErrorInitialize()
    result = f(ipt.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsInputGetTime(ipt: HelicsInput) -> HelicsTime:
    """
    Get a time value from a subscription.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: The resulting time value.
    """
    f = loadSym("helicsInputGetTime")
    err = helicsErrorInitialize()
    result = f(ipt.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return result


def helicsInputGetChar(ipt: HelicsInput) -> str:
    """
    Get a single character value from an input.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: The resulting character value.
    """
    f = loadSym("helicsInputGetChar")
    err = helicsErrorInitialize()
    result = f(ipt.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        # TODO: this is a char, will ffi.string conversion work?
        return result.decode()


def helicsInputGetComplexObject(ipt: HelicsInput) -> Tuple[float, float]:
    """
    Get a complex object from an input object.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: `complex`.
    """
    f = loadSym("helicsInputGetComplexObject")
    err = helicsErrorInitialize()
    result = f(ipt.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        warnings.warn("This function will return a complex number in the next major release")
        return (result.real, result.imag)


def helicsInputGetComplex(ipt: HelicsInput) -> Tuple[float, float]:
    """
    Get a pair of double forming a complex number from a subscriptions.

    **Parameters**

    - **`ipt`** - The input to get the data for.

    **Returns**: a pair of floating point values that represent the real and imag values
    """
    f = loadSym("helicsInputGetComplex")
    err = helicsErrorInitialize()
    real = ffi.new("double *")
    imag = ffi.new("double *")
    f(ipt.handle, real, imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        warnings.warn("This function will return a complex number in the next major release")
        return (real[0], imag[0])


def helicsInputGetVectorSize(ipt: HelicsInput) -> int:
    """
    Get the size of a value for subscription assuming return as an array of doubles.

    **Returns**: The number of doubles in a returned vector.
    """
    f = loadSym("helicsInputGetVectorSize")
    result = f(ipt.handle)
    return result


def helicsInputGetVector(ipt: HelicsInput) -> List[float]:
    """
    Get a vector from a subscription.

    **Parameters**

    - **`ipt`** - The input to get the result for.

    **Returns**: a list of floating point values
    """
    f = loadSym("helicsInputGetVector")
    err = helicsErrorInitialize()
    maxlen = helicsInputGetVectorSize(ipt) + 1024
    data = ffi.new("double[{maxlen}]".format(maxlen=maxlen))
    actualSize = ffi.new("int[1]")
    f(ipt.handle, data, maxlen, actualSize, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return [x for x in data][0 : actualSize[0]]


def helicsInputGetNamedPoint(ipt: HelicsInput) -> Tuple[str, float]:
    """
    Get a named point from a subscription.

    **Parameters**

    - **`ipt`** - The input to get the result for.

    **Returns**: a string and a double value for the named point
    """
    f = loadSym("helicsInputGetNamedPoint")
    err = helicsErrorInitialize()
    maxStringLen = helicsInputGetStringSize(ipt) + 1024
    outputString = ffi.new("char[{maxStringLen}]".format(maxStringLen=maxStringLen))
    actualLength = ffi.new("int[1]")
    value = ffi.new("double[1]")
    f(ipt.handle, outputString, maxStringLen, actualLength, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(outputString, maxlen=actualLength[0]).decode(), value[0]


def helicsInputSetDefaultRaw(ipt: HelicsInput, data: bytes):
    """

    Default Value functions.
    These functions set the default value for a subscription. That is the value returned if nothing was published from elsewhere.
    Set the default as a raw data array.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`data`** - A pointer to the raw data to use for the default.

    **DEPRECATED**
    """
    warnings.warn("This function has been deprecated. Use `helicsInputSetDefaultRaw` instead.")
    helicsInputSetDefaultBytes(ipt, data)


def helicsInputSetDefaultBytes(ipt: HelicsInput, data: bytes):
    """

    Default Value functions.
    These functions set the default value for a subscription. That is the value returned if nothing was published from elsewhere.
    Set the default as a raw data array.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`data`** - A pointer to the raw data to use for the default.
    """
    try:
        f = loadSym("helicsInputSetDefaultBytes")
    except AttributeError:
        f = loadSym("helicsInputSetDefaultRaw")
    err = helicsErrorInitialize()
    if isinstance(data, str):
        data = data.encode()
    if not isinstance(data, bytes):
        raise HelicsException(
            """Raw data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data))
        )
    inputDataLength = len(data)
    f(ipt.handle, data, inputDataLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultString(ipt: HelicsInput, string: str):
    """
    Set the default as a string.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`string`** - A pointer to the default string.
    """
    f = loadSym("helicsInputSetDefaultString")
    err = helicsErrorInitialize()
    f(ipt.handle, cstring(string), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultInteger(ipt: HelicsInput, value: int):
    """
    Set the default as an integer.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`value`** - The default integer.
    """
    f = loadSym("helicsInputSetDefaultInteger")
    err = helicsErrorInitialize()
    f(ipt.handle, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultBoolean(ipt: HelicsInput, value: bool):
    """
    Set the default as a boolean.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`value`** - The default boolean value.
    """
    f = loadSym("helicsInputSetDefaultBoolean")
    err = helicsErrorInitialize()
    f(ipt.handle, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultTime(ipt: HelicsInput, value: HelicsTime):
    """
    Set the default as a time.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`value`** - The default time value.
    """
    f = loadSym("helicsInputSetDefaultTime")
    err = helicsErrorInitialize()
    f(ipt.handle, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultChar(ipt: HelicsInput, value: str):
    """
    Set the default as a char.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`value`** - The default char value.
    """
    f = loadSym("helicsInputSetDefaultChar")
    err = helicsErrorInitialize()
    f(ipt.handle, cchar(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultDouble(ipt: HelicsInput, value: float):
    """
    Set the default as a double.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`value`** - The default double value.
    """
    f = loadSym("helicsInputSetDefaultDouble")
    err = helicsErrorInitialize()
    f(ipt.handle, value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultComplex(ipt: HelicsInput, real: float, imag: float = 0):
    """
    Set the default as a complex number.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`real`** - The default real value.
    - **`imag`** - The default imaginary value.
    """
    c = complex(real, imag)
    f = loadSym("helicsInputSetDefaultComplex")
    err = helicsErrorInitialize()
    f(ipt.handle, c.real, c.imag, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultVector(ipt: HelicsInput, vectorInput: List[float]):
    """
    Set the default as a vector of doubles.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`vectorInput`** - A pointer to an array of double data.
    """
    f = loadSym("helicsInputSetDefaultVector")
    err = helicsErrorInitialize()
    vectorLength = len(vectorInput)
    f(ipt.handle, vectorInput, vectorLength, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultNamedPoint(ipt: HelicsInput, string: str, value: float):
    """
    Set the default as a `NamedPoint`.

    **Parameters**

    - **`ipt`** - The input to set the default for.
    - **`string`** - A pointer to a string representing the name.
    - **`value`** - A double value for the value of the named point.
    """
    f = loadSym("helicsInputSetDefaultNamedPoint")
    err = helicsErrorInitialize()
    f(ipt.handle, cstring(string), cdouble(value), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetType(ipt: HelicsInput) -> str:
    """
    Get the type of an input.

    **Parameters**

    - **`ipt`** - The input to query

    **Returns**: A string with the type information.
    """
    f = loadSym("helicsInputGetType")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsInputGetPublicationType(ipt: HelicsInput) -> str:
    """
    Get the type the publisher to an input is sending.

    **Parameters**

    - **`ipt`** - The input to query

    **Returns**: A string with the type information.
    """
    f = loadSym("helicsInputGetPublicationType")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsPublicationGetType(pub: HelicsPublication) -> str:
    """
    Get the type of a publication.

    **Parameters**

    - **`pub`** - The publication to query

    **Returns**: A string with the publication type information.
    """
    f = loadSym("helicsPublicationGetType")
    result = f(pub.handle)
    return ffi.string(result).decode()


def helicsInputGetKey(ipt: HelicsInput) -> str:
    """
    Get the key of an input.

    **Parameters**

    - **`ipt`** - The input to query

    **Returns**: A string with the key information.
    """
    f = loadSym("helicsInputGetKey")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsSubscriptionGetKey(ipt: HelicsInput) -> str:
    """
    Get the key of a subscription.

    **Returns**: A string with the subscription key.
    """
    f = loadSym("helicsSubscriptionGetKey")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsPublicationGetKey(pub: HelicsPublication) -> str:
    """
    Get the key of a publication.
    This will be the global key used to identify the publication to the federation.

    **Parameters**

    - **`pub`** - The publication to query.

    **Returns**: A string with the units information.
    """
    f = loadSym("helicsPublicationGetKey")
    result = f(pub.handle)
    return ffi.string(result).decode()


def helicsInputGetUnits(ipt: HelicsInput) -> str:
    """
    Get the units of an input.

    **Parameters**

    - **`ipt`** - The input to query.

    **Returns**: A string with the units information.
    """
    f = loadSym("helicsInputGetUnits")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsInputGetInjectionUnits(ipt: HelicsInput) -> str:
    """
    Get the units of the publication that an input is linked to.

    **Parameters**

    - **`ipt`** - The input to query.

    **Returns**: A string with the units information.
    """
    f = loadSym("helicsInputGetInjectionUnits")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsInputGetExtractionUnits(ipt: HelicsInput) -> str:
    """
    Get the units of an input.
    The same as `helics.helicsInputGetUnits`.

    **Parameters**

    - **`ipt`** - The input to query.

    **Returns**: A string with the units information.
    """
    f = loadSym("helicsInputGetExtractionUnits")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsPublicationGetUnits(pub: HelicsPublication) -> str:
    """
    Get the units of a publication.

    **Parameters**

    - **`pub`** - The publication to query.

    **Returns**: A string with the units information.
    """
    f = loadSym("helicsPublicationGetUnits")
    result = f(pub.handle)
    return ffi.string(result).decode()


def helicsInputGetInfo(ipt: HelicsInput) -> str:
    """
    Get the data in the info field of an input.

    **Parameters**

    - **`ipt`** - The input to query.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsInputGetInfo")
    result = f(ipt.handle)
    return ffi.string(result).decode()


def helicsInputSetInfo(ipt: HelicsInput, info: str):
    """
    Set the data in the info field for an input.

    **Parameters**

    - **`ipt`** - The input to query.
    - **`info`** - The string to set.
    """
    f = loadSym("helicsInputSetInfo")
    err = helicsErrorInitialize()
    f(ipt.handle, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetInfo(pub: HelicsPublication) -> str:
    """
    Get the data in the info field of an publication.

    **Parameters**

    - **`pub`** - The publication to query.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsPublicationGetInfo")
    result = f(pub.handle)
    return ffi.string(result).decode()


def helicsPublicationSetInfo(pub: HelicsPublication, info: str):
    """
    Set the data in the info field for a publication.

    **Parameters**

    - **`pub`** - The publication to set the info field for.
    - **`info`** - The string to set.
    """
    f = loadSym("helicsPublicationSetInfo")
    err = helicsErrorInitialize()
    f(pub.handle, cstring(info), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetOption(ipt: HelicsInput, option: HelicsHandleOption) -> int:
    """
    Get the current value of an input handle option.

    **Parameters**

    - **`ipt`** - The input to query.
    - **`option`** - Integer representation of the option in question see `helics.HelicsHandleOption`.

    **Returns**: An integer value with the current value of the given option.
    """
    f = loadSym("helicsInputGetOption")
    result = f(ipt.handle, HelicsHandleOption(option))
    return result


def helicsInputSetOption(ipt: HelicsInput, option: HelicsHandleOption, value: int):
    """
    Set an option on an input.

    **Parameters**

    - **`ipt`** - The input to query.
    - **`option`** - The option to set for the input `helics.HelicsHandleOption`.
    - **`value`** - The value to set the option to.
    """
    f = loadSym("helicsInputSetOption")
    err = helicsErrorInitialize()
    f(ipt.handle, HelicsHandleOption(option), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetOption(pub: HelicsPublication, option: HelicsHandleOption) -> int:
    """
    Get the value of an option for a publication.

    **Parameters**

    - **`pub`** - The publication to query.
    - **`option`** - The value to query see `helics.HelicsHandleOption`.

    **Returns**: A string with the info field string.
    """
    f = loadSym("helicsPublicationGetOption")
    result = f(pub.handle, HelicsHandleOption(option))
    return result


def helicsPublicationSetOption(pub: HelicsPublication, option: HelicsHandleOption, value: int):
    """
    Set the value of an option for a publication.

    **Parameters**

    - **`pub`** - The publication to query.
    - **`option`** - Integer code for the option to set `helics.HelicsHandleOption`.
    - **`value`** - The value to set the option to.
    """
    f = loadSym("helicsPublicationSetOption")
    err = helicsErrorInitialize()
    f(pub.handle, HelicsHandleOption(option), value, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationSetMinimumChange(pub: HelicsPublication, tolerance: float):
    """
    Set the minimum change detection tolerance.

    **Parameters**

    - **`pub`** - The publication to modify.
    - **`tolerance`** - The tolerance level for publication, values changing less than this value will not be published.
    """
    f = loadSym("helicsPublicationSetMinimumChange")
    err = helicsErrorInitialize()
    f(pub.handle, cdouble(tolerance), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetMinimumChange(ipt: HelicsInput, tolerance: float):
    """
    Set the minimum change detection tolerance.

    **Parameters**

    - **`ipt`** - The input to modify.
    - **`tolerance`** - The tolerance level for registering an update, values changing less than this value will not show asbeing updated.
    """
    f = loadSym("helicsInputSetMinimumChange")
    err = helicsErrorInitialize()
    f(ipt.handle, cdouble(tolerance), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsUpdated(ipt: HelicsInput) -> bool:
    """
    Check if a particular subscription was updated.

    **Returns**: `True` if it has been updated since the last value retrieval.
    """
    f = loadSym("helicsInputIsUpdated")
    result = f(ipt.handle)
    return result == 1


def helicsInputLastUpdateTime(ipt: HelicsInput) -> HelicsTime:
    """
    Get the last time a subscription was updated.
    """
    f = loadSym("helicsInputLastUpdateTime")
    result = f(ipt.handle)
    return result


def helicsInputClearUpdate(ipt: HelicsInput):
    """
    Clear the updated flag from an input.
    """
    f = loadSym("helicsInputClearUpdate")
    f(ipt.handle)


def helicsFederateGetPublicationCount(fed: HelicsFederate) -> int:
    """
    Get the number of publications in a federate.

    **Returns**: (-1) if fed was not a valid federate otherwise returns the number of publications.
    """
    f = loadSym("helicsFederateGetPublicationCount")
    result = f(fed.handle)
    return result


def helicsFederateGetInputCount(fed: HelicsFederate) -> int:
    """
    Get the number of subscriptions in a federate.

    **Returns**: (-1) if fed was not a valid federate otherwise returns the number of subscriptions.
    """
    f = loadSym("helicsFederateGetInputCount")
    result = f(fed.handle)
    return result


def helicsFederateSetLoggingCallback(fed: HelicsFederate, logger, user_data):
    """
    Set the logging callback for a `helics.HelicsFederate`

    Add a logging callback function for the C.
    The logging callback will be called when a message flows into a `helics.HelicsFederate` from the core or from a federate.

    # Parameters

    - **`fed`**: the `helics.HelicsFederate` that is created with `helics.helicsCreateValueFederate`, `helics.helicsCreateMessageFederate` or `helics.helicsCreateCombinationFederate`
    - **`logger`**: a callback with signature void(int, const char *, const char *, void *); the function arguments are loglevel, an identifier string, and a message string, and a pointer to user data
    - **`user_data`**: a pointer to user data that is passed to the function when executing
    """
    f = loadSym("helicsFederateSetLoggingCallback")
    err = helicsErrorInitialize()
    f(fed.handle, logger, user_data, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetCustomCallback(filter: HelicsFilter, callback, userdata):
    f = loadSym("helicsFilterSetCustomCallback")
    err = helicsErrorInitialize()
    f(filter.handle, callback, userdata, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerClearTimeBarrier(broker: HelicsBroker):
    f = loadSym("helicsBrokerClearTimeBarrier")
    f(broker.handle)


def helicsBrokerSetTimeBarrier(broker: HelicsBroker, barrier_time: HelicsTime):
    """
    Set the broker time barrier

    # Parameters

    - **`broker`**: the `helics.HelicsBroker`
    - **`barrier_time`**: the barrier time
    """
    f = loadSym("helicsBrokerSetTimeBarrier")
    err = helicsErrorInitialize()
    f(broker.handle, barrier_time, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSendCommand(fed: HelicsFederate, target: str, command: str):
    f = loadSym("helicsFederateSendCommand")
    err = helicsErrorInitialize()
    f(fed.handle, cstring(target), cstring(command), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetCommand(fed: HelicsFederate) -> str:
    f = loadSym("helicsFederateGetCommand")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsFederateGetCommandSource(fed: HelicsFederate) -> str:
    f = loadSym("helicsFederateGetCommandSource")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsFederateWaitCommand(fed: HelicsFederate) -> str:
    f = loadSym("helicsFederateWaitCommand")
    err = helicsErrorInitialize()
    result = f(fed.handle, err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return ffi.string(result).decode()


def helicsCoreSendCommand(core, target, command, err):
    f = loadSym("helicsCoreSendCommand")
    err = helicsErrorInitialize()
    f(core.handle, cstring(target), cstring(command), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSendCommand(broker, target, command, err):
    f = loadSym("helicsBrokerSendCommand")
    err = helicsErrorInitialize()
    f(broker.handle, cstring(target), cstring(command), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRegisterTargetedEndpoint(fed: HelicsFederate, name: str, type: str):
    """
    Create an targeted endpoint.
    The endpoint becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for endpoints.
    # Parameters
    - **`fed`** - The `helics.HelicsFederate` in which to create an endpoint must have been created with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    - **`name`** - The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
    - **`type`** - A string describing the expected type of the publication (optional).
    **Returns**: `helics.HelicsEndpoint`.
    """
    f = loadSym("helicsFederateRegisterTargetedEndpoint")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsEndpoint(result)


def helicsFederateRegisterGlobalTargetedEndpoint(fed: HelicsFederate, name: str, type: str):
    """
    Create a globally targeted endpoint.
    The endpoint becomes part of the federate and is destroyed when the federate is freed so there are no separate free functions for endpoints.
    # Parameters
    - **`fed`** - The `helics.HelicsFederate` in which to create an endpoint must have been created with helicsCreateMessageFederate or helicsCreateCombinationFederate.
    - **`name`** - The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
    - **`type`** - A string describing the expected type of the publication (optional).
    **Returns**: `helics.HelicsEndpoint`.
    """
    f = loadSym("helicsFederateGlobalRegisterTargetedEndpoint")
    err = helicsErrorInitialize()
    result = f(fed.handle, cstring(name), cstring(type), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
    else:
        return HelicsEndpoint(result)


def helicsEndpointAddSourceTarget(endpoint: HelicsEndpoint, source_name: str):
    """
    Add a source target to a endpoint.
    All messages coming from a source are copied to the delivery address(es).
    # Parameters
    - **`endpoint`** - The given endpoint.
    - **`source_name`** - The name of the endpoint to add as a source target.
    """
    f = loadSym("helicsEndpointAddSourceTarget")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(source_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointAddDestinationTarget(endpoint: HelicsEndpoint, destination_name: str):
    """
    Add a destination target to a endpoint.
    All messages coming from a source are copied to the delivery address(es).
    # Parameters
    - **`endpoint`** - The given endpoint.
    - **`source_name`** - The name of the endpoint to add as a source target.
    """
    f = loadSym("helicsEndpointAddDestinationTarget")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(destination_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointRemoveTarget(endpoint: HelicsEndpoint, target: str):
    """
    Remove target from endpoint
    # Parameters
    - **`endpoint`** - The given endpoint.
    - **`target_name`** - The name of the endpoint to remove.
    """
    f = loadSym("helicsEndpointAddRemoveTarget")
    err = helicsErrorInitialize()
    f(filter.handle, cstring(target), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointAddSourceFilter(endpoint: HelicsEndpoint, filter_name: str):
    """
    Add source filter to endpoint
    # Parameters
    - **`endpoint`** - The endpoint.
    - **`filter_name`** - The name of the filter.
    """
    f = loadSym("helicsEndpointAddSourceFilter")
    err = helicsErrorInitialize()
    f(endpoint.handle, cstring(filter_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointAddDestinationFilter(endpoint: HelicsEndpoint, filter_name: str):
    """
    Add destination filter to endpoint
    # Parameters
    - **`endpoint`** - The endpoint.
    - **`filter_name`** - The name of the filter.
    """
    f = loadSym("helicsEndpointAddDestinationFilter")
    err = helicsErrorInitialize()
    f(endpoint.handle, cstring(filter_name), err)
    if err.error_code != 0:
        raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
