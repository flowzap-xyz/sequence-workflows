# Two Factor Setup

Two-factor authentication setup workflow with method selection (TOTP/SMS), QR code generation, backup codes, and verification confirmation.

**Domain:** business-operations  
**Complexity:** 2/5  
**Tags:** [two-factor-auth, mfa, totp, authenticator-app, security, account-protection]

## Lanes
- **User** - Initiates 2FA setup and completes verification
- **Auth System** - Generates secrets, QR codes, and validates codes

## Process Flow
1. User navigates to security settings
2. Select 2FA method (authenticator app or SMS)
3. Generate TOTP secret and QR code
4. User scans QR code with authenticator app
5. User enters verification code
6. Validate code against secret
7. Generate backup recovery codes
8. Store 2FA configuration
9. Send confirmation email
