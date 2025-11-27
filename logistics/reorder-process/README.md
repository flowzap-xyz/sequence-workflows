# Reorder Process

Inventory reorder workflow with reorder point monitoring, economic order quantity calculation, safety stock consideration, and automatic purchase requisition generation.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [reorder-process, reorder-point, safety-stock, eoq, demand-planning, auto-replenishment]

## Lanes
- **Inventory System** - Monitors levels, triggers reorders
- **Procurement** - Reviews and places purchase orders

## Process Flow
1. Monitor inventory levels continuously
2. Compare to reorder point threshold
3. Trigger reorder alert when below ROP
4. Calculate economic order quantity (EOQ)
5. Factor in safety stock requirements
6. Generate purchase requisition
7. Route for approval if needed
8. Convert to purchase order
9. Send to supplier
