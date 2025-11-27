# Packing Process

Order packing workflow with carton selection, item verification, packing slip insertion, weight check, and package sealing for shipment.

**Domain:** logistics  
**Complexity:** 2/5  
**Tags:** [order-packing, box-selection, packing-slip, weight-verification, cartonization, fulfillment]

## Lanes
- **Packer** - Selects box, packs items, seals package
- **System** - Verifies contents, prints packing slip

## Process Flow
1. Receive picked items at packing station
2. Scan order to retrieve packing instructions
3. Select appropriate box size
4. Verify all items present
5. Add packing materials for protection
6. Insert packing slip
7. Seal package
8. Weigh package and verify
9. Move to shipping staging area
