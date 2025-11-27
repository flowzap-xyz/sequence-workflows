# Push Notification

Mobile push notification workflow with audience targeting, platform routing (iOS/Android), delivery tracking, and engagement analytics.

**Domain:** business-operations  
**Complexity:** 3/5  
**Tags:** [push-notification, mobile-engagement, firebase-fcm, apns, segmentation, deep-linking]

## Lanes
- **Marketing/System** - Triggers notification
- **Push Service** - Routes to platform providers
- **Mobile Device** - Receives and displays

## Process Flow
1. Trigger push notification event
2. Select target audience segment
3. Compose notification content
4. Add deep link for action
5. Route to FCM (Android) or APNS (iOS)
6. Deliver to device
7. Track delivery status
8. User taps notification
9. Record engagement metrics
