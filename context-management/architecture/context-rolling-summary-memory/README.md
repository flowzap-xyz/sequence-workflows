# Context Management - Rolling Summary Memory

Compressed history pattern that keeps full history for a while, then when a threshold is hit, summarizes the last chunk and replaces detailed turns with a shorter summary message. Dramatically reduces prompt size on long-running chats while maintaining gist continuity.

**Template ID:** `context-rolling-summary-memory`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** context-management  
**Secondary use cases:** None  
**Complexity:** 3/5  
**Nodes:** 8  
**Lanes:** 4  
**Tags:** [context-management, rolling-summary, compression, memory, architecture-diagram]  
**Source path:** ``  
**Repo path:** `context-management/architecture/context-rolling-summary-memory`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
