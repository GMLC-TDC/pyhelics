"""Typed response models for standard HELICS queries.

The registry is intentionally small at first.  Each additional standard query
can register its response model here without coupling query parsing to the web
server implementation.
"""

from __future__ import annotations

from typing import Any, Dict, Literal, Type

from pydantic import BaseModel


class QueryResponse(BaseModel):
    """The common envelope returned for every HELICS query."""

    target: str
    query: str
    value: Any


class IsConnectedQueryResponse(QueryResponse):
    """Response from HELICS' standard ``isconnected`` query."""

    query: Literal["isconnected"]
    value: bool


STANDARD_QUERY_RESPONSES: Dict[str, Type[QueryResponse]] = {
    "isconnected": IsConnectedQueryResponse,
}


def parse_query_response(target: str, query: str, value: Any) -> QueryResponse:
    """Validate a standard HELICS query response or retain a custom response.

    User-defined queries remain valid HELICS queries.  They use the common
    envelope until an application provides a model for their query name.
    """
    response_model = STANDARD_QUERY_RESPONSES.get(query.lower(), QueryResponse)
    return response_model.model_validate(
        {
            "target": target,
            "query": query.lower(),
            "value": value,
        }
    )
