# GDPR Data Deletion

GDPR data deletion workflow with identity verification, data inventory scan, PII removal across systems, backup purging, and deletion confirmation.

**Domain:** business-operations  
**Complexity:** 4/5  
**Tags:** [gdpr-deletion, right-to-be-forgotten, data-privacy, pii-removal, compliance, dsar]

## Lanes
- **Data Subject** - Requests deletion
- **Privacy Team** - Verifies and coordinates
- **Systems** - Execute deletion across databases
- **Compliance** - Audits and confirms

## Process Flow
1. Receive data deletion request (DSAR)
2. Verify requester identity
3. Inventory all systems with user data
4. Check for legal retention requirements
5. Delete PII from primary databases
6. Remove from analytics and logs
7. Purge from backups (within retention)
8. Notify third-party processors
9. Send deletion confirmation to user
