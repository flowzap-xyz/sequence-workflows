# Context Management - Session Memory

Short-term context pattern where the channel sends new messages plus recent history. The agent runtime merges that with local session state, assembles the prompt, and persists the response back into history. Simple but cost and latency grow with history length.

**Template ID:** `context-session-memory`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** context-management  
**Secondary use cases:** None  
**Complexity:** 2/5  
**Nodes:** 9  
**Lanes:** 3  
**Tags:** [context-management, session-memory, short-term, memory, architecture-diagram]  
**Source path:** ``  
**Repo path:** `context-management/architecture/context-session-memory`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
