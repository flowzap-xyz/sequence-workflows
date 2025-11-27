# Cache-Aside Pattern

Cache-aside pattern with cache lookup, database fallback on miss, cache population, TTL-based expiration, and write-through invalidation.

**Domain:** patterns  
**Complexity:** 3/5  
**Tags:** [cache-aside, lazy-loading, cache-miss, cache-invalidation, redis, performance]

## Lanes
- **Application** - Requests data, manages cache
- **Cache (Redis)** - Stores cached data
- **Database** - Source of truth for data

## Process Flow
1. Application requests data by key
2. Check cache for existing entry
3. If cache hit, return cached data
4. If cache miss, query database
5. Store result in cache with TTL
6. Return data to caller
7. On data update, invalidate cache entry
8. Next read will refresh from database
