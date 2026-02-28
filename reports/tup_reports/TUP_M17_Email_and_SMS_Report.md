# TUP M17: Email & SMS

**Status:** migrated | **Quality:** 8.4/10 | **Version:** 1.0.0
**Cluster:** BCL-4 (Retention & Lifecycle)

---

## 📋 Overview

- **Workshop Date:** 2026-02-07
- **Actor:** Caio + Claude (session D)
- **Protocol Used:** TWP-001 v2.0.0
- **Change Type:** initial_workshop

### Workshop Dialogue
- **Personas Used:** Skeptical Investor, Growth Engineer, Operations Expert
- **Rounds:** 7
- **Saturated:** True
- **Upgrades Applied:** 5
- **Unresolved Issues:** 0

### Quality Assessment
- **Score:** 8.4/10
- **Rationale:** All content tab groups filled with graded evidence. Full email sequences with actual copy for 4 major flows. Danilo's aspirational statistics explicitly tagged as [VOID]. FTC compliance gaps flagged. Discount defense policy added. Maintenance time budgeted. 5 dialogue upgrades applied. Main limitations: all benchmarks are industry averages (IonWave data doesn't exist yet), some health claims need legal review.

---

## 📁 Content Files

- 📄 MD **data/m17/email_flow_architecture.md**
- 📄 MD **data/m17/email_segmentation.md**
- 📄 MD **data/m17/email_welcome_series.md**
- 📄 MD **data/m17/email_abandoned_cart.md**
- 📄 MD **data/m17/email_post_purchase.md**
- 📄 MD **data/m17/email_winback.md**
- 📄 MD **data/m17/email_subject_lines.md**
- 📄 MD **data/m17/sms_strategy.md**
- 📄 MD **data/m17/physical_touchpoints.md**
- 📄 MD **data/m17/dialogue_summary.md**
- 📄 MD **data/m17/opkit_email_lifecycle.md**
- 🔧 JSON **data/m17/_meta.json**

---

## 🔧 Structured Data

_JSON files converted to human-readable format_

_No JSON files in this TUP._

---

## 📝 Narrative Content

### 📄 dialogue_summary.md

# M17: Expert Persona Dialogue Summary

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0

---

## Personas

1. **Skeptical Investor** — Financial rigor, ROI validation, margin math
2. **Growth Engineer** — Unit economics, compounding mechanisms, growth loops
3. **Operations Expert** — Scalability, maintenance burden, execution reality

---

## Round Log

### ROUND 1
- **CHALLENGE**: Over-engineered 12-flow email system for a pre-launch brand with 0 customers
- **RESPONSE**: Build order addresses this — only 3 flows at launch. ROI is asymmetric (build once, earn continuously). Cart flow alone pays for Klaviyo after 4 recoveries.
- **SYNTHESIS**: Architecture is sound IF maintenance time is quantified. Solo founder needs to know ongoing hours/month.
- **OUTCOME**: UPGRADED
- **ACTION**: U1 — Added §7 "Maintenance Time Budget" to email_flow_architecture.md (~1.5 hrs/month for 3 launch flows, ~3-4 hrs/month at full 12 flows)

### ROUND 2
- **CHALLENGE**: Discount escalation across flows creates arbitrage — customers learn to abandon carts or lapse to get bigger discounts
- **RESPONSE**: Different incentive types per flow (% off vs. free shipping vs. larger %). Time-gating prevents manipulation (25% off requires 90 days of inactivity).
- **SYNTHESIS**: Margin math confirms profitability even at 25% off ($14.15 net/order). Defense is: never offer bigger discount in a faster flow + no code stacking.
- **OUTCOME**: UPGRADED
- **ACTION**: U2 — Added "Discount Defense Policy" to email_abandoned_cart.md with 5 explicit rules + margin math

### ROUND 3
- **CHALLENGE**: Unverified health claims in post-purchase emails (73% energy improvement, etc.) create FTC risk
- **RESPONSE**: Flag all unsubstantiated claims as [VOID], build pre-launch compliance checklist, use qualitative language until real data exists
- **SYNTHESIS**: FTC enforcement in supplements is aggressive. Must differentiate safe claims (ingredients, sourcing) from risky claims (energy, sleep, recovery) from prohibited claims (disease treatment).
- **OUTCOME**: UPGRADED
- **ACTION**: U3 — Added "FTC Compliance Checklist" to email_post_purchase.md with safe/risky/prohibited claim categories

### ROUND 4
- **CHALLENGE**: Welcome flow doesn't split by acquisition source — should it from Day 1?
- **RESPONSE**: One good flow beats 4 mediocre source-specific flows at low volume. But need clear triggers for when to build the first split.
- **SYNTHESIS**: Define specific thresholds: source concentration >30% AND total list >500, or CVR variance >50% between sources.
- **OUTCOME**: UPGRADED
- **ACTION**: U4 — Added §5.5 "Segmentation Trigger Thresholds" to email_segmentation.md with 4 quantified triggers

### ROUND 5
- **CHALLENGE**: Box insert ROI — is $0.50-0.70/package justified or feel-good branding?
- **RESPONSE**: Referral card math is positive (1 referral per 50 orders = 7.8x ROI on $0.15 card cost). Quick start guide reduces onboarding confusion for novel product.
- **SYNTHESIS**: Both referral ROI and churn prevention justify the spend. Box inserts are defensible.
- **OUTCOME**: RESOLVED

### ROUND 6
- **CHALLENGE**: 9 markdown files vs. Klaviyo execution — documentation-to-execution gap
- **RESPONSE**: Designate markdown as v1.0 blueprint, Klaviyo as live source of truth post-build. Files are "why we built it" reference, not living docs.
- **SYNTHESIS**: All three personas agree — add clear Source of Truth policy.
- **OUTCOME**: UPGRADED
- **ACTION**: U6 — Added §8 "Source of Truth Policy" to email_flow_architecture.md

### ROUND 7
- **CHALLENGE**: Final review across all content
- **RESPONSE**: All personas agree content is coherent. Discount defense, compliance tagging, Founder Mode phasing, and segmentation triggers address major concerns.
- **OUTCOME**: RESOLVED — **Saturation reached.**

---

## Summary

| Metric | Value |
|--------|-------|
| Total rounds | 7 |
| Saturated | Yes (Round 7) |
| Upgrades applied | 5 (U1, U2, U3, U4, U6) |
| Unresolved gaps | 0 |
| Files modified | email_flow_architecture.md (U1, U6), email_abandoned_cart.md (U2), email_post_purchase.md (U3), email_segmentation.md (U4) |

---

## What Would Have Been Missed

Without the persona dialogue, the following gaps would have remained:

1. **No maintenance time budget** — founder would have built 12 flows without knowing the ongoing time cost
2. **Discount arbitrage vulnerability** — customers could game the system by abandoning or lapsing
3. **FTC compliance risk** — unverified statistics would have been sent as email claims
4. **Premature segmentation** — no clear triggers for when to invest in source-specific flows
5. **Documentation drift** — no clear policy on markdown vs. Klaviyo as source of truth


---

### 📄 email_abandoned_cart.md

# M17: Abandoned Cart Email Sequence — Canonical Version

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 436 (detailed copy), 440, 441 (structural frameworks) — merged
**Build Priority**: #1 (build before launch — highest revenue per email)

---

## Overview

**Trigger**: Cart created, no purchase within 1 hour
**Emails**: 3 emails + 1 optional SMS
**Timeline**: 1hr → 24hr → 72hr
**Goal**: Recover 10-15% of abandoned carts
**Expected revenue impact**: 5-15% of total email revenue [Confidence: B | Source: Klaviyo DTC benchmark]

**Discount escalation strategy**: No discount in Email 1 (many people just got distracted). Objection handling in Email 2 (address the "why not"). Discount + urgency in Email 3 (final push for the holdouts).

---

## Sequence Architecture

```
Hour 1 ─── Email 1: Simple Reminder (no discount) ──→ Purchased? ── YES → Exit
                                                              └── NO ↓
Hour 24 ── Email 2: Objection Handling (FAQ) ────────→ Purchased? ── YES → Exit
                                                              └── NO ↓
Hour 48 ── [Optional] SMS: "Your cart is waiting" ───→
                                                              ↓
Hour 72 ── Email 3: Urgency + Free Shipping ─────────→ Purchased? ── YES → Exit
                                                              └── NO → End (enter regular nurture)
```

**Exit condition**: Purchase at any point → exit flow, enter Post-Purchase flow.

---

## Email 1 — 1 Hour After Abandonment: Simple Reminder

**Subject**: `You left something behind...`
**Preview**: `Your IonWave is waiting`
**Strategy**: Helpful, not pushy. Many people just got distracted — a simple reminder converts 40-60% of total cart recovery. [Confidence: B | Source: Klaviyo cart recovery data]
**Discount**: NO

### Body

> Hey {{first_name}},
>
> Looks like you got interrupted.
>
> Your IonWave is still in your cart:
>
> **{{product_name}}** — {{quantity}}
> **{{price}}**
>
> **[CTA BUTTON: Complete Your Order →]**
>
> Quick reminder of what you're getting:
>
> ✓ 78 ionic minerals (not 3-4 like synthetic brands)
> ✓ 98% bioavailable (vs ~10% for pills)
> ✓ 30-day feel-the-difference guarantee
> ✓ Free shipping on subscriptions
>
> Your cart will stay saved for 72 hours.
>
> — The IonWave Team
>
> P.S. Questions holding you back? Just reply. We're here.

**Design**: Clean, product-focused. Dynamic product image from cart. Prominent CTA. Short — this is a reminder, not a sales pitch.

---

## Email 2 — 24 Hours: Objection Handling

**Subject**: `Still thinking about it?`
**Preview**: `Let me answer the question you're probably asking...`
**Strategy**: Address the 4 most common objections directly. Convert the "interested but hesitant."
**Discount**: Optional — 5-10% if needed, but try without first.

### Body

> Hey {{first_name}},
>
> Still on the fence? Totally fair.
>
> Here are the questions most people have before they try IonWave:
>
> ---
>
> **"DOES IT ACTUALLY TASTE OKAY?"**
> Mildly mineral, like high-quality spring water. Most people drink it straight, some add it to juice. Either works.
>
> **"HOW LONG UNTIL I FEEL SOMETHING?"**
> Most customers notice more stable energy within 3-7 days. Full benefits typically show up over 2-4 weeks.
>
> **"IS THIS JUST EXPENSIVE SEAWATER?"**
> No. Seawater is 35g/L salt. Marine plasma is harvested from a specific depth where mineral ratios match human biology, then filtered and concentrated. Very different.
>
> **"WHAT IF IT DOESN'T WORK FOR ME?"**
> 30-day guarantee. Feel the difference or get every penny back. No questions, no hassle.
>
> ---
>
> Still have questions? Hit reply. I'll answer personally.
>
> Or if you're ready:
>
> **[CTA BUTTON: Complete Your Order →]**
>
> — The IonWave Team

**Design**: Text-heavy, conversational. FAQ format with bold questions. No heavy imagery — this should feel like a personal message, not a marketing email.

---

## Email 3 — 72 Hours: Urgency + Incentive (Final)

**Subject**: `Last chance: your cart expires tonight`
**Preview**: `Plus: free shipping on us`
**Strategy**: Create genuine urgency (cart actually clears) + add a small incentive to tip the decision.
**Discount**: YES — free shipping (lower margin impact than % off)

### Body

> Hey {{first_name}},
>
> Your IonWave cart expires in 24 hours.
>
> After that, you'll need to start over.
>
> Before it clears, I wanted to offer something:
>
> **USE CODE: FIRSTBOX**
> **FREE SHIPPING ON YOUR FIRST ORDER**
>
> No minimum. Just enter the code at checkout.
>
> Here's what's waiting for you:
>
> **{{product_name}}** — {{quantity}}
> **{{price}}**
>
> **[CTA BUTTON: Claim Free Shipping →]**
>
> 78 minerals. 30 seconds. 30-day guarantee.
>
> Your body will thank you.
>
> — The IonWave Team
>
> P.S. This is the last email about your cart. If now's not the right time, no worries. We'll be here when you're ready.

**Design**: Slightly more designed than Email 2. Discount code prominent (maybe in a box/banner). Product image. Urgency indicators. But still not spammy — respectful tone.

---

## Optional SMS — 48 Hours

**Trigger**: Cart abandoned 48 hours ago AND opted into SMS AND has not purchased AND has not clicked Email 2
**Send between**: 8am-9pm recipient time only (TCPA compliance)

> Hey {{first_name}}! You left IonWave in your cart. Complete your order: {{cart_link}}
>
> Reply STOP to opt out

**Design notes**: Keep under 160 characters. No emojis. Include opt-out. Link to cart.

---

## Discount Escalation Analysis

**Founder Mode concern**: The cart flow offers free shipping; the welcome flow offers [X]% off; the win-back flow offers 25% off. This creates a potential "wait for the bigger discount" behavior.

**Mitigation strategy:**

| Flow | Discount | Rationale |
|------|----------|-----------|
| Welcome | 10% off first order | Small hook to drive first conversion |
| Cart Email 1-2 | No discount | Test if reminder + objection handling is enough |
| Cart Email 3 | Free shipping (not %) | Different incentive type — doesn't devalue product |
| Win-back (90 days) | 20-25% off | Large gap between purchase attempts justifies larger discount |

**Key principle**: Never offer a bigger discount in a faster email. Customers who wait should not be rewarded more than customers who buy quickly. If anything, the fastest buyers should get the best deal (welcome discount). [Confidence: B | Source: DTC pricing psychology best practices]

**A/B test plan (Month 3+)**: Test Email 3 with free shipping vs. 10% off vs. no discount to find optimal balance of recovery rate and margin preservation.

### Discount Defense Policy (Dialogue Upgrade U2)

**Explicit rules to prevent discount arbitrage:**

1. **Cart flow discount (free shipping) MUST be a different type than welcome discount (% off).** Customers shouldn't feel they "unlocked a better deal" by abandoning.
2. **Never offer a larger discount in a faster flow.** Welcome (10% off) → Cart (free shipping) → Win-back (25% off after 90 DAYS). The discount escalation requires TIME, not behavior manipulation.
3. **Cart Email 1-2: NEVER include a discount.** Many cart abandoners just got distracted — a reminder is enough. Don't train discount-seeking behavior.
4. **Coupon code exclusion rules in Shopify:** Set cart recovery code (FIRSTBOX) to NOT stack with welcome code or win-back code. One discount per order, max.
5. **Margin math at 25% off (worst case):** $59 × 0.75 = $44.25 revenue − $23.60 COGS − $6.50 shipping = $14.15 net. Still profitable, but thin. Monitor margin per flow quarterly.

---

## Flow-Level Metrics & Benchmarks

| Metric | Target (Month 1-3) | Target (Month 4+) | Source |
|--------|-------------------|--------------------|--------|
| Cart recovery rate (flow total) | 8-12% | 12-18% | [Confidence: B \| Source: Klaviyo DTC avg 10-15%] |
| Email 1 recovery rate | 5-8% | 7-10% | [Confidence: B \| Source: first email typically recovers 40-60% of total] |
| Revenue per recipient | $2-5 | $4-8 | [Confidence: C] |
| Open rate (avg) | 40-55% | 45-60% | [Confidence: B] |
| Click rate (avg) | 5-10% | 8-15% | [Confidence: B] |

---

## Klaviyo Implementation Notes

1. **Trigger**: "Checkout Started" (Shopify event) → wait 1 hour → check if "Placed Order" = false → send
2. **Filter**: Exclude anyone who placed order since flow trigger
3. **Conditional split**: After each email, check if order placed → yes = exit, no = continue
4. **Smart Sending**: ON but with shorter window (8 hours) — cart emails are time-sensitive
5. **SMS branch**: Add conditional split at 48hr — if SMS opted in AND has not clicked Email 2 → send SMS
6. **Suppress**: If subscriber is currently in Welcome flow Email 1-2, delay cart flow by 4 hours (don't flood)

---

## Intelligence Gaps

| Gap | Grade | Upgrade Path |
|-----|-------|-------------|
| IonWave cart abandonment rate | D | Measure after 30 days with Shopify analytics |
| Free shipping vs. % off effectiveness | C | A/B test after 100+ cart flow entries |
| Optimal SMS timing within cart flow | C | Test 24hr vs 48hr SMS after 200+ SMS subscribers |
| Cart value threshold for SMS inclusion | D | Analyze: does SMS recovery rate vary by cart value? (requires 3+ months data) |

---

*This is the #1 revenue flow. Build it before launch. See `email_flow_architecture.md` for build order context.*


---

### 📄 email_flow_architecture.md

# M17: Email Flow Architecture

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 421, 422, 446; Klaviyo DTC benchmarks

---

## 1. Customer Lifecycle Stages

Every customer moves through a lifecycle. Email flows are triggered by transitions between stages.

```
VISITOR → SUBSCRIBER → FIRST-TIME BUYER → REPEAT BUYER → SUBSCRIBER (subscription) → ADVOCATE
   ↓           ↓              ↓                  ↓               ↓                    ↓
 Browse    Welcome        Post-Purchase      Replenish      Retention            Referral
 Abandon   Series         + Review           + Upsell       + VIP                + Community
           Cart Recovery  Onboarding         Sub Offer      Churn Prevent
```

**Stage Definitions:**

| Stage | Definition | Primary Email Goal | Key Metric |
|-------|-----------|-------------------|------------|
| 1. Visitor | Browsed site, no email | Capture email (pop-up, lead magnet) | Email capture rate >3% [Confidence: B \| Source: Klaviyo benchmarks \| Date: 2025] |
| 2. Subscriber | Opted in, $0 spent | Convert to first purchase | Welcome→purchase CVR >8% [Confidence: B \| Source: Klaviyo DTC avg \| Date: 2025] |
| 3. First-Time Buyer | 1 purchase completed | Onboard, reduce buyer's remorse, drive review | NPS >8, review rate >15% [Confidence: C \| Source: industry avg \| Date: 2025] |
| 4. Repeat Buyer | 2+ purchases, not subscribed | Convert to subscription | Sub conversion >12% [Confidence: C \| Source: DTC supplement avg \| Date: 2025] |
| 5. Subscriber | Active subscription | Retain, reduce churn, upsell | Monthly churn <8% [Confidence: B \| Source: subscription DTC benchmarks \| Date: 2025] |
| 6. Advocate | 3+ purchases OR $150+ LTV | Referral, UGC, community | Referral opt-in >20% [Confidence: C \| Source: best-in-class DTC \| Date: 2025] |
| 7. At-Risk | No purchase 60+ days | Win-back | Win-back rate >5% [Confidence: B \| Source: Klaviyo benchmarks \| Date: 2025] |
| 8. Churned | No engagement 90+ days | Sunset or re-engage | Re-engage >3% or clean list [Confidence: C \| Source: deliverability best practice \| Date: 2025] |

---

## 2. Core Email Flows — Build Order

**Founder Mode principle**: Build flows in revenue-impact order. A solo founder should NOT build all flows before launch. Build the top 3, launch, then add the rest in Month 2-3.

### Priority 1 — Build Before Launch (Week -2 to Launch)

| # | Flow | Trigger | Emails | Revenue Impact | Why First |
|---|------|---------|--------|---------------|-----------|
| 1 | **Abandoned Cart** | Cart created, no purchase in 1hr | 3 + 1 SMS | 5-15% of total email revenue [Confidence: B \| Source: Klaviyo DTC avg] | Highest $ per email. Captures purchase intent that's already demonstrated. |
| 2 | **Welcome Series** | Email opt-in (no purchase) | 5 | Drives first purchase from subscribers | Sets brand tone. Delivers on popup/lead magnet promise. |
| 3 | **Post-Purchase (basic)** | First purchase completed | 3 (confirm + ship + check-in) | Reduces refunds, drives reviews | Without this, customers feel abandoned after buying. |

**Minimum Viable Email Infrastructure at launch = these 3 flows.**

### Priority 2 — Build in Month 2 (Weeks 5-8)

| # | Flow | Trigger | Emails | Revenue Impact |
|---|------|---------|--------|---------------|
| 4 | **Post-Purchase (extended)** | Expand basic to full 7-email | 7 | Review collection, subscription upsell |
| 5 | **Abandoned Checkout** | Checkout started, no completion | 3 | 3-8% of email revenue [Confidence: C \| Source: Klaviyo] |
| 6 | **Replenishment** | Projected product depletion (~Day 25) | 2 + 1 SMS | 10-20% repeat rate lift [Confidence: C \| Source: subscription DTC avg] |

### Priority 3 — Build in Month 3+ (Weeks 9-12)

| # | Flow | Trigger | Emails |
|---|------|---------|--------|
| 7 | **Win-Back** | No purchase in 60 days | 4 |
| 8 | **Browse Abandonment** | Product page view, no cart in 24hr | 2 |
| 9 | **Subscription Upsell** | 2nd purchase completed | 2 |
| 10 | **VIP Recognition** | 3rd purchase OR $150+ LTV | 1 + surprise |
| 11 | **Review Solicitation** | 14 days post-delivery | 2 + 1 SMS |
| 12 | **Referral Activation** | VIP recognized | 2 + in-package |

### Priority 4 — Build When Data Supports (Month 4+)

| # | Flow | Trigger | Emails |
|---|------|---------|--------|
| 13 | **Sunset** | No email engagement in 90 days | 2 |
| 14 | **Churn Intervention** | Churn risk score >70 | 1 + CS outreach |
| 15 | **Birthday/Anniversary** | Date-based | 1 |

---

## 3. Master Automation Map

All 12 production automations with triggers, channels, timing, and goal metrics:

| Automation | Trigger | Stage Transition | Channel | Timing | Content Arc | Goal Metric |
|-----------|---------|-----------------|---------|--------|------------|-------------|
| Welcome Series | Email opt-in (no purchase) | 2→3 | Email (5) | Day 0, 1, 3, 5, 7 | Brand story → Education → Social proof → Offer → Check-in | First purchase CVR >8% |
| Abandoned Cart | Cart created, no purchase 1hr | 3→4 | Email (3) + SMS (1) | 1hr, 24hr, 72hr | Reminder → Objection handling → Urgency + discount | Recovery rate >10% |
| Browse Abandonment | Product page view, no cart 24hr | 2→3 | Email (2) | 24hr, 72hr | Product highlight → Social proof | Cart creation rate >5% |
| Post-Purchase | First purchase completed | 4→5 | Email (7) | Day 0, 1, 7, 14, 21, 25, 30 | Confirm → Onboard → Science → Remind → Review → Milestone | NPS >8, Review rate >15% |
| Replenishment | Projected depletion (~Day 25) | 5→6 | Email (2) + SMS (1) | 5 days before, 2 days before, day of | Reminder → Subscription offer → Last chance | Repeat rate >35% |
| Subscription Offer | 2nd purchase completed | 6→6 | Email (2) | Day 1, 5 after 2nd order | Subscribe & save pitch → Value comparison | Sub conversion >12% |
| VIP Recognition | 3rd purchase OR $150+ LTV | 6→7 | Email (1) + surprise | After qualifying event | Thank you + exclusive offer + referral invite | Referral opt-in >20% |
| Referral Activation | VIP recognized | 7→7 | Email (2) + in-package | With VIP email + next shipment | How it works → Share link → Reward reminder | Referral share rate >15% |
| Review Solicitation | 14 days post-delivery | 5→7 | Email (2) + SMS (1) | Day 14, 21, 28 | Review request → Photo request → Incentive | Review rate >20% |
| Win-Back | No purchase 60 days | 8→4 | Email (4) | Day 60, 75, 90, 105 | Miss you → What's new → Big offer → Sunset | Win-back rate >5% |
| Sunset | No email engagement 90 days | 8→9 | Email (2) | Day 90, 97 | Want to stay? → Final goodbye | Re-engage >3% or clean list |
| Churn Intervention | Churn risk score >70 | 6→8 | Email (1) + CS outreach | Within 24hr of trigger | Personal check-in, retention offer | Save rate >15% |

---

## 4. Klaviyo Setup Guide — Founder Mode

### Pre-Launch Checklist (Do these first)

- [ ] Set up Klaviyo account, connect Shopify
- [ ] Import brand assets (logo, colors, fonts) into template builder
- [ ] Create master email template (header + footer consistent across all flows)
- [ ] Set up core segments: All Subscribers, Customers, Non-Customers, VIPs
- [ ] Build Flow #1: Abandoned Cart (3 emails)
- [ ] Build Flow #2: Welcome Series (5 emails)
- [ ] Build Flow #3: Post-Purchase Basic (3 emails: confirm, ship, check-in)
- [ ] Test all 3 flows with a test profile
- [ ] Set up signup form / popup (10% off first order, or lead magnet)
- [ ] Enable Shopify integration for order events

### Month 2 Additions

- [ ] Expand Post-Purchase to full 7-email sequence
- [ ] Add Abandoned Checkout flow
- [ ] Add Replenishment reminder flow
- [ ] Begin weekly campaign sends (education content, 1x/week)
- [ ] Set up A/B testing on welcome series subject lines

### Month 3+ Additions

- [ ] Add Win-Back flow
- [ ] Add Browse Abandonment flow
- [ ] Add Subscription Upsell flow
- [ ] Set up engagement-based segmentation
- [ ] Begin bi-weekly campaign cadence if list >1,000

---

## 5. Email Cadence Rules

**Flow emails take priority over campaigns.** Klaviyo handles this with Smart Sending, but set these rules explicitly:

| Rule | Setting |
|------|---------|
| Smart Sending window | 16 hours (no contact within 16hr of last email) |
| Max emails per person per week | 5 (flows + campaigns combined) |
| Flow emails | Always send (override campaign suppression) |
| Campaign frequency | 1x/week (Month 1-2), 2x/week (Month 3+ if list >1K) |
| SMS frequency | Max 4 SMS/month per subscriber |
| Quiet hours | No SMS between 9pm-8am recipient time |

---

## 6. Benchmarks — DTC Supplement Vertical

**Realistic benchmarks for a new brand (Month 1-6, <5,000 subscribers):**

| Metric | Flow Emails | Campaign Emails |
|--------|------------|-----------------|
| Open Rate | 40-60% [Confidence: B] | 25-35% [Confidence: B] |
| Click Rate | 3-8% [Confidence: B] | 1.5-3% [Confidence: B] |
| Revenue per Recipient | $0.50-2.00 [Confidence: C] | $0.05-0.15 [Confidence: C] |
| Unsubscribe Rate | <0.3% per send [Confidence: B] | <0.5% per send [Confidence: B] |
| Spam Complaint Rate | <0.01% [Confidence: A \| Source: Klaviyo/ESP policy] | <0.01% |

**Revenue attribution targets:**

| Timeframe | Email % of Total Revenue | Source |
|-----------|------------------------|--------|
| Month 1-3 | 15-25% | [Confidence: C \| Source: Klaviyo DTC avg for new brands] |
| Month 4-6 | 25-35% | [Confidence: C \| Source: Klaviyo DTC avg] |
| Month 7-12 | 30-40% | [Confidence: B \| Source: Klaviyo mature DTC brands] |
| Mature (Year 2+) | 35-50% | [Confidence: B \| Source: Klaviyo top-quartile DTC] |

**Note:** These are realistic for a solo founder who builds the 3 priority flows before launch and adds flows monthly. Brands that launch with only a welcome popup and no flows typically see email at <10% of revenue for months.

---

## 7. Maintenance Time Budget (Dialogue Upgrade U1)

**Building a flow is not the end — maintaining it is the ongoing cost.**

| Flow | Build Time (one-time) | Monthly Maintenance | What Maintenance Includes |
|------|----------------------|--------------------|--------------------------|
| Abandoned Cart (3 emails) | 3-4 hours | 30 min/month | Check recovery rate, update discount codes, refresh copy if stale |
| Welcome Series (5 emails) | 4-6 hours | 30 min/month | Update testimonials, check conversion rate, A/B test subjects |
| Post-Purchase Basic (3 emails) | 2-3 hours | 15 min/month | Verify shipping triggers work, update tracking links |
| Post-Purchase Extended (7 emails) | 4-5 hours | 30 min/month | Update data claims, refresh review links, check upsell performance |
| Win-Back (4 emails) | 2-3 hours | 15 min/month | Update "What's New" content quarterly, check discount code validity |
| All other flows (each) | 1-2 hours | 15 min/month | Basic health checks |

**Total ongoing maintenance for 12 flows: ~3-4 hours/month.**
At Founder Mode scale (3 flows at launch), ongoing maintenance is ~1.5 hours/month. This is manageable alongside other duties.

**Monthly maintenance ritual (15 min):**
1. Check Klaviyo flow analytics dashboard
2. Note any flow with <5% open rate (deliverability issue) or <1% click rate (content issue)
3. Fix the worst-performing email in the worst-performing flow
4. Move on. Don't optimize everything at once.

---

## 8. Source of Truth Policy (Dialogue Upgrade U6)

**These markdown files are the v1.0 BUILD BLUEPRINT — not a living document.**

| Layer | Source of Truth | Purpose |
|-------|----------------|---------|
| **Strategy** (why we built it this way) | These markdown files (`data/m17/*.md`) | Reference for "why this flow exists, what it's supposed to do, what benchmarks we targeted" |
| **Execution** (what's actually live) | Klaviyo flows | The live emails, actual copy, current subject lines, real performance data |

**Once flows are built in Klaviyo:**
- Klaviyo is the source of truth for copy, timing, and structure
- These markdown files are the historical blueprint + strategic rationale
- If you change copy in Klaviyo, you do NOT need to update the markdown file
- If you fundamentally restructure a flow (add/remove emails, change strategy), update the markdown for documentation

---

## 9. Intelligence Gaps

| Gap | Current Grade | Upgrade Path | Priority |
|-----|--------------|-------------|----------|
| IonWave-specific conversion rates | D (no data) | Measure after 30 days of live data | HIGH |
| Optimal replenishment timing | C (assumes 30-day supply) | Validate with actual consumption data from first 100 customers | MEDIUM |
| Churn risk scoring model | D (placeholder) | Requires 3-6 months of subscription data to build | LOW (Month 4+) |
| SMS ROI at IonWave's scale | C (industry benchmarks) | Test with first 500 SMS subscribers | MEDIUM |
| Optimal discount escalation ladder | C (Danilo's proposed) | A/B test over 90 days: discount vs. no-discount in Cart Email 3 | HIGH |

---

*Next: See `email_segmentation.md` for segment definitions, `email_welcome_series.md` for the canonical welcome sequence.*


---

### 📄 email_post_purchase.md

# M17: Post-Purchase Email Sequence — Canonical Version

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 437 (detailed 7-email copy), 442, 443 (structural frameworks) — merged
**Build Priority**: #3 basic (3 emails at launch), expand to full 7 in Month 2

---

## Overview

**Trigger**: First purchase completed
**Emails**: 7 (launch with first 3, expand in Month 2)
**Timeline**: Day 0 → Day 60
**Goal**: Onboard, retain, get reviews, convert to subscription, create advocates
**Primary metrics**: NPS >8, review rate >15%, subscription conversion >12%

**This is the longest and most strategically important sequence.** It's where one-time buyers become subscribers and subscribers become advocates. Every email has a specific job in the retention engine.

---

## Sequence Architecture

```
LAUNCH (Priority 3A — Build before launch):
Day 0 ──── Email 1: Order Confirmation + First-Use Tip
Day 1 ──── [Auto: Shipping notification via Shopify — not custom email]
Day 7 ──── Email 2: First Week Check-In
Day 14 ─── Email 3: The Science (education + reinforcement)

MONTH 2 EXPANSION (Priority 3B):
Day 21 ─── Email 4: Subscription Reminder (next box ships in 9 days)
Day 25 ─── Email 5: Review Request
Day 30 ─── Email 6: 30-Day Milestone + Upsell
Day 60 ─── Email 7: 60-Day Survey + Referral
```

**Exit condition**: None — everyone who purchases goes through this full sequence. Subscribers and non-subscribers get slightly different versions of Emails 4 and 6 (conditional split).

---

## Email 1 — Day 0: Order Confirmation + First-Use Tip

**Subject**: `Your order is confirmed!`
**Preview**: `Here's your first-use tip`
**Send**: Immediately after purchase

### Body

> Hey {{first_name}},
>
> Your IonWave order is confirmed! 🎉
>
> **Order #{{order_number}}**
> {{product_name}} — {{quantity}}
>
> **YOUR FIRST-USE TIP:**
>
> For best results: **empty stomach, before coffee.**
>
> Mix one sachet in 8-12oz water. Drink it first thing in the morning.
>
> Why? Your body absorbs minerals most efficiently when your stomach is empty. The ionic form means near-instant absorption — no waiting, no digestion required.
>
> **WHAT TO EXPECT:**
> - **Days 1-3**: Subtle alertness, hydration that "hits different"
> - **Days 4-14**: Energy stabilizes, afternoon crashes fade
> - **Days 15-30**: Full benefits — mental clarity, better recovery, improved sleep
>
> Your IonWave ships within 24 hours. We'll send tracking info as soon as it's on the way.
>
> Welcome to the community.
>
> — The IonWave Team
>
> P.S. Questions about anything? Just reply. We're here.

**Design**: Transactional feel (order number, product details) but warmer than standard Shopify confirmation. The first-use tip turns a boring confirmation into an onboarding moment.

---

## Email 2 — Day 7: First Week Check-In

**Subject**: `How's your first week going?`
**Preview**: `What most people feel by now`
**Send**: Day 7 after purchase

### Body

> Hey {{first_name}},
>
> One week of IonWave. Let's check in.
>
> **BY NOW, YOU MIGHT NOTICE:**
> → More stable energy through the day
> → Less of that 3pm crash
> → Subtle improvement in mental clarity
> → Hydration that actually feels different
>
> If you're feeling some of these — great. Your body is responding.
>
> If not yet — that's normal too. Bodies that have been mineral-depleted for years sometimes need 2-3 weeks to fully calibrate.
>
> **The key: don't stop.** Consistency is everything.
>
> One sachet. Every morning. Let the minerals do their work.
>
> **HOW CAN WE HELP?**
>
> If something's not working, reply to this email. I read everything and respond personally.
>
> You're not just a customer. You're part of this now.
>
> — The IonWave Team

**Design**: Personal, plain-text style. No heavy imagery. This should feel like a founder checking in, not a marketing email.

---

## Email 3 — Day 14: The Science

**Subject**: `The changes happening inside you`
**Preview**: `What 2 weeks of proper mineralization actually does`
**Send**: Day 14 after purchase

### Body

> Hey {{first_name}},
>
> Two weeks in. Here's what's happening beneath the surface:
>
> **CELLULAR HYDRATION**
> Your cells are finally getting minerals in ionic form — the only form they can actually use. This is different from drinking more water. This is water that works.
>
> **ENZYME ACTIVATION**
> Over 300 enzymes in your body require minerals to function. They've been running on fumes. Now they have fuel.
> [Confidence: B | Source: peer-reviewed biochemistry — magnesium alone is a cofactor for 300+ enzymes]
>
> **NERVOUS SYSTEM SUPPORT**
> Magnesium, potassium, calcium — these aren't just electrolytes. They're how your neurons fire. Properly mineralized = calmer, clearer, faster.
>
> **RECOVERY OPTIMIZATION**
> Your muscles don't just need protein. They need the minerals that power repair at the cellular level.
>
> This isn't hype. This is biochemistry.
>
> And you're two weeks into it.
>
> Keep going. The best changes are still ahead.
>
> — The IonWave Team
>
> P.S. Tracking your health metrics? We'd love to see your before/after. Reply with screenshots if you've got them.

**Design**: Science-forward. Consider infographic showing the 4 mechanisms. Clean, authoritative. Different tone from the personal check-in — this builds intellectual confidence in the product.

**Compliance note**: All health claims should be reviewed for FTC/FD&C Act compliance. "Enzyme activation" and "nervous system support" are structure/function claims that may require disclaimers. [VOID — requires: legal review of email health claims]

### FTC Compliance Checklist (Dialogue Upgrade U3)

**Before launching ANY post-purchase email with health claims:**

- [ ] **Review all statistical claims** — "73% of customers report..." is ONLY acceptable with real survey data. Until then, replace with qualitative language ("many customers tell us...")
- [ ] **Structure/function claims** require "This statement has not been evaluated by the FDA" disclaimer if making any claims about body function
- [ ] **No disease claims** — never imply IonWave treats, cures, or prevents any disease
- [ ] **Testimonials must be representative** — FTC requires testimonials reflect typical results, not exceptional cases
- [ ] **"Typical results" disclaimer** — if using before/after data, include "Results may vary. These are individual experiences, not guaranteed outcomes."
- [ ] **Email 3 (The Science)** — "enzyme activation" and "nervous system support" are structure/function claims. Add FDA disclaimer or soften language to "may support..."
- [ ] **Email 6 (30-Day Milestone)** — ALL statistics (73%, 68%, 61%, 84%) are currently [VOID — Danilo projections]. DO NOT SEND until replaced with real data or removed entirely.

**Safe claims (no disclaimer needed):** Product ingredients, how to use, serving size, mineral count (78), sourcing information.
**Risky claims (need review):** Energy improvement, sleep quality, recovery optimization, mental clarity.
**Prohibited claims:** Disease treatment, disease prevention, "cures" anything.

---

## Email 4 — Day 21: Subscription Reminder

**Subject**: `Heads up: box #2 ships in 9 days`
**Preview**: `Plus: a way to save on your next order`
**Send**: Day 21 after purchase
**Conditional split**: Subscriber vs. Non-Subscriber

### Body (Subscriber version)

> Hey {{first_name}},
>
> Quick logistical note:
>
> Your next box of IonWave ships in 9 days.
>
> Same address. Same payment method. Nothing you need to do.
>
> **WANT TO ADD ANYTHING?**
> Some customers grab a second box for travel. Or switch to our 3-month bundle for better savings.
>
> **[CTA: Manage Your Subscription →]**
>
> **NEED TO PAUSE OR CHANGE TIMING?**
> No problem. You can:
> — Push back your next shipment
> — Change delivery frequency
> — Update your address
>
> All from your account dashboard. No phone calls, no hassle.
>
> **[CTA: Update Preferences →]**
>
> Thanks for sticking with it. Three weeks of consistent minerals is when most people really start to feel the difference.
>
> — The IonWave Team

### Body (Non-Subscriber version)

> Hey {{first_name}},
>
> Quick heads up: you're about 9 days from running low on IonWave.
>
> **THE EASY WAY TO NEVER RUN OUT:**
>
> Subscribe & Save — get IonWave delivered every 30 days.
> - **Save [X]%** vs. one-time purchase
> - **Free shipping** on every order
> - **Skip or cancel anytime** — no commitment
>
> **[CTA: Subscribe & Save →]**
>
> Or just reorder when you're ready:
>
> **[CTA: Reorder Now →]**
>
> — The IonWave Team

---

## Email 5 — Day 25: Review Request

**Subject**: `Quick favor? Takes 30 seconds.`
**Preview**: `Your feedback helps more than you know`
**Send**: Day 25 after purchase

### Body

> Hey {{first_name}},
>
> You've been with us almost a month now.
>
> Can I ask a quick favor?
>
> If IonWave has made a difference for you — more energy, better recovery, clearer thinking, anything — would you take 30 seconds to leave a review?
>
> **[CTA BUTTON: Leave a Review →]**
>
> **WHY IT MATTERS:**
>
> We're a small team. We don't have celebrity endorsers or massive ad budgets.
>
> What we have is customers who feel the difference and tell others about it.
>
> Your review helps someone else take the chance you took a month ago.
>
> Even just a sentence or two helps.
>
> Thank you — seriously.
>
> — The IonWave Team
>
> P.S. Had a problem? Don't leave a bad review — just reply to this email. We'll fix it.

**Design**: Simple, short. One prominent CTA button. The P.S. is critical — it redirects negative feedback to a private channel instead of a public review.

---

## Email 6 — Day 30: 30-Day Milestone + Upsell

**Subject**: `One month in. Here's what we've learned.`
**Preview**: `Congratulations — and a special offer`
**Send**: Day 30 after purchase

### Body

> Hey {{first_name}},
>
> 30 days of IonWave.
>
> This is the point where it stops being an experiment and becomes a habit.
>
> **WHAT OUR DATA SHOWS AT 30 DAYS:**
> → 73% of customers report sustained energy improvements
> → 68% report better recovery after workouts
> → 61% report improved sleep quality
> → 84% continue their subscription past month 3
>
> [Confidence: D | Source: Danilo projections — NOT verified data. Replace with actual customer survey data once available.]
> [VOID — requires: real customer data from first 100 subscribers to validate or replace these numbers]
>
> You're part of this now.
>
> **AS A THANK YOU:**
>
> For hitting the 30-day mark, here's an exclusive offer:
>
> **UPGRADE TO 90-DAY SUPPLY**
> Save 28% vs monthly
> Code: **MONTH1**
>
> **[CTA: Claim Offer →]**
>
> Locks in your current price. Ships every 3 months. Less to think about.
>
> Or keep your monthly subscription — either way, we're glad you're here.
>
> Here's to month two.
>
> — The IonWave Team

---

## Email 7 — Day 60: Two-Month Survey + Referral

**Subject**: `Your 60-day check-in`
**Preview**: `Quick survey + chance to win`
**Send**: Day 60 after purchase

### Body

> Hey {{first_name}},
>
> Two months of consistent mineralization.
>
> At this point, IonWave isn't a supplement you're trying — it's part of your daily system.
>
> **I'D LOVE YOUR FEEDBACK:**
>
> A quick 2-minute survey helps us make better decisions:
>
> **[CTA: Take 2-Min Survey →]**
>
> Everyone who completes it gets entered to win a FREE 3-month supply.
>
> **A FEW QUICK QUESTIONS:**
> 1. What's the #1 change you've noticed?
> 2. What would make IonWave better?
> 3. Would you recommend us? Why or why not?
>
> Your answers shape what we build next.
>
> ---
>
> **SHARE THE LOVE:**
>
> Know someone who should try IonWave? Forward this email and they'll get 15% off their first box with code **FRIEND15**.
>
> You'll get $10 credit for every friend who orders.
>
> **[CTA: Get Your Referral Link →]**
>
> Thanks for being part of this.
>
> — The IonWave Team

---

## Flow-Level Metrics & Benchmarks

| Metric | Target | Source |
|--------|--------|--------|
| Open rate (avg across 7 emails) | 45-60% | [Confidence: B \| Source: Klaviyo post-purchase avg for DTC] |
| Review request conversion (Email 5) | 10-20% click, 5-10% review submitted | [Confidence: C \| Source: DTC review collection benchmarks] |
| Subscription conversion (Email 4 non-sub version) | 8-15% | [Confidence: C] |
| 90-day upsell conversion (Email 6) | 5-10% | [Confidence: C] |
| Referral link share rate (Email 7) | 10-15% | [Confidence: C] |
| Survey completion rate (Email 7) | 15-25% | [Confidence: C] |

---

## Intelligence Gaps

| Gap | Grade | Upgrade Path |
|-----|-------|-------------|
| 30-day customer data (Email 6 stats) | D (Danilo projections) | Survey first 100 customers at Day 30. Replace placeholder data. **HIGH PRIORITY.** |
| Optimal review request timing | C (Day 25 assumed) | Test Day 14 vs Day 25 vs Day 30 after 200+ orders |
| Subscription conversion rate | D (no data) | Measure after 60 days of live Post-Purchase flow |
| Health claim compliance | D (not reviewed) | **Legal review required** before launching Emails 3 and 6 |
| Referral program mechanics | C (placeholder) | Finalize referral structure in M24 (Referral) TUP |

---

*Build the first 3 emails before launch. Expand to full 7 in Month 2. See `email_flow_architecture.md` for build order.*


---

### 📄 email_segmentation.md

# M17: Email Segmentation Strategy

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 420, 423, 424; Klaviyo segmentation best practices

---

## 1. When Segmentation Matters

**Founder Mode reality check**: Segmentation is powerful but premature at low volume.

| Subscriber Count | Segmentation Level | Rationale |
|-----------------|-------------------|-----------|
| 0-500 | **None** — Send to all | Sample too small. Focus on building flows and list. [Confidence: B \| Source: Klaviyo small-brand guidance] |
| 500-2,000 | **Basic** — Customers vs. Non-Customers | Enough data to separate buyers from browsers. Two send lists. |
| 2,000-5,000 | **Intermediate** — Add engagement + purchase frequency | Can meaningfully split engaged vs. unengaged, one-time vs. repeat |
| 5,000+ | **Advanced** — Full lifecycle + behavioral + interest-based | Enough volume to see statistically meaningful differences in segment performance |

**Do NOT over-segment before you have volume.** A perfectly segmented email to 50 people loses to a good email to 500 people.

---

## 2. Core Segments (Lifecycle-Based)

These are the primary segments based on purchase behavior. Build these first.

| Segment | Definition | Size Estimate (Year 1) | Email Strategy | Klaviyo Logic |
|---------|-----------|----------------------|----------------|---------------|
| **Never Purchased** | Subscribed, $0 spent | 60-70% of list | Welcome flow → education → first purchase incentive | `Has placed order: 0 times` |
| **One-Time Buyers** | Exactly 1 purchase | 15-20% of list | Post-purchase nurture → subscription push → replenishment | `Has placed order: exactly 1 time` |
| **Repeat Buyers** | 2+ purchases, not subscribed | 5-10% of list | Loyalty → subscription push → referral | `Has placed order: at least 2 times AND Active subscription: false` |
| **Subscribers** | Active subscription | 5-15% of list | Retention → upsell → VIP treatment → reduce churn | `Active subscription: true` |
| **Churned Subscribers** | Cancelled subscription | 2-5% of list | Win-back → feedback survey → re-subscription offer | `Cancelled subscription: true AND Active subscription: false` |
| **At-Risk** | No engagement in 30+ days | Variable | Re-engagement campaign → sunset if no response | `Last opened email: more than 30 days ago` |
| **VIPs** | Top 10% by LTV | ~3-5% of list | Exclusive access → early launches → personal founder touch | `Total revenue: top 10%` OR `Has placed order: at least 3 times` |

[Confidence: B | Source: Danilo tabs 420+423+424 merged, validated against Klaviyo DTC patterns | Date: 2026]

---

## 3. Engagement-Based Segments

Layered ON TOP of lifecycle segments. Critical for deliverability health.

| Segment | Definition | Email Strategy | Action |
|---------|-----------|----------------|--------|
| **Highly Engaged** | Opened 3+ of last 5 emails | Full communication — send more, they want it | Send all campaigns + flows |
| **Engaged** | Opened 1-2 of last 5 emails | Normal cadence — standard campaign sends | Send weekly campaigns + all flows |
| **Disengaged** | 0 opens in last 5 emails | Reduce cadence → re-engagement attempt | Send only high-value campaigns (sales, new product) |
| **Unengaged** | No open in 60+ days | Sunset sequence → suppress or remove | 2-email sunset series, then suppress from campaigns |

[Confidence: B | Source: Danilo tab 424 + deliverability best practices]

**Why this matters:** Sending to unengaged subscribers kills deliverability. Gmail, Yahoo, and Outlook use engagement signals to determine inbox vs. spam. Suppressing unengaged subscribers protects the health of your ENTIRE list.

**Sunset policy:**
1. 60 days no open → Move to "Unengaged" segment
2. Send 2-email sunset series ("Want to stay?" + "Final goodbye")
3. If no engagement → Suppress from campaigns (keep in flows only)
4. 90 days no engagement → Remove from list entirely

---

## 4. Acquisition Source Segments

Track where subscribers came from to tailor the welcome experience:

| Source | Expected Behavior | Welcome Flow Adjustment |
|--------|------------------|------------------------|
| **Meta/Facebook Ads** | Need more education, lower purchase intent | Longer welcome series, more social proof, bigger discount needed [Confidence: C \| Source: DTC heuristic] |
| **Organic/SEO** | Already researching, higher intent | Shorter education arc, faster path to purchase [Confidence: C \| Source: DTC heuristic] |
| **Referral** | High trust, fastest to convert | Lean into social proof, referrer's story, smaller discount needed [Confidence: C \| Source: DTC heuristic] |
| **Influencer (specific)** | Came for that influencer's recommendation | Reference the specific influencer in welcome, match tone [Confidence: C \| Source: DTC heuristic] |
| **Popup (on-site)** | Browsing, may be price-shopping | Standard welcome flow, emphasize differentiation from competitors [Confidence: C \| Source: DTC heuristic] |

**Implementation note:** In Klaviyo, track UTM source on signup. Use `$source` property or custom properties to tag acquisition channel. Build conditional welcome flow splits by Month 3+ when you have enough volume per source.

---

## 5. Interest-Based Segments (Phase 2+)

These require either self-declared data (quiz, preference center) or behavioral inference:

| Segment | Signal | Content Strategy |
|---------|--------|-----------------|
| **Keto-Focused** | Indicated keto interest in quiz/browsing | Keto-specific content: electrolyte needs on keto, "keto flu" prevention, low-carb recipes |
| **Athletes / Fitness** | Indicated fitness interest | Performance content: recovery optimization, workout hydration, endurance |
| **Wellness / General Health** | Default / general interest | Broad wellness: energy, sleep, stress, daily vitality |
| **Biohackers** | Browsed science pages, engaged with mechanism-of-action content | Deep science: bioavailability data, mineral ratios, research citations |

[Confidence: C | Source: Danilo tab 424 + IonWave persona research]

**When to build:** After Month 4, when quiz/preference center data or behavioral signals provide enough segmentation signal. Do NOT guess interest from demographics alone.

---

## 5.5. Segmentation Trigger Thresholds (Dialogue Upgrade U4)

**Don't segment because you can — segment when the data tells you to.**

Specific triggers that signal when to build source-specific welcome flow splits:

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Any single acquisition source = 30%+ of subscribers AND total list >500 | e.g., "Meta Ads = 35% of 600 subscribers" | Build a Meta-specific welcome flow variant |
| Open rate variance between sources >15 percentage points | e.g., "Organic opens at 55%, Meta opens at 35%" | Source-specific subject lines and content arcs |
| Welcome-to-purchase CVR varies >50% between sources | e.g., "Referral converts at 15%, Meta converts at 6%" | Adjust discount strategy and education depth by source |
| Total subscribers >2,000 | Enough volume for statistically meaningful splits | Enable engagement-based segmentation tiers |

**Until these triggers fire:** Run a single welcome flow for all sources. A good general flow beats 4 mediocre source-specific flows.

---

## 6. Segment Priority Matrix

What to build and when:

| Phase | Segments to Build | Prerequisite |
|-------|------------------|-------------|
| **Pre-Launch** | Customers vs. Non-Customers (just 2 lists) | Klaviyo connected to Shopify |
| **Month 1-2** | Add: VIPs, One-Time vs. Repeat | Need 50+ customers |
| **Month 3-4** | Add: Engagement tiers (Highly Engaged / Engaged / Disengaged) | Need 60+ days of email data |
| **Month 4-6** | Add: Acquisition source segments | Need enough volume per source (50+ per channel) |
| **Month 6+** | Add: Interest-based segments | Need quiz/preference center OR 1,000+ behavioral data points |

---

## 7. Klaviyo Implementation Notes

### Segment vs. List

| Use | When |
|-----|------|
| **Lists** | Signup sources only (Main List, Popup List, Checkout Opt-in) |
| **Segments** | Everything else — dynamic, auto-updating based on conditions |

**Rule:** Never manually add people to segments. Segments should be condition-based and auto-update. Lists are for opt-in sources only.

### Key Segments to Create in Klaviyo (Day 1)

```
1. "All Subscribers" — Everyone on any list
2. "Customers" — Has placed order at least 1 time
3. "Non-Customers" — Has placed order 0 times
4. "Engaged 30d" — Opened or clicked email in last 30 days
5. "VIP" — Has placed order at least 3 times OR Total revenue > $150
```

### Campaign Send Rules by Segment

| Campaign Type | Send To | Exclude |
|--------------|---------|---------|
| Weekly newsletter | Engaged 30d | Unengaged |
| Product launch | All Subscribers | Suppressed |
| Flash sale | Engaged 30d + Customers | Non-customers (unless very compelling) |
| Re-engagement | Disengaged (30-60 days) | Unengaged (60+) |
| VIP exclusive | VIP segment only | Everyone else |

---

## 8. Intelligence Gaps

| Gap | Current Grade | Upgrade Path |
|-----|--------------|-------------|
| Actual segment sizes for IonWave | D (estimates only) | Measure after 90 days of list building |
| Conversion rates by acquisition source | D (no data) | Tag UTM sources, measure after 60 days |
| Optimal engagement threshold definitions | C (industry standard) | Calibrate with IonWave-specific open/click data after 60 days |
| Interest segment effectiveness | D (no data) | Requires quiz/preference center implementation |

---

*Next: See `email_welcome_series.md` for the canonical welcome sequence that drives Stage 2→3 conversion.*


---

### 📄 email_subject_lines.md

# M17: Subject Line Formula Library

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 425, 426; email marketing best practices

---

## 1. Subject Line Principles

| Principle | Why | Evidence |
|-----------|-----|---------|
| Keep under 50 characters | Mobile preview truncates at ~40-50 chars. 70%+ of opens are mobile. | [Confidence: A \| Source: Litmus/Klaviyo data] |
| Create curiosity OR be ultra-specific | Mid-range performs worst ("kind of interesting"). Go all the way in one direction. | [Confidence: B \| Source: email marketing consensus] |
| Personalization increases opens 20%+ | `[First Name]` in subject line signals "this is for me" | [Confidence: B \| Source: Klaviyo personalization data] |
| Preview text is equally important | Subject + preview = your pitch in the inbox. Treat as a unit. | [Confidence: B \| Source: Litmus eye-tracking] |
| Test emojis cautiously | Work for some audiences (younger, wellness). Can feel spammy for others. | [Confidence: C \| Source: mixed evidence] |
| Front-load important words | First 3-4 words determine open — the rest may be truncated | [Confidence: B \| Source: mobile UX data] |
| Match subject to email content | Bait-and-switch kills trust and deliverability (spam complaints) | [Confidence: A \| Source: ESP policy + best practice] |

---

## 2. Subject Line Formulas

11 proven formula types with IonWave-specific examples:

| # | Formula | Mechanism | Example | Best For |
|---|---------|-----------|---------|----------|
| 1 | **Personal + Specific** | Name + clear value | `{{first_name}}, your energy awaits` | Welcome, cart recovery |
| 2 | **Question** | Engages curiosity, invites self-reflection | `Still tired by 2pm?` | Awareness, re-engagement |
| 3 | **Curiosity Gap** | Creates information gap reader needs to close | `The mineral you're missing` | Education, nurture |
| 4 | **Number + Benefit** | Specificity signals substance | `78 reasons you're dehydrated` | Education |
| 5 | **How-To** | Promises actionable value | `How to beat the afternoon crash` | Education |
| 6 | **Urgency + Offer** | Scarcity drives action | `24 hours left: 20% off` | Sales, cart recovery |
| 7 | **Social Proof** | Others validate the choice | `Why 10,000 people switched` | Conversion |
| 8 | **Story Tease** | Narrative hook creates curiosity | `Why I almost gave up` | Founder story, brand |
| 9 | **Direct Offer** | Straight to the value | `25% off - today only` | Sales |
| 10 | **FOMO** | Fear of missing out | `Everyone's talking about this` | Launch, trending |
| 11 | **Emoji + Short** | Pattern interrupt in inbox | `You forgot something` | Cart recovery |

---

## 3. Subject Lines by Flow

### Welcome Series

| Email | Subject Line A | Subject Line B (A/B test) | Preview Text |
|-------|---------------|--------------------------|--------------|
| W1 (Immediate) | `Welcome to IonWave — here's your [X]% off` | `You're in! Here's what happens next` | `Plus: why 78 minerals changes everything` |
| W2 (Day 1) | `{{first_name}}, here's your getting started ritual` | `Quick tip: empty stomach, before coffee` | `Most people feel the difference by Day 3` |
| W3 (Day 3) | `Why we started IonWave (it's personal)` | `The 120-year-old science behind this` | `It started with a French biologist named René Quinton...` |
| W4 (Day 5) | `See what others are saying` | `"I finally stopped crashing at 2pm"` | `Real customers, real results` |
| W5 (Day 7) | `How's it going? (quick check-in)` | `{{first_name}}, quick question` | `Hit reply — I read every one` |

### Abandoned Cart

| Email | Subject Line A | Subject Line B | Preview Text |
|-------|---------------|---------------|--------------|
| AC1 (1 hour) | `You left something behind...` | `Did you forget something?` | `Your IonWave is waiting` |
| AC2 (24 hours) | `Still thinking about it?` | `Is something holding you back?` | `Let me answer the question you're probably asking` |
| AC3 (72 hours) | `Last chance: your cart expires tonight` | `Your cart is about to expire (+ free shipping)` | `Plus: free shipping on us` |

### Post-Purchase

| Email | Subject Line A | Subject Line B | Preview Text |
|-------|---------------|---------------|--------------|
| PP1 (Day 0) | `Your order is confirmed!` | `Order #{{order_number}} confirmed` | `Here's your first-use tip` |
| PP2 (Day 7) | `How's your first week going?` | `One week in — here's what to expect` | `What most people feel by now` |
| PP3 (Day 14) | `The changes happening inside you` | `What 2 weeks of minerals actually does` | `Science, not hype` |
| PP4 (Day 21) | `Heads up: box #2 ships in 9 days` | `Your next shipment is almost here` | `Plus: a way to save` |
| PP5 (Day 25) | `Quick favor? Takes 30 seconds.` | `How are you liking IonWave?` | `Your feedback helps more than you know` |
| PP6 (Day 30) | `One month in. Here's what we've learned.` | `30 days of IonWave — congratulations` | `Plus a special offer` |
| PP7 (Day 60) | `Your 60-day check-in` | `{{first_name}}, quick survey` | `Quick survey + chance to win` |

### Win-Back

| Email | Subject Line A | Subject Line B | Preview Text |
|-------|---------------|---------------|--------------|
| WB1 (60 days) | `We miss you, {{first_name}}` | `It's been a while...` | `Is everything okay?` |
| WB2 (75 days) | `A lot has changed...` | `Here's what's new at IonWave` | `Updates you might have missed` |
| WB3 (90 days) | `{{first_name}}, here's 25% off` | `Here's 25% off to come back` | `Our biggest discount` |
| WB4 (105 days) | `Should we say goodbye?` | `Last email from us (unless...)` | `We don't want to bother you` |

---

## 4. A/B Testing Framework

### Founder Mode Testing Cadence

| Volume | Testing Approach | Why |
|--------|-----------------|-----|
| <1,000 subscribers | **Don't A/B test campaigns** — sample too small for significance | Need 1,000+ sends per variant for reliable results [Confidence: B \| Source: statistical significance calculators] |
| <1,000 subscribers | **DO A/B test flow subject lines** — flows accumulate volume over time | Welcome + Cart flows will get enough sends after 2-3 months |
| 1,000-5,000 | Test 1 thing per campaign send (subject line only, or send time only) | Keep variables isolated |
| 5,000+ | Full A/B testing: subject lines, preview text, send time, content | Enough volume for statistical significance per test |

### What to Test (Priority Order)

1. **Subject line** — Highest impact, easiest to test. Test 2 variants.
2. **Send time** — Morning vs. evening. Test after subject line winner is found.
3. **Preview text** — Often overlooked. Test once subject line is optimized.
4. **CTA button text** — "Shop Now" vs. "Get Started" vs. "Claim Your Discount"
5. **Email length** — Long-form story vs. short-form direct. Test on campaigns only.

### A/B Test Protocol

1. Set variant split to 50/50
2. Wait minimum 4 hours before declaring winner (Klaviyo default)
3. Record results in a simple spreadsheet (date, flow, subject A, subject B, winner, open rate difference)
4. After 3 months, review patterns — which formula types win consistently?
5. Don't test during launches, sales, or holidays (confounding variables)

---

## 5. Subject Line Do's and Don'ts

### Do

- [ ] Front-load the benefit or hook in first 4-5 words
- [ ] Use `{{first_name}}` on 1 in 3 emails (not every one — it loses power)
- [ ] Write preview text intentionally (don't let it default to "View in browser")
- [ ] Use lowercase naturally (sentence case, not Title Case)
- [ ] Reference specific numbers when possible (78 minerals, 30-day guarantee)

### Don't

- [ ] ALL CAPS (looks spammy, triggers filters)
- [ ] More than 1 emoji per subject line
- [ ] Misleading subjects ("RE:" or "FWD:" when it's not a reply)
- [ ] Exclamation marks!!! (1 max, and sparingly)
- [ ] Spam trigger words: "FREE!!!", "Act now!", "Limited time only!!!", "Click here"
- [ ] Over-promising: "This will change your life" → tone down to "This might change your mornings"

---

## 6. Intelligence Gaps

| Gap | Current Grade | Upgrade Path |
|-----|--------------|-------------|
| IonWave-specific open rates by subject formula | D (no data) | Track after 60 days of sends |
| Emoji impact on IonWave audience | C (mixed evidence) | A/B test emoji vs. no emoji on welcome email |
| Optimal personalization frequency | C (heuristic: 1 in 3) | Track unsubscribe rates when personalization is used vs. not |
| Preview text impact on opens | C (industry data) | A/B test after subject line optimization is stable |

---

*See `email_welcome_series.md`, `email_abandoned_cart.md`, `email_post_purchase.md`, `email_winback.md` for the full sequences these subject lines belong to.*


---

### 📄 email_welcome_series.md

# M17: Welcome Email Series — Canonical Sequence

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 435 (detailed copy), 438, 439 (structural frameworks) — merged into single canonical version
**Build Priority**: #2 (build before launch)

---

## Overview

**Trigger**: Email opt-in without purchase (popup, lead magnet, footer form)
**Emails**: 5
**Timeline**: Day 0 → Day 7
**Goal**: Convert subscriber to first purchase (target: >8% CVR)
**Tone**: Personal, warm, founder-voice. Not corporate. Like a friend who discovered something amazing.

**Merge note**: Danilo provided 3 versions of the welcome series. Tab 435 had full production-quality copy for a 5-email buyer-welcome; tabs 438+439 had structural frameworks for subscriber-welcome (6-7 emails). This canonical version uses tab 435's copy quality applied to the subscriber-welcome use case, with structural guidance from 438+439.

---

## Sequence Architecture

```
Day 0 ─── Email 1: Welcome + Discount ───→ Purchased? ─── YES → Exit to Post-Purchase flow
   │                                                 └── NO ↓
Day 1 ─── Email 2: Getting Started Ritual / Why We're Different
   │
Day 3 ─── Email 3: Founder Story (René Quinton, marine plasma science)
   │
Day 5 ─── Email 4: Social Proof (customer testimonials)
   │
Day 7 ─── Email 5: Check-In + Subscription Reminder / Final Offer
```

**Exit condition**: If subscriber purchases at ANY point, remove from Welcome flow and enter Post-Purchase flow. In Klaviyo: add a conditional split checking "Has placed order since starting this flow."

---

## Email 1 — Immediate: Welcome + Deliver Promise

**Subject**: `Welcome to IonWave — here's your [X]% off`
**Preview**: `Plus: why 78 minerals changes everything`
**Send**: Immediately on signup

### Body

> Hey {{first_name}},
>
> Welcome! You just joined [X] people who are done feeling tired, foggy, and dehydrated.
>
> Here's your exclusive [X]% discount: **[CODE]**
>
> Quick intro — IonWave is different because:
> - **78 ocean-sourced minerals** (not 3-4 synthetic ones)
> - **Zero sugar, zero junk**
> - **Actually hydrates your cells** (98% bioavailable vs ~10% for pills)
>
> Over the next few days, I'll share:
> - Why most electrolytes don't work
> - The science behind ocean minerals
> - What to expect when you start
>
> For now, use code **[CODE]** for [X]% off your first order.
>
> **[CTA BUTTON: Shop Now]**
>
> Talk soon,
> [Founder Name]
>
> P.S. This code expires in 7 days. Don't miss out.

**Design notes**: Clean, minimal. Brand colors. Product hero image above the fold. CTA button prominent. No navigation bar (keep them focused).

**KPI targets**: Open rate 50-70%, Click rate 5-10% [Confidence: B | Source: Klaviyo welcome email avg for DTC]

---

## Email 2 — Day 1: Getting Started / Education

**Subject**: `{{first_name}}, here's how to get the most from IonWave`
**Preview**: `One simple ritual that changes everything`
**Send**: Day 1 after signup

### Body

> Hey {{first_name}},
>
> One quick tip that makes all the difference:
>
> **THE MORNING RITUAL**
> - Empty stomach, before coffee
> - One sachet in 8-12oz water
> - Drink it straight or add to juice — either works
>
> **WHAT TO EXPECT:**
> - **Days 1-3**: You might feel more alert, hydration that "hits different"
> - **Days 4-14**: Energy stabilizes, afternoon crashes fade
> - **Days 15-30**: Full benefits — clearer thinking, better recovery, deeper sleep
>
> The key is consistency. Your body has been running on depleted minerals for years. Give it time to recalibrate.
>
> **WHY 78 MINERALS MATTERS**
>
> Most electrolyte brands give you 3-4 minerals (sodium, potassium, maybe magnesium) plus a bunch of sugar.
>
> Your body uses 78+ minerals for over 300 enzymatic processes. IonWave delivers all of them in ionic form — the only form your cells can actually absorb.
>
> That's the difference between "drinking more water" and actual cellular hydration.
>
> Ready to feel the difference?
>
> **[CTA BUTTON: Shop Now — [X]% Off]**
>
> — [Founder Name]

**Design notes**: Simple, educational. Maybe an infographic showing "3 minerals vs 78 minerals." Keep CTA visible but don't hard-sell.

---

## Email 3 — Day 3: Founder Story / Brand

**Subject**: `Why we started IonWave (it's personal)`
**Preview**: `It started with a French biologist named René Quinton...`
**Send**: Day 3 after signup

### Body

> Hey {{first_name}},
>
> I want to tell you why IonWave exists.
>
> **THE DISCOVERY**
>
> In 1897, a French biologist named René Quinton made a discovery that changed medicine: the mineral composition of ocean water at specific depths almost perfectly mirrors human blood plasma.
>
> He called it "marine plasma" — and spent his career proving that these ocean-sourced minerals could restore health at the cellular level. His clinics treated thousands. His work was published in major journals.
>
> Then he was mostly forgotten.
>
> **WHY WE STARTED**
>
> We found Quinton's research and couldn't believe this science existed but wasn't available to everyday people. So we built IonWave:
>
> - Harvested from the same specific ocean depths Quinton identified
> - Filtered and concentrated using modern pharmaceutical-grade processes
> - 78 minerals in the exact ratios your body recognizes
>
> This isn't "electrolyte water." This is mineral restoration backed by 120+ years of science.
>
> **THE DIFFERENCE**
>
> - Seawater = 35g/L salt. Not this.
> - Synthetic electrolytes = 3-4 lab-made minerals + sugar. Not this.
> - Marine plasma = nature's full mineral spectrum, bioidentical to your blood plasma. This.
>
> Every batch we make honors that original science.
>
> Want to experience it yourself?
>
> **[CTA BUTTON: Try IonWave — [X]% Off]**
>
> — [Founder Name]
>
> P.S. If you're curious about the science, I'm happy to nerd out. Just reply.

**Design notes**: Story-driven. No product images — this is about mission and science. Founder headshot optional. Minimal design, lots of white space.

---

## Email 4 — Day 5: Social Proof

**Subject**: `"I finally stopped crashing at 2pm"`
**Preview**: `Real customers, real results`
**Send**: Day 5 after signup

### Body

> Hey {{first_name}},
>
> Don't just take our word for it. Here's what IonWave customers are saying:
>
> ---
>
> **"THE ENERGY IS DIFFERENT"**
> "I've tried every electrolyte brand. IonWave is the first one where I noticed a difference within days, not weeks. The afternoon crash is basically gone."
> — *Sarah M., Austin TX*
>
> **"FINALLY, HYDRATION THAT WORKS"**
> "I drink 3 liters of water a day and was STILL dehydrated. IonWave changed that. My skin is better, my workouts are better, everything."
> — *James K., Denver CO*
>
> **"SUBTLE BUT REAL"**
> "It's not like an energy drink that hits you and crashes. It's more like... your baseline just goes up. Steady all day."
> — *Maria L., Portland OR*
>
> **"SKEPTIC CONVERTED"**
> "My wife bought this. I thought it was woo-woo. Three weeks later I'm the one re-ordering."
> — *David R., Chicago IL*
>
> ---
>
> These are real people who were where you are now — curious but unsure.
>
> They took the chance. Their bodies did the rest.
>
> **30-day feel-the-difference guarantee.** If you don't notice a change, full refund. No questions.
>
> **[CTA BUTTON: Try Risk-Free — [X]% Off]**
>
> — [Founder Name]

**Design notes**: Testimonial-focused. Customer photos if available (even stock-style lifestyle photos work). Star ratings if you have them. Guarantee badge prominent.

**[VOID — requires: real customer testimonials]** These are placeholder testimonials from Danilo's framework. Replace with actual customer quotes once available. Until then, use only verifiable testimonials or remove this email from the flow.

---

## Email 5 — Day 7: Check-In + Final Push

**Subject**: `{{first_name}}, quick check-in`
**Preview**: `Hit reply — I read every one`
**Send**: Day 7 after signup

### Body

> Hey {{first_name}},
>
> It's been a week since you joined the IonWave community.
>
> I wanted to check in:
>
> **→ Have you tried IonWave yet?**
>
> If yes — how's it going? Reply and tell me. I read everything and respond personally.
>
> If not yet — no pressure. Here's a quick reminder of what's waiting:
>
> ✓ 78 ionic minerals (not 3-4 like synthetic brands)
> ✓ 98% bioavailable (vs ~10% for pills)
> ✓ 30-day feel-the-difference guarantee
> ✓ Free shipping on subscriptions
>
> Your code **[CODE]** is still active, but it expires in 48 hours.
>
> **[CTA BUTTON: Claim Your [X]% Off Before It Expires]**
>
> If now's not the right time, I understand. We'll keep sharing useful content — no spam, no pressure.
>
> Thanks for being here.
>
> — [Founder Name]
>
> P.S. Hit reply and tell me: what's the #1 thing holding you back? I personally respond to every email.

**Design notes**: Short, personal. No fancy design — plain text style (looks like a real email from a real person). The "reply" CTA is as important as the shop CTA — replies boost deliverability and provide qualitative insights.

---

## Flow-Level Metrics & Benchmarks

| Metric | Target (Month 1-3) | Target (Month 4+) | Source |
|--------|-------------------|--------------------|--------|
| Flow open rate (avg across 5 emails) | 45-60% | 50-65% | [Confidence: B \| Source: Klaviyo DTC welcome avg] |
| Flow click rate (avg) | 3-6% | 4-8% | [Confidence: B] |
| Welcome-to-purchase CVR | 5-8% | 8-12% | [Confidence: C \| Source: Klaviyo DTC] |
| Revenue per recipient (flow total) | $1-3 | $2-5 | [Confidence: C] |
| Unsubscribe rate per email | <0.5% | <0.3% | [Confidence: B] |

---

## Klaviyo Implementation Notes

1. **Trigger**: "Subscribed to list" → Main List (or specific signup source)
2. **Filter**: Exclude anyone who has already placed an order (they should go to buyer welcome / post-purchase)
3. **Exit condition**: If person places order → exit flow → enter Post-Purchase
4. **Smart Sending**: ON (16-hour window)
5. **Time delays**: Use "Wait X days" not specific times (adapts to subscriber timezone)
6. **Conditional split after Email 3**: If opened Email 1 OR Email 2 → continue. If 0 opens → skip to Email 5 (re-engagement/sunset approach).

---

## Intelligence Gaps

| Gap | Grade | Upgrade Path |
|-----|-------|-------------|
| Actual customer testimonials | D (placeholders used) | Collect from first 20 customers. Replace placeholders in Email 4. **HIGH PRIORITY.** |
| Optimal discount percentage | C (placeholder [X]%) | A/B test 10% vs 15% after 200+ flow entries |
| Day 7 reply rate | D (no data) | Track after 30 days. If <2% reply rate, consider changing CTA approach |
| Welcome-to-purchase CVR | D (no data) | Measure after 60 days of flow data |

---

*This is the canonical welcome series. See `email_subject_lines.md` for A/B test variants. See `email_flow_architecture.md` for how this flow fits in the lifecycle.*


---

### 📄 email_winback.md

# M17: Win-Back Email Sequence

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 444, 445 — merged
**Build Priority**: #7 (Month 3+)

---

## Overview

**Trigger**: No purchase in 60 days (for past customers only — not for never-purchased subscribers)
**Emails**: 4
**Timeline**: Day 60 → Day 105
**Goal**: Re-engage lapsed customers (target: >5% win-back rate)
**Discount escalation**: No discount → What's new → 25% off → Sunset warning

**When to build this flow:** Month 3+ only. You need 60+ days of customer data before any customer even qualifies for this flow. Don't build it at launch — there's literally no one to send it to yet.

---

## Sequence Architecture

```
Day 60 ──── Email 1: "We miss you" (emotional, no discount)
                └── Purchased? YES → Exit to Post-Purchase
                └── NO ↓
Day 75 ──── Email 2: "What's new" (updates, improvements)
                └── Purchased? YES → Exit
                └── NO ↓
Day 90 ──── Email 3: Big Offer (25% off)
                └── Purchased? YES → Exit
                └── NO ↓
Day 105 ─── Email 4: "Should we say goodbye?" (sunset warning)
                └── Engaged? YES → Keep on list, reduce cadence
                └── NO → Move to sunset/suppression
```

---

## Email 1 — Day 60: We Miss You

**Subject**: `We miss you, {{first_name}}`
**Preview**: `Is everything okay?`
**Send**: 60 days since last purchase
**Discount**: None

### Body

> Hey {{first_name}},
>
> It's been a while since we've seen you.
>
> Everything okay?
>
> Maybe you:
> - Got busy and forgot to reorder
> - Tried something else
> - Had an issue we can help with
>
> Whatever it is, we'd love to have you back.
>
> If something wasn't right with your last order, reply to this email and we'll make it right.
>
> **[CTA: Shop IonWave →]**
>
> Miss you,
>
> — [Founder Name]

**Design**: Personal, short. Plain-text style. Founder name (not "The IonWave Team"). This should feel like a real person reaching out.

---

## Email 2 — Day 75: What's New

**Subject**: `A lot has changed...`
**Preview**: `Updates you might have missed`
**Send**: 75 days since last purchase
**Discount**: None (yet)

### Body

> Hey {{first_name}},
>
> Since you last ordered, we've been busy:
>
> [DYNAMIC CONTENT — update quarterly with real news:]
>
> **NEW:** [New product / flavor / format announcement]
> **IMPROVED:** [Any product improvements, packaging updates]
> **COMMUNITY:** [Customer count milestone, review highlights]
> **CONTENT:** [Link to best recent blog post or video]
>
> We're not the same IonWave you left. We're better.
>
> Come see what's new:
>
> **[CTA: See What's New →]**
>
> — [Founder Name]

**Implementation note**: This email needs quarterly content updates. Set a calendar reminder to refresh the "What's New" content every 90 days so lapsed customers always see something fresh. [VOID — requires: quarterly content refresh process]

---

## Email 3 — Day 90: Big Offer

**Subject**: `{{first_name}}, here's 25% off to come back`
**Preview**: `Our biggest discount`
**Send**: 90 days since last purchase
**Discount**: YES — 25% off

### Body

> Hey {{first_name}},
>
> I really want you to experience IonWave again.
>
> So here's our biggest discount: **25% off.**
>
> Use code: **COMEBACK25**
>
> **[CTA: Claim 25% Off →]**
>
> Valid for 7 days only.
>
> — [Founder Name]
>
> P.S. If something wasn't right last time, reply and let me know. I'd love to make it right.

**Design**: Short, direct. Discount code prominent. No long copy — at 90 days, they know the product. Either the discount moves them or it doesn't.

**Discount rationale**: 25% is the largest discount in the IonWave email ecosystem. It's justified because: (1) the customer hasn't purchased in 90 days, (2) acquiring a new customer costs $25-40 (CAC), (3) re-activating a lapsed customer at 25% off is cheaper than acquiring a new one. [Confidence: B | Source: CAC vs. win-back economics]

---

## Email 4 — Day 105: Sunset Warning

**Subject**: `Should we say goodbye?`
**Preview**: `We don't want to bother you`
**Send**: 105 days since last purchase
**Discount**: No (the 25% offer already expired)

### Body

> Hey {{first_name}},
>
> We've been reaching out, and we haven't heard back.
>
> We don't want to clog your inbox if you're not interested anymore.
>
> **If you still want to hear from us:** Click below and we'll keep you on the list.
>
> **[CTA: Yes, Keep Me →]**
>
> **If not:** No hard feelings. You'll be removed from our email list automatically.
>
> Either way, thank you for giving IonWave a try. We're grateful you were part of this.
>
> — [Founder Name]
>
> P.S. If you ever want to come back, you can re-subscribe anytime at ionwave.com.

**Design**: Minimal, respectful. Two options: stay or leave. The "Yes, Keep Me" click re-engages them and resets their engagement score.

**Post-Email 4 logic:**
- If clicked "Keep Me" → Move back to regular nurture (reduce campaign frequency to 1x/month)
- If no engagement within 7 days → Suppress from all campaigns. Keep profile for transactional emails only.
- After 30 more days of no engagement → Consider full suppression

---

## Flow-Level Metrics & Benchmarks

| Metric | Target | Source |
|--------|--------|--------|
| Overall win-back rate (any purchase across 4 emails) | 5-10% | [Confidence: B \| Source: Klaviyo DTC avg ~5-8%] |
| Email 1 win-back rate | 2-3% | [Confidence: C \| Source: emotional appeal alone recovers ~2%] |
| Email 3 win-back rate (with 25% off) | 3-5% | [Confidence: C \| Source: discount-driven win-back rates] |
| Email 4 "Keep Me" click rate | 5-10% | [Confidence: C] |
| Sunset suppression rate | 30-50% of flow entrants | [Confidence: C \| Source: deliverability best practice] |

---

## Intelligence Gaps

| Gap | Grade | Upgrade Path |
|-----|-------|-------------|
| IonWave-specific churn reasons | D | Add exit survey to cancellation flow; mine support tickets |
| Optimal win-back offer | C | A/B test 20% vs 25% vs free shipping after 50+ flow entries |
| Re-engagement durability | D | Track: of customers won back, what % purchase again within 90 days? |
| "What's New" content refresh cadence | C | Set quarterly review; measure Email 2 open/click trends |

---

*Build this flow in Month 3+ when you have enough lapsed customers to populate it. See `email_flow_architecture.md` for build order.*


---

### 📄 opkit_email_lifecycle.md

# OpKit: Email & Lifecycle Automation Kit

**OpKit ID**: OK-M17-001
**TUP Source**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Reusability**: Any DTC brand using Klaviyo (or similar ESP) with subscription model

---

## Purpose

This OpKit enables any DTC brand to build a complete email lifecycle automation system — from first subscriber to loyal advocate. It provides the strategy, sequence scaffolds, and implementation guidance to go from zero email infrastructure to a full 12-flow lifecycle engine.

---

## Components

### 1. Instruction Doc — How to Build a DTC Email Lifecycle

**Step-by-step process:**

1. **Choose your ESP** (Klaviyo recommended for DTC/Shopify). Connect to e-commerce platform.
2. **Import brand assets** — logo, colors, fonts into email template builder.
3. **Create a master template** — header/footer consistent across all flows.
4. **Build 4 core segments** — All Subscribers, Customers, Non-Customers, VIPs.
5. **Build Priority 1 flows** (pre-launch):
   - Abandoned Cart (3 emails) — highest revenue per email
   - Welcome Series (5 emails) — sets brand tone, drives first purchase
   - Post-Purchase Basic (3 emails) — reduces refunds, drives reviews
6. **Set up signup form/popup** with email + SMS opt-in.
7. **Test all flows** with test profiles before launch.
8. **Launch**. Monitor for 30 days.
9. **Expand in Month 2**: Post-Purchase to full 7 emails, add Abandoned Checkout, Replenishment.
10. **Expand in Month 3+**: Win-Back, Browse Abandonment, Subscription Upsell, VIP.
11. **Add SMS at 500+ subscribers**: Start with shipping notifications, add cart recovery SMS.
12. **Monthly maintenance**: 1.5-4 hours/month depending on flow count. Check analytics, fix worst performer.

### 2. Grading Rubric

| Grade | Criteria |
|-------|---------|
| **A (Excellent)** | All 12 flows live. Segmentation by lifecycle + engagement. A/B testing active. Email drives 30%+ of revenue. Compliance reviewed. |
| **B (Good)** | Priority 1-2 flows live (6+ flows). Basic segmentation. Email drives 20-30% of revenue. |
| **C (Adequate)** | Priority 1 flows live (3 flows). No segmentation. Email drives 10-20% of revenue. |
| **D (Minimal)** | Only welcome popup + 1 flow. No automation. Email drives <10% of revenue. |
| **F (Absent)** | No email flows. Klaviyo connected but unused. |

**IonWave graded example**: Currently D (pre-launch, no flows live). Target: B by Month 3, A by Month 6.

### 3. Scaffold — Email Flow Templates

**For each core flow, the scaffold includes:**

- **Trigger definition** (what event starts the flow)
- **Email count and timing** (how many emails, days between)
- **Subject line formulas** (2 variants per email for A/B testing)
- **Body structure** (sections, CTAs, tone)
- **Exit conditions** (when to stop sending)
- **KPI targets** (open rate, click rate, conversion rate)

**Available scaffolds in this OpKit:**
1. Welcome Series (5 emails, Day 0-7)
2. Abandoned Cart (3 emails + SMS, 1hr-72hr)
3. Post-Purchase (7 emails, Day 0-60)
4. Win-Back (4 emails, Day 60-105)
5. Subject Line Formula Library (11 types)
6. Segmentation Framework (lifecycle + engagement + source)
7. SMS Strategy + TCPA Compliance Checklist
8. Physical Touchpoints (box inserts + direct mail)

### 4. IonWave Graded Example

IonWave's M17 content serves as the first graded example:
- **Quality**: 8.4/10
- **Strengths**: Full email sequences with actual copy, clear build order, compliance awareness, discount defense policy
- **Weaknesses**: All benchmarks are industry averages (no brand-specific data yet), health claims need legal review, testimonials are placeholders
- **Files**: 9 content files + dialogue summary + this OpKit in `data/m17/`

---

## Adaptation Guide

**To use this OpKit for a different Trade:**

1. Replace all brand-specific copy (IonWave, marine plasma, 78 minerals) with your brand's product/value prop
2. Adjust discount percentages to match your margin structure
3. Review and adapt the FTC compliance checklist for your product category
4. Keep the flow architecture, timing, and segmentation framework — these are universal DTC patterns
5. Adjust the subject line examples but keep the formula types — they work across categories
6. If not subscription-based, remove replenishment + subscription-related flows
7. If not physical product, remove box insert strategy

---

## Key Principles (Universal)

1. **Build in revenue-impact order.** Don't build 12 flows before proving the product sells.
2. **Never offer a bigger discount in a faster flow.** Time-gate your escalation.
3. **Segment when data tells you to, not because you can.** One good flow > 4 mediocre flows.
4. **Klaviyo is the source of truth once live.** Strategy docs are blueprints, not living documents.
5. **Compliance before creativity.** FTC/FD&C review before any health claim goes live.
6. **Monthly maintenance ritual.** 15 minutes to check analytics and fix the worst performer. Don't let flows rot.


---

### 📄 physical_touchpoints.md

# M17: Physical Touchpoints — Box Inserts & Direct Mail

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 429 (box inserts), 430 (direct mail)
**Build Priority**: Box inserts = Pre-Launch (low cost, high ROI). Direct mail = Month 6+ (higher cost, requires data).

---

## 1. Why Physical Touchpoints Matter

In a digital-first brand, physical touchpoints are:
- **Pattern interrupts** — customers are numb to email, but a handwritten card gets attention
- **Brand-building moments** — unboxing is the highest-emotion touchpoint in the customer journey
- **Retention tools** — physical objects stay on desks, fridges, counters (emails disappear)

**Founder Mode**: Box inserts are low-cost and high-ROI. Do them from Day 1. Direct mail is powerful but requires scale and data — defer until Month 6+.

---

## 2. Box Insert Strategy (DO THIS FROM ORDER #1)

Every package should include a set of printed inserts. These are cheap ($0.50-1.00 per package) and have outsized impact on retention, referrals, and reviews.

### Standard Insert Kit

| Insert | Purpose | Include When | Est. Cost | ROI |
|--------|---------|-------------|-----------|-----|
| **Thank You Card** | Personal touch, brand warmth | Every order | $0.15-0.20 | High — sets tone for entire experience |
| **Quick Start Guide** | Usage instructions, what to expect | First order only | $0.20-0.30 | High — reduces "I don't know how to use this" churn |
| **Referral Card** | "Give $10, Get $10" with unique code/QR | Every order | $0.15-0.20 | High — physical referral cards outperform email referral links [Confidence: C \| Source: DTC anecdotal] |
| **Sample** | Cross-sell, try new product | Every 3rd order OR with subscription renewals | $1-3 | Medium — drives product exploration |

[Confidence: B | Source: Danilo tab 429 + DTC box insert best practices]

### Thank You Card Design

**Front**: IonWave logo, clean design, "Thank You" in brand font
**Back**:
> Thank you for choosing IonWave.
>
> You're now part of a community of people who take their health seriously.
>
> **YOUR FIRST-USE TIP**: Empty stomach, before coffee. One sachet. Feel the difference.
>
> Questions? Email us at hello@ionwave.com — we respond to every message.
>
> — [Founder signature]

**Design notes**: Matte cardstock, 4x6". Brand colors. Keep it warm and human, not corporate. A handwritten-style font for the signature adds authenticity.

### Quick Start Guide Design

**Format**: Tri-fold card or single 5x7" card
**Content**:
1. **How to take**: One sachet + 8-12oz water, empty stomach, before coffee
2. **What to expect**: Days 1-3, Days 4-14, Days 15-30 (same as Email 1 post-purchase)
3. **Pro tips**: Add to juice, use before workouts, double dose during keto flu
4. **QR code**: Links to "Getting Started" page or welcome video
5. **Support**: hello@ionwave.com, reply to any email

### Referral Card Design

**Front**: "Give $10. Get $10."
**Back**:
> Share IonWave with a friend.
>
> They get $10 off their first order.
> You get $10 credit on your next order.
>
> **How**: Give them this card OR use your link:
> ionwave.com/refer/{{customer_code}}
>
> [QR CODE linking to referral page]

**Production notes**: Unique codes can be pre-printed in batches (100 per run) or use a single universal referral URL that tracks via cookies. For early stage, a universal URL is simpler.

### Print Production

| Item | Quantity | Est. Cost | Recommended Vendor |
|------|----------|-----------|-------------------|
| Thank You Cards | 500 | $75-100 | Vistaprint, local printer |
| Quick Start Guides | 250 (first orders only) | $60-90 | Vistaprint, local printer |
| Referral Cards | 500 | $75-100 | Vistaprint, local printer |
| **Total per package** | — | **$0.50-0.70** | — |

[Confidence: B | Source: Vistaprint/local printer pricing for small batch]

**Founder Mode**: Order 250-500 of each. That covers your first 250-500 orders. Reorder when you run low. Don't over-invest in printing before validating demand.

---

## 3. Direct Mail Strategy (Month 6+)

Direct mail is powerful but expensive. It works best when targeted at specific segments with data to back the investment.

### When Direct Mail Makes Sense

| Use Case | What to Send | When to Send | Expected ROI | Min. Data Required |
|----------|-------------|-------------|-------------|-------------------|
| **Win-Back** | Postcard + offer (20-25% off) | 90+ days since last order | Medium — 3-5% conversion [Confidence: C] | Need 50+ lapsed customers |
| **VIP Thank You** | Handwritten note + free gift | Top 10% by LTV | High — retention value | Need LTV data (Month 4+) |
| **Birthday/Anniversary** | Card + small discount | On customer's birthday/purchase anniversary | Medium | Need birthdate data |
| **Subscription Save** | Personal letter before cancellation | When churn signals detected | High — cheaper than re-acquisition | Need churn prediction model (Month 6+) |
| **New Product Launch** | Announcement + sample | To best 50-100 customers | Medium | Need product ready to sample |

### Why Physical Mail Works for Win-Back

- Email addresses go stale (people stop checking that inbox). Physical addresses don't.
- A postcard has zero inbox competition — it's the only "marketing email" in your mailbox today.
- The perceived effort signals "we actually care" in a way email can't replicate.

[Confidence: B | Source: Danilo tab 430 + DTC direct mail case studies]

### Direct Mail Providers

| Provider | Best For | Shopify Integration | Cost per Piece |
|----------|---------|-------------------|----------------|
| **PostPilot** | DTC Shopify brands, easy setup | Yes (native) | $0.50-2.00 depending on format [Confidence: B] |
| **Lob** | API-driven, automated triggers | Via Zapier/custom | $0.75-3.00 |
| **Postable** | Handwritten notes | Manual/API | $3-5 per note |
| **Sendoso** | Gifts and swag | Enterprise | $10+ per piece |
| **Local printer** | Package inserts only | Manual | $0.15-0.30 per piece |

**Recommendation**: Start with PostPilot for automated postcard campaigns (win-back, VIP). Use Postable or handwrite yourself for VIP thank-you notes (first 20 VIPs, it's worth the personal touch).

### Direct Mail ROI Math

**Win-back postcard example:**
- Cost per postcard: $1.50 (printed + mailed via PostPilot)
- Send to 100 lapsed customers
- Total cost: $150
- Win-back rate: 5% = 5 recovered customers
- Average order value: $59
- Revenue recovered: $295
- **ROI: ~97%** (before margin)
- After margin (~60%): Net profit ~$27 on $150 spend = **18% net ROI**

[Confidence: C | Source: derived calculation using assumed conversion rates and IonWave pricing]

**Verdict**: Viable but not urgent. Direct mail ROI is positive but modest at small scale. The real value is in VIP retention (where the emotional impact drives long-term LTV, not just one order).

---

## 4. Implementation Timeline

| Phase | Action | When |
|-------|--------|------|
| **Pre-Launch** | Design + print Thank You Cards, Quick Start Guides, Referral Cards | 2 weeks before launch |
| **Launch** | Include full insert kit in every order | Day 1 |
| **Month 3** | Track referral card usage — are physical cards driving referrals? | Review referral data |
| **Month 4** | Evaluate: do first-order customers who received Quick Start Guide have higher retention? | Compare retention rates |
| **Month 6** | If 50+ lapsed customers: run first PostPilot win-back postcard test | Send 50 postcards, measure |
| **Month 6** | Send handwritten VIP notes to top 10-20 customers | Handwrite or use Postable |
| **Month 9+** | Evaluate direct mail ROI. Scale if positive. | Analyze PostPilot results |

---

## 5. Intelligence Gaps

| Gap | Grade | Upgrade Path |
|-----|-------|-------------|
| Referral card conversion rate (physical vs. email link) | D | Track referral codes from physical cards vs. email links after 90 days |
| Quick Start Guide impact on retention | D | A/B test: orders with vs. without guide (or compare retention before/after introduction) |
| PostPilot win-back conversion rate for IonWave | D | Run 50-postcard test after Month 6 |
| Handwritten note impact on VIP LTV | D | Track VIP LTV before/after handwritten note program |
| Optimal sample inclusion frequency | C | Test every 3rd order vs. every order for cross-sell impact |

---

*Box inserts are Day 1. Direct mail is Month 6+. Both are powerful physical touchpoints in an increasingly digital-only landscape. See `email_flow_architecture.md` for how these integrate with the email lifecycle.*


---

### 📄 sms_strategy.md

# M17: SMS Strategy & Compliance

**TUP**: M17 — Email & SMS
**Version**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0
**Sources**: Danilo tabs 427, 428; TCPA regulations; Klaviyo SMS benchmarks

---

## 1. SMS at IonWave's Scale: Worth It?

**Short answer: Not yet. Defer to Month 3+.**

| Factor | Assessment |
|--------|-----------|
| Subscriber volume needed | Minimum 500 SMS opt-ins for meaningful impact [Confidence: C \| Source: DTC SMS heuristic] |
| Expected opt-in rate | 30-40% of email subscribers also opt into SMS [Confidence: B \| Source: Klaviyo SMS benchmark] |
| Cost per SMS | $0.01-0.03/message (US, Klaviyo pricing) [Confidence: B \| Source: Klaviyo pricing 2025] |
| IonWave timeline | Won't reach 500 SMS subscribers until Month 3-4 at earliest |
| **Recommendation** | **Collect SMS opt-ins from Day 1, but don't send SMS until 500+ subscribers** |

**Why collect early but send later:** Building the SMS list costs nothing (add checkbox to popup/checkout). But sending SMS to 50 people has negligible revenue impact and high per-message cost relative to email. Wait until volume justifies the channel.

---

## 2. SMS vs. Email: Channel Selection

| Use Case | Channel | Why |
|----------|---------|-----|
| **Shipping notification** | SMS | Time-sensitive, brief, high open value |
| **Flash sale (24hr or less)** | SMS | Urgency requires immediate attention |
| **Abandoned cart (last resort)** | SMS | After 2 emails, SMS is the pattern interrupt |
| **Back in stock alert** | SMS | Time-sensitive, brief |
| **VIP exclusive offer** | SMS | Feels personal, exclusive |
| **Weekly newsletter** | Email | Long-form, SMS not appropriate |
| **Educational content** | Email | Too long for SMS |
| **Post-purchase onboarding** | Email | Multi-step, needs space |
| **Review request** | Email (primary), SMS (follow-up) | Email gives context, SMS is the nudge |
| **Win-back** | Email (primary) | SMS for win-back can feel intrusive at this scale |

**Rule of thumb**: SMS for urgency and brevity. Email for everything else. [Confidence: B | Source: DTC channel strategy best practices]

---

## 3. TCPA Compliance — Non-Negotiable

The Telephone Consumer Protection Act (TCPA) governs SMS marketing. Violations carry fines of **$500-$1,500 per message**. This is not optional.

### Compliance Checklist

| Requirement | Implementation | Status |
|-------------|---------------|--------|
| **Explicit opt-in required** | Separate SMS consent checkbox (cannot be bundled with email consent) | [VOID — requires: Shopify popup/checkout implementation] |
| **Clear opt-in language** | "By checking this box, you consent to receive marketing text messages from IonWave. Msg & data rates apply. Reply STOP to unsubscribe." | Required at every collection point |
| **Easy opt-out** | Every SMS must include opt-out instructions OR honor STOP replies instantly | Klaviyo handles STOP automatically |
| **Quiet hours** | Only send between 8am-9pm **recipient's local time** | Configure in Klaviyo flow settings |
| **Never buy SMS lists** | All SMS subscribers must be organic opt-ins | Policy: hard rule, no exceptions |
| **Message frequency disclosure** | Tell subscribers how often you'll text at opt-in | "Up to 4 msgs/month" |
| **Proper sender registration** | Register toll-free number or short code with carrier | Klaviyo handles during onboarding |

[Confidence: A | Source: TCPA statute + FCC enforcement guidance]

**Founder Mode warning**: If you're unsure about SMS compliance, just don't send SMS until you've verified your setup. The fines are real and disproportionate to the revenue from early-stage SMS marketing.

---

## 4. SMS Templates

### Abandoned Cart SMS (48 hours, after Email 2)

```
Hey {{first_name}}! You left IonWave in your cart.
Complete your order: {{cart_link}}

Reply STOP to opt out
```

**Timing**: 48 hours after cart abandonment, only if Email 1 and 2 haven't converted
**Character count**: ~120 (under 160 limit)

### Shipping Notification

```
Your IonWave is on the way! 📦
Track: {{tracking_link}}
```

**Timing**: When shipping label created
**Character count**: ~65

### Flash Sale

```
24 HOURS ONLY: 25% off everything
Code: FLASH25
{{shop_link}}

Reply STOP to opt out
```

**Timing**: Sale start time (morning, 8-10am)
**Character count**: ~100

### Replenishment Reminder

```
Hey {{first_name}}! Running low on IonWave?
Reorder now: {{reorder_link}}

Or subscribe & save: {{subscribe_link}}

Reply STOP to opt out
```

**Timing**: 3 days before projected depletion
**Character count**: ~140

### Back in Stock

```
{{first_name}}, {{product_name}} is back in stock!
Get it before it sells out: {{product_link}}

Reply STOP to opt out
```

**Timing**: Immediately when back in stock
**Character count**: ~120

---

## 5. SMS Flow Integration

SMS doesn't replace email — it supplements specific flows:

| Flow | SMS Role | Trigger |
|------|----------|---------|
| Abandoned Cart | Last-resort recovery (after 2 emails) | 48hr, if no purchase and no Email 2 click |
| Replenishment | Urgency nudge | 3 days before projected depletion |
| Flash Sale (campaigns) | Primary channel for time-limited offers | Campaign send |
| Shipping | Transactional notification | Shipping label created |
| Review Request | Follow-up nudge (after email) | Day 21 post-purchase, if no review submitted |

### SMS Frequency Rules

| Rule | Setting |
|------|---------|
| Max SMS per subscriber per month | 4 messages |
| Quiet hours | 8am-9pm recipient local time |
| Flow SMS | Max 1 SMS per flow |
| Campaign SMS | Max 2 per month |
| Transactional SMS (shipping) | Always send (doesn't count toward limit) |

---

## 6. SMS Metrics & Benchmarks

| Metric | Target | Source |
|--------|--------|--------|
| SMS opt-in rate (of email subscribers) | 30-40% | [Confidence: B \| Source: Klaviyo SMS benchmarks] |
| SMS open rate | 95%+ | [Confidence: A \| Source: SMS industry data — virtually all SMS are opened] |
| SMS click rate | 15-25% | [Confidence: B \| Source: Klaviyo DTC SMS avg] |
| SMS revenue per recipient | $0.10-0.50 | [Confidence: C \| Source: DTC SMS avg — varies wildly by segment] |
| SMS unsubscribe rate | <2% per campaign | [Confidence: B \| Source: if higher, you're sending too often] |
| Cart recovery via SMS | 2-5% incremental (on top of email) | [Confidence: C \| Source: Klaviyo SMS cart recovery data] |

---

## 7. Implementation Timeline

| Phase | Action | When |
|-------|--------|------|
| **Pre-Launch** | Add SMS opt-in checkbox to popup and checkout | Before launch |
| **Pre-Launch** | Register sender number in Klaviyo | Before launch |
| **Month 1-2** | Collect SMS opt-ins passively. **Do not send any SMS.** | Ongoing |
| **Month 3** | If 500+ SMS subscribers: Launch shipping notification SMS (transactional, low risk) | Month 3 |
| **Month 3** | Add SMS to abandoned cart flow (48hr, after Email 2) | After shipping SMS is working |
| **Month 4+** | Add replenishment SMS and flash sale SMS | When comfortable with SMS channel |
| **Month 6+** | Full SMS strategy with campaign sends | When list size justifies |

---

## 8. Intelligence Gaps

| Gap | Grade | Upgrade Path |
|-----|-------|-------------|
| IonWave SMS opt-in rate | D | Measure after 60 days of popup with SMS checkbox |
| SMS cart recovery incrementality | C | A/B test: cart flow with vs. without SMS after 200+ entries |
| Optimal SMS frequency for IonWave audience | C | Start conservative (2/month), increase if unsubscribe <1% |
| SMS ROI at IonWave scale | D | Calculate after 90 days of SMS sending |
| Carrier registration requirements | B | Verify with Klaviyo during onboarding — may need A2P 10DLC registration |

---

*SMS is a high-impact channel — but only at sufficient scale. Collect opt-ins from Day 1, send from Month 3+. See `email_flow_architecture.md` for how SMS integrates with email flows.*


---

## 🔗 Dependencies & Relationships

### Feeds Into
- M18
- M19
- M20
- M24

### Requires
- M0

---

## ⚠️ Intelligence Gaps

- IonWave-specific email conversion rates (D — measure after 30 days)
- Real customer testimonials for welcome Email 4 (D — collect from first 20 customers)
- 30-day customer outcome statistics for post-purchase Email 6 (D — survey first 100 subscribers)
- FTC compliance review of health claims in post-purchase emails (D — legal review required)
- SMS ROI at IonWave's scale (D — measure after 90 days of SMS)
- Optimal discount escalation ladder (C — A/B test after 90 days)

---

## 🎯 Next Actions

Build 3 priority flows in Klaviyo before launch


---

## 🧰 OpKits

- OK-M17-001

---

---

_Report generated: 2026-02-09 17:49:43_

_Source: `data\m17`_