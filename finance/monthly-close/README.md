# Monthly Close

Corporate month-end financial close process including transaction posting, bank reconciliation, accruals, depreciation, trial balance validation, and financial statement generation.

**Domain:** finance  
**Complexity:** 4/5  
**Tags:** [monthly-close, financial-reporting, accounting, reconciliation, trial-balance, period-close]

## Lanes
- **Controller** - Initiates close, reviews checklist, approves statements
- **Accounting Team** - Posts transactions, reconciles accounts, records accruals
- **Validation** - Runs trial balance, verifies debits/credits balance
- **Financial Reporting** - Generates income statement, balance sheet, cash flow

## Process Flow
1. Controller initiates month-end close process
2. Accounting posts pending transactions and reconciles bank accounts
3. System checks if reconciliation is balanced (retry if not)
4. Record accruals and post depreciation entries
5. Review intercompany transactions
6. Run trial balance and verify debits equal credits
7. Lock accounting period once validated
8. Generate financial statements (P&L, balance sheet, cash flow)
9. Prepare variance analysis and package for leadership
10. Controller approves final financial statements
