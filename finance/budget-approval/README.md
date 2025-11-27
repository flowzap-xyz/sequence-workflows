# Budget Approval

Corporate budget approval workflow with tiered approval routing based on amount thresholds (CFO < $100K, CEO $100K-$1M, Board > $1M), prior year comparison, and fund allocation.

**Domain:** finance  
**Complexity:** 4/5  
**Tags:** [budget-approval, financial-planning, tiered-approval, cfo-approval, ceo-approval, board-approval, fund-allocation]

## Lanes
- **Department Manager** - Submits budget request, justifies line items
- **Finance Department** - Reviews request, compares to prior year
- **Executive Approval** - Tiered approval based on budget amount

## Process Flow
1. Department manager submits budget request
2. Justify line items and submit to Finance
3. Finance reviews and compares to prior year
4. If within guidelines, recommend approval
5. If over budget, recommend reduction
6. Route to appropriate approver based on amount
7. < $100K: CFO approval
8. $100K-$1M: CEO approval
9. > $1M: Board approval
10. If approved, allocate funds to department
