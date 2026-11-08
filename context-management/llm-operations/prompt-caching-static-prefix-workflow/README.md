# Prompt Caching with Static Prefix Workflow

Static system prompt assembled once and cached by the provider, then only the volatile user input is appended — a cache hit reads 50k tokens from the KV cache.

**Template ID:** `prompt-caching-static-prefix-workflow`  
**Kind:** workflow  
**Source domain:** LLM Operations  
**Primary use case:** context-management  
**Secondary use cases:** None  
**Complexity:** 3/5  
**Nodes:** 14  
**Lanes:** 2  
**Tags:** [token-optimization, prompt-caching, kv-cache, context-management, llmops]  
**Source path:** ``  
**Repo path:** `context-management/llm-operations/prompt-caching-static-prefix-workflow`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
