# Certificate Renewal

SSL/TLS certificate renewal workflow with expiration monitoring, certificate request by type (DV/OV/EV), domain validation, deployment to load balancers, and health check verification with rollback.

**Domain:** devops  
**Complexity:** 4/5  
**Tags:** [ssl-certificate, tls-renewal, lets-encrypt, certificate-authority, domain-validation, load-balancer, health-check]

## Lanes
- **Certificate Monitor** - Monitors expiration, triggers renewal process
- **Certificate Authority** - Requests certificates, validates domains
- **Deployment** - Deploys to load balancers, verifies health

## Process Flow
1. Monitor certificate expiration dates
2. Trigger renewal 30 days before expiry
3. Determine certificate type (DV/OV/EV)
4. Submit certificate request to CA
5. Complete domain validation (DNS/HTTP)
6. Download renewed certificate
7. Deploy to load balancers
8. Run health checks on endpoints
9. Rollback to previous cert if health check fails
10. Update certificate inventory
