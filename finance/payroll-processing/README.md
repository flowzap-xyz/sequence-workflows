# Payroll Processing

Complete payroll processing workflow with timesheet collection, gross pay calculation, overtime, tax withholding (federal, state, FICA), benefits deductions, compliance validation, and ACH direct deposit.

**Domain:** finance  
**Complexity:** 5/5  
**Tags:** [payroll-processing, salary-calculation, tax-withholding, fica, ach-direct-deposit, benefits-deductions, compliance]

## Lanes
- **HR System** - Collects timesheets, imports attendance, finalizes payroll
- **Payroll Engine** - Applies pay rates, calculates overtime, processes deductions
- **Compliance** - Withholds taxes (federal, state, FICA), validates compliance
- **Banking** - Creates ACH batch, submits to bank, confirms transfers

## Process Flow
1. Collect timesheet data and import attendance records
2. Apply pay rates and calculate overtime
3. Add bonuses and commissions
4. Process deductions and validate
5. Calculate net pay
6. Withhold federal and state taxes
7. Calculate FICA contributions
8. Process benefits deductions
9. Run compliance check
10. Generate pay stubs
11. Create ACH batch file and submit to bank
12. Confirm transfers and update payroll records
