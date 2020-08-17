# -*- coding: utf-8 -*-
from . import capi as h
from typing import List


class Broker:
    def __init__(self, *, type: str, name: str, initString: str = "", arguments: List[str] = [], broker=None):

        if len(arguments) > 0:
            self._broker = h.helicsCreateBrokerFromArgs(type, name, arguments)
        elif broker is not None:
            if type(broker) is Broker:
                self._broker = h.helicsBrokerClone(broker._broker)
            else:
                raise NotImplementedError("Received `broker` keyword argument that is not of type python `Broker`")
        else:
            self._broker = h.helicsCreateBroker(type, name, initString)

    def __del__(self):
        h.helicsBrokerFree(self._broker)

    def is_connected(self):
        """check if the broker is connected"""
        return h.helicsBrokerIsConnected(self._broker) is True

    def wait_for_disconnect(self, ms_to_wait: int = -1):
        """ waits in the current thread until the broker is disconnected
        - `ms_to_wait`  the timeout to wait for disconnect (-1) implies no timeout

        Returns: `True` if the disconnect was successful false if it timed out
        """
        return h.helicsBrokerWaitForDisconnect(self._broker, ms_to_wait) is True

    def disconnect(self):
        """disconnect the broker from any other brokers and communications"""
        return h.helicsBrokerDisconnect(self._broker)

    @property
    def identifier(self):
        """get the local identification for the broker"""
        return h.helicsBrokerGetIdentifier(self._broker)

    @property
    def address(self):
        """get the connection address for the broker"""
        return h.helicsBrokerGetAddress(self._broker)

    def set_global(self, name: str, value: str):
        """ set a federation global value
        @details this overwrites any previous value for this name
        globals can be queried with a target of "global" and queryStr of the value to Query
        @param valueName the name of the global to set
        @param value the value of the global
        """
        h.helicsBrokerSetGlobal(self._broker, name, value)

    def data_link(self, source: str, target: str):
        """ create a data link between a named publication and a named input
         @param source the name of the publication
         @param target the name of the input"""
        h.helicsBrokerDataLink(self._broker, source, target)

    def add_source_filter_to_endpoint(self, filter: str, target: str):
        """ create a filter connection between a named filter and a named endpoint for messages coming
        from that endpoint
        @param filter the name of the filter
        @param target the name of the source target"""
        h.helicsBrokerAddSourceFilterToEndpoint(self.broker, filter, target)

    def add_destination_filter_to_endpoint(self, filter: str, target: str):
        """ create a filter connection between a named filter and a named endpoint for destination
        processing
        @param filter the name of the filter
        @param target the name of the source target"""
        h.helicsBrokerAddDestinationFilterToEndpoint(self._broker, filter, target)

    def query(self, target: str, queryStr) -> str:
        """make a query of the broker
        @details this call is blocking until the value is returned which may take some time depending
        on the size of the federation and the specific string being queried
        @param target  the target of the query can be "federation", "federate", "broker", "core", or a
        specific name of a federate, core, or broker
        @param queryStr a string with the query, see other documentation for specific properties to
        query, can be defined by the federate
        @return a string with the value requested.  this is either going to be a vector of strings value
        or a JSON string stored in the first element of the vector.  The string "#invalid" is returned
        if the query was not valid
        """
        q = h.helicsCreateQuery(target, queryStr)
        result = h.helicsQueryBrokerExecute(q, self._broker)
        h.helicsQueryFree(q)
        return result
