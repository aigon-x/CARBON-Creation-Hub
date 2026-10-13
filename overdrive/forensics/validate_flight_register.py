#!/usr/bin/env python3
"""Fail-closed integrity checks for the existing append-only flight register.

This is a read-only CI/preflight guard. It never appends, rewrites, or repairs
register events and does not start or schedule any runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


def git_blob_sha1(raw: bytes) -> str:
    """Return the Git blob object SHA-1 for exact file bytes."""
    header = b"blob " + str(len(raw)).encode("ascii") + b"\0"
    return hashlib.sha1(header + raw).hexdigest()


def validate(register_bytes: bytes, index_text: str) -> list[str]:
    errors: list[str] = []
    events: list[dict[str, Any]] = []
    line_by_id: dict[str, int] = {}
    events_by_flight: dict[str, list[tuple[int, dict[str, Any]]]] = defaultdict(list)

    for line_no, raw_line in enumerate(register_bytes.splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            event = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"register line {line_no}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(event, dict):
            errors.append(f"register line {line_no}: event must be a JSON object")
            continue

        event_id = event.get("event_id")
        flight_id = event.get("flight_id")
        event_type = event.get("event_type")
        status = event.get("status")
        missing = [
            key for key, value in (
                ("event_id", event_id),
                ("flight_id", flight_id),
                ("event_type", event_type),
                ("status", status),
            )
            if not isinstance(value, str) or not value.strip()
        ]
        if missing:
            errors.append(
                f"register line {line_no}: missing/invalid required field(s): "
                + ", ".join(missing)
            )
            continue
        if event_id in line_by_id:
            errors.append(
                f"register line {line_no}: duplicate event_id {event_id!r}; "
                f"first seen on line {line_by_id[event_id]}"
            )
        else:
            line_by_id[event_id] = line_no
        events.append(event)
        events_by_flight[flight_id].append((line_no, event))

    if not events:
        errors.append("register contains no valid events")

    launch_by_flight: dict[str, tuple[int, dict[str, Any]]] = {}
    for flight_id, flight_events in events_by_flight.items():
        launches = [
            (line_no, event)
            for line_no, event in flight_events
            if event.get("event_type") == "LAUNCH"
        ]
        if len(launches) != 1:
            errors.append(
                f"flight {flight_id!r}: expected exactly one registered LAUNCH, "
                f"found {len(launches)}"
            )
            continue
        launch_by_flight[flight_id] = launches[0]
        launch_line, launch = launches[0]
        launch_auth = launch.get("authorization_id")

        for line_no, event in flight_events:
            event_id = event.get("event_id")
            if line_no < launch_line:
                errors.append(
                    f"flight {flight_id!r}: event {event_id!r} precedes its LAUNCH"
                )
            if line_no == launch_line:
                continue

            event_auth = event.get("authorization_id")
            # Historical entries are immutable; tolerate a missing historical
            # authorization field, but never tolerate an explicit mismatch.
            if event_auth and launch_auth and event_auth != launch_auth:
                errors.append(
                    f"flight {flight_id!r}: event {event_id!r} authorization "
                    f"does not match its LAUNCH"
                )

            prior = event.get("prior_event")
            if prior:
                prior_line = line_by_id.get(prior)
                if prior_line is None:
                    errors.append(
                        f"register line {line_no}: prior_event {prior!r} is absent"
                    )
                elif prior_line >= line_no:
                    errors.append(
                        f"register line {line_no}: prior_event {prior!r} is not earlier"
                    )
                else:
                    prior_event = next(
                        (item for item in events if item.get("event_id") == prior),
                        None,
                    )
                    if prior_event and prior_event.get("flight_id") != flight_id:
                        errors.append(
                            f"register line {line_no}: prior_event {prior!r} belongs "
                            f"to a different flight"
                        )

    # The Index's top continuity pointer must point to the exact current register
    # blob and to the final event in the register, not a stale/phantom checkpoint.
    pointer = re.search(
        r"Latest continuity checkpoint:.*?event \x60([^\x60]+)\x60, "
        r"blob \x60([0-9a-f]{40})\x60",
        index_text,
    )
    if not pointer:
        errors.append("INTAKE_INDEX.md: latest continuity checkpoint pointer not found")
    else:
        pointer_event, pointer_blob = pointer.groups()
        if pointer_event not in line_by_id:
            errors.append(
                f"INTAKE_INDEX.md: latest checkpoint event {pointer_event!r} "
                "is absent from the register"
            )
        elif events and events[-1].get("event_id") != pointer_event:
            errors.append(
                "INTAKE_INDEX.md: latest checkpoint is not the final register event"
            )
        actual_blob = git_blob_sha1(register_bytes)
        if pointer_blob != actual_blob:
            errors.append(
                "INTAKE_INDEX.md: register blob pointer is stale "
                f"(index={pointer_blob}, actual={actual_blob})"
            )

    # Text may call a flight "existing" only if its launch is actually registered.
    for line_no, line in enumerate(index_text.splitlines(), start=1):
        match = re.search(r"\*\*Existing flight:\*\*\s+\x60([^\x60]+)\x60", line)
        if not match:
            continue
        flight_id = match.group(1)
        if flight_id not in launch_by_flight:
            errors.append(
                f"INTAKE_INDEX.md line {line_no}: flight {flight_id!r} is labelled "
                "Existing flight but has no registered LAUNCH"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", required=True, type=Path)
    parser.add_argument("--index", required=True, type=Path)
    args = parser.parse_args()

    try:
        register_bytes = args.register.read_bytes()
        index_text = args.index.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"FAIL: unable to read validation inputs: {exc}")
        return 2

    errors = validate(register_bytes, index_text)
    if errors:
        print("FAIL: dynamic flight register integrity")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "PASS: JSONL structure, unique event IDs, one launch per registered flight, "
        "authorization consistency where recorded, prior-event ordering where linked, "
        "and current Index checkpoint/blob readback."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
