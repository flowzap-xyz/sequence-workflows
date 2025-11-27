# Event Sourcing

Event sourcing pattern with event capture, event store persistence, aggregate reconstruction, snapshot optimization, and temporal state queries.

**Domain:** patterns  
**Complexity:** 4/5  
**Tags:** [event-sourcing, event-store, aggregate, replay, audit-log, temporal-query]

## Lanes
- **Command Handler** - Validates and processes commands
- **Event Store** - Persists immutable event stream
- **Projection** - Builds read models from events

## Process Flow
1. Receive command to modify aggregate
2. Load aggregate from event store
3. Replay events to rebuild current state
4. Validate command against current state
5. Generate new domain event
6. Append event to event store
7. Publish event to subscribers
8. Update read model projections
9. Return success to caller
