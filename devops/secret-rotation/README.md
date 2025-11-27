# Secret Rotation

Automated secret rotation workflow with HashiCorp Vault for API keys, database passwords, and certificates including Kubernetes secret updates and rolling service restarts.

**Domain:** devops  
**Complexity:** 4/5  
**Tags:** [secret-rotation, vault, kubernetes-secrets, api-keys, database-passwords, certificates, security]

## Lanes
- **Rotation Scheduler** - Monitors expiration dates, triggers rotation
- **Secret Vault** - Generates new secrets, stores versions by type
- **Secret Deployment** - Updates K8s secrets, triggers rolling restarts

## Process Flow
1. Check secret expiration dates in inventory
2. Identify secrets due for rotation
3. Generate new secret value in Vault
4. Store new version with metadata
5. Route by secret type (API key, DB password, certificate)
6. Update Kubernetes secrets
7. Trigger rolling restart of dependent services
8. Verify services are healthy after restart
9. Mark rotation successful or rollback to previous
