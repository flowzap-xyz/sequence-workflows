# Agent Sandbox Containment Workflow

Layer 1 of the agent containment stack: every tool call executes in an ephemeral container, and any path outside the workspace is denied and logged as a security event.

**Template ID:** `agent-sandbox-containment-workflow`  
**Kind:** workflow  
**Source domain:** Agentic Security  
**Primary use case:** agentic-security  
**Secondary use cases:** security, agentic  
**Complexity:** 2/5  
**Nodes:** 8  
**Lanes:** 2  
**Tags:** [agent-containment, sandbox, blast-radius, security, tool-call]  
**Source path:** ``  
**Repo path:** `agentic-security/agentic-security/agent-sandbox-containment-workflow`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
