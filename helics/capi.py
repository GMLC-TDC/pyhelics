import enum
import signal
import sys
try:
	from typing import List, Tuple, Union
except ImportError:
	pass

from . import _build


lib = _build.lib
ffi = _build.ffi


def signal_handler(sig, frame):
	helicsCloseLibrary()
	print("User pressed 'CTRL-C'. Exiting...")
	sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class _HelicsCHandle:
	def __init__(self, handle):
		self.handle = handle


class HelicsException(Exception):
	pass


class HelicsCoreTypes(enum.IntEnum):
	""" pick a core type depending on compile configuration usually either ZMQ if available or TCP

	Attributes:
		HELICS_CORE_TYPE_DEFAULT: value:0	a default core type that will default to something available
		HELICS_CORE_TYPE_ZMQ: value:1	use the Zero MQ networking protocol
		HELICS_CORE_TYPE_MPI: value:2	use MPI for operation on a parallel cluster
		HELICS_CORE_TYPE_TEST: value:3	use the Test core if all federates are in the same process
		HELICS_CORE_TYPE_INTERPROCESS: value:4	interprocess uses memory mapped files to transfer data (for use when all federates are on the same machine
		HELICS_CORE_TYPE_IPC: value:5	interprocess uses memory mapped files to transfer data (for use when all federates are on the same machine ipc is the same as /ref HELICS_CORE_TYPE_interprocess
		HELICS_CORE_TYPE_TCP: value:6	use a generic TCP protocol message stream to send messages
		HELICS_CORE_TYPE_UDP: value:7	use UDP packets to send the data
		HELICS_CORE_TYPE_ZMQ_SS: value:10	single socket version of ZMQ core usually for high fed count on the same system
		HELICS_CORE_TYPE_NNG: value:9	for using the nanomsg communications
		HELICS_CORE_TYPE_TCP_SS: value:11	a single socket version of the TCP core for more easily handling firewalls
		HELICS_CORE_TYPE_HTTP: value:12	a core type using http for communication
		HELICS_CORE_TYPE_WEBSOCKET: value:14	a core using websockets for communication
		HELICS_CORE_TYPE_INPROC: value:18	an in process core type for handling communications in shared memory it is pretty similar to the test core but stripped from the "test" components
		HELICS_CORE_TYPE_NULL: value:66	an explicit core type that is recognized but explicitly doesn't exist, for testing and a few other assorted reasons
		HELICS_CORE_TYPE_EMPTY: value:77	an explicit core type exists but does nothing but return empty values or sink calls
	"""

	HELICS_CORE_TYPE_DEFAULT = 0
	HELICS_CORE_TYPE_ZMQ = 1
	HELICS_CORE_TYPE_MPI = 2
	HELICS_CORE_TYPE_TEST = 3
	HELICS_CORE_TYPE_INTERPROCESS = 4
	HELICS_CORE_TYPE_IPC = 5
	HELICS_CORE_TYPE_TCP = 6
	HELICS_CORE_TYPE_UDP = 7
	HELICS_CORE_TYPE_ZMQ_SS = 10
	HELICS_CORE_TYPE_NNG = 9
	HELICS_CORE_TYPE_TCP_SS = 11
	HELICS_CORE_TYPE_HTTP = 12
	HELICS_CORE_TYPE_WEBSOCKET = 14
	HELICS_CORE_TYPE_INPROC = 18
	HELICS_CORE_TYPE_NULL = 66
	HELICS_CORE_TYPE_EMPTY = 77


HELICS_CORE_TYPE_DEFAULT = HelicsCoreTypes.HELICS_CORE_TYPE_DEFAULT
HELICS_CORE_TYPE_ZMQ = HelicsCoreTypes.HELICS_CORE_TYPE_ZMQ
HELICS_CORE_TYPE_MPI = HelicsCoreTypes.HELICS_CORE_TYPE_MPI
HELICS_CORE_TYPE_TEST = HelicsCoreTypes.HELICS_CORE_TYPE_TEST
HELICS_CORE_TYPE_INTERPROCESS = HelicsCoreTypes.HELICS_CORE_TYPE_INTERPROCESS
HELICS_CORE_TYPE_IPC = HelicsCoreTypes.HELICS_CORE_TYPE_IPC
HELICS_CORE_TYPE_TCP = HelicsCoreTypes.HELICS_CORE_TYPE_TCP
HELICS_CORE_TYPE_UDP = HelicsCoreTypes.HELICS_CORE_TYPE_UDP
HELICS_CORE_TYPE_ZMQ_SS = HelicsCoreTypes.HELICS_CORE_TYPE_ZMQ_SS
HELICS_CORE_TYPE_NNG = HelicsCoreTypes.HELICS_CORE_TYPE_NNG
HELICS_CORE_TYPE_TCP_SS = HelicsCoreTypes.HELICS_CORE_TYPE_TCP_SS
HELICS_CORE_TYPE_HTTP = HelicsCoreTypes.HELICS_CORE_TYPE_HTTP
HELICS_CORE_TYPE_WEBSOCKET = HelicsCoreTypes.HELICS_CORE_TYPE_WEBSOCKET
HELICS_CORE_TYPE_INPROC = HelicsCoreTypes.HELICS_CORE_TYPE_INPROC
HELICS_CORE_TYPE_NULL = HelicsCoreTypes.HELICS_CORE_TYPE_NULL
HELICS_CORE_TYPE_EMPTY = HelicsCoreTypes.HELICS_CORE_TYPE_EMPTY

helics_core_type_default = HelicsCoreTypes.HELICS_CORE_TYPE_DEFAULT
helics_core_type_zmq = HelicsCoreTypes.HELICS_CORE_TYPE_ZMQ
helics_core_type_mpi = HelicsCoreTypes.HELICS_CORE_TYPE_MPI
helics_core_type_test = HelicsCoreTypes.HELICS_CORE_TYPE_TEST
helics_core_type_interprocess = HelicsCoreTypes.HELICS_CORE_TYPE_INTERPROCESS
helics_core_type_ipc = HelicsCoreTypes.HELICS_CORE_TYPE_IPC
helics_core_type_tcp = HelicsCoreTypes.HELICS_CORE_TYPE_TCP
helics_core_type_udp = HelicsCoreTypes.HELICS_CORE_TYPE_UDP
helics_core_type_zmq_ss = HelicsCoreTypes.HELICS_CORE_TYPE_ZMQ_SS
helics_core_type_nng = HelicsCoreTypes.HELICS_CORE_TYPE_NNG
helics_core_type_tcp_ss = HelicsCoreTypes.HELICS_CORE_TYPE_TCP_SS
helics_core_type_http = HelicsCoreTypes.HELICS_CORE_TYPE_HTTP
helics_core_type_websocket = HelicsCoreTypes.HELICS_CORE_TYPE_WEBSOCKET
helics_core_type_inproc = HelicsCoreTypes.HELICS_CORE_TYPE_INPROC
helics_core_type_null = HelicsCoreTypes.HELICS_CORE_TYPE_NULL
helics_core_type_empty = HelicsCoreTypes.HELICS_CORE_TYPE_EMPTY


class HelicsDataTypes(enum.IntEnum):
	""" enumeration of allowable data types for publications and inputs

	Attributes:
		HELICS_DATA_TYPE_UNKNOWN: value:-1	
		HELICS_DATA_TYPE_STRING: value:0	a sequence of characters
		HELICS_DATA_TYPE_DOUBLE: value:1	a double precision floating point number
		HELICS_DATA_TYPE_INT: value:2	a 64 bit integer
		HELICS_DATA_TYPE_COMPLEX: value:3	a pair of doubles representing a complex number
		HELICS_DATA_TYPE_VECTOR: value:4	an array of doubles
		HELICS_DATA_TYPE_COMPLEX_VECTOR: value:5	a complex vector object
		HELICS_DATA_TYPE_NAMED_POINT: value:6	a named point consisting of a string and a double
		HELICS_DATA_TYPE_BOOLEAN: value:7	a boolean data type
		HELICS_DATA_TYPE_TIME: value:8	time data type
		HELICS_DATA_TYPE_RAW: value:25	raw data type
		HELICS_DATA_TYPE_JSON: value:30	type converts to a valid json string
		HELICS_DATA_TYPE_MULTI: value:33	the data type can change
		HELICS_DATA_TYPE_ANY: value:25262	open type that can be anything
	"""

	HELICS_DATA_TYPE_UNKNOWN = -1
	HELICS_DATA_TYPE_STRING = 0
	HELICS_DATA_TYPE_DOUBLE = 1
	HELICS_DATA_TYPE_INT = 2
	HELICS_DATA_TYPE_COMPLEX = 3
	HELICS_DATA_TYPE_VECTOR = 4
	HELICS_DATA_TYPE_COMPLEX_VECTOR = 5
	HELICS_DATA_TYPE_NAMED_POINT = 6
	HELICS_DATA_TYPE_BOOLEAN = 7
	HELICS_DATA_TYPE_TIME = 8
	HELICS_DATA_TYPE_RAW = 25
	HELICS_DATA_TYPE_JSON = 30
	HELICS_DATA_TYPE_MULTI = 33
	HELICS_DATA_TYPE_ANY = 25262


HELICS_DATA_TYPE_UNKNOWN = HelicsDataTypes.HELICS_DATA_TYPE_UNKNOWN
HELICS_DATA_TYPE_STRING = HelicsDataTypes.HELICS_DATA_TYPE_STRING
HELICS_DATA_TYPE_DOUBLE = HelicsDataTypes.HELICS_DATA_TYPE_DOUBLE
HELICS_DATA_TYPE_INT = HelicsDataTypes.HELICS_DATA_TYPE_INT
HELICS_DATA_TYPE_COMPLEX = HelicsDataTypes.HELICS_DATA_TYPE_COMPLEX
HELICS_DATA_TYPE_VECTOR = HelicsDataTypes.HELICS_DATA_TYPE_VECTOR
HELICS_DATA_TYPE_COMPLEX_VECTOR = HelicsDataTypes.HELICS_DATA_TYPE_COMPLEX_VECTOR
HELICS_DATA_TYPE_NAMED_POINT = HelicsDataTypes.HELICS_DATA_TYPE_NAMED_POINT
HELICS_DATA_TYPE_BOOLEAN = HelicsDataTypes.HELICS_DATA_TYPE_BOOLEAN
HELICS_DATA_TYPE_TIME = HelicsDataTypes.HELICS_DATA_TYPE_TIME
HELICS_DATA_TYPE_RAW = HelicsDataTypes.HELICS_DATA_TYPE_RAW
HELICS_DATA_TYPE_JSON = HelicsDataTypes.HELICS_DATA_TYPE_JSON
HELICS_DATA_TYPE_MULTI = HelicsDataTypes.HELICS_DATA_TYPE_MULTI
HELICS_DATA_TYPE_ANY = HelicsDataTypes.HELICS_DATA_TYPE_ANY

helics_data_type_unknown = HelicsDataTypes.HELICS_DATA_TYPE_UNKNOWN
helics_data_type_string = HelicsDataTypes.HELICS_DATA_TYPE_STRING
helics_data_type_double = HelicsDataTypes.HELICS_DATA_TYPE_DOUBLE
helics_data_type_int = HelicsDataTypes.HELICS_DATA_TYPE_INT
helics_data_type_complex = HelicsDataTypes.HELICS_DATA_TYPE_COMPLEX
helics_data_type_vector = HelicsDataTypes.HELICS_DATA_TYPE_VECTOR
helics_data_type_complex_vector = HelicsDataTypes.HELICS_DATA_TYPE_COMPLEX_VECTOR
helics_data_type_named_point = HelicsDataTypes.HELICS_DATA_TYPE_NAMED_POINT
helics_data_type_boolean = HelicsDataTypes.HELICS_DATA_TYPE_BOOLEAN
helics_data_type_time = HelicsDataTypes.HELICS_DATA_TYPE_TIME
helics_data_type_raw = HelicsDataTypes.HELICS_DATA_TYPE_RAW
helics_data_type_json = HelicsDataTypes.HELICS_DATA_TYPE_JSON
helics_data_type_multi = HelicsDataTypes.HELICS_DATA_TYPE_MULTI
helics_data_type_any = HelicsDataTypes.HELICS_DATA_TYPE_ANY


class HelicsFederateFlags(enum.IntEnum):
	""" enumeration of possible federate flags

	Attributes:
		HELICS_FLAG_OBSERVER: value:0	flag indicating that a federate is observe only
		HELICS_FLAG_UNINTERRUPTIBLE: value:1	flag indicating that a federate can only return requested times
		HELICS_FLAG_INTERRUPTIBLE: value:2	flag indicating that a federate can be interrupted
		HELICS_FLAG_SOURCE_ONLY: value:4	flag indicating that a federate/interface is a signal generator only
		HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE: value:6	flag indicating a federate/interface should only transmit values if they have changed(binary equivalence)
		HELICS_FLAG_ONLY_UPDATE_ON_CHANGE: value:8	flag indicating a federate/interface should only trigger an update if a value has changed (binary equivalence)
		HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE: value:10	flag indicating a federate should only grant time if all other federates have already passed the requested time
		HELICS_FLAG_RESTRICTIVE_TIME_POLICY: value:11	flag indicating a federate should operate on a restrictive time policy, which disallows some 2nd order time evaluation and can be useful for certain types of dependency cycles and update patterns, but generally shouldn't be used as it can lead to some very slow update conditions
		HELICS_FLAG_ROLLBACK: value:12	flag indicating that a federate has rollback capability
		HELICS_FLAG_FORWARD_COMPUTE: value:14	flag indicating that a federate performs forward computation and does internal rollback
		HELICS_FLAG_REALTIME: value:16	flag indicating that a federate needs to run in real time
		HELICS_FLAG_SINGLE_THREAD_FEDERATE: value:27	flag indicating that the federate will only interact on a single thread
		HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS: value:67	used to not display warnings on mismatched requested times
		HELICS_FLAG_STRICT_CONFIG_CHECKING: value:75	specify that checking on configuration files should be strict and throw and error on any invalid values
		HELICS_FLAG_USE_JSON_SERIALIZATION: value:79	specify that the federate should use json serialization for all data types
		HELICS_FLAG_EVENT_TRIGGERED: value:81	specify that the federate is event triggered-meaning (all/most) events are triggered by incoming events
		HELICS_FLAG_LOCAL_PROFILING_CAPTURE: value:96	specify that that federate should capture the profiling data to the local federate logging system
	"""

	HELICS_FLAG_OBSERVER = 0
	HELICS_FLAG_UNINTERRUPTIBLE = 1
	HELICS_FLAG_INTERRUPTIBLE = 2
	HELICS_FLAG_SOURCE_ONLY = 4
	HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE = 6
	HELICS_FLAG_ONLY_UPDATE_ON_CHANGE = 8
	HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE = 10
	HELICS_FLAG_RESTRICTIVE_TIME_POLICY = 11
	HELICS_FLAG_ROLLBACK = 12
	HELICS_FLAG_FORWARD_COMPUTE = 14
	HELICS_FLAG_REALTIME = 16
	HELICS_FLAG_SINGLE_THREAD_FEDERATE = 27
	HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS = 67
	HELICS_FLAG_STRICT_CONFIG_CHECKING = 75
	HELICS_FLAG_USE_JSON_SERIALIZATION = 79
	HELICS_FLAG_EVENT_TRIGGERED = 81
	HELICS_FLAG_LOCAL_PROFILING_CAPTURE = 96


HELICS_FLAG_OBSERVER = HelicsFederateFlags.HELICS_FLAG_OBSERVER
HELICS_FLAG_UNINTERRUPTIBLE = HelicsFederateFlags.HELICS_FLAG_UNINTERRUPTIBLE
HELICS_FLAG_INTERRUPTIBLE = HelicsFederateFlags.HELICS_FLAG_INTERRUPTIBLE
HELICS_FLAG_SOURCE_ONLY = HelicsFederateFlags.HELICS_FLAG_SOURCE_ONLY
HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE = HelicsFederateFlags.HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE
HELICS_FLAG_ONLY_UPDATE_ON_CHANGE = HelicsFederateFlags.HELICS_FLAG_ONLY_UPDATE_ON_CHANGE
HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE = HelicsFederateFlags.HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE
HELICS_FLAG_RESTRICTIVE_TIME_POLICY = HelicsFederateFlags.HELICS_FLAG_RESTRICTIVE_TIME_POLICY
HELICS_FLAG_ROLLBACK = HelicsFederateFlags.HELICS_FLAG_ROLLBACK
HELICS_FLAG_FORWARD_COMPUTE = HelicsFederateFlags.HELICS_FLAG_FORWARD_COMPUTE
HELICS_FLAG_REALTIME = HelicsFederateFlags.HELICS_FLAG_REALTIME
HELICS_FLAG_SINGLE_THREAD_FEDERATE = HelicsFederateFlags.HELICS_FLAG_SINGLE_THREAD_FEDERATE
HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS = HelicsFederateFlags.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS
HELICS_FLAG_STRICT_CONFIG_CHECKING = HelicsFederateFlags.HELICS_FLAG_STRICT_CONFIG_CHECKING
HELICS_FLAG_USE_JSON_SERIALIZATION = HelicsFederateFlags.HELICS_FLAG_USE_JSON_SERIALIZATION
HELICS_FLAG_EVENT_TRIGGERED = HelicsFederateFlags.HELICS_FLAG_EVENT_TRIGGERED
HELICS_FLAG_LOCAL_PROFILING_CAPTURE = HelicsFederateFlags.HELICS_FLAG_LOCAL_PROFILING_CAPTURE

helics_flag_observer = HelicsFederateFlags.HELICS_FLAG_OBSERVER
helics_flag_uninterruptible = HelicsFederateFlags.HELICS_FLAG_UNINTERRUPTIBLE
helics_flag_interruptible = HelicsFederateFlags.HELICS_FLAG_INTERRUPTIBLE
helics_flag_source_only = HelicsFederateFlags.HELICS_FLAG_SOURCE_ONLY
helics_flag_only_transmit_on_change = HelicsFederateFlags.HELICS_FLAG_ONLY_TRANSMIT_ON_CHANGE
helics_flag_only_update_on_change = HelicsFederateFlags.HELICS_FLAG_ONLY_UPDATE_ON_CHANGE
helics_flag_wait_for_current_time_update = HelicsFederateFlags.HELICS_FLAG_WAIT_FOR_CURRENT_TIME_UPDATE
helics_flag_restrictive_time_policy = HelicsFederateFlags.HELICS_FLAG_RESTRICTIVE_TIME_POLICY
helics_flag_rollback = HelicsFederateFlags.HELICS_FLAG_ROLLBACK
helics_flag_forward_compute = HelicsFederateFlags.HELICS_FLAG_FORWARD_COMPUTE
helics_flag_realtime = HelicsFederateFlags.HELICS_FLAG_REALTIME
helics_flag_single_thread_federate = HelicsFederateFlags.HELICS_FLAG_SINGLE_THREAD_FEDERATE
helics_flag_ignore_time_mismatch_warnings = HelicsFederateFlags.HELICS_FLAG_IGNORE_TIME_MISMATCH_WARNINGS
helics_flag_strict_config_checking = HelicsFederateFlags.HELICS_FLAG_STRICT_CONFIG_CHECKING
helics_flag_use_json_serialization = HelicsFederateFlags.HELICS_FLAG_USE_JSON_SERIALIZATION
helics_flag_event_triggered = HelicsFederateFlags.HELICS_FLAG_EVENT_TRIGGERED
helics_flag_local_profiling_capture = HelicsFederateFlags.HELICS_FLAG_LOCAL_PROFILING_CAPTURE


class HelicsCoreFlags(enum.IntEnum):
	""" enumeration of additional core flags

	Attributes:
		HELICS_FLAG_DELAY_INIT_ENTRY: value:45	used to delay a core from entering initialization mode even if it would otherwise be ready
		HELICS_FLAG_ENABLE_INIT_ENTRY: value:47	used to clear the HELICS_DELAY_INIT_ENTRY flag in cores
		HELICS_FLAG_IGNORE: value:999	ignored flag used to test some code paths
	"""

	HELICS_FLAG_DELAY_INIT_ENTRY = 45
	HELICS_FLAG_ENABLE_INIT_ENTRY = 47
	HELICS_FLAG_IGNORE = 999


HELICS_FLAG_DELAY_INIT_ENTRY = HelicsCoreFlags.HELICS_FLAG_DELAY_INIT_ENTRY
HELICS_FLAG_ENABLE_INIT_ENTRY = HelicsCoreFlags.HELICS_FLAG_ENABLE_INIT_ENTRY
HELICS_FLAG_IGNORE = HelicsCoreFlags.HELICS_FLAG_IGNORE

helics_flag_delay_init_entry = HelicsCoreFlags.HELICS_FLAG_DELAY_INIT_ENTRY
helics_flag_enable_init_entry = HelicsCoreFlags.HELICS_FLAG_ENABLE_INIT_ENTRY
helics_flag_ignore = HelicsCoreFlags.HELICS_FLAG_IGNORE


class HelicsFlags(enum.IntEnum):
	""" enumeration of general flags that can be used in federates/cores/brokers

	Attributes:
		HELICS_FLAG_SLOW_RESPONDING: value:29	flag specifying that a federate, core, or broker may be slow to respond to pings If the federate goes offline there is no good way to detect it so use with caution
		HELICS_FLAG_DEBUGGING: value:31	flag specifying the federate/core/broker is operating in a user debug mode so deadlock timers and timeout are disabled this flag is a combination of slow_responding and disabling of some timeouts
		HELICS_FLAG_TERMINATE_ON_ERROR: value:72	specify that a federate error should terminate the federation
		HELICS_FLAG_FORCE_LOGGING_FLUSH: value:88	specify that the log files should be flushed on every log message
		HELICS_FLAG_DUMPLOG: value:89	specify that a full log should be dumped into a file
		HELICS_FLAG_PROFILING: value:93	specify that helics should capture profiling data
		HELICS_FLAG_PROFILING_MARKER: value:95	flag trigger for generating a profiling marker
	"""

	HELICS_FLAG_SLOW_RESPONDING = 29
	HELICS_FLAG_DEBUGGING = 31
	HELICS_FLAG_TERMINATE_ON_ERROR = 72
	HELICS_FLAG_FORCE_LOGGING_FLUSH = 88
	HELICS_FLAG_DUMPLOG = 89
	HELICS_FLAG_PROFILING = 93
	HELICS_FLAG_PROFILING_MARKER = 95


HELICS_FLAG_SLOW_RESPONDING = HelicsFlags.HELICS_FLAG_SLOW_RESPONDING
HELICS_FLAG_DEBUGGING = HelicsFlags.HELICS_FLAG_DEBUGGING
HELICS_FLAG_TERMINATE_ON_ERROR = HelicsFlags.HELICS_FLAG_TERMINATE_ON_ERROR
HELICS_FLAG_FORCE_LOGGING_FLUSH = HelicsFlags.HELICS_FLAG_FORCE_LOGGING_FLUSH
HELICS_FLAG_DUMPLOG = HelicsFlags.HELICS_FLAG_DUMPLOG
HELICS_FLAG_PROFILING = HelicsFlags.HELICS_FLAG_PROFILING
HELICS_FLAG_PROFILING_MARKER = HelicsFlags.HELICS_FLAG_PROFILING_MARKER

helics_flag_slow_responding = HelicsFlags.HELICS_FLAG_SLOW_RESPONDING
helics_flag_debugging = HelicsFlags.HELICS_FLAG_DEBUGGING
helics_flag_terminate_on_error = HelicsFlags.HELICS_FLAG_TERMINATE_ON_ERROR
helics_flag_force_logging_flush = HelicsFlags.HELICS_FLAG_FORCE_LOGGING_FLUSH
helics_flag_dumplog = HelicsFlags.HELICS_FLAG_DUMPLOG
helics_flag_profiling = HelicsFlags.HELICS_FLAG_PROFILING
helics_flag_profiling_marker = HelicsFlags.HELICS_FLAG_PROFILING_MARKER


class HelicsLogLevels(enum.IntEnum):
	""" log level definitions

	Attributes:
		HELICS_LOG_LEVEL_DUMPLOG: value:-10	log level for dumping log messages
		HELICS_LOG_LEVEL_NO_PRINT: value:-4	don't print anything except a few catastrophic errors
		HELICS_LOG_LEVEL_ERROR: value:0	only print error level indicators
		HELICS_LOG_LEVEL_PROFILING: value:2	profiling log level
		HELICS_LOG_LEVEL_WARNING: value:3	only print warnings and errors
		HELICS_LOG_LEVEL_SUMMARY: value:6	warning errors and summary level information
		HELICS_LOG_LEVEL_CONNECTIONS: value:9	summary+ notices about federate and broker connections +messages about network connections
		HELICS_LOG_LEVEL_INTERFACES: value:12	connections+ interface definitions
		HELICS_LOG_LEVEL_TIMING: value:15	interfaces + timing message
		HELICS_LOG_LEVEL_DATA: value:18	timing+ data transfer notices
		HELICS_LOG_LEVEL_DEBUG: value:21	data+ additional debug message
		HELICS_LOG_LEVEL_TRACE: value:24	all internal messages
	"""

	HELICS_LOG_LEVEL_DUMPLOG = -10
	HELICS_LOG_LEVEL_NO_PRINT = -4
	HELICS_LOG_LEVEL_ERROR = 0
	HELICS_LOG_LEVEL_PROFILING = 2
	HELICS_LOG_LEVEL_WARNING = 3
	HELICS_LOG_LEVEL_SUMMARY = 6
	HELICS_LOG_LEVEL_CONNECTIONS = 9
	HELICS_LOG_LEVEL_INTERFACES = 12
	HELICS_LOG_LEVEL_TIMING = 15
	HELICS_LOG_LEVEL_DATA = 18
	HELICS_LOG_LEVEL_DEBUG = 21
	HELICS_LOG_LEVEL_TRACE = 24


HELICS_LOG_LEVEL_DUMPLOG = HelicsLogLevels.HELICS_LOG_LEVEL_DUMPLOG
HELICS_LOG_LEVEL_NO_PRINT = HelicsLogLevels.HELICS_LOG_LEVEL_NO_PRINT
HELICS_LOG_LEVEL_ERROR = HelicsLogLevels.HELICS_LOG_LEVEL_ERROR
HELICS_LOG_LEVEL_PROFILING = HelicsLogLevels.HELICS_LOG_LEVEL_PROFILING
HELICS_LOG_LEVEL_WARNING = HelicsLogLevels.HELICS_LOG_LEVEL_WARNING
HELICS_LOG_LEVEL_SUMMARY = HelicsLogLevels.HELICS_LOG_LEVEL_SUMMARY
HELICS_LOG_LEVEL_CONNECTIONS = HelicsLogLevels.HELICS_LOG_LEVEL_CONNECTIONS
HELICS_LOG_LEVEL_INTERFACES = HelicsLogLevels.HELICS_LOG_LEVEL_INTERFACES
HELICS_LOG_LEVEL_TIMING = HelicsLogLevels.HELICS_LOG_LEVEL_TIMING
HELICS_LOG_LEVEL_DATA = HelicsLogLevels.HELICS_LOG_LEVEL_DATA
HELICS_LOG_LEVEL_DEBUG = HelicsLogLevels.HELICS_LOG_LEVEL_DEBUG
HELICS_LOG_LEVEL_TRACE = HelicsLogLevels.HELICS_LOG_LEVEL_TRACE

helics_log_level_dumplog = HelicsLogLevels.HELICS_LOG_LEVEL_DUMPLOG
helics_log_level_no_print = HelicsLogLevels.HELICS_LOG_LEVEL_NO_PRINT
helics_log_level_error = HelicsLogLevels.HELICS_LOG_LEVEL_ERROR
helics_log_level_profiling = HelicsLogLevels.HELICS_LOG_LEVEL_PROFILING
helics_log_level_warning = HelicsLogLevels.HELICS_LOG_LEVEL_WARNING
helics_log_level_summary = HelicsLogLevels.HELICS_LOG_LEVEL_SUMMARY
helics_log_level_connections = HelicsLogLevels.HELICS_LOG_LEVEL_CONNECTIONS
helics_log_level_interfaces = HelicsLogLevels.HELICS_LOG_LEVEL_INTERFACES
helics_log_level_timing = HelicsLogLevels.HELICS_LOG_LEVEL_TIMING
helics_log_level_data = HelicsLogLevels.HELICS_LOG_LEVEL_DATA
helics_log_level_debug = HelicsLogLevels.HELICS_LOG_LEVEL_DEBUG
helics_log_level_trace = HelicsLogLevels.HELICS_LOG_LEVEL_TRACE


class HelicsErrorTypes(enum.IntEnum):
	""" enumeration of return values from the C interface functions

	Attributes:
		HELICS_ERROR_FATAL: value:-404	global fatal error for federation
		HELICS_ERROR_EXTERNAL_TYPE: value:-203	an unknown non-helics error was produced
		HELICS_ERROR_OTHER: value:-101	the function produced a helics error of some other type
		HELICS_ERROR_USER_ABORT: value:-27	user system abort
		HELICS_ERROR_INSUFFICIENT_SPACE: value:-18	insufficient space is available to store requested data
		HELICS_ERROR_EXECUTION_FAILURE: value:-14	the function execution has failed
		HELICS_ERROR_INVALID_FUNCTION_CALL: value:-10	the call made was invalid in the present state of the calling object
		HELICS_ERROR_INVALID_STATE_TRANSITION: value:-9	error issued when an invalid state transition occurred
		HELICS_WARNING: value:-8	the function issued a warning of some kind
		HELICS_ERROR_SYSTEM_FAILURE: value:-6	the federate has terminated unexpectedly and the call cannot be completed
		HELICS_ERROR_DISCARD: value:-5	the input was discarded and not used for some reason
		HELICS_ERROR_INVALID_ARGUMENT: value:-4	the parameter passed was invalid and unable to be used
		HELICS_ERROR_INVALID_OBJECT: value:-3	indicator that the object used was not a valid object
		HELICS_ERROR_CONNECTION_FAILURE: value:-2	the operation to connect has failed
		HELICS_ERROR_REGISTRATION_FAILURE: value:-1	registration has failed
		HELICS_OK: value:0	the function executed successfully
	"""

	HELICS_ERROR_FATAL = -404
	HELICS_ERROR_EXTERNAL_TYPE = -203
	HELICS_ERROR_OTHER = -101
	HELICS_ERROR_USER_ABORT = -27
	HELICS_ERROR_INSUFFICIENT_SPACE = -18
	HELICS_ERROR_EXECUTION_FAILURE = -14
	HELICS_ERROR_INVALID_FUNCTION_CALL = -10
	HELICS_ERROR_INVALID_STATE_TRANSITION = -9
	HELICS_WARNING = -8
	HELICS_ERROR_SYSTEM_FAILURE = -6
	HELICS_ERROR_DISCARD = -5
	HELICS_ERROR_INVALID_ARGUMENT = -4
	HELICS_ERROR_INVALID_OBJECT = -3
	HELICS_ERROR_CONNECTION_FAILURE = -2
	HELICS_ERROR_REGISTRATION_FAILURE = -1
	HELICS_OK = 0


HELICS_ERROR_FATAL = HelicsErrorTypes.HELICS_ERROR_FATAL
HELICS_ERROR_EXTERNAL_TYPE = HelicsErrorTypes.HELICS_ERROR_EXTERNAL_TYPE
HELICS_ERROR_OTHER = HelicsErrorTypes.HELICS_ERROR_OTHER
HELICS_ERROR_USER_ABORT = HelicsErrorTypes.HELICS_ERROR_USER_ABORT
HELICS_ERROR_INSUFFICIENT_SPACE = HelicsErrorTypes.HELICS_ERROR_INSUFFICIENT_SPACE
HELICS_ERROR_EXECUTION_FAILURE = HelicsErrorTypes.HELICS_ERROR_EXECUTION_FAILURE
HELICS_ERROR_INVALID_FUNCTION_CALL = HelicsErrorTypes.HELICS_ERROR_INVALID_FUNCTION_CALL
HELICS_ERROR_INVALID_STATE_TRANSITION = HelicsErrorTypes.HELICS_ERROR_INVALID_STATE_TRANSITION
HELICS_WARNING = HelicsErrorTypes.HELICS_WARNING
HELICS_ERROR_SYSTEM_FAILURE = HelicsErrorTypes.HELICS_ERROR_SYSTEM_FAILURE
HELICS_ERROR_DISCARD = HelicsErrorTypes.HELICS_ERROR_DISCARD
HELICS_ERROR_INVALID_ARGUMENT = HelicsErrorTypes.HELICS_ERROR_INVALID_ARGUMENT
HELICS_ERROR_INVALID_OBJECT = HelicsErrorTypes.HELICS_ERROR_INVALID_OBJECT
HELICS_ERROR_CONNECTION_FAILURE = HelicsErrorTypes.HELICS_ERROR_CONNECTION_FAILURE
HELICS_ERROR_REGISTRATION_FAILURE = HelicsErrorTypes.HELICS_ERROR_REGISTRATION_FAILURE
HELICS_OK = HelicsErrorTypes.HELICS_OK

helics_error_fatal = HelicsErrorTypes.HELICS_ERROR_FATAL
helics_error_external_type = HelicsErrorTypes.HELICS_ERROR_EXTERNAL_TYPE
helics_error_other = HelicsErrorTypes.HELICS_ERROR_OTHER
helics_error_user_abort = HelicsErrorTypes.HELICS_ERROR_USER_ABORT
helics_error_insufficient_space = HelicsErrorTypes.HELICS_ERROR_INSUFFICIENT_SPACE
helics_error_execution_failure = HelicsErrorTypes.HELICS_ERROR_EXECUTION_FAILURE
helics_error_invalid_function_call = HelicsErrorTypes.HELICS_ERROR_INVALID_FUNCTION_CALL
helics_error_invalid_state_transition = HelicsErrorTypes.HELICS_ERROR_INVALID_STATE_TRANSITION
helics_warning = HelicsErrorTypes.HELICS_WARNING
helics_error_system_failure = HelicsErrorTypes.HELICS_ERROR_SYSTEM_FAILURE
helics_error_discard = HelicsErrorTypes.HELICS_ERROR_DISCARD
helics_error_invalid_argument = HelicsErrorTypes.HELICS_ERROR_INVALID_ARGUMENT
helics_error_invalid_object = HelicsErrorTypes.HELICS_ERROR_INVALID_OBJECT
helics_error_connection_failure = HelicsErrorTypes.HELICS_ERROR_CONNECTION_FAILURE
helics_error_registration_failure = HelicsErrorTypes.HELICS_ERROR_REGISTRATION_FAILURE
helics_ok = HelicsErrorTypes.HELICS_OK


class HelicsProperties(enum.IntEnum):
	""" enumeration of properties that apply to federates and sometimes cores

	Attributes:
		HELICS_PROPERTY_TIME_DELTA: value:137	the property controlling the minimum time delta for a federate
		HELICS_PROPERTY_TIME_PERIOD: value:140	the property controlling the period for a federate
		HELICS_PROPERTY_TIME_OFFSET: value:141	the property controlling time offset for the period of federate
		HELICS_PROPERTY_TIME_RT_LAG: value:143	the property controlling real time lag for a federate the max time a federate can lag real time
		HELICS_PROPERTY_TIME_RT_LEAD: value:144	the property controlling real time lead for a federate the max time a federate can be ahead of real time
		HELICS_PROPERTY_TIME_RT_TOLERANCE: value:145	the property controlling real time tolerance for a federate sets both rt_lag and rt_lead
		HELICS_PROPERTY_TIME_INPUT_DELAY: value:148	the property controlling input delay for a federate
		HELICS_PROPERTY_TIME_OUTPUT_DELAY: value:150	the property controlling output delay for a federate
		HELICS_PROPERTY_TIME_GRANT_TIMEOUT: value:161	the property specifying a timeout to trigger actions if the time for granting exceeds a certain threshold
		HELICS_PROPERTY_INT_MAX_ITERATIONS: value:259	integer property controlling the maximum number of iterations in a federate
		HELICS_PROPERTY_INT_LOG_LEVEL: value:271	integer property controlling the log level in a federate see HelicsLogLevels
		HELICS_PROPERTY_INT_FILE_LOG_LEVEL: value:272	integer property controlling the log level for file logging in a federate see HelicsLogLevels
		HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL: value:274	integer property controlling the log level for console logging in a federate see HelicsLogLevels
		HELICS_PROPERTY_INT_LOG_BUFFER: value:276	integer property controlling the size of the log buffer
	"""

	HELICS_PROPERTY_TIME_DELTA = 137
	HELICS_PROPERTY_TIME_PERIOD = 140
	HELICS_PROPERTY_TIME_OFFSET = 141
	HELICS_PROPERTY_TIME_RT_LAG = 143
	HELICS_PROPERTY_TIME_RT_LEAD = 144
	HELICS_PROPERTY_TIME_RT_TOLERANCE = 145
	HELICS_PROPERTY_TIME_INPUT_DELAY = 148
	HELICS_PROPERTY_TIME_OUTPUT_DELAY = 150
	HELICS_PROPERTY_TIME_GRANT_TIMEOUT = 161
	HELICS_PROPERTY_INT_MAX_ITERATIONS = 259
	HELICS_PROPERTY_INT_LOG_LEVEL = 271
	HELICS_PROPERTY_INT_FILE_LOG_LEVEL = 272
	HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL = 274
	HELICS_PROPERTY_INT_LOG_BUFFER = 276


HELICS_PROPERTY_TIME_DELTA = HelicsProperties.HELICS_PROPERTY_TIME_DELTA
HELICS_PROPERTY_TIME_PERIOD = HelicsProperties.HELICS_PROPERTY_TIME_PERIOD
HELICS_PROPERTY_TIME_OFFSET = HelicsProperties.HELICS_PROPERTY_TIME_OFFSET
HELICS_PROPERTY_TIME_RT_LAG = HelicsProperties.HELICS_PROPERTY_TIME_RT_LAG
HELICS_PROPERTY_TIME_RT_LEAD = HelicsProperties.HELICS_PROPERTY_TIME_RT_LEAD
HELICS_PROPERTY_TIME_RT_TOLERANCE = HelicsProperties.HELICS_PROPERTY_TIME_RT_TOLERANCE
HELICS_PROPERTY_TIME_INPUT_DELAY = HelicsProperties.HELICS_PROPERTY_TIME_INPUT_DELAY
HELICS_PROPERTY_TIME_OUTPUT_DELAY = HelicsProperties.HELICS_PROPERTY_TIME_OUTPUT_DELAY
HELICS_PROPERTY_TIME_GRANT_TIMEOUT = HelicsProperties.HELICS_PROPERTY_TIME_GRANT_TIMEOUT
HELICS_PROPERTY_INT_MAX_ITERATIONS = HelicsProperties.HELICS_PROPERTY_INT_MAX_ITERATIONS
HELICS_PROPERTY_INT_LOG_LEVEL = HelicsProperties.HELICS_PROPERTY_INT_LOG_LEVEL
HELICS_PROPERTY_INT_FILE_LOG_LEVEL = HelicsProperties.HELICS_PROPERTY_INT_FILE_LOG_LEVEL
HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL = HelicsProperties.HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL
HELICS_PROPERTY_INT_LOG_BUFFER = HelicsProperties.HELICS_PROPERTY_INT_LOG_BUFFER

helics_property_time_delta = HelicsProperties.HELICS_PROPERTY_TIME_DELTA
helics_property_time_period = HelicsProperties.HELICS_PROPERTY_TIME_PERIOD
helics_property_time_offset = HelicsProperties.HELICS_PROPERTY_TIME_OFFSET
helics_property_time_rt_lag = HelicsProperties.HELICS_PROPERTY_TIME_RT_LAG
helics_property_time_rt_lead = HelicsProperties.HELICS_PROPERTY_TIME_RT_LEAD
helics_property_time_rt_tolerance = HelicsProperties.HELICS_PROPERTY_TIME_RT_TOLERANCE
helics_property_time_input_delay = HelicsProperties.HELICS_PROPERTY_TIME_INPUT_DELAY
helics_property_time_output_delay = HelicsProperties.HELICS_PROPERTY_TIME_OUTPUT_DELAY
helics_property_time_grant_timeout = HelicsProperties.HELICS_PROPERTY_TIME_GRANT_TIMEOUT
helics_property_int_max_iterations = HelicsProperties.HELICS_PROPERTY_INT_MAX_ITERATIONS
helics_property_int_log_level = HelicsProperties.HELICS_PROPERTY_INT_LOG_LEVEL
helics_property_int_file_log_level = HelicsProperties.HELICS_PROPERTY_INT_FILE_LOG_LEVEL
helics_property_int_console_log_level = HelicsProperties.HELICS_PROPERTY_INT_CONSOLE_LOG_LEVEL
helics_property_int_log_buffer = HelicsProperties.HELICS_PROPERTY_INT_LOG_BUFFER


class HelicsMultiInputModes(enum.IntEnum):
	""" enumeration of the multi_input operations

	Attributes:
		HELICS_MULTI_INPUT_NO_OP: value:0	time and priority order the inputs from the core library
		HELICS_MULTI_INPUT_VECTORIZE_OPERATION: value:1	vectorize the inputs either double vector or string vector
		HELICS_MULTI_INPUT_AND_OPERATION: value:2	all inputs are assumed to be boolean and all must be true to return true
		HELICS_MULTI_INPUT_OR_OPERATION: value:3	all inputs are assumed to be boolean and at least one must be true to return true
		HELICS_MULTI_INPUT_SUM_OPERATION: value:4	sum all the inputs
		HELICS_MULTI_INPUT_DIFF_OPERATION: value:5	do a difference operation on the inputs, first-sum(rest) for double input, vector diff for vector input
		HELICS_MULTI_INPUT_MAX_OPERATION: value:6	find the max of the inputs
		HELICS_MULTI_INPUT_MIN_OPERATION: value:7	find the min of the inputs
		HELICS_MULTI_INPUT_AVERAGE_OPERATION: value:8	take the average of the inputs
	"""

	HELICS_MULTI_INPUT_NO_OP = 0
	HELICS_MULTI_INPUT_VECTORIZE_OPERATION = 1
	HELICS_MULTI_INPUT_AND_OPERATION = 2
	HELICS_MULTI_INPUT_OR_OPERATION = 3
	HELICS_MULTI_INPUT_SUM_OPERATION = 4
	HELICS_MULTI_INPUT_DIFF_OPERATION = 5
	HELICS_MULTI_INPUT_MAX_OPERATION = 6
	HELICS_MULTI_INPUT_MIN_OPERATION = 7
	HELICS_MULTI_INPUT_AVERAGE_OPERATION = 8


HELICS_MULTI_INPUT_NO_OP = HelicsMultiInputModes.HELICS_MULTI_INPUT_NO_OP
HELICS_MULTI_INPUT_VECTORIZE_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_VECTORIZE_OPERATION
HELICS_MULTI_INPUT_AND_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_AND_OPERATION
HELICS_MULTI_INPUT_OR_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_OR_OPERATION
HELICS_MULTI_INPUT_SUM_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_SUM_OPERATION
HELICS_MULTI_INPUT_DIFF_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_DIFF_OPERATION
HELICS_MULTI_INPUT_MAX_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_MAX_OPERATION
HELICS_MULTI_INPUT_MIN_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_MIN_OPERATION
HELICS_MULTI_INPUT_AVERAGE_OPERATION = HelicsMultiInputModes.HELICS_MULTI_INPUT_AVERAGE_OPERATION

helics_multi_input_no_op = HelicsMultiInputModes.HELICS_MULTI_INPUT_NO_OP
helics_multi_input_vectorize_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_VECTORIZE_OPERATION
helics_multi_input_and_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_AND_OPERATION
helics_multi_input_or_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_OR_OPERATION
helics_multi_input_sum_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_SUM_OPERATION
helics_multi_input_diff_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_DIFF_OPERATION
helics_multi_input_max_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_MAX_OPERATION
helics_multi_input_min_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_MIN_OPERATION
helics_multi_input_average_operation = HelicsMultiInputModes.HELICS_MULTI_INPUT_AVERAGE_OPERATION


class HelicsHandleOptions(enum.IntEnum):
	""" enumeration of options that apply to handles

	Attributes:
		HELICS_HANDLE_OPTION_CONNECTION_REQUIRED: value:397	specify that a connection is required for an interface and will generate an error if not available
		HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL: value:402	specify that a connection is NOT required for an interface and will only be made if available no warning will be issues if not available
		HELICS_HANDLE_OPTION_SINGLE_CONNECTION_ONLY: value:407	specify that only a single connection is allowed for an interface
		HELICS_HANDLE_OPTION_MULTIPLE_CONNECTIONS_ALLOWED: value:409	specify that multiple connections are allowed for an interface
		HELICS_HANDLE_OPTION_BUFFER_DATA: value:411	specify that the last data should be buffered and sent on subscriptions after init
		HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING: value:414	specify that the types should be checked strictly for pub/sub and filters
		HELICS_HANDLE_OPTION_IGNORE_UNIT_MISMATCH: value:447	specify that the mismatching units should be ignored
		HELICS_HANDLE_OPTION_ONLY_TRANSMIT_ON_CHANGE: value:452	specify that an interface will only transmit on change(only applicable to publications)
		HELICS_HANDLE_OPTION_ONLY_UPDATE_ON_CHANGE: value:454	specify that an interface will only update if the value has actually changed
		HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS: value:475	specify that an interface does not participate in determining time interrupts
		HELICS_HANDLE_OPTION_MULTI_INPUT_HANDLING_METHOD: value:507	specify the multi-input processing method for inputs
		HELICS_HANDLE_OPTION_INPUT_PRIORITY_LOCATION: value:510	specify the source index with the highest priority
		HELICS_HANDLE_OPTION_CLEAR_PRIORITY_LIST: value:512	specify that the priority list should be cleared or question if it is cleared
		HELICS_HANDLE_OPTION_CONNECTIONS: value:522	specify the required number of connections or get the actual number of connections
	"""

	HELICS_HANDLE_OPTION_CONNECTION_REQUIRED = 397
	HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL = 402
	HELICS_HANDLE_OPTION_SINGLE_CONNECTION_ONLY = 407
	HELICS_HANDLE_OPTION_MULTIPLE_CONNECTIONS_ALLOWED = 409
	HELICS_HANDLE_OPTION_BUFFER_DATA = 411
	HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING = 414
	HELICS_HANDLE_OPTION_IGNORE_UNIT_MISMATCH = 447
	HELICS_HANDLE_OPTION_ONLY_TRANSMIT_ON_CHANGE = 452
	HELICS_HANDLE_OPTION_ONLY_UPDATE_ON_CHANGE = 454
	HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS = 475
	HELICS_HANDLE_OPTION_MULTI_INPUT_HANDLING_METHOD = 507
	HELICS_HANDLE_OPTION_INPUT_PRIORITY_LOCATION = 510
	HELICS_HANDLE_OPTION_CLEAR_PRIORITY_LIST = 512
	HELICS_HANDLE_OPTION_CONNECTIONS = 522


HELICS_HANDLE_OPTION_CONNECTION_REQUIRED = HelicsHandleOptions.HELICS_HANDLE_OPTION_CONNECTION_REQUIRED
HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL = HelicsHandleOptions.HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL
HELICS_HANDLE_OPTION_SINGLE_CONNECTION_ONLY = HelicsHandleOptions.HELICS_HANDLE_OPTION_SINGLE_CONNECTION_ONLY
HELICS_HANDLE_OPTION_MULTIPLE_CONNECTIONS_ALLOWED = HelicsHandleOptions.HELICS_HANDLE_OPTION_MULTIPLE_CONNECTIONS_ALLOWED
HELICS_HANDLE_OPTION_BUFFER_DATA = HelicsHandleOptions.HELICS_HANDLE_OPTION_BUFFER_DATA
HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING = HelicsHandleOptions.HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING
HELICS_HANDLE_OPTION_IGNORE_UNIT_MISMATCH = HelicsHandleOptions.HELICS_HANDLE_OPTION_IGNORE_UNIT_MISMATCH
HELICS_HANDLE_OPTION_ONLY_TRANSMIT_ON_CHANGE = HelicsHandleOptions.HELICS_HANDLE_OPTION_ONLY_TRANSMIT_ON_CHANGE
HELICS_HANDLE_OPTION_ONLY_UPDATE_ON_CHANGE = HelicsHandleOptions.HELICS_HANDLE_OPTION_ONLY_UPDATE_ON_CHANGE
HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS = HelicsHandleOptions.HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS
HELICS_HANDLE_OPTION_MULTI_INPUT_HANDLING_METHOD = HelicsHandleOptions.HELICS_HANDLE_OPTION_MULTI_INPUT_HANDLING_METHOD
HELICS_HANDLE_OPTION_INPUT_PRIORITY_LOCATION = HelicsHandleOptions.HELICS_HANDLE_OPTION_INPUT_PRIORITY_LOCATION
HELICS_HANDLE_OPTION_CLEAR_PRIORITY_LIST = HelicsHandleOptions.HELICS_HANDLE_OPTION_CLEAR_PRIORITY_LIST
HELICS_HANDLE_OPTION_CONNECTIONS = HelicsHandleOptions.HELICS_HANDLE_OPTION_CONNECTIONS

helics_handle_option_connection_required = HelicsHandleOptions.HELICS_HANDLE_OPTION_CONNECTION_REQUIRED
helics_handle_option_connection_optional = HelicsHandleOptions.HELICS_HANDLE_OPTION_CONNECTION_OPTIONAL
helics_handle_option_single_connection_only = HelicsHandleOptions.HELICS_HANDLE_OPTION_SINGLE_CONNECTION_ONLY
helics_handle_option_multiple_connections_allowed = HelicsHandleOptions.HELICS_HANDLE_OPTION_MULTIPLE_CONNECTIONS_ALLOWED
helics_handle_option_buffer_data = HelicsHandleOptions.HELICS_HANDLE_OPTION_BUFFER_DATA
helics_handle_option_strict_type_checking = HelicsHandleOptions.HELICS_HANDLE_OPTION_STRICT_TYPE_CHECKING
helics_handle_option_ignore_unit_mismatch = HelicsHandleOptions.HELICS_HANDLE_OPTION_IGNORE_UNIT_MISMATCH
helics_handle_option_only_transmit_on_change = HelicsHandleOptions.HELICS_HANDLE_OPTION_ONLY_TRANSMIT_ON_CHANGE
helics_handle_option_only_update_on_change = HelicsHandleOptions.HELICS_HANDLE_OPTION_ONLY_UPDATE_ON_CHANGE
helics_handle_option_ignore_interrupts = HelicsHandleOptions.HELICS_HANDLE_OPTION_IGNORE_INTERRUPTS
helics_handle_option_multi_input_handling_method = HelicsHandleOptions.HELICS_HANDLE_OPTION_MULTI_INPUT_HANDLING_METHOD
helics_handle_option_input_priority_location = HelicsHandleOptions.HELICS_HANDLE_OPTION_INPUT_PRIORITY_LOCATION
helics_handle_option_clear_priority_list = HelicsHandleOptions.HELICS_HANDLE_OPTION_CLEAR_PRIORITY_LIST
helics_handle_option_connections = HelicsHandleOptions.HELICS_HANDLE_OPTION_CONNECTIONS


class HelicsFilterTypes(enum.IntEnum):
	""" enumeration of the predefined filter types

	Attributes:
		HELICS_FILTER_TYPE_CUSTOM: value:0	a custom filter type that executes a user defined callback
		HELICS_FILTER_TYPE_DELAY: value:1	a filter type that executes a fixed delay on a message
		HELICS_FILTER_TYPE_RANDOM_DELAY: value:2	a filter type that executes a random delay on the messages
		HELICS_FILTER_TYPE_RANDOM_DROP: value:3	a filter type that randomly drops messages
		HELICS_FILTER_TYPE_REROUTE: value:4	a filter type that reroutes a message to a different destination than originally specified
		HELICS_FILTER_TYPE_CLONE: value:5	a filter type that duplicates a message and sends the copy to a different destination
		HELICS_FILTER_TYPE_FIREWALL: value:6	a customizable filter type that can perform different actions on a message based on firewall like rules
	"""

	HELICS_FILTER_TYPE_CUSTOM = 0
	HELICS_FILTER_TYPE_DELAY = 1
	HELICS_FILTER_TYPE_RANDOM_DELAY = 2
	HELICS_FILTER_TYPE_RANDOM_DROP = 3
	HELICS_FILTER_TYPE_REROUTE = 4
	HELICS_FILTER_TYPE_CLONE = 5
	HELICS_FILTER_TYPE_FIREWALL = 6


HELICS_FILTER_TYPE_CUSTOM = HelicsFilterTypes.HELICS_FILTER_TYPE_CUSTOM
HELICS_FILTER_TYPE_DELAY = HelicsFilterTypes.HELICS_FILTER_TYPE_DELAY
HELICS_FILTER_TYPE_RANDOM_DELAY = HelicsFilterTypes.HELICS_FILTER_TYPE_RANDOM_DELAY
HELICS_FILTER_TYPE_RANDOM_DROP = HelicsFilterTypes.HELICS_FILTER_TYPE_RANDOM_DROP
HELICS_FILTER_TYPE_REROUTE = HelicsFilterTypes.HELICS_FILTER_TYPE_REROUTE
HELICS_FILTER_TYPE_CLONE = HelicsFilterTypes.HELICS_FILTER_TYPE_CLONE
HELICS_FILTER_TYPE_FIREWALL = HelicsFilterTypes.HELICS_FILTER_TYPE_FIREWALL

helics_filter_type_custom = HelicsFilterTypes.HELICS_FILTER_TYPE_CUSTOM
helics_filter_type_delay = HelicsFilterTypes.HELICS_FILTER_TYPE_DELAY
helics_filter_type_random_delay = HelicsFilterTypes.HELICS_FILTER_TYPE_RANDOM_DELAY
helics_filter_type_random_drop = HelicsFilterTypes.HELICS_FILTER_TYPE_RANDOM_DROP
helics_filter_type_reroute = HelicsFilterTypes.HELICS_FILTER_TYPE_REROUTE
helics_filter_type_clone = HelicsFilterTypes.HELICS_FILTER_TYPE_CLONE
helics_filter_type_firewall = HelicsFilterTypes.HELICS_FILTER_TYPE_FIREWALL


class HelicsSequencingModes(enum.IntEnum):
	""" enumeration of sequencing modes for queries and commands fast is the default, meaning the query travels along priority channels and takes precedence of over existing messages; ordered means it follows normal priority patterns and will be ordered along with existing messages

	Attributes:
		HELICS_SEQUENCING_MODE_FAST: value:0	sequencing mode to operate on priority channels
		HELICS_SEQUENCING_MODE_ORDERED: value:1	sequencing mode to operate on the normal channels
		HELICS_SEQUENCING_MODE_DEFAULT: value:2	select the default channel
	"""

	HELICS_SEQUENCING_MODE_FAST = 0
	HELICS_SEQUENCING_MODE_ORDERED = 1
	HELICS_SEQUENCING_MODE_DEFAULT = 2


HELICS_SEQUENCING_MODE_FAST = HelicsSequencingModes.HELICS_SEQUENCING_MODE_FAST
HELICS_SEQUENCING_MODE_ORDERED = HelicsSequencingModes.HELICS_SEQUENCING_MODE_ORDERED
HELICS_SEQUENCING_MODE_DEFAULT = HelicsSequencingModes.HELICS_SEQUENCING_MODE_DEFAULT

helics_sequencing_mode_fast = HelicsSequencingModes.HELICS_SEQUENCING_MODE_FAST
helics_sequencing_mode_ordered = HelicsSequencingModes.HELICS_SEQUENCING_MODE_ORDERED
helics_sequencing_mode_default = HelicsSequencingModes.HELICS_SEQUENCING_MODE_DEFAULT


class HelicsIterationRequest(enum.IntEnum):
	""" enumeration of the different iteration results

	Attributes:
		HELICS_ITERATION_REQUEST_NO_ITERATION: value:0	no iteration is requested
		HELICS_ITERATION_REQUEST_FORCE_ITERATION: value:1	force iteration return when able
		HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED: value:2	only return an iteration if necessary
	"""

	HELICS_ITERATION_REQUEST_NO_ITERATION = 0
	HELICS_ITERATION_REQUEST_FORCE_ITERATION = 1
	HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED = 2


HELICS_ITERATION_REQUEST_NO_ITERATION = HelicsIterationRequest.HELICS_ITERATION_REQUEST_NO_ITERATION
HELICS_ITERATION_REQUEST_FORCE_ITERATION = HelicsIterationRequest.HELICS_ITERATION_REQUEST_FORCE_ITERATION
HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED = HelicsIterationRequest.HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED

helics_iteration_request_no_iteration = HelicsIterationRequest.HELICS_ITERATION_REQUEST_NO_ITERATION
helics_iteration_request_force_iteration = HelicsIterationRequest.HELICS_ITERATION_REQUEST_FORCE_ITERATION
helics_iteration_request_iterate_if_needed = HelicsIterationRequest.HELICS_ITERATION_REQUEST_ITERATE_IF_NEEDED


class HelicsIterationResult(enum.IntEnum):
	""" enumeration of possible return values from an iterative time request

	Attributes:
		HELICS_ITERATION_RESULT_NEXT_STEP: value:0	the iterations have progressed to the next time
		HELICS_ITERATION_RESULT_ERROR: value:1	there was an error
		HELICS_ITERATION_RESULT_HALTED: value:2	the federation has halted
		HELICS_ITERATION_RESULT_ITERATING: value:3	the federate is iterating at current time
	"""

	HELICS_ITERATION_RESULT_NEXT_STEP = 0
	HELICS_ITERATION_RESULT_ERROR = 1
	HELICS_ITERATION_RESULT_HALTED = 2
	HELICS_ITERATION_RESULT_ITERATING = 3


HELICS_ITERATION_RESULT_NEXT_STEP = HelicsIterationResult.HELICS_ITERATION_RESULT_NEXT_STEP
HELICS_ITERATION_RESULT_ERROR = HelicsIterationResult.HELICS_ITERATION_RESULT_ERROR
HELICS_ITERATION_RESULT_HALTED = HelicsIterationResult.HELICS_ITERATION_RESULT_HALTED
HELICS_ITERATION_RESULT_ITERATING = HelicsIterationResult.HELICS_ITERATION_RESULT_ITERATING

helics_iteration_result_next_step = HelicsIterationResult.HELICS_ITERATION_RESULT_NEXT_STEP
helics_iteration_result_error = HelicsIterationResult.HELICS_ITERATION_RESULT_ERROR
helics_iteration_result_halted = HelicsIterationResult.HELICS_ITERATION_RESULT_HALTED
helics_iteration_result_iterating = HelicsIterationResult.HELICS_ITERATION_RESULT_ITERATING


class HelicsFederateState(enum.IntEnum):
	""" enumeration of possible federate states

	Attributes:
		HELICS_STATE_STARTUP: value:0	when created the federate is in startup state
		HELICS_STATE_INITIALIZATION: value:1	entered after the enterInitializingMode call has returned
		HELICS_STATE_EXECUTION: value:2	entered after the enterExectuationState call has returned
		HELICS_STATE_FINALIZE: value:3	the federate has finished executing normally final values may be retrieved
		HELICS_STATE_ERROR: value:4	error state no core communication is possible but values can be retrieved
		HELICS_STATE_PENDING_INIT: value:5	indicator that the federate is pending entry to initialization state
		HELICS_STATE_PENDING_EXEC: value:6	state pending EnterExecution State
		HELICS_STATE_PENDING_TIME: value:7	state that the federate is pending a timeRequest
		HELICS_STATE_PENDING_ITERATIVE_TIME: value:8	state that the federate is pending an iterative time request
		HELICS_STATE_PENDING_FINALIZE: value:9	state that the federate is pending a finalize request
		HELICS_STATE_FINISHED: value:10	state that the federate is finished simulating but still connected
	"""

	HELICS_STATE_STARTUP = 0
	HELICS_STATE_INITIALIZATION = 1
	HELICS_STATE_EXECUTION = 2
	HELICS_STATE_FINALIZE = 3
	HELICS_STATE_ERROR = 4
	HELICS_STATE_PENDING_INIT = 5
	HELICS_STATE_PENDING_EXEC = 6
	HELICS_STATE_PENDING_TIME = 7
	HELICS_STATE_PENDING_ITERATIVE_TIME = 8
	HELICS_STATE_PENDING_FINALIZE = 9
	HELICS_STATE_FINISHED = 10


HELICS_STATE_STARTUP = HelicsFederateState.HELICS_STATE_STARTUP
HELICS_STATE_INITIALIZATION = HelicsFederateState.HELICS_STATE_INITIALIZATION
HELICS_STATE_EXECUTION = HelicsFederateState.HELICS_STATE_EXECUTION
HELICS_STATE_FINALIZE = HelicsFederateState.HELICS_STATE_FINALIZE
HELICS_STATE_ERROR = HelicsFederateState.HELICS_STATE_ERROR
HELICS_STATE_PENDING_INIT = HelicsFederateState.HELICS_STATE_PENDING_INIT
HELICS_STATE_PENDING_EXEC = HelicsFederateState.HELICS_STATE_PENDING_EXEC
HELICS_STATE_PENDING_TIME = HelicsFederateState.HELICS_STATE_PENDING_TIME
HELICS_STATE_PENDING_ITERATIVE_TIME = HelicsFederateState.HELICS_STATE_PENDING_ITERATIVE_TIME
HELICS_STATE_PENDING_FINALIZE = HelicsFederateState.HELICS_STATE_PENDING_FINALIZE
HELICS_STATE_FINISHED = HelicsFederateState.HELICS_STATE_FINISHED

helics_state_startup = HelicsFederateState.HELICS_STATE_STARTUP
helics_state_initialization = HelicsFederateState.HELICS_STATE_INITIALIZATION
helics_state_execution = HelicsFederateState.HELICS_STATE_EXECUTION
helics_state_finalize = HelicsFederateState.HELICS_STATE_FINALIZE
helics_state_error = HelicsFederateState.HELICS_STATE_ERROR
helics_state_pending_init = HelicsFederateState.HELICS_STATE_PENDING_INIT
helics_state_pending_exec = HelicsFederateState.HELICS_STATE_PENDING_EXEC
helics_state_pending_time = HelicsFederateState.HELICS_STATE_PENDING_TIME
helics_state_pending_iterative_time = HelicsFederateState.HELICS_STATE_PENDING_ITERATIVE_TIME
helics_state_pending_finalize = HelicsFederateState.HELICS_STATE_PENDING_FINALIZE
helics_state_finished = HelicsFederateState.HELICS_STATE_FINISHED


class HelicsInput(_HelicsCHandle):
	"""
	opaque object representing an input
	"""
	pass


class HelicsPublication(_HelicsCHandle):
	"""
	opaque object representing a publication
	"""
	pass


class HelicsEndpoint(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsFilter(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsCore(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsBroker(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsFederate(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsFederateInfo(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsQuery(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsQueryBuffer(_HelicsCHandle):
	"""
	None
	"""
	pass


class HelicsMessage(_HelicsCHandle):
	"""
	None
	"""
	pass


HelicsTime = float


HelicsBool = int


"""
	structure defining a basic complex type

	members:
	real	None
	imag	None
"""
HelicsComplex = ffi.new("HelicsComplex *")


"""
	helics error object

	members:
	error_code	an error code associated with the error
	message	a message associated with the error
"""
HelicsError = ffi.new("HelicsError *")


HELICS_DATA_TYPE_CHAR = HELICS_DATA_TYPE_STRING


HELICS_BIG_NUMBER = 9223372036.854774


HELICS_INVALID_OPTION_INDEX = -101


HELICS_INVALID_PROPERTY_VALUE = 972	#result returned for requesting the value of an invalid/unknown property


cHelicsBigNumber = HELICS_BIG_NUMBER


HELICS_TIME_ZERO = 0.0	#definition of time zero-the beginning of simulation


HELICS_TIME_EPSILON = 1e-09	#definition of the minimum time resolution


HELICS_TIME_INVALID = 1.785e+39	#definition of an invalid time that has no meaning


HELICS_TIME_MAXTIME = HELICS_BIG_NUMBER	#definition of time signifying the federate has terminated or run until the end of the simulation


HELICS_TRUE = 1	#indicator used for a true response


HELICS_FALSE = 0	#indicator used for a false response


def helicsGetVersion() -> str:
	"""
		Get a version string for HELICS.
	"""
	fn = getattr(lib, "helicsGetVersion")
	result = fn()
	return ffi.string(result).decode()


def helicsGetBuildFlags() -> str:
	"""
		Get the build flags used to compile HELICS.
	"""
	fn = getattr(lib, "helicsGetBuildFlags")
	result = fn()
	return ffi.string(result).decode()


def helicsGetCompilerVersion() -> str:
	"""
		Get the compiler version used to compile HELICS.
	"""
	fn = getattr(lib, "helicsGetCompilerVersion")
	result = fn()
	return ffi.string(result).decode()


def helicsGetSystemInfo() -> str:
	"""
		Get a json formatted system information string, containing version info.
		The string contains fields with system information like cpu, core count, operating system, and memory,
		as well as information about the HELICS build.  Used for debugging reports and gathering other information.
	"""
	fn = getattr(lib, "helicsGetSystemInfo")
	result = fn()
	return ffi.string(result).decode()


def helicsErrorInitialize() -> HelicsError:
	"""
		Return an initialized error object.
	"""
	fn = getattr(lib, "helicsErrorInitialize")
	result = fn()
	return ffi.new("HelicsError *",result)


def helicsErrorClear(err):
	"""
		Clear an error object.
	"""
	f = getattr(lib, "helicsErrorClear")
	f(err)


def helicsLoadSignalHandler():
	""" Load a signal handler that handles Ctrl-C and shuts down all HELICS brokers, cores,
and federates then exits the process.*/	"""
	fn = getattr(lib, "helicsLoadSignalHandler")
	fn()


def helicsLoadThreadedSignalHandler():
	""" Load a signal handler that handles Ctrl-C and shuts down all HELICS brokers, cores,
and federates then exits the process.  This operation will execute in a newly created and detached thread returning control back to the
calling program before completing operations.*/	"""
	fn = getattr(lib, "helicsLoadThreadedSignalHandler")
	fn()


def helicsClearSignalHandler():
	""" Clear HELICS based signal handlers.*/	"""
	fn = getattr(lib, "helicsClearSignalHandler")
	fn()


def helicsLoadSignalHandlerCallback(handler, useSeparateThread: bool):
	""" Load a custom signal handler to execute prior to the abort signal handler.
@details  This function is not 100% reliable it will most likely work but uses some functions and
techniques that are not 100% guaranteed to work in a signal handler
and in worst case it could deadlock.  That is somewhat unlikely given usage patterns
but it is possible.  The callback has signature HelicsBool(*handler)(int) and it will take the SIG_INT as an argument
and return a boolean.  If the boolean return value is HELICS_TRUE (or the callback is null) the default signal handler is run after the
callback finishes; if it is HELICS_FALSE the default callback is not run and the default signal handler is executed. If the second
argument is set to HELICS_TRUE the default signal handler will execute in a separate thread(this may be a bad idea)./	"""
	fn = getattr(lib, "helicsLoadSignalHandlerCallback")
	fn(handler, useSeparateThread)


def helicsAbort(errorCode: int, errorString: str):
	""" Execute a global abort by sending an error code to all cores, brokers,
and federates that were created through the current library instance.*/	"""
	fn = getattr(lib, "helicsAbort")
	fn(errorCode, ffi.new("char[]",errorString.encode()))


def helicsIsCoreTypeAvailable(type: str) -> bool:
	"""
		Returns true if core/broker type specified is available in current compilation.

		@param type A string representing a core type.

		@details Options include "zmq", "udp", "ipc", "interprocess", "tcp", "default", "mpi".
	"""
	fn = getattr(lib, "helicsIsCoreTypeAvailable")
	result = fn(ffi.new("char[]",type.encode()))
	return result==1


def helicsCreateCore(type: str, name: str, initString: str) -> HelicsCore:
	"""
		Create a core object.

		@param type The type of the core to create.
		@param name The name of the core. It can be a nullptr or empty string to have a name automatically assigned.
		@param initString An initialization string to send to the core. The format is similar to command line arguments.
		                  Typical options include a broker name, the broker address, the number of federates, etc.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return A HelicsCore object.

		If the core is invalid, err will contain the corresponding error message and the returned object will be NULL.

	"""
	fn = getattr(lib, "helicsCreateCore")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",type.encode()), ffi.new("char[]",name.encode()), ffi.new("char[]",initString.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsCore(result)


def helicsCreateCoreFromArgs(type: str, name: str, arguments: List[str]) -> HelicsCore:
	"""
		Create a core object by passing command line arguments.

		@param type The type of the core to create.
		@param name The name of the core. It can be an empty string to have a name automatically assigned..
		@param arguments The list of string values from a command line.

		@return A HelicsCore object.
	"""
	fn = getattr(lib, "helicsCreateCoreFromArgs")
	err = helicsErrorInitialize()
	argc = len(arguments)
	argv = ffi.new("char*[{argc}]".format(argc=argc))
	for i, s in enumerate(arguments):
		argv[i] = ffi.new("char[]",s.encode())
	result = fn(ffi.new("char[]",type.encode()), ffi.new("char[]",name.encode()), argc, argv, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsCore(result)


def helicsCoreClone(core: HelicsCore) -> HelicsCore:
	"""
		Create a new reference to an existing core.

		@details This will create a new broker object that references the existing broker. The new broker object must be freed as well.

		@param core An existing HelicsCore.
		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A new reference to the same broker.
	"""
	fn = getattr(lib, "helicsCoreClone")
	err = helicsErrorInitialize()
	result = fn(core.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsCore(result)


def helicsCoreIsValid(core: HelicsCore) -> bool:
	"""
		Check if a core object is a valid object.

		@param core The HelicsCore object to test.
	"""
	fn = getattr(lib, "helicsCoreIsValid")
	result = fn(core.handle)
	return result==1


def helicsCreateBroker(type: str, name: str, initString: str) -> HelicsBroker:
	"""
		Create a broker object.

		@param type The type of the broker to create.
		@param name The name of the broker. It can be a nullptr or empty string to have a name automatically assigned.
		@param initString An initialization string to send to the core-the format is similar to command line arguments.
		                  Typical options include a broker address such as --broker="XSSAF" if this is a subbroker, or the number of federates,
		or the address.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return A HelicsBroker object.

		It will be NULL if there was an error indicated in the err object.

	"""
	fn = getattr(lib, "helicsCreateBroker")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",type.encode()), ffi.new("char[]",name.encode()), ffi.new("char[]",initString.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsBroker(result)


def helicsCreateBrokerFromArgs(type: str, name: str, arguments: List[str]) -> HelicsBroker:
	"""
		Create a core object by passing command line arguments.

		@param type The type of the core to create.
		@param name The name of the core. It can be an empty string to have a name automatically assigned.
		@param arguments The list of string values from a command line.

		@return a HelicsBroker object.
	"""
	fn = getattr(lib, "helicsCreateBrokerFromArgs")
	err = helicsErrorInitialize()
	argc = len(arguments)
	argv = ffi.new("char*[{argc}]".format(argc=argc))
	for i, s in enumerate(arguments):
		argv[i] = ffi.new("char[]",s.encode())
	result = fn(ffi.new("char[]",type.encode()), ffi.new("char[]",name.encode()), argc, argv, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsBroker(result)


def helicsBrokerClone(broker: HelicsBroker) -> HelicsBroker:
	"""
		Create a new reference to an existing broker.

		@details This will create a new broker object that references the existing broker it must be freed as well.

		@param broker An existing HelicsBroker.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return A new reference to the same broker.
	"""
	fn = getattr(lib, "helicsBrokerClone")
	err = helicsErrorInitialize()
	result = fn(broker.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsBroker(result)


def helicsBrokerIsValid(broker: HelicsBroker) -> bool:
	"""
		Check if a broker object is a valid object.

		@param broker The HelicsBroker object to test.
	"""
	fn = getattr(lib, "helicsBrokerIsValid")
	result = fn(broker.handle)
	return result==1


def helicsBrokerIsConnected(broker: HelicsBroker) -> bool:
	"""
		Check if a broker is connected.

		@details A connected broker implies it is attached to cores or cores could reach out to communicate.

		@return HELICS_FALSE if not connected.
	"""
	fn = getattr(lib, "helicsBrokerIsConnected")
	result = fn(broker.handle)
	return result==1


def helicsBrokerDataLink(broker: HelicsBroker, source: str, target: str):
	"""
		Link a named publication and named input using a broker.

		@param broker The broker to generate the connection from.
		@param source The name of the publication (cannot be NULL).
		@param target The name of the target to send the publication data (cannot be NULL).

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsBrokerDataLink")
	err = helicsErrorInitialize()
	fn(broker.handle, ffi.new("char[]",source.encode()), ffi.new("char[]",target.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddSourceFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
	"""
		Link a named filter to a source endpoint.

		@param broker The broker to generate the connection from.
		@param filter The name of the filter (cannot be NULL).
		@param endpoint The name of the endpoint to filter the data from (cannot be NULL).

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsBrokerAddSourceFilterToEndpoint")
	err = helicsErrorInitialize()
	fn(broker.handle, ffi.new("char[]",filter.encode()), ffi.new("char[]",endpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerAddDestinationFilterToEndpoint(broker: HelicsBroker, filter: str, endpoint: str):
	"""
		Link a named filter to a destination endpoint.

		@param broker The broker to generate the connection from.
		@param filter The name of the filter (cannot be NULL).
		@param endpoint The name of the endpoint to filter the data going to (cannot be NULL).

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsBrokerAddDestinationFilterToEndpoint")
	err = helicsErrorInitialize()
	fn(broker.handle, ffi.new("char[]",filter.encode()), ffi.new("char[]",endpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerMakeConnections(broker: HelicsBroker, file: str):
	"""
		Load a file containing connection information.

		@param broker The broker to generate the connections from.
		@param file A JSON or TOML file containing connection information.

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsBrokerMakeConnections")
	err = helicsErrorInitialize()
	fn(broker.handle, ffi.new("char[]",file.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreWaitForDisconnect(core: HelicsCore, msToWait: int) -> bool:
	"""
		Wait for the core to disconnect.

		@param core The core to wait for.
		@param msToWait The time out in millisecond (<0 for infinite timeout).

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return HELICS_TRUE if the disconnect was successful, HELICS_FALSE if there was a timeout.
	"""
	fn = getattr(lib, "helicsCoreWaitForDisconnect")
	err = helicsErrorInitialize()
	result = fn(core.handle, msToWait, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result==1


def helicsBrokerWaitForDisconnect(broker: HelicsBroker, msToWait: int) -> bool:
	"""
		Wait for the broker to disconnect.

		@param broker The broker to wait for.
		@param msToWait The time out in millisecond (<0 for infinite timeout).

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return HELICS_TRUE if the disconnect was successful, HELICS_FALSE if there was a timeout.
	"""
	fn = getattr(lib, "helicsBrokerWaitForDisconnect")
	err = helicsErrorInitialize()
	result = fn(broker.handle, msToWait, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result==1


def helicsCoreIsConnected(core: HelicsCore) -> bool:
	"""
		Check if a core is connected.

		@details A connected core implies it is attached to federates or federates could be attached to it

		@return HELICS_FALSE if not connected, HELICS_TRUE if it is connected.
	"""
	fn = getattr(lib, "helicsCoreIsConnected")
	result = fn(core.handle)
	return result==1


def helicsCoreDataLink(core: HelicsCore, source: str, target: str):
	"""
		Link a named publication and named input using a core.

		@param core The core to generate the connection from.
		@param source The name of the publication (cannot be NULL).
		@param target The name of the target to send the publication data (cannot be NULL).

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsCoreDataLink")
	err = helicsErrorInitialize()
	fn(core.handle, ffi.new("char[]",source.encode()), ffi.new("char[]",target.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddSourceFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
	"""
		Link a named filter to a source endpoint.

		@param core The core to generate the connection from.
		@param filter The name of the filter (cannot be NULL).
		@param endpoint The name of the endpoint to filter the data from (cannot be NULL).

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsCoreAddSourceFilterToEndpoint")
	err = helicsErrorInitialize()
	fn(core.handle, ffi.new("char[]",filter.encode()), ffi.new("char[]",endpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreAddDestinationFilterToEndpoint(core: HelicsCore, filter: str, endpoint: str):
	"""
		Link a named filter to a destination endpoint.

		@param core The core to generate the connection from.
		@param filter The name of the filter (cannot be NULL).
		@param endpoint The name of the endpoint to filter the data going to (cannot be NULL).

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsCoreAddDestinationFilterToEndpoint")
	err = helicsErrorInitialize()
	fn(core.handle, ffi.new("char[]",filter.encode()), ffi.new("char[]",endpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreMakeConnections(core: HelicsCore, file: str):
	"""
		Load a file containing connection information.

		@param core The core to generate the connections from.
		@param file A JSON or TOML file containing connection information.

		@param[in,out] err A HelicsError object, can be NULL if the errors are to be ignored.

	"""
	fn = getattr(lib, "helicsCoreMakeConnections")
	err = helicsErrorInitialize()
	fn(core.handle, ffi.new("char[]",file.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerGetIdentifier(broker: HelicsBroker) -> str:
	"""
		Get an identifier for the broker.

		@param broker The broker to query.

		@return A string containing the identifier for the broker.
	"""
	fn = getattr(lib, "helicsBrokerGetIdentifier")
	result = fn(broker.handle)
	return ffi.string(result).decode()


def helicsCoreGetIdentifier(core: HelicsCore) -> str:
	"""
		Get an identifier for the core.

		@param core The core to query.

		@return A string with the identifier of the core.
	"""
	fn = getattr(lib, "helicsCoreGetIdentifier")
	result = fn(core.handle)
	return ffi.string(result).decode()


def helicsBrokerGetAddress(broker: HelicsBroker) -> str:
	"""
		Get the network address associated with a broker.

		@param broker The broker to query.

		@return A string with the network address of the broker.
	"""
	fn = getattr(lib, "helicsBrokerGetAddress")
	result = fn(broker.handle)
	return ffi.string(result).decode()


def helicsCoreGetAddress(core: HelicsCore) -> str:
	"""
		Get the network address associated with a core.

		@param core The core to query.

		@return A string with the network address of the broker.
	"""
	fn = getattr(lib, "helicsCoreGetAddress")
	result = fn(core.handle)
	return ffi.string(result).decode()


def helicsCoreSetReadyToInit(core: HelicsCore):
	"""
		Set the core to ready for init.

		@details This function is used for cores that have filters but no federates so there needs to be
		         a direct signal to the core to trigger the federation initialization.

		@param core The core object to enable init values for.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsCoreSetReadyToInit")
	err = helicsErrorInitialize()
	fn(core.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreConnect(core: HelicsCore) -> bool:
	"""
		Connect a core to the federate based on current configuration.

		@param core The core to connect.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return HELICS_FALSE if not connected, HELICS_TRUE if it is connected.
	"""
	fn = getattr(lib, "helicsCoreConnect")
	err = helicsErrorInitialize()
	result = fn(core.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result==1


def helicsCoreDisconnect(core: HelicsCore):
	"""
		Disconnect a core from the federation.

		@param core The core to query.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsCoreDisconnect")
	err = helicsErrorInitialize()
	fn(core.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetFederateByName(fedName: str) -> HelicsFederate:
	"""
		Get an existing federate object from a core by name.

		@details The federate must have been created by one of the other functions and at least one of the objects referencing the created
		         federate must still be active in the process.

		@param fedName The name of the federate to retrieve.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return NULL if no fed is available by that name otherwise a HelicsFederate with that name.
	"""
	fn = getattr(lib, "helicsGetFederateByName")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",fedName.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsBrokerDisconnect(broker: HelicsBroker):
	"""
		Disconnect a broker.

		@param broker The broker to disconnect.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsBrokerDisconnect")
	err = helicsErrorInitialize()
	fn(broker.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateDestroy(fed: HelicsFederate):
	"""
		Disconnect and free a federate.
	"""
	fn = getattr(lib, "helicsFederateDestroy")
	fn(fed.handle)


def helicsBrokerDestroy(broker: HelicsBroker):
	"""
		Disconnect and free a broker.
	"""
	fn = getattr(lib, "helicsBrokerDestroy")
	fn(broker.handle)


def helicsCoreDestroy(core: HelicsCore):
	"""
		Disconnect and free a core.
	"""
	fn = getattr(lib, "helicsCoreDestroy")
	fn(core.handle)


def helicsCoreFree(core: HelicsCore):
	"""
		Release the memory associated with a core.
	"""
	fn = getattr(lib, "helicsCoreFree")
	fn(core.handle)


def helicsBrokerFree(broker: HelicsBroker):
	"""
		Release the memory associated with a broker.
	"""
	fn = getattr(lib, "helicsBrokerFree")
	fn(broker.handle)


def helicsCreateValueFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
	"""
		Create a value federate from a federate info object.

		@details HelicsFederate objects can be used in all functions that take a HelicsFederate or HelicsFederate object as an argument.

		@param fedName The name of the federate to create, can NULL or an empty string to use the default name from fi or an assigned name.
		@param fi The federate info object that contains details on the federate.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return An opaque value federate object.
	"""
	fn = getattr(lib, "helicsCreateValueFederate")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",fedName.encode()), fi.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsCreateValueFederateFromConfig(configFile: str) -> HelicsFederate:
	"""
		Create a value federate from a JSON file, JSON string, or TOML file.

		@details HelicsFederate objects can be used in all functions that take a HelicsFederate or HelicsFederate object as an argument.

		@param configFile A JSON file or a JSON string or TOML file that contains setup and configuration information.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return An opaque value federate object.
	"""
	fn = getattr(lib, "helicsCreateValueFederateFromConfig")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",configFile.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsCreateMessageFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
	"""
		Create a message federate from a federate info object.

		@details helics_message_federate objects can be used in all functions that take a helics_message_federate or HelicsFederate object as an
		argument.

		@param fedName The name of the federate to create.
		@param fi The federate info object that contains details on the federate.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return An opaque message federate object.
	"""
	fn = getattr(lib, "helicsCreateMessageFederate")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",fedName.encode()), fi.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsCreateMessageFederateFromConfig(configFile: str) -> HelicsFederate:
	"""
		Create a message federate from a JSON file or JSON string or TOML file.

		@details helics_message_federate objects can be used in all functions that take a helics_message_federate or HelicsFederate object as an
		argument.

		@param configFile A Config(JSON,TOML) file or a JSON string that contains setup and configuration information.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return An opaque message federate object.
	"""
	fn = getattr(lib, "helicsCreateMessageFederateFromConfig")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",configFile.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsCreateCombinationFederate(fedName: str, fi: HelicsFederateInfo) -> HelicsFederate:
	"""
		Create a combination federate from a federate info object.

		@details Combination federates are both value federates and message federates, objects can be used in all functions
		                     that take a HelicsFederate, helics_message_federate or HelicsFederate object as an argument

		@param fedName A string with the name of the federate, can be NULL or an empty string to pull the default name from fi.
		@param fi The federate info object that contains details on the federate.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return An opaque value federate object nullptr if the object creation failed.
	"""
	fn = getattr(lib, "helicsCreateCombinationFederate")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",fedName.encode()), fi.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsCreateCombinationFederateFromConfig(configFile: str) -> HelicsFederate:
	"""
		Create a combination federate from a JSON file or JSON string or TOML file.

		@details Combination federates are both value federates and message federates, objects can be used in all functions
		         that take a HelicsFederate, helics_message_federate or HelicsFederate object as an argument

		@param configFile A JSON file or a JSON string or TOML file that contains setup and configuration information.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return An opaque combination federate object.
	"""
	fn = getattr(lib, "helicsCreateCombinationFederateFromConfig")
	err = helicsErrorInitialize()
	result = fn(ffi.new("char[]",configFile.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsFederateClone(fed: HelicsFederate) -> HelicsFederate:
	"""
		Create a new reference to an existing federate.

		@details This will create a new HelicsFederate object that references the existing federate. The new object must be freed as well.

		@param fed An existing HelicsFederate.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return A new reference to the same federate.
	"""
	fn = getattr(lib, "helicsFederateClone")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederate(result)


def helicsCreateFederateInfo() -> HelicsFederateInfo:
	"""
		Create a federate info object for specifying federate information when constructing a federate.

		@return A HelicsFederateInfo object which is a reference to the created object.
	"""
	fn = getattr(lib, "helicsCreateFederateInfo")
	result = fn()
	return HelicsFederateInfo(result)


def helicsFederateInfoClone(fi: HelicsFederateInfo) -> HelicsFederateInfo:
	"""
		Create a federate info object from an existing one and clone the information.

		@param fi A federateInfo object to duplicate.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		 @return A HelicsFederateInfo object which is a reference to the created object.
	"""
	fn = getattr(lib, "helicsFederateInfoClone")
	err = helicsErrorInitialize()
	result = fn(fi.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederateInfo(result)


def helicsFederateInfoLoadFromArgs(fi: HelicsFederateInfo, arguments: List[str]):
	"""
		Load federate info from command line arguments.

		@param fi A federateInfo object.
		@param arguments A list of strings from the command line.
	"""
	fn = getattr(lib, "helicsFederateInfoLoadFromArgs")
	err = helicsErrorInitialize()
	argc = len(arguments)
	argv = ffi.new("char*[{argc}]".format(argc=argc))
	for i, s in enumerate(arguments):
		argv[i] = ffi.new("char[]",s.encode())
	fn(fi.handle, argc, argv, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoLoadFromString(fi: HelicsFederateInfo, args: str):
	"""
		Load federate info from command line arguments contained in a string.

		@param fi A federateInfo object.
		@param args Command line arguments specified in a string.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoLoadFromString")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",args.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoFree(fi: HelicsFederateInfo):
	"""
		Delete the memory associated with a federate info object.
	"""
	fn = getattr(lib, "helicsFederateInfoFree")
	fn(fi.handle)


def helicsFederateIsValid(fed: HelicsFederate) -> bool:
	"""
		Check if a federate_object is valid.

		@return HELICS_TRUE if the federate is a valid active federate, HELICS_FALSE otherwise
	"""
	fn = getattr(lib, "helicsFederateIsValid")
	result = fn(fed.handle)
	return result==1


def helicsFederateInfoSetCoreName(fi: HelicsFederateInfo, corename: str):
	"""
		Set the name of the core to link to for a federate.

		@param fi The federate info object to alter.
		@param corename The identifier for a core to link to.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetCoreName")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",corename.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreInitString(fi: HelicsFederateInfo, coreInit: str):
	"""
		Set the initialization string for the core usually in the form of command line arguments.

		@param fi The federate info object to alter.
		@param coreInit A string containing command line arguments to be passed to the core.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetCoreInitString")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",coreInit.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerInitString(fi: HelicsFederateInfo, brokerInit: str):
	"""
		Set the initialization string that a core will pass to a generated broker usually in the form of command line arguments.

		@param fi The federate info object to alter.
		@param brokerInit A string with command line arguments for a generated broker.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetBrokerInitString")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",brokerInit.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreType(fi: HelicsFederateInfo, coretype: int):
	"""
		Set the core type by integer code.

		@details Valid values available by definitions in api-data.h.
		@param fi The federate info object to alter.
		@param coretype An numerical code for a core type see /ref helics_CoreType.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetCoreType")
	err = helicsErrorInitialize()
	fn(fi.handle, coretype, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetCoreTypeFromString(fi: HelicsFederateInfo, coretype: str):
	"""
		Set the core type from a string.

		@param fi The federate info object to alter.
		@param coretype A string naming a core type.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetCoreTypeFromString")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",coretype.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBroker(fi: HelicsFederateInfo, broker: str):
	"""
		Set the name or connection information for a broker.

		@details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
		@param fi The federate info object to alter.
		@param broker A string which defines the connection information for a broker either a name or an address.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetBroker")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",broker.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerKey(fi: HelicsFederateInfo, brokerkey: str):
	"""
		Set the key for a broker connection.

		@details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
		@param fi The federate info object to alter.
		@param brokerkey A string containing a key for the broker to connect.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetBrokerKey")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",brokerkey.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetBrokerPort(fi: HelicsFederateInfo, brokerPort: int):
	"""
		Set the port to use for the broker.

		@details This is only used if the core is automatically created, the broker information will be transferred to the core for connection.
		This will only be useful for network broker connections.
		@param fi The federate info object to alter.
		@param brokerPort The integer port number to use for connection with a broker.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetBrokerPort")
	err = helicsErrorInitialize()
	fn(fi.handle, brokerPort, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetLocalPort(fi: HelicsFederateInfo, localPort: str):
	"""
		Set the local port to use.

		@details This is only used if the core is automatically created, the port information will be transferred to the core for connection.
		@param fi The federate info object to alter.
		@param localPort A string with the port information to use as the local server port can be a number or "auto" or "os_local".

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateInfoSetLocalPort")
	err = helicsErrorInitialize()
	fn(fi.handle, ffi.new("char[]",localPort.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsGetPropertyIndex(val: str) -> HelicsProperties:
	"""
		Get a property index for use in /ref helicsFederateInfoSetFlagOption, /ref helicsFederateInfoSetTimeProperty,
		or /ref helicsFederateInfoSetIntegerProperty
		@param val A string with the property name.
		@return An HelicsProperties with the property code or (-1) if not a valid property.
	"""
	fn = getattr(lib, "helicsGetPropertyIndex")
	result = fn(ffi.new("char[]",val.encode()))
	if result == -1 or result == -101:
		raise HelicsException(f"[-1] Unknown index for HelicsProperties {val}")
	else:
		return HelicsProperties(result)


def helicsGetFlagIndex(val: str) -> HelicsFederateFlags:
	"""
		Get a property index for use in /ref helicsFederateInfoSetFlagOption, /ref helicsFederateSetFlagOption,
		@param val A string with the option name.
		@return An HelicsFederateFlags with the property code or (-1) if not a valid property.
	"""
	fn = getattr(lib, "helicsGetFlagIndex")
	result = fn(ffi.new("char[]",val.encode()))
	if result == -1 or result == -101:
		raise HelicsException(f"[-1] Unknown index for HelicsFederateFlags {val}")
	else:
		return HelicsFederateFlags(result)


def helicsGetOptionIndex(val: str) -> HelicsHandleOptions:
	"""
		Get an option index for use in /ref helicsPublicationSetOption, /ref helicsInputSetOption, /ref helicsEndpointSetOption,
		/ref helicsFilterSetOption, and the corresponding get functions.
		@param val A string with the option name.
		@return An HelicsHandleOptions with the property code or (-1) if not a valid property.
	"""
	fn = getattr(lib, "helicsGetOptionIndex")
	result = fn(ffi.new("char[]",val.encode()))
	if result == -1 or result == -101:
		raise HelicsException(f"[-1] Unknown index for HelicsHandleOptions {val}")
	else:
		return HelicsHandleOptions(result)


def helicsGetOptionValue(val: str) -> int:
	"""
		Get an option index for use in /ref helicsPublicationSetOption, /ref helicsInputSetOption, /ref helicsEndpointSetOption,
		or /ref helicsFederateInfoSetIntegerProperty
		@param val A string with the option name.
		@return An int with the property code or (-1) if not a valid property.
	"""
	fn = getattr(lib, "helicsGetOptionValue")
	result = fn(ffi.new("char[]",val.encode()))
	if result == -1 or result == -101:
		raise HelicsException(f"[-1] Unknown option value for flag {val}")
	else:
		return result


def helicsGetDataType(val: str) -> int:
	"""
		Get the data type for use in /ref helicsFederateRegisterPublication, /ref helicsFederateRegisterInput,
		/ref helicsFilterSetOption.

		@param val A string representing a data type.

		@return An int with the data type or HELICS_DATA_TYPE_UNKNOWN(-1) if not a valid value.
	"""
	fn = getattr(lib, "helicsGetDataType")
	result = fn(ffi.new("char[]",val.encode()))
	return result


def helicsFederateInfoSetFlagOption(fi: HelicsFederateInfo, flag: int, value: bool):
	"""
		Set a flag in the info structure.

		@details Valid flags are available /ref helics_federate_flags.
		@param fi The federate info object to alter.
		@param flag A numerical index for a flag.
		@param value The desired value of the flag HELICS_TRUE or HELICS_FALSE.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateInfoSetFlagOption")
	err = helicsErrorInitialize()
	fn(fi.handle, flag, value, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetSeparator(fi: HelicsFederateInfo, separator: str):
	"""
		Set the separator character in the info structure.

		@details The separator character is the separation character for local publications/endpoints in creating their global name.
		For example if the separator character is '/'  then a local endpoint would have a globally reachable name of fedName/localName.
		@param fi The federate info object to alter.
		@param separator The character to use as a separator.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateInfoSetSeparator")
	err = helicsErrorInitialize()
	fn(fi.handle, separator.encode(), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetTimeProperty(fi: HelicsFederateInfo, timeProperty: int, propertyValue: HelicsTime):
	"""
		Set the output delay for a federate.

		@param fi The federate info object to alter.
		@param timeProperty An integer representation of the time based property to set see /ref helics_properties.
		@param propertyValue The value of the property to set the timeProperty to.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateInfoSetTimeProperty")
	err = helicsErrorInitialize()
	fn(fi.handle, timeProperty, propertyValue, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateInfoSetIntegerProperty(fi: HelicsFederateInfo, intProperty: int, propertyValue: int):
	"""
		Set an integer property for a federate.

		@details Set known properties.

		@param fi The federateInfo object to alter.
		@param intProperty An int identifying the property.
		@param propertyValue The value to set the property to.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateInfoSetIntegerProperty")
	err = helicsErrorInitialize()
	fn(fi.handle, intProperty, propertyValue, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRegisterInterfaces(fed: HelicsFederate, file: str):
	"""
		Load interfaces from a file.

		@param fed The federate to which to load interfaces.
		@param file The name of a file to load the interfaces from either JSON, or TOML.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateRegisterInterfaces")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",file.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGlobalError(fed: HelicsFederate, errorCode: int, errorString: str):
	"""
		Generate a global error from a federate.

		@details A global error halts the co-simulation completely.

		@param fed The federate to create an error in.
		@param errorCode The integer code for the error.
		@param errorString A string describing the error.
		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateGlobalError")
	err = helicsErrorInitialize()
	fn(fed.handle, errorCode, ffi.new("char[]",errorString.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLocalError(fed: HelicsFederate, errorCode: int, errorString: str):
	"""
		Generate a local error in a federate.

		@details This will propagate through the co-simulation but not necessarily halt the co-simulation, it has a similar effect to finalize
		but does allow some interaction with a core for a brief time.
		@param fed The federate to create an error in.
		@param errorCode The integer code for the error.
		@param errorString A string describing the error.
		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateLocalError")
	err = helicsErrorInitialize()
	fn(fed.handle, errorCode, ffi.new("char[]",errorString.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFinalize(fed: HelicsFederate):
	"""
		Disconnect/finalize the federate. This function halts all communication in the federate and disconnects it from the core.
	"""
	fn = getattr(lib, "helicsFederateFinalize")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFinalizeAsync(fed: HelicsFederate):
	"""
		Disconnect/finalize the federate in an async call.
	"""
	fn = getattr(lib, "helicsFederateFinalizeAsync")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFinalizeComplete(fed: HelicsFederate):
	"""
		Complete the asynchronous disconnect/finalize call.
	"""
	fn = getattr(lib, "helicsFederateFinalizeComplete")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateDisconnect(fed: HelicsFederate):
	"""
		Disconnect/finalize the federate. This function halts all communication in the federate and disconnects it
		from the core.  This call is identical to helicsFederateFinalize.
	"""
	fn = getattr(lib, "helicsFederateDisconnect")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateDisconnectAsync(fed: HelicsFederate):
	"""
		Disconnect/finalize the federate in an async call.  This call is identical to helicsFederateFinalizeAsync.
	"""
	fn = getattr(lib, "helicsFederateDisconnectAsync")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateDisconnectComplete(fed: HelicsFederate):
	"""
		Complete the asynchronous disconnect/finalize call.  This call is identical to helicsFederateFinalizeComplete
	"""
	fn = getattr(lib, "helicsFederateDisconnectComplete")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateFree(fed: HelicsFederate):
	"""
		Release the memory associated with a federate.
	"""
	fn = getattr(lib, "helicsFederateFree")
	fn(fed.handle)


def helicsCloseLibrary():
	"""
		Call when done using the helics library.
		This function will ensure the threads are closed properly. If possible this should be the last call before exiting.
	"""
	fn = getattr(lib, "helicsCloseLibrary")
	fn()


def helicsFederateEnterInitializingMode(fed: HelicsFederate):
	"""
		Enter the initialization state of a federate.

		@details The initialization state allows initial values to be set and received if the iteration is requested on entry to the execution
		state. This is a blocking call and will block until the core allows it to proceed.

		@param fed The federate to operate on.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateEnterInitializingMode")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterInitializingModeAsync(fed: HelicsFederate):
	"""
		Non blocking alternative to \ref helicsFederateEnterInitializingMode.

		@details The function helicsFederateEnterInitializationModeFinalize must be called to finish the operation.

		@param fed The federate to operate on.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateEnterInitializingModeAsync")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateIsAsyncOperationCompleted(fed: HelicsFederate) -> bool:
	"""
		Check if the current Asynchronous operation has completed.

		@param fed The federate to operate on.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return HELICS_FALSE if not completed, HELICS_TRUE if completed.
	"""
	fn = getattr(lib, "helicsFederateIsAsyncOperationCompleted")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result==1


def helicsFederateEnterInitializingModeComplete(fed: HelicsFederate):
	"""
		Finalize the entry to initialize mode that was initiated with /ref heliceEnterInitializingModeAsync.

		@param fed The federate desiring to complete the initialization step.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateEnterInitializingModeComplete")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingMode(fed: HelicsFederate):
	"""
		Request that the federate enter the Execution mode.

		@details This call is blocking until granted entry by the core object. On return from this call the federate will be at time 0.
		         For an asynchronous alternative call see /ref helicsFederateEnterExecutingModeAsync.

		@param fed A federate to change modes.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateEnterExecutingMode")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeAsync(fed: HelicsFederate):
	"""
		Request that the federate enter the Execution mode.

		@details This call is non-blocking and will return immediately. Call /ref helicsFederateEnterExecutingModeComplete to finish the call
		sequence.

		@param fed The federate object to complete the call.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateEnterExecutingModeAsync")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeComplete(fed: HelicsFederate):
	"""
		Complete the call to /ref helicsFederateEnterExecutingModeAsync.

		@param fed The federate object to complete the call.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateEnterExecutingModeComplete")
	err = helicsErrorInitialize()
	fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterative(fed: HelicsFederate, iterate: HelicsIterationRequest) -> HelicsIterationResult:
	"""
		Request an iterative time.

		@details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
		         iteration request, and returns a time and iteration status.

		@param fed The federate to make the request of.
		@param iterate The requested iteration mode.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return An iteration structure with field containing the time and iteration status.
	"""
	fn = getattr(lib, "helicsFederateEnterExecutingModeIterative")
	err = helicsErrorInitialize()
	result = fn(fed.handle, HelicsIterationRequest(iterate), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsIterationResult(result)


def helicsFederateEnterExecutingModeIterativeAsync(fed: HelicsFederate, iterate: HelicsIterationRequest):
	"""
		Request an iterative entry to the execution mode.

		@details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
		         iteration request, and returns a time and iteration status

		@param fed The federate to make the request of.
		@param iterate The requested iteration mode.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateEnterExecutingModeIterativeAsync")
	err = helicsErrorInitialize()
	fn(fed.handle, HelicsIterationRequest(iterate), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateEnterExecutingModeIterativeComplete(fed: HelicsFederate) -> HelicsIterationResult:
	"""
		Complete the asynchronous iterative call into ExecutionMode.

		@param fed The federate to make the request of.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return An iteration object containing the iteration time and iteration_status.
	"""
	fn = getattr(lib, "helicsFederateEnterExecutingModeIterativeComplete")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsIterationResult(result)


def helicsFederateGetState(fed: HelicsFederate) -> HelicsFederateState:
	"""
		Get the current state of a federate.

		@param fed The federate to query.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return State the resulting state if void return HELICS_OK.
	"""
	fn = getattr(lib, "helicsFederateGetState")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFederateState(result)


def helicsFederateGetCore(fed: HelicsFederate) -> HelicsCore:
	"""
		Get the core object associated with a federate.

		@param fed A federate object.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A core object, nullptr if invalid.
	"""
	fn = getattr(lib, "helicsFederateGetCore")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsCore(result)


def helicsFederateRequestTime(fed: HelicsFederate, requestTime: HelicsTime) -> HelicsTime:
	"""
		Request the next time for federate execution.

		@param fed The federate to make the request of.
		@param requestTime The next requested time.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return The time granted to the federate, will return HELICS_TIME_MAXTIME if the simulation has terminated or is invalid.
	"""
	fn = getattr(lib, "helicsFederateRequestTime")
	err = helicsErrorInitialize()
	result = fn(fed.handle, requestTime, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsFederateRequestTimeAdvance(fed: HelicsFederate, timeDelta: HelicsTime) -> HelicsTime:
	"""
		Request the next time for federate execution.

		@param fed The federate to make the request of.
		@param timeDelta The requested amount of time to advance.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return The time granted to the federate, will return HELICS_TIME_MAXTIME if the simulation has terminated or is invalid
	"""
	fn = getattr(lib, "helicsFederateRequestTimeAdvance")
	err = helicsErrorInitialize()
	result = fn(fed.handle, timeDelta, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsFederateRequestNextStep(fed: HelicsFederate) -> HelicsTime:
	"""
		Request the next time step for federate execution.

		@details Feds should have setup the period or minDelta for this to work well but it will request the next time step which is the current
		time plus the minimum time step.

		@param fed The federate to make the request of.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return The time granted to the federate, will return HELICS_TIME_MAXTIME if the simulation has terminated or is invalid
	"""
	fn = getattr(lib, "helicsFederateRequestNextStep")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsFederateRequestTimeIterative(fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest) -> Tuple[HelicsTime, HelicsIterationResult]:
	"""
		Request an iterative time.

		@details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and and
		iteration request, and returns a time and iteration status.

		@param fed The federate to make the request of.
		@param requestTime The next desired time.
		@param iterate The requested iteration mode.

		@return tuple of HelicsTime and HelicsIterationResult.
	"""
	fn = getattr(lib, "helicsFederateRequestTimeIterative")
	outIteration = ffi.new("HelicsIterationResult *")
	err = helicsErrorInitialize()
	result = fn(fed.handle, requestTime, HelicsIterationRequest(iterate), outIteration, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return (result, HelicsIterationResult(outIteration[0]))


def helicsFederateRequestTimeAsync(fed: HelicsFederate, requestTime: HelicsTime):
	"""
		Request the next time for federate execution in an asynchronous call.

		@details Call /ref helicsFederateRequestTimeComplete to finish the call.

		@param fed The federate to make the request of.
		@param requestTime The next requested time.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateRequestTimeAsync")
	err = helicsErrorInitialize()
	fn(fed.handle, requestTime, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeComplete(fed: HelicsFederate) -> HelicsTime:
	"""
		Complete an asynchronous requestTime call.

		@param fed The federate to make the request of.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return The time granted to the federate, will return HELICS_TIME_MAXTIME if the simulation has terminated.
	"""
	fn = getattr(lib, "helicsFederateRequestTimeComplete")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsFederateRequestTimeIterativeAsync(fed: HelicsFederate, requestTime: HelicsTime, iterate: HelicsIterationRequest):
	"""
		Request an iterative time through an asynchronous call.

		@details This call allows for finer grain control of the iterative process than /ref helicsFederateRequestTime. It takes a time and
		iteration request, and returns a time and iteration status. Call /ref helicsFederateRequestTimeIterativeComplete to finish the process.

		@param fed The federate to make the request of.
		@param requestTime The next desired time.
		@param iterate The requested iteration mode.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateRequestTimeIterativeAsync")
	err = helicsErrorInitialize()
	fn(fed.handle, requestTime, HelicsIterationRequest(iterate), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRequestTimeIterativeComplete(fed: HelicsFederate) -> Tuple[HelicsTime, HelicsIterationResult]:
	"""
		Complete an iterative time request asynchronous call.

		@param fed The federate to make the request of.

		@return tuple of HelicsTime and HelicsIterationResult.
	"""
	fn = getattr(lib, "helicsFederateRequestTimeIterativeComplete")
	outIterate = ffi.new("HelicsIterationResult *")
	err = helicsErrorInitialize()
	result = fn(fed.handle, outIterate, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return (result, HelicsIterationResult(outIterate[0]))


def helicsFederateProcessCommunications(fed: HelicsFederate, period: HelicsTime):
	"""
		Tell helics to process internal communications for a period of time.

		@param fed The federate to tell to process.

		@param period The length of time to process communications and then return control.
		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

	"""
	fn = getattr(lib, "helicsFederateProcessCommunications")
	err = helicsErrorInitialize()
	fn(fed.handle, period, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetName(fed: HelicsFederate) -> str:
	"""
		Get the name of the federate.

		@param fed The federate object to query.

		@return A pointer to a string with the name.
	"""
	fn = getattr(lib, "helicsFederateGetName")
	result = fn(fed.handle)
	return ffi.string(result).decode()


def helicsFederateSetTimeProperty(fed: HelicsFederate, timeProperty: int, time: HelicsTime):
	"""
		Set a time based property for a federate.

		@param fed The federate object to set the property for.
		@param timeProperty A integer code for a time property.
		@param time The requested value of the property.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateSetTimeProperty")
	err = helicsErrorInitialize()
	fn(fed.handle, timeProperty, time, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetFlagOption(fed: HelicsFederate, flag: int, flagValue: bool):
	"""
		Set a flag for the federate.

		@param fed The federate to alter a flag for.
		@param flag The flag to change.
		@param flagValue The new value of the flag. 0 for false, !=0 for true.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateSetFlagOption")
	err = helicsErrorInitialize()
	fn(fed.handle, flag, flagValue, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetSeparator(fed: HelicsFederate, separator: str):
	"""
		Set the separator character in a federate.

		@details The separator character is the separation character for local publications/endpoints in creating their global name.
		         For example if the separator character is '/' then a local endpoint would have a globally reachable name of fedName/localName.

		@param fed The federate info object to alter.
		@param separator The character to use as a separator.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateSetSeparator")
	err = helicsErrorInitialize()
	fn(fed.handle, separator.encode(), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetIntegerProperty(fed: HelicsFederate, intProperty: int, propertyVal: int):
	"""
		Set an integer based property of a federate.

		@param fed The federate to change the property for.
		@param intProperty The property to set.
		@param propertyVal The value of the property.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateSetIntegerProperty")
	err = helicsErrorInitialize()
	fn(fed.handle, intProperty, propertyVal, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetTimeProperty(fed: HelicsFederate, timeProperty: int) -> HelicsTime:
	"""
		Get the current value of a time based property in a federate.

		@param fed The federate query.
		@param timeProperty The property to query.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateGetTimeProperty")
	err = helicsErrorInitialize()
	result = fn(fed.handle, timeProperty, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsFederateGetFlagOption(fed: HelicsFederate, flag: int) -> bool:
	"""
		Get a flag value for a federate.

		@param fed The federate to get the flag for.
		@param flag The flag to query.

		@param[in,out] err A pointer to an error object for catching errors.

		@return The value of the flag.
	"""
	fn = getattr(lib, "helicsFederateGetFlagOption")
	err = helicsErrorInitialize()
	result = fn(fed.handle, flag, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result==1


def helicsFederateGetIntegerProperty(fed: HelicsFederate, intProperty: int) -> int:
	"""
		Get the current value of an integer property (such as a logging level).

		@param fed The federate to get the flag for.
		@param intProperty A code for the property to set /ref helics_handle_options.

		@param[in,out] err A pointer to an error object for catching errors.

		@return The value of the property.
	"""
	fn = getattr(lib, "helicsFederateGetIntegerProperty")
	err = helicsErrorInitialize()
	result = fn(fed.handle, intProperty, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsFederateGetCurrentTime(fed: HelicsFederate) -> HelicsTime:
	"""
		Get the current time of the federate.

		@param fed The federate object to query.

		@param[in,out] err A pointer to an error object for catching errors.

		@return The current time of the federate.
	"""
	fn = getattr(lib, "helicsFederateGetCurrentTime")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsFederateSetGlobal(fed: HelicsFederate, valueName: str, value: str):
	"""
		Set a federation global value through a federate.

		@details This overwrites any previous value for this name.
		@param fed The federate to set the global through.
		@param valueName The name of the global to set.
		@param value The value of the global.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateSetGlobal")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",valueName.encode()), ffi.new("char[]",value.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetTag(fed: HelicsFederate, tagName: str, value: str):
	"""
		Set a federate tag value.

		@details This overwrites any previous value for this tag.
		@param fed The federate to set the tag for.
		@param tagName The name of the tag to set.
		@param value The value of the tag.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateSetTag")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",tagName.encode()), ffi.new("char[]",value.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetTag(fed: HelicsFederate, tagName: str) -> str:
	"""
		Get a federate tag value.

		@param fed The federate to get the tag for.
		@param tagName The name of the tag to query.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateGetTag")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",tagName.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsFederateAddDependency(fed: HelicsFederate, fedName: str):
	"""
		Add a time dependency for a federate. The federate will depend on the given named federate for time synchronization.

		@param fed The federate to add the dependency for.
		@param fedName The name of the federate to depend on.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateAddDependency")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",fedName.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetLogFile(fed: HelicsFederate, logFile: str):
	"""
		Set the logging file for a federate (actually on the core associated with a federate).

		@param fed The federate to set the log file for.
		@param logFile The name of the log file.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateSetLogFile")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",logFile.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogErrorMessage(fed: HelicsFederate, logmessage: str):
	"""
		Log an error message through a federate.

		@param fed The federate to log the error message through.
		@param logmessage The message to put in the log.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateLogErrorMessage")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",logmessage.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogWarningMessage(fed: HelicsFederate, logmessage: str):
	"""
		Log a warning message through a federate.

		@param fed The federate to log the warning message through.
		@param logmessage The message to put in the log.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateLogWarningMessage")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",logmessage.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogInfoMessage(fed: HelicsFederate, logmessage: str):
	"""
		Log an info message through a federate.

		@param fed The federate to log the info message through.
		@param logmessage The message to put in the log.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateLogInfoMessage")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",logmessage.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogDebugMessage(fed: HelicsFederate, logmessage: str):
	"""
		Log a debug message through a federate.

		@param fed The federate to log the debug message through.
		@param logmessage The message to put in the log.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateLogDebugMessage")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",logmessage.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateLogLevelMessage(fed: HelicsFederate, loglevel: int, logmessage: str):
	"""
		Log a message through a federate.

		@param fed The federate to log the message through.
		@param loglevel The level of the message to log see /ref helics_log_levels.
		@param logmessage The message to put in the log.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsFederateLogLevelMessage")
	err = helicsErrorInitialize()
	fn(fed.handle, loglevel, ffi.new("char[]",logmessage.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSendCommand(fed: HelicsFederate, target: str, command: str):
	"""
		Send a command to another helics object through a federate.

		@param fed The federate to send the command through.
		@param target The name of the object to send the command to.
		@param command The command to send.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsFederateSendCommand")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",target.encode()), ffi.new("char[]",command.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateGetCommand(fed: HelicsFederate) -> str:
	"""
		Get a command sent to the federate.

		@param fed The federate to get the command for.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A string with the command for the federate, if the string is empty no command is available.
	"""
	fn = getattr(lib, "helicsFederateGetCommand")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsFederateGetCommandSource(fed: HelicsFederate) -> str:
	"""
		Get the source of the most recently retrieved command sent to the federate.

		@param fed The federate to get the command for.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A string with the command for the federate, if the string is empty no command is available.
	"""
	fn = getattr(lib, "helicsFederateGetCommandSource")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsFederateWaitCommand(fed: HelicsFederate) -> str:
	"""
		Get a command sent to the federate. Blocks until a command is received.

		@param fed The federate to get the command for.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A string with the command for the federate, if the string is empty no command is available.
	"""
	fn = getattr(lib, "helicsFederateWaitCommand")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsCoreSetGlobal(core: HelicsCore, valueName: str, value: str):
	"""
		Set a global value in a core.

		@details This overwrites any previous value for this name.

		@param core The core to set the global through.
		@param valueName The name of the global to set.
		@param value The value of the global.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsCoreSetGlobal")
	err = helicsErrorInitialize()
	fn(core.handle, ffi.new("char[]",valueName.encode()), ffi.new("char[]",value.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetGlobal(broker: HelicsBroker, valueName: str, value: str):
	"""
		Set a federation global value.

		@details This overwrites any previous value for this name.

		@param broker The broker to set the global through.
		@param valueName The name of the global to set.
		@param value The value of the global.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsBrokerSetGlobal")
	err = helicsErrorInitialize()
	fn(broker.handle, ffi.new("char[]",valueName.encode()), ffi.new("char[]",value.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSendCommand(core: HelicsCore, target: str, command: str):
	"""
		Send a command to another helics object though a core.

		@param core The core to send the command through.
		@param target The name of the object to send the command to.
		@param command The command to send.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsCoreSendCommand")
	err = helicsErrorInitialize()
	fn(core.handle, ffi.new("char[]",target.encode()), ffi.new("char[]",command.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSendCommand(broker: HelicsBroker, target: str, command: str):
	"""
		Send a command to another helics object through a broker.

		@param broker The broker to send the command through.
		@param target The name of the object to send the command to.
		@param command The command to send.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsBrokerSendCommand")
	err = helicsErrorInitialize()
	fn(broker.handle, ffi.new("char[]",target.encode()), ffi.new("char[]",command.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetLogFile(core: HelicsCore, logFileName: str):
	"""
		Set the log file on a core.

		@param core The core to set the log file for.
		@param logFileName The name of the file to log to.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsCoreSetLogFile")
	err = helicsErrorInitialize()
	fn(core.handle, ffi.new("char[]",logFileName.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetLogFile(broker: HelicsBroker, logFileName: str):
	"""
		Set the log file on a broker.

		@param broker The broker to set the log file for.
		@param logFileName The name of the file to log to.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsBrokerSetLogFile")
	err = helicsErrorInitialize()
	fn(broker.handle, ffi.new("char[]",logFileName.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerSetTimeBarrier(broker: HelicsBroker, barrierTime: HelicsTime):
	"""
		Set a broker time barrier.

		@param broker The broker to set the time barrier for.
		@param barrierTime The time to set the barrier at.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsBrokerSetTimeBarrier")
	err = helicsErrorInitialize()
	fn(broker.handle, barrierTime, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsBrokerClearTimeBarrier(broker: HelicsBroker):
	"""
		Clear any time barrier on a broker.

		@param broker The broker to clear the barriers on.
	"""
	fn = getattr(lib, "helicsBrokerClearTimeBarrier")
	fn(broker.handle)


def helicsBrokerGlobalError(broker: HelicsBroker, errorCode: int, errorString: str):
	"""
		Generate a global error through a broker. This will terminate the federation.

		@param broker The broker to generate the global error on.
		@param errorCode The error code to associate with the global error.
		@param errorString An error message to associate with the global error.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsBrokerGlobalError")
	err = helicsErrorInitialize()
	fn(broker.handle, errorCode, ffi.new("char[]",errorString.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreGlobalError(core: HelicsCore, errorCode: int, errorString: str):
	"""
		Generate a global error through a broker. This will terminate the federation.

		@param core The core to generate the global error.
		@param errorCode The error code to associate with the global error.
		@param errorString An error message to associate with the global error.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsCoreGlobalError")
	err = helicsErrorInitialize()
	fn(core.handle, errorCode, ffi.new("char[]",errorString.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCreateQuery(target: str, query: str) -> HelicsQuery:
	"""
		Create a query object.

		@details A query object consists of a target and query string.

		@param target The name of the target to query.
		@param query The query to make of the target.
	"""
	fn = getattr(lib, "helicsCreateQuery")
	result = fn(ffi.new("char[]",target.encode()), ffi.new("char[]",query.encode()))
	return HelicsQuery(result)


def helicsQueryExecute(query: HelicsQuery, fed: HelicsFederate) -> str:
	"""
		Execute a query.

		@details The call will block until the query finishes which may require communication or other delays.

		@param query The query object to use in the query.
		@param fed A federate to send the query through.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.


		@return A pointer to a string.  The string will remain valid until the query is freed or executed again.
		The return will be nullptr if fed or query is an invalid object, the return string will be "#invalid" if the query itself was
		invalid.
	"""
	fn = getattr(lib, "helicsQueryExecute")
	err = helicsErrorInitialize()
	result = fn(query.handle, fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsQueryCoreExecute(query: HelicsQuery, core: HelicsCore) -> str:
	"""
		Execute a query directly on a core.

		@details The call will block until the query finishes which may require communication or other delays.

		@param query The query object to use in the query.
		@param core The core to send the query to.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A pointer to a string.  The string will remain valid until the query is freed or executed again.
		The return will be nullptr if core or query is an invalid object, the return string will be "#invalid" if the query itself was
		invalid.
	"""
	fn = getattr(lib, "helicsQueryCoreExecute")
	err = helicsErrorInitialize()
	result = fn(query.handle, core.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsQueryBrokerExecute(query: HelicsQuery, broker: HelicsBroker) -> str:
	"""
		Execute a query directly on a broker.

		@details The call will block until the query finishes which may require communication or other delays.

		@param query The query object to use in the query.
		@param broker The broker to send the query to.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A pointer to a string.  The string will remain valid until the query is freed or executed again.
		The return will be nullptr if broker or query is an invalid object, the return string will be "#invalid" if the query itself was
		invalid
	"""
	fn = getattr(lib, "helicsQueryBrokerExecute")
	err = helicsErrorInitialize()
	result = fn(query.handle, broker.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsQueryExecuteAsync(query: HelicsQuery, fed: HelicsFederate):
	"""
		Execute a query in a non-blocking call.

		@param query The query object to use in the query.
		@param fed A federate to send the query through.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsQueryExecuteAsync")
	err = helicsErrorInitialize()
	fn(query.handle, fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryExecuteComplete(query: HelicsQuery) -> str:
	"""
		Complete the return from a query called with /ref helicsExecuteQueryAsync.

		@details The function will block until the query completes /ref isQueryComplete can be called to determine if a query has completed or
		not.

		@param query The query object to complete execution of.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.

		@return A pointer to a string. The string will remain valid until the query is freed or executed again.
		The return will be nullptr if query is an invalid object
	"""
	fn = getattr(lib, "helicsQueryExecuteComplete")
	err = helicsErrorInitialize()
	result = fn(query.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(result).decode()


def helicsQueryIsCompleted(query: HelicsQuery) -> bool:
	"""
		Check if an asynchronously executed query has completed.

		@details This function should usually be called after a QueryExecuteAsync function has been called.

		@param query The query object to check if completed.

		@return Will return HELICS_TRUE if an asynchronous query has completed or a regular query call was made with a result,
		and false if an asynchronous query has not completed or is invalid
	"""
	fn = getattr(lib, "helicsQueryIsCompleted")
	result = fn(query.handle)
	return result==1


def helicsQuerySetTarget(query: HelicsQuery, target: str):
	"""
		Update the target of a query.

		@param query The query object to change the target of.
		@param target the name of the target to query


		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsQuerySetTarget")
	err = helicsErrorInitialize()
	fn(query.handle, ffi.new("char[]",target.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQuerySetQueryString(query: HelicsQuery, queryString: str):
	"""
		Update the queryString of a query.

		@param query The query object to change the target of.
		@param queryString the new queryString

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsQuerySetQueryString")
	err = helicsErrorInitialize()
	fn(query.handle, ffi.new("char[]",queryString.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQuerySetOrdering(query: HelicsQuery, mode: int):
	"""
		Update the ordering mode of the query, fast runs on priority channels, ordered goes on normal channels but goes in sequence

		@param query The query object to change the order for.
		@param mode 0 for fast, 1 for ordered


		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsQuerySetOrdering")
	err = helicsErrorInitialize()
	fn(query.handle, mode, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryFree(query: HelicsQuery):
	"""
		Free the memory associated with a query object.
	"""
	fn = getattr(lib, "helicsQueryFree")
	fn(query.handle)


def helicsCleanupLibrary():
	"""
		Function to do some housekeeping work.

		@details This runs some cleanup routines and tries to close out any residual thread that haven't been shutdown yet.
	"""
	fn = getattr(lib, "helicsCleanupLibrary")
	fn()


def helicsFederateRegisterSubscription(fed: HelicsFederate, key: str, units: str) -> HelicsInput:
	"""
		Create a subscription.

		@details The subscription becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions and publications.

		@param fed The federate object in which to create a subscription, must have been created with /ref helicsCreateValueFederate or
		/ref helicsCreateCombinationFederate.
		@param key The identifier matching a publication to get a subscription for.
		@param units A string listing the units of the subscription (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the subscription.
	"""
	fn = getattr(lib, "helicsFederateRegisterSubscription")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsInput(result)


def helicsFederateRegisterPublication(fed: HelicsFederate, key: str, type: HelicsDataTypes, units: str) -> HelicsPublication:
	"""
		Register a publication with a known type.

		@details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions and publications.

		@param fed The federate object in which to create a publication.
		@param key The identifier for the publication the global publication key will be prepended with the federate name.
		@param type A code identifying the type of the input see /ref HelicsDataTypes for available options.
		@param units A string listing the units of the subscription (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the publication.
	"""
	fn = getattr(lib, "helicsFederateRegisterPublication")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), HelicsDataTypes(type), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateRegisterTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
	"""
		Register a publication with a defined type.

		@details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions and publications.

		@param fed The federate object in which to create a publication.
		@param key The identifier for the publication.
		@param type A string labeling the type of the publication.
		@param units A string listing the units of the subscription (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the publication.
	"""
	fn = getattr(lib, "helicsFederateRegisterTypePublication")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), ffi.new("char[]",type.encode()), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateRegisterGlobalPublication(fed: HelicsFederate, key: str, type: HelicsDataTypes, units: str) -> HelicsPublication:
	"""
		Register a global named publication with an arbitrary type.

		@details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions and publications.

		@param fed The federate object in which to create a publication.
		@param key The identifier for the publication.
		@param type A code identifying the type of the input see /ref HelicsDataTypes for available options.
		@param units A string listing the units of the subscription (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the publication.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalPublication")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), HelicsDataTypes(type), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateRegisterGlobalTypePublication(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
	"""
		Register a global publication with a defined type.

		@details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions and publications.

		@param fed The federate object in which to create a publication.
		@param key The identifier for the publication.
		@param type A string describing the expected type of the publication.
		@param units A string listing the units of the subscription (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the publication.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalTypePublication")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), ffi.new("char[]",type.encode()), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateRegisterInput(fed: HelicsFederate, key: str, type: HelicsDataTypes, units: str) -> HelicsInput:
	"""
		Register a named input.

		@details The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions, inputs, and publications.

		@param fed The federate object in which to create an input.
		@param key The identifier for the publication the global input key will be prepended with the federate name.
		@param type A code identifying the type of the input see /ref HelicsDataTypes for available options.
		@param units A string listing the units of the input (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the input.
	"""
	fn = getattr(lib, "helicsFederateRegisterInput")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), HelicsDataTypes(type), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsInput(result)


def helicsFederateRegisterTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsInput:
	"""
		Register an input with a defined type.

		@details The input becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions, inputs, and publications.

		@param fed The federate object in which to create an input.
		@param key The identifier for the input.
		@param type A string describing the expected type of the input.
		@param units A string listing the units of the input maybe NULL.

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the publication.
	"""
	fn = getattr(lib, "helicsFederateRegisterTypeInput")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), ffi.new("char[]",type.encode()), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsInput(result)


def helicsFederateRegisterGlobalInput(fed: HelicsFederate, key: str, type: HelicsDataTypes, units: str) -> HelicsPublication:
	"""
		Register a global named input.

		@details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions and publications.

		@param fed The federate object in which to create a publication.
		@param key The identifier for the publication.
		@param type A code identifying the type of the input see /ref HelicsDataTypes for available options.
		@param units A string listing the units of the subscription maybe NULL.

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the publication.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalInput")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), HelicsDataTypes(type), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateRegisterGlobalTypeInput(fed: HelicsFederate, key: str, type: str, units: str) -> HelicsPublication:
	"""
		Register a global publication with an arbitrary type.

		@details The publication becomes part of the federate and is destroyed when the federate is freed so there are no separate free
		functions for subscriptions and publications.

		@param fed The federate object in which to create a publication.
		@param key The identifier for the publication.
		@param type A string defining the type of the input.
		@param units A string listing the units of the subscription maybe NULL.

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the publication.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalTypeInput")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), ffi.new("char[]",type.encode()), ffi.new("char[]",units.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateGetPublication(fed: HelicsFederate, key: str) -> HelicsPublication:
	"""
		Get a publication object from a key.

		@param fed The value federate object to use to get the publication.
		@param key The name of the publication.

		@param[in,out] err The error object to complete if there is an error.


		@return A HelicsPublication object, the object will not be valid and err will contain an error code if no publication with the
		specified key exists.
	"""
	fn = getattr(lib, "helicsFederateGetPublication")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateGetPublicationByIndex(fed: HelicsFederate, index: int) -> HelicsPublication:
	"""
		Get a publication by its index, typically already created via registerInterfaces file or something of that nature.

		@param fed The federate object in which to create a publication.
		@param index The index of the publication to get.

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsPublication.
	"""
	fn = getattr(lib, "helicsFederateGetPublicationByIndex")
	err = helicsErrorInitialize()
	result = fn(fed.handle, index, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsPublication(result)


def helicsFederateGetInput(fed: HelicsFederate, key: str) -> HelicsInput:
	"""
		Get an input object from a key.

		@param fed The value federate object to use to get the publication.
		@param key The name of the input.

		@param[in,out] err The error object to complete if there is an error.


		@return A HelicsInput object, the object will not be valid and err will contain an error code if no input with the specified
		key exists.
	"""
	fn = getattr(lib, "helicsFederateGetInput")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsInput(result)


def helicsFederateGetInputByIndex(fed: HelicsFederate, index: int) -> HelicsInput:
	"""
		Get an input by its index, typically already created via registerInterfaces file or something of that nature.

		@param fed The federate object in which to create a publication.
		@param index The index of the publication to get.

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsInput, which will be NULL if an invalid index.
	"""
	fn = getattr(lib, "helicsFederateGetInputByIndex")
	err = helicsErrorInitialize()
	result = fn(fed.handle, index, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsInput(result)


def helicsFederateGetSubscription(fed: HelicsFederate, key: str) -> HelicsInput:
	"""
		Get an input object from a subscription target.

		@param fed The value federate object to use to get the publication.
		@param key The name of the publication that a subscription is targeting.

		@param[in,out] err The error object to complete if there is an error.


		@return A HelicsInput object, the object will not be valid and err will contain an error code if no input with the specified
		key exists.
	"""
	fn = getattr(lib, "helicsFederateGetSubscription")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",key.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsInput(result)


def helicsFederateClearUpdates(fed: HelicsFederate):
	"""
		Clear all the update flags from a federates inputs.

		@param fed The value federate object for which to clear update flags.
	"""
	fn = getattr(lib, "helicsFederateClearUpdates")
	fn(fed.handle)


def helicsFederateRegisterFromPublicationJSON(fed: HelicsFederate, json: str):
	"""
		Register the publications via JSON publication string.

		@param fed The value federate object to use to register the publications.
		@param json The JSON publication string.

		@param[in,out] err The error object to complete if there is an error.


		@details This would be the same JSON that would be used to publish data.
	"""
	fn = getattr(lib, "helicsFederateRegisterFromPublicationJSON")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",json.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederatePublishJSON(fed: HelicsFederate, json: str):
	"""
		Publish data contained in a JSON file or string.

		@param fed The value federate object through which to publish the data.
		@param json The publication file name or literal JSON data string.

		@param[in,out] err The error object to complete if there is an error.

	"""
	fn = getattr(lib, "helicsFederatePublishJSON")
	err = helicsErrorInitialize()
	fn(fed.handle, ffi.new("char[]",json.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationIsValid(pub: HelicsPublication) -> bool:
	"""
		Check if a publication is valid.

		@param pub The publication to check.

		@return HELICS_TRUE if the publication is a valid publication.
	"""
	fn = getattr(lib, "helicsPublicationIsValid")
	result = fn(pub.handle)
	return result==1


def helicsPublicationPublishBytes(pub: HelicsPublication, data: bytes):
	"""
		Publish raw data.

		@param pub The publication to publish for.
		@param data the raw byte data to publish.
	"""
	fn = getattr(lib, "helicsPublicationPublishBytes")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(pub.handle, data, inputDataLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishString(pub: HelicsPublication, string: str):
	"""
		Publish a string.

		@param pub The publication to publish for.
		@param str The string to publish.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishString")
	err = helicsErrorInitialize()
	fn(pub.handle, ffi.new("char[]",string.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishInteger(pub: HelicsPublication, val: int):
	"""
		Publish an integer value.

		@param pub The publication to publish for.
		@param val The numerical value to publish.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishInteger")
	err = helicsErrorInitialize()
	fn(pub.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishBoolean(pub: HelicsPublication, val: bool):
	"""
		Publish a Boolean Value.

		@param pub The publication to publish for.
		@param val The boolean value to publish.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishBoolean")
	err = helicsErrorInitialize()
	fn(pub.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishDouble(pub: HelicsPublication, val: float):
	"""
		Publish a double floating point value.

		@param pub The publication to publish for.
		@param val The numerical value to publish.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishDouble")
	err = helicsErrorInitialize()
	fn(pub.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishTime(pub: HelicsPublication, val: HelicsTime):
	"""
		Publish a time value.

		@param pub The publication to publish for.
		@param val The numerical value to publish.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishTime")
	err = helicsErrorInitialize()
	fn(pub.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishChar(pub: HelicsPublication, val: str):
	"""
		Publish a single character.

		@param pub The publication to publish for.
		@param val The numerical value to publish.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishChar")
	err = helicsErrorInitialize()
	fn(pub.handle, val.encode(), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishComplex(pub: HelicsPublication, value: complex):
	"""
		Publish a complex number.

		@param pub The publication to publish for.
		@param value The complex number.
	"""
	fn = getattr(lib, "helicsPublicationPublishComplex")
	err = helicsErrorInitialize()
	fn(pub.handle, value.real, value.imag, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishVector(pub: HelicsPublication, vectorInput: List[float]):
	"""
		Publish a vector of doubles.

		@param pub The publication to publish for.
		@param vectorInput The list of floating point values.
	"""
	fn = getattr(lib, "helicsPublicationPublishVector")
	vectorLength = len(vectorInput)
	err = helicsErrorInitialize()
	fn(pub.handle, vectorInput, vectorLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishComplexVector(pub: HelicsPublication, vectorInput: float, vectorLength: int):
	"""
		Publish a vector of complex doubles.

		@param pub The publication to publish for.
		@param vectorInput A pointer to an array of complex double data (alternating real and imaginary values).

		@param vectorLength The number of values to publish; vectorInput must contain 2xvectorLength values.
		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishComplexVector")
	err = helicsErrorInitialize()
	fn(pub.handle, vectorInput, vectorLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationPublishNamedPoint(pub: HelicsPublication, string: str, val: float):
	"""
		Publish a named point.

		@param pub The publication to publish for.
		@param str A string for the name to publish.
		@param val A double for the value to publish.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationPublishNamedPoint")
	err = helicsErrorInitialize()
	fn(pub.handle, ffi.new("char[]",string.encode()), val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationAddTarget(pub: HelicsPublication, target: str):
	"""
		Add a named input to the list of targets a publication publishes to.

		@param pub The publication to add the target for.
		@param target The name of an input that the data should be sent to.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsPublicationAddTarget")
	err = helicsErrorInitialize()
	fn(pub.handle, ffi.new("char[]",target.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsValid(ipt: HelicsInput) -> bool:
	"""
		Check if an input is valid.

		@param ipt The input to check.

		@return HELICS_TRUE if the Input object represents a valid input.
	"""
	fn = getattr(lib, "helicsInputIsValid")
	result = fn(ipt.handle)
	return result==1


def helicsInputAddTarget(ipt: HelicsInput, target: str):
	"""
		Add a publication to the list of data that an input subscribes to.

		@param ipt The named input to modify.
		@param target The name of a publication that an input should subscribe to.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsInputAddTarget")
	err = helicsErrorInitialize()
	fn(ipt.handle, ffi.new("char[]",target.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetByteCount(ipt: HelicsInput) -> int:
	"""
		Get the size of the raw value for subscription.

		@return The size of the raw data/string in bytes.
	"""
	fn = getattr(lib, "helicsInputGetByteCount")
	result = fn(ipt.handle)
	return result


def helicsInputGetBytes(ipt: HelicsInput) -> bytes:
	"""
		Get the raw data for the latest value of a subscription.

		@param ipt The input to get the data for.

		@return  raw Bytes of the value, the value is uninterpreted raw bytes.
	"""
	fn = getattr(lib, "helicsInputGetBytes")
	maxDataLen = helicsInputGetByteCount(ipt) + 1024
	data = ffi.new(f"char[{maxDataLen}]")
	actualSize = ffi.new("int[1]")
	err = helicsErrorInitialize()
	fn(ipt.handle, data, maxDataLen, actualSize, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.unpack(data, length=actualSize[0])


def helicsInputGetStringSize(ipt: HelicsInput) -> int:
	"""
		Get the size of a value for subscription assuming return as a string.

		@return The size of the string.
	"""
	fn = getattr(lib, "helicsInputGetStringSize")
	result = fn(ipt.handle)
	return result


def helicsInputGetString(ipt: HelicsInput) -> str:
	"""
		Get a string value from a subscription.

		@param ipt The input to get the string for.

		@return  the string value.
	"""
	fn = getattr(lib, "helicsInputGetString")
	maxStringLength = helicsInputGetStringSize(ipt) + 1024
	outputString = ffi.new(f"char[{maxStringLength}]")
	actualLength = ffi.new("int[1]")
	err = helicsErrorInitialize()
	fn(ipt.handle, outputString, maxStringLength, actualLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.string(outputString, maxlen=actualLength[0]).decode()


def helicsInputGetInteger(ipt: HelicsInput) -> int:
	"""
		Get an integer value from a subscription.

		@param ipt The input to get the data for.

		@param[in,out] err A pointer to an error object for catching errors.

		@return An int64_t value with the current value of the input.
	"""
	fn = getattr(lib, "helicsInputGetInteger")
	err = helicsErrorInitialize()
	result = fn(ipt.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsInputGetBoolean(ipt: HelicsInput) -> bool:
	"""
		Get a boolean value from a subscription.

		@param ipt The input to get the data for.

		@param[in,out] err A pointer to an error object for catching errors.

		@return A boolean value of current input value.
	"""
	fn = getattr(lib, "helicsInputGetBoolean")
	err = helicsErrorInitialize()
	result = fn(ipt.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result==1


def helicsInputGetDouble(ipt: HelicsInput) -> float:
	"""
		Get a double value from a subscription.

		@param ipt The input to get the data for.

		@param[in,out] err A pointer to an error object for catching errors.

		@return The double value of the input.
	"""
	fn = getattr(lib, "helicsInputGetDouble")
	err = helicsErrorInitialize()
	result = fn(ipt.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsInputGetTime(ipt: HelicsInput) -> HelicsTime:
	"""
		Get a time value from a subscription.

		@param ipt The input to get the data for.

		@param[in,out] err A pointer to an error object for catching errors.

		@return The resulting time value.
	"""
	fn = getattr(lib, "helicsInputGetTime")
	err = helicsErrorInitialize()
	result = fn(ipt.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result


def helicsInputGetChar(ipt: HelicsInput) -> str:
	"""
		Get a single character value from an input.

		@param ipt The input to get the data for.

		@param[in,out] err A pointer to an error object for catching errors.

		@return The resulting character value.
		        NAK (negative acknowledgment) symbol returned on error
	"""
	fn = getattr(lib, "helicsInputGetChar")
	err = helicsErrorInitialize()
	result = fn(ipt.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return result.decode()


def helicsInputGetComplexObject(ipt: HelicsInput) -> complex:
	"""
		Get a complex value from an input object.

		@param ipt The input to get the data for.

		@return  A complex number.
	"""
	fn = getattr(lib, "helicsInputGetComplexObject")
	err = helicsErrorInitialize()
	result = fn(ipt.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return complex(result.real, result.imag)


def helicsInputGetComplex(ipt: HelicsInput) -> complex:
	"""
		Get a complex value from an input object.

		@param ipt The input to get the data for.

		@return  A complex number.
	"""
	fn = getattr(lib, "helicsInputGetComplex")
	real = ffi.new("double *")
	imag = ffi.new("double *")
	err = helicsErrorInitialize()
	fn(ipt.handle, real, imag, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return complex(real[0], imag[0])


def helicsInputGetVectorSize(ipt: HelicsInput) -> int:
	"""
		Get the size of a value for subscription assuming return as an array of doubles.

		@return The number of doubles in a returned vector.
	"""
	fn = getattr(lib, "helicsInputGetVectorSize")
	result = fn(ipt.handle)
	return result


def helicsInputGetVector(ipt: HelicsInput) -> List[float]:
	"""
		Get a vector from a subscription.

		@param ipt The input to get the vector for.

		@return  a list of floating point values.
	"""
	fn = getattr(lib, "helicsInputGetVector")
	maxLength = helicsInputGetVectorSize(ipt) + 1024
	data = ffi.new(f"double[{maxLength}]")
	actualSize = ffi.new("int[1]")
	err = helicsErrorInitialize()
	fn(ipt.handle, data, maxLength, actualSize, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return [x for x in data][0 : actualSize[0]]


def helicsInputGetComplexVector(ipt: HelicsInput, data: List[float], maxLength: int, actualSize: int):
	"""
		Get a complex vector from an input.

		@param ipt The input to get the result for.

		@param[out] data The location to store the data. The data will be stored in alternating real and imaginary values.
		@param maxLength The maximum number of values data can hold.
		@param[out] actualSize Location to place the actual length of the resulting complex vector (will be 1/2 the number of values assigned).
		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputGetComplexVector")
	actualSize = ffi.new("int[1]")
	err = helicsErrorInitialize()
	fn(ipt.handle, data, maxLength, actualSize, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetNamedPoint(ipt: HelicsInput) -> Tuple[str, float]:
	"""
		Get a named point from a subscription.

		@param ipt The input to get the result for.

		@return a tuple of a string and a double value for the named point
	"""
	fn = getattr(lib, "helicsInputGetNamedPoint")
	maxStringLen = helicsInputGetStringSize(ipt) + 1024
	outputString = ffi.new(f"char[{maxStringLen}]")
	actualLength = ffi.new("int[1]")
	val = ffi.new("double[1]")
	err = helicsErrorInitialize()
	fn(ipt.handle, outputString, maxStringLen, actualLength, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return (ffi.string(outputString, maxlen=actualLength[0]).decode(), val[0])


def helicsInputSetDefaultBytes(ipt: HelicsInput, data: bytes):
	"""
		Set the default as a raw data array.

		@param ipt The input to set the default for.
		@param data A pointer to the raw data to use for the default.
	"""
	fn = getattr(lib, "helicsInputSetDefaultBytes")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(ipt.handle, data, inputDataLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultString(ipt: HelicsInput, string: str):
	"""
		Set the default as a string.

		@param ipt The input to set the default for.
		@param str A pointer to the default string.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultString")
	err = helicsErrorInitialize()
	fn(ipt.handle, ffi.new("char[]",string.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultInteger(ipt: HelicsInput, val: int):
	"""
		Set the default as an integer.

		@param ipt The input to set the default for.
		@param val The default integer.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultInteger")
	err = helicsErrorInitialize()
	fn(ipt.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultBoolean(ipt: HelicsInput, val: bool):
	"""
		Set the default as a boolean.

		@param ipt The input to set the default for.
		@param val The default boolean value.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultBoolean")
	err = helicsErrorInitialize()
	fn(ipt.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultTime(ipt: HelicsInput, val: HelicsTime):
	"""
		Set the default as a time.

		@param ipt The input to set the default for.
		@param val The default time value.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultTime")
	err = helicsErrorInitialize()
	fn(ipt.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultChar(ipt: HelicsInput, val: str):
	"""
		Set the default as a char.

		@param ipt The input to set the default for.
		@param val The default char value.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultChar")
	err = helicsErrorInitialize()
	fn(ipt.handle, val.encode(), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultDouble(ipt: HelicsInput, val: float):
	"""
		Set the default as a double.

		@param ipt The input to set the default for.
		@param val The default double value.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultDouble")
	err = helicsErrorInitialize()
	fn(ipt.handle, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultComplex(ipt: HelicsInput, value: complex):
	"""
		Set the default as a complex number.

		@param ipt The input to get the data for.
		@param value The default complex value.
	"""
	fn = getattr(lib, "helicsInputSetDefaultComplex")
	err = helicsErrorInitialize()
	fn(ipt.handle, value.real, value.imag, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultVector(ipt: HelicsInput, vectorInput: List[float]):
	"""
		Set the default as a list of floats.

		@param ipt The input to get the data for.
		@param vectorInput The default list of floating point values.
	"""
	fn = getattr(lib, "helicsInputSetDefaultVector")
	vectorLength = len(vectorInput)
	err = helicsErrorInitialize()
	fn(ipt.handle, vectorInput, vectorLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultComplexVector(ipt: HelicsInput, vectorInput: float, vectorLength: int):
	"""
		Set the default as a vector of complex doubles. The format is alternating real, imag doubles.

		@param ipt The input to set the default for.
		@param vectorInput A pointer to an array of double data alternating between real and imaginary.
		@param vectorLength the number of complex values in the publication (vectorInput must contain 2xvectorLength elements).

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultComplexVector")
	err = helicsErrorInitialize()
	fn(ipt.handle, vectorInput, vectorLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetDefaultNamedPoint(ipt: HelicsInput, string: str, val: float):
	"""
		Set the default as a NamedPoint.

		@param ipt The input to set the default for.
		@param str A pointer to a string representing the name.
		@param val A double value for the value of the named point.

		@param[in,out] err An error object that will contain an error code and string if any error occurred during the execution of the function.
	"""
	fn = getattr(lib, "helicsInputSetDefaultNamedPoint")
	err = helicsErrorInitialize()
	fn(ipt.handle, ffi.new("char[]",string.encode()), val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetType(ipt: HelicsInput) -> str:
	"""
		Get the type of an input.

		@param ipt The input to query.

		@return A void enumeration, HELICS_OK if everything worked.
	"""
	fn = getattr(lib, "helicsInputGetType")
	result = fn(ipt.handle)
	return ffi.string(result).decode()


def helicsInputGetPublicationType(ipt: HelicsInput) -> str:
	"""
		Get the type the publisher to an input is sending.

		@param ipt The input to query.

		@return A const char with the type name.
	"""
	fn = getattr(lib, "helicsInputGetPublicationType")
	result = fn(ipt.handle)
	return ffi.string(result).decode()


def helicsInputGetPublicationDataType(ipt: HelicsInput) -> int:
	"""
		Get the type the publisher to an input is sending.

		@param ipt The input to query.

		@return An int containing the enumeration value of the publication type.
	"""
	fn = getattr(lib, "helicsInputGetPublicationDataType")
	result = fn(ipt.handle)
	return result


def helicsPublicationGetType(pub: HelicsPublication) -> str:
	"""
		Get the type of a publication.

		@param pub The publication to query.

		@return A void enumeration, HELICS_OK if everything worked.
	"""
	fn = getattr(lib, "helicsPublicationGetType")
	result = fn(pub.handle)
	return ffi.string(result).decode()


def helicsInputGetName(ipt: HelicsInput) -> str:
	"""
		Get the key of an input.

		@param ipt The input to query.

		@return A const char with the input name.
	"""
	fn = getattr(lib, "helicsInputGetName")
	result = fn(ipt.handle)
	return ffi.string(result).decode()


def helicsSubscriptionGetTarget(ipt: HelicsInput) -> str:
	"""
		Get the target of a subscription.

		@return A const char with the subscription target.
	"""
	fn = getattr(lib, "helicsSubscriptionGetTarget")
	result = fn(ipt.handle)
	return ffi.string(result).decode()


def helicsPublicationGetName(pub: HelicsPublication) -> str:
	"""
		Get the name of a publication.

		@details This will be the global key used to identify the publication to the federation.

		@param pub The publication to query.

		@return A const char with the publication name.
	"""
	fn = getattr(lib, "helicsPublicationGetName")
	result = fn(pub.handle)
	return ffi.string(result).decode()


def helicsInputGetUnits(ipt: HelicsInput) -> str:
	"""
		Get the units of an input.

		@param ipt The input to query.

		@return A void enumeration, HELICS_OK if everything worked.
	"""
	fn = getattr(lib, "helicsInputGetUnits")
	result = fn(ipt.handle)
	return ffi.string(result).decode()


def helicsInputGetInjectionUnits(ipt: HelicsInput) -> str:
	"""
		Get the units of the publication that an input is linked to.

		@param ipt The input to query.

		@return A void enumeration, HELICS_OK if everything worked.
	"""
	fn = getattr(lib, "helicsInputGetInjectionUnits")
	result = fn(ipt.handle)
	return ffi.string(result).decode()


def helicsInputGetExtractionUnits(ipt: HelicsInput) -> str:
	"""
		Get the units of an input.

		@details The same as helicsInputGetUnits.

		@param ipt The input to query.

		@return A void enumeration, HELICS_OK if everything worked.
	"""
	fn = getattr(lib, "helicsInputGetExtractionUnits")
	result = fn(ipt.handle)
	return ffi.string(result).decode()


def helicsPublicationGetUnits(pub: HelicsPublication) -> str:
	"""
		Get the units of a publication.

		@param pub The publication to query.

		@return A void enumeration, HELICS_OK if everything worked.
	"""
	fn = getattr(lib, "helicsPublicationGetUnits")
	result = fn(pub.handle)
	return ffi.string(result).decode()


def helicsInputGetInfo(inp: HelicsInput) -> str:
	"""
		Get the data in the info field of an input.

		@param inp The input to query.

		@return A string with the info field string.
	"""
	fn = getattr(lib, "helicsInputGetInfo")
	result = fn(inp.handle)
	return ffi.string(result).decode()


def helicsInputSetInfo(inp: HelicsInput, info: str):
	"""
		Set the data in the info field for an input.

		@param inp The input to query.
		@param info The string to set.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsInputSetInfo")
	err = helicsErrorInitialize()
	fn(inp.handle, ffi.new("char[]",info.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetTag(inp: HelicsInput, tagname: str) -> str:
	"""
		Get the data in a specified tag of an input.

		@param inp The input object to query.
		@param tagname The name of the tag to get the value for.
		@return A string with the tag data.
	"""
	fn = getattr(lib, "helicsInputGetTag")
	result = fn(inp.handle, ffi.new("char[]",tagname.encode()))
	return ffi.string(result).decode()


def helicsInputSetTag(inp: HelicsInput, tagname: str, tagvalue: str):
	"""
		Set the data in a specific tag for an input.

		@param inp The input object to query.
		@param tagname The string to set.
		@param tagvalue The string value to associate with a tag.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsInputSetTag")
	err = helicsErrorInitialize()
	fn(inp.handle, ffi.new("char[]",tagname.encode()), ffi.new("char[]",tagvalue.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetInfo(pub: HelicsPublication) -> str:
	"""
		Get the data in the info field of an publication.

		@param pub The publication to query.

		@return A string with the info field string.
	"""
	fn = getattr(lib, "helicsPublicationGetInfo")
	result = fn(pub.handle)
	return ffi.string(result).decode()


def helicsPublicationSetInfo(pub: HelicsPublication, info: str):
	"""
		Set the data in the info field for a publication.

		@param pub The publication to set the info field for.
		@param info The string to set.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsPublicationSetInfo")
	err = helicsErrorInitialize()
	fn(pub.handle, ffi.new("char[]",info.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetTag(pub: HelicsPublication, tagname: str) -> str:
	"""
		Get the data in a specified tag of a publication.

		@param pub The publication object to query.
		@param tagname The name of the tag to query.
		@return A string with the tag data.
	"""
	fn = getattr(lib, "helicsPublicationGetTag")
	result = fn(pub.handle, ffi.new("char[]",tagname.encode()))
	return ffi.string(result).decode()


def helicsPublicationSetTag(pub: HelicsPublication, tagname: str, tagvalue: str):
	"""
		Set the data in a specific tag for a publication.

		@param pub The publication object to set a tag for.
		@param tagname The name of the tag to set.
		@param tagvalue The string value to associate with a tag.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsPublicationSetTag")
	err = helicsErrorInitialize()
	fn(pub.handle, ffi.new("char[]",tagname.encode()), ffi.new("char[]",tagvalue.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputGetOption(inp: HelicsInput, option: int) -> int:
	"""
		Get the current value of an input handle option

		@param inp The input to query.
		@param option Integer representation of the option in question see /ref helics_handle_options.

		@return An integer value with the current value of the given option.
	"""
	fn = getattr(lib, "helicsInputGetOption")
	result = fn(inp.handle, option)
	return result


def helicsInputSetOption(inp: HelicsInput, option: int, value: int):
	"""
		Set an option on an input

		@param inp The input to query.
		@param option The option to set for the input /ref helics_handle_options.
		@param value The value to set the option to.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsInputSetOption")
	err = helicsErrorInitialize()
	fn(inp.handle, option, value, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationGetOption(pub: HelicsPublication, option: int) -> int:
	"""
		Get the value of an option for a publication

		@param pub The publication to query.
		@param option The value to query see /ref helics_handle_options.

		@return A string with the info field string.
	"""
	fn = getattr(lib, "helicsPublicationGetOption")
	result = fn(pub.handle, option)
	return result


def helicsPublicationSetOption(pub: HelicsPublication, option: int, val: int):
	"""
		Set the value of an option for a publication

		@param pub The publication to query.
		@param option Integer code for the option to set /ref helics_handle_options.
		@param val The value to set the option to.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsPublicationSetOption")
	err = helicsErrorInitialize()
	fn(pub.handle, option, val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsPublicationSetMinimumChange(pub: HelicsPublication, tolerance: float):
	"""
		Set the minimum change detection tolerance.

		@param pub The publication to modify.
		@param tolerance The tolerance level for publication, values changing less than this value will not be published.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsPublicationSetMinimumChange")
	err = helicsErrorInitialize()
	fn(pub.handle, tolerance, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputSetMinimumChange(inp: HelicsInput, tolerance: float):
	"""
		Set the minimum change detection tolerance.

		@param inp The input to modify.
		@param tolerance The tolerance level for registering an update, values changing less than this value will not show as being updated.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsInputSetMinimumChange")
	err = helicsErrorInitialize()
	fn(inp.handle, tolerance, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsInputIsUpdated(ipt: HelicsInput) -> bool:
	"""
		Check if a particular subscription was updated.

		@return HELICS_TRUE if it has been updated since the last value retrieval.
	"""
	fn = getattr(lib, "helicsInputIsUpdated")
	result = fn(ipt.handle)
	return result==1


def helicsInputLastUpdateTime(ipt: HelicsInput) -> HelicsTime:
	"""
		Get the last time a subscription was updated.
	"""
	fn = getattr(lib, "helicsInputLastUpdateTime")
	result = fn(ipt.handle)
	return result


def helicsInputClearUpdate(ipt: HelicsInput):
	"""
		Clear the updated flag from an input.
	"""
	fn = getattr(lib, "helicsInputClearUpdate")
	fn(ipt.handle)


def helicsFederateGetPublicationCount(fed: HelicsFederate) -> int:
	"""
		Get the number of publications in a federate.

		@return (-1) if fed was not a valid federate otherwise returns the number of publications.
	"""
	fn = getattr(lib, "helicsFederateGetPublicationCount")
	result = fn(fed.handle)
	return result


def helicsFederateGetInputCount(fed: HelicsFederate) -> int:
	"""
		Get the number of subscriptions in a federate.

		@return (-1) if fed was not a valid federate otherwise returns the number of subscriptions.
	"""
	fn = getattr(lib, "helicsFederateGetInputCount")
	result = fn(fed.handle)
	return result


def helicsFederateRegisterEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
	"""
		Create an endpoint.

		@details The endpoint becomes part of the federate and is destroyed when the federate is freed
		         so there are no separate free functions for endpoints.

		@param fed The federate object in which to create an endpoint must have been created
		          with helicsCreateMessageFederate or helicsCreateCombinationFederate.
		@param name The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
		@param type A string describing the expected type of the publication (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the endpoint, or nullptr on failure.
	"""
	fn = getattr(lib, "helicsFederateRegisterEndpoint")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), ffi.new("char[]",type.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsEndpoint(result)


def helicsFederateRegisterGlobalEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
	"""
		Create an endpoint.

		@details The endpoint becomes part of the federate and is destroyed when the federate is freed
		         so there are no separate free functions for endpoints.

		@param fed The federate object in which to create an endpoint must have been created
              with helicsCreateMessageFederate or helicsCreateCombinationFederate.
		@param name The identifier for the endpoint, the given name is the global identifier.
		@param type A string describing the expected type of the publication (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.

		@return An object containing the endpoint, or nullptr on failure.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalEndpoint")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), ffi.new("char[]",type.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsEndpoint(result)


def helicsFederateRegisterTargetedEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
	"""
		Create a targeted endpoint.  Targeted endpoints have specific destinations predefined and do not allow sending messages to other
		endpoints

		@details The endpoint becomes part of the federate and is destroyed when the federate is freed
		         so there are no separate free functions for endpoints.

		@param fed The federate object in which to create an endpoint must have been created
		          with helicsCreateMessageFederate or helicsCreateCombinationFederate.
		@param name The identifier for the endpoint. This will be prepended with the federate name for the global identifier.
		@param type A string describing the expected type of the publication (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return An object containing the endpoint, or nullptr on failure.
	"""
	fn = getattr(lib, "helicsFederateRegisterTargetedEndpoint")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), ffi.new("char[]",type.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsEndpoint(result)


def helicsFederateRegisterGlobalTargetedEndpoint(fed: HelicsFederate, name: str, type: str) -> HelicsEndpoint:
	"""
		Create a global targeted endpoint, Targeted endpoints have specific destinations predefined and do not allow sending messages to other
 endpoints

		@details The endpoint becomes part of the federate and is destroyed when the federate is freed
		         so there are no separate free functions for endpoints.

		@param fed The federate object in which to create an endpoint must have been created
              with helicsCreateMessageFederate or helicsCreateCombinationFederate.
		@param name The identifier for the endpoint, the given name is the global identifier.
		@param type A string describing the expected type of the publication (may be NULL).

		@param[in,out] err A pointer to an error object for catching errors.

		@return An object containing the endpoint, or nullptr on failure.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalTargetedEndpoint")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), ffi.new("char[]",type.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsEndpoint(result)


def helicsFederateGetEndpoint(fed: HelicsFederate, name: str) -> HelicsEndpoint:
	"""
		Get an endpoint object from a name.

		@param fed The message federate object to use to get the endpoint.
		@param name The name of the endpoint.

		@param[in,out] err The error object to complete if there is an error.


		@return A HelicsEndpoint object.

		The object will not be valid and err will contain an error code if no endpoint with the specified name exists.
	"""
	fn = getattr(lib, "helicsFederateGetEndpoint")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsEndpoint(result)


def helicsFederateGetEndpointByIndex(fed: HelicsFederate, index: int) -> HelicsEndpoint:
	"""
		Get an endpoint by its index, typically already created via registerInterfaces file or something of that nature.

		@param fed The federate object in which to create a publication.
		@param index The index of the publication to get.

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsEndpoint.

		The HelicsEndpoint returned will be NULL if given an invalid index.
	"""
	fn = getattr(lib, "helicsFederateGetEndpointByIndex")
	err = helicsErrorInitialize()
	result = fn(fed.handle, index, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsEndpoint(result)


def helicsEndpointIsValid(endpoint: HelicsEndpoint) -> bool:
	"""
		Check if an endpoint is valid.

		@param endpoint The endpoint object to check.

		@return HELICS_TRUE if the Endpoint object represents a valid endpoint.
	"""
	fn = getattr(lib, "helicsEndpointIsValid")
	result = fn(endpoint.handle)
	return result==1


def helicsEndpointSetDefaultDestination(endpoint: HelicsEndpoint, dst: str):
	"""
		Set the default destination for an endpoint if no other endpoint is given.

		@param endpoint The endpoint to set the destination for.
		@param dst A string naming the desired default endpoint.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsEndpointSetDefaultDestination")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",dst.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetDefaultDestination(endpoint: HelicsEndpoint) -> str:
	"""
		Get the default destination for an endpoint.

		@param endpoint The endpoint to set the destination for.

		@return A string with the default destination.
	"""
	fn = getattr(lib, "helicsEndpointGetDefaultDestination")
	result = fn(endpoint.handle)
	return ffi.string(result).decode()


def helicsEndpointSendBytes(endpoint: HelicsEndpoint, data: bytes):
	"""
		Send a message to the targeted destinations.

		@param endpoint The endpoint to send the data from.
		@param data The data to send.
	"""
	fn = getattr(lib, "helicsEndpointSendBytes")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(endpoint.handle, data, inputDataLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendBytesTo(endpoint: HelicsEndpoint, data: bytes, dst: str):
	"""
		Send a message to the specified destination.

		@param endpoint The endpoint to send the data from.
		@param data The data to send.
		@param dst The destination to send the message to.
	"""
	fn = getattr(lib, "helicsEndpointSendBytesTo")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(endpoint.handle, data, inputDataLength, ffi.new("char[]",dst.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendBytesToAt(endpoint: HelicsEndpoint, data: bytes, dst: str, time: HelicsTime):
	"""
		Send a message to the specified destination at a specified time.

		@param endpoint The endpoint to send the data from.
		@param data The data to send.
		@param dst The destination to send the message to.
		@param time The time to send the message at.
	"""
	fn = getattr(lib, "helicsEndpointSendBytesToAt")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(endpoint.handle, data, inputDataLength, ffi.new("char[]",dst.encode()), time, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendBytesAt(endpoint: HelicsEndpoint, data: bytes, time: HelicsTime):
	"""
		Send a message to the targeted destinations at a specified time.

		@param endpoint The endpoint to send the data from.
		@param data The data to send.
		@param time The time to send the message at.
	"""
	fn = getattr(lib, "helicsEndpointSendBytesAt")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(endpoint.handle, data, inputDataLength, time, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessage(endpoint: HelicsEndpoint, message: HelicsMessage):
	"""
		Send a message object from a specific endpoint.

		@param endpoint The endpoint to send the data from.
		@param message The actual message to send which will be copied.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsEndpointSendMessage")
	err = helicsErrorInitialize()
	fn(endpoint.handle, message.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSendMessageZeroCopy(endpoint: HelicsEndpoint, message: HelicsMessage):
	"""
		Send a message object from a specific endpoint, the message will not be copied and the message object will no longer be valid
		after the call.

		@param endpoint The endpoint to send the data from.
		@param message The actual message to send which will be copied.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsEndpointSendMessageZeroCopy")
	err = helicsErrorInitialize()
	fn(endpoint.handle, message.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSubscribe(endpoint: HelicsEndpoint, key: str):
	"""
		Subscribe an endpoint to a publication.

		@param endpoint The endpoint to use.
		@param key The name of the publication.

		@param[in,out] err A pointer to an error object for catching errors.
	"""
	fn = getattr(lib, "helicsEndpointSubscribe")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",key.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateHasMessage(fed: HelicsFederate) -> bool:
	"""
		Check if the federate has any outstanding messages.

		@param fed The federate to check.

		@return HELICS_TRUE if the federate has a message waiting, HELICS_FALSE otherwise.
	"""
	fn = getattr(lib, "helicsFederateHasMessage")
	result = fn(fed.handle)
	return result==1


def helicsEndpointHasMessage(endpoint: HelicsEndpoint) -> bool:
	"""
		Check if a given endpoint has any unread messages.

		@param endpoint The endpoint to check.

		@return HELICS_TRUE if the endpoint has a message, HELICS_FALSE otherwise.
	"""
	fn = getattr(lib, "helicsEndpointHasMessage")
	result = fn(endpoint.handle)
	return result==1


def helicsFederatePendingMessageCount(fed: HelicsFederate) -> int:
	"""
		Returns the number of pending receives for the specified destination endpoint.

		@param fed The federate to get the number of waiting messages from.
	"""
	fn = getattr(lib, "helicsFederatePendingMessageCount")
	result = fn(fed.handle)
	return result


def helicsEndpointPendingMessageCount(endpoint: HelicsEndpoint) -> int:
	"""
		Returns the number of pending receives for all endpoints of a particular federate.

		@param endpoint The endpoint to query.
	"""
	fn = getattr(lib, "helicsEndpointPendingMessageCount")
	result = fn(endpoint.handle)
	return result


def helicsEndpointGetMessage(endpoint: HelicsEndpoint) -> HelicsMessage:
	"""
		Receive a packet from a particular endpoint.

		@param[in] endpoint The identifier for the endpoint.

		@return A message object.
	"""
	fn = getattr(lib, "helicsEndpointGetMessage")
	result = fn(endpoint.handle)
	return HelicsMessage(result)


def helicsEndpointCreateMessage(endpoint: HelicsEndpoint) -> HelicsMessage:
	"""
		Create a new empty message object.

		@details The message is empty and isValid will return false since there is no data associated with the message yet.

		@param endpoint The endpoint object to associate the message with.

		@param[in,out] err An error object to fill out in case of an error.


		@return A new HelicsMessage.
	"""
	fn = getattr(lib, "helicsEndpointCreateMessage")
	err = helicsErrorInitialize()
	result = fn(endpoint.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsMessage(result)


def helicsFederateGetMessage(fed: HelicsFederate) -> HelicsMessage:
	"""
		Receive a communication message for any endpoint in the federate.

		@details The return order will be in order of endpoint creation.
		         So all messages that are available for the first endpoint, then all for the second, and so on.
		         Within a single endpoint, the messages are ordered by time, then source_id, then order of arrival.

		@return A HelicsMessage which references the data in the message.
	"""
	fn = getattr(lib, "helicsFederateGetMessage")
	result = fn(fed.handle)
	return HelicsMessage(result)


def helicsFederateCreateMessage(fed: HelicsFederate) -> HelicsMessage:
	"""
		Create a new empty message object.

		@details The message is empty and isValid will return false since there is no data associated with the message yet.

		@param fed the federate object to associate the message with

		@param[in,out] err An error object to fill out in case of an error.


		@return A HelicsMessage containing the message data.
	"""
	fn = getattr(lib, "helicsFederateCreateMessage")
	err = helicsErrorInitialize()
	result = fn(fed.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsMessage(result)


def helicsFederateClearMessages(fed: HelicsFederate):
	"""
		Clear all stored messages from a federate.

		@details This clears messages retrieved through helicsEndpointGetMessage or helicsFederateGetMessage

		@param fed The federate to clear the message for.
	"""
	fn = getattr(lib, "helicsFederateClearMessages")
	fn(fed.handle)


def helicsEndpointGetType(endpoint: HelicsEndpoint) -> str:
	"""
		Get the type specified for an endpoint.

		@param endpoint The endpoint object in question.

		@return The defined type of the endpoint.
	"""
	fn = getattr(lib, "helicsEndpointGetType")
	result = fn(endpoint.handle)
	return ffi.string(result).decode()


def helicsEndpointGetName(endpoint: HelicsEndpoint) -> str:
	"""
		Get the name of an endpoint.

		@param endpoint The endpoint object in question.

		@return The name of the endpoint.
	"""
	fn = getattr(lib, "helicsEndpointGetName")
	result = fn(endpoint.handle)
	return ffi.string(result).decode()


def helicsFederateGetEndpointCount(fed: HelicsFederate) -> int:
	"""
		Get the number of endpoints in a federate.

		@param fed The message federate to query.

		@return (-1) if fed was not a valid federate, otherwise returns the number of endpoints.
	"""
	fn = getattr(lib, "helicsFederateGetEndpointCount")
	result = fn(fed.handle)
	return result


def helicsEndpointGetInfo(end: HelicsEndpoint) -> str:
	"""
		Get the local information field of an endpoint.

		@param end The endpoint to query.

		@return A string with the info field string.
	"""
	fn = getattr(lib, "helicsEndpointGetInfo")
	result = fn(end.handle)
	return ffi.string(result).decode()


def helicsEndpointSetInfo(endpoint: HelicsEndpoint, info: str):
	"""
		Set the data in the interface information field for an endpoint.

		@param endpoint The endpoint to set the information for
		@param info The string to store in the field

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsEndpointSetInfo")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",info.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetTag(endpoint: HelicsEndpoint, tagname: str) -> str:
	"""
		Get the data in a specified tag of an endpoint

		@param endpoint The endpoint to query.
		@param tagname The name of the tag to query.
		@return A string with the tag data.
	"""
	fn = getattr(lib, "helicsEndpointGetTag")
	result = fn(endpoint.handle, ffi.new("char[]",tagname.encode()))
	return ffi.string(result).decode()


def helicsEndpointSetTag(endpoint: HelicsEndpoint, tagname: str, tagvalue: str):
	"""
		Set the data in a specific tag for an endpoint.

		@param endpoint The endpoint to query.
		@param tagname The string to set.
		@param tagvalue The string value to associate with a tag.

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsEndpointSetTag")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",tagname.encode()), ffi.new("char[]",tagvalue.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointSetOption(endpoint: HelicsEndpoint, option: int, value: int):
	"""
		Set a handle option on an endpoint.

		@param endpoint The endpoint to modify.
		@param option Integer code for the option to set /ref helics_handle_options.
		@param value The value to set the option to.

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsEndpointSetOption")
	err = helicsErrorInitialize()
	fn(endpoint.handle, option, value, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointGetOption(endpoint: HelicsEndpoint, option: int) -> int:
	"""
		Set a handle option on an endpoint.

		@param endpoint The endpoint to modify.
		@param option Integer code for the option to set /ref helics_handle_options.
		@return the value of the option, for boolean options will be 0 or 1
	"""
	fn = getattr(lib, "helicsEndpointGetOption")
	result = fn(endpoint.handle, option)
	return result


def helicsEndpointAddSourceTarget(endpoint: HelicsEndpoint, targetEndpoint: str):
	"""
		add a source target to an endpoint,  Specifying an endpoint to receive undirected messages from

		@param endpoint The endpoint to modify.
		@param targetEndpoint the endpoint to get messages from

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsEndpointAddSourceTarget")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",targetEndpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointAddDestinationTarget(endpoint: HelicsEndpoint, targetEndpoint: str):
	"""
		add a destination target to an endpoint,  Specifying an endpoint to send undirected messages to

		@param endpoint The endpoint to modify.
		@param targetEndpoint the name of the endpoint to send messages to

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsEndpointAddDestinationTarget")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",targetEndpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointRemoveTarget(endpoint: HelicsEndpoint, targetEndpoint: str):
	"""
		remove an endpoint from being targeted

		@param endpoint The endpoint to modify.
		@param targetEndpoint the name of the endpoint to send messages to

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsEndpointRemoveTarget")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",targetEndpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointAddSourceFilter(endpoint: HelicsEndpoint, filterName: str):
	"""
		add a source Filter to an endpoint

		@param endpoint The endpoint to modify.
		@param filterName the name of the filter to add

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsEndpointAddSourceFilter")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",filterName.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsEndpointAddDestinationFilter(endpoint: HelicsEndpoint, filterName: str):
	"""
		add a destination filter to an endpoint

		@param endpoint The endpoint to modify.
		@param filterName The name of the filter to add.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsEndpointAddDestinationFilter")
	err = helicsErrorInitialize()
	fn(endpoint.handle, ffi.new("char[]",filterName.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageGetSource(message: HelicsMessage) -> str:
	"""
		Get the source endpoint of a message.

		@param message The message object in question.

		@return A string with the source endpoint.
	"""
	fn = getattr(lib, "helicsMessageGetSource")
	result = fn(message.handle)
	return ffi.string(result).decode()


def helicsMessageGetDestination(message: HelicsMessage) -> str:
	"""
		Get the destination endpoint of a message.

		@param message The message object in question.

		@return A string with the destination endpoint.
	"""
	fn = getattr(lib, "helicsMessageGetDestination")
	result = fn(message.handle)
	return ffi.string(result).decode()


def helicsMessageGetOriginalSource(message: HelicsMessage) -> str:
	"""
		Get the original source endpoint of a message, the source may have been modified by filters or other actions.

		@param message The message object in question.

		@return A string with the source of a message.
	"""
	fn = getattr(lib, "helicsMessageGetOriginalSource")
	result = fn(message.handle)
	return ffi.string(result).decode()


def helicsMessageGetOriginalDestination(message: HelicsMessage) -> str:
	"""
		Get the original destination endpoint of a message, the destination may have been modified by filters or other actions.

		@param message The message object in question.

		@return A string with the original destination of a message.
	"""
	fn = getattr(lib, "helicsMessageGetOriginalDestination")
	result = fn(message.handle)
	return ffi.string(result).decode()


def helicsMessageGetTime(message: HelicsMessage) -> HelicsTime:
	"""
		Get the helics time associated with a message.

		@param message The message object in question.

		@return The time associated with a message.
	"""
	fn = getattr(lib, "helicsMessageGetTime")
	result = fn(message.handle)
	return result


def helicsMessageGetString(message: HelicsMessage) -> str:
	"""
		Get the payload of a message as a string.

		@param message The message object in question.

		@return A string representing the payload of a message.
	"""
	fn = getattr(lib, "helicsMessageGetString")
	result = fn(message.handle)
	return ffi.string(result).decode()


def helicsMessageGetMessageID(message: HelicsMessage) -> int:
	"""
		Get the messageID of a message.

		@param message The message object in question.

		@return The messageID.
	"""
	fn = getattr(lib, "helicsMessageGetMessageID")
	result = fn(message.handle)
	return result


def helicsMessageGetFlagOption(message: HelicsMessage, flag: int) -> bool:
	"""
		Check if a flag is set on a message.

		@param message The message object in question.
		@param flag The flag to check should be between [0,15].

		@return The flags associated with a message.
	"""
	fn = getattr(lib, "helicsMessageGetFlagOption")
	result = fn(message.handle, flag)
	return result==1


def helicsMessageGetByteCount(message: HelicsMessage) -> int:
	"""
		Get the size of the data payload in bytes.

		@param message The message object in question.

		@return The size of the data payload.
	"""
	fn = getattr(lib, "helicsMessageGetByteCount")
	result = fn(message.handle)
	return result


def helicsMessageGetBytes(message: HelicsMessage) -> bytes:
	"""
		Get the raw data for a message object.

		@param message A message object to get the data for.

		@return Raw string data.
	"""
	fn = getattr(lib, "helicsMessageGetBytes")
	maxMessageLength = helicsMessageGetByteCount(message) + 1024
	data = ffi.new(f"char[{maxMessageLength}]")
	actualSize = ffi.new("int[1]")
	err = helicsErrorInitialize()
	fn(message.handle, data, maxMessageLength, actualSize, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return ffi.unpack(data, length=actualSize[0])


def helicsMessageGetBytesPointer(message: HelicsMessage):
	"""
		Get a pointer to the raw data of a message.

		@param message A message object to get the data for.

		@return A pointer to the raw data in memory, the pointer may be NULL if the message is not a valid message.
	"""
	fn = getattr(lib, "helicsMessageGetBytesPointer")
	result = fn(message.handle)
	return result


def helicsMessageIsValid(message: HelicsMessage) -> bool:
	"""
		A check if the message contains a valid payload.

		@param message The message object in question.

		@return HELICS_TRUE if the message contains a payload.
	"""
	fn = getattr(lib, "helicsMessageIsValid")
	result = fn(message.handle)
	return result==1


def helicsMessageSetSource(message: HelicsMessage, src: str):
	"""
		Set the source of a message.

		@param message The message object in question.
		@param src A string containing the source.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetSource")
	err = helicsErrorInitialize()
	fn(message.handle, ffi.new("char[]",src.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetDestination(message: HelicsMessage, dst: str):
	"""
		Set the destination of a message.

		@param message The message object in question.
		@param dst A string containing the new destination.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetDestination")
	err = helicsErrorInitialize()
	fn(message.handle, ffi.new("char[]",dst.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalSource(message: HelicsMessage, src: str):
	"""
		Set the original source of a message.

		@param message The message object in question.
		@param src A string containing the new original source.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetOriginalSource")
	err = helicsErrorInitialize()
	fn(message.handle, ffi.new("char[]",src.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetOriginalDestination(message: HelicsMessage, dst: str):
	"""
		Set the original destination of a message.

		@param message The message object in question.
		@param dst A string containing the new original source.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetOriginalDestination")
	err = helicsErrorInitialize()
	fn(message.handle, ffi.new("char[]",dst.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetTime(message: HelicsMessage, time: HelicsTime):
	"""
		Set the delivery time for a message.

		@param message The message object in question.
		@param time The time the message should be delivered.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetTime")
	err = helicsErrorInitialize()
	fn(message.handle, time, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageResize(message: HelicsMessage, newSize: int):
	"""
		Resize the data buffer for a message.

		@details The message data buffer will be resized. There are no guarantees on what is in the buffer in newly allocated space.
		         If the allocated space is not sufficient new allocations will occur.

		@param message The message object in question.
		@param newSize The new size in bytes of the buffer.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageResize")
	err = helicsErrorInitialize()
	fn(message.handle, newSize, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageReserve(message: HelicsMessage, reserveSize: int):
	"""
		Reserve space in a buffer but don't actually resize.

		@details The message data buffer will be reserved but not resized.

		@param message The message object in question.
		@param reserveSize The number of bytes to reserve in the message object.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageReserve")
	err = helicsErrorInitialize()
	fn(message.handle, reserveSize, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetMessageID(message: HelicsMessage, messageID: int):
	"""
		Set the message ID for the message.

		@details Normally this is not needed and the core of HELICS will adjust as needed.

		@param message The message object in question.
		@param messageID A new message ID.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetMessageID")
	err = helicsErrorInitialize()
	fn(message.handle, messageID, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClearFlags(message: HelicsMessage):
	"""
		Clear the flags of a message.

		@param message The message object in question
	"""
	fn = getattr(lib, "helicsMessageClearFlags")
	fn(message.handle)


def helicsMessageSetFlagOption(message: HelicsMessage, flag: int, flagValue: bool):
	"""
		Set a flag on a message.

		@param message The message object in question.
		@param flag An index of a flag to set on the message.
		@param flagValue The desired value of the flag.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetFlagOption")
	err = helicsErrorInitialize()
	fn(message.handle, flag, flagValue, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetString(message: HelicsMessage, string: str):
	"""
		Set the data payload of a message as a string.

		@param message The message object in question.
		@param str A string containing the message data.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageSetString")
	err = helicsErrorInitialize()
	fn(message.handle, ffi.new("char[]",string.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageSetData(message: HelicsMessage, data: bytes):
	"""
		Set the data payload of a message as raw data.

		@param message The message object in question.
		@param data A string containing the message data.
	"""
	fn = getattr(lib, "helicsMessageSetData")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(message.handle, data, inputDataLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageAppendData(message: HelicsMessage, data: bytes):
	"""
		Append data to the payload.

		@param message The message object in question.
		@param data A string containing the message data to append.
	"""
	fn = getattr(lib, "helicsMessageAppendData")
	if isinstance(data, str):
		data = data.encode()
	if not isinstance(data, bytes):
		raise Exception("""data must be of type `bytes`. Got {t} instead. Try converting it to bytes (e.g. `"hello world".encode()`""".format(t=type(data)))
	inputDataLength = len(data)
	err = helicsErrorInitialize()
	fn(message.handle, data, inputDataLength, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageCopy(src_message: HelicsMessage, dst_message: HelicsMessage):
	"""
		Copy a message object.

		@param src_message The message object to copy from.
		@param dst_message The message object to copy to.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageCopy")
	err = helicsErrorInitialize()
	fn(src_message.handle, dst_message.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsMessageClone(message: HelicsMessage) -> HelicsMessage:
	"""
		Clone a message object.

		@param message The message object to copy from.

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageClone")
	err = helicsErrorInitialize()
	result = fn(message.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsMessage(result)


def helicsMessageFree(message: HelicsMessage):
	"""
		Free a message object from memory
		@param message The message object to copy from.
		@details memory for message is managed so not using this function does not create memory leaks, this is an indication
		to the system that the memory for this message is done being used and can be reused for a new message.
		helicsFederateClearMessages() can also be used to clear up all stored messages at once
	"""
	fn = getattr(lib, "helicsMessageFree")
	fn(message.handle)


def helicsMessageClear(message: HelicsMessage):
	"""
		Reset a message to empty state
		@param message The message object to copy from.
		@details The message after this function will be empty, with no source or destination

		@param[in,out] err An error object to fill out in case of an error.
	"""
	fn = getattr(lib, "helicsMessageClear")
	err = helicsErrorInitialize()
	fn(message.handle, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateRegisterFilter(fed: HelicsFederate, type: HelicsFilterTypes, name: str) -> HelicsFilter:
	"""
		Create a source Filter on the specified federate.

		@details Filters can be created through a federate or a core, linking through a federate allows
		         a few extra features of name matching to function on the federate interface but otherwise equivalent behavior

		@param fed The federate to register through.
		@param type The type of filter to create /ref HelicsFilterTypes.
		@param name The name of the filter (can be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsFilter object.
	"""
	fn = getattr(lib, "helicsFederateRegisterFilter")
	err = helicsErrorInitialize()
	result = fn(fed.handle, HelicsFilterTypes(type), ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsFederateRegisterGlobalFilter(fed: HelicsFederate, type: HelicsFilterTypes, name: str) -> HelicsFilter:
	"""
		Create a global source filter through a federate.

		@details Filters can be created through a federate or a core, linking through a federate allows
		         a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

		@param fed The federate to register through.
		@param type The type of filter to create /ref HelicsFilterTypes.
		@param name The name of the filter (can be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsFilter object.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalFilter")
	err = helicsErrorInitialize()
	result = fn(fed.handle, HelicsFilterTypes(type), ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsFederateRegisterCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
	"""
		Create a cloning Filter on the specified federate.

		@details Cloning filters copy a message and send it to multiple locations, source and destination can be added
		         through other functions.

		@param fed The federate to register through.
		@param name The name of the filter (can be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsFilter object.
	"""
	fn = getattr(lib, "helicsFederateRegisterCloningFilter")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsFederateRegisterGlobalCloningFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
	"""
		Create a global cloning Filter on the specified federate.

		@details Cloning filters copy a message and send it to multiple locations, source and destination can be added
		         through other functions.

		@param fed The federate to register through.
		@param name The name of the filter (can be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsFilter object.
	"""
	fn = getattr(lib, "helicsFederateRegisterGlobalCloningFilter")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsCoreRegisterFilter(core: HelicsCore, type: HelicsFilterTypes, name: str) -> HelicsFilter:
	"""
		Create a source Filter on the specified core.

		@details Filters can be created through a federate or a core, linking through a federate allows
		         a few extra features of name matching to function on the federate interface but otherwise equivalent behavior.

		@param core The core to register through.
		@param type The type of filter to create /ref HelicsFilterTypes.
		@param name The name of the filter (can be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsFilter object.
	"""
	fn = getattr(lib, "helicsCoreRegisterFilter")
	err = helicsErrorInitialize()
	result = fn(core.handle, HelicsFilterTypes(type), ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsCoreRegisterCloningFilter(core: HelicsCore, name: str) -> HelicsFilter:
	"""
		Create a cloning Filter on the specified core.

		@details Cloning filters copy a message and send it to multiple locations, source and destination can be added
		         through other functions.

		@param core The core to register through.
		@param name The name of the filter (can be NULL).

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsFilter object.
	"""
	fn = getattr(lib, "helicsCoreRegisterCloningFilter")
	err = helicsErrorInitialize()
	result = fn(core.handle, ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsFederateGetFilterCount(fed: HelicsFederate) -> int:
	"""
		Get the number of filters registered through a federate.

		@param fed The federate object to use to get the filter.

		@return A count of the number of filters registered through a federate.
	"""
	fn = getattr(lib, "helicsFederateGetFilterCount")
	result = fn(fed.handle)
	return result


def helicsFederateGetFilter(fed: HelicsFederate, name: str) -> HelicsFilter:
	"""
		Get a filter by its name, typically already created via registerInterfaces file or something of that nature.

		@param fed The federate object to use to get the filter.
		@param name The name of the filter.

		@param[in,out] err The error object to complete if there is an error.


		@return A HelicsFilter object, the object will not be valid and err will contain an error code if no filter with the specified name
		exists.
	"""
	fn = getattr(lib, "helicsFederateGetFilter")
	err = helicsErrorInitialize()
	result = fn(fed.handle, ffi.new("char[]",name.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsFederateGetFilterByIndex(fed: HelicsFederate, index: int) -> HelicsFilter:
	"""
		Get a filter by its index, typically already created via registerInterfaces file or something of that nature.

		@param fed The federate object in which to create a publication.
		@param index The index of the publication to get.

		@param[in,out] err A pointer to an error object for catching errors.


		@return A HelicsFilter, which will be NULL if an invalid index is given.
	"""
	fn = getattr(lib, "helicsFederateGetFilterByIndex")
	err = helicsErrorInitialize()
	result = fn(fed.handle, index, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())
	return HelicsFilter(result)


def helicsFilterIsValid(filt: HelicsFilter) -> bool:
	"""
		Check if a filter is valid.

		@param filt The filter object to check.

		@return HELICS_TRUE if the Filter object represents a valid filter.
	"""
	fn = getattr(lib, "helicsFilterIsValid")
	result = fn(filt.handle)
	return result==1


def helicsFilterGetName(filt: HelicsFilter) -> str:
	"""
		Get the name of the filter and store in the given string.

		@param filt The given filter.

		@return A string with the name of the filter.
	"""
	fn = getattr(lib, "helicsFilterGetName")
	result = fn(filt.handle)
	return ffi.string(result).decode()


def helicsFilterSet(filt: HelicsFilter, prop: str, val: float):
	"""
		Set a property on a filter.

		@param filt The filter to modify.
		@param prop A string containing the property to set.
		@param val A numerical value for the property.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterSet")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",prop.encode()), val, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetString(filt: HelicsFilter, prop: str, val: str):
	"""
		Set a string property on a filter.

		@param filt The filter to modify.
		@param prop A string containing the property to set.
		@param val A string containing the new value.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterSetString")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",prop.encode()), ffi.new("char[]",val.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDestinationTarget(filt: HelicsFilter, dst: str):
	"""
		Add a destination target to a filter.

		@details All messages going to a destination are copied to the delivery address(es).
		@param filt The given filter to add a destination target to.
		@param dst The name of the endpoint to add as a destination target.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterAddDestinationTarget")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",dst.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddSourceTarget(filt: HelicsFilter, source: str):
	"""
		Add a source target to a filter.

		@details All messages coming from a source are copied to the delivery address(es).

		@param filt The given filter.
		@param source The name of the endpoint to add as a source target.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterAddSourceTarget")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",source.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterAddDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
	"""
		Add a delivery endpoint to a cloning filter.

		@details All cloned messages are sent to the delivery address(es).

		@param filt The given filter.
		@param deliveryEndpoint The name of the endpoint to deliver messages to.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterAddDeliveryEndpoint")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",deliveryEndpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveTarget(filt: HelicsFilter, target: str):
	"""
		Remove a destination target from a filter.

		@param filt The given filter.
		@param target The named endpoint to remove as a target.


		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterRemoveTarget")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",target.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterRemoveDeliveryEndpoint(filt: HelicsFilter, deliveryEndpoint: str):
	"""
		Remove a delivery destination from a cloning filter.

		@param filt The given filter (must be a cloning filter).
		@param deliveryEndpoint A string with the delivery endpoint to remove.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterRemoveDeliveryEndpoint")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",deliveryEndpoint.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetInfo(filt: HelicsFilter) -> str:
	"""
		Get the data in the info field of a filter.

		@param filt The given filter.

		@return A string with the info field string.
	"""
	fn = getattr(lib, "helicsFilterGetInfo")
	result = fn(filt.handle)
	return ffi.string(result).decode()


def helicsFilterSetInfo(filt: HelicsFilter, info: str):
	"""
		Set the data in the info field for a filter.

		@param filt The given filter.
		@param info The string to set.

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsFilterSetInfo")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",info.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetTag(filt: HelicsFilter, tagname: str) -> str:
	"""
		Get the data in a specified tag of a filter.

		@param filt The filter to query.
		@param tagname The name of the tag to query.
		@return A string with the tag data.
	"""
	fn = getattr(lib, "helicsFilterGetTag")
	result = fn(filt.handle, ffi.new("char[]",tagname.encode()))
	return ffi.string(result).decode()


def helicsFilterSetTag(filt: HelicsFilter, tagname: str, tagvalue: str):
	"""
		Set the data in a specific tag for a filter.

		@param filt The filter object to set the tag for.
		@param tagname The string to set.
		@param tagvalue the string value to associate with a tag.

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsFilterSetTag")
	err = helicsErrorInitialize()
	fn(filt.handle, ffi.new("char[]",tagname.encode()), ffi.new("char[]",tagvalue.encode()), err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetOption(filt: HelicsFilter, option: int, value: int):
	"""
		Set an option value for a filter.

		@param filt The given filter.
		@param option The option to set /ref helics_handle_options.
		@param value The value of the option commonly 0 for false 1 for true.

		@param[in,out] err An error object to fill out in case of an error.

	"""
	fn = getattr(lib, "helicsFilterSetOption")
	err = helicsErrorInitialize()
	fn(filt.handle, option, value, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterGetOption(filt: HelicsFilter, option: int) -> int:
	"""
		Get a handle option for the filter.

		@param filt The given filter to query.
		@param option The option to query /ref helics_handle_options.
	"""
	fn = getattr(lib, "helicsFilterGetOption")
	result = fn(filt.handle, option)
	return result


def helicsBrokerSetLoggingCallback(broker: HelicsBroker, logger, userdata):
	"""
		Set the logging callback to a broker.

		@details Add a logging callback function to a broker.
		         The logging callback will be called when
		         a message flows into a broker from the core or from a broker.

		@param broker The broker object in which to set the callback.
		@param logger A callback with signature void(int, const char, const char, void);
		              the function arguments are loglevel, an identifier, a message string, and a pointer to user data.
		@param userdata A pointer to user data that is passed to the function when executing.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsBrokerSetLoggingCallback")
	err = helicsErrorInitialize()
	fn(broker.handle, logger, userdata, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsCoreSetLoggingCallback(core: HelicsCore, logger, userdata):
	"""
		Set the logging callback for a core.

		@details Add a logging callback function to a core. The logging callback will be called when
		         a message flows into a core from the core or from a broker.

		@param core The core object in which to set the callback.
		@param logger A callback with signature void(int, const char, const char, void);
		              The function arguments are loglevel, an identifier, a message string, and a pointer to user data.
		@param userdata A pointer to user data that is passed to the function when executing.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsCoreSetLoggingCallback")
	err = helicsErrorInitialize()
	fn(core.handle, logger, userdata, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetLoggingCallback(fed: HelicsFederate, logger, userdata):
	"""
		Set the logging callback for a federate.

		@details Add a logging callback function to a federate. The logging callback will be called when
		         a message flows into a federate from the core or from a federate.

		@param fed The federate object in which to create a subscription must have been created with
		           helicsCreateValueFederate or helicsCreateCombinationFederate.
		@param logger A callback with signature void(int, const char, const char, void);
		       The function arguments are loglevel, an identifier string, a message string, and a pointer to user data.
		@param userdata A pointer to user data that is passed to the function when executing.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFederateSetLoggingCallback")
	err = helicsErrorInitialize()
	fn(fed.handle, logger, userdata, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFilterSetCustomCallback(filter: HelicsFilter, filtCall, userdata):
	"""
		Set a general callback for a custom filter.

		@details Add a custom filter callback for creating a custom filter operation in the C shared library.

		@param filter The filter object to set the callback for.
		@param filtCall A callback with signature helics_message_object(helics_message_object, void);
		                The function arguments are the message to filter and a pointer to user data.
		                The filter should return a new message.
		@param userdata A pointer to user data that is passed to the function when executing.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFilterSetCustomCallback")
	err = helicsErrorInitialize()
	fn(filter.handle, filtCall, userdata, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetQueryCallback(fed: HelicsFederate, queryAnswer, userdata):
	"""
		Set callback for queries executed against a federate.

		@details There are many queries that HELICS understands directly, but it is occasionally useful to have a federate be able to respond
		to specific queries with answers specific to a federate.

		@param fed The federate to set the callback for.
		@param queryAnswer A callback with signature const char(const charquery, int querySize,intanswerSize, voiduserdata);
		                The function arguments are the query string requesting an answer along with its size, the string is not guaranteed to be
		null terminated answerSize is an outputParameter intended to filled out by the userCallback and should contain the length of the return
		string. The return pointer can be NULL if no answer is given and HELICS will generate the appropriate response.
		@param userdata A pointer to user data that is passed to the function when executing.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFederateSetQueryCallback")
	err = helicsErrorInitialize()
	fn(fed.handle, queryAnswer, userdata, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsFederateSetTimeUpdateCallback(fed: HelicsFederate, timeUpdate, userdata):
	"""
		Set callback for the time update.

		@details This callback will be executed every time the simulation time is updated starting on entry to executing mode.

		@param fed The federate to set the callback for.
		@param timeUpdate A callback with signature void(HelicsTime newTime, bool iterating, voiduserdata);
		                The function arguments are the new time value, a bool indicating that the time is iterating, and pointer to the userdata.
		@param userdata A pointer to user data that is passed to the function when executing.

		@param[in,out] err A pointer to an error object for catching errors.

	"""
	fn = getattr(lib, "helicsFederateSetTimeUpdateCallback")
	err = helicsErrorInitialize()
	fn(fed.handle, timeUpdate, userdata, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


def helicsQueryBufferFill(buffer: HelicsQueryBuffer, string: str):
	"""
		Set the data for a query callback.

		@details There are many queries that HELICS understands directly, but it is occasionally useful to have a federate be able to respond to specific queries with answers specific to a federate.

		@param buffer The buffer received in a helicsQueryCallback.
		@param string The string with the data to fill the buffer with.
	"""
	fn = getattr(lib, "helicsQueryBufferFill")
	strLen = len(string)
	err = helicsErrorInitialize()
	fn(buffer.handle, ffi.new("char[]",string.encode()), strLen, err)
	if err.error_code != 0:
		raise HelicsException("[" + str(err.error_code) + "] " + ffi.string(err.message).decode())


