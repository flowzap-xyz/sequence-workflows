# Plan Downgrade

Subscription plan downgrade workflow with retention offer, feature restriction warning, data migration handling, and end-of-period scheduling.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [plan-downgrade, retention, feature-restriction, data-migration, churn-prevention, billing]

## Lanes
- **Customer** - Requests downgrade
- **Retention** - Offers alternatives
- **Billing System** - Schedules change
- **Product** - Handles feature restrictions

## Process Flow
1. Customer initiates downgrade request
2. Show retention offer (discount, pause)
3. If declined, show feature loss warning
4. Check data limits on new plan
5. Warn about data that won't fit
6. Schedule downgrade for period end
7. Send confirmation with effective date
8. At period end, restrict features
9. Adjust billing to new plan rate
