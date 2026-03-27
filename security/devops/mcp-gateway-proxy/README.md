# MCP Gateway Proxy Architecture

An API gateway pattern that sits between agents and MCP servers to handle authentication, rate limits, and auditing. The gateway enforces OAuth 2.0, SAML, SSO, tool-level rate limiting, and team-based quotas. Essential for multi-team or multi-tenant MCP deployments.

**Template ID:** `mcp-gateway-proxy`  
**Kind:** architecture  
**Source domain:** DevOps  
**Primary use case:** security  
**Secondary use cases:** compliance, mcp  
**Complexity:** 3/5  
**Nodes:** 7  
**Lanes:** 3  
**Tags:** [mcp, gateway, proxy, oauth, rate-limiting, audit, architecture-diagram, production-grade]  
**Source path:** ``  
**Repo path:** `security/devops/mcp-gateway-proxy`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
