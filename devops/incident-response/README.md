# Incident Response

Production incident response workflow with severity-based routing, war room coordination, incident commander assignment, customer communication, root cause analysis, and postmortem scheduling.

**Domain:** devops  
**Complexity:** 5/5  
**Tags:** [incident-management, on-call, pagerduty, war-room, severity-levels, postmortem, sre]

## Lanes
- **Monitoring System** - Triggers alerts, pages on-call, logs timeline
- **On-Call Responder** - Acknowledges, assesses severity, escalates
- **Incident Command** - Opens war room, assigns commander, coordinates
- **Resolution** - Root cause analysis, fix implementation, postmortem

## Process Flow
1. Alert triggered by monitoring system
2. Page on-call responder via PagerDuty
3. Responder acknowledges and assesses severity
4. SEV-1/2: Declare major incident, open war room
5. SEV-3/4: Begin direct troubleshooting
6. Assign incident commander for major incidents
7. Coordinate response teams and communicate status
8. Notify customer success if customer impact detected
9. Identify root cause and implement fix
10. Verify recovery and close incident
11. Schedule postmortem for learning
