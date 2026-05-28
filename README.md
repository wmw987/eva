# Eva

Local-first geo-temporal context layer for LLM agents.

Eva is an early architecture and prototype skeleton for structured
geo-temporal agent memory. It models events by time, place, source,
confidence, risk, and relationships, then exposes bounded context packets for
agent reasoning.

Technical architecture: **Geo-Temporal Context Core**.

## Why

Vector memory is useful, but it often loses the operational shape of real-world
context: when something happened, where it happened, which source supports it,
how confident the system is, and what changed over time.

Eva treats the LLM as an interpreter over structured context, not as the
database of record.

## Status

Eva is currently an early public specification and prototype skeleton.

## What Works Today

- Create an empty SQLite event table.
- Validate synthetic event fixtures against JSON Schema.
- Validate synthetic context packets.
- Ingest a synthetic event into SQLite.
- Query synthetic events back as bounded context packets.
- Run tests without any real operational data.

## What Is Not Implemented Yet

- No production collector.
- No real data ingestion in the public repository.
- No map or timeline UI.
- No MCP server.
- No temporal supersession engine.
- No production-ready geospatial index.

## Quick Start

Create a virtual environment and install development dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

On Windows PowerShell:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Run the tests:

```bash
python -m unittest discover -s tests
```

Create an empty SQLite store and ingest the synthetic event:

```bash
python scripts/ingest_synthetic.py --db eva.db examples/synthetic_event.json
```

Query it back as a context packet:

```bash
python scripts/query_events.py --db eva.db --region "Example Region" --since PT48H --risk high
```

## Architecture

```mermaid
flowchart LR
  A[Sources] --> B[Collectors and Parsers]
  B --> C[Normalized Event Records]
  C --> D[Geo-Temporal Event Store]
  D --> E[Full-text / Vector / Graph / Spatial Indexes]
  E --> F[Map and Timeline Interfaces]
  E --> G[LLM Retrieval Tools]
  G --> H[Context Packets]
```

## Repository Layout

```text
docs/       Architecture, privacy model, origin, publishing notes
schemas/    JSON Schemas for public interfaces
examples/   Synthetic fixtures only
db/         Empty database migrations
scripts/    Minimal synthetic ingest and query scripts
tests/      Tests that use only synthetic fixtures
```

## Security And Privacy

This repository is designed to be useful from zero without publishing
operational data. It should not contain public data dumps, scraped corpora, real
event records, generated reports, populated databases, map exports, logs,
telemetry, local paths, hostnames, credentials, or tokens.

Use synthetic fixtures for public examples. Connect real sources only in your
own private local deployment.

## Origin

Eva originated from local-first agent-memory experiments in OpenClaw, but the
public core is runtime-agnostic.

## Documentation

- [Geo-Temporal Context Core](docs/GEO_TEMPORAL_CONTEXT_CORE.md)
- [Start From Zero](docs/START_FROM_ZERO.md)
- [Privacy Model](docs/PRIVACY_MODEL.md)
- [OpenClaw Origin](docs/OPENCLAW_ORIGIN.md)
- [Maintainer Guide](docs/MAINTAINER_GUIDE.md)
