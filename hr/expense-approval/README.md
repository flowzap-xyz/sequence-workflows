# Expense Approval

Employee expense approval workflow with receipt validation, policy compliance check, tiered approval based on amount, and reimbursement processing.

**Domain:** hr  
**Complexity:** 3/5  
**Tags:** [expense-approval, travel-expenses, receipt-validation, policy-compliance, tiered-approval, reimbursement]

## Lanes
- **Employee** - Submits expense report with receipts
- **Manager** - Reviews and approves within limit
- **Finance** - Validates policy, processes reimbursement

## Process Flow
1. Employee submits expense report
2. Attach receipts and categorize expenses
3. System validates against expense policy
4. Route to manager for approval
5. If over manager limit, escalate to director
6. Finance reviews for policy compliance
7. Flag any out-of-policy items
8. Process approved reimbursement
9. Deposit to employee account
