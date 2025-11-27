# Database Migration

Database schema migration workflow with CI testing, DBA review and approval, maintenance window scheduling, backup snapshots, migration execution, data integrity verification, and automatic rollback.

**Domain:** devops  
**Complexity:** 4/5  
**Tags:** [database-migration, schema-changes, flyway, liquibase, rollback, dba-approval, maintenance-window]

## Lanes
- **Developer** - Creates migration script, tests locally, reviews results
- **CI Pipeline** - Runs migration in test DB, generates rollback script
- **Database Admin** - Reviews migration plan, approves for production
- **Production Database** - Creates backup, executes migration, verifies integrity

## Process Flow
1. Developer creates migration script
2. Test migration locally
3. CI runs migration in test database
4. If successful, generate rollback script
5. DBA reviews migration plan
6. If approved, schedule maintenance window
7. Create backup snapshot before migration
8. Enable maintenance mode
9. Execute migration script
10. Verify data integrity
11. If failed, execute rollback script
12. Disable maintenance mode and notify developer
