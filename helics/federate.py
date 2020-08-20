# -*- coding: utf-8 -*-
from . import capi as h
from .core import Core
import logging

from typing import List, Any, TypeVar

Federate = TypeVar("Any")
FederateInfo = TypeVar("Any")


class FederateInfo:
    def __init__(self, *, core_type: str = "", federate_info=None, clone=False):

        if federate_info is not None and type(federate_info) == FederateInfo and clone is True:
            self._federate_info = h.helicsFederateClone(federate_info._federate_info)
        elif federate_info is not None and type(federate_info) == FederateInfo and clone is False:
            self._federate_info = federate_info._federate_info
        elif federate_info is not None and type(federate_info) != FederateInfo and clone is False:
            self._federate_info = federate_info
        else:
            self._federate_info = h.helicsCreateFederateInfo()

        self.core_type = core_type

    def __del__(self):
        h.helicsFederateInfoFree(self._federate_info)

    @property
    def core_name(self):
        raise AttributeError("Unreadable attribute `core_name`")

    @core_name.setter
    def core_name(self, core_name: str):
        """Set the core name to use in the federateInfo
        @param corename the core name to use"""
        h.helicsFederateInfoSetCoreName(self._federate_info, core_name)

    @property
    def core_name(self):
        raise AttributeError("Unreadable attribute `core_name`")

    @property
    def separator(self):
        raise AttributeError("Unreadable attribute `separator`")

    @separator.setter
    def separator(self, separator: str):
        """Set the separator character"""
        h.helicsFederateInfoSetSeparator(self._federate_info, separator)

    @property
    def core_init(self):
        raise AttributeError("Unreadable attribute `core_init`")

    @core_init.setter
    def core_init(self, core_init: str):
        """Set the core init string to use in the federateInfo
        @param coreInit the core name to use"""
        h.helicsFederateInfoSetCoreInitString(self._federate_info, core_init)

    @property
    def broker_init(self):
        raise AttributeError("Unreadable attribute `broker_init`")

    @broker_init.setter
    def broker_init(self, broker_init: str):
        """
        Set a string for the broker initialization in command line argument format
        """
        h.helicsFederateInfoSetBrokerInitString(self._federate_info, broker_init)

    @property
    def core_type(self):
        raise AttributeError("Unreadable attribute `core_type`")

    @core_type.setter
    def core_type(self, core_type):
        """set the core type from a string with the core type
        @param coretype the string defining a core type
        """
        if type(core_type) == str:
            h.helicsFederateInfoSetCoreTypeFromString(self._federate_info, core_type)
        elif type(core_type) == int or type(core_type) == h.HelicsCoreType:
            h.helicsFederateInfoSetCoreType(self._federate_info, core_type)

    def broker(self, broker: str):
        """set the broker to connect with
        @param broker a string with the broker connection information or name
        """
        h.helicsFederateInfoSetBroker(self._federate_info, broker)

    def broker_key(self, broker_key: str):
        """set the broker key to use
        @param brokerkey a string with the broker key information
        """
        h.helicsFederateInfoSetBrokerKey(self._federate_info, broker_key)

    def set_flag_option(self, flag: int, value: bool = True):
        """set a flag
        @param flag /ref helics_federate_flags
        @param value the value of the flag usually helics_true or helics_false
        """
        h.helicsFederateInfoSetFlagOption(self._federate_info, flag, value)

    def set_property(self, property, value):
        """set a time federate or core property
        @param timeProperty /ref helics_federate_properties an integer code with the property
        @param timeValue the value to set the property to
        set an integral federate or core property
        @param integerProperty /ref helics_federate_properties an integer code with the property
        @param propertyValue the value to set the property to
        """
        if type(value) == float:
            h.helicsFederateInfoSetTimeProperty(self._federate_info, property, value)
        else:
            h.helicsFederateInfoSetIntegerProperty(self._federate_info, property, value)


class Federate:
    """Federate object"""

    exec_async_iterate = False

    def __init__(self, *, name="", from_config=None, federate_info: FederateInfo = None, federate: Federate = None):
        if from_config is not None:
            self._federate = h.helicsCreateCombinationFederateFromConfig(from_config)
        elif federate is not None:
            self._federate = h.helicsFederateClone(federate._federate)
        elif federate_info is not None:
            self._federate = h.helicsCreateCombinationFederate(name, federate_info)
        else:
            raise h.HelicsException("Cannot create Federate instance")

        assert h.helicsFederateIsValid(self._federate)

        self.property = _FederatePropertyAccessor(self._federate)

    def __repr__(self):

        publications = h.helicsFederateGetPublicationCount(self._federate)
        endpoints = h.helicsFederateGetEndpointCount(self._federate)
        filters = h.helicsFederateGetFilterCount(self._federate)
        inputs = h.helicsFederateGetInputCount(self._federate)
        return f"<helics.{self.__class__.__name__}(publications = {publications}, inputs = {inputs}, endpoints = {endpoints}, filters = {filters}) at {hex(id(self))}>"

    def __del__(self):
        if h.helicsFederateIsValid(self._federate):
            h.helicsFederateFinalize(self._federate)
        h.helicsFederateFree(self._federate)

    def set_flag_option(self, flag: int, value: bool = True):
        """ set a flag for the federate
        @param flag an index into the flag /ref flag-definitions.h
        @param flagValue the value of the flag defaults to true
        """
        h.helicsFederateSetFlagOption(self._federate, flag, value)

    def get_property(self, property):
        """get the value of a property for the federate
        """
        return h.helicsFederateGetTimeProperty(self._federate, property)
        return h.helicsFederateGetIntegerProperty(self._federate, property)

    def set_property(self, property, value):
        """set a time federate or core property
        @param timeProperty /ref helics_federate_properties an integer code with the property
        @param timeValue the value to set the property to
        set an integral federate or core property
        @param integerProperty /ref helics_federate_properties an integer code with the property
        @param propertyValue the value to set the property to
        """
        if type(value) == float:
            h.helicsFederateSetTimeProperty(self._federate, property, value)
        else:
            h.helicsFederateSetIntegerProperty(self._federate, property, value)

    def get_flag_option(self, flag: int):
        """get the value of a flag option
        @param flag an index into the flag /ref flag-definitions.h
        """
        return h.helicsFederateGetFlagOption(self._federate, flag) is True

    @property
    def separator(self):
        raise AttributeError("Unreadable attribute `separator`")

    @separator.setter
    def separator(self, separator: str):
        """specify a separator to use for naming separation between the federate name and the interface
        name setSeparator('.') will result in future registrations of local endpoints such as
        fedName.endpoint setSeparator('/') will result in fedName/endpoint the default is '/'  any
        character can be used though many will not make that much sense.  This call is not thread safe
        and should be called before any local interfaces are created otherwise it may not be possible to
        retrieve them without using the full name.  recommended possibilities are ('.','/', ':','-','_')
        """
        h.helicsFederateSetSeparator(self._federate, separator)

    def registerInterfaces(self, config):
        """ register a set of interfaces defined in a file
        @details call is only valid in startup mode
        @param configString  the location of the file or config String to load to generate the
        interfaces
        """
        h.helicsFederateRegisterInterfaces(self._federate, config)

    @property
    def state(self):
        return h.helicsFederateGetState(self._federate)

    def enter_initializing_mode(self):
        """enter the initialization mode after all interfaces have been defined
        @details the call will block until all federates have entered initialization mode
        """
        h.helicsFederateEnterInitializingMode(self._federate)

    def enter_initializing_mode_async(self):
        """enter the initialization mode after all interfaces have been defined
        @details  the call will not block but a call to enterInitializingModeComplete should be made
        to complete the call sequence
        """
        h.helicsFederateEnterInitializingModeAsync(self._federate)

    def is_async_operation_completed(self):
        """called after one of the async calls and will indicate true if an async operation has
        completed
        @details only call from the same thread as the one that called the initial async call and will
        return false if called when no aysnc operation is in flight"""
        return h.helicsFederateIsAsyncOperationCompleted(self._federate)

    def enter_initializing_mode_complete(self):
        """second part of the async process for entering initializationState call after a call to
        enterInitializingModeAsync if call any other time it will throw an InvalidFunctionCall
        exception"""
        h.helicsFederateEnterInitializingModeComplete(self._federate)

    def enter_executing_mode(self):
        """enter the normal execution mode
        @details call will block until all federates have entered this mode
        @param iterate an optional flag indicating the desired iteration mode
        """
        raise NotImplementedError("TODO: implement this to work for iterative and non iterative modes")
        h.helicsFederateEnterExecutingMode(self._federate)
        # out_iterate = h.helicsFederateEnterExecutingModeIterative(self._federate, iterate)
        # return out_iterate

    def enter_executing_mode_async(self):
        """enter the normal execution mode
        @details call will return immediately but \ref enterExecutingModeComplete should be called to
        complete the operation
        @param iterate an optional flag indicating the desired iteration mode
        """
        raise NotImplementedError("TODO: implement this to work for iterative and non iterative modes")
        h.helicsFederateEnterExecutingModeAsync(self._federate)
        # h.helicsFederateEnterExecutingModeIterativeAsync(self._federate, iterate)

    def enter_executing_mode_complete(self):
        """complete the async call for entering Execution state
        @details call will not block but will return quickly.  The enterInitializingModeComplete must be
        called before doing other operations
        """
        raise NotImplementedError("TODO: implement this to work for iterative and non iterative modes")
        out_iterate = h.helicsFederateEnterExecutingModeIterativeComplete(self._federate)
        h.helicsFederateEnterExecutingModeComplete(self._federate)
        return out_iterate

    def finalize(self):
        """terminate the simulation
        @details call is will block until the finalize has been acknowledged, no commands that interact
        with the core may be called after this function function"""

        # TODO: finalizeAsync and finalizeComplete
        h.helicsFederateFinalize(self._federate)

    def request_time(self, time: float):
        """
        @param time the next requested time step
        @return the granted time step
        """
        return h.helicsFederateRequestTime(self._federate, time)

    def request_next_step(self):
        """request a time advancement to the next allowed time
        @return the granted time step"""
        return h.helicsFederateRequestNextStep(self._federate)

    def request_time_advance(self, time_delta: float):
        """request a time advancement to the next allowed time
        @param timeDelta the amount of time requested to advance
        @return the granted time step"""
        return h.helicsFederateRequestTimeAdvance(self._federate, time_delta)

    def request_time_iterative(self, time: float, iterate: h.HelicsIterationRequest):
        """request a time advancement
        @param time the next requested time step
        @param iterate a requested iteration mode
        @return the granted time step in a structure containing a return time and an iteration_result"""
        grantedTime, status = h.helicsFederateRequestTimeIterative(self._federate, time, iterate)
        return grantedTime, status

    def request_time_async(self, time: float):
        """/**  request a time advancement and return immediately for asynchronous function.
        @details /ref requestTimeComplete should be called to finish the operation and get the result
        @param time the next requested time step
        """
        return h.helicsFederateRequestTimeAsync(self._federate, time)

    def request_time_iterative_async(self, time: float, iterate: h.HelicsIterationRequest):
        """request a time advancement with iterative call and return for asynchronous function.
        @details /ref requestTimeIterativeComplete should be called to finish the operation and get the result
        @param time the next requested time step
        @param iterate a requested iteration level (none, require, optional)
        """
        return h.helicsFederateRequestTimeIterativeAsync(self._federate, time, iterate)

    def request_time_complete(self):
        """request a time advancement
        @return the granted time step"""
        return h.helicsFederateRequestTimeComplete(self._federate)

    def request_time_iterative_complete(self):
        """finalize the time advancement request
        @return the granted time step in an iteration_time structure which contains a time and iteration
        result"""
        granted_time, status = h.helicsFederateRequestTimeIterativeComplete(self._federate)
        return granted_time, status

    @property
    def name(self):
        return h.helicsFederateGetName(self._federate)

    def query(self, target: str, query: str):
        """make a query of the federate
        @details this call is blocking until the value is returned which make take some time depending
        on the size of the federation and the specific string being queried
        @param target  the target of the query can be "federation", "federate", "broker", "core", or a
        specific name of a federate, core, or broker
        @param queryStr a string with the query see other documentation for specific properties to
        query, can be defined by the federate
        @return a string with the value requested.  this is either going to be a vector of strings value
        or a JSON string stored in the first element of the vector.  The string "#invalid" is returned
        if the query was not valid
        """
        q = h.helicsCreateQuery(target, query)
        result = h.helicsQueryExecute(q, self._federate)
        h.helicsQueryFree(q)
        return result

    def register_filter(self, type: h.HelicsFilterType, filter_name: str):
        """define a filter interface
        @details a filter will modify messages coming from or going to target endpoints
        @param type the type of the filter to register
        @param filterName the name of the filter
        """
        return Filter(helicsFederateRegisterFilter(self._federate, type, filter_name))

    def register_cloning_fitler(self, delivery_endpoint):
        """create a cloning Filter on the specified federate
        @details cloning filters copy a message and send it to multiple locations source and destination
        can be added through other functions
        @param deliveryEndpoint the specified endpoint to deliver the message
        @return a helics_filter object
        """
        return CloningFilter(h.helicsFederateRegisterCloningFilter(self._federate, delivery_endpoint))

    def register_global_filter(self, type: h.HelicsFilterType, filter_name):
        """define a filter interface
        @details a filter will modify messages coming from or going to target endpoints
        @param type the type of the filter to register
        @param filterName the name of the filter"""
        return Filter(h.helicsFederateRegisterGlobalFilter(self._federate, type, filter_name))

    def register_global_cloning_filter(self, delivery_endpoint):
        """create a cloning Filter on the specified federate
        @details cloning filters copy a message and send it to multiple locations source and destination
        can be added through other functions
        @param deliveryEndpoint the specified endpoint to deliver the message
        @return a CloningFilter object
        """
        return CloningFilter(h.helicsFederateRegisterGlobalCloningFilter(self._federate, delivery_endpoint))

    def get_filter_name(self, filter_name):
        """get the id of a source filter from the name of the endpoint
        @param filterName the name of the filter
        @return a reference to a filter object which could be invalid if filterName is not valid"""
        return Filter(h.helicsFederateGetFilter(self._federate, filter_name))

    def get_filter_index(self, filter_index):
        """get a filter from its index
        @param index the index of a filter
        @return a reference to a filter object which could be invalid if filterName is not valid"""
        return Filter(h.helicsFederateGetFilterByIndex(self._federate, filter_index))

    def set_global(self, name: str, value: str):
        """set a federation global value
        @details this overwrites any previous value for this name
        @param valueName the name of the global to set
        @param value the value of the global
        """
        h.helicsFederateSetGlobal(self._federate, name, value)

    def add_dependency(self, federate_name):
        """add a dependency for this federate
        @details adds an additional internal time dependency for the federate
        @param fedName the name of the federate to add a dependency on
        """
        h.helicsFederateAddDependency(self._federate, federate_name)

    def local_error(self, error_code: int, error_string: str):
        """generate a local federate error
        @param error_code an error code to give to the error
        @param error_string a string message associated with the error
        """
        h.helicsFederateLocalError(self._federate, error_code)

    def global_error(self, error_code: int, error_string: str):
        """generate a global error to terminate the federation
        @param error_code an error code to give to the error
        @param error_string a string message associated with the error
        """
        h.helicsFederateGlobalError(self._federate, error_code)

    def log_message(self, message: str, level):
        """log an message"""
        if level == logging.ERROR:
            h.helicsFederateLogErrorMessage(self._federate, message)
        elif level == logging.WARN:
            h.helicsFederateLogWarningMessage(self._federate, message)
        elif level == logging.INFO:
            h.helicsFederateLogInfoMessage(self._federate, message)
        elif level == logging.DEBUG:
            h.helicsFederateLogDebugMessage(self._federate, message)

    @property
    def core(self):
        return Core(core=h.helicsFederateGetCoreObject(self._federate))


class _PublicationOptionAccessor:
    def __init__(self, publication):
        self._publication = publication

    def __getitem__(self, index):
        if type(index) == str:
            idx = h.helicsGetOptionIndex(index)
        else:
            idx = h.HelicsHandleOption(index)
        return h.helicsPublicationGetOption(self._publication, index)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = h.helicsGetOptionIndex(index)
        else:
            idx = h.HelicsHandleOption(index)
        return h.helicsPublicationSetOption(self._publication, index, value)

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class _FederateFlagAccessor:
    def __init__(self, federate):
        self._federate = federate

    def __getitem__(self, index):
        if type(index) == str:
            idx = h.helicsGetFlagIndex(index)
        else:
            idx = h.HelicsFederateFlag(index)
        return h.helicsFederateGetFlagOption(self._federate, index)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = h.helicsGetFlagIndex(index)
        else:
            idx = h.HelicsFederateFlag(index)
        return h.helicsFederateSetFlagOption(self._federate, index, value)

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")


class _FederatePropertyAccessor:
    def __init__(self, federate):
        self._federate = federate

    def __getitem__(self, index):
        if type(index) == str:
            idx = h.helicsGetPropertyIndex(index)
        else:
            idx = h.HelicsProperty(index)
        if "TIME_" in idx.name:
            return h.helicsFederateGetTimeProperty(self._federate, index)
        elif "INT_" in idx.name:
            return h.helicsFederateGetIntegerProperty(self._federate, index)

    def __setitem__(self, index, value):
        if type(index) == str:
            idx = h.helicsGetPropertyIndex(index)
        else:
            idx = h.HelicsProperty(index)
        if "TIME_" in idx.name:
            return h.helicsFederateSetTimeProperty(self._federate, idx, value)
        elif "INT_" in idx.name:
            return h.helicsFederateSetIntegerProperty(self._federate, index, value)

    def __repr__(self):
        l = []
        for p in h.HelicsProperty:
            l.append(f"{p.name} = {self[p]}")
        return f"<HelicsProperty({', '.join(l)})>"

    def __delitem__(self, index):
        raise NotImplementedError("Cannot delete index")
