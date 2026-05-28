import json
import unittest
from pathlib import Path

from referencing import Registry, Resource
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


class ContextPacketSchemaTest(unittest.TestCase):
    def test_synthetic_context_packet_matches_schema(self):
        event_schema = json.loads((ROOT / "schemas" / "event.schema.json").read_text())
        packet_schema = json.loads((ROOT / "schemas" / "context-packet.schema.json").read_text())
        packet = json.loads((ROOT / "examples" / "synthetic_context_packet.json").read_text())
        registry = Registry().with_resource(
            "event.schema.json",
            Resource.from_contents(event_schema),
        )

        validator = Draft202012Validator(packet_schema, registry=registry)
        errors = sorted(validator.iter_errors(packet), key=lambda error: error.path)

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
