# Shipping Process

Order shipping workflow with carrier selection, rate shopping, label generation, tracking number assignment, and dispatch confirmation.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [shipping-process, order-fulfillment, carrier-selection, label-generation, tracking-number, dispatch]

## Lanes
- **Warehouse** - Picks, packs, and stages orders for shipping
- **Shipping System** - Selects carrier, generates labels
- **Carrier** - Picks up and delivers packages

## Process Flow
1. Receive packed order ready for shipping
2. Determine shipping method (ground, express, freight)
3. Rate shop across carriers for best price
4. Select carrier and service level
5. Generate shipping label
6. Assign tracking number
7. Stage for carrier pickup
8. Confirm dispatch and update order status
9. Send tracking notification to customer
