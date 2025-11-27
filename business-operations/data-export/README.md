# Data Export

User data export workflow with export request, async job processing, data aggregation, secure file generation, and download link delivery.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [data-export, data-portability, gdpr, bulk-export, async-job, download-link]

## Lanes
- **User** - Requests export, downloads data
- **Export Service** - Aggregates and packages data
- **Storage** - Stores export file temporarily

## Process Flow
1. User requests data export
2. Verify user identity
3. Queue async export job
4. Aggregate data from all sources
5. Generate export file (JSON/CSV)
6. Encrypt and store temporarily
7. Generate secure download link
8. Email download link to user
9. Auto-delete file after expiry
