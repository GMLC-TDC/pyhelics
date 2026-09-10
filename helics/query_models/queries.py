"""Typed response models for standard HELICS queries.

Each standard query can register its response model here without coupling
query parsing to the web server implementation.  Structured queries use
flexible Pydantic objects until their nested HELICS schemas are stabilized.
"""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Type

from pydantic import BaseModel, ConfigDict, Field, ValidationError


class QueryResponse(BaseModel):
    """The common envelope returned for every HELICS query."""

    target: str
    query: str
    value: Any


class BooleanQueryResponse(QueryResponse):
    """Envelope for a HELICS query whose value is a boolean."""

    value: bool


class IsConnectedQueryResponse(QueryResponse):
    """Response from HELICS' standard ``isconnected`` query."""

    query: Literal["isconnected"]
    value: bool


class StringQueryResponse(QueryResponse):
    """Envelope for a HELICS query whose value is a string."""

    value: str


class StringListQueryResponse(QueryResponse):
    """Envelope for a HELICS query returning named HELICS objects."""

    value: List[str]


class StructuredQueryResponse(QueryResponse):
    """Envelope for HELICS introspection queries returning JSON objects."""

    value: Dict[str, Any]


class CounterQueryResponse(QueryResponse):
    """Envelope for the numeric federation-change counter."""

    value: int


class QueryObject(BaseModel):
    """Common shape for objects returned by HELICS introspection queries."""

    model_config = ConfigDict(extra="allow")


class CurrentStateValue(QueryObject):
    attributes: Dict[str, Any] = Field(default_factory=dict)
    brokers: List[Any] = Field(default_factory=list)
    cores: List[Any] = Field(default_factory=list)
    federates: List[Any] = Field(default_factory=list)
    state: Optional[str] = None
    status: Optional[bool] = None


class CurrentStateQueryResponse(QueryResponse):
    """Envelope for a broker/core ``current_state`` query."""

    value: CurrentStateValue


class CountsValue(QueryObject):
    attributes: Dict[str, Any] = Field(default_factory=dict)
    brokers: int = 0
    countable_federates: int = 0
    federates: int = 0
    interfaces: int = 0


class CountsQueryResponse(QueryResponse):
    """Envelope for a broker/core ``counts`` query."""

    value: CountsValue


class StatusValue(QueryObject):
    attributes: Dict[str, Any] = Field(default_factory=dict)
    state: Optional[str] = None
    status: Optional[bool] = None


class StatusQueryResponse(QueryResponse):
    """Envelope for a broker/core ``status`` query."""

    value: StatusValue


class VersionAllValue(QueryObject):
    attributes: Dict[str, Any] = Field(default_factory=dict)
    brokers: List[Any] = Field(default_factory=list)
    version: str


class VersionAllQueryResponse(QueryResponse):
    """Envelope for a broker/core ``version_all`` query."""

    value: VersionAllValue


class GlobalStatusValue(QueryObject):
    status: Optional[str] = None
    timestep: Optional[float] = None


class GlobalStatusQueryResponse(QueryResponse):
    """Envelope for a broker ``global_status`` query."""

    value: GlobalStatusValue


STANDARD_QUERY_RESPONSES: Dict[str, Type[QueryResponse]] = {
    "name": StringQueryResponse,
    "address": StringQueryResponse,
    "isinit": BooleanQueryResponse,
    "isconnected": IsConnectedQueryResponse,
    "publications": StringListQueryResponse,
    "endpoints": StringListQueryResponse,
    "inputs": StringListQueryResponse,
    "filters": StringListQueryResponse,
    "federates": StringListQueryResponse,
    "brokers": StringListQueryResponse,
    "dependson": StringListQueryResponse,
    "dependents": StringListQueryResponse,
    "queries": StringListQueryResponse,
    "version": StringQueryResponse,
    "counter": CounterQueryResponse,
    "monitor": StringQueryResponse,
    "current_state": CurrentStateQueryResponse,
    "counts": CountsQueryResponse,
    "status": StatusQueryResponse,
    "version_all": VersionAllQueryResponse,
    "publication_details": StructuredQueryResponse,
    "input_details": StructuredQueryResponse,
    "endpoint_details": StructuredQueryResponse,
    "filter_details": StructuredQueryResponse,
    "dependencies": StructuredQueryResponse,
    "barriers": StructuredQueryResponse,
    "global_state": StructuredQueryResponse,
    "global_time": StructuredQueryResponse,
    "federate_map": StructuredQueryResponse,
    "dependency_graph": StructuredQueryResponse,
    "data_flow_graph": StructuredQueryResponse,
    "logs": StructuredQueryResponse,
    "global_time_debugging": StructuredQueryResponse,
    "global_flush": StructuredQueryResponse,
    "global_status": GlobalStatusQueryResponse,
}


def parse_query_response(target: str, query: str, value: Any) -> QueryResponse:
    """Validate a standard HELICS query response or retain a custom response.

    User-defined queries remain valid HELICS queries.  They use the common
    envelope until an application provides a model for their query name.
    """
    normalized_query = query.lower()
    response_data = {"target": target, "query": normalized_query, "value": value}
    response_model = STANDARD_QUERY_RESPONSES.get(normalized_query, QueryResponse)
    try:
        return response_model.model_validate(response_data)
    except ValidationError:
        # HELICS returns structured error objects for unavailable queries.  A
        # failed validation must not hide that response or break custom query
        # compatibility, so retain the common envelope in that case.
        return QueryResponse.model_validate(response_data)
