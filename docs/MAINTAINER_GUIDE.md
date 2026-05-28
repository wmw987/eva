# GitHub Publication Guide

This guide explains how to publish **Eva**, a local-first geo-temporal memory
repository, in a way that is visible, credible, safe, and useful from a clean
start.

## 1. Choose the public shape

Recommended options:

1. **Architecture note in an existing repository**
   - Best if the repository already contains the relevant code.
   - Add `docs/GEO_TEMPORAL_CONTEXT_CORE.md`.

2. **Standalone repository**
   - Best if the goal is public visibility and serious discussion.
   - Suggested repository names:
     - `eva-memory`
     - `eva-geo-temporal-memory`
     - `eva-agent-memory`

3. **GitHub Discussion or Issue**
   - Best as an opening proposal before code is cleaned for publication.
   - Link back to the architecture note.

My recommendation: publish a standalone repository if this should be treated as
a serious project, not just an internal subsystem.

## 2. Repository description

Use a short, searchable description:

```text
Local-first geo-temporal context layer for LLM agents: events, maps,
timelines, provenance, and structured retrieval.
```

Suggested topics:

```text
llm, ai-agents, agent-memory, knowledge-graph, geospatial, temporal,
spatio-temporal, local-first, rag, mcp, sqlite, geojson
```

## 3. Safe initial file set

For the first public push, include only reviewed files:

```text
README.md
docs/GEO_TEMPORAL_CONTEXT_CORE.md
docs/START_FROM_ZERO.md
docs/OPENCLAW_ORIGIN.md
docs/PRIVACY_MODEL.md
CONTRIBUTING.md
SECURITY.md
schemas/event.schema.json
schemas/context-packet.schema.json
db/migrations/001_init.sql
examples/synthetic_event.json
examples/synthetic_context_packet.json
scripts/ingest_synthetic.py
scripts/query_events.py
tests/test_event_schema.py
tests/test_context_packet_schema.py
tests/test_migration.py
tests/test_ingest_event.py
LICENSE
```

For a clean public launch, avoid mixing the reusable architecture with
machine-specific files, public data dumps, private logs, private memory,
generated operational reports, scraped content, caches, databases, map exports,
or telemetry. Empty migrations, synthetic fixtures, and tests are allowed and
recommended.

## 4. Suggested README outline

```markdown
# Eva

Local-first geo-temporal context layer for LLM agents.

Technical architecture: Geo-Temporal Context Core.

## What it is

A structured memory layer for events, places, timelines, sources, risk,
confidence, and map-based context.

## Why

Vector memory alone loses time, geography, provenance, and state changes.
LLM agents need an external world model they can query.

## Current status

Early architecture/prototype. The public repository currently contains the
specification, schema direction, empty setup path, and synthetic examples only.

## Origin

Eva originated as a local-first agent memory experiment inside OpenClaw.
OpenClaw was the prototyping workspace; Eva's public core is runtime-agnostic.

## Core idea

The LLM interprets structured context. It does not store truth.

## Roadmap

- Minimal event schema
- CLI query interface
- Static map/timeline demo
- MCP-style agent tools
- Bitemporal state and supersession

## Security

This repository contains only reusable architecture, schemas, examples, and
documentation. Public datasets, deployment-specific data, generated reports,
logs, caches, populated databases, and credentials are intentionally out of
scope.
```

## 5. Suggested GitHub issue body

```markdown
## Proposal: Eva

I am building Eva, a local-first spatio-temporal memory layer for LLM agents.

The goal is to move beyond flat vector memory by giving agents a structured
world model:

- events with time, geography, source, confidence, and risk;
- thematic map layers;
- point-in-time and time-windowed queries;
- provenance-aware context packets;
- LLM tools that retrieve bounded context instead of raw dumps.

The design principle is:

> The LLM should interpret structured context, not become the database.

Related areas include temporal knowledge graphs, GraphRAG, agent memory
databases, geospatial knowledge graphs, and local-first AI systems. The specific
focus here is the combination of geography, timeline, provenance, and agent
retrieval.

Architecture note:
`docs/GEO_TEMPORAL_CONTEXT_CORE.md`

Feedback wanted:

- minimal schema design;
- temporal validity model;
- geospatial query patterns;
- MCP/tool interface shape;
- synthetic demo design;
- safety and privacy review.
```

## 6. Commands for a new standalone repository

Run these from a clean directory:

```bash
mkdir eva
cd eva
git init
mkdir -p docs examples
cp /path/to/reviewed/GEO_TEMPORAL_CONTEXT_CORE.md docs/
```

Create `README.md`, `LICENSE`, and synthetic examples, then:

```bash
git add README.md docs schemas db examples tests LICENSE
git commit -m "Add Eva architecture note"
git branch -M main
git remote add origin git@github.com:<your-user>/eva.git
git push -u origin main
```

## 7. Commands for an existing repository

Only use this if the existing repository is already intended to be public:

```bash
mkdir -p docs schemas examples db/migrations tests
git add README.md CONTRIBUTING.md SECURITY.md docs schemas examples db scripts tests LICENSE .gitignore pyproject.toml requirements-dev.txt .github
git commit -m "Add Eva public architecture note"
git push
```

Before pushing, run:

```bash
git diff --cached
```

Check that the staged diff contains no private paths, hostnames, IP addresses,
ports, tokens, personal identifiers, or operational logs.

## 8. How to make it noticeable

For visibility, the first public version should be precise and restrained:

- lead with the one-sentence value proposition;
- include a simple architecture diagram;
- include a small synthetic JSON example;
- include an empty migration and a test that loads only synthetic fixtures;
- clearly state what is working vs planned;
- compare respectfully with temporal knowledge graphs and vector memory;
- use GitHub topics aggressively;
- publish one concise post on LinkedIn, X, Hacker News "Show HN" if there is a
  runnable demo, and relevant Reddit communities only after the repository is
  clean.

Good communities to consider after there is a demo:

- `r/LocalLLaMA`
- `r/AI_Agents`
- `r/Rag`
- `r/KnowledgeGraph`
- GIS/geospatial developer communities

Avoid overclaiming. The serious framing is:

```text
This is an early architecture and prototype direction for structured,
geo-temporal agent memory. Feedback on schema, retrieval, and safety is welcome.
```

## 9. Pre-publication safety checklist

Before publishing:

- [ ] Search for IP addresses and local ports.
- [ ] Search for usernames, local paths, and hostnames.
- [ ] Search for tokens, API keys, cookies, and credentials.
- [ ] Remove private memory and logs.
- [ ] Remove public datasets, scraped content, generated reports, databases,
      map exports, telemetry, and caches.
- [ ] Replace real examples with fully synthetic records.
- [ ] Confirm the repo can initialize an empty local store from scratch.
- [ ] Confirm tests run only on synthetic fixtures.
- [ ] Confirm `.gitignore` excludes generated data, databases, caches, and logs.
- [ ] Review the final GitHub page in a browser before sharing links publicly.
