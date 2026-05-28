import sqlite3
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MigrationTest(unittest.TestCase):
    def test_init_migration_creates_events_table(self):
        sql = (ROOT / "db" / "migrations" / "001_init.sql").read_text()

        connection = sqlite3.connect(":memory:")
        try:
            connection.executescript(sql)
            columns = [
                row[1]
                for row in connection.execute("PRAGMA table_info(events)").fetchall()
            ]
        finally:
            connection.close()

        self.assertIn("id", columns)
        self.assertIn("geometry_geojson", columns)
        self.assertIn("provenance_json", columns)


if __name__ == "__main__":
    unittest.main()
