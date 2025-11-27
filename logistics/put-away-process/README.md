# Put Away Process

Warehouse put-away workflow with location assignment, slotting optimization, forklift routing, barcode confirmation, and WMS location update.

**Domain:** logistics  
**Complexity:** 2/5  
**Tags:** [put-away, warehouse-storage, location-assignment, slotting, wms, inventory-placement]

## Lanes
- **WMS System** - Assigns locations, optimizes slotting
- **Warehouse Worker** - Transports and stores items

## Process Flow
1. Receive items staged for put-away
2. Scan item barcode
3. WMS assigns optimal storage location
4. Generate put-away task
5. Transport item to assigned location
6. Scan location barcode to verify
7. Place item in location
8. Confirm put-away complete
9. Update WMS inventory location
