# Purchase Order

Procurement purchase order workflow with requisition creation, budget validation, vendor sourcing, competitive bidding, and tiered approval routing based on amount thresholds.

**Domain:** finance  
**Complexity:** 4/5  
**Tags:** [purchase-order, procurement, requisition, vendor-sourcing, competitive-bidding, tiered-approval, budget-validation]

## Lanes
- **Requester** - Creates requisition, adds line items, receives PO number
- **Procurement** - Reviews requisition, sources vendors, requests quotes
- **Approval Chain** - Routes based on amount, manager/director/VP approval

## Process Flow
1. Requester creates purchase requisition with line items
2. Attach specifications and submit
3. Procurement reviews and checks budget availability
4. Source vendors and determine if competitive bids required
5. Request quotes from multiple vendors if required
6. Select best vendor based on price/quality
7. Route for approval based on amount threshold
8. < $5K: Manager approval
9. $5K-$50K: Director approval
10. > $50K: VP approval
11. Generate PO number upon approval
