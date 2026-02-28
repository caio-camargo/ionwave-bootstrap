# TUP M20: Customer Support

**Status:** migrated | **Quality:** 8.6/10 | **Version:** 1.0.0
**Cluster:** BCL-4 (Retention & Lifecycle)

---

## 📋 Overview

- **Workshop Date:** 2026-02-07
- **Actor:** Claude (TWP-001)
- **Protocol Used:** TWP-001 v2.0.0
- **Change Type:** initial_workshop

### Workshop Dialogue
- **Personas Used:** Skeptical Investor, Operations Expert, Customer Anthropologist
- **Rounds:** 8
- **Saturated:** True
- **Upgrades Applied:** 6
- **Unresolved Issues:** 0

### Quality Assessment
- **Score:** 8.6/10
- **Rationale:** Strong actionability (Day-1 ready for founder). A-grade FDA/FTC compliance content. B-grade tool recommendations and benchmarks. D-grade activation targets and expected outcomes (pre-revenue estimates). Chargeback monitoring caught by dialogue. 6 upgrades applied.

---

## 📁 Content Files

- 📄 MD **data/m20/support_operations.md**
- 📄 MD **data/m20/customer_feedback_system.md**
- 📄 MD **data/m20/customer_success_playbook.md**
- 📄 MD **data/m20/dialogue_summary.md**
- 📄 MD **data/m20/opkit_customer_support.md**
- 🔧 JSON **data/m20/_meta.json**

---

## 🔧 Structured Data

_JSON files converted to human-readable format_

_No JSON files in this TUP._

---

## 📝 Narrative Content

### 📄 customer_feedback_system.md

# M20: Customer Feedback System

**TUP**: M20 — Customer Support
**Scope**: Measurement layer — NPS, CSAT, win/loss analysis
**Source Tabs**: 473 (NPS Tracking), 474 (NPS CSAT Implementation), 475 (Win/Loss Analysis)
**Version**: 1.0.0 (initial workshop)
**Last Updated**: 2026-02-07

---

## 1. Feedback System Overview

IonWave runs three feedback loops:

| Loop | What It Measures | When | Tool | Cadence |
|------|-----------------|------|------|---------|
| **NPS** | Customer loyalty / advocacy likelihood | Post-purchase Day 30 | Delighted or Retently | Every order cycle |
| **CSAT** | Support interaction satisfaction | After ticket resolution | Gorgias (built-in) | Every resolved ticket |
| **Win/Loss** | Why people bought or didn't | Post-purchase survey + cart abandonment | Fairing (post-purchase), Klaviyo (abandoned cart) | Continuous |

**Purpose**: These three loops create a closed feedback system — NPS identifies promoters and detractors, CSAT measures operational quality, and Win/Loss reveals the decision drivers behind conversion and loss.

---

## 2. NPS (Net Promoter Score)

### What NPS Measures

**The question**: "On a scale of 0-10, how likely are you to recommend IonWave to a friend?"

| Score | Category | Meaning |
|-------|----------|---------|
| 9-10 | **Promoters** | Loyal enthusiasts who will refer others |
| 7-8 | **Passives** | Satisfied but vulnerable to competitors |
| 0-6 | **Detractors** | Unhappy, may damage brand through negative WOM |

**NPS = % Promoters - % Detractors**
Range: -100 to +100

### NPS Benchmarks

| Benchmark | Score | Source |
|-----------|-------|--------|
| E-commerce average | 59 | `[Confidence: B | Source: Delighted/Sobot 2025 data]` |
| Healthcare average | 53 | `[Confidence: B | Source: industry reports]` |
| "Good" threshold | 50+ | `[Confidence: B]` |
| "World-class" | 70+ | `[Confidence: B]` |
| **IonWave Year 1 target** | 50+ | `[Confidence: D | recommendation]` |
| **IonWave Year 2 target** | 60+ | `[Confidence: D | recommendation]` |

> **⚠️ INTELLIGENCE GAP**: No published NPS benchmark exists specifically for DTC supplement brands. Wellness industry holds highest digital experience score among DTC verticals, suggesting above-average satisfaction. `[Priority: LOW | Validation: establish own baseline after first 50 NPS responses]`

### NPS Collection Setup

**Timing**: Post-purchase Day 30 (after customer has used product for ~3 weeks)
- Day 14-21 is too early for supplements — customers haven't had time to notice effects `[Confidence: C]`
- Day 30 is the sweet spot for efficacy-dependent products `[Confidence: C]`
- For subscription renewals: survey around 2nd or 3rd order (established usage pattern)

**Tool Recommendation**: **Delighted** or **Retently**

| Tool | Strengths | Shopify Integration | Price |
|------|-----------|--------------------:|-------|
| **Delighted** | Post-delivery NPS/CSAT, real-time dashboards, customizable branding | Yes (Shopify trigger) | Free tier → $224/mo+ |
| **Retently** | Shopify order-triggered surveys, in-platform analysis | Yes (native) | $25/mo+ |
| Fairing | Post-purchase attribution + NPS in checkout | Yes | $49/mo+ |

`[Confidence: B | Source: tool documentation review | Date: 2026]`

**Alternative (Budget)**: Klaviyo flow with embedded NPS question at Day 30 + Google Form for detailed follow-up. Free but less sophisticated analytics. `[Confidence: D | recommendation for pre-revenue stage]`

### NPS Follow-Up Question

**Always ask**: "What's the primary reason for your score?"

This open-ended follow-up is as valuable as the score itself. It provides:
- Specific product feedback (efficacy, taste, packaging)
- Service feedback (shipping, support experience)
- Competitive intelligence (what alternatives they've considered)
- Language for marketing copy (customer's own words)

### NPS Action Playbook

| Segment | Score | Action | Timing | Owner |
|---------|-------|--------|--------|-------|
| **Promoters** | 9-10 | Thank-you message → Referral invite → Review request → UGC ask | Within 24h | Automated (Klaviyo) |
| **Passives** | 7-8 | Ask: "What would make it a 10?" → Targeted offer/education | Within 48h | Automated + manual review |
| **Detractors** | 0-6 | Alert support team → Personal outreach → AAAA+F recovery | Within 4h | Founder/support lead |

`[Confidence: B | Source: NPS best practice synthesis | Date: 2026]`

**Detractor Recovery Targets**:
- Response within 4 hours of NPS submission `[Confidence: C]`
- 20% detractor-to-promoter conversion within 90 days `[Confidence: C]`
- Detractors are up to 50% more likely to churn within 3 months without intervention `[Confidence: C]`

### NPS Tracker Template

Track monthly:

| Period | Responses | % Promoters | % Passives | % Detractors | NPS Score | vs. Prior |
|--------|-----------|-------------|------------|-------------|-----------|-----------|
| Month 1 | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] | — |
| Month 2 | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] |
| Month 3 | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] |

**Minimum sample size**: 30+ responses before treating NPS as directionally reliable. Below 30, individual scores have high variance. `[Confidence: B | Source: survey methodology standards]`

---

## 3. CSAT (Customer Satisfaction Score)

### Two Types of CSAT

| CSAT Type | Measures | Timing | Tool |
|-----------|----------|--------|------|
| **Support CSAT** | Satisfaction with support interaction | Immediately after ticket resolution | Gorgias (built-in survey) |
| **Product CSAT** | Satisfaction with product experience | Day 7-14 after delivery | Delighted / Retently / Klaviyo |

**Keep these separate**. Support CSAT measures operational quality. Product CSAT measures product-market fit. Mixing them masks both signals.

### Support CSAT Setup

Gorgias includes a built-in satisfaction survey. After every resolved ticket:
1. Customer receives "How would you rate your support experience?" (1-5 stars or thumbs up/down)
2. Optional text field for feedback
3. Results appear in Gorgias dashboard

**Benchmarks**:
- E-commerce average CSAT: 80/100 (3.8/5) `[Confidence: B]`
- Best-in-class: 88%+ (4.4+/5) `[Confidence: B]`
- **IonWave target**: 88%+ (aspire to best-in-class from Day 1 while volume is low)

### Product CSAT Setup

Via Klaviyo flow or Delighted/Retently:
- Trigger: Day 7-14 after first delivery
- Question: "How satisfied are you with IonWave so far?" (1-5 stars)
- Follow-up: "What could we improve?"

**Why Day 7-14** (not Day 30 like NPS):
- Product CSAT captures early experience (taste, packaging, ease of use)
- NPS at Day 30 captures loyalty intent (would you recommend)
- Two different signals at two different moments

---

## 4. Win/Loss Analysis

### What Win/Loss Tracks

Win/loss analysis reveals **why people bought or didn't**. This feeds directly into:
- Marketing messaging (amplify win reasons)
- Product development (address loss reasons)
- Competitive positioning (who else they considered)
- Sales objection handling (pre-answer the loss reasons)

### Win Analysis (Why They Bought)

**Collection Method**: Post-purchase survey (Fairing or Klaviyo Day-1 flow)

#### Survey Methodology — Open-Ended First

> **⚠️ IMPORTANT**: Always ask the **open-ended question first**, THEN offer categories. Leading with categories confirms your own messaging rather than revealing real purchase drivers. Customers often rationalize post-purchase — open-ended captures the authentic reason.

**Question 1** (open-ended): "In your own words, what was the #1 reason you decided to try IonWave?"
**Question 2** (multiple choice): "Which of these best describes your main reason?" [categories below]

| Win Reason | Expected Rank | Hypothesis Link |
|------------|---------------|-----------------|
| 78 minerals vs 3 (differentiation) | #1 | — |
| Price/value perception | #2 | HYP-004 (Gross Margin) |
| Ocean-sourced / natural positioning | #3 | — |
| Recommendation / review | #4 | HYP-006 (Organic Growth) |
| Subscription convenience | #5 | HYP-002 (Subscription Conversion) |

**Minimum sample sizes**: N=50 for directional reads, N=200 for confident decision-making. Do not restructure marketing based on <50 responses. `[Confidence: B | Source: survey methodology standards]`

`[Confidence: C | Source: Danilo's framework — percentages TBD from real data | Date: 2026]`

### Win Tracker Template

| Date | Customer | Source (channel) | Primary Win Reason | Secondary Reasons | Competitor Considered | Quote |
|------|----------|-----------------|-------------------|-------------------|----------------------|-------|
| [VOID] | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] |

### Loss Analysis (Why They Didn't Buy)

**Collection Methods**:
- Cart abandonment survey (Klaviyo / Shopify flow)
- Exit-intent popup (optional)
- Post-cancellation survey (Loop Subscriptions)

| Loss Reason | Expected Rank | Decision Trigger | Action |
|-------------|---------------|-----------------|--------|
| Price too high | #1 | **>25% cite price** → trigger M10 pricing review | Test pricing / offer structure (→ M10) |
| Prefer known brand (LMNT) | #2 | **>20% cite LMNT** → create comparison page | Competitive content / comparison pages (→ M16) |
| Skeptical of claims | #3 | **>20% cite skepticism** → invest in social proof | Third-party validation / reviews / UGC |
| Didn't need / didn't want | #4 | **>15% cite no need** → review targeting | Targeting accuracy — may be reaching wrong audience |
| Found cheaper alternative | #5 | **>15% cite alternative** → competitive audit | Value messaging — emphasize 78 minerals vs. 3 |

**Decision triggers activate at N=50+ loss responses.** Below that threshold, treat as qualitative signal only.

`[Confidence: C | Source: Danilo's framework — percentages TBD from real data. Decision triggers are recommendations. | Date: 2026]`

### Loss Tracker Template

| Date | Source (channel) | Got To (stage) | Primary Objection | Secondary Objections | Went With (competitor) | Quote |
|------|-----------------|----------------|-------------------|---------------------|----------------------|-------|
| [VOID] | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] | [VOID] |

**"Got To" column** is critical — it tells you WHERE in the funnel people drop:
- Saw ad → clicked → left (awareness problem)
- Landing page → PDP → left (messaging/trust problem)
- Add to cart → checkout → abandoned (price/friction problem)
- Purchased → cancelled (product/retention problem)

### Win/Loss Summary Dashboard

Track quarterly:

| Metric | Q1 | Q2 | Q3 | Q4 |
|--------|----|----|----|----|
| Top win reason | [VOID] | [VOID] | [VOID] | [VOID] |
| Top loss reason | [VOID] | [VOID] | [VOID] | [VOID] |
| Most-mentioned competitor | [VOID] | [VOID] | [VOID] | [VOID] |
| Win:Loss ratio (surveyed) | [VOID] | [VOID] | [VOID] | [VOID] |
| New themes emerged | [VOID] | [VOID] | [VOID] | [VOID] |

### Cross-Reference: M27 (Customer Research VOC)

Win/Loss Analysis in M20 covers **structured decision tracking** (why bought/didn't buy, tracked over time). M27 (Customer Research VOC) covers **deep qualitative research** (customer interviews, review mining, segment-level insights). They're complementary:

- **M20 Win/Loss** = ongoing operational metric (every purchase, automated survey)
- **M27 VOC** = periodic deep dive (quarterly interviews, review analysis batches)

When M27 is workshopped, it should pull from M20's win/loss data as input.

---

## 5. Feedback Loop Integration

### How the Three Loops Feed Each Other

```
NPS → Detractors → Support (AAAA+F recovery)
NPS → Promoters → Referral Program (M22)
NPS → Follow-up text → Win/Loss themes
CSAT (support) → Low scores → Agent coaching + process improvement
CSAT (product) → Low scores → Product development + messaging adjustment
Win/Loss (wins) → Marketing copy fuel + positioning validation
Win/Loss (losses) → Pricing (M10) + Competitive (M26) + Content (M16) action
```

### Monthly Feedback Review (Add to MBR from M25)

At each Monthly Business Review, add a feedback section:

1. **NPS trend** — score, movement, top verbatim themes
2. **CSAT trend** — support CSAT, product CSAT, any outlier tickets
3. **Win/Loss shift** — any new win/loss reasons emerging? Competitor landscape changing?
4. **Issue type distribution** — are shipping issues decreasing? Are efficacy complaints increasing?
5. **Refund rate trend** — rate, top reason code, exchange ratio

This section feeds directly into the MBR decision framework established in M25.

---

## 6. Implementation Timeline

| Phase | When | What | Tool |
|-------|------|------|------|
| **Pre-launch** | Month -1 | Set up Gorgias (CSAT auto-survey enabled) | Gorgias |
| **Pre-launch** | Month -1 | Build NPS Klaviyo flow (Day 30 trigger) | Klaviyo |
| **Pre-launch** | Month -1 | Build post-purchase survey (Fairing or Klaviyo Day 1) | Fairing / Klaviyo |
| **Launch** | Month 0 | Start collecting support CSAT on every ticket | Gorgias |
| **Launch** | Month 0 | Start collecting post-purchase "why did you buy" | Fairing / Klaviyo |
| **Month 1** | 30 days post-launch | First NPS survey batch sends | Delighted / Klaviyo |
| **Month 2** | | First cart abandonment survey analysis | Klaviyo |
| **Month 3** | | First quarterly win/loss summary | Manual review |
| **Month 6** | | Evaluate upgrading to Delighted or Retently for NPS | Budget review |

---

## Intelligence Gaps

| Gap | Priority | Validation Path |
|-----|----------|----------------|
| DTC supplement-specific NPS benchmark | LOW | Establish own baseline after 50+ responses |
| Fairing vs Klaviyo for post-purchase surveys | MEDIUM | Test both during first 2 months, compare response rates |
| Optimal NPS survey timing for supplements | MEDIUM | A/B test Day 21 vs Day 30 vs Day 45 after 100+ data points |
| Win/loss reason percentages | HIGH | Populate from real survey data after 100 orders |
| Cart abandonment survey response rate | LOW | Measure after launch |


---

### 📄 customer_success_playbook.md

# M20: Customer Success Playbook

**TUP**: M20 — Customer Support
**Scope**: Proactive success — journey touchpoints, activation, at-risk signals, 11-star experience vision
**Source Tabs**: 468 (Customer Success Playbook), 476 (11-Star Experience)
**Version**: 1.0.0 (initial workshop)
**Last Updated**: 2026-02-07

---

## 1. Support vs. Success

| Dimension | Customer Support | Customer Success |
|-----------|-----------------|------------------|
| **Trigger** | Customer contacts us (reactive) | We contact them (proactive) |
| **Goal** | Resolve the issue | Prevent the issue |
| **Metric** | CSAT, resolution time | Activation rate, retention rate |
| **Mindset** | Cost center | Revenue driver |
| **When** | After something breaks | Before something breaks |

IonWave blends both. At pre-revenue scale, the same person (founder) handles both. The distinction matters for mindset, not org chart.

---

## 2. Customer Journey Touchpoints

### Day 0-90 Touchpoint Map

This maps the **support-relevant** touchpoints in the first 90 days. For full lifecycle email flows, see M17 (Email Marketing). For subscription retention mechanics, see M21 (Subscription & Retention).

| Day | Touchpoint | Channel | Goal | Owner |
|-----|-----------|---------|------|-------|
| **Day 0** | Order confirmation | Email (Shopify) | Set expectations, reduce buyer's remorse | Automated |
| **Day 1** | Welcome + what to expect | Email (Klaviyo) | Educate on product, set timeline for results | Automated |
| **Day 2-3** | Shipping confirmation + tracking | Email (Shopify/fulfillment) | Reduce WISMO tickets | Automated |
| **Day 5-7** | Delivery + first use prompt | Email (Klaviyo) | Encourage immediate use, dosage guidance | Automated |
| **Day 7** | Product CSAT check | Email (Klaviyo / Delighted) | Catch early issues, taste/texture feedback | Automated → manual if negative |
| **Day 14** | "How's it going?" check-in | Email (Klaviyo) | Encourage consistency, link to education content | Automated |
| **Day 21** | Review request | Email (Judge.me / Okendo) | Collect social proof from happy customers | Automated |
| **Day 28** | Subscription renewal heads-up | Email (Loop / Klaviyo) | Reduce "I didn't know" subscription complaints | Automated |
| **Day 30** | NPS survey | Email (Delighted / Klaviyo) | Measure loyalty, trigger Promoter/Detractor flows | Automated → manual for Detractors |
| **Day 45** | "Milestone" content | Email (Klaviyo) | Reinforce results narrative, testimonials | Automated |
| **Day 60** | Mid-journey check | Email (Klaviyo) or SMS | Re-engage if inactive, celebrate if active | Automated |
| **Day 90** | "You've been with us 3 months" | Email (Klaviyo) | Thank subscriber, ask for referral, offer community access | Automated |

`[Confidence: B-C | Source: Danilo's journey framework + DTC supplement lifecycle research | Date: 2026]`

### Touchpoint-to-Ticket Relationship

Each touchpoint is designed to **prevent** specific ticket types:

| Touchpoint | Prevents | Ticket Type Avoided |
|-----------|----------|-------------------|
| Order confirmation | "Did my order go through?" | Billing |
| Shipping confirmation | "Where is my order?" | Shipping/Delivery |
| First use prompt | "How do I use this?" | Product Education |
| Day 7 CSAT | Unvoiced dissatisfaction | Product Quality (silent churn) |
| Renewal heads-up | "I didn't authorize this charge" | Subscription Management |

---

## 3. What "Working" Looks Like — Setting Expectations

Marine plasma is novel enough that customers won't have a reference frame for what "working" means. Proactive education prevents premature "it's not working" tickets and churn.

### Expected Outcomes Timeline

| Timeframe | What Customers May Notice | Why |
|-----------|--------------------------|-----|
| **Week 1** | Improved hydration, possible taste adjustment period | Electrolyte balance responds quickly; ocean mineral taste is unfamiliar |
| **Week 2-3** | Sustained energy, reduced afternoon crashes | Mineral cofactors support cellular energy production |
| **Month 1-2** | Improved recovery, sleep quality, or general well-being | Deeper mineral repletion takes time — this is the "stick with it" window |
| **Month 3+** | Systemic benefits (nail/hair/skin, exercise recovery, cognitive clarity) | Long-term mineral balance — varies significantly by individual |

`[Confidence: D | Source: general mineral supplementation timelines — IonWave-specific outcomes unvalidated | Date: 2026]`

> **⚠️ IMPORTANT**: These are general mineral supplementation expectations, NOT medical claims. All customer-facing communications must include appropriate disclaimers. FTC and FDA rules apply. See adverse event protocol in `support_operations.md`.

> **⚠️ INTELLIGENCE GAP**: Expected outcomes timeline needs validation from product testing and early customer feedback. Track actual customer-reported timelines starting Month 1. `[Priority: HIGH | Validation: first 50 customer check-in responses]`

### Where This Timeline Gets Used

- **Day 1 welcome email**: "Here's what to expect in your first month"
- **Day 7 CSAT check-in**: Anchor expectations against Week 1 outcomes
- **Day 14 check-in**: "You're in Week 2-3 territory — here's what's happening"
- **Support Macro 3** (product not working): Reference this timeline in response
- **Cancellation save flow**: "Most customers notice the biggest difference in Month 2"

---

## 4. Customer Activation

### Definition: When Is a Customer "Activated"?

A customer is activated when they've completed **all 4 core criteria** (behavioral, measurable):

| # | Criterion | How to Measure | Timeline |
|---|-----------|---------------|----------|
| 1 | **Received product** | Delivery confirmed via tracking | Day 3-7 |
| 2 | **Engaged with 3+ emails** | Klaviyo opens + clicks on welcome, education, or check-in emails | Day 1-14 |
| 3 | **Reached Day 14 without a complaint ticket** | No negative-sentiment Gorgias tickets | Day 0-14 |
| 4 | **Confirmed or received 2nd order** | Subscription renewal shipped OR repeat purchase | Day 28-60 |

**Bonus signal** (not gating): Customer self-reports noticing a difference (Day 14 check-in response or NPS follow-up text). Valuable data but not measurable at scale.

`[Confidence: C | Source: Danilo's activation checklist adapted to behavioral metrics per persona dialogue | Date: 2026]`

### Why Activation Matters

- Activated customers are **3-5x more likely to retain** through the first renewal `[Confidence: B | Source: SaaS/DTC retention research]`
- The activation window for supplements is **Day 7-21** — if a customer hasn't established a daily habit by Day 21, retention probability drops sharply `[Confidence: C]`
- Activation is the single best early predictor of subscription retention, better than NPS or CSAT `[Confidence: C]`

### Activation Rate Tracking

| Metric | Target | Red Flag |
|--------|--------|----------|
| Overall activation rate (all 4 criteria) | >50% | <30% |
| Email engagement rate (3+ emails, criterion 2) | >40% | <20% |
| Complaint-free Day 14 rate (criterion 3) | >85% | <70% |
| 2nd order rate within 60 days (criterion 4) | >45% | <25% |

> **Add to Weekly Support Scorecard** (see `support_operations.md` Section 7): Activation rate should appear alongside CSAT, NPS, and refund rate as a core support metric. It is the single best early predictor of retention.

> **⚠️ INTELLIGENCE GAP**: These activation rate targets are estimates. IonWave has no baseline data yet. Track from Day 1 and calibrate after 100 customers. `[Priority: HIGH | Validation: first 100 customers]`

---

## 4. At-Risk Signals & Intervention Playbook

### Early Warning Signals

| Signal | Data Source | Risk Level | Window to Intervene |
|--------|-----------|-----------|-------------------|
| No email engagement (0 opens in 14 days) | Klaviyo | 🟡 Medium | Day 14-21 |
| Subscription paused | Loop Subscriptions | 🟠 High | Within 48h |
| Negative review posted | Judge.me / Okendo / Google | 🔴 Critical | Within 4h |
| No reorder after 45 days (one-time buyer) | Shopify | 🟡 Medium | Day 45-60 |
| NPS Detractor score (0-6) | Delighted / NPS tool | 🔴 Critical | Within 4h |
| Support ticket unresolved >48h | Gorgias | 🟠 High | Immediately |
| Failed payment (dunning) | Loop Subscriptions | 🟠 High | Within 24h (automated) |
| Multiple contacts on same issue | Gorgias | 🟠 High | Tier 3 escalation |

### Intervention Playbook

| Signal | Intervention | Channel | Owner |
|--------|-------------|---------|-------|
| **No email engagement** | SMS nudge: "Hey [Name], just checking in — how's your IonWave experience?" | SMS | Automated (Klaviyo) |
| **Subscription paused** | Personal email from founder: "I noticed you paused — can I help with anything?" Include option to swap frequency/product | Email (manual) | Founder |
| **Negative review** | "Make it right" outreach: personal apology + resolution offer (refund + free product) + ask to update review after resolution | Email/DM (manual) | Founder |
| **No reorder (Day 45)** | Win-back offer: 20% off next order + education content on benefits of continued use | Email (Klaviyo) | Automated |
| **NPS Detractor** | Immediate Tier 3 escalation → AAAA+F recovery (see support_operations.md) | Phone/email (manual) | Founder |
| **Unresolved ticket >48h** | Internal alert + priority reassignment | Gorgias/Slack | Support lead |
| **Failed payment** | Dunning sequence: 3 retry attempts over 7 days + "update your card" email | Automated (Loop) | Automated → manual after 3 failures |
| **Multiple contacts** | Escalate to Tier 3 + proactive outreach with comprehensive resolution | Email/phone | Founder |

`[Confidence: B-C | Source: Danilo's intervention playbook + M21 retention playbook + DTC best practices | Date: 2026]`

### Cross-Reference: M21 Retention Playbook

M21 contains the comprehensive retention playbook (15 tactics in 3 tiers). The interventions above are the **support-triggered** subset. For full retention infrastructure including:
- Pre-cancellation save flow → see `data/m21/retention_playbook.md`
- Win-back offer ladder → see `data/m21/win_back_offer_ladder.md`
- Churn prediction signals → see `data/m21/churn_prediction.json`
- Subscription psychology → see `data/m21/subscription_psychology.md`

M20's intervention playbook is the **first responder** layer. M21 is the **strategic retention** layer. They connect at the handoff point: when a support intervention doesn't resolve the at-risk signal, it feeds into M21's deeper retention machinery.

---

## 5. The 11-Star Experience Framework

### Airbnb's Framework Applied to IonWave

The 11-Star framework starts with your current experience (5-star) and asks "what would make this even better?" all the way to absurd (11-star). Then work backwards to find the sweet spot between aspirational and feasible.

### The Spectrum

#### ⭐⭐⭐⭐⭐ 5-Star (Baseline — What We Deliver at Launch)

- Product arrives in 3-5 days
- Clean, functional packaging
- Product works as described
- Basic email support (<4 hour response)
- Standard subscription option

#### ⭐⭐⭐⭐⭐⭐ 6-Star (Better Than Expected)

- Arrives in 2 days with proactive tracking updates
- Beautiful unboxing experience
- Personalized note in first order
- Quick-start guide included in package
- Easy subscription management (pause/skip/swap)

#### ⭐⭐⭐⭐⭐⭐⭐ 7-Star (Memorable)

- Free sample of new flavor/variant with order
- Hand-written thank you card (founder)
- Access to private community (Skool/Circle)
- Live chat support with real humans
- Referral rewards program ($10 give / $10 get)

#### ⭐⭐⭐⭐⭐⭐⭐⭐ 8-Star (Remarkable)

- Mineral education course included (email series)
- Video from founder explaining their specific order
- Quarterly surprise gift for long-term subscribers
- Direct text line to support (SMS)
- Annual subscriber appreciation event (virtual)

#### ⭐⭐⭐⭐⭐⭐⭐⭐⭐ 9-Star (Life-Changing)

- Free mineral blood/hair test with subscription
- Personalized mineral blend based on test results
- 1:1 consultation with nutritionist
- Dedicated health concierge
- Personal results tracking dashboard

#### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 10-Star (Unbelievable)

- Install a mineral water system in your home
- Monthly check-in call with personal health coach
- Trip to see the ocean source in Portugal
- Lifetime supply for your family
- Custom product line with your name on it

#### ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ 11-Star (Absurd / Impossible)

- Private island retreat focused on mineral wellness
- Celebrity personally delivers your order
- We cure all your health problems forever
- Your own ocean to harvest minerals from
- Time travel back to drink primordial ocean water

### The Sweet Spot: Feasible in Next 6 Months

From the 6-9 star ideas, what can IonWave actually implement?

| Initiative | Star Level | Feasibility | Cost | Impact | Priority |
|-----------|-----------|-------------|------|--------|----------|
| ☐ Personalized note in first order | 6★ | Easy — print template, hand-write name | ~$0.50/order | Medium (memorable first impression) | P1 |
| ☐ Quick-start guide in package | 6★ | Easy — design once, print in bulk | ~$0.30/order | High (reduces education tickets) | P1 |
| ☐ Access to private community | 7★ | Medium — set up Skool or email community first | $0-99/month | Medium (loyalty + retention) | P2 |
| ☐ Referral rewards program | 7★ | Medium — implement via Smile.io or manual | $0-49/month + reward cost | High (organic growth) | P1 (see M22) |
| ☐ Quarterly surprise for long-term subscribers | 8★ | Medium — plan quarterly, budget per subscriber | $3-5/subscriber/quarter | High (retention + delight) | P2 |
| ☐ Results tracking via simple survey | 9★ lite | Easy — Typeform or Klaviyo flow | Free-$25/month | Medium (engagement + data) | P2 |
| ☐ Mineral education email course | 8★ | Easy — write 5-7 email sequence in Klaviyo | Time only | High (engagement + trust) | P1 |

`[Confidence: C-D | Source: Danilo's sweet spot framework + cost estimates | Date: 2026]`

### How 11-Star Connects to Daily Operations

The 11-Star framework is a **thinking tool**, not an operations checklist. Use it:
- **Quarterly**: In QBR (M25), review the sweet spot list. What have we implemented? What's next?
- **Monthly**: In MBR, check if any 6-7 star initiatives are slipping below 5-star baseline
- **When stuck**: If retention is flat, look at the 7-9 star column for ideas to test

---

## 6. Support-Driven Product Intelligence

### Turning Tickets Into Product Insights

Support tickets are the richest source of unfiltered customer feedback. Systematically mine them:

| Ticket Pattern | Insight Category | Feeds Into |
|---------------|-----------------|-----------|
| Recurring taste complaints | Product development | M10 (Pricing/Offer) — flavor options |
| "Didn't know it was a subscription" | UX/checkout design | M14 (Testing) — subscription clarity test |
| "How much should I take?" | Packaging/labeling | Product packaging redesign |
| "Can I give this to my kids?" | Market expansion signal | M27 (Customer Research) — family segment |
| "I mixed it with [X] and loved it" | Content/recipe ideas | M16 (Content) — usage content |
| "Compared to LMNT, this is..." | Competitive intelligence | M26 (Competitive Intel) — positioning data |

### Monthly Support Intelligence Report

Add to the MBR feedback section (see `customer_feedback_system.md`):

1. **Top 3 new themes** from support tickets this month
2. **Issue type shift** — what's growing vs. declining?
3. **Product feedback gems** — direct customer quotes worth sharing
4. **Competitive mentions** — who are customers comparing us to?
5. **Feature requests** — what do customers wish we had?

---

## 7. Founder Mode: Support at Scale of 1

### Month 1-6 Reality

At IonWave's stage, the "support team" is the founder (Danilo/operator). This is optimal for learning but unsustainable past ~100 orders/month.

### Founder Support Playbook

| Month | Orders | Tickets (est.) | Setup |
|-------|--------|----------------|-------|
| 0-1 | 0-50 | 0-40 | Founder handles all. Gorgias on phone. 30 min/day. |
| 1-3 | 50-200 | 35-140 | Founder handles all. Macros save 50% time. 1 hr/day. |
| 3-6 | 200-500 | 120-300 | Hire part-time VA for Tier 1. Founder handles Tier 2-3. VA: 2-3 hrs/day. |
| 6-12 | 500-2,000 | 300-1,200 | Full Tier 1 VA. Consider Gorgias Pro. Founder: Tier 3 only. |

### When to Hire First Support VA

**Trigger**: When support takes >2 hours/day consistently for 2+ weeks AND founder is pulled from growth work.

**Profile**:
- E-commerce support experience (Gorgias/Zendesk preferred)
- Supplement/health product familiarity (bonus)
- US timezone (for <1 hour response target)
- Start part-time (10-15 hrs/week), expand as needed

**Cost estimate**: $15-20/hr US-based VA, $8-12/hr international VA `[Confidence: C | Source: DTC VA market rates | Date: 2026]`

### What the Founder Should NEVER Delegate (Until VP of CX)

- Tier 4 escalations (adverse events, legal threats)
- NPS Detractor recovery outreach
- Monthly support intelligence review
- Policy exceptions >$50
- Negative review responses

---

## Intelligence Gaps

| Gap | Priority | Validation Path |
|-----|----------|----------------|
| Activation rate baseline (all 5 criteria) | HIGH | Track from first 100 customers |
| Actual at-risk signal accuracy | MEDIUM | Validate signals against actual churn data after 6 months |
| 11-Star sweet spot ROI | LOW | Track implementation cost vs. retention impact per initiative |
| Founder support time per day at each scale | LOW | Log actual time starting Month 1 |
| VA hiring trigger point (exact order volume) | MEDIUM | Monitor founder time allocation weekly |
| Sachet-specific packaging insert cost | LOW | Get print quote pre-launch |


---

### 📄 dialogue_summary.md

# M20: Customer Support — Persona Dialogue Summary

**TUP**: M20 — Customer Support
**TUP Version Tested**: 1.0.0
**Date**: 2026-02-07
**Protocol**: TWP-001 v2.0.0

---

## Personas

| Persona | Role | Lens |
|---------|------|------|
| **Skeptical Investor** | Financial grounding | "Does this reduce churn? Show me the ROI." |
| **Operations Expert** | Scalability + failure modes | "What breaks at scale? Where are the SPOFs?" |
| **Customer Anthropologist** | Customer reality | "What are actual customers experiencing? Are we hearing them?" |

---

## Dialogue Log

### ROUND 1
- **CHALLENGE**: Marine plasma "working" is undefined — support macros ask about results but customers have no reference frame for what results look like.
- **RESPONSE**: Ops Expert confirms adverse event protocol requires structured communication but onboarding fails to set expectations first.
- **SYNTHESIS**: Need a "What Working Looks Like" section with expected outcomes timeline, fed into macros and check-in emails.
- **OUTCOME**: UPGRADED
- **ACTION**: U1 — Added Section 3 "What Working Looks Like" to customer_success_playbook.md with Week 1/2-3/Month 1-2/3+ timeline. Connected to macros and touchpoint emails.

### ROUND 2
- **CHALLENGE**: 4-tier escalation system designed for a team that doesn't exist — founder IS all tiers for Month 0-6.
- **RESPONSE**: Tier structure is premature operationally but valuable as a hiring spec and training document.
- **SYNTHESIS**: Phase-gate the escalation system: Founder Mode (all tiers = founder) vs Team Mode (table activates at hire).
- **OUTCOME**: UPGRADED
- **ACTION**: U2 — Added Founder Mode vs Team Mode phase-gating with transition checklist to support_operations.md.

### ROUND 3
- **CHALLENGE**: Win/loss survey uses pre-set categories (confirms marketing messaging, not real purchase drivers). Loss analysis captures data but has no decision triggers.
- **RESPONSE**: Open-ended questions first, then categories. Need minimum sample sizes and thresholds for action.
- **SYNTHESIS**: Survey methodology fix + decision triggers + N thresholds added.
- **OUTCOME**: UPGRADED
- **ACTION**: U3 — Added open-ended-first methodology, decision triggers (>25% price → M10 review, etc.), N=50 directional/N=200 confident thresholds.

### ROUND 4
- **CHALLENGE**: Chargeback risk missing — supplements are high-risk category, Stripe 0.75% threshold can shut down payments. Refund rate ≠ chargeback rate.
- **RESPONSE**: Proactive refunds prevent chargebacks. Clear billing descriptors prevent "unrecognized charge" disputes.
- **SYNTHESIS**: Chargeback monitoring section needed with distinct tracking and prevention protocol.
- **OUTCOME**: UPGRADED
- **ACTION**: U4 — Added Section 7 "Chargeback Monitoring & Prevention" with Stripe thresholds, proactive refund strategy, billing descriptor guidance.

### ROUND 5
- **CHALLENGE**: Review management platforms missing. 11-Star framework not measurable. Sweet spot initiatives have no ROI case.
- **RESPONSE**: Review management belongs in M16/M29 (cross-ref). NPS/CSAT IS the measurement layer. ROI requires real data.
- **SYNTHESIS**: Cross-references sufficient. ROI calculation deferred to Track B (post-6-month data).
- **OUTCOME**: RESOLVED

### ROUND 6
- **CHALLENGE**: Activation criterion #5 (self-reports noticing something) is unmeasurable at scale. Activation should be entirely behavioral.
- **RESPONSE**: Replace self-report with behavioral proxy: "confirmed 2nd order within 60 days." Add activation rate to scorecard.
- **SYNTHESIS**: 5 criteria → 4 behavioral criteria. Self-report becomes bonus signal. Activation rate added to weekly scorecard.
- **OUTCOME**: UPGRADED
- **ACTION**: U5 — Revised activation to 4 behavioral criteria, added activation rate to support scorecard, added note that activation is #1 retention predictor.

### ROUND 7
- **CHALLENGE**: Support tool stack costs ~$1,300/month with VA — too much for pre-revenue bootstrapped founder.
- **RESPONSE**: Minimum viable stack: Gorgias Basic + Klaviyo flows + free tools = $60/month. Layer tools as revenue grows.
- **SYNTHESIS**: Phase-gated tool spending with revenue-based thresholds.
- **OUTCOME**: UPGRADED
- **ACTION**: U6 — Added "Minimum Viable Support Stack" section with Month 0-3/3-6/6-12/12+ phases and 10x revenue rule.

### ROUND 8
- **CHALLENGE**: Macro taste advice may have ingredient interaction risks. Promoter NPS timing.
- **RESPONSE**: Ingredient interactions flagged as intelligence gap. Promoter timing already addressed ("within 24h").
- **SYNTHESIS**: Refinement-level feedback, not structural gaps. All personas satisfied.
- **OUTCOME**: RESOLVED

---

## Saturation Log

| Check | Result |
|-------|--------|
| 3 consecutive RESOLVED? | No (but Round 5+8 = 2 RESOLVED with only minor UPGRADED between) |
| Last UNRESOLVED gaps are restatements? | N/A — 0 UNRESOLVED |
| All 3 personas agree content is coherent? | Yes (Round 8 explicit consensus) |
| Hard stop (8 rounds)? | Yes — hard stop reached |

**Saturation: REACHED at Round 8 (hard stop, all personas satisfied)**

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total rounds | 8 |
| UPGRADED | 6 |
| RESOLVED | 2 |
| UNRESOLVED | 0 |
| Upgrades applied | 6/6 (all applied to content) |

---

## Upgrades Applied

| ID | Description | File Modified |
|----|-------------|---------------|
| U1 | "What Working Looks Like" section — expected outcomes timeline for marine plasma | customer_success_playbook.md |
| U2 | Founder Mode vs Team Mode phase-gating for escalation framework | support_operations.md |
| U3 | Open-ended-first survey methodology + decision triggers + N thresholds | customer_feedback_system.md |
| U4 | Chargeback monitoring section — Stripe threshold, prevention, tracker | support_operations.md |
| U5 | Behavioral activation criteria (4 criteria) + activation rate on scorecard | customer_success_playbook.md + support_operations.md |
| U6 | Minimum Viable Support Stack — phase-gated tool spending ($60/month start) | support_operations.md |

---

## What Would Have Been Missed Without Dialogue

1. **Chargeback risk** (U4): The entire chargeback monitoring section — Stripe's 0.75% threshold could shut down payment processing. This is an existential risk that was completely absent from the original content.
2. **Premature tool spending** (U6): $1,300+/month in support tools before revenue. The minimum viable stack cuts this to $60/month.
3. **Unmeasurable activation** (U5): Self-reported "noticing something" as a gating activation criterion would have made the metric unreliable at any scale.
4. **Misleading win/loss data** (U3): Category-first surveys would have confirmed marketing messaging rather than revealing real purchase drivers.
5. **Founder/team confusion** (U2): Tier system designed for a team that won't exist for 6+ months would have been ignored, defeating its purpose as a training document.


---

### 📄 opkit_customer_support.md

# OpKit: Customer Support Operations (OK-M20-001)

**Type**: Production OpKit
**Domain**: Customer Support Operations
**Applicable To**: Any DTC brand (supplement-specific sections flagged)
**Source TUP**: M20 — Customer Support
**Version**: 1.0.0
**Date Created**: 2026-02-07

---

## 1. Instruction Doc — How to Build a DTC Support Operation

### Step-by-Step (8 Steps)

**Step 1: Choose Your Helpdesk**
- For Shopify brands: Gorgias (best native integration)
- For non-Shopify: Zendesk or Freshdesk
- Start with the cheapest plan that includes ticket tracking, customer order visibility, and CSAT surveys
- Do NOT start with free email — you need ticket tracking for patterns and compliance

**Step 2: Design Your Escalation Framework**
- Define 3-4 tiers with response time targets per tier
- Map which issue types go to which tier
- Set agent authority levels (what each tier can offer without approval)
- If solo founder: document the tier system anyway — it's your future hiring spec

**Step 3: Write Your Support Macros**
- Create templates for your top 5-6 ticket types
- Each macro should: acknowledge the issue, show empathy, take action, set next-step expectation
- Include one macro for health/safety escalation (if applicable to your product category)
- Review and update macros monthly based on actual ticket patterns

**Step 4: Design Your Refund & Return Policy**
- Choose your guarantee window (30/60/90 days)
- Decide "keep the product" vs. return for each scenario
- Document refund reason categories (6-8 standard categories)
- Set refund rate health benchmarks and monitoring cadence
- For consumables: "keep the product" is almost always more economical than return shipping

**Step 5: Set Up Feedback Loops**
- NPS: post-purchase Day 14-30 (adjust for your product's value-delivery timeline)
- CSAT: after every support ticket resolution (built into most helpdesks)
- Win/Loss: post-purchase attribution survey + cart abandonment survey
- Design action playbooks for each: Promoter → referral, Detractor → recovery, Loss reasons → specific fixes

**Step 6: Build Your At-Risk Signal System**
- Identify 5-8 behavioral signals that predict churn (no email opens, subscription paused, negative review, etc.)
- Map each signal to a specific intervention (SMS, personal email, founder outreach, win-back offer)
- Cross-reference with your retention playbook if you have one

**Step 7: Define Customer Activation**
- Choose 3-5 behavioral criteria that define "activated" (NOT self-reported satisfaction)
- Track activation rate alongside NPS/CSAT
- Set target activation rates and red flags
- Activation is typically the #1 predictor of retention

**Step 8: Build Your Scorecard**
- Weekly: response times, CSAT, activation rate, refund rate, ticket volume
- Monthly: NPS trend, win/loss analysis, chargeback rate, issue type distribution
- Quarterly: support cost as % of revenue, team scaling needs, tool stack review

### For Supplement/Health Brands — Additional Requirements
- Build an adverse event reporting protocol that complies with FDA requirements (15-day SAE reporting, 6-year record retention)
- Include health/safety escalation triggers in your tier system
- Monitor chargeback rate carefully — supplements are high-risk category for payment processors
- Product labels must include domestic contact info for adverse event reporting

---

## 2. Grading Rubric

| Dimension | A (Excellent) | B (Good) | C (Adequate) | D (Weak) | F (Failing) |
|-----------|--------------|----------|--------------|----------|-------------|
| **Escalation Design** | 3-4 tiers with response times, agent authority, triggers, phase-gating | 3+ tiers with response times | Tiers defined but no response times | Ad-hoc escalation | No escalation system |
| **Macro Library** | 6+ macros covering top ticket types, updated monthly | 4-5 macros for common issues | 2-3 basic macros | 1 generic template | No macros |
| **Refund Policy** | Documented policy, reason tracking, health benchmarks, chargeback monitoring | Policy documented with basic tracking | Policy exists but inconsistently applied | Verbal policy only | No policy |
| **Feedback System** | NPS + CSAT + Win/Loss all active with action playbooks | 2 of 3 active | 1 feedback mechanism | Occasional surveys | No feedback collection |
| **Activation Tracking** | Behavioral criteria defined, tracked weekly, linked to retention | Criteria defined, tracked monthly | Criteria defined but not tracked | Vague definition | No activation concept |
| **Compliance** | Full adverse event protocol, chargeback monitoring, billing descriptors | Most compliance items covered | Some compliance awareness | Reactive compliance only | No compliance system |

---

## 3. Graded Example — IonWave (Trade #84)

| Dimension | Grade | Rationale |
|-----------|-------|-----------|
| Escalation Design | **B+** | 4 tiers with response times, agent authority, and phase-gating (Founder Mode / Team Mode). Not yet tested in production. |
| Macro Library | **B** | 6 macros covering top ticket types including adverse reaction escalation. Taste advice needs product-specific ingredient safety review. |
| Refund Policy | **A-** | Documented policy with reason codes, health benchmarks, chargeback monitoring section. "Keep the product" first-order guarantee is industry-appropriate. |
| Feedback System | **B** | NPS, CSAT, and Win/Loss all designed with action playbooks. Minimum viable stack phase-gates tool spending. Survey methodology upgraded (open-ended first). |
| Activation Tracking | **B** | 4 behavioral criteria defined with targets. Activation rate on weekly scorecard. Expected outcomes timeline supports activation. All targets are pre-revenue estimates. |
| Compliance | **A-** | FDA adverse event protocol with 15-day reporting, 6-year retention, MedWatch form. Chargeback monitoring with Stripe thresholds. Legal review flagged as CRITICAL pre-launch gap. |

**Overall: 8.6/10**

---

## 4. Scaffolds

### Scaffold A: Support Operations Setup

```
## [Brand] Support Operations

### Tool Stack
- Helpdesk: [Platform] ([Plan], $[X]/month)
- Subscription: [Platform] (for sidebar integration)
- Email: [Platform] (for customer data in tickets)

### Escalation Tiers
| Tier | Name | Response Time | Handler | Scope |
|------|------|--------------|---------|-------|
| 1 | Standard | [X hours] | [Who] | [What] |
| 2 | Issue | [X hours] | [Who] | [What] |
| 3 | Escalated | [X hours] | [Who] | [What] |
| 4 | Crisis | [X minutes] | [Who] | [What] |

### Agent Authority
| Action | Tier 1 | Tier 2 | Tier 3+ |
|--------|--------|--------|---------|
| Store credit | Up to $[X] | Up to $[X] | Unlimited |
| Refund | [Scope] | Up to $[X] | Unlimited |
| Replacement | [Y/N] | [Y/N] | [Y/N] |

### Refund Policy
| Scenario | Action | Keep Product? |
|----------|--------|---------------|
| First order, [X] days | [Action] | [Y/N] |
| Repeat order | [Action] | [Y/N] |
| International | [Action] | [Y/N] |

### Refund Reason Codes
| Code | Category | Description |
|------|----------|-------------|
| RF-001 | [Category] | [Description] |
| RF-002 | [Category] | [Description] |
...

### Weekly Scorecard
| Metric | Target | Red Flag |
|--------|--------|----------|
| First response time | [Target] | [Red flag] |
| CSAT | [Target] | [Red flag] |
| Refund rate | [Target] | [Red flag] |
| Chargeback rate | [Target] | [Red flag] |
| Activation rate | [Target] | [Red flag] |
```

### Scaffold B: Customer Feedback System

```
## [Brand] Feedback System

### NPS
- Tool: [Tool]
- Timing: Day [X] post-delivery
- Question: "How likely are you to recommend [Brand] to a friend?" (0-10)
- Follow-up: "What's the primary reason for your score?"

### NPS Action Playbook
| Segment | Score | Action | Timing |
|---------|-------|--------|--------|
| Promoters | 9-10 | [Actions] | Within [X]h |
| Passives | 7-8 | [Actions] | Within [X]h |
| Detractors | 0-6 | [Actions] | Within [X]h |

### Win/Loss Tracking
- Win survey question (open-ended): "[Question]"
- Win survey question (categories): [List categories]
- Loss collection method: [Method]
- Decision triggers:
  - If >[X]% cite [reason] → [Action]
  - Minimum N for decisions: [N]

### Monthly Feedback Review
1. NPS trend + top verbatim themes
2. CSAT trend + outlier tickets
3. Win/Loss shift + new reasons
4. Issue type distribution
5. Refund rate + reason codes
```

### Scaffold C: Customer Success Playbook

```
## [Brand] Customer Success Playbook

### Customer Journey (Day 0-90)
| Day | Touchpoint | Channel | Goal |
|-----|-----------|---------|------|
| 0 | [Touchpoint] | [Channel] | [Goal] |
| 1 | [Touchpoint] | [Channel] | [Goal] |
...

### What "[Product] Working" Looks Like
| Timeframe | Expected Outcome |
|-----------|-----------------|
| Week 1 | [Outcome] |
| Week 2-3 | [Outcome] |
| Month 1-2 | [Outcome] |
| Month 3+ | [Outcome] |

### Activation Criteria (Behavioral)
| # | Criterion | How to Measure | Target Rate |
|---|-----------|---------------|-------------|
| 1 | [Criterion] | [Measurement] | [Target] |
| 2 | [Criterion] | [Measurement] | [Target] |
...

### At-Risk Signals
| Signal | Risk Level | Intervention |
|--------|-----------|-------------|
| [Signal] | [Level] | [Action] |
...
```


---

### 📄 support_operations.md

# M20: Support Operations

**TUP**: M20 — Customer Support
**Scope**: Reactive support operations — escalation, issue tracking, refund/return policy
**Source Tabs**: 469 (Complaint Escalation), 470 (Customer Issue Log), 471 (Refund Return Tracker), 472 (Returns & Exchanges)
**Version**: 1.0.0 (initial workshop)
**Last Updated**: 2026-02-07

---

## 1. Support Philosophy

**Vision**: Every complaint is a signal and every resolution increases LTV.

IonWave runs a **support-as-retention** model, not a cost center. At pre-revenue scale, the founder handles Tier 2-3 personally. This is a feature, not a bug — it builds product intuition and customer empathy that can't be delegated.

**The service recovery paradox**: Customers who experience a well-managed complaint resolution often become more loyal than those who never had a problem. `[Confidence: B | Source: Zendesk research, HBR | Date: 2026]`

---

## 2. Tool Stack

### Recommended Stack

| Tool | Role | Plan | Cost | Phase |
|------|------|------|------|-------|
| **Gorgias** | Helpdesk | Basic | $60/month (300 tickets) | Day 0 |
| **Loop Subscriptions** | Subscription management in sidebar | Pro (for Gorgias integration) | Per Loop plan | Day 0 |
| **Klaviyo** | Customer data in sidebar + NPS flows | Standard | Per Klaviyo plan | Day 0 |
| **Shopify** | Order management in ticket view | Standard | Per Shopify plan | Day 0 |

`[Confidence: A | Source: Gorgias, Loop Subscriptions, Klaviyo official documentation | Date: 2026]`

### Why Gorgias Over Alternatives

| Factor | Gorgias | Zendesk | Freshdesk | Richpanel |
|--------|---------|---------|-----------|-----------|
| Shopify integration depth | ★★★★★ (native) | ★★★ (bolt-on) | ★★★ (solid) | ★★★★ (good) |
| Pricing model | Per-ticket | Per-agent | Per-agent | Per-user |
| E-commerce AI tuning | Yes | Generic | Generic | Self-service focus |
| Starting cost | $60/mo | $19/agent/mo | $15/agent/mo | $85/user/mo |
| Unlimited seats | Yes (Basic+) | No | No | No |

50% of the top 1,500 Shopify stores use Gorgias. `[Confidence: C | Source: Gorgias marketing claim | Date: 2026]`

### Gorgias Upgrade Path

| Plan | Tickets/mo | Cost/mo | When to Upgrade |
|------|-----------|---------|-----------------|
| Starter | 50 | $10 | Testing only (limited to 3 seats) |
| **Basic** | 300 | $60 | **Launch tier** — IonWave starts here |
| Pro | 2,000 | $360 | >400 tickets/month consistently, need AI + advanced reporting |
| Advanced | 5,000 | $900 | Scaling brand, complex workflows |

Overages: $0.36-$0.40 per ticket beyond plan limit. AI Agent add-on: $1 per AI-resolved ticket. `[Confidence: B | Source: Gorgias pricing page | Date: 2026]`

### Integration Verification Status

| Integration | Status | Notes |
|-------------|--------|-------|
| Gorgias + Shopify | ✅ Verified (A-grade) | Order history, shipping status, refund/return actions in ticket view |
| Gorgias + Klaviyo | ✅ Verified (A-grade) | Campaign/list membership visible, SMS routes to agents |
| Gorgias + Loop | ✅ Verified (A-grade) | Requires Loop Pro plan. Subscription data in Gorgias sidebar. |

> **⚠️ INTELLIGENCE GAP**: Gorgias AI Agent ($1/resolved ticket) — no first-hand testing data. Need to evaluate accuracy on supplement-specific queries before enabling. `[Priority: MEDIUM | Validation: test with 50 sample tickets post-launch]`

### Minimum Viable Support Stack (Month 0-3)

For a bootstrapped founder, don't over-invest in tools before revenue justifies it. Phase-gate spending:

| Phase | Tools | Monthly Cost | When to Activate |
|-------|-------|-------------|-----------------|
| **Month 0-3** | Gorgias Basic + Klaviyo flows (NPS via embedded form) + Google Form (win/loss) | **~$60/month** | Launch |
| **Month 3-6** | + Fairing (post-purchase attribution) | **~$109/month** | When you need attribution data for ad spend decisions |
| **Month 6-12** | + Delighted or Retently (NPS-specific) | **~$134-284/month** | When NPS volume justifies dedicated tool (50+ responses/month) |
| **Month 12+** | + Gorgias Pro (AI + advanced reporting) | **~$360+/month** | When ticket volume >400/month consistently |

**Rule**: No tool gets added until revenue from the previous month covers the tool cost 10x. A $49/month tool needs $490/month in revenue to justify. `[Confidence: D | Source: recommendation based on bootstrapped DTC economics]`

---

## 3. Escalation Framework

### 4-Tier Escalation System

> **⚠️ PHASE-GATING**: This tier system has two modes. Read the correct one for your current stage.

#### Founder Mode (Month 0-6, <500 orders/month)

In Founder Mode, **all tiers are you**. The founder handles Tier 1-4 personally. This is optimal for learning but the tier structure still matters — it determines your **response time and resolution authority** per issue type.

| Tier | Name | Response Time | Handler (Founder Mode) | Scope |
|------|------|--------------|----------------------|-------|
| **Tier 1** | Standard | <4 hours (email), <2 min (chat) | Founder (use macros) | Order status, shipping, basic FAQ, subscription skip/pause |
| **Tier 2** | Issue | <2 hours | Founder (manual) | Product complaints, billing disputes, policy exceptions, ingredient questions |
| **Tier 3** | Angry | <1 hour | Founder (personal touch) | Repeated contacts, social media threats, negative reviews, complex complaints |
| **Tier 4** | Crisis | <30 minutes | Founder + Legal (if needed) | Health issues, lawyer mentions, safety concerns, FDA-reportable events |

**Founder Mode daily time budget**: 30-60 min/day at <100 orders/month, 1-2 hrs/day at 100-500 orders/month.

#### Team Mode (Month 6+, >500 orders/month)

When support takes >2 hours/day for 2+ consecutive weeks, transition to Team Mode. The tier table becomes the **VA training document**.

| Tier | Name | Response Time | Handler (Team Mode) | Scope |
|------|------|--------------|-------------------|-------|
| **Tier 1** | Standard | <4 hours (email), <2 min (chat) | Support VA / Gorgias AI | Order status, shipping, basic FAQ, subscription skip/pause |
| **Tier 2** | Issue | <2 hours | Trained support agent | Product complaints, billing disputes, policy exceptions, ingredient questions |
| **Tier 3** | Angry | <1 hour | Founder/Operator | Repeated contacts, social media threats, negative reviews, complex complaints |
| **Tier 4** | Crisis | <30 minutes | Founder + Legal (if needed) | Health issues, lawyer mentions, safety concerns, FDA-reportable events |

#### Transition Checklist (Founder Mode → Team Mode)

- [ ] Support consistently takes >2 hrs/day for 2+ weeks
- [ ] Founder is being pulled from growth work
- [ ] At least 100 historical tickets exist (for VA training examples)
- [ ] Macro library covers 80%+ of Tier 1 scenarios
- [ ] VA hired and trained on escalation triggers
- [ ] Gorgias rules configured for auto-assignment

`[Confidence: B | Source: DTC industry standard adapted from Danilo's 4-tier model + research benchmarks | Date: 2026]`

### Response Time Benchmarks

| Channel | IonWave Target | Industry Average | Best-in-Class |
|---------|---------------|------------------|---------------|
| Email first response | <1 hour | 4-6 hours | 30-60 minutes |
| Live chat | <30 seconds | <2 minutes | <30 seconds |
| Social media | <30 minutes | 1-2 hours | <30 minutes |

64% of shoppers expect a response within one hour. `[Confidence: B | Source: multiple industry reports | Date: 2026]`

### Escalation Triggers (Automatic Tier Upgrade)

Any of these immediately escalate to Tier 3 or 4:

| Trigger | Escalate To | Rationale |
|---------|-------------|-----------|
| Customer mentions lawyer/legal action | Tier 4 | Legal exposure |
| Customer reports health issue or adverse reaction | Tier 4 | FDA reporting requirement |
| Customer threatens social media post or review | Tier 3 | Brand reputation |
| Profanity or abusive language | Tier 3 | Agent safety + complex resolution |
| 3+ contacts on same issue | Tier 3 | Systemic failure signal |
| Product safety concern (contamination, foreign object) | Tier 4 | Regulatory + liability |
| Chargeback dispute filed | Tier 3 | Revenue + payment processor relationship |

### Tier 3-4 Response Playbook: AAAA+F

For escalated complaints, use the **AAAA+F framework**:

1. **Acknowledge** — "I hear you, and I understand this is frustrating."
2. **Apologize** — "I'm sorry this happened. This isn't the experience we want for you."
3. **Act** — Take concrete action immediately (refund, replacement, credit). Don't ask the customer to do more work.
4. **Add** — Add unexpected value beyond the fix (extra product, extended subscription, personal note from founder).
5. **Follow Up** — Check back in 48-72 hours. "I wanted to make sure everything is resolved."

**Agent Authority Table** (what agents can do without escalation):

| Action | Tier 1 | Tier 2 | Tier 3+ |
|--------|--------|--------|---------|
| Issue store credit | Up to $10 | Up to $25 | Unlimited |
| Process refund | First-order guarantee only | Up to $50 | Unlimited |
| Send free replacement | No | Yes (1 unit) | Yes (any amount) |
| Extend subscription trial | No | +7 days | +30 days |
| Offer discount on next order | 10% | 15-20% | Custom |

`[Confidence: C | Source: Danilo's AAAA+F framework + industry best practice synthesis | Date: 2026]`

---

## 4. Adverse Event Reporting Protocol

### ⚠️ REGULATORY REQUIREMENT — NOT OPTIONAL

FDA requires supplement brand owners to report Serious Adverse Events (SAEs) within **15 business days**. Failure to comply = product is legally "misbranded." `[Confidence: A | Source: Dietary Supplement and Nonprescription Drug Consumer Protection Act, FDA.gov | Date: 2026]`

### What Qualifies as a Serious Adverse Event (SAE)

ANY of these outcomes from product use:
- Death
- Life-threatening experience
- Hospitalization (inpatient)
- Persistent or significant disability/incapacity
- Birth defect or congenital anomaly
- Medical intervention required to prevent one of the above

### Adverse Event Response Procedure

**Step 1: Immediate Response** (within 1 hour of report)
- Tell customer to **stop using the product immediately**
- Advise them to **contact their healthcare provider**
- Express concern and document the interaction

**Step 2: Documentation** (within 24 hours)
- Complete controlled complaint form:
  - Customer name, contact info
  - Product name, lot number, purchase date
  - Symptoms reported (customer's exact words)
  - Timeline (when started using, when symptoms appeared)
  - Medical history relevant to complaint (only what customer volunteers)
  - Whether customer sought medical attention

**Step 3: Assessment** (within 48 hours)
- Classify as SAE or non-serious
- If SAE → proceed to Step 4
- If non-serious → document fully, voluntary FDA submission recommended

**Step 4: FDA Reporting** (within 15 business days of receiving report)
- Submit via FDA MedWatch Form 3500A
- Include all documentation from Step 2
- Retain all records for **6 years**

**Step 5: Internal Review**
- Pull the lot number — check for other reports
- Review manufacturing/fulfillment for that lot
- If pattern emerges → consider voluntary recall consultation with FDA

### IonWave Label Requirements

Product label MUST include a domestic US address or phone number for adverse event reporting. This is a legal requirement, not a customer service choice. `[Confidence: A | Source: 21 CFR, FDA regulations | Date: 2026]`

> **CRITICAL**: Consult with a supplement industry attorney before launch to review adverse event procedures. This protocol is a starting framework, not legal advice. `[Priority: CRITICAL | Track: B — requires legal review]`

---

## 5. Issue Tracking System

### Issue Log Structure

Every support ticket that reveals a product, process, or systemic issue should be logged:

| Field | Description | Example |
|-------|-------------|---------|
| Date | When reported | 2026-03-15 |
| Order # | Shopify order reference | #1042 |
| Customer | Name/email | jane@example.com |
| Issue Type | Category (see below) | Shipping Damage |
| Description | Customer's words | "Package arrived crushed, sachets leaking" |
| Root Cause | What went wrong | Insufficient packaging for sachet format |
| Resolution | What we did | Full refund + free replacement + packaging upgrade |
| Cost | Resolution cost to IonWave | $38 (product) + $8 (shipping) = $46 |
| Resolved? | Yes/No | Yes |
| Systemic? | Pattern or one-off? | Yes — 3rd damage report this month |

### Issue Type Categories

| Category | Description | Expected % of Tickets |
|----------|-------------|----------------------|
| **Shipping/Delivery** | Delays, damage, lost packages, tracking issues | 25-35% |
| **Subscription Management** | Skip, pause, cancel, swap, billing questions | 20-30% |
| **Product Quality** | Taste, texture, efficacy, appearance issues | 10-15% |
| **Wrong Item/Missing** | Wrong product sent, items missing from order | 5-10% |
| **Billing/Payment** | Overcharges, failed payments, refund status | 10-15% |
| **Product Education** | Dosage, usage instructions, ingredient questions | 10-15% |
| **Other** | Catch-all | 5% |

`[Confidence: C | Source: synthesis of DTC supplement ticket distribution research | Date: 2026]`

### Systemic Issue Detection

When any issue type hits **3+ occurrences in 30 days**, it triggers a root cause investigation:

| Occurrences (30-day) | Action |
|----------------------|--------|
| 3 | Flag in weekly review |
| 5 | Root cause analysis required |
| 10 | Process change required — escalate to founder |
| 15+ | Emergency review — potential product/fulfillment issue |

### Support Macro Library

Pre-written templates for Gorgias (customize per-ticket):

**Macro 1: WISMO (Where Is My Order?)**
> Hi [Name]! Thanks for reaching out. I just checked your order #[number] and it's [currently in transit / out for delivery / delivered on [date]]. You can track it here: [tracking link]. If you don't see any updates in the next [24/48] hours, reply to this email and I'll dig deeper for you. — [Agent Name], IonWave

**Macro 2: Subscription Cancel Request**
> Hi [Name], I understand you'd like to cancel your subscription. Before I process that, I wanted to let you know about a couple of options: [1] **Pause** your subscription for 1-3 months (no charge until you resume), or [2] **Skip** your next delivery and adjust your schedule. If you'd still like to cancel, I completely understand — just reply "cancel" and I'll take care of it right away. No hard feelings! — [Agent Name], IonWave

**Macro 3: Product Not Working / Efficacy Complaint**
> Hi [Name], thank you for letting me know. I want to make sure you're getting the most from IonWave. A few questions: [1] How long have you been using it? [2] Are you taking it daily? [3] When do you take it (morning, with meals, etc.)? Most customers notice a difference after 2-3 weeks of consistent daily use. If you've been using it consistently and aren't seeing results after 30 days, we offer a full money-back guarantee on first orders. I'd love to help you get the best experience — let me know! — [Agent Name], IonWave

**Macro 4: Taste/Texture Complaint**
> Hi [Name], I appreciate you sharing that feedback — taste experience matters to us. A few things that often help: [1] **Mix with juice or sparkling water** instead of plain water, [2] **Adjust the amount of water** (more water = more diluted), [3] **Try it cold** — temperature makes a big difference. If you've tried these and still aren't happy, we stand behind our 30-day satisfaction guarantee. Just say the word and I'll process a refund. — [Agent Name], IonWave

**Macro 5: Shipping Damage**
> Hi [Name], I'm really sorry your order arrived damaged. That's not the experience we want for you. I've already queued a free replacement to ship out [today/tomorrow], and you don't need to return the damaged product. You should receive tracking info within [24 hours]. I've also flagged this with our fulfillment team so we can improve packaging. Thanks for your patience! — [Agent Name], IonWave

**Macro 6: Adverse Reaction / Health Concern**
> Hi [Name], thank you for letting me know. Your health is our top priority. I strongly recommend: [1] **Please stop using the product immediately**, [2] **Contact your healthcare provider** if symptoms persist. I'm escalating this to our team lead right now. Someone will reach out to you personally within [1 hour] to get more details and make sure you're taken care of. Is there a phone number where we can reach you? — [Agent Name], IonWave

> **Note**: Macro 6 triggers an immediate Tier 4 escalation. It is NOT a resolution — it's a handoff to the adverse event procedure (Section 4).

---

## 6. Refund & Return Policy

### Policy Summary

| Scenario | Action | Who Pays Return | Keep Product? |
|----------|--------|----------------|---------------|
| First order, within 30 days, any reason | Full refund | N/A — keep the product | Yes |
| First order, opened/used | Full refund | N/A — keep the product | Yes |
| First order, unopened | Full refund | IonWave pays return | Return |
| Repeat order, within 30 days, product issue | Refund or exchange | Case-by-case | Usually yes |
| Repeat order, changed mind | Store credit or exchange | Customer pays return | Return |
| International order, any reason | Full refund | N/A — keep the product | Yes (return shipping uneconomical) |
| Subscription auto-ship, unwanted | Refund current shipment + pause/cancel sub | N/A — keep | Yes |

`[Confidence: B | Source: Synthesis of industry best practices (Onnit, Care/of, 1st Phorm models) | Date: 2026]`

### Why "Keep the Product" for First Orders

1. Used supplements cannot be resold (hygiene/safety regulations) `[Confidence: B]`
2. Return shipping costs often exceed product COGS for sachets `[Confidence: C]`
3. Friction-free refunds build trust and reduce chargeback disputes `[Confidence: B]`
4. 81% of shoppers review return policies before purchasing `[Confidence: B]`

### Refund Processing Workflow

**Step 1**: Verify order (order number, customer email, purchase date)
**Step 2**: Ask reason for refund (select from categories below)
**Step 3**: Process in Shopify (Gorgias has refund action in ticket view)
**Step 4**: Log in refund tracker (see below)
**Step 5**: Tag in Gorgias for reporting

### Refund Reason Categories

| Reason Code | Category | Description | Expected % |
|-------------|----------|-------------|------------|
| RF-001 | Taste/Texture | Didn't like the taste or texture | 15-20% |
| RF-002 | No Results | Didn't feel a difference | 20-25% |
| RF-003 | Shipping Damage | Product arrived damaged | 10-15% |
| RF-004 | Ordered by Mistake | Accidental purchase or wrong item | 5-10% |
| RF-005 | Found Alternative | Switched to competitor or doesn't need | 10-15% |
| RF-006 | Subscription Unwanted | Didn't realize it was a subscription | 15-20% |
| RF-007 | Price/Value | Too expensive for perceived value | 5-10% |
| RF-008 | Adverse Reaction | Health concern (triggers Tier 4) | 1-3% |
| RF-009 | Other | Catch-all | 5% |

`[Confidence: C | Source: Danilo's 7-category framework expanded with research findings | Date: 2026]`

### Refund Rate Health Benchmarks

| Rate | Status | Action |
|------|--------|--------|
| <5% | Excellent | Maintain course |
| 5-8% | Healthy | Monitor monthly |
| 8-12% | Watch | Investigate top reason codes |
| 12-15% | Concerning | Root cause analysis, process changes required |
| >15% | Alarming | Product/positioning problem — escalate to business review |

General e-commerce return rate: 20-30%. Supplement-specific refund target: <12% for healthy business. `[Confidence: C | Source: industry benchmarks + Capital and Growth research | Date: 2026]`

### Refund Tracker Summary (Monthly)

| Metric | How to Calculate | Target |
|--------|-----------------|--------|
| Refund count (MTD) | Count of refund transactions | Track trend |
| Refund rate | Refunds / Total orders × 100 | <8% |
| Average refund amount | Total $ refunded / Refund count | Track trend |
| Top reason code | Most frequent RF-XXX | Monitor for patterns |
| Exchange rate | Exchanges / (Exchanges + Refunds) × 100 | >30% (higher = healthier) |
| Cost of refunds | Total $ refunded + shipping costs | Track as % of revenue |

---

## 7. Chargeback Monitoring & Prevention

### Why This Is Critical for Supplements

Supplements are classified as **high-risk** by payment processors. Stripe's dispute (chargeback) rate threshold is **0.75%** — exceeding it can result in:
- Account under review
- Reserve fund requirements (10-20% of processing volume held)
- Account termination (losing the ability to process payments)
- Forced migration to high-risk processor (higher fees)

`[Confidence: A | Source: Stripe Terms of Service, payment processor industry standards | Date: 2026]`

### Chargeback vs. Refund: Different Metrics, Different Consequences

| Metric | What It Is | Threshold | Consequence of Exceeding |
|--------|-----------|-----------|------------------------|
| **Refund rate** | Refunds you initiate / Total orders | <8% healthy, >15% alarming | Margin erosion, product/positioning signal |
| **Chargeback rate** | Customer disputes with bank / Total transactions | **<0.75%** (Stripe), <1% (general) | Payment processor flags, account at risk |

**Chargebacks are 10x more expensive than refunds**: Each chargeback costs the product amount + $15-25 dispute fee + potential fines + processor relationship damage.

### Proactive Refund Strategy (Prevent Chargebacks)

1. **Refund before they dispute**: If a customer is unhappy and seems likely to dispute, proactively offer a refund. A $30 refund is better than a $30 chargeback + $25 fee.
2. **Clear billing descriptor**: Make sure the credit card statement shows "IONWAVE" (not "SHOPIFY*123"). Unfamiliar descriptors cause "I don't recognize this charge" disputes.
3. **Pre-shipment subscription reminder**: Email before each subscription charge. "Your order ships in 3 days — manage or skip here." Prevents "I didn't authorize this" disputes.
4. **Easy cancellation**: Per FTC Click-to-Cancel guidance, cancellation must be as easy as signup. Making it hard to cancel INCREASES chargebacks. `[Confidence: A | Source: FTC proposed rule]`

### Chargeback Response Protocol

| Rate | Status | Action |
|------|--------|--------|
| <0.25% | Healthy | Monitor monthly |
| 0.25-0.50% | Watch | Review all disputes, identify patterns |
| 0.50-0.75% | Warning | Emergency review — implement all prevention measures |
| >0.75% | Critical | Contact payment processor proactively, consider chargeback management service (Chargeflow, Chargeback.io) |

### Chargeback Tracker (Monthly)

| Metric | How to Calculate | Target |
|--------|-----------------|--------|
| Total chargebacks | Count of disputes filed | Track trend |
| Chargeback rate | Chargebacks / Total transactions × 100 | <0.50% |
| Win rate (disputes won) | Disputes won / Total disputes × 100 | >60% |
| Top chargeback reason | Most frequent reason code | Monitor |
| Chargeback cost | (Product + fees) per chargeback | Minimize |

`[Confidence: B | Source: Payment processor industry standards + Stripe documentation | Date: 2026]`

---

## 8. Support Performance Metrics

### Weekly Support Scorecard

| Metric | Target | Red Flag |
|--------|--------|----------|
| First response time (email) | <1 hour | >4 hours |
| First response time (chat) | <30 seconds | >2 minutes |
| First contact resolution rate | >80% | <60% |
| CSAT (support interactions) | >88% | <75% |
| **Activation rate** (4-criteria behavioral) | >50% | <30% |
| Refund rate | <8% | >15% |
| **Chargeback rate** | <0.50% | >0.75% (CRITICAL) |
| Tickets per 1,000 orders | <700 | >900 |
| Escalation rate (Tier 1 → Tier 2+) | <15% | >25% |
| Cost per ticket | <$5 | >$10 |

> **Activation rate** measures 4 behavioral criteria (see `customer_success_playbook.md` Section 4). It is the single best early predictor of subscription retention — if activation drops below 30%, the problem is upstream of support (onboarding, product, or targeting).

`[Confidence: B-C | Source: Gorgias, industry benchmark synthesis | Date: 2026]`

### Ticket Volume Expectations

| Stage | Orders/Month | Expected Tickets | Ticket:Order Ratio |
|-------|-------------|------------------|-------------------|
| Pre-launch (Month 0-1) | 50-100 | 40-80 | 0.8:1 |
| Early traction (Month 2-6) | 100-500 | 70-350 | 0.7:1 |
| Growth (Month 6-12) | 500-2,000 | 300-1,200 | 0.6:1 |
| Scale (Month 12+) | 2,000+ | 1,000+ | 0.5:1 |

Ratio decreases over time as self-service, FAQ, and automation improve. `[Confidence: C | Source: e-commerce support volume research | Date: 2026]`

---

## 8. Social Media Complaint Handling

### The Public-DM-Public Close Pattern

**Step 1: Acknowledge Publicly** (within 60 minutes)
> "Hi [Name], thanks for flagging this. I'm looking into it right now. Going to send you a DM so we can sort this out quickly."

**Step 2: Move to DM**
> Handle details, order info, and any health-related data privately. Never share order numbers, personal info, or health details in public replies.

**Step 3: Resolve Privately**
> Follow standard resolution procedures (AAAA+F for escalated cases).

**Step 4: Close Publicly**
> "Happy to report this is all sorted, [Name]! Thanks for giving us the chance to make it right." (Only if customer consents to public acknowledgment.)

`[Confidence: B | Source: B Squared Media, DTC social support best practices | Date: 2026]`

### Why This Pattern Matters for Supplements

- Public complaints may involve sensitive health information → privacy requirement
- Other potential customers are watching → demonstrate responsiveness
- 42% of consumers expect social media complaint response within 60 minutes `[Confidence: B]`
- **Never delete public complaints** — signals unwillingness to engage and amplifies negative sentiment

---

## Intelligence Gaps

| Gap | Priority | Validation Path |
|-----|----------|----------------|
| Gorgias AI Agent accuracy on supplement queries | MEDIUM | Test with 50 sample tickets post-launch |
| Actual ticket volume per 1,000 orders (IonWave-specific) | LOW | Measure after first 100 orders |
| Optimal agent authority dollar thresholds | LOW | Calibrate after 3 months of ticket data |
| Adverse event procedure legal review | CRITICAL | Supplement industry attorney review pre-launch |
| Sachet-specific shipping damage rate | MEDIUM | Track after first 500 shipments |


---

## 🔗 Dependencies & Relationships

### Feeds Into
- m19
- m27
- m21

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

- **Adverse event procedure legal review**
  - Priority: CRITICAL
- **Activation rate baseline targets**
  - Priority: HIGH
- **Win/loss reason percentages**
  - Priority: HIGH
- **Expected outcomes timeline for marine plasma**
  - Priority: HIGH
- **Gorgias AI Agent accuracy on supplement queries**
  - Priority: MEDIUM
- **Sachet-specific shipping damage rate**
  - Priority: MEDIUM
- **Optimal NPS timing for supplements (Day 21 vs 30 vs 45)**
  - Priority: MEDIUM

---

## 🎯 Next Actions

Populate win/loss data post-launch; validate activation rate targets after first 100 customers; legal review of adverse event protocol


---

## 🧰 OpKits

- OK-M20-001

---

---

_Report generated: 2026-02-09 17:49:44_

_Source: `data\m20`_