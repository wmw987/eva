# OpenClaw Origin

Eva originated as a local-first agent memory experiment inside OpenClaw.

OpenClaw was the prototyping environment for the operational loop: reports,
context routing, map-oriented thinking, source-aware retrieval, and iterative
agent workflows. That origin matters because Eva was shaped by practical agent
work rather than by a purely abstract schema exercise.

The public Eva core is intentionally runtime-agnostic. It should be possible to
adapt the same ideas to CLI tools, local APIs, MCP servers, desktop assistants,
or other agent runtimes.

## What OpenClaw Means Here

- OpenClaw was the workspace where the architecture was explored.
- OpenClaw influenced the emphasis on local-first operation, bounded context,
  provenance, and agent-friendly tools.
- OpenClaw is not required to understand or reuse the public Eva specification.

## What Is Not Included

The public repository should not include operational OpenClaw data:

- reports;
- logs;
- message history;
- local memory files;
- generated map exports;
- databases;
- caches;
- hostnames, ports, usernames, credentials, or deployment topology.

Eva's public repository should contain the reusable architecture, schemas,
interfaces, empty setup path, documentation, and synthetic fixtures only.
