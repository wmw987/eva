# Roadmap

Eva is currently an early public architecture and prototype skeleton for a local-first geo-temporal context layer for LLM agents.

## Phase 1 — Public skeleton

- Public documentation
- Synthetic examples only
- JSON schemas
- SQLite migration draft
- Basic CLI scripts
- Unit tests
- GitHub Actions workflow

## Phase 2 — Query correctness

- Implement real `--since` time filtering
- Add stronger validation for event timestamps
- Add tests for risk, region, topic, and time filters
- Improve query behavior documentation

## Phase 3 — Spatial context

- Add basic spatial queries
- Support region hierarchy
- Improve location normalization
- Prepare map-ready exports

## Phase 4 — Agent interface

- Add an MCP-compatible interface or tool wrapper
- Return bounded context packets for LLM agents
- Add provenance-aware query responses

## Phase 5 — Timeline and map demo

- Add simple timeline output
- Add map-ready synthetic demo scenarios
- Add examples showing how an agent should consume context packets

## Phase 6 — Bitemporal and supersession logic

- Track when events occurred
- Track when events were observed
- Support corrections, superseded claims, and conflicting sources
