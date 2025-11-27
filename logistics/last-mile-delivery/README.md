# Last Mile Delivery

Last mile delivery workflow with route optimization, real-time GPS tracking, delivery attempt handling, proof of delivery capture, and customer notification.

**Domain:** logistics  
**Complexity:** 3/5  
**Tags:** [last-mile-delivery, route-optimization, proof-of-delivery, delivery-exception, customer-notification, gps-tracking]

## Lanes
- **Dispatch System** - Optimizes routes, tracks drivers
- **Driver** - Executes deliveries, captures POD

## Process Flow
1. Load packages onto delivery vehicle
2. Generate optimized delivery route
3. Send customer delivery window notification
4. Navigate to delivery address
5. Attempt delivery
6. If customer unavailable, handle exception
7. Capture proof of delivery (signature/photo)
8. Update delivery status in real-time
9. Complete route and return to depot
