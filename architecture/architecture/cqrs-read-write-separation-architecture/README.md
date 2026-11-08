# CQRS Read-Write Separation Architecture

A CQRS read-write separation architecture diagram with dedicated command and query paths, PostgreSQL for writes, Redis or Elasticsearch for optimized reads, and an event-driven synchronization layer with lag monitoring. This template demonstrates the core CQRS principle of separating read and write models to independently scale and optimize each path. Ideal for applications with asymmetric read/write ratios where query performance is critical.

**Template ID:** `cqrs-read-write-separation-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** architecture  
**Secondary use cases:** None  
**Complexity:** 4/5  
**Nodes:** 18  
**Lanes:** 4  
**Tags:** [cqrs, read-write-separation, command-query, postgresql, redis, elasticsearch, read-model-sync, architecture-diagram]  
**Source path:** ``  
**Repo path:** `architecture/architecture/cqrs-read-write-separation-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
