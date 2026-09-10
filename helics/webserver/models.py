"""Request and response models for the HELICS web API."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator

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
    local_federates: Optional[int] = Field(
        default=None,
        ge=0,
        description="Minimum direct-child federates before initialization",
    )
    local_subbrokers: Optional[int] = Field(
        default=None,
        ge=0,
        description="Minimum direct-child brokers before initialization",
    )
    required_federates: List[str] = Field(
        default_factory=list,
        description="Federate names that must register before initialization",
    )
    port: Optional[int] = Field(default=None, ge=1, le=65535)
    interface: Optional[str] = Field(default=None, min_length=1)
    log_level: Optional[str] = Field(default=None, min_length=1)

    @field_validator("arguments")
    @classmethod
    def arguments_must_not_contain_empty_values(cls, values: List[str]) -> List[str]:
        if any(not value.strip() for value in values):
            raise ValueError("arguments must not contain empty values")
        return values

    @field_validator("required_federates")
    @classmethod
    def required_federates_must_be_names(cls, values: List[str]) -> List[str]:
        normalized = []
        for value in values:
            value = value.strip()
            if not value or "," in value or "\x00" in value:
                raise ValueError(
                    "required_federates names must be non-empty and must not contain commas"
                )
            normalized.append(value)
        return normalized

    def broker_arguments(self) -> List[str]:
        """Return arguments in the format expected by HELICS."""
        arguments = list(self.arguments)
        if self.num_federates is not None:
            arguments.append(f"--federates={self.num_federates}")
        if self.num_brokers is not None:
            arguments.append(f"--minbrokers={self.num_brokers}")
        if self.local_federates is not None:
            arguments.append(f"--local_federates={self.local_federates}")
        if self.local_subbrokers is not None:
            arguments.append(f"--local_subbrokers={self.local_subbrokers}")
        if self.required_federates:
            arguments.append(f"--required_federates={','.join(self.required_federates)}")
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


RunnerStatus = Literal["pending", "running", "success", "failed", "terminated", "unknown"]


class RunnerFederateConfig(BaseModel):
    """Validated federate configuration consumed by ``helics run``."""

    name: str = Field(min_length=1, max_length=256)
    exec: str = Field(min_length=1, description="Executable and arguments for the federate")
    directory: str = Field(default=".", min_length=1)
    host: str = Field(default="localhost", min_length=1)
    env: Dict[str, str] = Field(default_factory=dict)

    @field_validator("name", "exec", "directory", "host")
    @classmethod
    def values_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("value must not be blank")
        if "\x00" in value:
            raise ValueError("value must not contain NUL bytes")
        return value

    @field_validator("env")
    @classmethod
    def environment_keys_must_be_valid(cls, values: Dict[str, str]) -> Dict[str, str]:
        for key, value in values.items():
            if not key or "=" in key or "\x00" in key:
                raise ValueError("environment variable names must be non-empty and not contain '='")
            if "\x00" in value:
                raise ValueError("environment variable values must not contain NUL bytes")
        return values


class RunnerConfig(BaseModel):
    """Complete, typed runner configuration.

    Unknown top-level fields are retained for forward compatibility with
    HELICS runner files, while the fields used to launch local processes are
    validated here before a run starts.
    """

    name: str = Field(default="HELICS Federation", min_length=1, max_length=256)
    federates: List[RunnerFederateConfig] = Field(default_factory=list)
    broker: bool = False
    logging_path: Optional[str] = None
    model_config = {"extra": "allow"}

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("name must not be blank")
        return value

    @field_validator("logging_path")
    @classmethod
    def logging_path_must_not_be_blank(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("logging_path must not be blank")
        if value is not None and "\x00" in value:
            raise ValueError("logging_path must not contain NUL bytes")
        return value

    @model_validator(mode="after")
    def federate_names_must_be_unique(self) -> "RunnerConfig":
        names = [federate.name for federate in self.federates]
        if len(names) != len(set(names)):
            duplicates = sorted({name for name in names if names.count(name) > 1})
            raise ValueError("federate names must be unique: " + ", ".join(duplicates))
        if self.broker and "broker" in names:
            raise ValueError("broker is reserved for the auto-created broker")
        return self


# Descriptive aliases for callers that prefer the full model names.
RunnerConfiguration = RunnerConfig
RunnerFederateConfiguration = RunnerFederateConfig


class RunnerFederate(BaseModel):
    """A federate entry in a runner configuration."""

    name: str = Field(min_length=1)
    exec: str = Field(min_length=1)
    directory: str = "."
    host: str = "localhost"
    old_name: Optional[str] = None
    log_available: bool = False
    status: Optional[RunnerStatus] = None
    model_config = {"extra": "allow"}


class RunnerFileResponse(BaseModel):
    """Runner configuration plus server-managed file metadata."""

    federates: List[RunnerFederate] = Field(default_factory=list)
    folder: str
    path: str
    filename: str
    broker: bool = False
    model_config = {"extra": "allow"}


class RunnerPathRequest(BaseModel):
    path: str = Field(min_length=1)


class RunnerNameRequest(BaseModel):
    name: str = Field(min_length=1)


class RunnerFolderRequest(BaseModel):
    folder: str = Field(min_length=1)


class RunnerFederateEdit(BaseModel):
    name: str = Field(min_length=1)
    exec: str = Field(min_length=1)
    directory: str = "."
    old_name: Optional[str] = None
    host: str = "localhost"


class RunnerStatusRequest(BaseModel):
    name: str = Field(min_length=1)
    status: RunnerStatus


class RunnerStatusResponse(BaseModel):
    status: Optional[RunnerStatus] = None


class RunnerProcessInfo(BaseModel):
    """Metadata for the process tree owned by a runner execution."""

    pid: int = Field(ge=1)
    runner_path: str
    server_url: str
    started_at: datetime
    owns_process_tree: bool = Field(
        default=True,
        description="The service owns and cleans up this process and all descendants",
    )
    broker_managed: bool = Field(
        default=False,
        description="The runner configuration requested an automatic HELICS broker",
    )


class RunnerRunResponse(BaseModel):
    status: bool
    process: Optional[RunnerProcessInfo] = None


class LogResponse(BaseModel):
    log: str


RunnerLogResponse = LogResponse


class DatabaseInfo(BaseModel):
    path: str
    exists: bool


class UploadResponse(BaseModel):
    status: str = "success"
    path: Optional[str] = None


class ProfileInterval(BaseModel):
    name: str
    s_enter: Optional[float] = None
    s_end: Optional[float] = None
    r_enter: Optional[float] = None
    r_end: Optional[float] = None


class ProfileResponse(BaseModel):
    profiles: Dict[str, List[ProfileInterval]]


class ObserverRow(BaseModel):
    """A database row returned by an observer endpoint."""

    model_config = {"extra": "allow"}

    # Keeping rows open-ended is intentional: observer databases can contain
    # dynamically generated publication columns.
    values: Dict[str, Any] = Field(default_factory=dict)
