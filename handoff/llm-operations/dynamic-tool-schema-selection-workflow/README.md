# Dynamic Tool Schema Selection Workflow

Instead of loading all 50 tool schemas into every request, the agent analyses the step, queries the MCP tool registry and injects only the two schemas it needs.

**Template ID:** `dynamic-tool-schema-selection-workflow`  
**Kind:** workflow  
**Source domain:** LLM Operations  
**Primary use case:** handoff  
**Secondary use cases:** mcp, llm-operations  
**Complexity:** 2/5  
**Nodes:** 8  
**Lanes:** 3  
**Tags:** [token-optimization, mcp, tool-schemas, tool-routing, llmops]  
**Source path:** ``  
**Repo path:** `handoff/llm-operations/dynamic-tool-schema-selection-workflow`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
