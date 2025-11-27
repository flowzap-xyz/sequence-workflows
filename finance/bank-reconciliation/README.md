# Bank Reconciliation

Bank reconciliation workflow with automated transaction matching, variance reporting, discrepancy research, and journal entry creation for timing differences and bank errors.

**Domain:** finance  
**Complexity:** 4/5  
**Tags:** [bank-reconciliation, gl-matching, variance-analysis, journal-entries, auto-matching, discrepancy-resolution]

## Lanes
- **Accountant** - Imports statements, reviews reports, approves reconciliation
- **Reconciliation Engine** - Parses transactions, auto-matches, generates reports
- **Manual Review** - Researches discrepancies, creates adjusting entries

## Process Flow
1. Accountant imports bank statement
2. Engine parses bank transactions and matches with GL entries
3. If auto-match rate > 95%, generate variance report
4. If < 95%, flag unmatched items and apply matching rules
5. Display unmatched items for manual review
6. Research discrepancies and classify type
7. Create journal entry for timing differences
8. Flag unknown discrepancies for investigation
9. Mark bank errors for follow-up
10. Accountant reviews and approves reconciliation
