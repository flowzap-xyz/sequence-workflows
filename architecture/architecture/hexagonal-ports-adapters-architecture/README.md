# Hexagonal (Ports and Adapters) Architecture

A hexagonal architecture diagram showing the clean separation between domain core, inbound adapters (REST, GraphQL, CLI, message consumers), outbound adapters (PostgreSQL, Stripe, email, Redis), and the port interfaces that connect them. This template visualizes the ports and adapters pattern where the domain core has zero dependencies on infrastructure, making it fully testable and technology-agnostic. Foundational for teams adopting clean architecture principles in their codebase.

**Template ID:** `hexagonal-ports-adapters-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** architecture  
**Secondary use cases:** None  
**Complexity:** 4/5  
**Nodes:** 16  
**Lanes:** 4  
**Tags:** [hexagonal-architecture, ports-and-adapters, clean-architecture, dependency-inversion, domain-core, testability, technology-agnostic, architecture-diagram]  
**Source path:** ``  
**Repo path:** `architecture/architecture/hexagonal-ports-adapters-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
