# SMS Verification

SMS phone verification workflow with OTP generation, rate limiting, code validation, retry handling, and verification status tracking.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [sms-verification, otp, twilio, phone-verification, 2fa, fraud-prevention]

## Lanes
- **User** - Enters phone, submits code
- **Application** - Validates input
- **SMS Provider** - Sends OTP via Twilio
- **Verification Service** - Validates code

## Process Flow
1. User enters phone number
2. Validate phone format
3. Check rate limits (prevent abuse)
4. Generate 6-digit OTP
5. Send SMS via Twilio
6. User receives and enters code
7. Validate code matches and not expired
8. If invalid, allow retry (max 3)
9. Mark phone as verified
