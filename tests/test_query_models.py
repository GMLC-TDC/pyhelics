"""Tests for typed HELICS query envelopes."""

from helics.query_models import (
    CounterQueryResponse,
    CountsQueryResponse,
    CurrentStateQueryResponse,
    GlobalStatusQueryResponse,
    IsConnectedQueryResponse,
    QueryResponse,
    StringListQueryResponse,
    StringQueryResponse,
    parse_query_response,
)


def test_standard_query_responses_are_typed():
    assert isinstance(parse_query_response("root", "isconnected", True), IsConnectedQueryResponse)
    assert isinstance(parse_query_response("root", "name", "broker"), StringQueryResponse)
    assert isinstance(parse_query_response("root", "federates", ["fed"]), StringListQueryResponse)
    assert isinstance(parse_query_response("root", "counter", -3), CounterQueryResponse)
    assert isinstance(
        parse_query_response(
            "root",
            "current_state",
            {"attributes": {}, "brokers": [], "cores": [], "federates": [], "state": "connected"},
        ),
        CurrentStateQueryResponse,
    )
    assert isinstance(
        parse_query_response(
            "root",
            "counts",
            {"attributes": {}, "brokers": 0, "countable_federates": 0, "federates": 0, "interfaces": 0},
        ),
        CountsQueryResponse,
    )
    assert isinstance(
        parse_query_response("root", "global_status", {"status": "init_requested", "timestep": -1}),
        GlobalStatusQueryResponse,
    )


def test_unknown_and_invalid_standard_responses_keep_generic_envelope():
    unknown = parse_query_response("root", "custom_query", {"answer": 42})
    assert isinstance(unknown, QueryResponse)
    assert unknown.query == "custom_query"

    # HELICS uses an error object when a standard query is unavailable.
    invalid = parse_query_response("root", "federates", {"error": {"code": 404}})
    assert type(invalid) is QueryResponse
    assert invalid.value["error"]["code"] == 404
