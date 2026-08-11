"""Thread-safe, in-process ownership of HELICS brokers."""

from __future__ import annotations

from threading import RLock
from typing import Callable, Dict, List

from .. import HelicsBroker, helicsCreateBrokerFromArgs
from .models import BrokerCreateRequest, BrokerSummary


class BrokerNotFoundError(LookupError):
    """Raised when a request refers to a broker not owned by this service."""


class BrokerAlreadyExistsError(ValueError):
    """Raised when a broker name is already registered."""


class BrokerService:
    """Manage the lifetime of brokers created through the web API.

    HELICS broker calls are made under a single lock.  This keeps the API
    predictable while queries and lifecycle operations are run from FastAPI's
    worker thread pool rather than blocking the event loop.
    """

    def __init__(
        self,
        create_broker: Callable[[str, str, List[str]], HelicsBroker] = helicsCreateBrokerFromArgs,
    ) -> None:
        self._create_broker = create_broker
        self._brokers: Dict[str, HelicsBroker] = {}
        self._lock = RLock()

    @staticmethod
    def _summary(broker: HelicsBroker) -> BrokerSummary:
        return BrokerSummary(
            name=broker.identifier,
            address=broker.address,
            is_connected=broker.is_connected(),
            is_root=broker.is_root(),
            is_open_to_new_federates=broker.is_open_to_new_federates(),
        )

    def create(self, request: BrokerCreateRequest) -> BrokerSummary:
        with self._lock:
            if request.name in self._brokers:
                raise BrokerAlreadyExistsError(request.name)
            broker = self._create_broker(
                request.core_type,
                request.name,
                request.broker_arguments(),
            )
            identifier = broker.identifier
            if identifier in self._brokers:
                broker.disconnect()
                raise BrokerAlreadyExistsError(identifier)
            self._brokers[identifier] = broker
            return self._summary(broker)

    def list(self) -> List[BrokerSummary]:
        with self._lock:
            return [self._summary(broker) for broker in self._brokers.values()]

    def summary(self, name: str) -> BrokerSummary:
        with self._lock:
            return self._summary(self.get(name))

    def get(self, name: str) -> HelicsBroker:
        with self._lock:
            try:
                return self._brokers[name]
            except KeyError as error:
                raise BrokerNotFoundError(name) from error

    def query(self, name: str, target: str, query: str):
        with self._lock:
            return self.get(name).query(target, query)

    def send_command(self, name: str, target: str, command: str) -> None:
        with self._lock:
            self.get(name).send_command(target, command)

    def set_time_barrier(self, name: str, time: float) -> None:
        with self._lock:
            self.get(name).set_time_barrier(time)

    def clear_time_barrier(self, name: str) -> None:
        with self._lock:
            self.get(name).clear_time_barrier()

    def delete(self, name: str) -> None:
        with self._lock:
            broker = self.get(name)
            broker.disconnect()
            del self._brokers[name]

    def shutdown(self) -> None:
        with self._lock:
            for broker in self._brokers.values():
                broker.disconnect()
            self._brokers.clear()
