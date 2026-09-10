"""Runner configuration and process management for the FastAPI service.

The runner service is intentionally small, but it owns the complete process
tree started for a run.  This is important when a runner file asks HELICS to
create an automatic broker: stopping the run must also stop that broker and
any federate children.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
from threading import RLock
from typing import Callable, Dict, Mapping, Optional
from urllib.parse import urlparse

from pydantic import ValidationError

from .models import (
    RunnerConfig,
    RunnerFederateEdit,
    RunnerFileResponse,
    RunnerProcessInfo,
    RunnerStatus,
    RunnerStatusResponse,
)


class RunnerFileError(ValueError):
    """Raised for an invalid or unavailable runner configuration."""


PopenFactory = Callable[..., subprocess.Popen]


class RunnerService:
    """Own a runner file and the process tree launched from it.

    ``server_url`` is the FastAPI API base (normally ending in ``/api/v1``)
    used by ``helics run --connect-server``.  It can be supplied explicitly or
    through ``HELICS_CLI_SERVER_API``.  The subprocess is started without a
    shell in a new process group/session, so :meth:`stop` and :meth:`shutdown`
    can clean up all descendants, including an auto-created broker.
    """

    DEFAULT_SERVER_URL = "http://127.0.0.1:8000/api/v1"

    def __init__(
        self,
        root_dir: Optional[Path | str] = None,
        server_url: Optional[str] = None,
        popen_factory: Optional[PopenFactory] = None,
    ) -> None:
        self._root = Path(root_dir or (Path.cwd() / "__helics-server")).expanduser().resolve()
        self._root.mkdir(parents=True, exist_ok=True)
        self._runner_filename = "runner.json"
        self._runner_path = self._root / self._runner_filename
        self._process: Optional[subprocess.Popen] = None
        self._run_started_at: Optional[datetime] = None
        self._run_broker_managed = False
        self._statuses: Dict[str, RunnerStatus] = {}
        self._lock = RLock()
        self._popen = popen_factory or subprocess.Popen
        self._server_url = self._normalise_server_url(
            server_url or os.environ.get("HELICS_CLI_SERVER_API") or self.DEFAULT_SERVER_URL
        )

    @staticmethod
    def _normalise_server_url(value: str) -> str:
        value = value.strip().rstrip("/")
        parsed = urlparse(value)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("server_url must be an absolute http:// or https:// URL")
        return value

    @property
    def runner_path(self) -> Path:
        return self._runner_path

    @property
    def runner_folder(self) -> Path:
        return self._runner_path.parent

    @property
    def server_url(self) -> str:
        return self._server_url

    def _resolve_path(self, value: str | Path, *, kind: str, must_exist: bool = False) -> Path:
        """Resolve a user-supplied path and apply common safety checks."""

        raw_value = os.fspath(value)
        if not raw_value.strip() or "\x00" in raw_value:
            raise RunnerFileError(f"{kind} path is empty or contains a NUL byte")
        try:
            target = Path(value).expanduser().resolve()
        except (OSError, RuntimeError, ValueError) as error:
            raise RunnerFileError(f"invalid {kind} path: {error}") from error
        if must_exist and not target.exists():
            raise RunnerFileError(f"{kind} path does not exist: {target}")
        return target

    def _resolve_federate_directory(self, directory: str) -> Path:
        # This mirrors helics.cli: relative directories are relative to the
        # runner file, while absolute paths are respected.  Federates may
        # intentionally live outside the runner folder, so containment is not
        # imposed here; existence and directory type are always checked.
        candidate = Path(directory).expanduser()
        target = self._resolve_path(
            candidate if candidate.is_absolute() else self.runner_folder / candidate,
            kind="federate working directory",
            must_exist=True,
        )
        if not target.is_dir():
            raise RunnerFileError(f"federate working directory is not a directory: {target}")
        return target

    def _resolve_logging_directory(self, logging_path: Optional[str]) -> Path:
        candidate = self._config_path(logging_path)
        target = self._resolve_path(
            candidate,
            kind="logging",
        )
        try:
            target.mkdir(parents=True, exist_ok=True)
        except OSError as error:
            raise RunnerFileError(
                f"unable to create logging directory {target}: {error}"
            ) from error
        if not target.is_dir():
            raise RunnerFileError(f"logging path is not a directory: {target}")
        return target

    def _config_path(self, value: Optional[str]) -> Path:
        """Resolve a path from runner JSON relative to the runner folder."""

        candidate = Path(value or ".").expanduser()
        return candidate if candidate.is_absolute() else self.runner_folder / candidate

    @staticmethod
    def _safe_upload_filename(filename: str) -> str:
        # Multipart clients should send a basename.  Reject path components
        # rather than silently allowing a client to select an arbitrary file.
        if not filename or "\x00" in filename or "/" in filename or "\\" in filename:
            raise RunnerFileError("uploaded runner filename must be a basename")
        name = Path(filename).name
        if name in {"", ".", ".."} or name != filename or Path(name).suffix.lower() != ".json":
            raise RunnerFileError("uploaded runner filename must end with .json")
        return name

    def _parse_config(self, data: Mapping[str, object]) -> RunnerConfig:
        try:
            return RunnerConfig.model_validate(data)
        except ValidationError as error:
            message = "; ".join(
                f"{'.'.join(str(part) for part in detail['loc'])}: {detail['msg']}"
                for detail in error.errors()
            )
            raise RunnerFileError(f"invalid runner configuration: {message}") from error

    def _read_raw(self) -> Optional[dict]:
        if not self._runner_path.exists():
            return None
        if not self._runner_path.is_file():
            raise RunnerFileError(f"runner path is not a file: {self._runner_path}")
        try:
            with self._runner_path.open(encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError) as error:
            raise RunnerFileError(f"Unable to read runner file: {error}") from error
        if not isinstance(data, dict):
            raise RunnerFileError("runner file must be a JSON object")
        self._parse_config(data)
        return data

    def _validated_config(self) -> RunnerConfig:
        data = self._read_raw()
        if data is None:
            raise RunnerFileError("runner file has not been selected")
        return self._parse_config(data)

    def file(self) -> Optional[RunnerFileResponse]:
        with self._lock:
            data = self._read_raw()
            if data is None:
                return None
            config = self._parse_config(data)
            logging_directory = self._resolve_path(
                self._config_path(config.logging_path), kind="logging"
            )
            federates = []
            for item in data.get("federates", []):
                # _read_raw already validated the launch fields.  Preserve
                # unknown fields (for forward-compatible runner extensions)
                # while adding server-managed status metadata.
                item = dict(item)
                item.setdefault("directory", ".")
                item.setdefault("host", "localhost")
                item["old_name"] = item.get("name")
                directory = Path(str(item["directory"])).expanduser()
                if not directory.is_absolute():
                    directory = self.runner_folder / directory
                item["directory"] = str(directory.resolve())
                item["log_available"] = (logging_directory / f"{item['name']}.log").exists()
                item["status"] = self._statuses.get(item["name"])
                federates.append(item)
            # The UI historically showed an auto-created broker. Keep that
            # useful information in the response without mutating runner.json.
            if data.get("broker", False) is True:
                federates.append(
                    {
                        "directory": str(self.runner_folder),
                        "exec": f"helics_broker -f{len(federates)}",
                        "host": "localhost",
                        "name": "broker",
                        "old_name": "broker",
                        "log_available": (logging_directory / "broker.log").exists(),
                        "status": self._statuses.get("broker"),
                    }
                )
            data["federates"] = federates
            data.update(
                folder=str(self.runner_folder),
                path=str(self.runner_path),
                filename=self._runner_filename,
            )
            return RunnerFileResponse.model_validate(data)

    def upload(self, content: bytes, filename: Optional[str] = None) -> RunnerFileResponse:
        with self._lock:
            if not content:
                raise RunnerFileError("runner file is empty")
            try:
                data = json.loads(content.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as error:
                raise RunnerFileError(f"runner file is not valid JSON: {error}") from error
            if not isinstance(data, dict):
                raise RunnerFileError("runner file must be a JSON object")
            self._parse_config(data)
            if filename:
                self._runner_filename = self._safe_upload_filename(filename)
                # Preserve an explicitly selected folder; the initial folder
                # is ``root_dir`` but users may switch folders before upload.
                self._runner_path = self.runner_folder / self._runner_filename
            self.runner_folder.mkdir(parents=True, exist_ok=True)
            try:
                with self._runner_path.open("wb") as handle:
                    handle.write(content)
            except OSError as error:
                raise RunnerFileError(f"unable to save runner file: {error}") from error
            return self.file()  # type: ignore[return-value]

    def set_name(self, name: str) -> RunnerFileResponse:
        with self._lock:
            safe_name = self._safe_upload_filename(
                name if name.lower().endswith(".json") else f"{name}.json"
            )
            self._runner_filename = safe_name
            self._runner_path = self.runner_folder / safe_name
            return self.file()  # type: ignore[return-value]

    def set_folder(self, folder: str) -> RunnerFileResponse:
        with self._lock:
            target = self._resolve_path(folder, kind="runner folder")
            try:
                target.mkdir(parents=True, exist_ok=True)
            except OSError as error:
                raise RunnerFileError(
                    f"unable to create runner folder {target}: {error}"
                ) from error
            if not target.is_dir():
                raise RunnerFileError(f"runner folder is not a directory: {target}")
            self._runner_path = target / self._runner_filename
            return self.file()  # type: ignore[return-value]

    def set_path(self, path: str) -> RunnerFileResponse:
        with self._lock:
            target = self._resolve_path(path, kind="runner", must_exist=True)
            if target.suffix.lower() != ".json" or not target.is_file():
                raise RunnerFileError("runner path must point to an existing .json file")
            self._runner_path = target
            self._runner_filename = target.name
            return self.file()  # type: ignore[return-value]

    def _write(self, data: dict) -> None:
        self._runner_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self._runner_path.with_suffix(self._runner_path.suffix + ".tmp")
        try:
            with temporary.open("w", encoding="utf-8") as handle:
                json.dump(data, handle, indent=2)
                handle.write("\n")
            temporary.replace(self._runner_path)
        except OSError as error:
            raise RunnerFileError(f"unable to write runner file: {error}") from error

    def edit(self, item: RunnerFederateEdit, mode: str) -> RunnerFileResponse:
        with self._lock:
            data = self._read_raw()
            if data is None:
                raise RunnerFileError("runner file has not been selected")
            federates = data.setdefault("federates", [])
            old_name = item.old_name or item.name
            if mode == "add":
                if any(f.get("name") == item.name for f in federates):
                    raise RunnerFileError(f"name already exists: {item.name}")
                federates.append(
                    {
                        "directory": item.directory,
                        "exec": item.exec,
                        "host": item.host,
                        "name": item.name,
                    }
                )
            elif mode == "delete":
                for index, federate in enumerate(federates):
                    if federate.get("name") == old_name:
                        federates.pop(index)
                        break
                else:
                    raise RunnerFileError(f"unknown federate: {old_name}")
            elif mode == "update":
                for federate in federates:
                    if federate.get("name") == old_name:
                        federate.update(
                            name=item.name,
                            exec=item.exec,
                            directory=item.directory,
                            host=item.host,
                        )
                        break
                else:
                    raise RunnerFileError(f"unknown federate: {old_name}")
            else:
                raise RunnerFileError(f"unsupported edit mode: {mode}")
            self._parse_config(data)
            self._write(data)
            return self.file()  # type: ignore[return-value]

    def log(self, name: str) -> str:
        with self._lock:
            if not name or Path(name).name != name or name in {".", ".."}:
                raise RunnerFileError("invalid federate log name")
            config = self._validated_config()
            names = {federate.name for federate in config.federates}
            if config.broker:
                names.add("broker")
            if name not in names:
                raise RunnerFileError(f"unknown federate: {name}")
            path = self._config_path(config.logging_path) / f"{name}.log"
            if not path.exists() or not path.is_file():
                raise RunnerFileError(f"log not found for federate: {name}")
            try:
                return path.read_text(encoding="utf-8", errors="replace")
            except OSError as error:
                raise RunnerFileError(f"unable to read log for federate {name}: {error}") from error

    def build_command(self) -> list[str]:
        """Build the exact argv passed to HELICS, without shell expansion."""

        executable = shutil.which("helics")
        command = [executable or sys.executable]
        if executable is None:
            command += ["-m", "helics.cli"]
        command += [
            "run",
            "--path",
            str(self._runner_path),
            "--connect-server",
            "--server-url",
            self._server_url,
        ]
        return command

    def _validate_launch(self) -> RunnerConfig:
        config = self._validated_config()
        self._resolve_path(self._runner_path, kind="runner", must_exist=True)
        for federate in config.federates:
            self._resolve_federate_directory(federate.directory)
        self._resolve_logging_directory(config.logging_path)
        return config

    def run(self) -> bool:
        with self._lock:
            if self._process is not None and self._process.poll() is None:
                return True
            if self._process is not None:
                # The parent may have exited while a child is still alive;
                # clean the previous owned group before replacing its handle.
                self._terminate_process_tree(self._process)
                self._process = None
            config = self._validate_launch()
            command = list(self.build_command())
            environment = os.environ.copy()
            # Explicit service configuration wins over a stale inherited value.
            environment["HELICS_CLI_SERVER_API"] = self._server_url
            creation: dict = {}
            if os.name == "nt":
                creation["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
            else:
                creation["start_new_session"] = True
            try:
                self._process = self._popen(
                    command,
                    cwd=str(self.runner_folder),
                    env=environment,
                    shell=False,
                    **creation,
                )
            except OSError as error:
                self._process = None
                raise RunnerFileError(f"unable to start HELICS runner: {error}") from error
            self._run_started_at = datetime.now(timezone.utc)
            self._run_broker_managed = config.broker
            self._statuses = {federate.name: "pending" for federate in config.federates}
            if config.broker:
                self._statuses["broker"] = "pending"
            return True

    def process_info(self) -> Optional[RunnerProcessInfo]:
        with self._lock:
            if self._process is None:
                return None
            return RunnerProcessInfo(
                pid=int(self._process.pid),
                runner_path=str(self._runner_path),
                server_url=self._server_url,
                started_at=self._run_started_at or datetime.now(timezone.utc),
                owns_process_tree=True,
                broker_managed=self._run_broker_managed,
            )

    def status(self) -> bool:
        with self._lock:
            return self._process is not None and self._process.poll() is None

    @staticmethod
    def _terminate_process_tree(process: subprocess.Popen) -> None:
        # A runner can have exited while a child is still alive.  Signal the
        # group/tree even in that case; on POSIX the runner PID is also the
        # session/process-group ID because it was started with
        # ``start_new_session``.
        active = process.poll() is None
        pid = getattr(process, "pid", None)
        if os.name == "nt":
            if pid:
                # taskkill /T reaches children created by helics run, including
                # an auto-broker.  argv is structured and shell=False by default.
                subprocess.run(
                    ["taskkill", "/PID", str(pid), "/T"],
                    check=False,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                process.terminate()
        else:
            try:
                if pid:
                    os.killpg(os.getpgid(pid), signal.SIGTERM)
                else:
                    process.terminate()
            except (OSError, ProcessLookupError):
                process.terminate()
        if active:
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass

        # The parent can exit after SIGTERM while a federate or broker child
        # remains alive.  Perform a final tree/group kill after the grace
        # period so shutdown cannot leak run-owned processes.
        if os.name == "nt" and pid:
            subprocess.run(
                ["taskkill", "/PID", str(pid), "/T", "/F"],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        elif pid:
            try:
                os.killpg(os.getpgid(pid), signal.SIGKILL)
            except (OSError, ProcessLookupError):
                if active and process.poll() is None:
                    process.kill()
        elif active and process.poll() is None:
            process.kill()
        if active and process.poll() is None:
            process.wait(timeout=5)

    def stop(self) -> bool:
        with self._lock:
            if self._process is None:
                self._statuses.clear()
                return False
            process = self._process
            try:
                self._terminate_process_tree(process)
            finally:
                self._process = None
                self._run_started_at = None
                self._run_broker_managed = False
                self._statuses.clear()
            # The response represents the state after stopping: not running.
            return False

    def stop_broker(self) -> bool:
        """Stop a run only when it owns an automatic broker.

        A broker launched by ``helics run`` shares the run's process group.
        There is deliberately no global ``killall helics_broker`` operation;
        this method therefore cleans up the complete owned run instead of
        risking unrelated brokers.
        """

        with self._lock:
            if not self._run_broker_managed:
                return False
            return self.stop()

    def set_status(self, name: str, status: RunnerStatus) -> RunnerStatusResponse:
        with self._lock:
            self._statuses[name] = status
            return RunnerStatusResponse(status=status)

    def get_status(self, name: str) -> RunnerStatusResponse:
        with self._lock:
            return RunnerStatusResponse(status=self._statuses.get(name))

    def shutdown(self) -> None:
        self.stop()
