# Ambassador Pattern Architecture

An ambassador pattern architecture diagram with a local proxy sidecar handling authentication header injection, circuit breaking, retry logic, and metrics collection for outbound requests to external third-party APIs. This template models the ambassador pattern where a helper service running alongside the application offloads cross-cutting concerns for external communication. Useful for teams integrating with unreliable third-party services that need resilience wrappers.

**Template ID:** `ambassador-pattern-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** mcp  
**Secondary use cases:** patterns  
**Complexity:** 3/5  
**Nodes:** 15  
**Lanes:** 3  
**Tags:** [ambassador-pattern, sidecar-proxy, external-api, retry-logic, circuit-breaker, metrics-collection, cross-cutting-concerns, architecture-diagram]  
**Source path:** ``  
**Repo path:** `mcp/architecture/ambassador-pattern-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
