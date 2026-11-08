# LLM Model Router — Cost-Aware Routing

An LLM gateway that reads the token budget, extracts intent and length, then routes the call to the cheap model or the premium one before delivering the response.

**Template ID:** `llm-model-router-cost-aware-routing`  
**Kind:** workflow  
**Source domain:** LLM Operations  
**Primary use case:** handoff  
**Secondary use cases:** mcp, llm-operations  
**Complexity:** 2/5  
**Nodes:** 10  
**Lanes:** 3  
**Tags:** [token-optimization, model-routing, llm-gateway, cost, llmops]  
**Source path:** ``  
**Repo path:** `handoff/llm-operations/llm-model-router-cost-aware-routing`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
