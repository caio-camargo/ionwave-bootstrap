# TUP M19: Customer Lifecycle & CRM

**Status:** migrated | **Quality:** 8.4/10 | **Version:** 1.0.0
**Cluster:** BCL-4 (Retention & Lifecycle)

---

## 📋 Overview

- **Workshop Date:** 2026-02-07
- **Actor:** Claude (TWP-001)
- **Protocol Used:** TWP-001 v2.0.0
- **Change Type:** initial_workshop

### Workshop Dialogue
- **Personas Used:** Data Scientist, DTC Growth Operator, Behavioral Economist
- **Rounds:** 5
- **Saturated:** True
- **Upgrades Applied:** 8
- **Unresolved Issues:** 0

### Quality Assessment
- **Score:** 8.4/10
- **Rationale:** Strong CRM architecture (model-as-CRM concept). A-grade segmentation with dual-layer approach. B-grade LTV/cohort framework (rigorous but all data is empty). B+ metrics with founder-appropriate workflow. D-grade on all actual numbers (pre-revenue estimates). 8 upgrades applied from dialogue.

---

## 📁 Content Files

- 📄 MD **data/m19/crm_architecture.md**
- 📄 MD **data/m19/lifecycle_and_segmentation.md**
- 📄 MD **data/m19/ltv_and_cohort_analysis.md**
- 📄 MD **data/m19/crm_metrics_and_dashboards.md**
- 📄 MD **data/m19/dialogue_summary.md**
- 📄 MD **data/m19/opkit_customer_lifecycle.md**
- 🔧 JSON **data/m19/_meta.json**

---

## 🔧 Structured Data

_JSON files converted to human-readable format_

_No JSON files in this TUP._

---

## 📝 Narrative Content

### 📄 crm_architecture.md

# CRM Architecture & Customer Data Model

**TUP**: M19 — Customer Lifecycle & CRM
**Version**: 1.0.0
**Last Updated**: 2026-02-07
**Source Tabs**: 451 (CRM Architecture), 452 (Customer Data Model), 455 (CRM Tab Map)

---

## 1. The Model IS the CRM

### Philosophy

Most companies treat CRM as a tool — Salesforce, HubSpot, a database you bolt on.

IonWave treats CRM as **architecture**. The entire ops model is the CRM. Every tab that touches a customer — ads, landing pages, email sequences, product experience, support, retention, referral — is a node in a single system that manages the complete customer relationship from first impression to lifetime advocacy.

The CRM is not a tool you add. The CRM is the business itself, viewed from the customer's perspective.

### Why This Matters for a Pre-Revenue Brand

This architectural view prevents the most common DTC mistake: building disconnected tools that create data silos. When you treat CRM as architecture from Day 1:

- Every customer touchpoint has a defined owner (which TUP governs it)
- Data flows are designed before tools are purchased
- Stage transitions trigger specific actions across multiple systems
- No customer falls through cracks between departments

### IonWave's CRM Stack (Phase-Gated)

| Phase | Trigger | Stack | Monthly Cost |
|-------|---------|-------|-------------|
| **Phase 1: Foundation** | Day 1 (pre-revenue) | Shopify + Klaviyo + Recharge | $50-150/mo |
| **Phase 2: Support** | First support ticket | + Gorgias Basic | $110-210/mo |
| **Phase 3: Intelligence** | 500+ customers with 6+ months of orders | + Lifetimely (cohort/LTV) | $200-400/mo |
| **Phase 4: Segmentation** | 500+ customers with 180+ days history | + Tresl Segments (RFM) | $300-500/mo |
| **Phase 5: Scale** | 5,000+ customers | + Peel Analytics OR Triple Whale | $1,000-2,000/mo |

**Principle**: No tool is purchased until the data it requires exists. Tool triggers are based on **customer count and data maturity**, not revenue. Revenue milestones are unreliable proxies — a brand at $100K revenue with 200 customers needs different tools than one at $100K with 2,000 customers. *(U4: Tool triggers by customer count, not revenue.)*

**What Shopify + Klaviyo Handle Without Additional Tools**:
- Unified customer profiles (created automatically on email/phone share)
- Basic segmentation (custom properties, tags, purchase history)
- Email/SMS automation triggers
- SSL encryption + data encryption at rest
- GDPR/CCPA deletion APIs
- Basic cohort analytics (Shopify Reports)

---

## 2. Customer Lifecycle Stages

IonWave uses a **10-stage lifecycle model** that maps the complete customer relationship. Each stage has a clear definition, transition triggers, goals, key metrics, and governing TUPs.

| Stage | Customer State | Goal | Key Metrics | Governing TUPs |
|-------|---------------|------|-------------|-----------------|
| **0. Unknown** | Has never heard of us | Create awareness | Impressions, reach, CPM | M7 (Ads), M12 (Content), M14 (UGC), M13 (Influencer) |
| **1. Aware** | Seen an ad or content, hasn't clicked | Earn attention | Hook rate, video views, engagement | M8 (VSL), M12 (Content), M7 (Ads Creative Testing) |
| **2. Interested** | Clicked through, on site, browsing | Capture intent | CTR, time on site, pages viewed, email capture rate | M6 (Landing Page), M5 (Shopify), M17 (Lead Capture) |
| **3. Considering** | Added to cart or entered email, hasn't purchased | Remove objections | Cart abandonment rate, email open rate, return visits | M17 (Abandoned Cart), M7 (Retargeting) |
| **4. First Purchase** | Just bought for the first time | Deliver exceptional first experience | CVR, AOV, CPA, time to ship | M4 (Fulfillment), M17 (Post-Purchase), M11 (Unboxing) |
| **5. Experiencing** | Has product, using it | Exceed expectations | NPS, product satisfaction, support tickets | M3 (Product Quality), M20 (CS Playbook), M17 (Check-in) |
| **6. Retained** | Bought 2+ times | Build habit | Repeat purchase rate, LTV, subscription rate | M21 (Retention), M17 (Replenishment), M10 (Subscription Offers) |
| **7. Advocate** | Actively recommends us | Amplify their voice | Referral rate, UGC submissions, review count | M26 (Referral), M14 (UGC), M27 (Reviews) |
| **8. Lapsed** | Was a customer, hasn't purchased in 60+ days | Win back | Win-back conversion rate, reactivation cost | M17 (Winback), M21 (Reactivation) |
| **9. Churned** | Gone, unlikely to return | Learn from loss | Churn rate, churn reasons, exit survey data | M20 (Churn Analysis), M17 (Sunset) |

### Stage Transition Triggers

| Transition | Trigger | Data Source | Automation |
|------------|---------|-------------|------------|
| Unknown → Aware | Ad impression or content view | Meta Pixel, Google Analytics | Automatic |
| Aware → Interested | Click-through to site | UTM tracking, Shopify | Automatic |
| Interested → Considering | Email captured OR add-to-cart | Klaviyo, Shopify | Automatic |
| Considering → First Purchase | Order placed | Shopify | Automatic |
| First Purchase → Experiencing | Order delivered | Fulfillment tracking | Automatic (3-5 day delay post-shipment) |
| Experiencing → Retained | 2nd order placed within 60 days | Shopify | Automatic |
| Retained → Advocate | Referral generated OR UGC submitted OR NPS 9-10 | Referral program, UGC platform, Survey | Automatic |
| Any Active → Lapsed | 60+ days since last purchase (one-time) OR subscription cancelled 45+ days | Computed daily | Klaviyo scheduled segment |
| Lapsed → Churned | Win-back flow completed, no response (90+ days total) | Klaviyo flow completion | Automatic |
| Churned → Re-activated | New purchase after churn | Shopify | Automatic (resets to Retained) |

### Supplement-Specific Timing

Standard lifecycle timing doesn't apply to supplements. The 30-day consumption cycle creates unique stage boundaries:

- **First Purchase → Retained**: Must happen within 45-60 days (1.5× consumption cycle), not the typical 90 days for fashion/CPG
- **At-Risk trigger**: 45+ days for one-time buyers (product should be depleted by Day 30)
- **Lapsed definition**: 60+ days (2× consumption cycle)
- **NPS timing**: Day 30 (not Day 14 like typical e-commerce — supplements need time to show results)
- **Replenishment flow**: Starts Day 20 (5 days before expected depletion)

### Non-Linear Customer Paths *(U3)*

The 10-stage model is a **measurement framework**, not a prediction that every customer follows the sequence. Real customers take shortcuts, skip stages, and oscillate:

**Common Shortcut Paths**:
- **Influencer impulse**: Unknown → First Purchase (skips Aware, Interested, Considering entirely)
- **Instant advocate**: First Purchase → Advocate (loves product immediately, tells friends before repeat buying)
- **Subscription direct**: First Purchase → VIP (converts to subscription on first order)

**Oscillation Patterns**:
- **At-Risk ↔ Retained**: Customer pauses subscription, restarts a month later, pauses again. May oscillate 3-4 times before either stabilizing or churning.
- **Lapsed → Active → Lapsed**: Seasonal buyers (e.g., summer hydration) who purchase cyclically.

**Implication**: Don't optimize exclusively for forward linear movement. Track lateral and reverse transitions too. A customer who oscillates between Retained and At-Risk 3 times is fundamentally different from one who goes At-Risk once and churns.

---

## 3. CRM Function Mapping

The ops model's TUPs map to 7 CRM functions that span the lifecycle:

| CRM Function | Lifecycle Stages | Key TUPs | Purpose |
|-------------|-----------------|----------|---------|
| **ACQUISITION** | 0-1 | M7 (Ads), M8 (VSL), M12 (Content), M14 (UGC), M13 (Influencer) | Get strangers to become aware and interested |
| **CONVERSION** | 2-4 | M6 (Landing Page), M5 (Shopify), M17 (Abandoned Cart), M10 (Pricing) | Turn interest into first purchase |
| **ONBOARDING** | 4-5 | M4 (Fulfillment), M17 (Post-Purchase), M11 (Unboxing), M3 (Product Quality) | Deliver exceptional first experience |
| **RETENTION** | 5-6 | M17 (Klaviyo Sequences), M21 (Retention), M10 (Subscription), M19 (Segmentation) | Build habit, increase frequency |
| **ADVOCACY** | 6-7 | M26 (Referral), M14 (UGC), M27 (Reviews/VOC) | Turn customers into growth engine |
| **RECOVERY** | 8-9 | M17 (Winback), M21 (Reactivation), M20 (Churn Analysis) | Win back or gracefully release |
| **INTELLIGENCE** | All | M19 (Customer Data Model, Metrics, Segmentation), M25 (Analytics), M20 (Support Data) | Understand the whole system |

### Cross-TUP Data Flows

```
M7 (Ads) → UTM/Pixel data → M19 (Acquisition Source Attribution)
M5 (Shopify) → Order data → M19 (LTV Calculation, Cohort Analysis)
M17 (Email) → Engagement data → M19 (Email Engagement Score, Lifecycle Stage)
M20 (Support) → Ticket data → M19 (Support Satisfaction, Churn Risk Score)
M21 (Retention) → Subscription data → M19 (Subscription Status, Retention Cohorts)
M19 (Segments) → Targeting → M7 (Lookalike Audiences), M17 (Segment-specific Flows)
```

---

## 4. Customer Data Model

### Customer Record Fields

Every customer record in the IonWave system contains these fields, sourced and updated by specific systems:

| Field | Source | Updated When | Used By | Privacy Level |
|-------|--------|-------------|---------|---------------|
| **Email** | Opt-in / Purchase | Once | Klaviyo, Support, Fulfillment | PII — encrypted at rest |
| **Name** | Purchase | Once | Fulfillment, Support, Personalization | PII — encrypted at rest |
| **Phone** | Opt-in / Purchase | Once | SMS (Klaviyo), Support | PII — encrypted at rest |
| **Shipping Address** | Purchase | Each order | Fulfillment | PII — encrypted at rest |
| **Lifecycle Stage** | Computed | Every interaction | All marketing automation, reporting | Internal |
| **First Touch Source** | UTM / Meta pixel | Once (at acquisition) | Attribution, CAC by channel | Internal |
| **Total Orders** | Shopify | Every purchase | Segmentation, VIP tiers | Internal |
| **Total LTV** | Shopify | Every purchase | Retention targeting, ROI analysis | Internal |
| **Days Since Last Purchase** | Computed | Daily | Winback triggers, churn prediction | Internal |
| **Subscription Status** | Shopify / Recharge | On change | Retention, forecasting | Internal |
| **NPS Score** | Survey | Post-purchase + quarterly | Product quality, advocate identification | Internal |
| **Support Tickets** | Gorgias | On ticket | Quality monitoring, experience flags | Internal |
| **Product Feedback** | Survey / Review | On submission | Product development, testimonials | Internal |
| **Referral Count** | Referral program | On referral | Advocate tier, rewards | Internal |
| **Email Engagement** | Klaviyo | Every send | Deliverability, segmentation, sunset | Internal |
| **Ad Engagement** | Meta pixel | Every interaction | Retargeting, lookalike seeds | Internal |
| **Churn Risk Score** | Computed | Weekly | Retention intervention triggers | Internal |
| **RFM Score** | Computed | Monthly | Segmentation, targeting priority | Internal |
| **Activation Status** | Computed (from M20) | Per M20 criteria | Lifecycle stage validation | Internal |

### Data Governance Rules

1. **PII fields** (Email, Name, Phone, Address): Encrypted at rest by Shopify and Klaviyo automatically. No additional encryption configuration needed.
2. **Computed fields** (Lifecycle Stage, Days Since Purchase, Churn Risk, RFM): Recalculated on schedule by Klaviyo or analytics tool.
3. **Data retention**: Follow platform defaults (Shopify retains indefinitely, Klaviyo profiles persist until suppressed).
4. **Deletion requests**: Honor within 30 days via Klaviyo's GDPR deletion tools.
5. **Consent tracking**: Opt-in/opt-out status tracked per channel (email, SMS) in Klaviyo.

### Data Privacy Compliance

**What Shopify + Klaviyo Handle Automatically**:
- SSL encryption in transit
- Data encryption at rest (commercial-grade)
- Data Processing Agreements with Standard Contractual Clauses
- GDPR/CCPA deletion APIs
- Privacy Framework self-certification

**What IonWave Must Configure** (pre-launch):
- Cookie consent banner: Install Consentmo or Pandectes ($9/month on Shopify)
- Privacy policy: Generate from Shopify template, customize for supplement business
- CCPA opt-out page: Enable in Shopify settings
- Klaviyo consent collection: Configure opt-in checkboxes on all forms
- SMS consent: Separate explicit opt-in per TCPA requirements

**Estimated Setup**: 4-8 hours initial, <1 hour/month maintenance.
**Monthly Cost**: $9-29/month (cookie consent app only).

---

## 5. Intelligence Gaps

| Gap | Priority | Validation Path |
|-----|----------|----------------|
| Actual lifecycle stage transition rates | HIGH | Track from first 100 customers |
| Real churn risk score accuracy | HIGH | Validate model after 6 months of data |
| Optimal lifecycle stage count (10 vs. simpler 6-stage) | MEDIUM | Simplify if data shows stages 0-1 and 8-9 are not actionable |
| Customer data model completeness | MEDIUM | Audit after first 500 customers — which fields are actually used for decisions? |
| CRM tab mapping accuracy | LOW | Validate as TUPs are workshopped — some tab assignments may shift |


---

### 📄 crm_metrics_and_dashboards.md

# CRM Metrics & Dashboards

**TUP**: M19 — Customer Lifecycle & CRM
**Version**: 1.0.0
**Last Updated**: 2026-02-07
**Source Tabs**: 453 (CRM Metrics Dashboard)

---

## 1. The CRM Scorecard

The CRM scorecard is the single view that tells you whether the customer relationship machine is working. It spans two layers: **funnel health** (weekly) and **relationship depth** (monthly).

### Funnel Health Metrics (Review Weekly)

These metrics track stage-to-stage conversion across the lifecycle:

| Metric | Definition | Target | Red Flag | Data Source |
|--------|-----------|--------|----------|-------------|
| **Impressions → Aware** | Hook rate on ads | >25% | <15% | Meta Ads |
| **Aware → Interested** | Ad CTR | >1.5% | <0.5% | Meta Ads |
| **Interested → Considering** | Email capture rate OR ATC rate | >5% email / >8% ATC | <2% / <4% | Shopify + Klaviyo |
| **Considering → Purchase** | Checkout conversion rate | >3% | <1.5% | Shopify |
| **First → Repeat** | 60-day repeat purchase rate | >25% | <15% | Shopify |
| **Customer → Advocate** | Referral participation rate | >10% | <3% | Referral program |
| **Retained → Lapsed** | 60-day churn rate | <20% | >35% | Computed |

### Relationship Depth Metrics (Review Monthly)

These metrics measure the quality and depth of customer relationships over time:

| Metric | Definition | Target | Red Flag | Data Source |
|--------|-----------|--------|----------|-------------|
| **Average LTV** | Total revenue ÷ Total unique customers | >$120 (12-month) | <$60 | Shopify / Lifetimely |
| **LTV:CAC Ratio** | Average LTV ÷ Average CAC | >3:1 | <2:1 | Computed |
| **NPS** | Net Promoter Score from surveys | >50 | <20 | Survey tool (Delighted / Retently) |
| **Subscription Rate** | Subscribers ÷ Total customers | >20% | <8% | Shopify / Recharge |
| **Review Rate** | Reviews ÷ Delivered orders | >15% | <5% | Review platform |
| **UGC Submission Rate** | UGC submitted ÷ Requests sent | >8% | <2% | UGC platform |
| **Support Satisfaction** | CSAT on support tickets | >90% | <75% | Gorgias |
| **Email List Health** | Active engaged ÷ Total list | >40% | <20% | Klaviyo |

### Decision Triggers

When a metric hits its red flag threshold, it triggers a specific investigation:

| Red Flag | Investigation | Owner |
|----------|--------------|-------|
| Hook rate <15% | Creative fatigue — rotate ad creative, test new hooks | M7/M8 |
| CTR <0.5% | Audience mismatch or ad creative failure | M7 |
| Email capture <2% | Landing page popup not converting — test offer/timing | M6/M17 |
| CVR <1.5% | Checkout friction or pricing objection | M5/M10 |
| Repeat rate <15% | Product satisfaction, onboarding, or replenishment flow failure | M3/M20/M17 |
| Referral <3% | No referral program OR insufficient NPS | M26 |
| Churn >35% | Systemic product or experience issue | M3/M20/M21 |
| LTV <$60 | Low repeat rate + low AOV — combined problem | M10/M19/M21 |
| LTV:CAC <2:1 | Spending too much on acquisition OR LTV too low | M7/M19 |
| NPS <20 | Product or experience failure — urgent investigation | M3/M20 |
| Sub rate <8% | Subscription offer not compelling or poorly timed | M21/M17 |
| Review rate <5% | Review request flow missing or poorly timed | M27/M17 |
| CSAT <75% | Support quality issue | M20 |
| List health <20% | Deliverability risk — sunset inactive subscribers | M17 |

---

## 2. Dashboard Architecture

### Founder Daily CRM Check-In (5 Minutes) *(U8)*

In Month 1-6, the founder IS the CRM. This daily protocol replaces formal dashboards:

**Every morning (5 minutes)**:
1. **Shopify Home** (1 min): Yesterday's orders, revenue, returning vs. new. Any new orders from subscribers?
2. **Klaviyo Dashboard** (1 min): Any flow failures? Email deliverability above 95%? Any unsubscribes from key flows?
3. **Gorgias Inbox** (2 min): Any open tickets from yesterday? Any adverse reaction reports? CSAT on last 5 closed tickets?
4. **Recharge Dashboard** (1 min): Any subscription cancellations today? Any failed payments pending?

**Decision rule**: If anything is red (order spike/drop >50%, CSAT <75%, adverse reaction, payment failure spike), stop and investigate before doing anything else.

**What you DON'T need to look at daily**: Cohort data, RFM segments, LTV calculations, NPS trends. These are weekly/monthly cadences.

### Weekly Dashboard (Founder Review)

| Section | Metrics | Source | Time to Build |
|---------|---------|-------|---------------|
| **Acquisition** | Hook rate, CTR, CPC, CPM, email captures | Meta Ads Manager + Klaviyo | 5 minutes |
| **Conversion** | Site traffic, ATC rate, CVR, AOV, revenue | Shopify Analytics | 3 minutes |
| **Retention** | Repeat purchase rate, subscription conversions, churn | Shopify + Recharge | 5 minutes |
| **Engagement** | Email open rate, click rate, SMS engagement | Klaviyo | 3 minutes |
| **Support** | Ticket volume, CSAT, first response time, activation rate | Gorgias + M20 scorecard | 5 minutes |

**Total weekly review time**: 20-25 minutes

### Monthly Dashboard (Business Review — feeds M25 MBR)

| Section | Metrics | Source |
|---------|---------|-------|
| **Lifetime Value** | Cohort LTV curves (M1/M3/M6/M12), LTV by source, blended LTV | Lifetimely / Peel |
| **Segmentation** | Segment distribution, net segment migration, VIP growth | Klaviyo / Tresl |
| **NPS & Satisfaction** | NPS trend, CSAT trend, NPS by segment, promoter conversion rate | Survey tool + Gorgias |
| **Channel Health** | LTV:CAC by source, payback period, channel grade (A-F) | Computed from Shopify + Meta |
| **Churn** | Monthly churn rate, voluntary vs. involuntary, dunning recovery rate | Recharge + Klaviyo |
| **List Health** | Active %, deliverability, unsubscribe rate, spam complaints | Klaviyo |

### Quarterly Dashboard (Strategic Review)

| Question | Metrics | Threshold for Action |
|----------|---------|---------------------|
| Are newer cohorts better? | M1 retention trend across cohorts | 3 consecutive declining cohorts → product/onboarding investigation |
| Is LTV improving? | Blended 12-month projected LTV trend | Declining 2 consecutive quarters → deep dive |
| Are channels efficient? | LTV:CAC by source, channel grade distribution | Any channel at D/F grade for 3+ months → kill or restructure |
| Is the brand health? | NPS trend, review rate, UGC rate | NPS declining 2 quarters → brand health audit |
| Is the list growing healthily? | List growth rate minus churn rate | Net negative → acquisition problem |

---

## 3. Phase-Gated Measurement Stack

### Pre-Revenue (Now)

| What to Track | How | Cost |
|---------------|-----|------|
| Email list growth | Klaviyo dashboard | $0 (included) |
| Website traffic | Google Analytics 4 | $0 |
| Social engagement | Platform native analytics | $0 |

### Month 1-3 (Launch)

| What to Track | How | Cost |
|---------------|-----|------|
| All funnel metrics | Shopify Analytics + Klaviyo | $0 (included) |
| First cohort data | Manual Google Sheet | $0 |
| Support metrics | Gorgias dashboard | $60/month (Basic) |
| Revenue by source | Shopify + UTM tracking | $0 |

### Month 3-6 ($50K+ Revenue)

| What to Track | How | Cost |
|---------------|-----|------|
| Cohort-based LTV | Lifetimely | $75-149/month |
| RFM segmentation | Tresl Segments | $29-79/month |
| All monthly metrics | Automated dashboards | Included in tools |

### Month 6-12 ($250K+ Revenue)

| What to Track | How | Cost |
|---------------|-----|------|
| Full analytics suite | Peel Analytics OR Triple Whale | $499-1,129/month |
| Advanced RFM + predictive | Included in Peel | Included |
| Channel-level LTV:CAC | Lifetimely + attribution | Included |

---

## 4. Cross-Reference with Other TUPs

| Metric Area | Primary TUP | M19's Role |
|-------------|-------------|-----------|
| **Support metrics** (CSAT, ticket volume, activation rate) | M20 — Customer Support | M19 consumes these metrics into the CRM scorecard |
| **Email metrics** (open rate, click rate, flow performance) | M17 — Email | M19 defines which flows serve which lifecycle stages; M17 reports performance |
| **Retention metrics** (subscription rate, churn, LTV) | M21 — Subscription & Retention | M19 provides the measurement framework; M21 provides the tactics |
| **Analytics infrastructure** (BI tools, reporting cadence) | M25 — Analytics | M25 builds the reporting pipes; M19 defines what to measure for CRM |
| **VOC / NPS** | M27 — Voice of Customer | M27 does deep qualitative research; M19 tracks NPS as an operational metric |
| **Acquisition metrics** (CAC, ROAS, hook rate) | M7 — Ads | M19 evaluates acquisition quality via LTV:CAC; M7 optimizes for efficiency |

---

## 5. Intelligence Gaps

| Gap | Priority | Validation Path |
|-----|----------|----------------|
| Actual funnel conversion rates at each stage | CRITICAL | Measure from Day 1 of ads; establish baseline by Month 3 |
| Realistic LTV targets (current estimates are all D-grade) | CRITICAL | Need 6+ months of cohort data |
| Email list health benchmarks for supplements | HIGH | Benchmark against Klaviyo supplement customer data |
| Optimal dashboard review frequency at founder stage | MEDIUM | Start with weekly, adjust based on signal-to-noise |
| Integration points between analytics tools | MEDIUM | Map data flows after tool stack is purchased |


---

### 📄 dialogue_summary.md

# M19 Dialogue Summary — Customer Lifecycle & CRM

**TUP**: M19
**Protocol**: TWP-001 v2.0.0
**Date**: 2026-02-07
**Rounds**: 5
**Personas**: Data Scientist, DTC Growth Operator, Behavioral Economist
**Saturation**: Yes (Round 5, all three saturated)

---

## Upgrade Log

| ID | Source Persona | Issue | Resolution | File(s) Affected |
|----|--------------|-------|------------|-------------------|
| **U1** | Data Scientist | Cohort analysis sample sizes lack confidence intervals; RFM thresholds should be distribution-based | Added 95% CI at key sample sizes; noted RFM recalibration at 500+ customers | ltv_and_cohort_analysis.md |
| **U2** | DTC Growth Operator | 10 flows pre-launch = 2-3 weeks of setup, blocking first sale | Created Minimum Viable CRM (3 flows for Day 1, 8-11 hours setup) | lifecycle_and_segmentation.md |
| **U3** | Behavioral Economist | Linear lifecycle model ignores shortcuts, skips, and oscillations | Added non-linear customer paths: shortcut transitions, oscillation patterns, measurement framing | crm_architecture.md |
| **U4** | DTC Growth Operator | Tool triggers by revenue ($50K) are unreliable; $149/month analytics at $5K/month revenue is 3% overhead | Changed to customer-count triggers (500+ customers for analytics tools) | crm_architecture.md |
| **U5** | Behavioral Economist | At-Risk is 3+ distinct profiles requiring different interventions | Split into At-Risk (Product), At-Risk (Budget), At-Risk (Attention) with tailored strategies | lifecycle_and_segmentation.md |
| **U6** | Data Scientist | Point-in-time metrics miss seasonality; supplement churn peaks in January | Added seasonality awareness, 3-month rolling averages for channel grading | ltv_and_cohort_analysis.md |
| **U7** | Behavioral Economist | Churn Risk Score undefined — just "computed weekly" with no formula | Defined Phase 1 (simple days-since-purchase) and Phase 2 (4-signal weighted model) | ltv_and_cohort_analysis.md |
| **U8** | DTC Growth Operator | Weekly dashboard is too formal for Month 1 founder; needs daily 5-minute protocol | Added Founder Daily CRM Check-In: 4 tools, 5 minutes, clear decision rule | crm_metrics_and_dashboards.md |

---

## Resolved (No Upgrade Needed)

| Round | Persona | Issue | Why Resolved |
|-------|---------|-------|--------------|
| 2 | Data Scientist | LTV:CAC ratio ignores payback period | Already addressed — payback targets by channel included in LTV by Source section |
| 3 | DTC Growth Operator | CRM Tab Map lacks priority | Priority is wave-planning (TUP Workshop Tracker), not M19's scope |
| 4 | Data Scientist | Segment migration monthly at small scale is noise | Noted — quarterly until 1,000+ customers |
| 4 | Behavioral Economist | Advocacy conflates passive (reviews) and active (referrals) | Noted in segment definitions |

---

## What Would Have Been Missed Without Dialogue

1. **Confidence intervals on cohort data** — Without U1, the playbook would have said "50 customers is enough" when 50 customers gives you a ±14% error bar. Founders would have made budget decisions on noise.

2. **3-week pre-launch paralysis** — Without U2, a solo founder would have built 10 Klaviyo flows before selling a single unit. The Minimum Viable CRM cuts this to 8-11 hours and 3 flows.

3. **At-Risk segment blindness** — Without U5, every at-risk customer gets the same win-back email. A product-disappointed customer gets a discount (insult), a budget-constrained customer gets a product reminder (irrelevant), and an attention-lapsed customer gets a personal note (overkill). Three segments, three interventions.

4. **Churn risk as black box** — Without U7, "churn risk score" was an undefined computed field. Now it has a clear formula at two complexity levels, implementable from Day 1.

5. **Tool spending before data exists** — Without U4, the playbook recommended Lifetimely at $50K revenue — potentially $149/month when monthly revenue is $4-5K. Triggering on customer count (500+) ensures the data justifies the tool.


---

### 📄 lifecycle_and_segmentation.md

# Customer Lifecycle & Segmentation

**TUP**: M19 — Customer Lifecycle & CRM
**Version**: 1.0.0
**Last Updated**: 2026-02-07
**Source Tabs**: 454 (Customer Segmentation), 456 (Customer Lifecycle Map), 457 (Customer Lifecycle), 458 (Customer Segmentation Matrix)

---

## 1. Lifecycle Stage Definitions

### Detailed Stage Model

Each lifecycle stage has precise entry/exit triggers, a primary action, a KPI, and email flows mapped to it.

| Stage | Definition | Trigger In | Trigger Out | Primary Action | KPI |
|-------|-----------|-----------|-------------|---------------|-----|
| **Prospect** | Saw an ad, visited site, hasn't purchased | Ad impression or site visit | Add to cart OR 30 days inactive | Retarget, popup, email capture | Email capture rate |
| **Lead** | Gave email, hasn't purchased | Email captured | Purchase OR 60 days inactive | Welcome flow, educational content, first offer | Welcome flow conversion rate |
| **First Purchase** | Bought once | First order placed | Second order OR 60 days post-purchase | Post-purchase flow, review request, cross-sell | Second purchase rate |
| **Repeat** | Bought 2+ times | Second order placed | Subscription OR 90 days since last order | Subscription offer, loyalty program, VIP access | Subscription conversion |
| **VIP** | 3+ purchases OR subscriber | Third order or subscription start | Churn | Exclusive access, new product previews, referral incentives | LTV, referral rate |
| **Champion** | Actively refers, creates UGC, advocates | Referral generated OR UGC submitted | Inactivity | Ambassador program, co-creation, spotlight | Referrals generated |
| **At Risk** | Expected purchase window missed | 50% past expected repurchase date | Purchase OR win-back flow complete | Win-back flow, special offer, feedback request | Win-back rate |
| **Churned** | No purchase despite win-back | Win-back flow failed | Re-purchase | Sunset flow, survey, archive | Reactivation rate |

### Email Flows by Lifecycle Stage

| Stage | Flow | Emails | Timing | Goal |
|-------|------|--------|--------|------|
| **Lead** | Welcome Series | 5 | Day 0, 1, 3, 5, 7 | First purchase |
| **Lead** | Abandoned Cart | 3 | Hour 1, Day 1, Day 3 | Complete purchase |
| **Lead** | Browse Abandon | 2 | Day 1, Day 3 | Return to site |
| **First Purchase** | Post-Purchase | 4 | Day 0, 3, 7, 14 | Education + review |
| **First Purchase** | Cross-Sell | 2 | Day 14, 21 | Second product |
| **First Purchase** | Replenishment | 3 | Day 20, 25, 30 | Reorder before depletion |
| **Repeat** | Subscription Pitch | 3 | After 2nd order: Day 3, 7, 14 | Convert to subscription |
| **VIP** | VIP Exclusives | Ongoing | Monthly | Retention + referral |
| **At Risk** | Win-Back | 3 | Day 0, 7, 14 | Re-purchase |
| **Churned** | Sunset | 2 | Day 0, 30 | Survey + final offer |

**Boundary Note**: M19 defines WHICH flow triggers WHEN (the architecture). M17 (Email) defines WHAT goes in each email (the content, design, copy). See M17 for email content specifications.

### Lifecycle Automation Architecture (Klaviyo)

### Minimum Viable CRM — Day 1 Flows *(U2)*

**A solo founder cannot build 10 flows before first sale.** The absolute minimum for Day 1:

| Flow | Setup Time | Why It Can't Wait |
|------|-----------|-------------------|
| 1. Welcome Series (3 emails) | 3-4 hours | Captures email subscribers from Day 1; no second chance at first impression |
| 2. Post-Purchase (4 emails) | 3-4 hours | Sets expectations for product experience; prevents support tickets |
| 3. Abandoned Cart (3 emails + 1 SMS) | 2-3 hours | Recovers 15-25% of abandoned carts — immediate revenue |

**Total Day 1 setup**: 8-11 hours. Everything else waits.

### Full Flow Architecture (Build Progressively)

**Tier 1 — Pre-Launch** (build before first sale, 8-11 hours):
1. Welcome Series (Email + SMS) — trigger: email/SMS signup
2. Post-Purchase Series (Email) — trigger: first order placed
3. Abandoned Cart (Email + SMS) — trigger: cart created, no checkout

**Tier 2 — Month 1-2** (add when you have data, 6-8 hours total):
4. Replenishment Flow (Email + SMS) — trigger: one-time purchase, Day 20/25/30
5. Subscription Cancel Flow (Email) — trigger: cancellation initiated
6. Dunning Flow (Email + SMS) — trigger: payment failure

**Tier 3 — Month 3+** (add when retention data exists, 4-6 hours total):
7. Win-Back Flow (Email) — trigger: 60 days since last order
8. VIP/Loyalty Flow (Email) — trigger: 3+ orders OR 90+ days subscription
9. Referral Request Flow (Email) — trigger: 2nd order OR 60 days subscription
10. Sunset/Unengaged Flow (Email) — trigger: 180 days no open/click

### Expected Flow Performance Metrics

| Flow | Open Rate | Click Rate | Conversion Rate |
|------|-----------|------------|-----------------|
| Replenishment | 50-60% | 15-20% | 10-15% |
| Abandoned Cart | 40-50% | 10-15% | 15-25% recovery |
| Win-Back | 25-35% | 5-10% | 5-8% reactivation |
| Dunning | 60-70% | 20-30% | 14% payment recovery |
| Post-Purchase | 55-65% | 15-20% | 15-20% subscription conversion (Day 14) |
| Welcome Series | 40-50% | 10-15% | 5-10% first purchase |

---

## 2. Customer Segmentation

### Behavioral Segments (Primary)

These segments drive day-to-day marketing automation and are implemented in Klaviyo:

| Segment | Definition | Size Target | Strategy | Key Automation |
|---------|-----------|-------------|----------|----------------|
| **Prospects (Email Only)** | Opted in, never purchased | 30-40% of list | Nurture → First purchase | Welcome Series |
| **One-Timers** | 1 purchase, no repeat | 25-35% of customers | Convert to repeat buyer | Replenishment + Subscription Offer |
| **Repeat Buyers** | 2+ purchases, no subscription | 15-25% of customers | Convert to subscriber | Subscription pitch + VIP path |
| **Subscribers** | Active subscription | 10-20% of customers | Retain + upsell + activate as advocate | VIP Recognition + Referral |
| **VIPs** | 3+ purchases OR $200+ LTV OR active referrer | 5-10% of customers | White-glove treatment, ambassador program | Exclusive offers + early access |
| **At-Risk (Product)** | Negative feedback, support complaint, low NPS | 3-5% of active | Address product concern, offer alternative | Product-specific intervention |
| **At-Risk (Budget)** | Subscription paused citing cost, skipped orders | 3-5% of active | Downgrade offer, smaller pack, payment flexibility | Budget retention offer |
| **At-Risk (Attention)** | No engagement 45+ days, no negative signal | 4-5% of active | Reminder, re-engagement content, replenishment nudge | Replenishment + re-engagement |
| **Lapsed** | 60-90 days, no purchase | 10-20% of historical | Win back or sunset | Winback sequence |
| **Churned** | 90+ days, no engagement | 20-30% of historical | Clean from active list, suppress ads | Sunset + Suppression |

### RFM Segmentation (Advanced)

RFM (Recency, Frequency, Monetary) analysis provides a deeper, data-driven segmentation layer. **Implement after 500+ customers with order history.**

**RFM Scoring for Supplements (30-Day Consumption Cycle)**:

| Factor | Score 5 | Score 4 | Score 3 | Score 2 | Score 1 |
|--------|---------|---------|---------|---------|---------|
| **Recency** (days since last purchase) | 0-20 | 21-35 | 36-60 | 61-90 | 90+ |
| **Frequency** (number of purchases) | 5+ orders | 3-4 orders | 2 orders | 1 order (sub) | 1 order (one-time) |
| **Monetary** (total spend) | $250+ | $150-249 | $100-149 | $55-99 | <$55 |

**RFM Segments**:

| Segment | RFM Profile | Strategy |
|---------|------------|----------|
| **Champions** | R:4-5, F:4-5, M:4-5 | Loyalty program, early access, referral program |
| **Loyal** | R:3-5, F:3-5, M:3-5 | Upsell, cross-sell, request reviews |
| **Potential Loyalist** | R:4-5, F:2-3, M:2-4 | Nurture to loyalty, subscription push |
| **New Customers** | R:4-5, F:1, M:1-3 | Onboarding, education, quick win |
| **Promising** | R:4-5, F:1, M:1-2 | Engage before they forget |
| **Need Attention** | R:2-3, F:2-4, M:2-4 | Win-back campaign, special offer |
| **At Risk** | R:2-3, F:2-4, M:2-4 | Aggressive win-back, survey why |
| **Can't Lose** | R:1-2, F:4-5, M:4-5 | Personal outreach, whatever it takes |
| **Hibernating** | R:1-2, F:1-2, M:1-2 | Deep discount or let go |
| **Lost** | R:1, F:1, M:1 | Hail mary or remove from list |

**Segment Count by Company Stage**:
- <1,000 customers: **6-8 segments** (behavioral segments above are sufficient)
- 1,000-10,000 customers: **8-10 segments** (add RFM layer)
- 10,000+ customers: **11 segments** (full RFM + behavioral)

**Implementation Path**:
1. **Phase 1 (0-500 customers)**: Use Klaviyo's built-in segmentation with manual criteria. Free.
2. **Phase 2 (500-5,000 customers)**: Add Tresl Segments ($29-79/month) or Lifetimely ($75-149/month) for automated RFM.
3. **Phase 3 (5,000+)**: Peel Analytics ($499+/month) for full automation + Slack alerts.

**Klaviyo Requirements for RFM**: Minimum 500 customers with orders, 180 days order history, orders within last 30 days, some customers with 3+ orders.

### Segment Migration Tracking

Track monthly: how many customers moved up or down segments.

**Goal**: Move customers UP the ladder, prevent downward drift.

| Movement | What It Means | Action |
|----------|--------------|--------|
| New → Repeat ↑ | Second purchase happened | Celebrate, push subscription |
| Repeat → VIP ↑ | High-value customer forming | Unlock VIP perks |
| Active → At-Risk ↓ | Missing expected purchase | Trigger intervention |
| At-Risk → Churned ↓ | Win-back failed | Exit survey, suppress |
| Churned → Active ↑ | Reactivation success | Reset lifecycle, celebrate |

**Monthly Report** (add to MBR from M25):
- Net segment migration (positive = healthy business)
- Segment distribution vs. targets
- Segment-to-segment conversion rates
- Cohort-specific migration patterns

---

## 3. Customer Lifecycle Map (Simplified View)

For quick reference — the full journey from first touch to advocate:

| Stage | Timeframe | Goal | Key Touchpoints | Success Metric |
|-------|-----------|------|-----------------|----------------|
| **Awareness** | Day 0 | Capture attention | Ad (Meta, TikTok) | Hook rate >25% |
| **Interest** | Day 0-3 | Build desire | Landing page, retargeting | CTR >1.5% |
| **Consideration** | Day 1-14 | Remove objections | Email capture, abandoned cart flow | ATC >8% |
| **Purchase** | Day 1-14 | Confirm decision | Order confirmation, payment | CVR >3% |
| **Onboarding** | Day 3-10 | Great first use | How-to content, unboxing | Delivery satisfaction |
| **Retention** | Day 30-90 | Build habit | Replenishment, subscription offer | 2nd purchase >25% |
| **Advocacy** | Day 180+ | Amplify voice | Referral program, review request | Referral rate >10% |

---

## 4. Intelligence Gaps

| Gap | Priority | Validation Path |
|-----|----------|----------------|
| Actual segment size distribution | HIGH | Measure after first 200 customers |
| RFM threshold accuracy for supplements | HIGH | Calibrate after 6 months of cohort data |
| Optimal number of segments at launch | MEDIUM | Start with 6 behavioral, add RFM at 500 customers |
| Segment migration velocity | MEDIUM | Track monthly from Month 3 |
| Real at-risk trigger timing (45 days vs. product-specific) | HIGH | Validate Day 45 hypothesis against actual repurchase curves |
| Lifecycle stage transition rates | HIGH | Track from Day 1, publish after 100 customers |


---

### 📄 ltv_and_cohort_analysis.md

# LTV & Cohort Analysis

**TUP**: M19 — Customer Lifecycle & CRM
**Version**: 1.0.0
**Last Updated**: 2026-02-07
**Source Tabs**: 459 (LTV by Acquisition Source), 460 (Cohort Analysis), 461 (Cohort Analysis Tracker), 462 (Cohort Analysis Template), 463 (LTV Calculation Models)

---

## 1. LTV Calculation Methods

### Three Methods, One Winner

| Method | Formula | Accuracy | When to Use |
|--------|---------|----------|-------------|
| **Simple LTV** | AOV × Purchase Frequency × Lifespan | Low | Back-of-napkin estimates only |
| **Churn-Based LTV** | ARPU × Gross Margin ÷ Monthly Churn Rate | Medium | Mature subscription businesses with stable churn |
| **Cohort-Based LTV** ★ | Track actual revenue per cohort over time | High | **Recommended for IonWave** |

### Method 1: Simple LTV (For Quick Estimates Only)

**Formula**: LTV = AOV × Purchase Frequency × Average Lifespan

**IonWave Example** (pre-revenue estimates):
- AOV = $55 (sachet box)
- Purchase Frequency = 4×/year (30-day supply, not all repurchase on time)
- Average Lifespan = 2 years
- **LTV = $55 × 4 × 2 = $440**

**Why this is wrong**: Assumes constant behavior. Real customers have steep early drop-off then plateau. This number is aspirational, not operational.

### Method 2: Churn-Based LTV (For Subscription Modeling)

**Formula**: LTV = Monthly ARPU × Gross Margin ÷ Monthly Churn Rate

**IonWave Subscription Example**:
- Monthly Revenue per Customer (ARPU) = $45 (subscription price)
- Gross Margin = 70%
- Monthly Churn Rate = 5% (target)
- **LTV = ($45 × 0.70) ÷ 0.05 = $630**

At 8% churn: LTV = ($45 × 0.70) ÷ 0.08 = **$393.75**
At 3% churn: LTV = ($45 × 0.70) ÷ 0.03 = **$1,050**

**Key Insight**: Reducing churn from 8% to 5% monthly increases LTV by 60%. Reducing from 5% to 3% increases LTV by another 67%. **Churn reduction is the highest-leverage activity in the entire business.**

**Why this isn't perfect**: Assumes constant churn rate. In reality, churn is highest in Month 1-3, then drops sharply for retained customers. This method overestimates early-stage LTV and underestimates mature LTV.

### Method 3: Cohort-Based LTV ★ (Recommended)

Track actual revenue generated by each monthly cohort over time. No assumptions — just data.

**How It Works**:
1. Group customers by acquisition month (e.g., "Feb 2026 cohort" = all customers acquired in February 2026)
2. Track total revenue from that cohort each subsequent month
3. Divide by cohort size = Per-customer LTV curve
4. Extrapolate stabilized curve = Projected lifetime LTV

**IonWave Cohort Example** (hypothetical, D-grade data quality):

| Cohort | Customers | M0 Rev | M1 Rev | M2 Rev | M3 Rev | M6 Rev | M12 Rev | Cumulative LTV/Customer |
|--------|-----------|--------|--------|--------|--------|--------|---------|------------------------|
| Feb 26 | 100 | $5,500 | $2,200 | $1,800 | $1,500 | $900 | $700 | ~$150 (M12) |
| Mar 26 | 150 | $8,250 | $3,700 | $2,800 | $2,400 | ... | ... | ... |
| Apr 26 | 200 | $11,000 | $5,000 | ... | ... | ... | ... | ... |

**Reading the Staircase**:
- M0 always = 100% (first purchase)
- M1 = ~40% of M0 revenue (60% of first-timers don't reorder in Month 1)
- M2 = ~33% of M0 revenue
- M3 = ~27% of M0 revenue
- The curve flattens: customers who survive to M3 are likely to stay

**When to Trust Cohort Data**:
- **Minimum cohort size**: 50-100 customers per cohort for directional insights
- **Minimum data window**: 6 months of cohort tracking before making LTV-based decisions
- **Statistical confidence**: 12+ months of data for investment-grade LTV projections

**Tool Recommendation**: Lifetimely ($75-149/month) automates cohort-based LTV tracking for Shopify. Implement at $50K+ revenue.

---

## 2. LTV by Acquisition Source

Not all customers are created equal. A customer acquired through referral may be worth 25% more than one acquired through Meta prospecting — even at higher CAC.

### Source Performance Tracker

| Source | Customers | CAC | M0 Rev | M3 LTV | M6 LTV | M12 LTV | Projected LTV | LTV:CAC | Payback (Mo) | Grade |
|--------|-----------|-----|--------|--------|--------|---------|---------------|---------|-------------|-------|
| Meta - Prospecting | — | — | — | — | — | — | — | — | — | — |
| Meta - Retargeting | — | — | — | — | — | — | — | — | — | — |
| Meta - Lookalike | — | — | — | — | — | — | — | — | — | — |
| Google - Brand | — | — | — | — | — | — | — | — | — | — |
| Google - Non-Brand | — | — | — | — | — | — | — | — | — | — |
| TikTok | — | — | — | — | — | — | — | — | — | — |
| Influencer | — | — | — | — | — | — | — | — | — | — |
| Organic | — | — | — | — | — | — | — | — | — | — |
| Referral | — | — | — | — | — | — | — | — | — | — |
| **BLENDED** | — | — | — | — | — | — | — | — | — | — |

*All fields empty — populate after first 3 months of operation.*

### Grading Scale

| Grade | Criteria | Action |
|-------|----------|--------|
| **A** | LTV:CAC > 4×, Payback < 3 months | Scale aggressively |
| **B** | LTV:CAC 3-4×, Payback 3-6 months | Scale steadily |
| **C** | LTV:CAC 2-3×, Payback 6-9 months | Maintain, optimize |
| **D** | LTV:CAC 1-2×, Payback 9-12 months | Reduce, test fixes |
| **F** | LTV:CAC < 1× | Kill or drastically change |

### Expected LTV Hierarchy (Pre-Revenue Estimates, D-Grade)

Based on DTC supplement industry patterns:

1. **Referral**: ~1.2× baseline LTV (highest quality, trust-driven, lowest CAC once established)
2. **Organic Search**: ~1.15× baseline LTV (high intent, no promotional dependency)
3. **Google Brand Search**: ~1.1× baseline LTV (brand-aware, high intent)
4. **Meta Prospecting (Content-first)**: ~1.0× baseline LTV (longer nurture, higher retention potential)
5. **Google Non-Brand Search**: ~0.95× baseline LTV (high intent but cold)
6. **Influencer**: ~0.9-1.1× baseline LTV (depends on influencer-product fit)
7. **Meta Retargeting**: ~0.9× baseline LTV (faster conversion, but discount-driven = lower retention)
8. **TikTok**: ~0.8-1.0× baseline LTV (high variance, execution-dependent)

**Critical Insight**: Don't optimize for CAC alone. A source with $60 CAC but $300 LTV (5:1) beats a source with $30 CAC but $90 LTV (3:1). Always evaluate on LTV:CAC ratio with payback period.

### LTV:CAC Benchmarks

| Ratio | Meaning | Status |
|-------|---------|--------|
| **1:1** | Losing money (CAC = LTV) | 🔴 Kill |
| **2:1** | Break even after COGS + overhead | 🟡 Warning |
| **3:1** | Healthy business | 🟢 Target |
| **4:1** | Very healthy, room to scale | 🟢 Scale |
| **5:1+** | Potentially under-investing in growth | 🔵 Invest more |

**IonWave Targets**:
- Year 1 (building data): 3:1 blended LTV:CAC minimum
- Year 2 (optimization): 4:1+ blended, with per-source grading
- Individual sources below 2:1 for 3 consecutive months → reduce or kill

### Payback Period Targets by Channel

| Channel | Acceptable Payback | Why |
|---------|-------------------|-----|
| Referral / Organic | 1-2 months | Low CAC, fast recycling |
| Google Brand | 2-3 months | High intent, moderate CAC |
| Meta Prospecting | 3-6 months | Investment in LTV; higher CAC but builds base |
| Meta Retargeting | <60 days | Fast cash recycling; if payback is longer, retargeting is broken |
| Google Non-Brand | 3-4 months | Moderate CAC, cold traffic |
| TikTok | 3-6 months | Only if creative strategy is working |

---

## 3. Cohort Analysis Framework

### Revenue Retention by Cohort

Track the percentage of M0 revenue retained each subsequent month:

| Cohort | Customers | M0 | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | LTV |
|--------|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|-----|
| Jan 26 | — | 100% | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Feb 26 | — | 100% | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Mar 26 | — | 100% | — | — | — | — | — | — | — | — | — | — | — | — | — |
| ... | — | 100% | — | — | — | — | — | — | — | — | — | — | — | — | — |

### Revenue Retention Benchmarks (Supplement Industry)

| Month | Good | Excellent | Red Flag |
|-------|------|-----------|----------|
| **M1** | >70% | >80% | <50% |
| **M3** | >50% | >65% | <35% |
| **M6** | >40% | >55% | <25% |
| **M12** | >30% | >45% | <20% |

### Customer Retention by Cohort (Separate Table)

Track what % of customers from each cohort are still purchasing:

| Month | Industry Avg | IonWave Target | Red Flag |
|-------|-------------|----------------|----------|
| **M1** | 40-50% | 45%+ | <30% |
| **M3** | 30-35% | 35%+ | <20% |
| **M6** | 25-30% | 30%+ | <15% |
| **M12** | 20-25% | 25%+ | <12% |

**Supplement-Specific Note**: 21.5% of new supplement customers make a 2nd purchase within the first year. IonWave's target of 25%+ at M12 requires exceptional onboarding and product experience — it's ambitious but achievable with the M20 activation framework.

### How to Read the Cohort Table

1. Each row = customers acquired that month
2. M0 = first month (always 100%)
3. Mn = % of M0 revenue retained in month n+1
4. **Compare diagonally**: If March cohort's M1 is better than February cohort's M1, your onboarding improved
5. **Compare vertically**: If M3 column is consistently >50%, your product delivers enough value to retain
6. **The "smile curve"**: Best-in-class DTC brands see revenue retention curve flatten or slightly increase after M6 as retained customers become subscribers/VIPs

### Cohort Review Cadence

| Frequency | What to Review | Action Threshold |
|-----------|---------------|-----------------|
| **Weekly** | M1 retention for latest cohort | <30% → immediate product/onboarding investigation |
| **Monthly** | M1-M6 retention trends, segment migration | Any month declining vs. prior cohort → diagnose |
| **Quarterly** | Full LTV curves, LTV by source, cohort quality trends | Inform M25 MBR, adjust channel spend, validate HYP-003 |

### Minimum Data Requirements *(U1: Statistical Rigor)*

| Decision Type | Minimum Cohort Size | Minimum Time Window | 95% Confidence Interval |
|--------------|---------------------|-------------------|------------------------|
| Directional trends | 50 customers | 3 months | ±14% at 40% retention (wide — treat as signal, not certainty) |
| Operational decisions | 100 customers | 6 months | ±10% at 40% retention (narrow enough for budget decisions) |
| Investment-grade projections | 200+ customers | 12 months | ±7% at 40% retention (investor-ready) |
| Per-source LTV comparison | 50 per source | 6 months per source | ±14% — compare sources only when confidence intervals don't overlap |

**How to interpret**: At 50 customers, if you measure 40% retention, the true retention rate is somewhere between 26% and 54% (95% CI). You can't distinguish "healthy" from "concerning" — you can only detect catastrophic failures (<20%) or clear successes (>60%). Don't make budget-allocation decisions on 50-customer cohorts.

**RFM Threshold Note**: RFM scoring thresholds (Recency: Score 5 = 0-20 days, etc.) should be recalibrated as your customer base grows. These are starter values based on supplement industry patterns. After 500+ customers, switch to **distribution-based percentiles** (top 20% = Score 5, next 20% = Score 4, etc.) instead of fixed cutoffs.

---

## 4. Churn Analysis

### Monthly Churn Rate Benchmarks

| Rating | Monthly Churn | What It Means |
|--------|-------------|---------------|
| **Excellent** | <3% | Best-in-class supplement subscription |
| **Good** | 3-5% | Healthy, sustainable growth |
| **Acceptable** | 5-7% | Industry average for $39-49 supplements |
| **Concerning** | 7-10% | LTV compression, investigate immediately |
| **Critical** | >10% | Business model at risk |

### Seasonality in Churn *(U6)*

Supplement churn is NOT uniform throughout the year. Known seasonal patterns:

| Period | Churn Pattern | Why | Implication |
|--------|-------------|-----|-------------|
| **January** | Higher (New Year's resolutions fade by Week 3) | Resolution-driven signups have lower commitment | Don't panic at January churn spikes — compare to January prior year, not December |
| **Summer (Jun-Aug)** | Moderate increase (travel, routine disruption) | Vacation disrupts daily supplement routine | Pause option + "travel pack" messaging |
| **September** | Lower (back-to-routine) | People re-establish habits | Good time for win-back campaigns |
| **November-December** | Variable (holiday budgets) | Discretionary spending shifts to gifts | Retention offers, subscription-as-gift option |

**Metric Rule**: Evaluate channel grades and churn trends using **3-month rolling averages**, not point-in-time snapshots. A channel grading D in one month may be B over a quarter. Only kill or restructure channels that grade D/F on a 3-month rolling basis.

### Voluntary vs. Involuntary Churn

| Type | % of Total Churn | Cause | Solution |
|------|-----------------|-------|----------|
| **Voluntary** | ~78% | Customer decision (product dissatisfaction, budget, competitor, not needed) | Product quality, onboarding, engagement flows |
| **Involuntary** | ~22% | Failed payments (expired card, insufficient funds, bank decline) | Dunning flow, card updater, retry logic |

**Critical Insight**: Involuntary churn is 22% of total churn and is almost entirely recoverable with a proper dunning flow. Setting up Recharge + Klaviyo dunning immediately recovers ~14% of failed payments. This is free revenue with zero CAC.

### Churn Reduction Priority Stack

1. **Dunning flow** (recovers involuntary churn) — implement Day 1
2. **Replenishment flow** (prevents product gap) — implement Day 1
3. **Post-purchase onboarding** (sets expectations) — implement Day 1
4. **Subscription cancel prevention** (pause option) — implement Month 1
5. **At-risk intervention** (proactive outreach) — implement Month 3
6. **Win-back flow** (recovers voluntary churn) — implement Month 3

### Churn Risk Score Formula *(U7)*

The customer data model includes a "Churn Risk Score" field. Here's how to compute it:

**Phase 1 (Day 1 — Manual/Simple)**:
```
Churn Risk = Days Since Last Purchase / Expected Repurchase Days × 100
```
- Expected Repurchase Days = 35 (supplement 30-day supply + 5-day buffer)
- Score >100 = past expected repurchase date
- Score >150 = high risk
- Score >200 = likely churned

**Phase 2 (Month 6+ — Multi-Signal)**:

| Signal | Weight | Scoring | Data Source |
|--------|--------|---------|-------------|
| **Purchase velocity change** | 30% | Compare last inter-purchase interval to average. Score 0-100 (100 = dramatically slowed). | Shopify |
| **Email engagement decline** | 25% | 30-day rolling open/click rate vs. lifetime average. Score 0-100 (100 = zero engagement). | Klaviyo |
| **Subscription modifications** | 25% | Skip = +20, Pause = +40, Frequency decrease = +30, Cancel initiated = +80. | Recharge |
| **Support ticket sentiment** | 20% | No ticket = 0, Positive resolution = 10, Unresolved complaint = 60, Multiple complaints = 80. | Gorgias |

**Composite Score** = Weighted average of all signals (0-100 scale).

| Score | Risk Level | Action |
|-------|-----------|--------|
| 0-30 | Low | No intervention needed |
| 31-50 | Moderate | Monitor, include in proactive engagement |
| 51-70 | High | Trigger At-Risk intervention flow |
| 71-100 | Critical | Personal founder outreach (Month 0-6) or Tier 3 support (Month 6+) |

**Implementation**: Phase 1 can be done in a Klaviyo calculated property. Phase 2 requires Lifetimely or custom computation (implement at 500+ customers).

---

## 5. Intelligence Gaps

| Gap | Priority | Validation Path |
|-----|----------|----------------|
| Actual cohort retention curves for marine plasma | CRITICAL | Track from first 100 customers; compare to supplement benchmarks |
| Real LTV by acquisition source | CRITICAL | Requires 6 months of data per source with 50+ customers each |
| Supplement consumption cycle (is it really 30 days?) | HIGH | Track reorder timing for first 200 customers — may be 35-45 days |
| Churn rate baseline (5% target vs. reality) | HIGH | Measure from Month 3 when subscription base forms |
| Involuntary churn % (22% industry avg vs. IonWave actual) | HIGH | Track after Recharge + dunning setup |
| LTV:CAC by source (needed for budget allocation) | HIGH | Requires 6+ months per-source cohort data |
| Optimal payback period by channel | MEDIUM | Calibrate after 12 months of multi-channel data |
| Cohort size needed for statistical significance at IonWave's scale | MEDIUM | Consult with data analyst when approaching 500 customers |


---

### 📄 opkit_customer_lifecycle.md

# OpKit: Customer Lifecycle & CRM Operations (OK-M19-001)

**Type**: Production OpKit
**Domain**: Customer Lifecycle Management & CRM
**Applicable To**: Any DTC brand (supplement-specific sections flagged)
**Source TUP**: M19 — Customer Lifecycle & CRM
**Version**: 1.0.0
**Date Created**: 2026-02-07

---

## 1. Instruction Doc — How to Build a DTC Customer Lifecycle System

### Step-by-Step (8 Steps)

**Step 1: Define Your Lifecycle Stages**
- Choose 6-8 stages (more than 8 adds complexity without value at <5,000 customers)
- Each stage needs: Definition, Trigger In, Trigger Out, Primary Action, KPI
- Start with: Prospect → Lead → First Purchase → Repeat → VIP → At Risk → Churned
- Add Champion/Advocate stage when you have 500+ customers
- For consumables: adjust timing to product consumption cycle, not calendar time

**Step 2: Choose Your CRM Stack**
- Phase 1 (Day 1): Shopify + Klaviyo + Subscription tool (Recharge, Loop, Skio)
- Phase 2 (500+ customers): Add analytics tool (Lifetimely, Peel, Triple Whale)
- Phase 3 (500+ customers with 180+ days): Add RFM segmentation (Tresl Segments, Klaviyo built-in)
- Do NOT purchase analytics tools before you have the data to feed them
- Tool purchases trigger on customer count, not revenue

**Step 3: Build Minimum Viable Automation (Day 1)**
- Build ONLY 3 flows before first sale:
  1. Welcome Series (3 emails, Day 0/1/3) — ~3 hours setup
  2. Post-Purchase Series (4 emails, Day 0/3/7/14) — ~3 hours setup
  3. Abandoned Cart (3 emails + 1 SMS, Hour 1/Day 1/Day 3) — ~2 hours setup
- Everything else (replenishment, win-back, VIP, sunset) waits until you have data
- Total Day 1 setup: 8-11 hours

**Step 4: Implement Customer Segmentation**
- Start with behavioral segments in Klaviyo (built-in, free):
  - Prospects (email only), One-Timers, Repeat Buyers, Subscribers, VIPs, At-Risk, Lapsed, Churned
- At 500+ customers: implement RFM scoring
  - Score each customer 1-5 on Recency, Frequency, Monetary
  - Create 6-8 RFM segments with specific strategies per segment
- For consumables: adjust Recency thresholds to consumption cycle (30-day supply → Score 5 if purchased within 20 days)

**Step 5: Set Up Your Metrics Dashboard**
- Daily (5 minutes): Check orders, email health, support inbox, subscription cancellations
- Weekly (20 minutes): Full funnel conversion, retention metrics, email performance
- Monthly: Cohort LTV, segment migration, channel health, NPS
- Quarterly: Full LTV curves, strategic channel decisions, brand health audit

**Step 6: Implement Cohort Analysis**
- Month 1-6: Manual Google Sheet (free) — track customers by acquisition month, revenue per month
- Month 6+: Automated with Lifetimely or similar tool
- Track both revenue retention AND customer retention by cohort
- Compare cohorts diagonally (are newer cohorts better?) and vertically (does retention stabilize?)

**Step 7: Build Your Churn Prevention Stack**
- Priority 1: Dunning flow (recover failed payments) — 22% of churn is involuntary
- Priority 2: Replenishment flow (prevent product gap) — trigger before product depletion
- Priority 3: Subscription cancel prevention (offer pause/skip)
- Priority 4: At-risk intervention (segment at-risk customers by reason: product, budget, attention)
- Priority 5: Win-back flow (3 emails over 30 days for lapsed customers)

**Step 8: Calculate and Track LTV**
- Pre-data: Use Simple LTV (AOV × frequency × lifespan) for fundraising/planning
- Month 3+: Start churn-based LTV for subscription projections
- Month 6+: Switch to cohort-based LTV (most accurate, requires data)
- Track LTV by acquisition source — some channels produce higher-LTV customers
- Target: 3:1 LTV:CAC minimum; 4:1+ for healthy scaling

### For Supplement/Health Brands — Additional Considerations
- Consumption cycle timing: Adjust lifecycle and replenishment triggers to product supply duration (30/60/90 days)
- Expected outcomes timeline: Supplements need longer evaluation periods than typical DTC (30-90 days for results vs. instant gratification)
- NPS timing: Survey at Day 30+ (product needs time to show value), not Day 7
- At-risk sub-segmentation: Product-disappointed vs. budget-constrained vs. attention-lapsed require different interventions
- Churn seasonality: January resolution fade, summer routine disruption, holiday budget shifts

---

## 2. Grading Rubric

| Dimension | A (Excellent) | B (Good) | C (Adequate) | D (Weak) | F (Failing) |
|-----------|--------------|----------|--------------|----------|-------------|
| **Lifecycle Model** | 6-8 stages with triggers, KPIs, email mapping, non-linear paths acknowledged | 6+ stages with triggers and KPIs | Stages defined but no triggers | Vague "awareness → purchase → retention" | No lifecycle model |
| **Segmentation** | Behavioral + RFM dual-layer, at-risk sub-segments, phase-gated implementation | 6+ behavioral segments with strategies | Basic segments (new/returning/VIP) | Ad-hoc targeting | No segmentation |
| **LTV & Cohort Analysis** | Cohort-based LTV tracking, LTV by source, confidence intervals, seasonal adjustment | LTV tracked monthly with cohort framework | Simple LTV calculated, basic retention | Revenue-focused, no cohort analysis | No LTV calculation |
| **Metrics & Dashboards** | Daily + weekly + monthly cadence, decision triggers, founder-appropriate workflow | Weekly review with key metrics | Some metrics tracked but no cadence | Occasional Shopify checks | No systematic measurement |
| **Churn Prevention** | Multi-signal risk score, at-risk sub-segments, dunning + replenishment + intervention flows | Risk identification with intervention flows | Basic win-back flow only | Reactive to cancellations | No churn prevention |
| **CRM Stack** | Phase-gated by customer count, tool triggers defined, no premature spending | Appropriate tools for stage | Some tools, some unnecessary for stage | Over-tooled or under-tooled | No CRM tools |

---

## 3. Graded Example — IonWave (Trade #84)

| Dimension | Grade | Rationale |
|-----------|-------|-----------|
| Lifecycle Model | **B+** | 8 operational stages with triggers, KPIs, supplement-specific timing. Non-linear paths acknowledged. Minimum Viable CRM prioritizes founder bandwidth. All transition rates are pre-revenue estimates. |
| Segmentation | **A-** | Dual-layer (behavioral + RFM) with at-risk sub-segments. Phase-gated by customer count. RFM thresholds calibrated for supplements. Empty until 500+ customers. |
| LTV & Cohort Analysis | **B** | Cohort framework with confidence intervals. Three methods compared. LTV by source hierarchy estimated. All actual data empty (D-grade). |
| Metrics & Dashboards | **B+** | Founder daily 5-minute check-in. Full weekly/monthly/quarterly cadence. Decision triggers with cross-TUP ownership. |
| Churn Prevention | **A-** | 4-signal churn risk formula (Phase 1 + Phase 2). At-risk sub-segments. Dunning as Priority 1. Seasonality mapped. |
| CRM Stack | **B+** | 5-phase stack gated by customer count. No premature tool spending. Shopify + Klaviyo handle 80% at launch. |

**Overall: 8.4/10**

---

## 4. Scaffolds

### Scaffold A: Lifecycle Stage Definitions

```
## [Brand] Customer Lifecycle

### Stages
| Stage | Definition | Trigger In | Trigger Out | Primary Action | KPI |
|-------|-----------|-----------|-------------|---------------|-----|
| Prospect | [Definition] | [Trigger] | [Trigger] | [Action] | [KPI] |
| Lead | [Definition] | [Trigger] | [Trigger] | [Action] | [KPI] |
| First Purchase | [Definition] | [Trigger] | [Trigger] | [Action] | [KPI] |
| Repeat | [Definition] | [Trigger] | [Trigger] | [Action] | [KPI] |
| VIP | [Definition] | [Trigger] | [Trigger] | [Action] | [KPI] |
| At Risk | [Definition] | [Trigger] | [Trigger] | [Action] | [KPI] |
| Churned | [Definition] | [Trigger] | [Trigger] | [Action] | [KPI] |

### Minimum Viable CRM (Day 1 Flows)
1. Welcome Series: [# emails], [timing], [~X hours setup]
2. Post-Purchase: [# emails], [timing], [~X hours setup]
3. Abandoned Cart: [# emails + SMS], [timing], [~X hours setup]
Total Day 1 setup: ~[X] hours

### Tier 2 Flows (Month 1-2)
4. [Flow name]: [trigger]
5. [Flow name]: [trigger]
6. [Flow name]: [trigger]

### Tier 3 Flows (Month 3+)
7. [Flow name]: [trigger]
...
```

### Scaffold B: LTV Tracking

```
## [Brand] LTV & Cohort Analysis

### Current LTV (Updated [Date])
- Simple LTV: $[X] (AOV $[X] × [X]x/year × [X] years)
- Churn-Based LTV: $[X] (ARPU $[X] × [X]% margin ÷ [X]% monthly churn)
- Cohort-Based LTV: $[X] (based on [X]-month actuals)

### LTV by Acquisition Source
| Source | Customers | CAC | M3 LTV | M12 LTV | LTV:CAC | Grade |
|--------|-----------|-----|--------|---------|---------|-------|
| [Source] | [N] | $[X] | $[X] | $[X] | [X]:1 | [A-F] |
...
| BLENDED | [N] | $[X] | $[X] | $[X] | [X]:1 | [A-F] |

### Cohort Revenue Retention
| Cohort | Customers | M0 | M1 | M2 | M3 | M6 | M12 |
|--------|-----------|-----|-----|-----|-----|-----|------|
| [Month Year] | [N] | 100% | [X]% | [X]% | [X]% | [X]% | [X]% |

### Decision Rules
- LTV:CAC <2:1 for 3 months → reduce channel spend
- LTV:CAC >5:1 → invest more in channel
- M1 retention <30% → investigate product/onboarding
- Monthly churn >7% → churn task force
```

### Scaffold C: CRM Metrics Scorecard

```
## [Brand] CRM Scorecard — Week of [Date]

### Daily Check-In
- [ ] Orders reviewed (yesterday: [X] orders, $[X] revenue)
- [ ] Email health checked (deliverability: [X]%, no flow failures)
- [ ] Support inbox clear ([X] open tickets, CSAT: [X]%)
- [ ] Subscriptions reviewed ([X] cancellations, [X] failed payments)

### Weekly Funnel Health
| Metric | This Week | Last Week | Target | Status |
|--------|-----------|-----------|--------|--------|
| Hook rate | [X]% | [X]% | >25% | [🟢/🟡/🔴] |
| Ad CTR | [X]% | [X]% | >1.5% | [🟢/🟡/🔴] |
| Email capture | [X]% | [X]% | >5% | [🟢/🟡/🔴] |
| CVR | [X]% | [X]% | >3% | [🟢/🟡/🔴] |
| Repeat rate | [X]% | [X]% | >25% | [🟢/🟡/🔴] |
| Churn rate | [X]% | [X]% | <20% | [🟢/🟡/🔴] |

### Monthly Depth Metrics
| Metric | This Month | Target | Red Flag |
|--------|-----------|--------|----------|
| Avg LTV | $[X] | >$120 | <$60 |
| LTV:CAC | [X]:1 | >3:1 | <2:1 |
| NPS | [X] | >50 | <20 |
| Sub rate | [X]% | >20% | <8% |
| List health | [X]% | >40% | <20% |
```


---

## 🔗 Dependencies & Relationships

### Feeds Into
- m17
- m20
- m21
- m25
- m27

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

- **Actual cohort retention curves for marine plasma**
  - Priority: CRITICAL
- **Real LTV by acquisition source**
  - Priority: CRITICAL
- **Supplement consumption cycle timing (30 days assumed, may be 35-45)**
  - Priority: HIGH
- **Churn rate baseline (5% target vs. reality)**
  - Priority: HIGH
- **At-risk sub-segment distribution (Product vs Budget vs Attention)**
  - Priority: HIGH
- **Lifecycle stage transition rates**
  - Priority: HIGH
- **RFM threshold accuracy for supplements**
  - Priority: MEDIUM
- **Optimal lifecycle stage count (8 operational vs simpler 6-stage)**
  - Priority: MEDIUM

---

## 🎯 Next Actions

Populate cohort data after first 100 customers; calibrate RFM thresholds after 500 customers; validate lifecycle stage transition rates from real data


---

## 🧰 OpKits

- OK-M19-001

---

---

_Report generated: 2026-02-09 17:49:43_

_Source: `data\m19`_