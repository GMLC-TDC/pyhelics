"""Read and upload HELICS observer SQLite databases without Flask/SQLAlchemy."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from threading import RLock
from typing import Any, Optional


class ObserverDatabaseError(ValueError):
    """Raised when an observer database is unavailable or invalid."""


class ObserverDatabaseService:
    """Manage the SQLite artifact produced by ``helics observer``.

    The observer writer may continue to use SQLAlchemy for now; the web API
    only needs read access and therefore uses the standard-library sqlite3
    driver, avoiding another web-service dependency.
    """

    TABLES = {
        "cores": "cores",
        "federates": "federates",
        "subscriptions": "subscriptions",
        "inputs": "inputs",
        "publications": "publications",
    }

    def __init__(self, root_dir: Optional[Path | str] = None) -> None:
        self._root = Path(root_dir or (Path.cwd() / "__helics-server")).expanduser().resolve()
        self._path = self._root / "helics-cli.sqlite.db"
        self._lock = RLock()

    @property
    def path(self) -> Path:
        return self._path

    def info(self) -> dict[str, Any]:
        return {"path": str(self._path), "exists": self._path.exists()}

    def upload(self, content: bytes) -> dict[str, Any]:
        if not content:
            raise ObserverDatabaseError("database upload is empty")
        self._root.mkdir(parents=True, exist_ok=True)
        temporary = self._path.with_suffix(".tmp")
        with temporary.open("wb") as handle:
            handle.write(content)
        try:
            connection = sqlite3.connect(f"file:{temporary}?mode=ro", uri=True)
            connection.execute("PRAGMA schema_version").fetchone()
            connection.close()
        except sqlite3.DatabaseError as error:
            temporary.unlink(missing_ok=True)
            raise ObserverDatabaseError(f"invalid SQLite database: {error}") from error
        temporary.replace(self._path)
        return self.info()

    def _connect(self) -> sqlite3.Connection:
        if not self._path.exists():
            raise ObserverDatabaseError("no observer database has been uploaded")
        connection = sqlite3.connect(self._path)
        connection.row_factory = sqlite3.Row
        return connection

    @staticmethod
    def _decode(value: Any) -> Any:
        if isinstance(value, str) and value[:1] in "[{":
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                pass
        return value

    def _rows(self, table: str) -> list[dict[str, Any]]:
        with self._lock:
            connection = self._connect()
            try:
                try:
                    rows = connection.execute(f'SELECT * FROM "{table}"').fetchall()
                except sqlite3.OperationalError as error:
                    if "no such table" in str(error).lower():
                        return []
                    raise
                values = [{key: self._decode(row[key]) for key in row.keys()} for row in rows]
                if table == "cores":
                    values = [
                        row
                        for row in values
                        if not str(row.get("name", "")).startswith("__observer__")
                    ]
                if table == "federates":
                    values = [row for row in values if row.get("name") != "__observer__"]
                return values
            finally:
                connection.close()

    def system_info(self) -> Any:
        rows = self._rows("systeminfo")
        return rows[0].get("data", {}) if rows else {}

    def cores(self) -> list[dict[str, Any]]:
        return self._rows("cores")

    def federates(self) -> list[dict[str, Any]]:
        return self._rows("federates")

    def graphs(self) -> dict[str, Any]:
        return {
            "federate": (self._rows("federategraph") or [{}])[0].get("data", {}),
            "data": (self._rows("datagraph") or [{}])[0].get("data", {}),
        }

    def subscriptions(self) -> list[dict[str, Any]]:
        return self._rows("subscriptions")

    def inputs(self) -> list[dict[str, Any]]:
        return self._rows("inputs")

    def publications(self) -> list[dict[str, Any]]:
        return self._rows("publications")

    def data(self) -> list[dict[str, Any]]:
        return self._rows("datatable")
