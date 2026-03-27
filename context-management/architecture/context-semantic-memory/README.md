# Context Management - Semantic Memory

Vector-based memory pattern where text is chunked, embedded, and stored in a vector database. On query, the question is embedded, a vector search is run, candidates are reranked, and top results are injected into the prompt. Where the agent feels like it remembers everything without hallucinating.

**Template ID:** `context-semantic-memory`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** context-management  
**Secondary use cases:** None  
**Complexity:** 3/5  
**Nodes:** 9  
**Lanes:** 4  
**Tags:** [context-management, semantic-memory, vector-db, embeddings, rag, architecture-diagram]  
**Source path:** ``  
**Repo path:** `context-management/architecture/context-semantic-memory`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
