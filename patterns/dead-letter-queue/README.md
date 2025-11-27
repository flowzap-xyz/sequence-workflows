# Dead Letter Queue

Dead letter queue pattern for handling failed messages with retry exhaustion detection, DLQ routing, manual inspection, and reprocessing capability.

**Domain:** patterns  
**Complexity:** 3/5  
**Tags:** [dead-letter-queue, dlq, message-retry, poison-message, error-handling, message-queue]

## Lanes
- **Message Consumer** - Processes messages, handles failures
- **DLQ Handler** - Stores and manages failed messages

## Process Flow
1. Consumer receives message from queue
2. Attempt to process message
3. If processing fails, increment retry count
4. Retry up to max attempts with backoff
5. If retries exhausted, route to DLQ
6. Store message with error details
7. Alert operations team
8. Manual inspection and fix
9. Reprocess or discard message
