# Saga Travel Booking Architecture

A travel booking saga architecture diagram orchestrating flight, hotel, and car rental reservations as a single distributed transaction, with automatic compensation to cancel all bookings if any reservation step fails. This template models the classic saga use case where multiple independent services must either all succeed or all roll back, ensuring travelers never end up with partial bookings. Perfect for demonstrating saga patterns with a real-world business scenario.

**Template ID:** `saga-travel-booking-architecture`  
**Kind:** architecture  
**Source domain:** Architecture  
**Primary use case:** ai-orchestration  
**Secondary use cases:** architecture, patterns  
**Complexity:** 4/5  
**Nodes:** 17  
**Lanes:** 5  
**Tags:** [saga-pattern, travel-booking, flight-reservation, hotel-booking, compensation, distributed-transaction, orchestration, architecture-diagram]  
**Source path:** ``  
**Repo path:** `ai-orchestration/architecture/saga-travel-booking-architecture`

## Files
- `workflow.fz` — FlowZap Code source
- `metadata.json` — Structured metadata
