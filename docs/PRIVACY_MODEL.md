# Privacy Model

Eva is designed as a local-first memory layer. The public repository should
let a new user build an empty instance from zero without publishing operational
data from any private deployment.

## Public Repository Boundary

The public repository may include:

- architecture notes;
- schema definitions;
- interface contracts;
- diagrams;
- empty database migrations;
- synthetic fixture records;
- synthetic context packets;
- importer skeletons;
- query skeletons;
- validation tests for synthetic fixtures;
- setup notes for empty local deployments;
- privacy and threat-model documentation.

The public repository should not include:

- public data dumps;
- scraped articles or source corpora;
- real event records;
- generated reports;
- local databases;
- map exports;
- logs, telemetry, caches, or runtime state;
- private memory files;
- hostnames, ports, usernames, credentials, tokens, or deployment topology.

## Examples

Examples must be synthetic. They can demonstrate structure, timing, geometry,
confidence, provenance, and relationships, but they should not encode real
events, real people, sensitive locations, or copied source text.

## Starting From Zero

A public Eva repository should make it possible to create a fresh local
deployment with no bundled real data. The expected path is:

1. Create an empty local store from migrations.
2. Load synthetic fixtures to validate the schema and queries.
3. Replace the fixtures with the user's own local sources in their private
   environment.
4. Keep generated reports, indexes, logs, and map exports out of the public
   repository.

## Deployment Rule

Architecture can be public. Operational memory stays local.

The same schema can be used in a private deployment, but the data produced by
that deployment should remain outside the public repository unless it is
explicitly synthetic and reviewed for release.
