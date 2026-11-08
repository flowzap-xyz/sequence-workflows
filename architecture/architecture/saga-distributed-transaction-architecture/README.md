# Saga Distributed Transaction Architecture

A distributed transaction architecture diagram implementing the two-phase commit protocol with a transaction coordinator sending prepare and commit messages to participating services, with global abort on any vote failure. This template visualizes the classic 2PC protocol used when strong consistency is required across multiple services, showing the prepare, vote, and commit/abort phases. Important for understanding distributed consensus trade-offs in microservices architectures.

**Template ID:** `saga-distributed-transaction-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** architecture  
**Secondary use cases:** ai-orchestration  
**Complexity:** 4/5  
**Nodes:** 17  
**Lanes:** 4  
**Tags:** [distributed-transaction, two-phase-commit, 2pc, transaction-coordinator, consensus, strong-consistency, prepare-commit, architecture-diagram]  
**Source path:** ``  
**Repo path:** `architecture/architecture/saga-distributed-transaction-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
