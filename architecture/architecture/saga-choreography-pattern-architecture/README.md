# Saga Choreography Pattern Architecture

A saga choreography architecture diagram where Order, Payment, and Inventory services coordinate through domain events without a central orchestrator, with each service publishing and subscribing to events that drive the transaction forward or trigger compensation. This template models the decentralized saga approach where services autonomously react to events, reducing single points of failure at the cost of increased complexity in tracking saga state. Best for teams preferring service autonomy over centralized control.

**Template ID:** `saga-choreography-pattern-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** architecture  
**Secondary use cases:** patterns  
**Complexity:** 4/5  
**Nodes:** 18  
**Lanes:** 5  
**Tags:** [saga-choreography, event-driven-saga, decentralized, domain-events, compensation, autonomous-services, distributed-transaction, architecture-diagram]  
**Source path:** ``  
**Repo path:** `architecture/architecture/saga-choreography-pattern-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
