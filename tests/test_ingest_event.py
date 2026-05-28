import json
import sqlite3
import unittest
from pathlib import Path

import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from ingest_synthetic import ensure_schema, ingest_event  # noqa: E402


class IngestEventTest(unittest.TestCase):
    def test_synthetic_event_maps_to_sqlite(self):
        event = json.loads((ROOT / "examples" / "synthetic_event.json").read_text())

        connection = sqlite3.connect(":memory:")
        connection.row_factory = sqlite3.Row
        try:
            ensure_schema(connection)
            ingest_event(connection, event)
            row = connection.execute(
                "SELECT * FROM events WHERE id = ?",
                (event["id"],),
            ).fetchone()
        finally:
            connection.close()

        self.assertIsNotNone(row)
        self.assertEqual(row["risk"], "high")
        self.assertEqual(row["confidence"], "signal")
        self.assertEqual(json.loads(row["geometry_geojson"]), event["geo"]["geometry"])
        self.assertEqual(json.loads(row["provenance_json"]), event["provenance"])
        self.assertEqual(json.loads(row["relations_json"]), event["relations"])


if __name__ == "__main__":
    unittest.main()
