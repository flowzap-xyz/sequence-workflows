# MCP Circuit Breaker Architecture

A resilience pattern that wraps MCP calls with health-aware gates using three states: Closed (normal), Open (failures detected, fast-fail), and Half-Open (testing recovery). Prevents cascading failures when tools become unresponsive. Essential for production-grade reliability.

**Template ID:** `mcp-circuit-breaker`  
**Kind:** architecture  
**Source domain:** DevOps  
**Primary use case:** mcp  
**Secondary use cases:** patterns  
**Complexity:** 3/5  
**Nodes:** 9  
**Lanes:** 3  
**Tags:** [mcp, circuit-breaker, resilience, fault-tolerance, health-check, architecture-diagram, production-grade]  
**Source path:** ``  
**Repo path:** `mcp/devops/mcp-circuit-breaker`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
