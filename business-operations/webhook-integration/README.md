# Webhook Integration

Webhook integration workflow with endpoint registration, payload signing, delivery attempt, retry with backoff, and delivery status tracking.

**Domain:** business-operations  
**Complexity:** 2/5  
**Tags:** [webhook, event-driven, http-callback, integration, retry-logic, payload-signing]

## Lanes
- **Source System** - Triggers events and sends webhooks
- **Webhook Service** - Manages delivery and retries

## Process Flow
1. Register webhook endpoint URL
2. Configure event subscriptions
3. Event occurs in source system
4. Build webhook payload
5. Sign payload with HMAC secret
6. POST to registered endpoint
7. Check response status code
8. Retry with exponential backoff on failure
9. Log delivery status and attempts
