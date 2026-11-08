# CQRS Materialized View Architecture

A CQRS materialized view architecture diagram with multiple projectors building purpose-specific read models: order summaries, customer dashboards, analytics cubes, and search indexes, all fed from a single event stream. This template shows how to create multiple optimized query views from the same write events, each tailored to a specific use case with sub-millisecond read latency. Perfect for systems requiring diverse query patterns from a single data source.

**Template ID:** `cqrs-materialized-view-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** architecture  
**Secondary use cases:** None  
**Complexity:** 4/5  
**Nodes:** 18  
**Lanes:** 4  
**Tags:** [materialized-view, cqrs, projectors, read-model, denormalization, query-optimization, event-stream, architecture-diagram]  
**Source path:** ``  
**Repo path:** `architecture/architecture/cqrs-materialized-view-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
