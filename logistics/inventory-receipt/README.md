# Inventory Receipt

Inventory receiving workflow with ASN verification, PO matching, quantity count, damage inspection, and WMS inventory update.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [inventory-receipt, goods-receiving, po-matching, asn-verification, dock-scheduling, wms]

## Lanes
- **Receiving Dock** - Unloads shipments, counts items
- **WMS System** - Matches to PO, updates inventory

## Process Flow
1. Receive advance shipping notice (ASN)
2. Schedule dock door and unload time
3. Unload shipment at receiving dock
4. Verify against ASN and purchase order
5. Count items and check for damage
6. Report discrepancies if any
7. Label items with location barcodes
8. Update WMS with received quantities
9. Stage for put-away
