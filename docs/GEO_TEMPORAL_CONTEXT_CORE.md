# Geo-Temporal Context Core

## A spatio-temporal world memory layer for LLM agents

**Project name:** Eva

Large language models are strong reasoning and language interfaces, but they are
weak as long-term stores of truth. A useful agent needs more than a vector index
over past messages. It needs a structured way to ask:

- What happened?
- Where did it happen?
- When did it happen?
- Which sources support it?
- Which entities, regions, topics, and risks are connected?
- What changed since the last known state?

**Eva** is the project name for this implementation direction.
**Geo-Temporal Context Core** is the technical architecture: a local-first
memory layer that gives LLM agents structured, queryable context across
geography, time, provenance, confidence, and thematic layers.

The central idea is simple:

> The LLM should interpret structured context, not become the database.

Instead of treating memory as a flat bag of embeddings, this project models
context as a layered event system: events have time, place, source, topic,
confidence, risk, and relationships to other entities. The LLM then uses this
system as an external cognitive substrate for analysis, summaries, alerts,
and decision support.

## Why this matters

Most LLM memory systems focus on one of three patterns:

1. Conversation recall: remembering what the user said.
2. Document retrieval: retrieving chunks from files or web pages.
3. Knowledge graphs: representing entities and relationships.

Those are useful, but they often miss the operational shape of real-world
context. Many important questions are inherently geo-temporal:

- Which events are clustering near a region?
- Did risk increase or decrease during a specific time window?
- Which historical layers matter for the current situation?
- What changed between two points in time?
- Which reports are about the same place but different topics?
- Which source claims are confirmed, uncertain, outdated, or superseded?

For an LLM agent, this is the difference between "searching memory" and
maintaining a working model of the world.

## Design principles

### 1. Local-first

The system should work on local data, local indexes, and local tools by default.
Cloud services may be useful for selected enrichment, but the core memory layer
should not require private context to leave the machine.

### 2. Structured truth, generative interpretation

The database stores facts, events, metadata, provenance, and relationships. The
LLM explains, prioritizes, compares, and drafts. These roles should not be mixed.

### 3. Time is a first-class dimension

Each record should carry explicit temporal metadata. The system should support
queries such as "what did we know at this time?", "what changed?", and "which
events occurred in this interval?"

### 4. Geography is not just metadata

Location should be queryable as a real dimension: country, region, city,
coordinate, bounding area, route, chokepoint, and thematic layer. This enables
spatial filtering, clustering, map views, and event correlation.

### 5. Confidence and provenance are mandatory

Agent memory should preserve uncertainty. Every significant record should carry
source references, confidence level, timestamps, and enough provenance to audit
why the system believes something.

### 6. The map is an interface, not the source of truth

A map view is a powerful way to inspect context, but the canonical state should
live in structured data stores and source documents. Visualizations are windows
into the memory layer.

## Conceptual architecture

```text
Sources
  -> collectors and parsers
  -> normalized event records
  -> geo-temporal event store
  -> full-text, vector, graph, and spatial indexes
  -> map and timeline interfaces
  -> LLM tools for retrieval, reasoning, and reporting
```

The memory layer can be implemented with ordinary components:

- an event store for normalized observations and reports;
- a geospatial layer for coordinates, regions, administrative areas, and
  thematic overlays;
- a timeline layer for event windows, validity intervals, and state changes;
- a search layer for full-text, semantic, and structured queries;
- a provenance layer for sources, confidence, and audit trails;
- an agent interface exposed through CLI tools, local APIs, or MCP-style tools.

The geometry model should be storage-agnostic. Simple deployments can store
GeoJSON as ordinary JSON, while advanced deployments can project the same
records into PostGIS, SpatiaLite, DuckDB, or another spatial index.

## Core data model

A minimal event record can look like this:

```json
{
  "id": "event_...",
  "title": "Short human-readable event title",
  "summary": "Compact description of the observation",
  "topic": "global-risk | market | infrastructure | research | ...",
  "time": {
    "observed_at": "2026-05-28T12:00:00Z",
    "valid_from": "2026-05-28T12:00:00Z",
    "valid_to": null,
    "precision": "hour"
  },
  "geo": {
    "label": "Region or place name",
    "country": "Example Country",
    "region": "Example Region",
    "geometry": {
      "type": "Point",
      "coordinates": [0.0, 0.0]
    },
    "centroid": {
      "lat": 0.0,
      "lon": 0.0
    },
    "precision_m": 10000
  },
  "assessment": {
    "risk": "low | medium | high",
    "confidence": "confirmed | signal | rumor | unknown"
  },
  "provenance": {
    "sources": [
      {
        "type": "synthetic-report | manual-note | test-fixture",
        "ref": "synthetic source identifier",
        "retrieved_at": "2026-05-28T12:05:00Z"
      }
    ]
  },
  "relations": [
    {
      "type": "mentions | affects | contradicts | supersedes | related_to",
      "target_id": "entity_or_event_id"
    }
  ]
}
```

This is intentionally conservative. The important part is not the exact schema,
but the separation of:

- observed event;
- time;
- place;
- confidence;
- provenance;
- relationships;
- downstream interpretation.

The `geometry` object should follow GeoJSON conventions and may represent a
`Point`, `Polygon`, `MultiPolygon`, or `LineString`. The `centroid` field is a
compatibility and fallback field for simple filtering, clustering, and map
views that do not need full spatial geometry.

## Example LLM queries

Once exposed as tools, the LLM should be able to ask precise questions:

- "Show high-risk events in this region during the last 48 hours."
- "Compare today's situation with the same region last month."
- "Which sources support this claim?"
- "List unresolved signals that have not been confirmed."
- "Find events near this route or chokepoint."
- "Summarize what changed since the last briefing."
- "Give me the map layers relevant to this question."

The result should be a bounded, inspectable context packet rather than a large
dump of raw data.

A compact context packet might look like this:

```json
{
  "query": {
    "region": "Example Region",
    "time_window": "P2D",
    "risk": "high"
  },
  "results": [
    {
      "id": "event_123",
      "title": "Synthetic disruption signal near example chokepoint",
      "time": "2026-05-28T09:30:00Z",
      "geo": {
        "label": "Example Chokepoint",
        "geometry": {
          "type": "Point",
          "coordinates": [0.0, 0.0]
        }
      },
      "assessment": {
        "risk": "high",
        "confidence": "signal"
      },
      "sources": ["source_ref_1"]
    }
  ],
  "limits": {
    "max_results": 10,
    "source_policy": "citations_required"
  }
}
```

## Relationship to existing work

This project is adjacent to temporal knowledge graphs, GraphRAG, agent memory
databases, and bitemporal memory systems. Related directions include:

- temporal knowledge graphs for agent memory;
- bitemporal fact stores;
- graph-based retrieval augmented generation;
- geospatial knowledge graphs;
- local-first AI memory systems;
- MCP-accessible memory tools.

The distinguishing focus here is the combination of:

- geography as a primary query dimension;
- timeline-native world events;
- thematic map layers;
- provenance and confidence tracking;
- local-first operation;
- LLMs as interpreters over structured memory, not as stores of truth.

## Current prototype direction

The prototype direction is to combine:

- a normalized event store;
- geospatial enrichment;
- time-windowed queries;
- generated map layers;
- compact context routing;
- report and source provenance;
- LLM-facing retrieval tools.

The first useful milestone is not a perfect database. It is a reliable loop:

```text
ingest -> normalize -> geotag -> timestamp -> index -> query -> visualize -> brief
```

Once that loop is stable, the system can grow toward:

- point-in-time state reconstruction;
- entity and relationship graphs;
- contradiction and supersession tracking;
- confidence scoring;
- scenario comparison;
- alerting;
- local agent workflows;
- synthetic demo records.

This document describes the reusable public core, not a dump of any private
deployment. A private prototype may keep compatibility fields such as latitude
and longitude centroids while gradually adding richer GeoJSON geometries and
spatial indexes. The public schema should be treated as an interface contract,
not as a requirement to expose operational data. Public repositories for Eva
should use synthetic fixtures and setup instructions, not public data dumps,
scraped corpora, or real operational records.

## Origin

Eva originated as a local-first agent memory experiment inside OpenClaw.
OpenClaw served as the operational workspace for reports, context routing, map
layers, and iterative agent workflows. The public core is designed to be
runtime-agnostic and can be adapted to CLI tools, local APIs, MCP servers, or
other agent runtimes.

## Publication and privacy posture

Projects in this category should be designed with a clear boundary between the
public architecture and any private operational deployment. A public repository
should be useful enough for someone to start from zero while revealing nothing
about a private deployment.

A public repository can safely include:

- schemas;
- small synthetic fixtures;
- diagrams;
- empty database migrations;
- local setup instructions;
- importer and query skeletons;
- validation tests for synthetic fixtures;
- threat model and privacy notes;
- extension points.

The public artifact should focus on the reusable design: schemas, interfaces,
query patterns, synthetic fixtures, setup instructions, and evaluation.
Deployment-specific data, scraped corpora, generated reports, logs, databases,
map exports, and real-world datasets belong in separate private environments.

## Suggested roadmap

### Phase 1: Public specification

- Publish the concept note.
- Define the minimal event schema.
- Add synthetic sample records.
- Document the local-first security model.
- Document the storage-agnostic geometry contract.

### Phase 2: Query interface

- Add CLI queries for time, geography, topic, risk, and confidence.
- Return compact JSON context packets suitable for LLM tools.
- Validate GeoJSON geometry, centroid fallback, and location precision.
- Add deterministic tests for filtering, provenance, and basic spatial queries.

### Phase 3: Map and timeline demo

- Publish a static demo using synthetic data only.
- Add timeline filtering.
- Add thematic overlays.
- Keep the demo disconnected from private local data and real public datasets.

### Phase 4: Agent integration

- Expose selected queries through an MCP-style interface or equivalent tool API.
- Add prompt examples showing how an LLM should use the memory layer.
- Add guardrails for bounded retrieval and source-aware answers.

### Phase 5: Temporal reasoning

- Add valid-time and recorded-time support.
- Track superseded facts.
- Support point-in-time reconstruction.
- Add contradiction and uncertainty workflows.

## One-sentence summary

Eva is a local-first geo-temporal context layer for LLM agents: a structured,
source-aware, map-and-timeline-native system that lets models reason over what
happened, where, when, and how confidently it is known.
