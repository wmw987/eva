import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

from referencing import Registry, Resource
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from ingest_synthetic import ensure_schema, ingest_event  # noqa: E402
from query_events import query_events  # noqa: E402


class QueryEventsTest(unittest.TestCase):
    def test_query_returns_schema_valid_context_packet(self):
        event = json.loads((ROOT / "examples" / "synthetic_event.json").read_text())
        event_schema = json.loads((ROOT / "schemas" / "event.schema.json").read_text())
        packet_schema = json.loads((ROOT / "schemas" / "context-packet.schema.json").read_text())
        registry = Registry().with_resource(
            "event.schema.json",
            Resource.from_contents(event_schema),
        )

        connection = sqlite3.connect(":memory:")
        try:
            ensure_schema(connection)
            ingest_event(connection, event)
            connection.commit()
            temp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
            temp.close()
            backup = Path(temp.name)
            disk_connection = sqlite3.connect(backup)
            try:
                connection.backup(disk_connection)
            finally:
                disk_connection.close()
        finally:
            connection.close()

        try:
            packet = query_events(backup, "Example Region", "high", 10, "PT48H")
        finally:
            backup.unlink(missing_ok=True)

        validator = Draft202012Validator(packet_schema, registry=registry)
        errors = sorted(validator.iter_errors(packet), key=lambda error: error.path)

        self.assertEqual(errors, [])
        self.assertEqual(len(packet["results"]), 1)


if __name__ == "__main__":
    unittest.main()
