# Chaos Engineering

Chaos engineering workflow with hypothesis definition, steady-state monitoring, controlled fault injection, blast radius limitation, and resilience validation.

**Domain:** devops  
**Complexity:** 4/5  
**Tags:** [chaos-engineering, fault-injection, resilience-testing, game-day, blast-radius, steady-state]

## Lanes
- **SRE Team** - Designs experiments, analyzes results
- **Chaos Platform** - Executes fault injection
- **Monitoring** - Tracks system behavior
- **Production System** - Target of chaos experiments

## Process Flow
1. Define hypothesis about system resilience
2. Establish steady-state metrics baseline
3. Design chaos experiment
4. Limit blast radius (start small)
5. Inject fault (network, CPU, pod kill)
6. Monitor system behavior
7. Verify graceful degradation
8. Halt if unexpected impact
9. Document findings and improvements
