# Event-Driven CDC (Change Data Capture) Architecture

A Change Data Capture architecture diagram using Debezium to tail database transaction logs and publish change events to Kafka, feeding downstream consumers that update search indexes, invalidate caches, load data warehouses, and write audit logs. This template shows how CDC eliminates dual-write problems by capturing changes at the database level without modifying application code. Critical for data synchronization across heterogeneous systems.

**Template ID:** `event-driven-cdc-change-data-capture-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** architecture  
**Secondary use cases:** None  
**Complexity:** 4/5  
**Nodes:** 17  
**Lanes:** 4  
**Tags:** [change-data-capture, cdc, debezium, transaction-log, kafka-connect, data-synchronization, dual-write, architecture-diagram]  
**Source path:** ``  
**Repo path:** `architecture/architecture/event-driven-cdc-change-data-capture-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
