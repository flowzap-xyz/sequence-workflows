# Invoice Processing

Accounts payable invoice automation with OCR data extraction, three-way PO matching, tiered approval workflow, and automated payment processing with GL updates.

**Domain:** finance  
**Complexity:** 4/5  
**Tags:** [accounts-payable, invoice-automation, ocr, po-matching, approval-workflow, payment-processing, three-way-match]

## Lanes
- **Vendor** - Submits invoices, receives payment notifications
- **AP Automation** - OCR extraction, PO matching, auto-approval
- **Approval Workflow** - Manager and director approval routing
- **Payment Processing** - Batch scheduling, bank transfers, GL updates

## Process Flow
1. Vendor submits invoice via email
2. OCR extracts invoice data automatically
3. System attempts to match invoice to purchase order
4. If PO match found and within threshold, auto-approve
5. If no match or over threshold, route to manual review
6. Manager approval required for flagged invoices
7. Director approval for amounts over manager limit
8. Schedule approved invoices in payment batch
9. Execute bank transfer and update general ledger
10. Send remittance advice to vendor
