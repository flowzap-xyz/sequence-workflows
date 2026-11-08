# Saga Orchestration Pattern Architecture

A saga orchestration architecture diagram with a central orchestrator coordinating multi-step distributed transactions across Order, Inventory, and Payment services, with a dedicated compensation chain for rollback on failure. This template models the orchestration-based saga pattern where a single coordinator manages the transaction lifecycle and triggers compensating actions when any step fails. Essential for architects implementing reliable distributed transactions without two-phase commit.

**Template ID:** `saga-orchestration-pattern-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** delivery  
**Secondary use cases:** ai-orchestration, architecture, patterns  
**Complexity:** 4/5  
**Nodes:** 19  
**Lanes:** 5  
**Tags:** [saga-pattern, orchestration, distributed-transaction, compensation, microservices, rollback, consistency, architecture-diagram]  
**Source path:** ``  
**Repo path:** `delivery/architecture/saga-orchestration-pattern-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
