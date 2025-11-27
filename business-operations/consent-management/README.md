# Consent Management

User consent management workflow with cookie banner, preference center, consent recording, downstream system sync, and audit trail.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [consent-management, gdpr, cookie-consent, privacy-preferences, opt-in-opt-out, compliance]

## Lanes
- **User** - Views banner, sets preferences
- **Consent Platform** - Records and syncs consent

## Process Flow
1. User visits site/app
2. Display cookie consent banner
3. User selects preferences (essential, analytics, marketing)
4. Record consent with timestamp
5. Store consent proof for audit
6. Sync preferences to analytics tools
7. Block non-consented tracking
8. Allow preference updates anytime
9. Re-prompt on policy changes
