# Retry With Backoff

Exponential backoff retry pattern for API calls with configurable retry limits, delay calculation, retryable error detection, and graceful degradation on permanent failures.

**Domain:** patterns  
**Complexity:** 4/5  
**Tags:** [retry-pattern, exponential-backoff, fault-tolerance, api-resilience, transient-errors, http-retry, jitter]

## Lanes
- **Client** - Prepares requests, processes responses, handles failures
- **Retry Handler** - Manages retry state, calculates delays, executes retries
- **API Server** - Receives requests, returns success or error responses

## Process Flow
1. Client prepares API request
2. Retry handler initializes retry state (counter, max retries)
3. Execute HTTP request to API server
4. Check response status code
5. 2xx: Return success to client
6. 4xx/5xx: Check if error is retryable (503, 429, etc.)
7. If retryable and retries remaining, calculate backoff delay
8. Wait exponential delay (e.g., 1s, 2s, 4s, 8s)
9. Increment retry counter and retry request
10. If max retries exceeded, return permanent failure
