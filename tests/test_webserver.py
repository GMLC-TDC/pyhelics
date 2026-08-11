"""Tests for the FastAPI broker-management API."""

from fastapi.testclient import TestClient

from helics.webserver.app import create_app
from helics.webserver.broker_service import BrokerService


class FakeBroker:
    def __init__(self, name, arguments):
        self.identifier = name
        self.address = "tcp://127.0.0.1:23404"
        self.arguments = arguments
        self.disconnected = False
        self.barrier = None
        self.commands = []

    def is_connected(self):
        return not self.disconnected

    def is_root(self):
        return True

    def is_open_to_new_federates(self):
        return not self.disconnected

    def query(self, target, query):
        if query == "isconnected":
            return True
        return {"target": target, "query": query}

    def disconnect(self):
        self.disconnected = True

    def send_command(self, target, command):
        self.commands.append((target, command))

    def set_time_barrier(self, value):
        self.barrier = value

    def clear_time_barrier(self):
        self.barrier = None


def make_client():
    created = {}

    def create_broker(core_type, name, arguments):
        broker = FakeBroker(name, arguments)
        created[name] = broker
        return broker

    service = BrokerService(create_broker=create_broker)
    return TestClient(create_app(service)), created


def test_broker_lifecycle():
    client, created = make_client()
    with client:
        response = client.get("/api/v1/health")
        assert response.status_code == 200

        response = client.post(
            "/api/v1/brokers",
            json={"name": "broker", "core_type": "test", "num_federates": 2},
        )
        assert response.status_code == 201
        assert response.json()["name"] == "broker"
        assert created["broker"].arguments == ["--federates=2"]

        assert client.post("/api/v1/brokers", json={"name": "broker"}).status_code == 409
        assert client.get("/api/v1/brokers").json()["brokers"][0]["is_root"] is True
        assert client.get("/api/v1/brokers/broker/state").json()["value"] == {
            "target": "root",
            "query": "current_state",
        }
        assert client.get("/api/v1/brokers/broker/connection").json()["value"] is True
        assert client.delete("/api/v1/brokers/broker").status_code == 204
        assert client.get("/api/v1/brokers/broker").status_code == 404


def test_broker_control_routes():
    client, created = make_client()
    with client:
        assert client.post("/api/v1/brokers", json={"name": "broker"}).status_code == 201
        assert client.post(
            "/api/v1/brokers/broker/query",
            json={"target": "root", "query": "current_state"},
        ).json()["value"] == {"target": "root", "query": "current_state"}
        assert client.post(
            "/api/v1/brokers/broker/query",
            json={"target": "root", "query": "isconnected"},
        ).json()["value"] is True
        assert client.post(
            "/api/v1/brokers/broker/commands",
            json={"target": "fed", "command": "stop"},
        ).status_code == 200
        assert client.put(
            "/api/v1/brokers/broker/time-barrier", json={"time": 2.5}
        ).status_code == 200
        assert client.delete("/api/v1/brokers/broker/time-barrier").status_code == 200

    assert created["broker"].commands == [("fed", "stop")]
    assert created["broker"].barrier is None
