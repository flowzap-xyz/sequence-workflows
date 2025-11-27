# Dunning Flow

Dunning collection workflow with escalating reminder emails, grace period management, account suspension, and payment recovery tracking.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [dunning-flow, collections, overdue-payment, payment-reminder, account-suspension, revenue-recovery]

## Lanes
- **Billing System** - Tracks overdue, sends reminders
- **Customer** - Receives notices, makes payment
- **Collections** - Escalates delinquent accounts

## Process Flow
1. Payment becomes overdue
2. Send first reminder (Day 1)
3. Wait grace period
4. Send second reminder with urgency (Day 7)
5. Send final notice with suspension warning (Day 14)
6. Suspend account access (Day 21)
7. Customer makes payment
8. Restore account access
9. Track recovery metrics
