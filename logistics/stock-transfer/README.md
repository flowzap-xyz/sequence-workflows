# Stock Transfer

Internal stock transfer workflow with transfer request, source location pick, destination put-away, and inventory record updates across locations.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [stock-transfer, inventory-movement, location-transfer, bin-to-bin, wms, inventory-rebalancing]

## Lanes
- **Requester** - Initiates transfer request
- **Source Location** - Picks and ships inventory
- **Destination Location** - Receives and puts away

## Process Flow
1. Create stock transfer request
2. Verify source location has available stock
3. Generate pick task at source
4. Pick items from source location
5. Update source inventory (decrement)
6. Ship to destination location
7. Receive at destination
8. Put away at destination location
9. Update destination inventory (increment)
