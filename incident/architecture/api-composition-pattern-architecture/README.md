# API Composition Pattern Architecture

An API composition architecture diagram with a composer service that fans out parallel requests to multiple microservices, collects responses with timeout handling, and merges results into a single unified response with partial fallback support. This template models the API composition pattern used when a single client query requires data from multiple services, avoiding the need for direct service-to-service calls. Useful for teams building aggregation layers in microservices architectures.

**Template ID:** `api-composition-pattern-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** incident  
**Secondary use cases:** None  
**Complexity:** 3/5  
**Nodes:** 16  
**Lanes:** 3  
**Tags:** [api-composition, response-aggregation, fan-out, parallel-requests, timeout-handling, partial-response, microservices, architecture-diagram]  
**Source path:** ``  
**Repo path:** `incident/architecture/api-composition-pattern-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
