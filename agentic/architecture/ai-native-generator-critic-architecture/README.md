# AI-Native Generator-Critic Architecture

A competitive / generator-critic architecture where multiple generators produce independent answers, then an evaluator agent scores and selects the best output. This approach improves quality and reduces single-model brittleness. It's costlier (multiple LLM calls) but pays off when correctness or creativity matters more than latency.

**Template ID:** `ai-native-generator-critic-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** agentic  
**Secondary use cases:** ai-orchestration  
**Complexity:** 3/5  
**Nodes:** 9  
**Lanes:** 3  
**Tags:** [ai-native, generator-critic, agentic-ai, tournament-mode, multi-agent, architecture-diagram]  
**Source path:** ``  
**Repo path:** `agentic/architecture/ai-native-generator-critic-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
