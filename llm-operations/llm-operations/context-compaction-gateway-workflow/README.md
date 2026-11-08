# Context Compaction Gateway Workflow

A context gateway that assembles raw context from the vector store and logs, compacts 100k tokens down to 15k and only then builds the final prompt.

**Template ID:** `context-compaction-gateway-workflow`  
**Kind:** workflow  
**Source domain:** LLM Operations  
**Primary use case:** llm-operations  
**Secondary use cases:** mcp, context-management  
**Complexity:** 2/5  
**Nodes:** 12  
**Lanes:** 4  
**Tags:** [token-optimization, context-management, compaction, rag, llmops]  
**Source path:** ``  
**Repo path:** `llm-operations/llm-operations/context-compaction-gateway-workflow`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
