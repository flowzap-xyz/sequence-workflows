# Personalization Engine

Make.com automation scenario for real-time personalization using Segment events, ML recommendation API, and Braze campaign delivery across email and push channels.

**Domain:** business-operations  
**Complexity:** 4/5  
**Tags:** [make-com, personalization, segment, braze, ml-recommendations, content-delivery, marketing-automation]

## Lanes
- **Make.com Scenario** - Watches Segment events, routes by event type
- **Make.com HTTP Module** - Calls ML recommendation API, evaluates confidence
- **Make.com Iterator** - Delivers personalized content via Braze campaigns

## Process Flow
1. Watch Segment user events (page view, purchase, signup)
2. Parse user properties and route by event type
3. POST to recommendation API for ML predictions
4. Evaluate confidence score (threshold: 0.7)
5. Select personalized or default content based on confidence
6. Fetch content variants and select best match
7. Update Braze user profile with preferences
8. Trigger Braze campaign based on channel preference (email/push)
