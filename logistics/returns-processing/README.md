# Returns Processing

Customer returns processing workflow with RMA generation, return receipt, quality inspection, disposition decision, and refund or exchange processing.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [returns-processing, rma, refund, restocking, quality-inspection, reverse-logistics]

## Lanes
- **Customer Service** - Initiates RMA, processes refund/exchange
- **Warehouse** - Receives return, inspects, restocks or disposes

## Process Flow
1. Customer requests return
2. Generate RMA (Return Merchandise Authorization)
3. Send return shipping label
4. Receive returned item at warehouse
5. Inspect item condition
6. Determine disposition (restock, refurbish, dispose)
7. Update inventory if restocking
8. Process refund or ship exchange
9. Close RMA and notify customer
