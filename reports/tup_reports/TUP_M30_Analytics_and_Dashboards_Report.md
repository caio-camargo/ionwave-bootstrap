# TUP M30: Analytics & Dashboards

**Status:** migrated | **Quality:** N/A/10 | **Version:** N/A
**Cluster:** BCL-6 (N/A)

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

### 📄 dashboards_and_reporting.md

# M30 Dashboards & Reporting
**TUP**: M30 Analytics & Dashboards
**Source Tabs**: 628 (Reporting Templates), 629 (Metrics Dashboard Master), 630 (Key Metrics Dashboard), 631 (KPI Dashboard)
**Version**: 1.0.0
**Quality**: 7.5/10
**Status**: Workshop Draft
**Confidence Baseline**: B-C (industry frameworks applied to IonWave stage)

---

## Purpose
Define what IonWave looks at, how often, and in what format. This is the operating rhythm made visible — the daily, weekly, monthly, and quarterly heartbeat of the business.

**Design Principle**: Founder Mode first. One person, wearing all hats, needs to check the business health in <5 minutes daily. No enterprise dashboarding tools needed at launch — a Google Sheet + Slack bot will do until $50K+ MRR.

---

## 1. Dashboard Architecture — Staged by Growth Phase

### Phase 0: Pre-Launch (Month 0)
**Tool**: Google Sheets + manual entry
**Time commitment**: 10 min/day

Track ONLY:
- Email list growth (daily count)
- Landing page conversion rate
- Pre-launch survey responses
- Cash remaining vs budget

### Phase 1: Launch → $10K MRR (Months 1-6)
**Tool**: Google Sheets MVD (Minimum Viable Dashboard) + Shopify native analytics + Meta Ads Manager
**Time commitment**: 10 min/day, 30 min/week, 1 hr/month

#### Minimum Viable Dashboard (MVD) — The Only 7 Numbers That Matter
*(Dialogue Upgrade U1: A solo founder tracking 50 metrics is tracking zero metrics.)*

| # | Metric | Target | Source | Cadence |
|---|--------|--------|--------|---------|
| 1 | **Revenue** (net) | Growing MoM | Shopify | Daily |
| 2 | **Orders** | Growing MoM | Shopify | Daily |
| 3 | **Ad Spend** | Within budget | Meta Ads | Daily |
| 4 | **CAC** (blended) | <$40 | Calculated: Spend / New Customers | Weekly |
| 5 | **Subscription Rate** | >50% | Subscription platform | Weekly |
| 6 | **Cash Balance** | >60 days runway | Bank | Daily |
| 7 | **MER** (blended efficiency) | >3x | Calculated: Total Revenue / Total Marketing | Weekly |

**Everything else waits.** No creative metrics, no cohort analysis, no NPS, no email revenue % until Phase 2. The MVD is a Google Sheet with 7 rows, conditional formatting (green/yellow/red), and formulas pre-built. See OpKit for template.

#### Phase 1 Full Cadence (builds on MVD)

| Cadence | What to Check | Where | Time |
|---------|--------------|-------|------|
| **Daily** | MVD metrics 1-3, 6 (Revenue, Orders, Spend, Cash) | Shopify + Meta + Bank | 5 min |
| **Daily** | Support tickets (any fires?) | Helpdesk | 3 min |
| **Weekly** | MVD metrics 4-5, 7 (CAC, Sub Rate, MER) | Calculated in Sheets | 10 min |
| **Weekly** | Inventory days remaining | 3PL + Sheets | 5 min |
| **Monthly** | Simplified MBR (see §4 below) | Sheets + Accounting | 1 hr |
| **Monthly** | Red Flag Dashboard scan (existential metrics only) | Sheets | 10 min |

#### Vanity Metrics Ban List — Phase 1 (Dialogue Upgrade U12)
The following metrics are explicitly BANNED from Phase 1 dashboards. They feel productive but drive zero revenue decisions:
- Social media followers (Instagram, TikTok, Twitter)
- Website pageviews (without conversion context)
- Email list size (without engagement rates)
- Instagram/TikTok engagement rate
- "Brand awareness" metrics of any kind
- Press mentions count

These may enter at Phase 3 ($50K+ MRR) when a brand marketing budget exists.

### Phase 2: $10K-$50K MRR (Months 6-12)
**Tool**: Add Triple Whale or Polar Analytics for attribution + automated dashboards
**Time commitment**: 10 min/day, 1 hr/week, 3 hrs/month

New additions:
- Automated daily Slack digest (revenue, orders, ROAS, CAC)
- Multi-touch attribution reporting
- Amazon channel dashboard (if launched)
- Creative performance tracker
- Cohort analysis automation

### Phase 3: $50K+ MRR (Month 12+)
**Tool**: Consider Looker/Metabase for custom dashboards if team grows beyond founder
**Time commitment**: Delegated to ops/analytics hire

New additions:
- Custom BI dashboards
- B2B channel reporting
- Retail channel reporting
- Team KPI dashboards
- Automated alerting (Slack/email when thresholds hit)

[Confidence: B | Source: D2C founder best practices, Triple Whale/Polar feature sets, IonWave growth model | Verified: 2026-02-08]

---

## 2. Founder Daily Check-In (The 5-Minute Pulse)

**When**: Every morning, before starting work.
**Where**: Shopify app + Meta Ads app + Bank app (mobile-first)

```
DAILY PULSE — [Date]
━━━━━━━━━━━━━━━━━━━━
Revenue:     $[___]  (vs yesterday: +/-%)
Orders:      [___]   (vs yesterday: +/-%)
Ad Spend:    $[___]
ROAS:        [___]x  (🟢 >2.5x | 🟡 1.5-2.5x | 🔴 <1.5x)
Cash:        $[___]  (runway: [___] days)
Fires:       [any support issues/stockouts/ad problems?]
━━━━━━━━━━━━━━━━━━━━
One thing to fix today: _______________
```

**Rule**: If any metric is RED, that becomes the day's #1 priority. Everything else waits.

**Slack Format** (for team updates):
```
📊 IonWave Daily — [Date]
💰 Revenue: $[X] | Orders: [X] | AOV: $[X]
📈 Ad Spend: $[X] | ROAS: [X]x | CAC: $[X]
🔋 Cash: $[X] | Runway: [X] days
🚦 Status: [🟢/🟡/🔴]
```

---

## 3. Weekly Report

**When**: Every Monday morning
**Audience**: Founder + any advisors/investors who requested updates
**Time to produce**: 30 minutes

### Template

```
IONWAVE WEEKLY — Week of [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 KEY METRICS
| Metric          | This Week | Last Week | Change | Target | Status |
|-----------------|-----------|-----------|--------|--------|--------|
| Revenue         | $[___]    | $[___]    | +/-%   | $[___] | 🟢/🟡/🔴 |
| Orders          | [___]     | [___]     | +/-%   | [___]  | 🟢/🟡/🔴 |
| New Customers   | [___]     | [___]     | +/-%   | [___]  | 🟢/🟡/🔴 |
| CAC (blended)   | $[___]    | $[___]    | +/-%   | <$40   | 🟢/🟡/🔴 |
| ROAS            | [___]x    | [___]x    | +/-%   | >2.5x  | 🟢/🟡/🔴 |
| Subscription %  | [___]%    | [___]%    | +/-%   | >50%   | 🟢/🟡/🔴 |
| MER             | [___]x    | [___]x    | +/-%   | >3x    | 🟢/🟡/🔴 |

🏆 WINS
• [What worked this week]
• [What worked this week]

🚧 BLOCKERS
• [What's stuck or broken]
• [What's stuck or broken]

📋 NEXT WEEK PRIORITIES
1. [Top priority]
2. [Second priority]
3. [Third priority]

🚨 RED FLAGS: [Any kill criteria approaching? Y/N — if Y, detail below]
```

---

## 4. Monthly Business Review (MBR)

### Early-Stage MBR (Months 1-3) — 1 Hour Max
*(Dialogue Upgrade U5: No pre-revenue founder should spend a full day on an MBR.)*

**When**: First week of each month
**Time**: 1 hour total — that's it.

The early-stage MBR answers exactly 4 questions:

**Q1: Are we acquiring customers at viable economics?**
- CAC this month: $[___] (target: <$40, kill: >$60)
- MER this month: [___]x (target: >3x)
- New customers: [___]

**Q2: Are they staying?**
- Subscription conversion: [___]% (target: >50%, YELLOW: <30%)
- Churn (if data available): [___]% (target: <8%)
- Any churn patterns? (cancellation reasons)

**Q3: How much cash do we have?**
- Cash on hand: $[___]
- Runway at current burn: [___] days (kill: <30)
- Cash in vs cash out this month: $[___] vs $[___]

**Q4: What are we doing differently next month?**
- Top learning from this month: ___
- #1 priority for next month: ___
- Anything to stop doing: ___

#### Monthly Hypothesis Prompt (Dialogue Upgrade U13)
For each of the 3 most critical hypotheses, write ONE sentence:

> "HYP-001 (CAC): This month's data [supports/weakens/doesn't change] this hypothesis because [specific reason]."
> "HYP-002 (Subscription): This month's data [supports/weakens/doesn't change] this hypothesis because [specific reason]."
> "HYP-003 (Churn): This month's data [supports/weakens/doesn't change] this hypothesis because [specific reason]."

If you can't write that sentence, you're not measuring the right things.

---

### Full MBR (Month 4+) — 3 Hours Max

**When**: First week of each month
**Time**: 2-3 hours of analysis + 1 hour review meeting (if team/advisors)

Expand to the full 8-section MBR only after Month 3, when you have enough data to make it worthwhile:

**Section 1: Executive Summary** (1 page)
- MRR and growth trajectory
- Months to $30K MRR target (updating projection monthly)
- Cash runway
- One-sentence health assessment: "On track / Watch / At risk / Critical"

**Section 2: Revenue Deep Dive**
- Revenue by channel (D2C, Amazon, B2B when applicable)
- Revenue by customer type (new vs returning vs subscription)
- AOV trends
- MRR bridge (beginning MRR + new + expansion - contraction - churn = ending MRR)

**Section 3: Acquisition**
- CAC by channel (Meta, Google, organic, referral, influencer)
- Best and worst performing creatives (top/bottom 3)
- CVR funnel: Impressions → Clicks → ATC → Purchase
- Email list growth and capture rate

**Section 4: Retention**
- Cohort retention table (each monthly cohort's retention curve)
- Churn analysis: voluntary vs involuntary, reasons
- Subscription conversion trends
- Monthly hypothesis prompt (see above)

**Section 5: Operations**
- Inventory status and reorder timeline
- Support ticket volume and satisfaction
- Shipping performance

**Section 6: Financial Health**
- Full P&L (revenue, COGS, gross margin, opex, net)
- Cash flow vs projection
- Updated 13-week cash forecast (from M25)

**Section 7: Red Flag & Hypothesis Check**
- Existential metrics status (CAC, Cash, Contribution Margin)
- Monitoring metrics status (all others)
- Hypothesis prompt for top 3 hypotheses
- Any confidence grade changes?

**Section 8: Decisions Needed**
- List of decisions to make this month
- Data supporting each decision
- Recommendation

**Cross-Reference**: Monthly MBR structure integrates with M25 Survival Five scorecard. The MBR IS the Survival Five review — don't create two separate processes.

[Confidence: B | Source: D2C MBR best practices, M25 Survival Five framework, Y Combinator startup metrics guidance | Verified: 2026-02-08]

---

## 5. Quarterly Deep Review

**When**: End of Q1 (Month 3), Q2 (Month 6), Q3 (Month 9), Q4 (Month 12)
**Time**: Half-day (4-6 hours)

### QBR Additions Beyond Monthly
- **Competitive landscape refresh** — has anything changed? (reference M26)
- **ICP validation** — are we selling to who we expected? (reference M27)
- **Pricing review** — should price/offer change? (reference M10)
- **Channel mix review** — rebalance channel allocation? (reference M28)
- **Hypothesis formal review** — upgrade/downgrade confidence grades, update validation plans
- **Portfolio Reality Check** — are we still on a viable path? (reference M28 constraint scenarios)
- **Product development pipeline** — any new SKUs warranted? (reference M28 product readiness triggers)

### Go/No-Go Gates
**Month 3**: First real data checkpoint. Enough to see CAC and initial conversion patterns.
- GREEN: CAC <$45, CVR >2%, subscription rate >35% → continue, optimize
- YELLOW: CAC $45-55, CVR 1.5-2%, sub rate 25-35% → investigate, adjust
- RED: CAC >$55, CVR <1.5%, sub rate <25% → pivot or kill discussion

**Month 6**: Follow-on capital decision point (from IonWave financial model).
- GREEN: On track for $15K+ MRR by Month 12 → raise follow-on
- YELLOW: $8-15K MRR trajectory → extend runway, optimize
- RED: <$8K MRR trajectory → serious pivot or wind-down

**Month 12**: Full-year review.
- Validate or invalidate each hypothesis with real data
- Update all projections with actuals
- Make Year 2 plan

---

## 6. Metrics Master View — IonWave KPIs

The consolidated single-page dashboard view. This is what you'd print and pin to the wall.

### Revenue & Growth
| Metric | Target | Warning | Kill | Cadence |
|--------|--------|---------|------|---------|
| MRR | $25K by M12 | <$8K at M6 | Negative growth 3 months | Monthly |
| MoM Growth | >20% | <10% | Negative 2 months | Monthly |
| AOV | $49 | <$35 | <$25 | Weekly |

### Acquisition
| Metric | Target | Warning | Kill | Cadence |
|--------|--------|---------|------|---------|
| CAC | <$40 | >$50 | >$60 for 14 days | Weekly |
| ROAS | >2.5x | <2x | <1.5x for 7 days | Daily |
| CVR | >2.5% | <2% | <1% | Daily |
| CTR | >1% | <0.5% | N/A | Daily |

### Retention
| Metric | Target | Warning | Kill | Cadence |
|--------|--------|---------|------|---------|
| Subscription % | >50% | <30% | <10% | Weekly |
| Monthly Churn | <8% | >12% | >15% for 2 months | Monthly |
| LTV:CAC | >3x | <2x | <1.5x | Monthly |
| Email Revenue % | >25% | <15% | N/A | Weekly (activate Month 3+, requires 1K+ subscribers — U9) |

### Operations
| Metric | Target | Warning | Kill | Cadence |
|--------|--------|---------|------|---------|
| Inventory Days | 30-45 | <14 | <7 | Weekly |
| Ship Time | <3 days | >5 days | >7 days | Daily |
| CSAT | >4.5 | <4.0 | <3.5 | Weekly |
| Chargeback Rate | <0.3% | >0.5% | >0.75% | Monthly |

### Financial
| Metric | Target | Warning | Kill | Cadence |
|--------|--------|---------|------|---------|
| Gross Margin | >65% | <60% | <50% | Monthly |
| Contribution Margin | >20% | <10% | Negative 30 days | Monthly |
| Runway | >90 days | <60 days | <30 days | Weekly |

---

## 7. Tool Progression

| Phase | Revenue | Analytics Stack | Cost | Setup Time |
|-------|---------|----------------|------|------------|
| Pre-launch | $0 | Google Sheets + Shopify native | $0 | 4 hrs |
| Launch ($0-10K MRR) | <$10K/mo | + Klaviyo analytics + Meta Ads dashboard | $0 (included) | 2 hrs |
| Growth ($10-50K MRR) | $10-50K/mo | + Triple Whale or Polar Analytics + post-purchase survey | $100-300/mo | 8 hrs |
| Scale ($50K+ MRR) | $50K+/mo | + Looker/Metabase (if team) + automated alerts | $500-1K/mo | 20+ hrs |

**Rule**: Never buy tools ahead of the data to fill them. A Google Sheet you actually update daily beats a $500/mo dashboard nobody checks.

[Confidence: B | Source: Triple Whale/Polar pricing, D2C analytics stack surveys, YC startup guidance | Verified: 2026-02-08]

---

## 8. Intelligence Gaps

| Gap | Impact | Upgrade Path | Priority |
|-----|--------|-------------|----------|
| G1: Templates are theoretical (no real data) | Can't validate utility until launch | First real MBR at Month 1 will reveal what's useful vs noise | HIGH (time-gated) |
| G2: Tool recommendations need testing | Pricing and features may change | Trial Triple Whale/Polar at $10K MRR, evaluate fit | MEDIUM |
| G3: Reporting cadence may be too heavy for solo founder | Risk of metric fatigue → stops checking | Start with daily pulse only, add weekly/monthly gradually | MEDIUM |


---

### 📄 data_dictionary.md

# M30 Data Dictionary
**TUP**: M30 Analytics & Dashboards
**Source Tabs**: 627 (Data Dictionary)
**Version**: 1.0.0
**Quality**: 7.5/10
**Status**: Workshop Draft
**Confidence Baseline**: B-C (industry-standard definitions applied to IonWave context)

---

## Purpose
Single source of truth for every metric IonWave tracks. Every metric has a precise definition, formula, data source, and update cadence so that two people looking at the same number always agree on what it means.

**Rule**: If a metric appears in any dashboard, report, or decision framework, it MUST have an entry here. No orphan metrics.

---

## 1. Revenue & Growth Metrics

| Metric | Definition | Formula | Source | Cadence | Notes |
|--------|-----------|---------|--------|---------|-------|
| **Revenue** | Total gross revenue before refunds/returns | Sum of all order values | Shopify | Daily | Includes one-time + subscription |
| **Net Revenue** | Revenue minus refunds, returns, chargebacks | Revenue - Refunds - Returns - Chargebacks | Shopify | Daily | This is the number that matters |
| **MRR** | Monthly Recurring Revenue from active subscriptions | Sum of all active subscription values | Subscription platform (Recharge/Loop) | Daily | Excludes one-time purchases |
| **ARR** | Annualized Recurring Revenue | MRR x 12 | Calculated | Monthly | Projection, not actuals |
| **MoM Growth** | Month-over-month revenue growth rate | (This Month Revenue - Last Month Revenue) / Last Month Revenue | Calculated | Monthly | Use net revenue |
| **AOV** | Average Order Value | Net Revenue / Total Orders | Shopify | Daily | Track separately for one-time vs subscription |
| **Revenue per Customer** | Average revenue generated per unique customer | Net Revenue / Unique Customers | Shopify | Monthly | Different from AOV (one customer can have multiple orders) |
| **Subscription Revenue %** | Share of revenue from subscriptions vs one-time | Subscription Revenue / Total Net Revenue | Calculated | Weekly | Target: >50%. Below 30% = YELLOW (see HYP-002 sensitivity) |

[Confidence: B | Source: Shopify standard definitions + IonWave model parameters | Verified: 2026-02-08]

---

## 2. Acquisition Metrics

| Metric | Definition | Formula | Source | Cadence | Notes |
|--------|-----------|---------|--------|---------|-------|
| **CAC** | Cost to Acquire a Customer | Total Marketing Spend / New Customers Acquired | Meta Ads + Shopify | Weekly | Use blended CAC (all channels) AND per-channel CAC. See HYP-001. |
| **Blended CAC** | CAC across all channels including organic | Total Marketing Spend / All New Customers (paid + organic) | All platforms | Weekly | Always lower than paid CAC. Track both. |
| **MER** | Marketing Efficiency Ratio — PRIMARY efficiency metric (Dialogue Upgrade U2) | Total Revenue / Total Marketing Spend | Calculated | Weekly | **Use this, not ROAS, for business decisions.** Includes organic revenue. Honest measure of total marketing efficiency. Target: >3x. Kill: <1.5x. |
| **ROAS** | Return on Ad Spend — SECONDARY, platform context only (U2) | Revenue attributed to ads / Ad Spend | Meta Ads Manager | Daily (during active spend) | Platform-reported ROAS overstates by 20-40% post-iOS 14.5. Use ONLY for comparing creatives/campaigns within Meta. Never use for business-level decisions. |
| **CPC** | Cost per Click | Ad Spend / Clicks | Meta Ads | Daily | Monitor for CPM inflation trends |
| **CPM** | Cost per 1,000 Impressions | (Ad Spend / Impressions) x 1,000 | Meta Ads | Daily | Rising CPMs = category getting crowded or creative fatigue |
| **CTR** | Click-Through Rate | Clicks / Impressions | Meta Ads | Daily | Target: >1%. Below 0.5% = creative problem |
| **CVR** | Conversion Rate (site) | Orders / Sessions | Shopify + GA4 | Daily | Target: >2.5%. Below 1.5% = landing page problem |
| **CPA** | Cost per Acquisition (any action) | Spend / Desired Actions | Meta Ads | Daily | Can be cost per lead, per ATC, per purchase |
| **New Customers** | Count of first-time purchasers | Unique customers with first order in period | Shopify | Daily | Distinguish from returning customers |
| **Email Capture Rate** | % of visitors who provide email | Email signups / Unique visitors | Klaviyo + GA4 | Weekly | Target: 5-10% with pop-up |
| **Post-Purchase Survey Attribution** | Self-reported "how did you hear about us?" | Survey responses categorized by channel | Post-purchase survey tool (e.g., Fairing/Enquire Labs) | Weekly | **Awareness attribution** — tells you where they DISCOVERED you. See attribution model below. |

### Attribution Model — Awareness vs Conversion (Dialogue Upgrade U4)

Two types of attribution answer different questions:

| Type | Question Answered | Source | Use For |
|------|------------------|--------|---------|
| **Awareness Attribution** | "How did they find us?" | Post-purchase survey | Channel investment decisions (should we spend more on podcasts vs Instagram?) |
| **Conversion Attribution** | "What drove the click/purchase?" | UTM parameters / last-click | Campaign optimization (which ad drove this purchase?) |

**When they disagree** (e.g., survey says "podcast" but UTM says "Meta retargeting ad"): This is NOT a data error. It means the customer discovered IonWave through a podcast but converted through a Meta retargeting ad. That's multi-touch attribution — both channels contributed. Neither is wrong.

**Decision rule**: For channel INVESTMENT decisions (should we sponsor more podcasts?), weight awareness attribution (survey) at 60% and conversion attribution (UTM) at 40%. For campaign OPTIMIZATION decisions (which ad creative works best?), use conversion attribution (UTM) only.

[Confidence: B | Source: Meta Ads standard definitions, Shopify analytics, M28 attribution model (U2), post-iOS 14.5 attribution research | Verified: 2026-02-08]

---

## 3. Retention & Subscription Metrics

| Metric | Definition | Formula | Source | Cadence | Notes |
|--------|-----------|---------|--------|---------|-------|
| **Monthly Churn** | % of active subscribers who cancel in a month | Cancelled Subscriptions / Active Subscriptions at start of month | Subscription platform | Monthly | Target: <8%. Kill: >15% for 2 months. See HYP-003. |
| **Voluntary Churn** | Churn from active customer cancellation | Voluntary Cancellations / Active Subs | Subscription platform | Monthly | Track separately from involuntary |
| **Involuntary Churn** | Churn from failed payments | Failed Payment Cancellations / Active Subs | Subscription platform + Stripe | Monthly | Recoverable via dunning. Target: <2% |
| **Subscription Conversion Rate** | % of first-time buyers who subscribe (vs one-time) | New Subscribers / New Customers | Shopify + Subscription platform | Weekly | Target: >50%. Viable to 30%. Crisis at 10%. See HYP-002 + M28 U12. |
| **LTV** | Customer Lifetime Value | Average Revenue per Customer x Average Lifespan | Calculated | Monthly | Use cohort-based LTV, not blended. See HYP-005. |
| **LTV:CAC** | Ratio of lifetime value to acquisition cost | LTV / CAC | Calculated | Monthly | Target: >3x. Kill: <1.5x. See Red Flag Dashboard. |
| **Repeat Purchase Rate** | % of customers who buy 2+ times | Customers with 2+ orders / Total Customers | Shopify | Monthly | Target: >30% |
| **Time to Second Order** | Average days between first and second purchase | Avg(Order 2 Date - Order 1 Date) | Shopify | Monthly | Shorter = healthier. Target: <45 days |
| **Cohort Retention** | % of a cohort still active at Month N | Active in Month N / Original Cohort Size | Subscription platform | Monthly | Track Month 1, 3, 6, 12 cohorts |
| **NPS** | Net Promoter Score | % Promoters (9-10) - % Detractors (0-6) | Survey tool | Monthly | Target: >50. Below 20 = product/experience problem |
| **Email Revenue %** | Revenue attributed to email channel | Email-attributed Revenue / Total Revenue | Klaviyo | Weekly | Target: >25%. Healthy D2C brands get 30-40%. |

[Confidence: B | Source: Subscription industry standards, IonWave hypothesis registry (HYP-002, HYP-003, HYP-005) | Verified: 2026-02-08]

---

## 4. Operations Metrics

| Metric | Definition | Formula | Source | Cadence | Notes |
|--------|-----------|---------|--------|---------|-------|
| **Inventory Days** | Days of inventory on hand at current sell rate | Current Inventory Units / Avg Daily Units Sold | 3PL + Shopify | Weekly | Target: 30-45 days. <7 = stockout risk (Red Flag). |
| **Ship Time** | Average days from order to delivery | Avg(Delivery Date - Order Date) | 3PL / Shipping carrier | Daily | Target: <3 days for fulfillment, <5 days total |
| **Order Accuracy** | % of orders shipped correctly | Correct Orders / Total Orders | 3PL | Weekly | Target: >99.5% |
| **Support Tickets** | Volume of customer support inquiries | Count of tickets opened | Helpdesk (Gorgias/Zendesk) | Daily | Track per 100 orders for ratio |
| **First Response Time** | Time to first reply on support ticket | Avg time from ticket creation to first agent response | Helpdesk | Daily | Target: <4 hours business hours |
| **Resolution Time** | Time to resolve support ticket | Avg time from creation to closure | Helpdesk | Weekly | Target: <24 hours |
| **CSAT** | Customer Satisfaction Score | Positive ratings / Total ratings | Helpdesk | Weekly | Target: >4.5/5 |
| **Return Rate** | % of orders returned | Returns / Total Orders | Shopify + 3PL | Monthly | Target: <3% for supplements |
| **Chargeback Rate** | % of transactions disputed | Chargebacks / Total Transactions | Stripe / Payment processor | Monthly | Kill threshold: >0.75% (Visa/MC will flag). See M20. |
| **Supplier Lead Time** | Days from PO to receipt | Avg(Receipt Date - PO Date) | Supplier tracking | Monthly | Kill: >90 days. Warning: >60 days. |

[Confidence: B-C | Source: D2C/3PL industry benchmarks, M20 support metrics, M24 fulfillment parameters | Verified: 2026-02-08]

---

## 5. Financial Health Metrics

| Metric | Definition | Formula | Source | Cadence | Notes |
|--------|-----------|---------|--------|---------|-------|
| **Cash on Hand** | Available cash balance | Bank balance + liquid investments | Bank account | Daily | The most important number pre-profitability |
| **Runway** | Days of operations remaining at current burn | Cash on Hand / Daily Burn Rate | Calculated | Weekly | Warning: <60 days. Kill: <30 days. See HYP-008. |
| **Burn Rate** | Monthly cash consumption | Monthly Expenses - Monthly Revenue | Calculated | Monthly | Track net burn (revenue-adjusted) not gross burn |
| **Gross Margin** | Revenue minus COGS as % | (Revenue - COGS) / Revenue | Calculated | Monthly | Target: >65%. Kill: <50%. See HYP-004. |
| **Contribution Margin** | Gross margin minus variable costs (shipping, payment processing, ads) | (Revenue - COGS - Variable Costs) / Revenue | Calculated | Monthly | Kill: Negative for 30 days. Must be positive for unit economics to work. |
| **COGS per Unit** | Direct cost to produce one unit | (Raw materials + Manufacturing + Packaging) / Units | Supplier invoices | Monthly | Track closely — this drives gross margin. |
| **Working Capital** | Cash available for short-term operations | Current Assets - Current Liabilities | Accounting | Monthly | Negative = danger |
| **Break-Even Point** | Units/revenue needed to cover all costs | Fixed Costs / Contribution Margin per Unit | Calculated | Quarterly | Update whenever pricing or COGS changes |

[Confidence: B | Source: Standard accounting definitions, IonWave financial model, HYP-004/HYP-008 | Verified: 2026-02-08]

---

## 6. Channel-Specific Metrics (Multi-Channel Phase)

| Metric | Definition | Formula | Source | Cadence | Notes |
|--------|-----------|---------|--------|---------|-------|
| **Amazon Revenue** | Revenue from Amazon channel | Amazon Seller Central sales | Amazon Seller Central | Daily (when live) | Track net after fees. See M28 Amazon margin waterfall. |
| **Amazon Margin** | Net margin on Amazon after all fees | (Revenue - COGS - Referral Fee - FBA Fee - PPC) / Revenue | Calculated | Weekly | Target: >20%. IonWave estimate: 26%. |
| **Amazon BSR** | Best Seller Rank in primary category | BSR number | Amazon | Daily | Lower = better. Track trends not absolute. |
| **Amazon Review Count** | Total verified reviews | Count | Amazon | Weekly | Cold start target: 50 reviews in 60 days. |
| **B2B Revenue** | Revenue from wholesale/B2B channel | B2B orders and invoices | B2B order system | Monthly | Track per-account and total. |
| **B2B Reorder Rate** | % of B2B accounts that reorder | Reordering Accounts / Total Active B2B Accounts | B2B system | Quarterly | Target: >80% with auto-reorder (M28 U3). |
| **Channel Concentration** | % of revenue from single channel | Largest Channel Revenue / Total Revenue | Calculated | Monthly | Warning: >70% from one channel for 6+ months (M28 U10). |

[Confidence: C | Source: M28 channel strategy, Amazon standard metrics | Verified: 2026-02-08]

---

## 7. Content & Creative Metrics

| Metric | Definition | Formula | Source | Cadence | Notes |
|--------|-----------|---------|--------|---------|-------|
| **Hook Rate** | % of ad viewers who watch past 3 seconds | 3-second views / Impressions | Meta Ads | Daily | Target: >30%. Below 20% = hook problem. |
| **Hold Rate** | % of ad viewers who watch to completion | ThruPlays / Impressions | Meta Ads | Daily | Target varies by length. 15s: >15%. |
| **Creative Fatigue Index** | Declining performance of a creative over time | CTR trend + CPA trend over 7 days | Calculated | Weekly | Replace creative when CTR drops >30% from peak |
| **UGC Assets in Library** | Total usable UGC content pieces | Count of approved assets | Content management | Monthly | Target: 6-10 per creator (M23 repurposing multiplier) |
| **Email Open Rate** | % of emails opened | Opens / Delivered | Klaviyo | Per send | Benchmark: 30-40% for flows, 20-30% for campaigns |
| **Email Click Rate** | % of email recipients who click | Clicks / Delivered | Klaviyo | Per send | Benchmark: 2-5% |

[Confidence: B-C | Source: Meta Ads definitions, Klaviyo standards, M23 creative metrics, M17 email benchmarks | Verified: 2026-02-08]

---

## 8. Hypothesis Monitoring Metrics

These metrics directly test IonWave's core business hypotheses:

| Hypothesis | Primary Metric | Kill Threshold | Warning | Target | Validation Method |
|-----------|---------------|----------------|---------|--------|-------------------|
| **HYP-001** CAC | Blended CAC | >$60 for 14 days | >$50 | <$40 | Meta Ads + Shopify attribution |
| **HYP-002** Subscription Rate | Subscription Conversion Rate | <10% | <20% | >50% | Shopify + Subscription platform |
| **HYP-003** Churn | Monthly Churn | >15% for 2 months | >12% | <8% | Subscription platform |
| **HYP-004** Gross Margin | Gross Margin % | <50% | <60% | >65% | Accounting (COGS vs Revenue) |
| **HYP-005** LTV | Cohort LTV at Month 12 | <$64 | <$100 | >$120 | Cohort analysis |
| **HYP-006** Organic Growth | MER (blended efficiency) | <1.5x | <2x | >3x | Total Revenue / Total Marketing |
| **HYP-007** Timeline | MRR vs Month | <50% of plan at Month 6 | <75% of plan | On track | MRR trend |
| **HYP-008** Capital | Cash Runway | <30 days | <60 days | >90 days | Bank balance / Burn rate |

[Confidence: B | Source: IonWave hypothesis registry, financial model, kill criteria from M0 Thesis | Verified: 2026-02-08]

---

## 9. Metric Naming Conventions

| Rule | Example | Why |
|------|---------|-----|
| Use standard abbreviations | CAC not "customer acquisition cost" in dashboards | Consistency |
| Always specify time period | "Monthly Churn" not just "Churn" | Ambiguity prevention |
| Distinguish current vs target | "CAC (Current)" vs "CAC (Target)" | Clarity |
| Note data source | "ROAS (Meta-reported)" vs "ROAS (post-purchase survey)" | Source matters — platform ROAS overstates |
| Prefix channel when multi-channel | "Amazon Revenue" vs "D2C Revenue" | Prevent aggregation confusion |

---

## 10. Intelligence Gaps

| Gap | Impact | Upgrade Path | Priority |
|-----|--------|-------------|----------|
| G1: No actual data yet (pre-launch) | All metrics are targets, not actuals | Fill as IonWave launches. First real data at Month 1. | HIGH (but time-gated) |
| G2: Attribution methodology not finalized | CAC accuracy depends on methodology | Implement post-purchase survey + UTM + unique codes (M28 U2) at launch | HIGH |
| G3: Cohort LTV requires 6+ months of data | Can't validate HYP-005 until Month 6+ | Use proxy cohorts from industry benchmarks until real data | MEDIUM |
| G4: B2B and Amazon metrics are theoretical | Channel not yet live | Add to tracking when channels launch (Phase 2+) | LOW (future) |


---

### 📄 data_governance.md

# M30 Data Governance
**TUP**: M30 Analytics & Dashboards
**Source Tabs**: 634 (Data Freshness Requirements), 635 (Screenshot Evidence Log)
**Version**: 1.0.0
**Quality**: 7.0/10
**Status**: Workshop Draft
**Confidence Baseline**: B-C (cadence recommendations based on D2C operational requirements)

---

## Purpose
Define data quality standards: how fresh data must be, how evidence is captured, and how data quality is maintained. Without governance, dashboards rot — numbers get stale, definitions drift, and decisions get made on bad data.

---

## 1. Data Freshness Requirements

Every piece of data in the IonWave model has a required update cadence. Stale data is worse than no data — it creates false confidence.

### Tier 1: Real-Time (Update as Events Happen)

| Data Type | Source | Why Real-Time | Owner |
|-----------|--------|--------------|-------|
| Decision Log | Manual | Decisions lose context if not logged immediately | Founder |
| Risk Register (new risks) | Manual | New risks need immediate visibility | Founder |
| Ad account status changes | Meta Ads | Account restrictions require immediate response | Founder |
| Stockout alerts | 3PL | Can't sell what you don't have | Ops |

**Implementation**: These are event-driven, not scheduled. Set up notifications from source systems (email alerts from Meta, low-stock alerts from 3PL).

### Tier 2: Daily

| Data Type | Source | Implementation | Est. Time |
|-----------|--------|---------------|-----------|
| Revenue & Orders | Shopify | Shopify daily email summary + manual check | 2 min |
| Ad Spend & ROAS | Meta Ads Manager | Meta daily email + manual check | 2 min |
| Cash Balance | Bank account | Mobile banking app | 1 min |
| Support Tickets (new) | Helpdesk | Helpdesk dashboard | 3 min |
| Inventory status (during low stock) | 3PL | 3PL portal | 2 min |

**Total daily commitment**: ~10 minutes

### Tier 3: Weekly

| Data Type | Source | Implementation | Est. Time |
|-----------|--------|---------------|-----------|
| CAC (blended) | Calculated | Ad spend / new customers for the week | 5 min |
| CVR (site) | Shopify + GA4 | Orders / sessions | 3 min |
| Subscription conversion rate | Subscription platform | New subs / new customers | 3 min |
| MER | Calculated | Total revenue / total marketing spend | 3 min |
| Email performance | Klaviyo | Open rates, click rates, email revenue | 10 min |
| Inventory days | 3PL + Shopify | Current stock / avg daily sales | 5 min |
| Creative performance | Meta Ads | CTR, hook rate, hold rate by creative | 10 min |
| Competitor monitoring | Manual / SEMrush | Price checks, new product launches, ad activity | 15 min |

**Total weekly commitment**: ~60 minutes (one Monday session)

### Tier 4: Monthly

| Data Type | Source | Implementation | Est. Time |
|-----------|--------|---------------|-----------|
| Full P&L | Accounting (QBO/Xero) | Revenue, COGS, gross margin, opex, net | 1 hr |
| Cohort retention analysis | Subscription platform | Month-N retention for each cohort | 30 min |
| Unit economics validation | Calculated | COGS, contribution margin, LTV actuals vs projections | 30 min |
| Cash flow forecast (13-week) | Spreadsheet (M25) | Update with actuals, re-project | 30 min |
| Churn analysis | Subscription platform | Rate, reasons, voluntary vs involuntary | 20 min |
| NPS / CSAT | Survey tool | Net Promoter Score, satisfaction trends | 15 min |
| Red Flag Dashboard scan | M30 | Check all 12 kill criteria against current data | 15 min |
| Cross-TUP validation spot check | M30 | Check 3-5 validation rules | 15 min |
| Hypothesis status review | Hypothesis registry | Any grades to update? Any near validation? | 15 min |

**Total monthly commitment**: ~4 hours (one afternoon)

### Tier 5: Quarterly

| Data Type | Source | Implementation | Est. Time |
|-----------|--------|---------------|-----------|
| Competitive landscape refresh | M26, web research | Has anything changed? New competitors? | 2 hrs |
| ICP validation | M27, customer data | Are we selling to who we expected? | 1 hr |
| Pricing review | M10, market data | Should price/offer change? | 1 hr |
| Channel mix review | M28, analytics | Rebalance channel allocation? | 1 hr |
| Full cross-TUP validation | M30 | All 10 rules checked | 1 hr |
| Hypothesis formal review | Hypothesis registry | Upgrade/downgrade confidence grades | 1 hr |

**Total quarterly commitment**: ~7 hours (one full day per quarter)

### Tier 6: Static (Update Only When Fundamentals Change)

| Data Type | Trigger for Update |
|-----------|-------------------|
| Core metric definitions (Data Dictionary) | When a metric formula changes |
| Kill criteria thresholds | When hypothesis is validated or invalidated |
| Business model parameters (price, COGS structure) | When pricing or supplier changes |
| ICP definition | After quarterly review if significant shift |
| Dashboard architecture | When new channels or tools are added |

[Confidence: B | Source: D2C operational cadence best practices, IonWave capacity constraints (solo founder), M25 financial ops rhythm | Verified: 2026-02-08]

---

## 2. Data Quality Standards

### The 5 Data Quality Rules

| Rule | Definition | Example Violation | Fix |
|------|-----------|-------------------|-----|
| **Accurate** | Number reflects reality | ROAS says 5x but real ROAS is 2.5x (platform over-attribution) | Use MER as primary, ROAS as secondary |
| **Complete** | No missing data points | Revenue tracked but COGS not updated → can't calculate margin | Block: no revenue reporting without COGS |
| **Consistent** | Same metric = same definition everywhere | "Churn" means cancellation in one tab, non-renewal in another | Single definition in Data Dictionary |
| **Timely** | Data arrives within its freshness window | Monthly P&L not done until 3 weeks into next month | Set calendar reminder, block 1st-week time |
| **Relevant** | Only track what drives decisions | Tracking 50 metrics when only 10 matter at current stage | Phase-gate metrics. Phase 1 = 15 metrics max. |

### Metric Staleness Indicators

| Staleness Level | Definition | Action |
|-----------------|-----------|--------|
| **Fresh** | Updated within its cadence window | No action needed |
| **Aging** | 1-2x overdue from cadence | Update priority — add to this week's task list |
| **Stale** | >2x overdue | Metric is unreliable. Mark as STALE in dashboard. Do not use for decisions until refreshed. |
| **Dead** | >4x overdue or source broken | Remove from dashboard. Either fix source or deprecate metric. |

**Example**: Weekly metric (CAC) not updated for 3 weeks = STALE. Must be refreshed before any ad spend decisions.

---

## 3. Evidence & Documentation Protocol

### Screenshot Evidence Log

Every significant milestone needs proof-of-work documentation. This builds the audit trail for investors, advisors, and future team members.

| Category | What to Capture | When | Where to Store |
|----------|----------------|------|---------------|
| **Ad launches** | Ads Manager showing campaign live | At launch | Google Drive → Evidence → Ads |
| **Email flows** | Flow builder showing active flow + test send | At activation | Google Drive → Evidence → Email |
| **Tracking verification** | Pixel/conversion events firing correctly | At setup + monthly | Google Drive → Evidence → Tracking |
| **Milestone achievements** | Dashboard showing metric achieved (e.g., first 100 orders) | When achieved | Google Drive → Evidence → Milestones |
| **Kill criteria triggered** | Dashboard showing metric in RED zone | When triggered | Google Drive → Evidence → Red Flags |
| **A/B test results** | Platform showing test results with statistical significance | At test completion | Google Drive → Evidence → Tests |
| **Financial milestones** | Bank/Stripe showing revenue thresholds | When crossed | Google Drive → Evidence → Financial |

### Evidence Log Template

| Date | Category | Description | Screenshot Link | Verified By | Notes |
|------|----------|-------------|-----------------|-------------|-------|
| [Date] | Ad Launch | Hook Test Ad #1 live in Meta Ads Manager | [Drive link] | [Name] | First paid ad launched |
| [Date] | Email Flow | Welcome flow triggered on test order | [Drive link] | [Name] | 5-email sequence active |
| [Date] | Tracking | Pixel firing on purchase event | [Drive link] | [Name] | Server-side + browser pixel confirmed |

### Evidence Quality Requirements

1. **Screenshots must include timestamps** — browser clock or platform timestamp visible
2. **Metric screenshots must show context** — not just a number, show the dashboard/report it came from
3. **Comparative screenshots** — for improvements, show before and after
4. **No editing** — screenshots must be unmodified. Use highlighting/annotations only.
5. **Naming convention**: `YYYY-MM-DD_Category_Description.png` (e.g., `2026-03-15_Ad_Hook-Test-1-Launch.png`)

---

## 4. Data Source Hierarchy

When two data sources disagree, which one wins?

| Rank | Source Type | Example | Trust Level | Known Limitations (Dialogue Upgrade U7) |
|------|-----------|---------|-------------|----------------------------------------|
| 1 | **Bank account / Stripe** | Actual cash received | Ground truth | Timing delays (pending transactions), refunds may not show same day |
| 2 | **Shopify orders** | Order count, revenue | Primary — source of truth for revenue | Doesn't account for returns until processed. Subscription revenue may lag. |
| 3 | **Subscription platform** | Subscription status, churn | Primary — source of truth for subscriptions | Paused vs cancelled distinction varies by platform. Define clearly. |
| 4 | **3PL system** | Inventory levels, shipments | Primary — source of truth for operations | Data may lag 24-48 hrs. Cycle count discrepancies common (2-5%). |
| 5 | **Post-purchase survey** | Attribution ("how did you hear about us?") | Strong signal — direct customer report | Response bias (customers forget, attribute to last touchpoint). 30-50% response rate typical. |
| 6 | **GA4 / server-side tracking** | Sessions, conversions, attribution | Good for funnel behavior | Under-reports by 10-25% due to ad blockers, consent mode, cross-device gaps. Not reliable for absolute conversion counts. |
| 7 | **Meta Ads Manager** | ROAS, conversions, attribution | Platform context only (U2) | Over-reports by 20-40% post-iOS 14.5. Use ONLY for comparing creatives/campaigns within Meta. Never for business decisions. |
| 8 | **Third-party tools** (Triple Whale, etc.) | Blended metrics, modeled attribution | Good for trends, not ground truth | Models vary. Different tools give different numbers. Compare to Stripe/Shopify actuals quarterly. |

**Rule**: When Stripe says you made $10K and Meta says you made $15K from ads, believe Stripe. Meta is inflating.

[Confidence: B | Source: iOS 14.5 attribution research, D2C analytics community consensus, Meta's own reporting caveats | Verified: 2026-02-08]

---

## 5. Data Governance Calendar

A unified calendar of all data activities:

| Timeframe | Activity | Time Required | Owner |
|-----------|---------|---------------|-------|
| **Every morning** | Daily Pulse check (revenue, spend, cash, fires) | 10 min | Founder |
| **Every Monday** | Weekly report compilation + metric refresh | 1 hr | Founder |
| **1st of each month** | Monthly Business Review preparation | 4 hrs | Founder |
| **1st of each month** | Cross-TUP validation spot check (3-5 rules) | 15 min | Founder |
| **1st of each month** | Red Flag Dashboard full scan | 15 min | Founder |
| **End of Q** | Quarterly Deep Review | Half-day | Founder + Advisors |
| **End of Q** | Full cross-TUP validation audit | 1 hr | Founder |
| **End of Q** | Hypothesis confidence grade review | 1 hr | Founder |
| **Ad hoc** | Metric definition updates (Data Dictionary) | 15 min | Whoever changes it |
| **Ad hoc** | Evidence logging (screenshots, milestones) | 5 min per event | Whoever achieves it |

### Graceful Degradation — When You Can't Do Everything (Dialogue Upgrade U11)

Founders will skip weeks. Life happens. The system needs to degrade gracefully, not collapse.

| If You Can Only Do... | Do This | Skip This |
|----------------------|---------|-----------|
| **1 thing** | Daily Pulse (5 min — revenue, cash, fires) | Everything else |
| **2 things** | Daily Pulse + Weekly MVD refresh (CAC, Sub Rate, MER) | Monthly MBR, evidence logging |
| **3 things** | Daily + Weekly + Monthly simplified MBR (4 questions, 1 hr) | Quarterly review, cross-TUP validation |
| **Everything** | Full governance calendar as documented | — |

**Minimum Viable Governance**: The Daily Pulse is NON-NEGOTIABLE. If you're not checking revenue, cash, and fires every morning, you're flying blind. Everything else can be recovered from. Missing the Daily Pulse for a week means you could miss a cash crisis.

**Recovery Protocol**: If you've skipped 2+ weeks of weekly reporting:
1. Don't try to backfill — just do THIS week's numbers
2. Compare to the last week you did track (even if it was 3 weeks ago)
3. Note the gap in your evidence log
4. Resume normal cadence

**Total ongoing time commitment**:
- Daily: 10 min (NON-NEGOTIABLE)
- Weekly: 1 hr (included in above)
- Monthly: ~5 hrs
- Quarterly: ~8 hrs

[Confidence: C | Source: Estimated time commitments — will need calibration with real experience | Verified: 2026-02-08]

---

## 6. IonWave-Specific Data Quality Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Meta over-attribution** | HIGH | Overestimates ROAS → overspend on ads | Always cross-check with MER. Post-purchase survey for true attribution. |
| **Subscription churn miscounting** | MEDIUM | Under/overcount if pauses vs cancellations mixed | Define precisely: churn = cancelled. Paused = separate metric. |
| **Cohort LTV calculation drift** | MEDIUM | Early cohorts may not represent steady-state behavior | Don't extrapolate LTV from <3 months of data. Use monthly cohort snapshots. |
| **Cash runway over-optimism** | HIGH | Projecting revenue growth into runway extends it artificially | Calculate runway on CURRENT burn rate only, not projected improvement. |
| **Vanity metrics distraction** | MEDIUM | Tracking followers/pageviews instead of revenue/LTV | Phase-gate metrics. Vanity metrics only enter at Phase 3+. |
| **Inventory data lag** | MEDIUM | 3PL data delayed → stockout surprise | Set reorder point at 2x lead time, not 1x. Buffer for data lag. |

---

## 7. Intelligence Gaps

| Gap | Impact | Upgrade Path | Priority |
|-----|--------|-------------|----------|
| G1: Evidence logging process untested | May be too heavy or too light for solo founder | Test at launch, simplify if needed. Minimum: milestone screenshots only. | MEDIUM |
| G2: Data governance calendar is aspirational | Solo founder may not sustain all cadences | Start with daily + weekly only. Add monthly at Month 2. Quarterly at Month 3. | HIGH |
| G3: No data backup/archival strategy | Data loss risk if tool accounts closed | Monthly export of key data to Google Drive. Don't rely solely on SaaS tools. | MEDIUM |
| G4: Freshness requirements reference many TUPs not yet workshopped | Some source systems don't exist yet | Update freshness requirements as TUPs are activated | LOW |


---

### 📄 dialogue_summary.md

# M30 Persona Dialogue Summary
**TUP**: M30 Analytics & Dashboards
**Dialogue ID**: M30-DLG-2026-02-08
**Rounds**: 6
**Personas**: 3
**Upgrades**: 13
**Unresolved**: 0
**Saturation**: Round 6 (all 3 personas RESOLVED)

---

## Personas

| Persona | Expertise | Key Bias | Role |
|---------|-----------|----------|------|
| **Data-Obsessed D2C Operator** | Ran analytics for $50M DTC brand | Minimalist — hates metric overload, wants only what drives decisions | Challenge complexity |
| **Growth Engineer / Technical Analyst** | Builds attribution models and dashboards post-iOS 14.5 | Technical accuracy — knows exactly how platforms lie | Challenge data quality |
| **Skeptical Investor** | Reviews startup metrics for a living | Pattern recognition — spots vanity metrics and hidden problems | Challenge reporting honesty |

---

## Round-by-Round Summary

### Round 1
- **D2C Operator**: 50+ metrics is too many for solo founder. Need 5 numbers.
- **Growth Engineer**: ROAS cadence inconsistent with CAC. MER should be primary, ROAS demoted.
- **Investor**: 12 kill criteria is too many. Want hierarchy — which 3 are truly existential?

### Round 2
- **D2C Operator**: Phase 1 needs literal MVD — 7 rows in a Google Sheet.
- **Growth Engineer**: Attribution model too simplistic. Distinguish awareness attribution (survey) vs conversion attribution (UTM). Disagreement = multi-touch, not error.
- **Investor**: MBR too heavy. Months 1-3 need 4 questions, 1 hour max.

### Round 3
- **D2C Operator**: MVD needs a TEMPLATE with formulas and conditional formatting. OpKit deliverable.
- **Growth Engineer**: Data source hierarchy missing known limitations. GA4 under-reports by 10-25%.
- **Investor**: V6 (kill criteria consistency) should be elevated to Rule Zero, checked first every month.

### Round 4
- **D2C Operator**: Email Revenue % meaningless before 1K subscribers / 60 days. Phase-gate it.
- **Growth Engineer**: Subscription conversion drop needs diagnostic decision tree, not just red/yellow/green.
- **Investor**: Existential = Cash Runway + CAC + Contribution Margin. Rest = monitoring.

### Round 5
- **D2C Operator**: System needs graceful degradation. Minimum viable governance = daily pulse only.
- **Growth Engineer**: Vanity metrics explicitly banned from Phase 1 (followers, pageviews, engagement rate).
- **Investor**: Monthly hypothesis prompt — one sentence per critical hypothesis.

### Round 6
- **D2C Operator**: RESOLVED. MVD, phase-gating, graceful degradation address all concerns.
- **Growth Engineer**: RESOLVED. Attribution framework, data source limitations cover technical concerns.
- **Investor**: RESOLVED. Existential/monitoring distinction, simplified MBR, hypothesis prompt.

---

## Upgrade Registry

| ID | Upgrade | Applied To | Round |
|----|---------|-----------|-------|
| U1 | Minimum Viable Dashboard (MVD) — 7 metrics for Phase 1 | dashboards_and_reporting.md | R1-2 |
| U2 | MER primary efficiency metric, ROAS demoted | data_dictionary.md | R1 |
| U3 | Existential vs Monitoring kill criteria classification | red_flags_and_validation.md | R1, R4 |
| U4 | Awareness vs Conversion attribution model | data_dictionary.md | R2 |
| U5 | Simplified early-stage MBR (4 questions, 1 hr, Months 1-3) | dashboards_and_reporting.md | R2 |
| U6 | Google Sheets MVD Template (OpKit deliverable) | opkit_analytics_measurement.md | R3 |
| U7 | Data source known limitations column | data_governance.md | R3 |
| U8 | V0 Master Consistency Check (elevated from V6) | red_flags_and_validation.md | R3 |
| U9 | Email Revenue % phase-gated to Month 3+ | dashboards_and_reporting.md | R4 |
| U10 | Subscription conversion diagnostic decision tree | red_flags_and_validation.md | R4 |
| U11 | Graceful degradation — minimum viable governance | data_governance.md | R5 |
| U12 | Vanity metrics ban list for Phase 1 | dashboards_and_reporting.md | R5 |
| U13 | Monthly hypothesis prompt (one sentence per critical HYP) | dashboards_and_reporting.md | R5 |

---

## Key Insights by Persona

**D2C Operator**: The biggest risk isn't missing data — it's drowning in data. A solo founder who checks 7 numbers daily will outperform one who has 50 metrics and checks none. MVD-first, expand later.

**Growth Engineer**: Post-iOS 14.5, every data source lies in a different direction. The solution isn't finding the "right" source — it's understanding HOW each source is wrong (known limitations) and choosing the right source for each decision type (awareness vs conversion attribution).

**Investor**: The most dangerous red flags aren't the most numerous — they're the most existential. Separating "this will kill us tomorrow" (cash, CAC, contribution margin) from "this will hurt us next quarter" (churn, LTV:CAC, stockout) prevents panic-driven decisions and ensures the truly fatal metrics get immediate attention.


---

### 📄 opkit_analytics_measurement.md

# OpKit OK-M30-001: Analytics & Measurement Kit
**Version**: 1.0.0
**Created**: 2026-02-08
**Source TUP**: M30 Analytics & Dashboards
**Quality Grade**: 8.2/10
**Reusability**: HIGH — any D2C brand, any stage

---

## What This Kit Does
Builds a complete measurement system for a D2C brand from zero. Includes metric definitions, dashboard architecture, red flag monitoring, and data governance — all phase-gated so you only track what matters at your current stage.

---

## Instructions (14 Steps)

### Step 1: Define Your Growth Phases
Map your revenue milestones to 4 phases:
- Phase 0: Pre-launch ($0)
- Phase 1: Launch → [X] MRR
- Phase 2: [X] → [Y] MRR
- Phase 3: [Y]+ MRR

*IonWave used: Phase 1 = $0-10K MRR, Phase 2 = $10-50K, Phase 3 = $50K+*

### Step 2: Build Your Minimum Viable Dashboard (MVD)
Select 5-7 metrics that are the ONLY ones you'll track in Phase 1. Template:

| # | Metric | Target | Source | Cadence |
|---|--------|--------|--------|---------|
| 1 | Revenue (net) | Growing MoM | [e-commerce platform] | Daily |
| 2 | Orders | Growing MoM | [e-commerce platform] | Daily |
| 3 | Ad Spend | Within budget | [ads platform] | Daily |
| 4 | CAC (blended) | <$[X] | Calculated | Weekly |
| 5 | [Key conversion metric] | >[X]% | [platform] | Weekly |
| 6 | Cash Balance | >[X] days runway | Bank | Daily |
| 7 | MER | >[X]x | Calculated | Weekly |

**Rule**: If it's not in this table, don't track it in Phase 1.

### Step 3: Create a Google Sheets MVD Dashboard (Dialogue Upgrade U6)
Build a single Google Sheet with:
- **Row per metric** (7 rows)
- **Columns**: Metric | Today | Yesterday | Change | WTD | MTD | Target | Status
- **Conditional formatting**: Green (above target), Yellow (warning), Red (below kill)
- **Formulas**: Auto-calculate Change %, auto-color Status
- **One tab only** — resist the urge to add tabs

### Step 4: Define Your Existential Kill Criteria
Identify the 3 metrics that would kill the business immediately (not slowly):

| Metric | Kill Threshold | Why Existential |
|--------|---------------|-----------------|
| [Metric 1] | [threshold] | [Why this kills you immediately] |
| [Metric 2] | [threshold] | [Why] |
| [Metric 3] | [threshold] | [Why] |

Everything else is "monitoring" — serious but not immediately fatal.

### Step 5: Build Your Data Dictionary
For EVERY metric in your MVD + kill criteria, define:
- Precise formula
- Data source
- Update cadence
- Known limitations of that source

**Rule**: Two people looking at the same metric must get the same number. If they don't, your definitions aren't precise enough.

### Step 6: Set Up Your Daily Pulse Routine
Design a 5-minute morning check-in:
- What 4 numbers do you look at?
- Where do you find them? (apps, dashboards)
- What does "RED" look like for each?
- What's your one-line Slack format for team updates?

### Step 7: Design Your Reporting Cadence
Map cadences to your capacity:

| Cadence | Time Budget | What's Included |
|---------|------------|-----------------|
| Daily | [X] min | [2-4 items] |
| Weekly | [X] min | [3-5 items] |
| Monthly | [X] hrs | [Simplified MBR] |

### Step 8: Build Your Simplified MBR (Months 1-3)
Design a 1-hour MBR answering exactly 4 questions:
1. Are we acquiring customers at viable economics?
2. Are they staying?
3. How much cash do we have?
4. What are we doing differently next month?

Plus the hypothesis prompt: one sentence per critical hypothesis.

### Step 9: Define Your Attribution Model
Choose your approach:
- **Awareness attribution**: How they found you (survey-based)
- **Conversion attribution**: What drove the purchase (UTM/last-click)
- **Reconciliation rule**: When they disagree, how do you weigh them?

### Step 10: Build Your Data Source Hierarchy
Rank your data sources by trust level. For each, document known limitations.

### Step 11: Set Up Red Flag Monitoring
Create a simple table with your existential + monitoring metrics, current values, and status indicators. Check existential metrics daily, monitoring metrics weekly.

### Step 12: Define Cross-Document Validation Rules
List 5-10 consistency checks: "If document X says [value], document Y must match."
V0 (Master Consistency): Kill criteria source of truth matches monitoring thresholds.

### Step 13: Establish Graceful Degradation Policy
Define what to do when you can't follow the full process:
- Minimum viable: [1 thing that's non-negotiable]
- Recovery protocol: How to get back on track after skipping

### Step 14: Plan Your Tool Progression
Map when to upgrade from basic tools (Sheets) to specialized tools:
- What revenue threshold triggers an upgrade?
- What tool category to add?
- What's the cost/setup time?

---

## Grading Rubric

| Grade | Criteria |
|-------|---------|
| **A (9-10)** | MVD operational with real data. Kill criteria monitored with automated alerts. Attribution model validated with 3+ months data. Full MBR cadence running. |
| **B (7-8)** | MVD built with clear metrics. Kill criteria defined with thresholds. Attribution planned. Reporting cadence documented. Phase-gating clear. |
| **C (5-6)** | Metrics defined but not phase-gated. Some kill criteria. Basic reporting. No attribution model. |
| **D (3-4)** | Generic metric list without specificity. No kill criteria. No reporting cadence. |
| **F (<3)** | No measurement system defined. "We'll figure it out later." |

---

## Scaffold (4 files to copy/customize)

1. `data_dictionary.md` — Complete metric definitions with formulas, sources, cadences, limitations
2. `dashboards_and_reporting.md` — MVD, daily pulse, weekly report, MBR templates, tool progression
3. `red_flags_and_validation.md` — Existential/monitoring kill criteria, escalation protocol, validation rules, diagnostic trees
4. `data_governance.md` — Data freshness requirements, quality standards, evidence logging, source hierarchy, graceful degradation

---

## IonWave Graded Example

**Grade: B+ (8.2/10)**

Strengths:
- MVD clearly defined (7 metrics) with phase-gating to prevent overload
- Existential vs monitoring classification prevents panic-driven decisions
- Attribution model distinguishes awareness vs conversion attribution
- Data source hierarchy with known limitations column
- Graceful degradation policy is practical and honest
- 13 dialogue upgrades made content significantly more actionable

Weaknesses:
- Pre-launch: all metrics are targets, no actuals yet (-1)
- Diagnostic trees could be deeper for more failure modes (-0.5)
- Google Sheets MVD template exists as concept but not as actual downloadable file (-0.3)

---

## Adaptation Guide

### For Supplement Brands (Similar to IonWave)
- Use the 7-metric MVD as-is
- Subscription conversion is your #1 retention metric
- Add supplement-specific: refund rate (product quality signal), review velocity

### For Non-Subscription D2C
- Replace Subscription Rate with Repeat Purchase Rate in MVD
- Adjust churn metric to "90-day repurchase rate"
- Email Revenue % becomes more important (primary retention mechanism)

### For B2B-First Brands
- Replace CAC with Customer Payback Period
- Replace Subscription Rate with Net Revenue Retention (NRR)
- Monthly churn → Annual churn
- Add: pipeline velocity, deal cycle length, expansion revenue

### For Marketplace-Only Brands (Amazon-first)
- Replace MER with TACoS (Total Advertising Cost of Sales)
- Add BSR (Best Seller Rank) to MVD
- Replace Cash Runway with Inventory Coverage Days
- Attribution is simpler (Amazon search → purchase) but organic rank matters

---

## Universal Principles (from M30 workshop)

1. **Track less, know more** — 7 metrics done daily beats 50 metrics done never
2. **MER over ROAS** — blended efficiency is always more honest than platform-reported ROAS
3. **Existential ≠ Monitoring** — separate sudden death (cash, CAC, contribution margin) from slow bleeds (churn, LTV:CAC)
4. **Attribution is two questions, not one** — awareness (how they found you) and conversion (what drove the purchase) are different answers
5. **Phase-gate everything** — don't build a Series B analytics stack for a pre-launch startup
6. **Graceful degradation** — design for reality (founders skip weeks), not perfection
7. **Your kill criteria ARE your strategy** — if the monitoring thresholds don't match the source of truth, you're flying blind


---

### 📄 red_flags_and_validation.md

# M30 Red Flags & Validation
**TUP**: M30 Analytics & Dashboards
**Source Tabs**: 632 (Red Flag Dashboard), 633 (Cross-Tab Validation Rules)
**Version**: 1.0.0
**Quality**: 8.0/10
**Status**: Workshop Draft
**Confidence Baseline**: B (kill criteria validated against hypothesis registry and financial model)

---

## Purpose
Two complementary systems:
1. **Red Flag Dashboard** — Monitor kill criteria in real-time. Catch existential threats before they become fatal.
2. **Cross-TUP Validation** — Ensure internal consistency. When one document says X, all related documents must agree.

Together they answer: "Are we dying?" and "Are we lying to ourselves?"

---

## 1. Red Flag Dashboard — Kill Criteria Monitor

### Existential vs Monitoring Classification (Dialogue Upgrade U3)

Not all red flags are equal. Three metrics can kill the business immediately. The rest are slow bleeds.

**EXISTENTIAL (sudden death — these 3 can end the company):**

| # | Metric | Kill Threshold | Warning Threshold | Source | Response Time | Why Existential |
|---|--------|---------------|-------------------|--------|--------------|-----------------|
| RF-1 | **CAC** | >$60 for 14 days | >$50 | HYP-001 | 48 hrs | Can't profitably acquire customers = no business |
| RF-5 | **Cash Runway** | <30 days | <60 days | HYP-008, M25 | Immediate | No cash = can't operate, period |
| RF-6 | **Contribution Margin** | Negative for 30 days | <5% | HYP-004, M25 | 2 weeks | Every sale loses money = faster you grow, faster you die |

**MONITORING (slow bleed — serious but not immediately fatal):**

| # | Metric | Kill Threshold | Warning Threshold | Source | Response Time | Escalation |
|---|--------|---------------|-------------------|--------|--------------|------------|
| RF-2 | **LTV:CAC Ratio** | <1.5x | <2x | HYP-005/001 | 1 week | Re-examine pricing, retention, or CAC |
| RF-3 | **Monthly Churn** | >15% for 2 months | >12% | HYP-003 | 2 weeks | Customer research, product/offer audit |
| RF-4 | **Gross Margin** | <50% | <60% | HYP-004 | 1 month | Renegotiate COGS, review pricing |
| RF-7 | **Supplier Lead Time** | >90 days | >60 days | M24 | 1 month | Activate backup supplier, adjust reorder point |
| RF-8 | **Ad Account Status** | Banned | Restricted | M11-M15 | Immediate | Backup account, appeal, diversify channels |
| RF-9 | **Stockout Risk** | <7 days inventory | <14 days | M24 | 1 week | Emergency reorder, manage demand |
| RF-10 | **Chargeback Rate** | >0.75% | >0.5% | M20 | 2 weeks | Fraud review, fulfillment audit, refund policy |
| RF-11 | **Subscription Conversion** | <10% for 60 days | <20% | HYP-002, M28 | 2 weeks | See diagnostic tree below (U10) |
| RF-12 | **MRR Growth** | Negative 3 months | Flat 2 months | HYP-007 | 1 month | Full strategy review, potential pivot |

[Confidence: B | Source: M0 Thesis kill criteria, IonWave financial model, hypothesis registry, M25 Survival Five | Verified: 2026-02-08]

---

## 2. Escalation Protocol

### Severity Levels

| Level | Condition | Who Acts | Response | Timeline |
|-------|-----------|----------|----------|----------|
| **GREEN** | All metrics above warning thresholds | Founder (routine monitoring) | Continue normal operations | Ongoing |
| **YELLOW** | 1+ metric in warning zone | Founder | Increase monitoring frequency to daily for affected metrics. Identify root cause. Develop action plan. | Action plan within 48 hrs |
| **RED (Single)** | 1 metric at or past kill threshold | Founder + Advisor | Daily updates on affected metric. Written action plan with 7-day milestones. | Action plan within 48 hrs, review at 7 days |
| **RED (Multiple)** | 2+ metrics at kill threshold simultaneously | Founder + Advisor + Co-founders | Emergency review. Consider pausing growth spend. All-hands on recovery. | Emergency call within 24 hrs |
| **RED (Sustained)** | Any kill metric RED for 30 days despite intervention | Full stakeholder group | Kill trade decision required. Formal review of pivot vs wind-down. | Decision within 7 days |

### Decision Tree

```
Metric hits WARNING →
  ├── Root cause identified within 48 hrs?
  │   ├── YES → Implement fix → Monitor for 7 days
  │   │         ├── Improving → Return to GREEN
  │   │         └── Not improving → Escalate to RED
  │   └── NO → Escalate to RED
  │
Metric hits KILL THRESHOLD →
  ├── Is this a data quality issue? (wrong formula, tracking error)
  │   ├── YES → Fix data, re-evaluate
  │   └── NO → Genuine business problem
  │         ├── 1 metric RED → Single RED protocol
  │         └── 2+ metrics RED → Multiple RED protocol
  │
RED for 30 days →
  └── Kill Trade Decision
      ├── Can we pivot to fix? (new channel, new offer, new ICP)
      │   ├── YES → Define pivot, reset timelines
      │   └── NO → Wind down gracefully
```

### Kill Trade Decision Framework

When a kill decision is triggered:

1. **Data check**: Is the data reliable? Could there be measurement errors?
2. **Root cause**: Why is the metric failing? Is it fixable or structural?
3. **Dependency check**: Is this metric failing because an upstream metric failed? (e.g., LTV:CAC <1.5x because churn >15%)
4. **Effort/probability**: What would it take to fix? What's the probability of success?
5. **Runway**: How much time/money do we have left to attempt a fix?
6. **Decision**: Continue (with specific fix plan) | Pivot (different ICP/channel/product) | Wind down

### Subscription Conversion Diagnostic Tree (Dialogue Upgrade U10)

When RF-11 (Subscription Conversion <20%) triggers, don't just "audit the offer." Diagnose WHY:

```
Subscription Conversion Dropping →
  ├── Do customers SEE the subscription option?
  │   ├── NO → Offer Visibility Problem
  │   │       Fix: Move subscription above the fold, test default-to-subscribe
  │   └── YES → They see it but don't choose it
  │         ├── Is subscription price compelling vs one-time?
  │         │   ├── Discount <15% → Pricing Problem
  │         │   │       Fix: Test 20% discount, free shipping, bonus item
  │         │   └── Discount ≥15% → Price is fine, it's something else
  │         │         ├── Do customers trust they'll want it again?
  │         │         │   ├── NO → Product Confidence Problem
  │         │         │   │       Fix: "Try once, subscribe later" flow,
  │         │         │   │       satisfaction guarantee, first-order review
  │         │         │   └── YES → Trust issue with subscriptions
  │         │         │         ├── Can they cancel easily?
  │         │         │         │   ├── Unclear → Friction Problem
  │         │         │         │   │       Fix: "Cancel anytime" messaging,
  │         │         │         │   │       show cancellation in 1 click
  │         │         │         │   └── Clear → Unknown barrier
  │         │         │         │       Action: Customer interviews needed
```

**Key Insight**: Most subscription conversion drops are visibility or pricing problems, not product problems. Check the simple things first.

[Confidence: B | Source: M0 Thesis kill criteria framework, Y Combinator shutdown guidance, IonWave financial model, M28 subscription sensitivity (U12) | Verified: 2026-02-08]

---

## 3. Cross-TUP Validation Rules

### The Principle
The model is only useful if it's internally consistent. When Unit Economics says COGS = $16.50, every other TUP that references COGS must use the same number. These rules catch contradictions before they cause bad decisions.

### Validation Rules

**RULE ZERO — Master Consistency Check (Dialogue Upgrade U8)**
Check this FIRST, EVERY month, before any other validation:

| Rule ID | If This TUP Says... | Then This TUP Must Match... | Check Frequency | Priority |
|---------|---------------------|----------------------------|-----------------|----------|
| **V0** | M0 (Thesis): Kill criteria thresholds | M30 (Red Flag Dashboard): EXACT same thresholds | **Monthly (FIRST check)** | **CRITICAL — MASTER** |

If V0 fails, ALL monitoring is unreliable. Fix immediately.

**Standard Validation Rules:**

| Rule ID | If This TUP Says... | Then This TUP Must Match... | Check Frequency | Priority |
|---------|---------------------|----------------------------|-----------------|----------|
| **V1** | M25 (Financial Ops): COGS = $X | M28 (Amazon margin), M28 (B2B pricing), M28 (retail economics): Same COGS | Monthly | CRITICAL |
| **V2** | M0 (Thesis): CAC target = $X | M28 (channel strategy), M14 (testing): Same CAC target | Monthly | CRITICAL |
| **V3** | M10 (Pricing): Price = $X | All revenue projections (M25, M28): Same price | Monthly | CRITICAL |
| **V4** | M24 (Fulfillment): Lead time = X days | M30 (Red Flag): Same lead time thresholds | Monthly | HIGH |
| **V5** | M0 (Thesis): Win criteria = $X MRR | M25 (Financial Ops), M28 (constraint scenarios): Same target | Quarterly | HIGH |
| **V6** | M0 (Thesis): Kill criteria thresholds | M30 (Red Flag Dashboard): Same thresholds | Quarterly | CRITICAL |
| **V7** | M27 (Customer Research): ICP definition | M17 (Email), M23 (Influencer), M11-M15 (Creative): Aligned targeting | Quarterly | HIGH |
| **V8** | M28 (B2B): MAP price = $44.10 | M10 (Pricing): Same MAP floor | Monthly | HIGH |
| **V9** | HYP registry: Current hypothesis values | M30 (Data Dictionary): Same targets/thresholds | Monthly | CRITICAL |
| **V10** | M17 (Email): Subscription discount = X% | M28 (Amazon): D2C sub > Amazon S&S pricing | Monthly | HIGH |

### When Mismatches Are Found

| Mismatch Type | Resolution | Owner |
|--------------|------------|-------|
| One TUP outdated (older value) | Update to current correct value | Most recent TUP author |
| Genuine disagreement (two TUPs have different but valid numbers) | Escalate to founder for decision, document reasoning | Founder |
| Formula error | Fix formula, validate all downstream calculations | Analyst |
| Structural issue (TUP architecture conflict) | May require TUP revision, flag for next workshop | Session lead |

### Validation Procedure

**Monthly Validation Checklist** (15 min):
1. Open data dictionary alongside financial model parameters
2. Spot-check 3-5 rules from the table above
3. If mismatch found: document in validation log, fix immediately
4. Log validation completion date

**Quarterly Full Audit** (1-2 hrs):
1. Check all 10 rules systematically
2. Cross-reference hypothesis registry values with all TUP content
3. Document any changes made
4. Update data dictionary if definitions have evolved

[Confidence: B | Source: Model consistency requirements from Danilo's ops model design, IonWave TUP cross-references | Verified: 2026-02-08]

---

## 4. Red Flag Integration Map

How the Red Flag Dashboard connects to other TUPs:

```
M0 (Thesis) ─── Kill Criteria Definitions ──→ M30 Red Flag Dashboard
M25 (Financial Ops) ─── Cash/Runway Monitoring ──→ RF-5, RF-6
M24 (Fulfillment) ─── Supply Chain Alerts ──→ RF-7, RF-9
M11-M15 (Creative/DR) ─── Ad Account Status ──→ RF-8
M20 (Support) ─── Chargeback Monitoring ──→ RF-10
M28 (Expansion) ─── Subscription Sensitivity ──→ RF-11
M17 (Email) ─── Email Revenue Share ──→ Retention metrics
M19 (CRM) ─── Churn Signals ──→ RF-3
HYP Registry ─── All Hypothesis Thresholds ──→ RF-1 through RF-12
```

**Key Insight**: M30 doesn't own the data — it MONITORS data owned by other TUPs. The Red Flag Dashboard is a viewer, not a data store. Every metric points back to a source TUP where the actual data lives.

---

## 5. Intelligence Gaps

| Gap | Impact | Upgrade Path | Priority |
|-----|--------|-------------|----------|
| G1: No real-time alerting system yet | Manual checking means delayed response | Implement Slack alerts at Phase 2 ($10K+ MRR) via Triple Whale or custom webhook | MEDIUM |
| G2: Kill thresholds are theoretical | May be too tight or too loose for IonWave specifically | Review and calibrate at Month 3 checkpoint with real data | HIGH |
| G3: Cross-TUP validation is manual | Labor-intensive, easy to skip | Build automated consistency checker if model grows beyond 20 TUPs | LOW |
| G4: No root cause analysis framework | Red flag fires but "why?" requires investigation | Build diagnostic decision trees for top 5 failure modes | MEDIUM |


---

## 🔗 Dependencies & Relationships

### Feeds Into
- _No downstream dependencies_

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

- G1: All metrics are targets, no actuals (pre-launch)
- G2: Attribution methodology needs implementation at launch
- G3: Cohort LTV requires 6+ months of data to validate
- G4: Google Sheets MVD template exists as concept, not downloadable file
- G5: Kill thresholds may need calibration after Month 3 with real data
- G6: Graceful degradation untested — may need further simplification

---

## 🎯 Next Actions

_No next actions documented._


---

---

_Report generated: 2026-02-09 17:49:46_

_Source: `data\m30`_