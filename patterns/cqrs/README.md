# CQRS (Command Query Responsibility Segregation)

CQRS pattern with separate command and query paths, domain event publishing, read model synchronization, and DTO transformation.

**Domain:** patterns  
**Complexity:** 4/5  
**Tags:** [cqrs, command-query-separation, event-sourcing, read-model, write-model, domain-events, eventual-consistency]

## Lanes
- **Client Application** - Initiates actions, routes to command or query side
- **Command Side** - Validates commands, executes domain logic, persists to write store
- **Event Handler** - Receives domain events, updates read model
- **Query Side** - Parses queries, reads from optimized read store, returns DTOs

## Process Flow
1. Client initiates user action
2. Determine if action is read or write operation
3. **Write path**: Send command to command side
4. Validate command against business rules
5. Execute domain logic and persist to write store
6. Publish domain event for read model sync
7. Event handler updates read model asynchronously
8. **Read path**: Send query to query side
9. Query optimized read store
10. Transform results to DTO and return to client
