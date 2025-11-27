# Circuit Breaker

Circuit breaker resilience pattern with closed, open, and half-open states for protecting services from cascading failures with automatic recovery testing.

**Domain:** patterns  
**Complexity:** 4/5  
**Tags:** [circuit-breaker, resilience, fault-tolerance, microservices, hystrix, half-open, fallback]

## Lanes
- **Client** - Makes service requests, receives responses or fallbacks
- **CircuitBreaker** - Manages state transitions (closed/open/half-open)
- **Service** - Downstream service that may fail

## Process Flow
1. Client initiates request to downstream service
2. Circuit breaker checks current state
3. **Closed state**: Forward request to service, track success/failure
4. If failure threshold exceeded, trip circuit to open state
5. **Open state**: Return fallback response immediately, start timeout
6. After timeout expires, transition to half-open state
7. **Half-open state**: Allow single test request through
8. If test succeeds, reset to closed state
9. If test fails, return to open state with new timeout
