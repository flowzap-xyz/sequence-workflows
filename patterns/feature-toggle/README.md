# Feature Toggle

Feature toggle pattern with flag configuration, user targeting rules, percentage rollouts, and instant kill-switch capability for production features.

**Domain:** patterns  
**Complexity:** 3/5  
**Tags:** [feature-toggle, feature-flags, dark-launch, a-b-testing, gradual-rollout, kill-switch]

## Lanes
- **Feature Flag Service** - Stores and evaluates flags
- **Application** - Checks flags, renders features
- **Admin Console** - Configures flag rules

## Process Flow
1. Define feature flag with default state
2. Configure targeting rules (user, %, environment)
3. Application requests flag evaluation
4. Evaluate rules against user context
5. Return flag state (on/off/variant)
6. Application renders appropriate experience
7. Track feature usage metrics
8. Adjust rollout percentage as needed
9. Kill-switch: Instantly disable if issues
