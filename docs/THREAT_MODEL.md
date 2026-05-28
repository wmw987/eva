# Threat Model

Eva is designed as a local-first geo-temporal context layer for LLM agents. The LLM should interpret structured context, not become the database of truth.

## Key risks

### Private data leakage

The public repository must never include real private datasets, API keys, credentials, logs, `.env` files, local databases, or user-specific files.

### Prompt injection

External sources may contain malicious instructions intended to influence an LLM agent. Eva should treat source content as data, not as trusted instructions.

### Source poisoning

Sources may be false, manipulated, outdated, or intentionally misleading. Events should keep provenance, confidence, and source metadata.

### Stale facts

World state changes over time. Eva should make it clear when an event was observed, when it occurred, and whether it has been superseded.

### False confidence

The system should avoid presenting uncertain or conflicting information as settled fact.

### Public/private boundary

The public repository should contain only documentation, schemas, synthetic examples, tests, and non-sensitive code. Real deployments should keep private data outside the public repo.

## Security posture

Eva is not a trust oracle. It is a structured memory and retrieval layer. Human review, source validation, and explicit provenance remain necessary.
