# MCP Context Proxy Architecture

A caching and compression layer that sits between agents and MCP servers, intercepting redundant context requests before they hit the wire. Uses TTL-based cache invalidation, Brotli compression, and semantic caching. Can achieve up to 95%+ token reduction and significantly lower LLM bills.

**Template ID:** `mcp-context-proxy`  
**Kind:** architecture  
**Source domain:** DevOps  
**Primary use case:** mcp  
**Secondary use cases:** None  
**Complexity:** 3/5  
**Nodes:** 7  
**Lanes:** 3  
**Tags:** [mcp, context-proxy, caching, compression, token-optimization, architecture-diagram, production-grade]  
**Source path:** ``  
**Repo path:** `mcp/devops/mcp-context-proxy`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
