import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


class EventSchemaTest(unittest.TestCase):
    def test_synthetic_event_matches_schema(self):
        schema = json.loads((ROOT / "schemas" / "event.schema.json").read_text())
        event = json.loads((ROOT / "examples" / "synthetic_event.json").read_text())

        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(event), key=lambda error: error.path)

        self.assertEqual(errors, [])

    def test_synthetic_event_is_not_real_source_data(self):
        event = json.loads((ROOT / "examples" / "synthetic_event.json").read_text())
        refs = [source["ref"] for source in event["provenance"]["sources"]]

        self.assertTrue(all(ref.startswith("fixture://") for ref in refs))


if __name__ == "__main__":
    unittest.main()
