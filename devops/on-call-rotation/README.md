# On-Call Rotation

On-call rotation workflow with schedule creation, shift handoffs, override management, escalation policies, and fair rotation distribution.

**Domain:** devops  
**Complexity:** 3/5  
**Tags:** [on-call-rotation, incident-management, pagerduty, escalation, schedule-management, handoff]

## Lanes
- **Engineering Manager** - Creates rotation schedule
- **On-Call Engineer** - Primary responder
- **Backup Engineer** - Secondary escalation
- **PagerDuty** - Manages schedules and alerts

## Process Flow
1. Create on-call rotation schedule
2. Assign engineers to shifts
3. Configure escalation policies
4. Handle override requests (PTO, swaps)
5. Notify engineer of upcoming shift
6. Conduct shift handoff meeting
7. Transfer context on active issues
8. Update schedule in PagerDuty
9. Track on-call burden for fairness
