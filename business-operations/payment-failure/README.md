# Payment Failure Recovery

Failed payment recovery workflow with smart retry scheduling, dunning email sequence, payment method update prompts, and involuntary churn prevention.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [payment-failure, dunning, retry-logic, card-decline, revenue-recovery, stripe]

## Lanes
- **Billing System** - Retries payments, manages dunning
- **Customer** - Updates payment method

## Process Flow
1. Detect failed payment
2. Classify failure reason (insufficient funds, expired, etc.)
3. Schedule smart retry based on failure type
4. Send first dunning email
5. Retry payment after delay
6. If still failing, send update card prompt
7. Customer updates payment method
8. Retry with new payment method
9. If all retries fail, suspend account
