# Fixed Assets

Fixed asset management workflow with asset capitalization, depreciation scheduling, physical inventory verification, and asset disposal/retirement processing.

**Domain:** finance  
**Complexity:** 3/5  
**Tags:** [fixed-assets, asset-tracking, depreciation, capitalization, asset-disposal, physical-inventory]

## Lanes
- **Asset Manager** - Requests capitalization, manages inventory
- **Finance System** - Calculates depreciation, maintains asset register

## Process Flow
1. Receive asset acquisition request
2. Determine if expense or capitalize (threshold check)
3. Create asset record with useful life
4. Calculate and schedule depreciation
5. Conduct periodic physical inventory
6. Reconcile physical count to register
7. Process asset transfers between locations
8. Handle asset disposal or retirement
