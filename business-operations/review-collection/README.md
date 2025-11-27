# Review Collection

Customer review collection workflow with post-purchase trigger, review request email, rating submission, moderation, and public display.

**Domain:** business-operations  
**Complexity:** 2/5  
**Tags:** [review-collection, customer-feedback, nps, ratings, social-proof, testimonials]

## Lanes
- **Customer** - Receives request, submits review
- **Review System** - Sends requests, moderates, displays

## Process Flow
1. Customer completes purchase/milestone
2. Wait appropriate delay (7 days)
3. Send review request email
4. Customer clicks to leave review
5. Submit star rating and comment
6. Auto-moderate for spam/profanity
7. Flag for manual review if needed
8. Publish approved review
9. Thank customer for feedback
