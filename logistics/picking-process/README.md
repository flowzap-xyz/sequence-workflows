# Picking Process

Warehouse order picking workflow with pick list generation, zone routing, batch picking optimization, barcode scanning verification, and pick completion confirmation.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [order-picking, warehouse-management, pick-list, batch-picking, wave-picking, wms]

## Lanes
- **WMS System** - Generates pick lists, optimizes routes
- **Picker** - Navigates warehouse, picks items
- **Quality Check** - Verifies picks, resolves discrepancies

## Process Flow
1. Receive orders for picking wave
2. Generate optimized pick list
3. Route picker through warehouse zones
4. Navigate to pick location
5. Scan location barcode to verify
6. Pick item and scan product barcode
7. Confirm quantity picked
8. Handle stock-outs or discrepancies
9. Complete pick and stage for packing
