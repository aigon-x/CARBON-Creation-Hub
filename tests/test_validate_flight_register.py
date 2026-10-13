import hashlib
import json
import unittest

from overdrive.forensics.validate_flight_register import git_blob_sha1, validate


def register_event(event_id, event_type, **extra):
    item = {
        "event_id": event_id,
        "event_type": event_type,
        "flight_id": "FLIGHT-1",
        "authorization_id": "AUTH-1",
        "status": "IN_FLIGHT",
        "recorded_at_utc": "2026-10-13T20:51:00Z",
    }
    item.update(extra)
    return item


def fixture(register_events, index_template):
    raw = ("\n".join(json.dumps(e, separators=(",", ":")) for e in register_events) + "\n").encode()
    index_text = index_template.replace("BLOB_SHA", git_blob_sha1(raw))
    return raw, index_text


class FlightRegisterValidationTests(unittest.TestCase):
    def test_valid_launch_checkpoint_and_index_readback(self):
        events = [
            register_event("launch-1", "LAUNCH"),
            register_event("checkpoint-1", "CHECKPOINT", prior_event="launch-1"),
        ]
        raw, index = fixture(
            events,
            "- **Latest continuity checkpoint:** event `checkpoint-1`, blob `BLOB_SHA`",
        )
        self.assertEqual(validate(raw, index), [])

    def test_index_cannot_claim_unregistered_flight(self):
        events = [register_event("launch-1", "LAUNCH")]
        raw, index = fixture(
            events,
            "- **Latest continuity checkpoint:** event `launch-1`, blob `BLOB_SHA`\n"
            "- **Existing flight:** `FORX-UNREGISTERED`, segment 04",
        )
        errors = validate(raw, index)
        self.assertTrue(any("FORX-UNREGISTERED" in error for error in errors))

    def test_stale_index_blob_fails(self):
        events = [register_event("launch-1", "LAUNCH")]
        raw, index = fixture(
            events,
            "- **Latest continuity checkpoint:** event `launch-1`, blob `0000000000000000000000000000000000000000`",
        )
        errors = validate(raw, index)
        self.assertTrue(any("blob pointer is stale" in error for error in errors))

    def test_duplicate_event_id_fails(self):
        events = [
            register_event("launch-1", "LAUNCH"),
            register_event("launch-1", "CHECKPOINT", prior_event="launch-1"),
        ]
        raw, index = fixture(
            events,
            "- **Latest continuity checkpoint:** event `launch-1`, blob `BLOB_SHA`",
        )
        errors = validate(raw, index)
        self.assertTrue(any("duplicate event_id" in error for error in errors))

    def test_flight_without_launch_fails_closed(self):
        events = [register_event("checkpoint-1", "CHECKPOINT")]
        raw, index = fixture(
            events,
            "- **Latest continuity checkpoint:** event `checkpoint-1`, blob `BLOB_SHA`",
        )
        errors = validate(raw, index)
        self.assertTrue(any("exactly one registered LAUNCH" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
