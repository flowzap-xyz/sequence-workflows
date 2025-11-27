# API Key Rotation

API key rotation workflow with new key generation, dual-key transition period, client notification, old key deprecation, and audit logging.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [api-key-rotation, security, credential-management, zero-downtime, secrets-manager, compliance]

## Lanes
- **Security System** - Generates keys, manages lifecycle
- **Developer Portal** - Displays keys, sends notifications
- **Client Application** - Updates to new key

## Process Flow
1. Trigger rotation (scheduled or manual)
2. Generate new API key
3. Enable dual-key acceptance period
4. Notify client of new key
5. Client retrieves new key
6. Client updates configuration
7. Monitor old key usage
8. Deprecate old key after grace period
9. Log rotation for audit
