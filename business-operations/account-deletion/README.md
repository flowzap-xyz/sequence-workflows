# Account Deletion

Account deletion workflow with cancellation reason capture, retention offer, subscription termination, data cleanup, and confirmation email.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [account-deletion, user-offboarding, data-cleanup, subscription-cancel, retention-offer, exit-survey]

## Lanes
- **User** - Requests deletion, provides feedback
- **System** - Processes deletion, cleans up data

## Process Flow
1. User requests account deletion
2. Present exit survey for feedback
3. Show retention offer (discount, pause)
4. If declined, confirm deletion intent
5. Cancel active subscriptions
6. Revoke API keys and tokens
7. Schedule data deletion
8. Send deletion confirmation
9. Purge data after grace period
