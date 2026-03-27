# MCP Tool Router Architecture

A routing pattern that puts a semantic router in front of MCP tools so the LLM only sees the subset it needs. Uses vector embeddings and cosine similarity to match user intent to tools dynamically. Achieves up to 96% reduction in input tokens when dealing with large tool catalogs.

**Template ID:** `mcp-tool-router`  
**Kind:** architecture  
**Source domain:** DevOps  
**Primary use case:** handoff  
**Secondary use cases:** mcp  
**Complexity:** 3/5  
**Nodes:** 8  
**Lanes:** 4  
**Tags:** [mcp, tool-router, semantic-routing, embeddings, token-optimization, architecture-diagram, production-grade]  
**Source path:** ``  
**Repo path:** `handoff/devops/mcp-tool-router`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
