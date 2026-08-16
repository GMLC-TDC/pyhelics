"""Real-HELICS acceptance tests for the FastAPI broker API.

These tests replace the lifecycle, query, and time-barrier coverage in
HELICS' former HTTP and WebSocket web-server test suites.  The FastAPI API
uses explicit resource routes and JSON request bodies, so it intentionally
does not reproduce the native server's path and custom-HTTP-verb variants.
"""

from __future__ import annotations

import time
from uuid import uuid4

import helics as h
from fastapi.testclient import TestClient

from helics.webserver import create_app


def unique_name(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def create_value_federate(broker_name: str, federate_name: str, federate_count: int):
    """Create an in-process value federate connected to an API-owned broker."""
    fedinfo = h.helicsCreateFederateInfo()
    h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "inproc")
    h.helicsFederateInfoSetCoreInitString(
        fedinfo,
        f"--broker={broker_name} --federates={federate_count}",
    )
    return h.helicsCreateValueFederate(federate_name, fedinfo), fedinfo


def test_webserver_broker_lifecycle_and_query():
    """Create, inspect, query, list, and delete a real local broker."""
    broker_name = unique_name("web_broker")

    with TestClient(create_app()) as client:
        response = client.get("/api/v1/brokers")
        assert response.status_code == 200
        assert response.json() == {"brokers": []}

        response = client.post(
            "/api/v1/brokers",
            json={
                "name": broker_name,
                "core_type": "inproc",
                "num_federates": 1,
            },
        )
        assert response.status_code == 201, response.text
        summary = response.json()
        assert summary["name"] == broker_name
        assert summary["is_connected"] is True
        assert summary["is_root"] is True
        assert summary["is_open_to_new_federates"] is True

        response = client.get("/api/v1/brokers")
        assert response.status_code == 200
        assert [broker["name"] for broker in response.json()["brokers"]] == [broker_name]

        response = client.get(f"/api/v1/brokers/{broker_name}/state")
        assert response.status_code == 200, response.text
        result = response.json()
        assert result["target"] == "root"
        assert result["query"] == "current_state"
        assert result["value"]["attributes"]["name"] == broker_name

        response = client.get(f"/api/v1/brokers/{broker_name}/connection")
        assert response.status_code == 200, response.text
        assert response.json() == {
            "target": "root",
            "query": "isconnected",
            "value": True,
        }

        response = client.post(
            f"/api/v1/brokers/{broker_name}/query",
            json={"target": "root", "query": "isconnected"},
        )
        assert response.status_code == 200, response.text
        assert response.json()["value"] is True

        assert client.post(
            "/api/v1/brokers",
            json={"name": broker_name, "core_type": "inproc"},
        ).status_code == 409
        assert client.get("/api/v1/brokers/does-not-exist").status_code == 404

        assert client.delete(f"/api/v1/brokers/{broker_name}").status_code == 204
        assert client.get(f"/api/v1/brokers/{broker_name}").status_code == 404


def test_webserver_time_barrier_controls_real_federate():
    """A time barrier set through the API must constrain time grants."""
    broker_name = unique_name("web_barrier")
    federate_name = unique_name("web_federate")

    with TestClient(create_app()) as client:
        response = client.post(
            "/api/v1/brokers",
            json={
                "name": broker_name,
                "core_type": "inproc",
                "num_federates": 1,
            },
        )
        assert response.status_code == 201, response.text

        federate, fedinfo = create_value_federate(broker_name, federate_name, 1)

        try:
            assert client.put(
                f"/api/v1/brokers/{broker_name}/time-barrier",
                json={"time": 2.0},
            ).status_code == 200

            h.helicsFederateEnterExecutingMode(federate)
            assert h.helicsFederateRequestTime(federate, 1.75) == 1.75

            h.helicsFederateRequestTimeAsync(federate, 3.0)
            time.sleep(0.05)
            assert h.helicsFederateIsAsyncOperationCompleted(federate) is False

            assert client.put(
                f"/api/v1/brokers/{broker_name}/time-barrier",
                json={"time": 5.0},
            ).status_code == 200
            assert h.helicsFederateRequestTimeComplete(federate) == 3.0

            h.helicsFederateRequestTimeAsync(federate, 6.0)
            time.sleep(0.05)
            assert h.helicsFederateIsAsyncOperationCompleted(federate) is False

            assert client.delete(
                f"/api/v1/brokers/{broker_name}/time-barrier"
            ).status_code == 200
            assert h.helicsFederateRequestTimeComplete(federate) == 6.0
        finally:
            h.helicsFederateDisconnect(federate)
            h.helicsFederateFree(federate)
            h.helicsFederateInfoFree(fedinfo)

        assert client.delete(f"/api/v1/brokers/{broker_name}").status_code == 204


def test_webserver_command_reaches_real_federate():
    """A command submitted to the API must arrive at its federate target."""
    broker_name = unique_name("web_command_broker")
    sender_name = unique_name("web_command_sender")
    receiver_name = unique_name("web_command_receiver")

    with TestClient(create_app()) as client:
        response = client.post(
            "/api/v1/brokers",
            json={
                "name": broker_name,
                "core_type": "inproc",
                "num_federates": 2,
            },
        )
        assert response.status_code == 201, response.text

        sender, sender_info = create_value_federate(broker_name, sender_name, 2)
        receiver, receiver_info = create_value_federate(broker_name, receiver_name, 2)

        try:
            response = client.post(
                f"/api/v1/brokers/{broker_name}/commands",
                json={"target": receiver_name, "command": "suspend"},
            )
            assert response.status_code == 200, response.text

            h.helicsFederateEnterExecutingModeAsync(sender)
            h.helicsFederateEnterExecutingMode(receiver)
            h.helicsFederateEnterExecutingModeComplete(sender)

            assert h.helicsFederateGetCommand(receiver) == "suspend"
            assert h.helicsFederateGetCommandSource(receiver) == broker_name

            response = client.post(
                f"/api/v1/brokers/{broker_name}/query",
                json={"target": receiver_name, "query": "current_state"},
            )
            assert response.status_code == 200, response.text
            assert response.json()["value"]["attributes"]["name"] == receiver_name
        finally:
            h.helicsFederateDisconnect(sender)
            h.helicsFederateDisconnect(receiver)
            h.helicsFederateFree(sender)
            h.helicsFederateFree(receiver)
            h.helicsFederateInfoFree(sender_info)
            h.helicsFederateInfoFree(receiver_info)

        assert client.delete(f"/api/v1/brokers/{broker_name}").status_code == 204
