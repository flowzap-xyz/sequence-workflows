# Carrier Selection

Carrier selection workflow with rate shopping, transit time comparison, service level matching, carrier performance scoring, and optimal carrier assignment.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [carrier-selection, rate-shopping, transit-time, service-level, tms, freight-optimization]

## Lanes
- **Order System** - Provides shipment requirements
- **TMS** - Shops rates, selects carrier
- **Carrier Network** - Provides rates and capacity

## Process Flow
1. Receive shipment requirements (weight, dimensions, destination)
2. Determine required service level (ground, express, freight)
3. Query carrier network for rates
4. Compare transit times vs delivery requirement
5. Factor in carrier performance scores
6. Apply business rules (preferred carriers, contracts)
7. Select optimal carrier
8. Book shipment with carrier
9. Generate shipping documents
