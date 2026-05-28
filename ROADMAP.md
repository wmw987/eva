# Eva Roadmap

Eva is currently an early public architecture and prototype skeleton for a local-first geo-temporal context layer for LLM agents.

This roadmap explains what exists now, what should be improved next, and what is intentionally not production-ready yet.

## Current status

Eva currently includes:

- public documentation
- synthetic examples only
- JSON schemas
- an SQLite migration draft
- basic CLI scripts
- unit tests
- a GitHub Actions workflow

Eva is not a finished product yet.

## Phase 1 - Public skeleton

Goal:

Make the public repository clear, honest, and easy to understand.

Includes:

- public documentation
- synthetic examples only
- JSON schemas
- SQLite migration draft
- basic CLI scripts
- unit tests
- GitHub Actions workflow

Status:

Mostly done.

Next improvements:

- improve README formatting
- add project badges
- add clear example output
- link all key documentation files from README
- keep public examples synthetic

## Phase 2 - Query correctness

Goal:

Make event querying more predictable and easier to test.

Planned work:

- implement real `--since` time filtering
- add stronger validation for event timestamps
- add tests for risk filters
- add tests for region filters
- add tests for topic filters
- add tests for time filters
- improve query behavior documentation

## Phase 3 - Spatial context

Goal:

Add basic spatial reasoning without pretending that Eva is a finished geospatial engine.

Planned work:

- add basic spatial queries
- support region hierarchy
- improve location normalization
- prepare map-ready exports
- keep all demo data synthetic

## Phase 4 - Agent interface

Goal:

Make Eva usable by local AI agents and external tools.

Planned work:

- design a minimal local API
- design an MCP-compatible interface or tool wrapper
- return bounded context packets for LLM agents
- add provenance-aware query responses
- document how an agent should consume Eva context

## Phase 5 - Timeline and map demo

Goal:

Show how geo-temporal context can be inspected visually.

Planned work:

- add simple timeline output
- add map-ready synthetic demo scenarios
- add examples showing how an agent should consume context packets
- avoid publishing real operational datasets

## Phase 6 - Bitemporal and supersession logic

Goal:

Support events that change over time, including corrections and conflicting claims.

Planned work:

- track when events occurred
- track when events were observed
- support corrected claims
- support superseded claims
- support conflicting sources
- make uncertainty visible in context packets

## Not production-ready yet

The following features are not finished and should not be presented as complete:

- real-time web crawling
- production data ingestion
- production geospatial indexing
- map and timeline UI
- automated fact verification
- MCP server
- OpenClaw integration
- large-scale world event database

## Project principle

The LLM should interpret structured context, not become the database.
