"""Tests for the FastAPI replacements for the legacy Flask capabilities."""

from __future__ import annotations

import json
import sqlite3

from fastapi.testclient import TestClient
import pytest

from helics.webserver import create_app
from helics.webserver.models import RunnerConfig
from helics.webserver.observer_service import ObserverDatabaseService
from helics.webserver.profile_service import ProfileService
from helics.webserver.runner_service import RunnerFileError, RunnerService
import helics.webserver.runner_service as runner_module


def make_client(tmp_path):
    return TestClient(
        create_app(
            runner_service=RunnerService(tmp_path),
            observer_service=ObserverDatabaseService(tmp_path),
            profile_service=ProfileService(tmp_path),
        )
    )


def test_runner_file_and_edit_routes(tmp_path):
    config = {"name": "demo", "federates": [{"name": "fed", "exec": "python -V", "directory": "."}]}
    with make_client(tmp_path) as client:
        response = client.post(
            "/api/v1/runner/file",
            files={"file": ("runner.json", json.dumps(config), "application/json")},
        )
        assert response.status_code == 200
        assert response.json()["filename"] == "runner.json"
        assert response.json()["federates"][0]["old_name"] == "fed"

        response = client.put(
            "/api/v1/runner/file/edit",
            json={"name": "fed2", "old_name": "fed", "exec": "python -V", "directory": "."},
        )
        assert response.status_code == 200
        assert response.json()["federates"][0]["name"] == "fed2"

        response = client.post(
            "/api/v1/runner/status",
            json={"name": "fed2", "status": "running"},
        )
        assert response.json() == {"status": "running"}
        assert client.get("/api/v1/runner/status", params={"name": "fed2"}).json() == {
            "status": "running"
        }


def test_runner_configuration_validation_rejects_duplicate_names():
    legacy = RunnerConfig(federates=[{"name": "fed", "exec": "python -V"}])
    assert legacy.name == "HELICS Federation"

    with pytest.raises(ValueError, match="federate names must be unique"):
        RunnerConfig(
            name="demo",
            federates=[
                {"name": "fed", "exec": "python -V"},
                {"name": "fed", "exec": "python -V"},
            ],
        )


def test_runner_rejects_path_components_and_validates_launch(tmp_path):
    service = RunnerService(tmp_path)
    config = {"name": "demo", "federates": [{"name": "fed", "exec": "python -V"}]}

    with pytest.raises(RunnerFileError, match="basename"):
        service.upload(json.dumps(config).encode(), "../escape.json")

    service.upload(json.dumps(config).encode(), "runner.json")
    selected_folder = tmp_path / "selected"
    service.set_folder(str(selected_folder))
    service.upload(json.dumps(config).encode(), "selected.json")
    assert service.runner_path == selected_folder / "selected.json"
    # A selected path must exist before it can be launched.
    missing = tmp_path / "missing.json"
    with pytest.raises(RunnerFileError, match="does not exist"):
        service.set_path(str(missing))


def test_runner_uses_structured_argv_and_owns_auto_broker_process_tree(tmp_path, monkeypatch):
    calls = []

    class FakeProcess:
        pid = 4242

        def __init__(self):
            self.returncode = None

        def poll(self):
            return self.returncode

        def wait(self, timeout=None):
            self.returncode = 0
            return self.returncode

        def terminate(self):
            self.returncode = -15

        def kill(self):
            self.returncode = -9

    process = FakeProcess()

    def fake_popen(command, **kwargs):
        calls.append((command, kwargs))
        return process

    if hasattr(runner_module.os, "killpg"):
        monkeypatch.setattr(runner_module.os, "killpg", lambda *_: None)
    else:
        monkeypatch.setattr(runner_module.subprocess, "run", lambda *args, **kwargs: None)
    service = RunnerService(
        tmp_path,
        server_url="http://example.test:9000/api/v1/",
        popen_factory=fake_popen,
    )
    config = {
        "name": "demo",
        "broker": True,
        "federates": [{"name": "fed", "exec": "python -V", "directory": "."}],
    }
    service.upload(json.dumps(config).encode(), "runner.json")

    assert service.run() is True
    command, kwargs = calls[0]
    assert isinstance(command, list)
    assert command[-5:] == [
        "--path",
        str(tmp_path / "runner.json"),
        "--connect-server",
        "--server-url",
        "http://example.test:9000/api/v1",
    ]
    assert kwargs["env"]["HELICS_CLI_SERVER_API"] == "http://example.test:9000/api/v1"
    assert kwargs["shell"] is False
    if runner_module.os.name == "nt":
        assert "creationflags" in kwargs
    else:
        assert kwargs["start_new_session"] is True
    assert service.process_info().broker_managed is True
    assert service.process_info().owns_process_tree is True
    assert service.get_status("fed").status == "pending"
    assert service.stop() is False
    assert service.status() is False


def test_runner_run_route_returns_owned_process_metadata(tmp_path, monkeypatch):
    class FakeProcess:
        pid = 5252
        returncode = None

        def poll(self):
            return self.returncode

        def wait(self, timeout=None):
            self.returncode = 0
            return self.returncode

        def terminate(self):
            self.returncode = -15

        def kill(self):
            self.returncode = -9

    process = FakeProcess()
    if runner_module.os.name == "nt":
        monkeypatch.setattr(runner_module.subprocess, "run", lambda *args, **kwargs: None)
    else:
        monkeypatch.setattr(runner_module.os, "killpg", lambda *_: None)

    service = RunnerService(tmp_path, popen_factory=lambda *args, **kwargs: process)
    service.upload(
        json.dumps(
            {
                "name": "demo",
                "broker": True,
                "federates": [{"name": "fed", "exec": "python -V"}],
            }
        ).encode(),
        "runner.json",
    )
    with TestClient(create_app(runner_service=service)) as client:
        response = client.post("/api/v1/runner/run")
        assert response.status_code == 200
        assert response.json()["process"]["pid"] == 5252
        assert response.json()["process"]["broker_managed"] is True
        assert client.get("/api/v1/runner/run").json()["process"]["owns_process_tree"] is True
        assert client.delete("/api/v1/runner/broker").json() == {"status": False}


def test_jinja_broker_page(tmp_path):
    with make_client(tmp_path) as client:
        response = client.get("/broker")
        assert response.status_code == 200
        assert "HELICS Brokers" in response.text
        assert "No service-managed brokers" in response.text


def test_observer_database_routes(tmp_path):
    source = tmp_path / "source.sqlite"
    connection = sqlite3.connect(source)
    connection.execute("CREATE TABLE systeminfo (id INTEGER, data TEXT)")
    connection.execute("INSERT INTO systeminfo VALUES (1, ?)", ('{"version": {"string": "3.7"}}',))
    connection.execute("CREATE TABLE cores (id INTEGER, name TEXT, address TEXT)")
    connection.execute("INSERT INTO cores VALUES (1, 'core', 'inproc://core')")
    connection.execute("CREATE TABLE federates (id INTEGER, name TEXT, parent INTEGER)")
    connection.execute("INSERT INTO federates VALUES (1, 'fed', 1)")
    connection.commit()
    connection.close()

    with make_client(tmp_path) as client:
        response = client.post(
            "/api/v1/observer/database",
            files={"file": ("observer.sqlite", source.read_bytes(), "application/octet-stream")},
        )
        assert response.status_code == 200
        assert client.get("/api/v1/observer/systeminfo").json()["version"]["string"] == "3.7"
        assert client.get("/api/v1/observer/cores").json() == [
            {"id": 1, "name": "core", "address": "inproc://core"}
        ]
        assert client.get("/api/v1/observer/federates").json()[0]["name"] == "fed"


def test_profile_routes(tmp_path):
    profile = (
        "<PROFILING>fed[1](running)HELICS CODE EXIT<2000000000>[t=2]</PROFILING>\n"
        "<PROFILING>fed[1](running)HELICS CODE ENTRY<1000000000>[t=1]</PROFILING>\n"
    )
    with make_client(tmp_path) as client:
        assert client.get("/api/v1/profile").json() == {}
        response = client.post(
            "/api/v1/profile",
            files={"file": ("profile.txt", profile, "text/plain")},
        )
        assert response.status_code == 200
        parsed = client.get("/api/v1/profile").json()
        assert list(parsed) == ["fed"]
        assert len(parsed["fed"]) == 1
        assert client.delete("/api/v1/profile").json()["status"] == "success"
