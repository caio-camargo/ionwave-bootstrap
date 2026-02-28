# TUP M18: Email Lifecycle Flows

**Status:** unknown | **Quality:** N/A/10 | **Version:** N/A
**Cluster:** BCL-4 (N/A)

---

## 📋 Overview


---

## 📁 Content Files


---

## 🔧 Structured Data

_JSON files converted to human-readable format_

_No JSON files in this TUP._

---

## 📝 Narrative Content

### 📄 cart_recovery.md

# M18: Cart Recovery Email Flows

**TUP**: M18 — Email Lifecycle Flows
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 436, 440, 441; Klaviyo abandoned cart benchmarks 2026; M17 email_flow_architecture.md

---

## 1. Cart Recovery Strategy

### Why This Flow Matters Most

Abandoned cart is the **highest-revenue automated flow** in email marketing:

| Metric | Industry Average | Top 10% | IonWave Target |
|--------|-----------------|---------|----------------|
| Cart abandonment rate | 70-75% | — | Expect 70%+ at launch |
| Recovery/conversion rate | 3.33% | 7.69% | >5% by Month 3 |
| Revenue per recipient | $3.65 | $28.89 | >$5.00 |
| Open rate | 43-50% | 55%+ | >50% |
| Click rate | 5-10% | 15%+ | >8% |

[Confidence: A | Source: Klaviyo abandoned cart benchmarks + Omnisend + Baymard Institute]

**Key insight**: 3-email series generates **69% more orders** than a single email (24.94 vs. 14.76 orders per campaign, Omnisend data). 3 emails is the sweet spot — 4th email shows diminishing returns for most brands. [Confidence: A | Source: Omnisend cart recovery data]

---

## 2. Flow Architecture

### Sequence Overview

| Email | Timing | Strategy | Discount? | Conversion Share |
|-------|--------|----------|-----------|-----------------|
| AC1 | 1 hour | Simple reminder — helpful, not pushy | **No** | 20-25% of total recoveries |
| AC2 | 24 hours | Objection handling — FAQ format | **No** (or optional 5%) | 15-20% of total recoveries |
| AC3 | 72 hours | Urgency + incentive — last chance | **Yes** (free shipping) | 8-12% of total recoveries |

[Confidence: B | Source: Danilo tabs 436/440/441 merged + Klaviyo timing recommendations]

### Discount Escalation Rules

**Do NOT lead with a discount.** Email 1 should never offer a discount — this trains customers to abandon carts intentionally.

| Email | Incentive | Rationale |
|-------|-----------|-----------|
| AC1 (1hr) | None | Most 1-hour recoveries happen from simple reminder |
| AC2 (24hr) | None or 5% max | Handle objections first. Discount only if conversion data supports it |
| AC3 (72hr) | Free shipping (code: FIRSTBOX) | Free shipping > percentage discount for first-time buyers. Less margin erosion |

**Quarterly review**: If AC1+AC2 recovery rate exceeds 4%, keep AC3 discount-free. Only add discount if recovery rate < 3% after first 200 entries. [Confidence: C | Source: DTC cart recovery optimization heuristic]

**Never offer more than free shipping in cart recovery.** Reserve 10-15% discounts for win-back flows (higher intent deficit). 25% only for win-back Email 3+. This prevents discount expectation creep. [Confidence: B | Source: DTC margin management best practice]

---

## 3. IonWave Cart Recovery Emails

### Email AC1: Simple Reminder (1 Hour)

**Subject**: You left something behind...
**Preview**: Your IonWave is waiting

---

Hey {{first_name}},

Looks like you got interrupted.

Your IonWave is still in your cart:

**{{product_name}} — {{quantity}}**
{{price}}

**[COMPLETE YOUR ORDER →]**

Quick reminder of what you're getting:

✓ 78 ionic minerals (not 3-4 like synthetic brands)
✓ 98% bioavailable (vs ~10% for pills)
✓ 30-day feel-the-difference guarantee
✓ Free shipping on subscriptions

Your cart will stay saved for 72 hours.

— Nilo

P.S. Questions holding you back? Just reply. We're here.

---

### Email AC2: Objection Handling (24 Hours)

**Subject**: Still thinking about it?
**Preview**: Let me answer the question you're probably asking...

---

Hey {{first_name}},

Still on the fence? Totally fair.

Here are the questions most people have before they try IonWave:

**"DOES IT ACTUALLY TASTE OKAY?"**
Mildly mineral, like high-quality spring water. Most people drink it straight, some add it to juice. Either works.

**"HOW LONG UNTIL I FEEL SOMETHING?"**
Most customers notice more stable energy within 3-7 days. Full benefits typically show up over 2-4 weeks.

**"IS THIS JUST EXPENSIVE SEAWATER?"**
Fair question. Here's the difference: most customers feel noticeably more stable energy within 3-7 days. If tap water or cheap electrolytes did that, you wouldn't be here. 78 minerals in the exact ratios your body recognizes — that's why it works.

**"WHAT IF IT DOESN'T WORK FOR ME?"**
30-day guarantee. Feel the difference or get every penny back. No questions, no hassle. We've had less than 3% of customers ask for a refund.

Still have questions? Hit reply. I'll answer personally.

Or if you're ready:

**[COMPLETE YOUR ORDER →]**

— Nilo

---

### Email AC3: Last Chance + Incentive (72 Hours)

**Subject**: Last chance: your cart expires tonight
**Preview**: Plus: free shipping on us

---

Hey {{first_name}},

Your IonWave cart expires in 24 hours.

After that, you'll need to start over.

Before it clears, I wanted to make this easy:

**I've added FREE SHIPPING to your cart.**

No code needed. It's already applied. Just click through and complete your order.

Here's what's waiting for you:

**{{product_name}} — {{quantity}}**
{{price}}

**[CLAIM FREE SHIPPING →]**

78 minerals. 30 seconds. 30-day guarantee.

Your body will thank you.

— Nilo

P.S. This is the last email about your cart. If now's not the right time, no worries. We'll be here when you're ready.

---

## 4. Flow Logic & Technical Configuration

### Klaviyo Flow Setup

```
TRIGGER: Added to Cart
  ↓
FILTER: Has NOT placed order since starting flow
FILTER: Has NOT been in this flow in last 7 days
  ↓
CONDITIONAL SPLIT: Is in Welcome Series (Track A)?
  YES → Delay 4 hours (avoid Smart Sending conflict with welcome flow)
  NO  → Continue immediately
  ↓
⏱️ Wait 1 hour
  ↓
📧 Send AC1 (Reminder)
  ↓
CONDITIONAL SPLIT: Has placed order?
  YES → EXIT FLOW
  NO  → Continue
  ↓
⏱️ Wait 23 hours (total: 24 hours from cart)
  ↓
📧 Send AC2 (Objection Handling)
  ↓
CONDITIONAL SPLIT: Has placed order?
  YES → EXIT FLOW
  NO  → Continue
  ↓
⏱️ Wait 48 hours (total: 72 hours from cart)
  ↓
📧 Send AC3 (Last Chance + Free Shipping)
  ↓
END FLOW
```

### Critical Filters

| Filter | Why |
|--------|-----|
| Placed Order → EXIT | Never send cart reminder to someone who already bought |
| Not in flow within 7 days | Prevent repeat abandoners from getting the same sequence back-to-back |
| Welcome flow check | Avoid Smart Sending suppression by delaying AC1 if welcome email was sent recently |
| Subscription status check | If customer is already a subscriber, skip free shipping offer (they already get it) |

[Confidence: A | Source: Klaviyo flow configuration best practices]

---

## 5. Abandoned Checkout Flow (U1 — Separate from Cart)

**Critical distinction**: Shopify fires TWO different events:
- **Added to Cart** → triggers the Cart Abandonment flow above
- **Checkout Started** → triggers the Abandoned Checkout flow below

Checkout abandoners have **HIGHER purchase intent** (they entered payment/shipping info). They need a faster, more direct sequence:

| Email | Timing | Strategy | Discount? |
|-------|--------|----------|-----------|
| CO1 | **15 minutes** | Direct reminder — you're almost done | No |
| CO2 | 4 hours | Trust reinforcement — guarantee, security badges | No |
| CO3 | 24 hours | Final push — auto-applied free shipping | Yes (auto-applied) |

**Why 15 minutes, not 1 hour**: Checkout abandoners are mid-purchase. The #1 reason for checkout abandonment is distraction, not indecision. A 15-minute reminder catches them while intent is still hot. [Confidence: B | Source: Klaviyo checkout flow recommendations]

### Klaviyo Setup

```
TRIGGER: Started Checkout
  ↓
FILTER: Has NOT placed order since starting flow
FILTER: Has NOT been in Cart Abandonment flow in last 24 hours
  ↓
⏱️ Wait 15 minutes
  ↓
📧 Send CO1 (Almost Done)
  ↓
CONDITIONAL SPLIT: Has placed order?
  YES → EXIT
  NO  → Wait 3.75 hours (total: 4 hours)
  ↓
📧 Send CO2 (Trust)
  ↓
CONDITIONAL SPLIT: Has placed order?
  YES → EXIT
  NO  → Wait 20 hours (total: 24 hours)
  ↓
📧 Send CO3 (Final + Free Shipping)
  ↓
END FLOW
```

**Conflict rule**: If a customer triggers BOTH Cart Abandonment AND Checkout Abandonment, Checkout takes priority. Suppress Cart Abandonment flow for that session. [Confidence: A | Source: Klaviyo flow priority logic]

---

## 6. Browse Abandonment (Phase 2 — Defer to Month 2)

**Do NOT build at launch.** Browse abandonment captures visitors who viewed a product page but didn't add to cart. It's the 3rd highest-performing flow after cart and welcome, but:

- Lower intent than cart abandonment → lower conversion (~1% vs 3.33%)
- Requires sufficient traffic volume to generate meaningful flow entries
- At launch, focus on the 3 core flows (welcome, cart, post-purchase)

### When to Build

**Build browse abandonment in Month 2** when:
1. Core 3 flows are live and generating data
2. Product page traffic exceeds 500 unique visitors/month
3. You have Klaviyo tracking pixel properly configured

### Browse Abandonment Structure (for future reference)

| Email | Timing | Content |
|-------|--------|---------|
| BA1 | 24 hours after product page view, no cart | Product highlight + key benefit + social proof snippet |
| BA2 | 72 hours | Testimonial-led, different angle, soft CTA |

**Target metrics**: Cart creation rate >5%, RPR >$1.00 [Confidence: B | Source: Klaviyo browse abandonment benchmarks]

### Set Up Tracking Now (U8)

Even though browse abandonment flow is deferred to Month 2, **configure the Klaviyo "Viewed Product" event tracking at launch**. This means:
- Install Klaviyo tracking snippet on all product pages (Day 1)
- Verify "Viewed Product" events fire in Klaviyo Activity Feed
- When you build the flow in Month 2, you'll have 4+ weeks of behavioral data to optimize against

[Confidence: A | Source: Klaviyo tracking setup best practice]

---

## 8. Performance Benchmarks & Optimization

### Monthly Review Checklist

| Metric | Check | Action If Below Target |
|--------|-------|----------------------|
| Recovery rate | >5% (of flow recipients) | Test subject lines, add/adjust discount |
| Open rate | >50% | Test subject lines, check deliverability |
| Click rate | >8% | Test CTA placement, button copy, email length |
| Revenue per recipient | >$5.00 | Test product recommendations, pricing display |
| Unsubscribe rate | <0.5% per email | Reduce frequency, check tone |

### A/B Testing Priority Order

1. **AC1 subject line** (highest volume, most impact) — test "You left something behind" vs. "Still want this?"
2. **AC3 incentive type** — free shipping vs. 10% off vs. no discount
3. **AC2 objection order** — test which FAQ question appears first
4. **Timing** — 30 min vs. 1 hr for AC1 (Klaviyo data suggests 30-60 min optimal)

---

## 9. Cross-TUP References

- **M17 email_flow_architecture.md**: Cart recovery is Priority 1 flow. Build before launch.
- **M17 sms_strategy.md**: SMS cart recovery (1 SMS at 48hr after Email 2) deferred to Month 3+ when 500+ SMS subscribers.
- **M9 tracking_and_attribution.md**: Cart recovery revenue tracked via MER, not platform ROAS.
- **M30 Analytics**: Cart recovery rate is one of MVD 7 daily metrics (flow performance).

---

*Cart recovery is the highest-revenue email flow. Build it before launch alongside welcome series. See `post_purchase_and_retention.md` for the next flow priority.*


---

### 📄 dialogue_summary.md

# M18 Dialogue Summary — Email Lifecycle Flows

**Rounds**: 6 (to saturation)
**Personas**: 3 (Klaviyo Flow Architect, D2C Email Copywriter, Retention Strategist)
**Upgrades**: 14
**Unresolved**: 0

---

## Key Themes

1. **Two welcome tracks are non-negotiable** — Subscriber (non-purchaser) vs. Purchaser must be completely separate flows with distinct messaging
2. **Founder voice everywhere** — "Nilo" not "The IonWave Team" across all flows. First-person increases reply rates 2-3x for D2C brands under $5M ARR
3. **Cart ≠ Checkout** — Shopify fires separate events. Checkout abandoners have higher intent and need a faster sequence (15 min vs 1 hr)
4. **Domain warm-up is non-optional** — New sending domain needs 2-4 week gradual volume increase. Blasting full list on Day 1 = spam trap
5. **Subscription conversion needs orchestration** — Single biggest revenue lever. Decision tree maps every touchpoint across all flows
6. **Pre-churn beats win-back** — Catching a cancel/payment failure immediately (1-2 hours) is far more effective than waiting 60 days for win-back
7. **Engagement segments protect deliverability** — Campaign emails target Engaged 30d/90d only. Never send campaigns to unengaged subscribers
8. **Single-question surveys get 3-4x responses** — PP7 reduced from 3 questions to 1. Creates testimonial flywheel.

## Upgrade Registry

| # | Upgrade | Persona | Applied To |
|---|---------|---------|-----------|
| U1 | Abandoned Checkout flow (separate trigger, 15-min) | Klaviyo Architect | cart_recovery.md |
| U2 | Founder voice ("Nilo") throughout all flows | Copywriter | All 4 files |
| U3 | PP6/PP7 moved from flow to campaign sends | Retention Strategist | post_purchase_and_retention.md |
| U4 | Klaviyo consent status + flow_status profile properties | Klaviyo Architect | welcome_and_nurture.md |
| U5 | AC2 objection rewrite: lead with result, not science defense | Copywriter | cart_recovery.md |
| U6 | AC3 auto-apply free shipping (no code friction) | Copywriter | cart_recovery.md |
| U7 | Pre-churn intervention (cancel/payment failure triggers) | Retention Strategist | winback_and_lifecycle.md |
| U8 | Viewed Product tracking from Day 1 (for Month 2 browse flow) | Klaviyo Architect | cart_recovery.md |
| U9 | PP5 statistics flagged as aspirational (Confidence: D) | Copywriter | post_purchase_and_retention.md |
| U10 | Subscription Conversion Decision Tree | Retention Strategist | post_purchase_and_retention.md |
| U11 | Engagement segments for campaign targeting (30d/90d) | Klaviyo Architect | winback_and_lifecycle.md |
| U12 | Standardize founder voice across all flow emails | Copywriter | All 4 files |
| U13 | Domain warm-up protocol (2-4 week ramp) | Klaviyo Architect | welcome_and_nurture.md |
| U14 | Single-question survey for 3-4x response rate | Retention Strategist | post_purchase_and_retention.md |


---

### 📄 opkit_email_lifecycle_flows.md

# OpKit: Email Lifecycle Flows

**ID**: OK-M18-001
**Source TUP**: M18 — Email Lifecycle Flows
**Version**: 1.0.0
**Date**: 2026-02-09
**Quality**: 8.7/10

---

## Purpose

Build a complete email lifecycle automation system for a D2C subscription brand using Klaviyo. Covers welcome flows, cart recovery, post-purchase retention, win-back, and list hygiene — from pre-launch setup through Month 6 maturity.

---

## Instructions (14 Steps)

### Pre-Launch (Week -4 to -1)

1. **Set up email authentication** — SPF, DKIM, DMARC. Separate marketing and transactional sending domains. Verify in Google Postmaster Tools and Yahoo Sender Hub.

2. **Configure Klaviyo tracking** — Install tracking snippet on all pages. Verify "Viewed Product", "Added to Cart", "Started Checkout", and "Placed Order" events fire correctly.

3. **Build Welcome Flow (Track A — Subscribers)** — 5-7 email sequence for non-purchasers. Immediate → Day 1 → Day 3 → Day 5 → Day 7 → Day 10 → Day 14. Educate → social proof → offer → urgency. Use founder voice.

4. **Build Welcome Flow (Track B — Purchasers)** — 5 email sequence for first-time buyers. Immediate → Day 1 → Day 3 → Day 5 → Day 7. Confirm → ritual guide → brand story → social proof → check-in. Use founder voice.

5. **Build Cart Abandonment Flow** — 3 emails. 1hr (reminder) → 24hr (objection handling) → 72hr (incentive). No discount in Email 1. Auto-apply free shipping in Email 3 (no code friction).

6. **Build Checkout Abandonment Flow** — 3 emails. 15min (fast reminder) → 4hr (trust) → 24hr (incentive). Separate from cart flow — higher intent, faster cadence.

7. **Build Basic Post-Purchase Flow** — 4 emails. Day 7 (check-in) → Day 14 (science) → Day 21 (subscription reminder) → Day 25 (review request). Expand to full 5-email flow + campaigns in Month 2.

### Launch Week

8. **Execute domain warm-up** — Start with 200-500 emails/day to most recent opt-ins. Increase by 50% every 2-3 days. Only send flow emails in Week 1. Hold campaigns until Week 2+.

### Month 2-3

9. **Build Browse Abandonment Flow** — 2 emails. 24hr → 72hr. Requires Viewed Product tracking (set up in Step 2) and >500 monthly product page visitors.

10. **Build Replenishment Flow** — 3 emails for non-subscribers. Day 23 → Day 28 → Day 30 from purchase. Subscription pitch at each touchpoint.

11. **Build Win-Back Flow** — 4 emails. Day 60 → Day 75 → Day 90 → Day 105. Discount escalation: none → 15% → 25% → 25% (final). Include sunset warning in Email 4.

### Month 4-6

12. **Build Pre-Churn Intervention** — Triggered by subscription cancel or payment failure events. Within 1-2 hours. Segment by cancel reason for personalized retention offers.

13. **Implement Sunset/List Hygiene** — Define engagement tiers (Champion → Active → Waning → Dormant → Lapsed). Automate re-engagement and suppression. Run monthly.

14. **Create Engagement Segments** — Engaged 30d, Engaged 90d, VIP, Unengaged 90d+. Target all campaign sends to Engaged 30d minimum. Never send campaigns to unengaged subscribers.

---

## Grading Rubric

| Grade | Criteria |
|-------|----------|
| **A (9-10)** | All 13 flows built. Engagement segments active. Domain reputation >90%. Flow revenue >30% of total email revenue. Recovery rate >5%. Subscription conversion >12%. |
| **B (7-8)** | P1 and P2 flows built. Engagement segments active. Authentication complete. Flow revenue >20% of total email revenue. Recovery rate >3%. |
| **C (5-6)** | P1 flows built (welcome, cart, basic post-purchase). Authentication complete. Some performance tracking but no optimization. |
| **D (3-4)** | 1-2 flows built. Authentication incomplete. No engagement segments. No domain warm-up. |
| **F (0-2)** | No automated flows. Sending campaigns to full list. Authentication not configured. |

---

## Scaffold (4 Files)

| File | Contents |
|------|----------|
| `welcome_and_nurture.md` | Track A (subscriber) + Track B (purchaser) welcome flows, email copy, deliverability requirements, domain warm-up protocol |
| `cart_recovery.md` | Cart abandonment + checkout abandonment flows, email copy, browse abandonment plan, discount escalation rules |
| `post_purchase_and_retention.md` | Post-purchase onboarding (7 emails), replenishment flow, review solicitation, subscription conversion decision tree |
| `winback_and_lifecycle.md` | Win-back sequence, pre-churn intervention, sunset/list hygiene, master lifecycle automation map, engagement segments |

---

## IonWave Graded Example: 8.7/10

**What IonWave did well**:
- Two distinct welcome tracks (subscriber vs. purchaser) with clear segmentation
- Fully written IonWave-specific email copy (not just templates) with founder voice
- Subscription Conversion Decision Tree orchestrating all touchpoints
- Domain warm-up protocol for new sending domain
- Pre-churn intervention for subscription cancel/payment failure
- Engagement segments (30d/90d) for campaign targeting

**What could be improved**:
- PP5 statistics are aspirational (Confidence: D) — need validation from actual customer data
- No email design/layout specifications (text-only content, no visual hierarchy guidance)
- Browse abandonment deferred — could lose early traffic

---

## Adaptation Guide

### For Non-Subscription D2C
- Remove replenishment flow and subscription conversion decision tree
- Replace PP3 (subscription reminder) with cross-sell/upsell
- Win-back trigger stays at 60-90 days but without subscription-specific offers
- Add post-purchase cross-sell flow (complementary products)

### For Multi-SKU Brands
- Add product-specific welcome content (conditional on which product was purchased)
- Browse abandonment becomes more valuable (multiple products to recommend)
- Post-purchase cross-sell flow is critical (Day 7-14 after purchase)
- Replenishment timing varies by product — use product-level supply duration

### For High-AOV / Considered Purchase
- Extend welcome series to 10-14 days (longer consideration period)
- Add abandoned cart Email 4 (Day 5-6, different format: founder note or FAQ)
- Review request timing: Day 21-30 (more time to evaluate)
- Win-back discount escalation can be more aggressive (higher margins allow it)

### For International Brands
- Add Consent Mode v2 for EU traffic (GDPR opt-in requirements)
- Quiet hours vary by timezone — Klaviyo handles per-recipient local time
- TCPA applies to US only. Other countries have different SMS regulations
- Consider language-specific flows if serving multiple markets

---

## Universal Principles

1. **Two welcome tracks**: Subscriber and purchaser are fundamentally different audiences. Never merge them.
2. **No discount in cart Email 1**: Simple reminder converts 20-25% of recoveries. Discounts in Email 1 train abandonment behavior.
3. **Auto-apply, never require codes**: Pre-applied incentives convert 15-20% better than discount codes.
4. **Founder voice always**: First-person ("I" not "we") for all marketing flows. "The Team" is for transactional only.
5. **Domain warm-up is not optional**: New domain + full blast = spam folder for months.
6. **Engagement segments protect everything**: Never send campaigns to unengaged subscribers. Deliverability is a shared resource.
7. **Pre-churn > win-back**: Catching a cancel within 2 hours is 10x more effective than waiting 60 days.


---

### 📄 post_purchase_and_retention.md

# M18: Post-Purchase & Retention Email Flows

**TUP**: M18 — Email Lifecycle Flows
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 437, 442, 443; Klaviyo post-purchase benchmarks 2026; M17 email_flow_architecture.md

---

## 1. Post-Purchase Flow Strategy

### Why Post-Purchase Emails Matter

Post-purchase is where IonWave turns a buyer into a subscriber. The 60-day window after first purchase is the highest-leverage retention period:

| Reality | Data |
|---------|------|
| Flow RPR is 20x higher than campaigns | $1.94 avg vs. $0.10 avg [Confidence: B | Source: Klaviyo benchmarks] |
| Automated flows drive 37% of email revenue | From just 2% of send volume [Confidence: B | Source: Omnisend] |
| Review rate target | >15% of customers leave a review [Confidence: C | Source: DTC supplement avg] |
| 30-day retention target | 84% continue subscription past Month 3 [Confidence: C | Source: Danilo tab 437 claim — needs validation] |

### Two-Phase Approach

| Phase | Period | Emails | Focus |
|-------|--------|--------|-------|
| **Phase 1: Onboarding** | Day 0-14 | 4 emails | Confirm → educate → science → check-in |
| **Phase 2: Retention** | Day 15-60 | 3 emails | Subscription management → review → milestone → upsell |

**Product format**: IonWave is a **sachet** (tear, pour, drink — 30 seconds). Not a scoop, not a powder tub. All copy must reference sachet format consistently. [Confidence: A | Source: IonWave product spec, Danilo tab 435]

---

## 2. Phase 1: Onboarding (Day 0-14)

### Flow Structure

| Email | Timing | Subject | Purpose |
|-------|--------|---------|---------|
| PP1 | Day 7 | How's your first week going? | Early check-in, set expectations |
| PP2 | Day 14 | The changes happening inside you | Science-backed education, deepen commitment |
| PP3 | Day 21 | Heads up: box #2 ships in 9 days | Subscription logistics, reduce surprise charges |
| PP4 | Day 25 | Quick favor? Takes 30 seconds. | Review request at peak satisfaction |

**Note**: Order confirmation (immediate) and shipping notification (when shipped) are **transactional emails** handled by Shopify, not Klaviyo flows. Post-purchase flow starts AFTER delivery. [Confidence: A | Source: M17 email_flow_architecture.md]

### Email PP1: First Week Check-In (Day 7)

**Subject**: How's your first week going?
**Preview**: What most people feel by now

---

Hey {{first_name}},

One week of IonWave. Let's check in.

**BY NOW, YOU MIGHT NOTICE:**

→ More stable energy through the day
→ Less of that 3pm crash
→ Subtle improvement in mental clarity
→ Hydration that actually feels different

If you're feeling some of these — great. Your body is responding.

If not yet — that's normal too. Bodies that have been mineral-depleted for years sometimes need 2-3 weeks to fully calibrate.

The key: don't stop. Consistency is everything.

One sachet. Every morning. Let the minerals do their work.

**HOW CAN WE HELP?**

If something's not working, reply to this email. I read everything and respond personally.

You're not just a customer. You're part of this now.

— Nilo

---

### Email PP2: The Science (Day 14)

**Subject**: The changes happening inside you
**Preview**: What 2 weeks of proper mineralization actually does

---

Hey {{first_name}},

Two weeks in. Here's what's happening beneath the surface:

**CELLULAR HYDRATION**
Your cells are finally getting minerals in ionic form — the only form they can actually use. This is different from drinking more water. This is water that works.

**ENZYME ACTIVATION**
Over 300 enzymes in your body require minerals to function. They've been running on fumes. Now they have fuel.

**NERVOUS SYSTEM SUPPORT**
Magnesium, potassium, calcium — these aren't just electrolytes. They're how your neurons fire. Properly mineralized = calmer, clearer, faster.

**RECOVERY OPTIMIZATION**
Your muscles don't just need protein. They need the minerals that power repair at the cellular level.

This isn't hype. This is biochemistry.

And you're two weeks into it.

Keep going. The best changes are still ahead.

— Nilo

P.S. Tracking your health metrics? We'd love to see your before/after. Reply with screenshots if you've got them.

---

### Email PP3: Subscription Reminder (Day 21)

**Subject**: Heads up: box #2 ships in 9 days
**Preview**: Plus: a way to save on your next order

---

Hey {{first_name}},

Quick logistical note:

Your next box of IonWave ships in 9 days.

Same address. Same payment method. Nothing you need to do.

**WANT TO ADD ANYTHING?**

Some customers grab a second box for travel. Or switch to our 3-month bundle for better savings.

**[MANAGE YOUR SUBSCRIPTION →]**

**NEED TO PAUSE OR CHANGE TIMING?**

No problem. You can:
— Push back your next shipment
— Change delivery frequency
— Update your address

All from your account dashboard. No phone calls, no hassle.

**[UPDATE PREFERENCES →]**

Thanks for sticking with it. Three weeks of consistent minerals is when most people really start to feel the difference.

— Nilo

---

### Email PP4: Review Request (Day 25)

**Subject**: Quick favor? Takes 30 seconds.
**Preview**: Your feedback helps more than you know

---

Hey {{first_name}},

You've been with us almost a month now.

Can I ask a quick favor?

If IonWave has made a difference for you — more energy, better recovery, clearer thinking, anything — would you take 30 seconds to leave a review?

**[LEAVE A REVIEW →]**

**WHY IT MATTERS:**

We're a small team. We don't have celebrity endorsers or massive ad budgets.

What we have is customers who feel the difference and tell others about it.

Your review helps someone else take the chance you took a month ago.

Even just a sentence or two helps.

Thank you — seriously.

— Nilo

P.S. Had a problem? Don't leave a bad review — just reply to this email. We'll fix it.

---

## 3. Phase 2: Retention Milestones (Day 30-60)

> **U3 Note**: PP5 (30-day milestone) remains in the post-purchase FLOW because it has a clear trigger (Day 30 from purchase). PP6 (early access) and PP7 (survey) are moved to CAMPAIGN sends because they depend on product availability and business timing, not customer lifecycle timing. Once a subscriber reaches Day 30, they exit the post-purchase flow and enter the regular subscriber email cadence.

### Flow Structure

| Email | Timing | Type | Subject | Purpose |
|-------|--------|------|---------|---------|
| PP5 | Day 30 | **FLOW** | One month in. Here's what we've learned. | Celebrate milestone, upgrade offer |
| PP6 | Month 2+ | **CAMPAIGN** (subscriber segment) | Members-only: new product preview | Early access, VIP treatment |
| PP7 | Month 2+ | **CAMPAIGN** (subscriber segment) | One quick question | Survey, feedback loop |

### Email PP5: 30-Day Milestone

**Subject**: One month in. Here's what we've learned.
**Preview**: Congratulations — and a special offer

---

Hey {{first_name}},

30 days of IonWave.

This is the point where it stops being an experiment and becomes a habit. Your body has had a full cycle to integrate proper mineralization.

**WHAT OUR DATA SHOWS AT 30 DAYS:**

→ 73% of customers report sustained energy improvements
→ 68% report better recovery after workouts
→ 61% report improved sleep quality
→ 84% continue their subscription past month 3

> **⚠️ CONTENT NOTE (U9)**: These statistics are from Danilo tab 437 and are ASPIRATIONAL until validated by actual IonWave customer data. Do NOT use in marketing emails until confirmed by real survey data (target: Month 3 post-launch). Replace with "[X]% of customers report..." placeholders if launching before validation. [Confidence: D | Source: Danilo claim — unverified]

You're part of this now.

**AS A THANK YOU:**

For hitting the 30-day mark, here's an exclusive offer:

**UPGRADE TO 90-DAY SUPPLY**
Save 28% vs monthly
Code: **MONTH1**

**[CLAIM OFFER →]**

Locks in your current price. Ships every 3 months. Less to think about.

Or keep your monthly subscription — either way, we're glad you're here.

Here's to month two.

— Nilo

---

### Email PP6: Early Access / VIP (Day 45)

**Subject**: Members-only: new product preview
**Preview**: You get first access

---

Hey {{first_name}},

Because you're a subscriber, you get first access to this:

**[PRODUCT PREVIEW: IONWAVE MINERAL DROPS]**

Same marine plasma. Travel-size format.

Perfect for:
— Flights (TSA-friendly)
— Hotel stays
— Days you forget your sachet
— Adding to coffee, smoothies, whatever

Launches next month. But you can reserve yours now at founding-member pricing:

**$19 (retail will be $29)**

**[RESERVE NOW →]**

Only available to existing subscribers. Not on our main site.

This is our way of saying thanks for being early.

— Nilo

P.S. Not interested in drops? No worries. Just wanted you to have first shot.

---

### Email PP7: Single-Question Survey (Campaign — Month 2+)

> **U14**: Reduced from 3 questions to 1. Single-question surveys get 3-4x the response rate. Use replies as testimonial content (with permission). This creates a flywheel: survey → testimonial → welcome email social proof.

**Subject**: One quick question
**Preview**: Takes 10 seconds. Your answer shapes what we build.

---

Hey {{first_name}},

You've been using IonWave for a while now. I have one question:

**What's the #1 change you've noticed since starting IonWave?**

Just hit reply and tell me in one sentence. That's it.

Your answer helps us build something better — and helps the next person decide to try it.

— Nilo

P.S. Know someone who should try IonWave? Forward this email and they'll get 15% off their first box with code FRIEND15.

---

## 4. Flow Logic & Technical Configuration

### Klaviyo Flow Setup

```
TRIGGER: Placed Order (first time)
  ↓
FILTER: Order count = 1 (first purchase only)
FILTER: Has NOT been in this flow before
  ↓
CONDITIONAL SPLIT: Is in Welcome Track A?
  YES → EXIT Track A, continue here
  NO  → Continue
  ↓
⏱️ Wait 7 days (from order date)
  ↓
📧 Send PP1 (Week 1 Check-In)
  ↓
⏱️ Wait 7 days (Day 14)
  ↓
📧 Send PP2 (Science)
  ↓
⏱️ Wait 7 days (Day 21)
  ↓
CONDITIONAL SPLIT: Is subscriber?
  YES → 📧 Send PP3 (Subscription Reminder)
  NO  → 📧 Send PP3-ALT (Subscription Pitch)
  ↓
⏱️ Wait 4 days (Day 25)
  ↓
CONDITIONAL SPLIT: Has left a review?
  YES → SKIP review email
  NO  → 📧 Send PP4 (Review Request)
  ↓
⏱️ Wait 5 days (Day 30)
  ↓
📧 Send PP5 (Milestone + Upsell)
  ↓
END FLOW → Customer enters regular subscriber email cadence
  (PP6 and PP7 are CAMPAIGN sends, not flow emails — see U3 note above)
```

### Critical Conditional Splits

| Split | Logic | Why |
|-------|-------|-----|
| First purchase only | Order count = 1 | Repeat buyers get a different (shorter) post-purchase flow |
| Subscriber vs. non-subscriber | PP3 subscription reminder vs. subscription pitch | Different messaging for each |
| Has left review | Skip PP4 if review already submitted | Don't ask twice |
| VIP threshold | After PP7, check if LTV >$150 or orders ≥3 | Route VIPs to referral flow |

---

## 5. Repeat Purchase Post-Purchase (Abbreviated)

Repeat buyers (order count ≥2) get a shortened flow:

| Email | Timing | Content |
|-------|--------|---------|
| RP1 | Day 1 after delivery | Thank you + "have you tried [new product]?" cross-sell |
| RP2 | Day 7 | Review request (if not already reviewed) |
| RP3 | Day 14 | Referral invitation (FRIEND15 code) |

**No onboarding needed** — they already know the product. Focus on cross-sell, review, and referral. [Confidence: B | Source: DTC post-purchase best practice]

---

## 6. Performance Targets

| Metric | Target | How to Measure |
|--------|--------|---------------|
| PP1 reply rate | >5% | Klaviyo metric: replies |
| PP4 review completion | >15% of recipients | Review platform + Klaviyo conversion metric |
| PP5 upgrade rate | >3% of recipients | Subscription plan changes tracked in Shopify |
| PP6 early access conversion | >5% of recipients | Landing page conversion |
| PP7 survey completion | >10% of recipients | Survey tool (Typeform/Google Forms) completion |
| 60-day retention rate | >70% of subscribers | Shopify subscription analytics |

---

## 7. Replenishment Flow (Separate from Post-Purchase)

For customers who purchased a one-time order (NOT subscription):

| Email | Timing | Subject | Strategy |
|-------|--------|---------|----------|
| R1 | Day 23 (7 days before 30-day supply runs out) | Running low on IonWave? | Gentle reminder + subscription pitch |
| R2 | Day 28 (2 days before) | Your minerals are almost gone | Urgency + subscribe & save offer |
| R3 | Day 30 (day of depletion) | Last sachet? Here's 15% off your next box | Discount for reorder |

**Trigger**: Product depletion projection based on purchase date and product supply duration.
**Suppression**: Exclude subscribers (they auto-renew). Exclude anyone who already reordered.
**Click-to-open rate benchmark**: 53.6% (replenishment emails are among the highest-performing flow emails) [Confidence: B | Source: DTC replenishment flow data]

---

## 8. Subscription Conversion Decision Tree (U10)

Every touchpoint where subscription is mentioned must follow a consistent escalation logic. This is the single biggest revenue lever for a consumable supplement brand:

```
FIRST PURCHASE
  ↓
Is subscriber already? ─── YES → Skip to Retention track (PP1-PP5)
  │
  NO
  ↓
PP3 (Day 21): Soft subscription mention
  "Switch to 3-month bundle for better savings"
  ↓
Replenishment R1 (Day 23): Subscription pitch alongside reorder
  "Subscribe & save [X]%"
  ↓
PP5 (Day 30): 90-day upgrade offer
  "Save 28% vs monthly" + Code: MONTH1
  ↓
Replenishment R3 (Day 30): Discount for one-time reorder
  "15% off your next box"
  ↓
SECOND PURCHASE
  ↓
Subscription Offer flow (Day 1 after 2nd order):
  "You've reordered twice. Lock in your price with a subscription."
  ↓
Subscription Offer flow (Day 5 after 2nd order):
  Value comparison: Subscription vs. one-time (show total cost over 6 months)
  ↓
STILL NOT SUBSCRIBED after 2nd purchase?
  ↓
Continue one-time replenishment cycle. Do NOT hard-sell subscription.
Wait for natural 3rd purchase → VIP Recognition flow → Subscription is implied.
```

**Rules**:
1. Never mention subscription more than once per email
2. Always frame as saving money/convenience, never as commitment
3. One-time buyers are valid customers — don't make them feel lesser
4. After 3 failed subscription pitches across different flows, stop pitching for 60 days

[Confidence: B | Source: DTC subscription conversion best practices + Retention Strategist dialogue]

---

## 9. Cross-TUP References

- **M17 email_flow_architecture.md**: Post-purchase is Priority 1, Phase 2 flow. Build basic version (PP1-PP3) at launch, expand to PP4-PP7 in Month 2.
- **M19** (Subscription): PP3/PP5 subscription management and upsell must align with subscription pricing and portal UX.
- **M9 store_setup_and_launch.md**: Subscription toggle UX (per M9 U8) — toggle > dropdown, sub price first.
- **M21** (Customer Experience): PP1 check-in and PP7 survey feed CX feedback loop.
- **M30** (Analytics): Post-purchase flow revenue and retention metrics feed MVD reporting.

---

*Post-purchase flows turn buyers into subscribers. Build PP1-PP3 at launch, expand to full 7-email sequence by Month 2. See `winback_and_lifecycle.md` for the final flow set.*


---

### 📄 welcome_and_nurture.md

# M18: Welcome & Nurture Email Flows

**TUP**: M18 — Email Lifecycle Flows
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 435, 438, 439; Klaviyo flow best practices 2026; M17 email_flow_architecture.md

---

## 1. Two Welcome Tracks (Critical Distinction)

IonWave has TWO distinct welcome audiences that must NEVER receive the same flow:

| Track | Trigger | Goal | Sequence |
|-------|---------|------|----------|
| **Track A: Subscriber Welcome** | Email opt-in (popup/lead magnet), NO purchase | Convert to first purchase | 5-7 emails over 10-14 days — educate → social proof → offer → urgency |
| **Track B: Purchaser Welcome** | First purchase completed | Onboard, reduce buyer's remorse, build habit | 5 emails over 7 days — usage ritual → brand story → community → check-in |

**Klaviyo Implementation**: Use conditional split at flow entry. "Has placed order = YES" → Track B. "Has placed order = NO" → Track A. [Confidence: A | Source: Klaviyo flow architecture]

**Rule**: If a Track A subscriber makes a purchase during the welcome flow, EXIT them from Track A and enter them into Track B (post-purchase). Never send "still thinking about it?" to someone who already bought. [Confidence: A | Source: DTC email best practice]

### Klaviyo Profile Properties (U4)

At flow entry, set these profile properties for flow conflict resolution:

| Property | Value | Purpose |
|----------|-------|---------|
| `flow_status` | `welcome_a_active` or `welcome_b_active` | Other flows check this to delay/skip |
| `consent_status` | Must = `subscribed` | 2026 Klaviyo requirement — verify at every flow entry |
| `welcome_completed_date` | Date of last email in flow | Used by campaign targeting to avoid over-sending to new subscribers |

Clear `flow_status` at flow exit (purchase or completion). [Confidence: A | Source: Klaviyo consent requirements 2026]

---

## 2. Track A: Subscriber Welcome Series (Non-Purchasers)

**Purpose**: Convert email subscribers who haven't bought yet.
**Source**: Danilo tabs 438, 439 (generic templates — adapted for IonWave)

### Flow Structure

| Email | Timing | Subject | Purpose | CTA | Discount? |
|-------|--------|---------|---------|-----|-----------|
| W1 | Immediate | Welcome to IonWave — here's your [X]% off | Deliver promise, set expectations | Shop Now | Yes (popup offer) |
| W2 | Day 1 | Why 78 minerals beats 3 | Education, differentiation | Learn More | No |
| W3 | Day 3 | {{first_name}}, real results from real people | Social proof, soft sell | Shop Now | No |
| W4 | Day 5 | What [customer_name] said about IonWave | Deeper social proof, testimonials | Shop Now | No |
| W5 | Day 7 | Your exclusive offer expires soon | Conversion push | Buy Now | Yes (original offer) |
| W6 | Day 10 | Still thinking about it? (let me answer that) | Objection handling | Buy Now | Optional 5% bump |
| W7 | Day 14 | Last chance: your [X]% off expires tonight | Final conversion | Buy Now | Yes (final) |

[Confidence: B | Source: Danilo tabs 438/439 + Klaviyo DTC welcome benchmarks]

### Email W1: Welcome (Template)

**Subject**: Welcome to IonWave — here's your {{discount_code_value}}% off
**Preview**: Your journey to real hydration starts now

---

Hey {{first_name}},

Welcome! You just joined {{subscriber_count}} people who are done feeling tired, foggy, and dehydrated.

As promised, here's your exclusive code: **{{discount_code}}**

Quick intro — IonWave is different because:

- 78 ocean-sourced minerals (not 3-4 synthetic ones)
- Zero sugar, zero junk
- Actually hydrates your cells (98% bioavailable vs ~10% for pills)

Over the next few days, I'll share:
- Why most electrolytes don't actually work
- Real stories from customers who finally feel energized
- The science behind ocean-sourced minerals

For now, use code **{{discount_code}}** for {{discount_code_value}}% off your first order.

**[CTA: Shop Now]**

Talk soon,
{{founder_name}}

P.S. This code expires in 7 days. Don't miss out.

---

### Key Rules for Track A

1. **Exit condition**: If subscriber places an order at ANY point → exit flow, enter Post-Purchase (Track B)
2. **Smart Sending**: Set to 16 hours minimum between emails to prevent overlap with other flows
3. **Suppression**: Exclude anyone who has already purchased (profile filter at flow entry)
4. **A/B test priority**: Subject lines on W1 (highest volume), then CTA placement on W5 (highest conversion intent)

---

## 3. Track B: Purchaser Welcome Series (First-Time Buyers)

**Purpose**: Onboard new customer, establish daily ritual, reduce buyer's remorse, build brand connection.
**Source**: Danilo tab 435 (IonWave-specific, fully written copy)

### Flow Structure

| Email | Timing | Subject | Purpose | Key Content |
|-------|--------|---------|---------|-------------|
| B1 | Immediate (order confirm) | Your minerals are on the way 🌊 | Confirm, set expectations | Order details + morning ritual instruction |
| B2 | Day 1 (getting started) | How to get the most from your first sachet | Usage guide, what to expect | The IonWave Ritual (30-second ritual), day-by-day timeline |
| B3 | Day 3 (brand story) | Why we started IonWave (the real reason) | Build connection, credibility | René Quinton discovery, 78 minerals, anti-synthetic positioning |
| B4 | Day 5 (social proof) | What our community is saying | Validate purchase decision | 4 customer testimonials with names + cities |
| B5 | Day 7 (check-in) | Quick check-in: how's it going? | Gather feedback, support | Expected results at 1 week, reply request for engagement |

[Confidence: A | Source: Danilo tab 435 — fully written IonWave copy]

### Email B1: Order Confirmation / Welcome

**Subject**: Your minerals are on the way 🌊
**Preview**: Here's what to expect (and what to do first)

---

Hey {{first_name}},

Your IonWave is officially on its way.

**Order #{{order_number}}**
{{product_name}} — {{quantity}}

You should receive tracking info within 24 hours, and your box will arrive in 3-5 business days.

**WHILE YOU WAIT:**

Before your first sachet arrives, here's the one thing that makes the biggest difference:

> Take it first thing in the morning. Empty stomach. Before coffee.

This gives your body the best window for absorption. Most customers who feel the difference fastest follow this ritual.

That's it. Tear, pour, drink. 30 seconds.

We're excited to have you. Welcome to IonWave.

— Nilo

P.S. Questions before your box arrives? Just reply to this email. We read everything.

---

### Email B2: Getting Started Guide

**Subject**: How to get the most from your first sachet
**Preview**: The 30-second ritual that changes everything

---

Hey {{first_name}},

Your box should be arriving soon (or maybe it's already there).

Here's how to make the most of it:

**THE IONWAVE RITUAL:**
- ☀️ Morning, empty stomach
- 💧 8oz water (room temp or cold)
- 📦 Tear one sachet
- ⏱️ Drink immediately

That's the whole thing. 30 seconds.

**WHAT TO EXPECT:**

| Timeline | What You'll Notice |
|----------|-------------------|
| **Day 1-3** | Subtle shifts — slightly more stable energy, less afternoon fog |
| **Day 4-14** | Real changes — more consistent energy, better recovery, clearer thinking |
| **Day 15-30** | Full system integration — this is what proper mineralization feels like |

The key is consistency. One sachet, every day. Don't skip.

Your body has been running on depleted minerals for years. Give it 30 days to remember what balanced feels like.

Talk soon,
Nilo

---

### Email B3: Brand Story

**Subject**: Why we started IonWave (the real reason)
**Preview**: It started with a 125-year-old discovery...

---

Hey {{first_name}},

Quick story about why IonWave exists.

In 1897, a French scientist named René Quinton discovered something extraordinary: human blood plasma is 98% identical to seawater. Same minerals. Same ratios. Same ionic structure.

He spent the rest of his life proving that marine plasma could restore mineral balance in the human body. French hospitals used it for decades. The research is solid.

So why hasn't everyone heard of this?

Because the supplement industry makes more money selling synthetic pills. Isolated compounds that cost pennies to produce, marked up 10x.

Marine plasma doesn't fit that model. It's harder to source. Harder to standardize. Can't be patented.

But it's what your body actually recognizes.

That's why we started IonWave. Not to create another supplement brand. To make Quinton's discovery accessible to anyone who wants to feel the difference.

78 minerals. Harvested from 30 meters below the ocean surface. The same form your body has used for millions of years.

No synthetic shortcuts. No factory compounds. Just pure ocean minerals.

We're glad you're here.

— Nilo

P.S. Want to go deeper? Here's the research: [LINK TO SCIENCE PAGE]

---

### Email B4: Social Proof

**Subject**: What our community is saying
**Preview**: Real results from real people

---

Hey {{first_name}},

You've been using IonWave for a few days now. Curious how others describe the experience?

---

> "I've tried every electrolyte brand. LMNT, Drip Drop, all of them. IonWave is the first one where I actually FELT different. My HRV is up, my energy is stable, and I cancelled three other supplements."
> — Marcus T., Austin

> "As a trainer, I recommend this to all my clients now. The difference in their recovery is visible."
> — Jennifer R., Los Angeles

> "I was skeptical. But three weeks in, my afternoon fatigue is gone. Just gone."
> — David K., New York

> "My sleep score went up 12 points in two weeks. Only thing I changed was adding IonWave in the morning."
> — Sarah M., Denver

---

Everyone's body is different. But if you're consistent — one sachet, every morning — you'll likely start noticing your own version of these results.

Keep going.

— Nilo

---

### Email B5: One-Week Check-In

**Subject**: Quick check-in: how's it going?
**Preview**: We want to hear from you

---

Hey {{first_name}},

One week in. How are you feeling?

**BY NOW, MOST PEOPLE NOTICE:**

✓ More stable energy (fewer crashes)
✓ Less brain fog, especially afternoon
✓ Better hydration that actually lasts
✓ Subtle but real improvement in recovery

If you're feeling these things — amazing. It means your body is responding to proper mineralization.

If you're not feeling much yet — that's okay too.

Some bodies take 2-3 weeks to fully respond, especially if you've been mineral-depleted for a long time. Stick with it. The changes are cumulative.

**ONE REQUEST:**

Hit reply and tell me one thing you've noticed. Good, bad, or just different.

I read every response. And your feedback helps us make IonWave better for everyone.

Here's to week two.

— Nilo

P.S. Running low? Your subscription automatically renews, so you'll never miss a day. Need to adjust your delivery schedule? [Manage Subscription]

---

## 4. Deliverability Requirements (2026)

Before ANY flow goes live, complete this authentication checklist:

| Requirement | Status | Notes |
|-------------|--------|-------|
| SPF record published | [ ] | List all authorized sending IPs in DNS |
| DKIM enabled | [ ] | Required by Gmail for all bulk senders (2024+) |
| DMARC policy set | [ ] | Minimum p=none. Align both SPF and DKIM |
| One-click unsubscribe header | [ ] | RFC 8058 List-Unsubscribe required for 5,000+ daily sends |
| Separate sending domains | [ ] | marketing@ionwave vs. orders@ionwave (transactional isolation) |
| Spam rate monitoring | [ ] | Google Postmaster Tools. Target: <0.1%. Hard limit: <0.3% |

[Confidence: A | Source: Google/Yahoo sender guidelines 2024-2026, enforced Nov 2025+]

**Microsoft enforcement**: As of May 2025, Outlook.com, Hotmail, and Live.com also enforce DKIM/DMARC. Triple-threat compliance is now table stakes. [Confidence: A | Source: Microsoft sender requirements 2025]

### Domain Warm-Up Protocol (U13)

**Do NOT blast your full list from a new sending domain on Day 1.** New Klaviyo accounts on a new domain need a 2-4 week gradual volume increase:

| Day | Daily Send Volume | Target Audience |
|-----|------------------|-----------------|
| Day 1-3 | 200-500 | Most recent opt-ins only (highest engagement probability) |
| Day 4-6 | 500-1,000 | Expand to all opt-ins from last 7 days |
| Day 7-10 | 1,000-2,500 | All engaged subscribers |
| Day 11-14 | 2,500-5,000 | Full list (if you have that many) |
| Day 15+ | Full volume | Normal sending cadence |

**Increase by ~50% every 2-3 days.** If bounce rate exceeds 5% or spam complaints exceed 0.1% at any step, pause for 48 hours and reduce volume.

**At launch**: Only send flow emails (welcome, cart, post-purchase) during Week 1. These are triggered by high-intent actions and have the best engagement rates, which builds domain reputation. Hold campaign sends until Week 2+. [Confidence: A | Source: ESP domain warm-up best practices]

---

## 5. Performance Targets

| Metric | Welcome Track A | Welcome Track B | Source |
|--------|----------------|----------------|--------|
| Open Rate | >45% | >55% | [Confidence: B | Klaviyo DTC health/wellness avg] |
| Click Rate | >3% | >5% | [Confidence: B | Klaviyo flow benchmarks] |
| First Purchase CVR (Track A) | >8% | N/A | [Confidence: B | Klaviyo DTC avg] |
| Unsubscribe Rate | <1% | <0.5% | [Confidence: B | Industry benchmark] |
| Reply Rate (B5 check-in) | >3% | >3% | [Confidence: C | DTC supplement heuristic] |

**Note on open rates**: Apple Mail Privacy Protection (46% of email clients) inflates open rates by ~18 points. Use click rate and conversion rate as primary performance indicators. [Confidence: A | Source: Apple MPP data]

---

## 6. Cross-TUP References

- **M17 email_flow_architecture.md**: Master lifecycle stages, flow build order, priority framework. M18 provides the actual email content within M17's architecture.
- **M17 sms_strategy.md**: SMS is a separate channel (defer to Month 3+). No SMS in welcome flows.
- **M19** (Subscription): Track B, Email B5 references subscription management. Subscription UX per M9 store_setup_and_launch.md.
- **M16** (Customer Acquisition): Subscriber welcome (Track A) is the bridge between acquisition and first purchase.

---

*Welcome flows are the highest-leverage email investment at launch. Build Track A and Track B before anything else. See `cart_recovery.md` for the next priority flow.*


---

### 📄 winback_and_lifecycle.md

# M18: Win-Back & Lifecycle Automation

**TUP**: M18 — Email Lifecycle Flows
**Version**: 1.0.0
**Date**: 2026-02-09
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 444, 445, 446; Klaviyo win-back benchmarks 2026; M17 email_flow_architecture.md

---

## 1. Win-Back Flow Strategy

### When to Trigger Win-Back

For a supplement brand with a 30-day product cycle:

| Inactivity | Status | Action |
|------------|--------|--------|
| 0-30 days | Normal purchase cycle | No action needed |
| 30-60 days | Missed one reorder | Replenishment flow handles this (see post_purchase_and_retention.md) |
| **60 days** | **Win-back trigger** | **Start win-back flow — they've missed 2 reorders** |
| 90 days | At risk of permanent churn | Final win-back attempt |
| 120 days | Lapsed | Sunset evaluation |

**IonWave recommendation**: Trigger win-back at **60 days** of no purchase (not 90). For a 30-day consumable, 60 days = 2 missed reorder windows. The customer is actively disengaging. [Confidence: B | Source: Klaviyo DTC supplement heuristic + Danilo tabs 444/445]

### Win-Back Performance Benchmarks

| Metric | Average | IonWave Target |
|--------|---------|----------------|
| Win-back open rate | Up to 57% | >40% |
| Win-back click rate | Up to 11% | >8% |
| Win-back conversion rate | 2-5% | >5% |
| Re-acquisition cost vs. new | 5x cheaper | Track via MER |

[Confidence: B | Source: Klaviyo + Omnisend win-back benchmarks]

---

## 2. Win-Back Sequence (4 Emails)

### Flow Structure

| Email | Timing | Subject | Strategy | Incentive |
|-------|--------|---------|----------|-----------|
| WB1 | Day 60 | We miss you, {{first_name}} 💙 | Emotional, remind of value | None |
| WB2 | Day 75 | A lot has changed... | What's new, social proof | 15% off |
| WB3 | Day 90 | {{first_name}}, here's 25% off | Significant discount, strong CTA | 25% off |
| WB4 | Day 105 | Should we say goodbye? | Final attempt, sunset warning | 25% (last chance) |

**Discount escalation is intentional**: Start with emotion (no discount), graduate to highest offer. Segment by LTV for efficiency — high-value customers get the bigger discount earlier. [Confidence: B | Source: DTC win-back best practice]

---

### Email WB1: We Miss You (Day 60)

**Subject**: We miss you, {{first_name}} 💙
**Preview**: It's been a while

---

Hey {{first_name}},

It's been a while since we've seen you.

Everything okay?

Just wanted to check in and remind you that sustained energy and real hydration is just one sachet away.

Come back and try it again:

**[SHOP IONWAVE →]**

Miss having you in the community.

— Nilo

---

### Email WB2: What's New (Day 75)

**Subject**: A lot has changed...
**Preview**: New products, new results, same mission

---

Hey {{first_name}},

Since you've been away, here's what's been happening at IonWave:

**WHAT'S NEW:**
→ [New product/feature 1 — dynamic content block]
→ [Customer milestone — e.g., "10,000 customers" — dynamic content block]
→ [New review/testimonial — dynamic content block]

We've missed having you as part of this.

Here's 15% off to make it easy to come back:

**Code: MISSYOU15**

**[CLAIM 15% OFF →]**

Valid for 14 days.

— Nilo

---

### Email WB3: Big Offer (Day 90)

**Subject**: {{first_name}}, here's 25% off to come back
**Preview**: Our biggest discount — just for you

---

Hey {{first_name}},

I really want you to experience IonWave again.

So here's our biggest discount: **25% off.**

**Code: COMEBACK25**

**[CLAIM 25% OFF →]**

Valid for 7 days only.

— Nilo

P.S. If something wasn't right last time, reply and let me know. I'd love to make it right.

---

### Email WB4: Sunset Warning (Day 105)

**Subject**: Should we say goodbye?
**Preview**: Last chance before we stop emailing

---

Hey {{first_name}},

It's been over 3 months since your last order.

I don't want to keep emailing you if you're not interested anymore. That's not fair to either of us.

**TWO OPTIONS:**

1. **Stay on the list** — click here and I'll keep sending you updates, offers, and health tips: **[YES, KEEP ME →]**

2. **Say goodbye** — no hard feelings. Just don't click anything and we'll quietly remove you from our email list in 7 days.

If you want one more round of IonWave, your **25% off code (COMEBACK25)** is still active for 7 more days.

Either way — thanks for being part of this, even briefly.

— Nilo

---

## 3. Pre-Churn Intervention (U7)

**The gap**: Between replenishment flow (Day 23-30) and win-back (Day 60), there's a full month of silence. If a subscriber cancels or their payment fails, you need an IMMEDIATE response — not a 30-day wait.

### Subscription Cancel / Payment Failure Triggers

| Event | Trigger Source | Response Time | Email |
|-------|---------------|---------------|-------|
| **Payment failure** | Shopify subscription webhook → Klaviyo | Within 1 hour | "Your subscription payment didn't go through" — helpful, not alarming |
| **Subscription cancelled** | Shopify subscription webhook → Klaviyo | Within 2 hours | "We're sorry to see you go" + reason-specific offer |
| **Subscription paused** | Shopify subscription webhook → Klaviyo | Within 24 hours | "Your subscription is paused" + "ready when you are" |

### Cancel Reason Segmentation

When a subscriber cancels, Shopify captures a reason. Use it to personalize the retention email:

| Cancel Reason | Email Response | Offer |
|---------------|---------------|-------|
| "Too expensive" | Downgrade option (smaller quantity, less frequent) | Switch to 60-day cadence or smaller pack |
| "Not seeing results" | Extended timeline education (some bodies take 4-6 weeks) | Free extra 2-week supply |
| "Switching to competitor" | Competitive comparison, unique differentiator (78 minerals vs. 3-4) | 25% off next 2 shipments |
| "Don't need it anymore" | Seasonal offer, gift option | Referral code for friends |
| No reason given | Generic "we miss you" + founder personal note | 15% off to reactivate |

**Klaviyo setup**: Create a flow triggered by `Subscription Cancelled` event. Use conditional split on `cancel_reason` property. Requires Shopify subscription app (Recharge, Skio, or Loop) integration with Klaviyo.

[Confidence: B | Source: DTC subscription churn intervention best practices]

---

## 4. Sunset / List Hygiene Flow

### Why Sunsetting Matters

Only 24% of email marketers have a sunset policy. Having one is a competitive advantage for deliverability. [Confidence: A | Source: Mailjet 2025 report]

| Problem | Impact |
|---------|--------|
| Sending to unengaged subscribers | Lowers domain reputation → emails land in spam for EVERYONE |
| Gmail/Yahoo engagement signals | ISPs use engagement to determine inbox vs. spam placement |
| ESP cost | Klaviyo charges by list size. Dead subscribers = wasted money |
| Apple MPP inflation | Open rates are unreliable. Must use clicks + purchases as engagement signals |

### Engagement Tiers

| Tier | Definition | Action |
|------|-----------|--------|
| **Champion** | Opened/clicked in last 30 days OR purchased in last 60 days | Full email cadence |
| **Active** | Opened/clicked in last 60 days | Full email cadence |
| **Waning** | No opens/clicks in 60-90 days, but has purchased before | Reduce to 1 email/month (best content only) |
| **Dormant** | No opens/clicks in 90-120 days | Enter win-back flow (if not already completed) |
| **Lapsed** | No engagement in 120+ days AND win-back completed with no response | Suppress from all marketing. Keep for transactional only |

[Confidence: B | Source: ESP deliverability best practices + Mailgun sunset policy guides]

### Sunset Process

```
1. IDENTIFY: Segment subscribers with no clicks in 90+ days
                ↓
2. RE-ENGAGE: Send 2-email "Do you still want to hear from us?" series
                ↓
3. EVALUATE: Did they click "Yes, keep me"?
   YES → Move to Active tier, full cadence
   NO  → Continue to Step 4
                ↓
4. SUPPRESS: Move to suppression list (pause all marketing, 30 days)
                ↓
5. FINAL CHECK: Any website visit or purchase in 30-day suppression?
   YES → Reactivate to Waning tier
   NO  → Remove from active marketing list
                ↓
6. RETAIN: Keep in system for transactional emails and compliance records
```

**Frequency**: Run sunset evaluation **monthly**. Build as automated Klaviyo segment + flow. [Confidence: B | Source: ESP best practice]

**Legal note**: Suppress rather than delete. GDPR data minimization + CAN-SPAM compliance records require retaining the relationship record even after marketing suppression.

---

## 5. Master Lifecycle Automation Map

Every automated touchpoint in the customer journey. This is the orchestration layer that connects all M18 flows:

| Automation | Trigger | Stage Transition | Channel | Timing | Goal Metric |
|-----------|---------|-----------------|---------|--------|-------------|
| **Welcome Series** | Email opt-in (no purchase) | Visitor → Subscriber | Email (5-7) | Day 0-14 | First purchase CVR >8% |
| **Abandoned Cart** | Cart created, no purchase 1hr | Subscriber → Buyer intent | Email (3) + SMS (1, Month 3+) | 1hr, 24hr, 72hr | Recovery rate >5% |
| **Browse Abandonment** | Product page view, no cart 24hr | Visitor → Subscriber | Email (2) | 24hr, 72hr | Cart creation rate >5% |
| **Post-Purchase** | First purchase completed | Buyer → Loyal customer | Email (7) | Day 0-60 | NPS >8, Review rate >15% |
| **Replenishment** | Projected product depletion | Buyer → Repeat buyer | Email (3) + SMS (1, Month 3+) | Day 23, 28, 30 | Repeat rate >35% |
| **Subscription Offer** | 2nd purchase completed | Repeat → Subscriber | Email (2) | Day 1, 5 after 2nd order | Sub conversion >12% |
| **VIP Recognition** | 3rd purchase OR $150+ LTV | Subscriber → Advocate | Email (1) + surprise | After qualifying event | Referral opt-in >20% |
| **Referral Activation** | VIP recognized | Advocate → Advocate | Email (2) + in-package card | With VIP email + next shipment | Referral share rate >15% |
| **Review Solicitation** | 14 days post-delivery | Buyer → Advocate | Email (2) + SMS (1, Month 3+) | Day 14, 21, 28 | Review rate >20% |
| **Win-back** | No purchase 60 days | At-Risk → Buyer or Churned | Email (4) + ad retarget | Day 60, 75, 90, 105 | Win-back rate >5% |
| **Sunset** | No email engagement 120 days | Churned → Suppressed | Email (2) | Day 120, 127 | Re-engage >3% or clean |
| **Churn Intervention** | Churn risk score >70 | Subscriber → At-Risk | Email (1) + CS outreach | Within 24hr of trigger | Save rate >15% |

[Confidence: B | Source: Danilo tab 446 + M17 email_flow_architecture.md lifecycle stages]

---

## 6. Flow Priority & Build Schedule

Aligned with M17's Founder Mode principle: build in revenue-impact order.

| Priority | Flow | Build When | Effort |
|----------|------|-----------|--------|
| **P1** | Abandoned Cart | Pre-launch (Week -2) | 3 emails, 2 hours |
| **P1** | Welcome Series (Track A + B) | Pre-launch (Week -2) | 12 emails, 4 hours |
| **P1** | Post-Purchase (basic: PP1-PP3) | Pre-launch (Week -1) | 3 emails, 1 hour |
| **P2** | Post-Purchase (full: PP4-PP7) | Month 1-2 | 4 emails, 2 hours |
| **P2** | Replenishment | Month 2 | 3 emails, 1 hour |
| **P2** | Browse Abandonment | Month 2 (when traffic >500/mo) | 2 emails, 1 hour |
| **P3** | Subscription Offer | Month 2-3 (when repeat buyers exist) | 2 emails, 1 hour |
| **P3** | Win-back | Month 3 (when 60-day cohort exists) | 4 emails, 2 hours |
| **P3** | VIP Recognition | Month 3+ (when VIPs exist) | 1 email + insert, 1 hour |
| **P3** | Referral Activation | Month 3+ (after VIP flow) | 2 emails, 1 hour |
| **P4** | Sunset / List Hygiene | Month 4 (when list >2,000) | 2 emails + automation, 1 hour |
| **P4** | Churn Intervention | Month 6+ (when churn data exists) | 1 email + CS process, 2 hours |
| **P4** | Review Solicitation (dedicated) | Month 2 (supplement PP4) | 3 emails, 1 hour |

**Total**: 42 emails across 13 automated flows. Build P1 in Week -2 to -1. P2 in Month 1-2. P3 in Month 3. P4 in Month 4-6.

---

## 7. Flow Conflict Resolution

When a customer is eligible for multiple flows simultaneously, use these priority rules:

| Conflict | Resolution |
|----------|-----------|
| Welcome + Cart Abandoned | Delay cart AC1 by 4 hours to avoid Smart Sending suppression |
| Post-Purchase + Welcome Track A | EXIT Track A immediately, start Post-Purchase |
| Win-back + Replenishment | Win-back takes priority (60+ day gap means replenishment already failed) |
| Win-back + Sunset | Complete win-back first. If no response → enter sunset |
| Post-Purchase + Review Solicitation | Post-Purchase PP4 IS the review request. Skip dedicated review flow for first-time buyers |
| Any flow + Flash Sale campaign | Campaign sends regardless. Flow emails delay by 24 hours via Smart Sending |

[Confidence: B | Source: Klaviyo Smart Sending documentation + DTC flow architecture best practices]

---

## 8. Engagement Segments for Campaign Targeting (U11)

**Critical deliverability protection**: Flow emails send to everyone (they're triggered by actions). But CAMPAIGN emails (newsletters, promotions, announcements) must ONLY target engaged subscribers.

### Required Klaviyo Segments

| Segment Name | Definition | Use For |
|-------------|-----------|---------|
| **Engaged 30d** | Opened OR clicked in last 30 days, OR purchased in last 30 days | Primary campaign audience. All regular sends target this segment |
| **Engaged 90d** | Opened OR clicked in last 90 days, OR purchased in last 60 days | Extended audience for major announcements, product launches |
| **Unengaged 90d+** | No opens, clicks, OR purchases in 90+ days | NEVER send campaigns. Flow emails only (win-back, sunset) |
| **VIP** | 3+ purchases OR $150+ LTV | Premium offers, early access, referral invitations |
| **Subscribers (Active)** | Active subscription status in Shopify | Subscription-specific communications (PP6, PP7 campaigns) |

### Campaign Targeting Rules

1. **Default campaign audience**: Engaged 30d segment
2. **Product launch / major announcement**: Engaged 90d segment (one-time exception)
3. **Flash sale**: Engaged 30d only (protect deliverability)
4. **Monthly newsletter**: Engaged 90d segment
5. **NEVER**: Send campaigns to full list including unengaged subscribers

**Apple MPP caveat**: Do not rely solely on open rates for engagement. Apple Mail Privacy Protection inflates opens. Weight clicks and purchases higher in segment definitions. [Confidence: A | Source: Klaviyo deliverability best practices + Apple MPP data]

---

## 9. Klaviyo-Specific Technical Notes

### New Klaviyo Features to Leverage (2025-2026)

| Feature | How to Use | Impact |
|---------|-----------|--------|
| **Personalized Send Time** | Enable on all flows — AI optimizes per-recipient timing | +10-15% open rate improvement |
| **Channel Affinity** | AI determines if customer prefers email vs. SMS | Reduces channel fatigue |
| **Exit Conditions** | Auto-stop flow when customer converts | Prevents "buy now" emails after purchase |
| **Multi-Touch Attribution** | Real-time revenue attribution beyond last-click | More accurate flow ROI measurement |
| **AI Image Remix** | Auto-generate email creative variations | Faster A/B testing |

[Confidence: B | Source: Klaviyo product announcements 2025-2026]

### Smart Sending Configuration

| Setting | Value | Why |
|---------|-------|-----|
| Minimum gap between emails | 16 hours | Prevents email fatigue from flow overlaps |
| Campaign override | ON for campaigns, OFF for transactional | Campaigns always send; transactional never suppressed |
| Smart Sending scope | Within flows only | Don't let flow-to-campaign conflicts suppress critical messages |

---

## 10. Cross-TUP References

- **M17 email_flow_architecture.md**: Master lifecycle stages and flow priority framework. M18 provides the email content within M17's architecture.
- **M17 sms_strategy.md**: SMS channel deferred to Month 3+. Win-back is email-only. Cart recovery gets 1 SMS at 48hr (Month 3+).
- **M17 email_winback.md**: M17 has win-back framework. M18 provides the actual IonWave win-back email copy.
- **M9 operations_governance.md**: List hygiene and sunset processes feed into M9's operational cadence (monthly governance).
- **M30** (Analytics): All flow metrics (recovery rate, conversion, RPR) feed MVD dashboard.
- **M19** (Subscription): Subscription offer flow and churn intervention align with M19 subscription model.

---

*Win-back and lifecycle automation complete the email flow ecosystem. Build P1 flows before launch, expand through P4 by Month 6. Total: 42 emails across 13 automated flows.*


---

## 🔗 Dependencies & Relationships

### Feeds Into
- _No downstream dependencies_

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

- **IonWave customer statistics (PP5)**
  - Upgrade Path: Validate with real survey data after Month 3
- **Supplement-specific email benchmarks**
  - Upgrade Path: Track IonWave-specific metrics from Day 1, compare to health/wellness vertical averages
- **Klaviyo AI features effectiveness**
  - Upgrade Path: Test Personalized Send Time and Channel Affinity after 30 days of data
- **Cart vs. Checkout abandonment split performance**
  - Upgrade Path: Measure after first 200 entries in each flow
- **Browse abandonment viability at IonWave scale**
  - Upgrade Path: Evaluate when product page traffic exceeds 500/month

---

## 🎯 Next Actions

_No next actions documented._


---

## 🧰 OpKits

- OK-M18-001

---

---

_Report generated: 2026-02-09 17:49:43_

_Source: `data\m18`_