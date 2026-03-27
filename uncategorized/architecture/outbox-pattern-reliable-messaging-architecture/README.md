# Outbox Pattern for Reliable Messaging Architecture

A transactional outbox architecture diagram where domain writes and event publishing happen in the same database transaction, with a relay process polling the outbox table and publishing events to a message broker with guaranteed delivery. This template solves the dual-write problem where updating a database and publishing an event are not atomic, ensuring exactly-once event delivery without distributed transactions. Critical for event-driven architectures requiring reliable message publishing.

**Template ID:** `outbox-pattern-reliable-messaging-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** uncategorized  
**Secondary use cases:** None  
**Complexity:** 4/5  
**Nodes:** 18  
**Lanes:** 4  
**Tags:** [outbox-pattern, transactional-outbox, reliable-messaging, dual-write, exactly-once, debezium, event-publishing, architecture-diagram]  
**Source path:** ``  
**Repo path:** `uncategorized/architecture/outbox-pattern-reliable-messaging-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
