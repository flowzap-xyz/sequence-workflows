# Authentication Flow

User authentication workflow with credential validation, MFA challenge, JWT token generation, session creation, and failed attempt tracking.

**Domain:** patterns  
**Complexity:** 3/5  
**Tags:** [authentication, login, jwt, oauth, mfa, session-management]

## Lanes
- **User** - Submits credentials, completes MFA
- **Auth Service** - Validates credentials, issues tokens

## Process Flow
1. User submits username and password
2. Validate credentials against user store
3. Check for account lockout status
4. If MFA enabled, send challenge
5. Verify MFA code
6. Generate JWT access token
7. Create refresh token
8. Establish user session
9. Return tokens to client
