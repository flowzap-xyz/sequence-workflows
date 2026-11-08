# Permission Gate Containment Workflow

Layer 2 of the agent containment stack: a permission gate checks the whitelist and path scope before execution, and aborts the call with a logged denial when the scope does not match.

**Template ID:** `permission-gate-containment-workflow`  
**Kind:** workflow  
**Source domain:** Agentic Security  
**Primary use case:** security  
**Secondary use cases:** agentic  
**Complexity:** 2/5  
**Nodes:** 8  
**Lanes:** 2  
**Tags:** [agent-containment, permissions, whitelist, security, blast-radius]  
**Source path:** ``  
**Repo path:** `security/agentic-security/permission-gate-containment-workflow`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
