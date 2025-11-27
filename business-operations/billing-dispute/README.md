# Billing Dispute

Billing dispute workflow with dispute intake, transaction review, fraud analysis, resolution decision, and chargeback response handling.

**Domain:** business-operations  
**Complexity:** 4/5  
**Tags:** [billing-dispute, chargeback, refund-request, dispute-resolution, fraud-review, stripe]

## Lanes
- **Customer** - Files dispute
- **Support** - Investigates claim
- **Finance** - Reviews transaction
- **Fraud Team** - Analyzes for fraud

## Process Flow
1. Receive billing dispute or chargeback
2. Acknowledge receipt to customer
3. Pull transaction and usage records
4. Review for fraud indicators
5. Determine if dispute is valid
6. If valid, process refund
7. If invalid, prepare evidence
8. Submit chargeback response
9. Notify customer of resolution
