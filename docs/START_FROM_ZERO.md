# Start From Zero

Eva should be publishable without bundling real operational data. A new user
should still be able to create a working local instance from the public repo.

## Intended Public Flow

1. Create an empty local store from the provided migrations.
2. Load synthetic fixtures to verify schema, validation, and query behavior.
3. Run local tests against the synthetic fixtures.
4. Add private sources in the user's own environment.
5. Keep generated reports, indexes, logs, databases, and map exports out of the
   public repository.

## Public Repo Contents

A useful public repository can include:

- schemas;
- empty migrations;
- importer skeletons;
- query skeletons;
- synthetic fixtures;
- tests that use only synthetic fixtures;
- documentation for privacy boundaries and local setup.

It should not include:

- public data dumps;
- scraped corpora;
- real event records;
- generated reports;
- populated databases;
- map exports;
- logs, telemetry, or caches;
- private deployment details.

## Minimal First Milestone

The first milestone should prove the loop without real data:

```text
synthetic fixture -> validate -> ingest -> query -> context packet -> test
```

After that works, users can connect their own local sources privately.

## Minimal Commands

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests
python scripts/ingest_synthetic.py --db eva.db examples/synthetic_event.json
python scripts/query_events.py --db eva.db --region "Example Region" --since PT48H --risk high
```
