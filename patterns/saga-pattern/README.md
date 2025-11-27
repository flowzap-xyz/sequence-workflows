# Saga Pattern

Saga orchestration pattern for distributed transactions across Order, Payment, and Shipping services with automatic compensation rollback on failures.

**Domain:** patterns  
**Complexity:** 5/5  
**Tags:** [saga-pattern, distributed-transactions, microservices, compensation, orchestration, eventual-consistency, rollback]

## Lanes
- **Saga Orchestrator** - Coordinates transaction steps, triggers compensations
- **Order Service** - Creates orders, reserves inventory
- **Payment Service** - Processes payments, handles refunds
- **Shipping Service** - Schedules shipments, generates tracking

## Process Flow
1. Orchestrator begins distributed transaction
2. **Step 1**: Order Service creates order and reserves inventory
3. If order fails, trigger compensation chain
4. **Step 2**: Payment Service processes payment
5. If payment fails, refund and release inventory
6. **Step 3**: Shipping Service schedules shipment
7. If shipping fails, compensate payment and order
8. On success, commit saga and generate tracking number
9. Compensation chain: Refund → Release inventory → Cancel order
