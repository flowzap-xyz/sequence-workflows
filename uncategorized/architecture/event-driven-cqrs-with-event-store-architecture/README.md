# Event-Driven CQRS with Event Store Architecture

A CQRS architecture diagram combining separate command and query APIs with an event bus for asynchronous read model synchronization, including projectors that build denormalized views from domain events. This template demonstrates the full CQRS+ES stack where writes go through domain validation and reads are served from optimized materialized views. Ideal for high-throughput systems where read and write workloads have fundamentally different scaling requirements.

**Template ID:** `event-driven-cqrs-with-event-store-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** uncategorized  
**Secondary use cases:** None  
**Complexity:** 4/5  
**Nodes:** 18  
**Lanes:** 4  
**Tags:** [cqrs, event-store, command-query-separation, read-model, write-model, projector, eventual-consistency, architecture-diagram]  
**Source path:** ``  
**Repo path:** `uncategorized/architecture/event-driven-cqrs-with-event-store-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
