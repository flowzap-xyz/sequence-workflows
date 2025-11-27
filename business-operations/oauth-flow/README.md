# OAuth 2.0 Flow

OAuth 2.0 authorization code flow with redirect handling, code exchange, token storage, refresh token rotation, and scope management.

**Domain:** business-operations  
**Complexity:** 4/5  
**Tags:** [oauth-flow, oauth2, authorization-code, token-exchange, sso, third-party-auth]

## Lanes
- **User** - Initiates login, grants consent
- **Client App** - Requests authorization
- **Auth Server** - Issues tokens
- **Resource Server** - Validates tokens

## Process Flow
1. User clicks "Login with Provider"
2. Redirect to authorization server
3. User authenticates and grants consent
4. Auth server redirects with auth code
5. Exchange code for access token
6. Receive access and refresh tokens
7. Store tokens securely
8. Use access token for API calls
9. Refresh token when expired
