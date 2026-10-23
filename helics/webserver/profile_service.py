"""HELICS profile artifact storage and parsing."""

from __future__ import annotations

import re
from pathlib import Path
from threading import RLock
from typing import Any, Optional


class ProfileError(ValueError):
    """Raised for unavailable or malformed profile data."""


class ProfileService:
    """Store and parse the profile artifact used by the web UI.

    The service keeps one UTF-8 ``profile.txt`` file beneath ``root_dir``.
    Uploading replaces the current artifact, parsing returns complete entry/
    exit intervals, and :meth:`clear` removes the artifact without affecting
    broker or runner state.
    """

    PATTERN = re.compile(
        r"(?P<name>\w+)\[(\d+)\]\((?P<state>\w+)\)"
        r"(?P<message>[\w\s]+)<(?P<realtime>\d+(?:\|\d+)?)>"
        r"\[t=(?P<simtime>-?\d*\.?\d+)\]"
    )

    def __init__(self, root_dir: Optional[Path | str] = None) -> None:
        root = Path(root_dir or (Path.cwd() / "__helics-server")).expanduser().resolve()
        root.mkdir(parents=True, exist_ok=True)
        self._path = root / "profile.txt"
        self._lock = RLock()

    @property
    def path(self) -> Path:
        """Return the path of the currently managed profile artifact."""
        return self._path

    def upload(self, content: bytes) -> None:
        """Validate and replace the stored profile artifact."""
        if not content:
            raise ProfileError("profile upload is empty")
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ProfileError("profile must be UTF-8 text") from error
        with self._lock:
            self._path.write_bytes(content)

    def parse(self) -> dict[str, list[dict[str, Any]]]:
        """Parse the stored profile into complete per-federate intervals."""
        with self._lock:
            if not self._path.exists():
                return {}
            text = self._path.read_text(encoding="utf-8", errors="replace")
        entries: dict[str, list[dict[str, Any]]] = {}
        for line_number, line in enumerate(
            text.replace("<PROFILING>", "").replace("</PROFILING>", "").splitlines(), 1
        ):
            match = self.PATTERN.fullmatch(line.strip())
            if match is None:
                if line.strip():
                    raise ProfileError(f"unrecognized profile line {line_number}")
                continue
            name = match.group("name")
            state = match.group("state")
            if state == "created":
                continue
            realtime = match.group("realtime")
            if "|" in realtime:
                realtime, marker = realtime.split("|", 1)
                # Marker values are useful to the old UI only for calibration;
                # retain the primary realtime value in the public response.
                _ = marker
            event = {
                "name": name,
                "state": state,
                "message": match.group("message").strip(),
                "simtime": float(match.group("simtime")),
                "realtime": float(realtime) / 1e9,
            }
            entries.setdefault(name, []).append(event)

        profiles: dict[str, list[dict[str, Any]]] = {name: [] for name in entries}
        # The native profiler writes ENTRY/EXIT pairs in reverse order.  Keep
        # the historical inversion while producing only complete intervals.
        for name, events in entries.items():
            pending: Optional[dict[str, Any]] = None
            for event in events:
                if "EXIT" in event["message"]:
                    pending = {
                        "name": name,
                        "s_enter": event["simtime"],
                        "r_enter": event["realtime"],
                    }
                elif "ENTRY" in event["message"] and pending is not None:
                    pending["s_end"] = event["simtime"]
                    pending["r_end"] = event["realtime"]
                    profiles[name].append(pending)
                    pending = None
        return profiles

    def clear(self) -> None:
        """Remove the stored profile artifact if one exists."""
        with self._lock:
            self._path.unlink(missing_ok=True)
