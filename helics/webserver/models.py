"""Request and response models for the HELICS web API."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

from ..query_models import QueryResponse


class BrokerCreateRequest(BaseModel):
    """Configuration for a broker owned by this web server."""

    name: str = Field(min_length=1, max_length=256, description="Unique broker name")
    core_type: str = Field(default="zmq", min_length=1, description="HELICS core type")
    arguments: List[str] = Field(
        default_factory=list,
        description="Additional HELICS broker command-line arguments",
    )
    num_federates: Optional[int] = Field(default=None, ge=1)
    num_brokers: Optional[int] = Field(default=None, ge=1)
    port: Optional[int] = Field(default=None, ge=1, le=65535)
    interface: Optional[str] = Field(default=None, min_length=1)
    log_level: Optional[str] = Field(default=None, min_length=1)

    @field_validator("arguments")
    @classmethod
    def arguments_must_not_contain_empty_values(cls, values: List[str]) -> List[str]:
        if any(not value.strip() for value in values):
            raise ValueError("arguments must not contain empty values")
        return values

    def broker_arguments(self) -> List[str]:
        """Return arguments in the format expected by HELICS."""
        arguments = list(self.arguments)
        if self.num_federates is not None:
            arguments.append(f"--federates={self.num_federates}")
        if self.num_brokers is not None:
            arguments.append(f"--minbrokers={self.num_brokers}")
        if self.port is not None:
            arguments.append(f"--port={self.port}")
        if self.interface is not None:
            arguments.append(f"--interface={self.interface}")
        if self.log_level is not None:
            arguments.append(f"--loglevel={self.log_level}")
        return arguments


class BrokerSummary(BaseModel):
    name: str
    address: str
    is_connected: bool
    is_root: bool
    is_open_to_new_federates: bool


class BrokerListResponse(BaseModel):
    brokers: List[BrokerSummary]


class QueryRequest(BaseModel):
    target: str = Field(default="root", min_length=1)
    query: str = Field(default="current_state", min_length=1)


class CommandRequest(BaseModel):
    target: str = Field(default="root", min_length=1)
    command: str = Field(min_length=1)


class TimeBarrierRequest(BaseModel):
    time: float = Field(ge=0)


class ActionResponse(BaseModel):
    status: str = "ok"


class HealthResponse(BaseModel):
    status: str = "ok"
