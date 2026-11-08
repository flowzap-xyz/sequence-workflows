# Context Management - Profile Memory

Identity-style memory pattern where profile data is loaded at session start. Each prompt combines system persona, user profile, and current message. New facts can be written back to profile memory. Small predictable overhead with big UX lift — the agent remembers your name, stack, tone, and constraints.

**Template ID:** `context-profile-memory`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** architecture  
**Secondary use cases:** context-management  
**Complexity:** 2/5  
**Nodes:** 7  
**Lanes:** 3  
**Tags:** [context-management, profile-memory, identity, user-profile, architecture-diagram]  
**Source path:** ``  
**Repo path:** `architecture/architecture/context-profile-memory`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
