# Payment Run

Accounts payable payment run workflow with batch creation, tiered approval (single/dual based on amount), ACH file generation, check printing, and vendor record updates.

**Domain:** finance  
**Complexity:** 4/5  
**Tags:** [payment-run, accounts-payable, ach-payments, check-run, dual-approval, bank-transfer, vendor-payments]

## Lanes
- **AP Clerk** - Selects invoices, creates batch, confirms payments
- **Payment Approval** - Reviews batch, routes for single/dual approval
- **Banking System** - Generates ACH files, prints checks, submits to bank

## Process Flow
1. AP clerk selects invoices for payment
2. Create payment batch
3. Review batch and check total amount
4. < $50K: Single approver required
5. >= $50K: Dual approval required
6. If rejected, return for correction
7. Generate ACH file or check run based on payment method
8. Submit to bank or print checks
9. Confirm transmission
10. Update vendor records with payment status
