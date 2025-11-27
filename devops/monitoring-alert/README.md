# Monitoring and Alerting

Monitoring and alerting workflow with metric collection, threshold evaluation, alert routing, escalation policies, and incident creation.

**Domain:** devops  
**Complexity:** 3/5  
**Tags:** [monitoring-alerting, prometheus, pagerduty, threshold-alerts, anomaly-detection, on-call]

## Lanes
- **Monitoring System** - Collects metrics, evaluates rules
- **Alert Manager** - Routes alerts, manages escalation
- **On-Call Engineer** - Receives and responds to alerts

## Process Flow
1. Collect metrics from services
2. Evaluate alerting rules
3. Detect threshold breach
4. Deduplicate and group alerts
5. Route to appropriate team
6. Send notification (Slack, PagerDuty)
7. If no acknowledgment, escalate
8. On-call investigates issue
9. Resolve or create incident
