"""Tests for the FastAPI broker-management API."""

from fastapi.testclient import TestClient

from helics.webserver.app import create_app
from helics.webserver.broker_service import BrokerService
from helics.webserver.models import BrokerCreateRequest


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
        if query == "counts":
            return {
                "attributes": {"name": self.identifier},
                "brokers": 0,
                "countable_federates": 0,
                "federates": 0,
                "interfaces": 0,
            }
        if query == "version":
            return "3.7.0"
        if query == "current_state":
            return {
                "attributes": {"name": self.identifier},
                "brokers": [],
                "cores": [],
                "federates": [],
                "state": "connected",
                "status": True,
            }
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
        assert client.get("/api/v1/brokers/broker/state").json()["value"]["state"] == "connected"
        assert client.get("/api/v1/brokers/broker/counts").json()["value"]["interfaces"] == 0
        assert client.get("/api/v1/brokers/broker/version").json()["value"] == "3.7.0"
        assert client.get("/api/v1/brokers/broker/connection").json()["value"] is True
        assert client.delete("/api/v1/brokers/broker").status_code == 204
        assert client.get("/api/v1/brokers/broker").status_code == 404


def test_broker_control_routes():
    client, created = make_client()
    with client:
        assert client.post("/api/v1/brokers", json={"name": "broker"}).status_code == 201
        assert (
            client.post(
                "/api/v1/brokers/broker/query",
                json={"target": "root", "query": "current_state"},
            ).json()["value"]["state"]
            == "connected"
        )
        assert (
            client.post(
                "/api/v1/brokers/broker/query",
                json={"target": "root", "query": "isconnected"},
            ).json()["value"]
            is True
        )
        assert (
            client.post(
                "/api/v1/brokers/broker/commands",
                json={"target": "fed", "command": "stop"},
            ).status_code
            == 200
        )
        assert (
            client.put("/api/v1/brokers/broker/time-barrier", json={"time": 2.5}).status_code == 200
        )
        assert client.delete("/api/v1/brokers/broker/time-barrier").status_code == 200

    assert created["broker"].commands == [("fed", "stop")]
    assert created["broker"].barrier is None


def test_broker_37_startup_controls_are_typed():
    request = BrokerCreateRequest(
        name="broker",
        local_federates=2,
        local_subbrokers=1,
        required_federates=["fed-a", "fed-b"],
    )
    assert request.broker_arguments() == [
        "--local_federates=2",
        "--local_subbrokers=1",
        "--required_federates=fed-a,fed-b",
    ]


def test_broker_page_accepts_37_startup_controls():
    client, created = make_client()
    with client:
        response = client.post(
            "/broker/actions/create",
            data={
                "name": "broker",
                "local_federates": "2",
                "local_subbrokers": "1",
                "required_federates": "fed-a, fed-b",
            },
        )
        assert response.status_code == 200
    assert created["broker"].arguments == [
        "--local_federates=2",
        "--local_subbrokers=1",
        "--required_federates=fed-a,fed-b",
    ]
