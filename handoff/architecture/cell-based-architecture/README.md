# Cell-Based Architecture

A cell-based architecture diagram with geographic routing to independent, self-contained cells (US-East, EU-West), each with its own gateway, compute, database, cache, and message queue, plus shared services for cross-cell replication and global configuration. This template models the cell architecture pattern used by hyperscale systems to achieve blast radius isolation, where failures in one cell cannot affect users in another. Key for architects designing systems that require extreme availability and fault isolation.

**Template ID:** `cell-based-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** handoff  
**Secondary use cases:** None  
**Complexity:** 4/5  
**Nodes:** 20  
**Lanes:** 4  
**Tags:** [cell-based-architecture, blast-radius, geographic-routing, fault-isolation, independent-cells, cross-cell-replication, hyperscale, architecture-diagram]  
**Source path:** ``  
**Repo path:** `handoff/architecture/cell-based-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
