# TUP M25: Financial Operations

**Status:** migrated | **Quality:** 8.8/10/10 | **Version:** 1.0.0
**Cluster:** BCL-2 (Money & Legal)

---

## 📋 Overview

- **Workshop Date:** 2026-02-06
- **Actor:** claude-opus-4-6
- **Protocol Used:** TWP-001 v2.0.0
- **Change Type:** initial_workshop

### Workshop Dialogue
- **Personas Used:** Skeptical Investor, Operations Expert, Growth Engineer
- **Rounds:** 8
- **Saturated:** True
- **Upgrades Applied:** 6
- **Unresolved Issues:** 0

### Quality Assessment
- **Score:** 8.8/10
- **Rationale:** High actionability (Day 1 Essentials, checklists, Survival Five scorecard). Excellent confidence honesty (dual-margin REC-001 treatment). Strong research grounding. Deductions for pre-launch D-grade assumptions and untested connector recommendation.

---

## 📁 Content Files

- 📄 MD **bookkeeping_setup.md**
- 📄 MD **unit_economics_tracking.md**
- 📄 MD **business_review_cadence.md**
- 📄 MD **dialogue_summary.md**
- 📄 MD **opkit_financial_ops.md**

---

## 🔧 Structured Data

_JSON files converted to human-readable format_

_No JSON files in this TUP._

---

## 📝 Narrative Content

### 📄 bookkeeping_setup.md

# Bookkeeping & Accounting Setup — M25: Financial Operations

**TUP**: M25
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-004 (Gross Margin), HYP-001 (CAC)
**Danilo Source**: ops_model_v10_dump/533_bookkeeping_accounting_setup.json (28 rows)
**Cross-Reference**: M3 (Financial Model), M10 (Pricing & Offer), M30 (Analytics)

---

## Purpose

Establish IonWave's bookkeeping and accounting foundation: what software to use, how accounts are structured, and what gets done every month. This file turns Danilo's 28-row tab (which listed tools and a checklist) into a fully grounded, IonWave-specific accounting setup guide.

**Core principle**: Financial clarity is a compounding asset. Clean books from Day 1 prevent the retroactive cleanup that costs 10x more. The goal is "books always current, reviews automatic, every number trustworthy" (Danilo's vision for M25).

---

## 1. Accounting Method

**Decision: Accrual Basis**

[Confidence: A | Source: IRS requirement for inventory businesses >$25M; best practice for all subscription DTC brands]

| Method | When Revenue Recognized | When Expenses Recognized | Best For |
|--------|------------------------|--------------------------|----------|
| **Cash** | When cash received | When cash paid | Service businesses, very small entities |
| **Accrual** | When earned (sale made) | When incurred (obligation created) | Inventory businesses, subscription models |

**Why accrual for IonWave:**
- Subscription revenue requires deferred revenue tracking (payment ≠ earned revenue)
- Inventory requires COGS matching (cost recognized when product sold, not when purchased)
- Investors/lenders require accrual-basis financials
- IRS requires accrual for inventory businesses exceeding $25M (set up correctly from start)

**Practical note**: Accrual P&L can show profit while cash is negative (common in growth phase). Always monitor cash flow separately — see business_review_cadence.md for the weekly cash review.

---

## 2. Software Stack

### Primary: QuickBooks Online (QBO)

[Confidence: B | Source: Most recommended accounting platform for DTC brands across multiple sources; Danilo's tab also lists QBO first]

| Plan | Monthly Cost | Key Features | Right For |
|------|-------------|-------------|-----------|
| **Simple Start** | $30/mo | 1 user, basic reports, invoicing | Solo founder, pre-revenue |
| **Essentials** | $60/mo | 3 users, bill management, multi-currency | **IonWave starting point** |
| **Plus** | $90/mo | 5 users, inventory tracking, project profitability | When inventory tracking matters |
| **Advanced** | $200/mo | 25 users, custom roles, batch invoicing, advanced reporting | Growth stage ($500K+ revenue) |

**Recommendation**: Start with **Essentials** ($60/mo). Upgrade to Plus when inventory tracking in QBO becomes necessary (likely after first 3PL integration stabilizes).

### Shopify-QBO Connector: Synder

[Confidence: B | Source: Best fit for subscription-first DTC model per research; handles recurring revenue recognition automatically]

**Why Synder over A2X:**

| Feature | Synder | A2X |
|---------|--------|-----|
| Sync mode | Real-time OR daily summary | Daily summary only |
| Individual order sync | Yes | No |
| Subscription revenue handling | Auto-recognizes recurring revenue | Manual tracking required |
| Deferred revenue | Native support | Requires manual journals |
| Multi-platform | Shopify + Amazon + Stripe + PayPal | Shopify + Amazon |
| Price | Volume-based | Volume-based |

**Key integration gotchas:**
1. **Payment processor fees**: Ensure Shopify Payments / Stripe fees post to correct expense accounts (not netted from revenue)
2. **Subscription timing**: ReCharge creates charges on billing date; Synder should match revenue recognition to delivery date, not billing date
3. **Refunds**: Must flow back correctly (reduce revenue, not create expense)
4. **Gift cards**: Liability when sold, revenue when redeemed — connector must handle this

### Sales Tax Automation

[Confidence: B | Source: Multi-source comparison of TaxJar, Avalara, Shopify Tax]

**Phase 1 (Launch — <$100K/state/year)**: Use **Shopify Tax** (built-in)
- No additional cost for tax calculation
- Rooftop accuracy across 11,000+ U.S. jurisdictions
- Nexus liability alerts (warns when approaching thresholds)
- Limitation: Shopify-only (no multi-channel support)

**Phase 2 (Growth — crossing nexus in 5+ states)**: Evaluate **TaxJar** ($19-99/mo)
- Multi-channel support (Shopify + Amazon + wholesale)
- AutoFile submits returns automatically ($30-35/state/return)
- Caveat: Mixed reviews post-Stripe acquisition (3.2/5 on Shopify App Store). Monitor quality.

**Phase 3 (Scale — >$1M revenue, international)**: Evaluate **Avalara**
- Enterprise-grade, no public pricing (requires sales call)
- Only justified at significant scale with multi-state/international complexity

**Economic nexus thresholds (2026):**
- Most states: $100,000 in gross annual sales (revenue threshold only — transaction count thresholds being phased out)
- Notable exceptions: California $500K, Texas $500K, New York $500K + 100 transactions
- **IonWave reality**: Likely hit nexus in home state + 3-5 high-volume states in Year 1

[Confidence: A | Source: South Dakota v. Wayfair (2018), 2026 state law updates, Sales Tax Institute state-by-state guide]

### Other Tools

| Tool | Purpose | Cost | When to Add |
|------|---------|------|-------------|
| **Shopify** | Sales platform, source of truth for orders | Included | Day 0 |
| **Stripe/Shopify Payments** | Payment processing | 2.9% + $0.30/txn | Day 0 |
| **ReCharge** | Subscription management | $99/mo + $0.19/txn | Day 0 |
| **Google Sheets** | Cash flow forecasting, 13-week model | $0 | Day 0 |
| **Inventory Planner** (or Cin7 Lite) | Demand forecasting, reorder alerts | $50-200/mo | Month 3-6 |

---

## 3. Chart of Accounts (IonWave-Specific)

[Confidence: B | Source: DTC ecommerce chart of accounts best practices, adapted for supplement brand with subscription model]

### Day 1 Essentials (Start Here) *(Dialogue upgrade U4)*

For launch day, set up only these 18 accounts. Add the rest when they become relevant.

| Account # | Account Name | Type |
|-----------|-------------|------|
| 1000 | Business Checking | Bank |
| 1010 | Stripe Balance | Bank |
| 1200 | Inventory — Finished Goods | Asset |
| 2000 | Accounts Payable | Liability |
| 2100 | Sales Tax Payable | Liability |
| 2200 | Deferred Revenue | Liability |
| 3000 | Owner's Equity | Equity |
| 3100 | Retained Earnings | Equity |
| 4000 | Product Revenue — Subscription | Revenue |
| 4010 | Product Revenue — One-Time | Revenue |
| 4100 | Discounts & Promos | Contra-Revenue |
| 4110 | Refunds Issued | Contra-Revenue |
| 5000 | COGS — Product | COGS |
| 6000 | Marketing — Meta Ads | Expense |
| 6100 | 3PL — Storage Fees | Expense |
| 6120 | Outbound Shipping | Expense |
| 6200 | Shopify Subscription | Expense |
| 6210 | Payment Processing Fees | Expense |

**Add later**: Separate COGS by line (when 2+ SKUs), marketing by channel (when running Google/TikTok), PayPal (when activated), inventory reserves (Month 3+), return reserve (when return data available).

### Full Chart of Accounts (Reference Architecture)

### Assets

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 1000 | Business Checking | Bank | Primary operating account |
| 1010 | Stripe Balance | Bank | Pending payouts (clears in 2 business days) |
| 1020 | PayPal Balance | Bank | If used |
| 1100 | Accounts Receivable | A/R | B2B/wholesale only (minimal for DTC) |
| 1200 | Inventory — Finished Goods | Asset | Product at 3PL, valued at landed cost |
| 1210 | Inventory — In Transit | Asset | Product shipped from CM, not yet at 3PL |
| 1220 | Reserve for Expired Inventory | Contra-Asset | 3-5% of inventory value |
| 1300 | Prepaid Expenses | Asset | Annual software subscriptions paid upfront |

### Liabilities

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 2000 | Accounts Payable | Liability | CM invoices, 3PL invoices, vendor bills |
| 2100 | Sales Tax Payable | Liability | Collected but not yet remitted |
| 2200 | Deferred Revenue | Liability | **Critical for subscriptions** — payment received, product not yet delivered |
| 2300 | Return Reserve | Liability | Estimated future returns (2-5% of revenue) |
| 2400 | Accrued Expenses | Liability | Expenses incurred but not yet billed |
| 2500 | Loans — Related Parties | Liability | Founder capital, if structured as loan |
| 2510 | Loans — External | Liability | RBF, SBA, bank line |

### Equity

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 3000 | Owner's Equity | Equity | Initial capital contribution |
| 3100 | Retained Earnings | Equity | Accumulated profits/losses |

### Revenue

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 4000 | Product Revenue — Subscription | Revenue | Recognized when product ships (not when billed) |
| 4010 | Product Revenue — One-Time | Revenue | Recognized when product ships |
| 4020 | Shipping Revenue | Revenue | Charged to customers at checkout |
| 4100 | Discounts & Promos | Contra-Revenue | Coupon codes, subscription discounts |
| 4110 | Refunds Issued | Contra-Revenue | Full and partial refunds |
| 4120 | Returns | Contra-Revenue | Product returns net impact |

**Why split subscription vs one-time revenue**: Different unit economics (HYP-002 tracks subscription attach rate), different LTV profiles, different retention dynamics. This split is essential for tracking HYP-005 (Blended LTV).

### Cost of Goods Sold

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 5000 | COGS — Product (Subscription) | COGS | Landed cost: CM price + freight-in |
| 5010 | COGS — Product (One-Time) | COGS | Same calculation |
| 5020 | COGS — Packaging | COGS | Boxes, inserts, labels |
| 5030 | COGS — Freight In | COGS | Shipping from CM to 3PL (capitalized into inventory) |
| 5040 | Loss on Expired Inventory | COGS | Write-off when product expires (if immaterial) |
| 5050 | COGS — Third-Party Testing | COGS | COA testing, heavy metals, microbiology ($500-1500/batch) |

**Gross margin calculation**: (Revenue − COGS) / Revenue
- HYP-004 target: 67% at $59 one-time price, ~62-64% blended with subscription discount
- Danilo tab 534-535 used 45% — this is the **REC-001 margin dispute**. See unit_economics_tracking.md for dual-scenario treatment.

[Confidence: B | Source: HYP-004 revision history. 67% is based on Biocean supplier quotes ($18-20 COGS). 45% origin in Danilo files is unexplained.]

### Operating Expenses — Marketing

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 6000 | Marketing — Meta Ads | Expense | Track ROAS per M13 (Media Buying) |
| 6010 | Marketing — Google Ads | Expense | Brand + search campaigns |
| 6020 | Marketing — TikTok Ads | Expense | If/when activated |
| 6030 | Marketing — Influencer/Creator | Expense | Product seeding + paid partnerships per M23 |
| 6040 | Marketing — Affiliate/Referral | Expense | Referral credits per M22 |
| 6050 | Marketing — Email/SMS Platform | Expense | Klaviyo subscription |
| 6060 | Marketing — Content Production | Expense | Freelance writers, graphic design per M16 |

**Why separate ad accounts by channel**: Required for CAC-by-channel tracking (see unit_economics_tracking.md). HYP-001 assumes $35 blended CAC — need channel-level data to validate.

### Operating Expenses — Fulfillment & Shipping

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 6100 | 3PL — Storage Fees | Expense | Monthly warehouse cost |
| 6110 | 3PL — Pick/Pack/Ship Fees | Expense | Per-order handling |
| 6120 | Outbound Shipping | Expense | Carrier cost to customer (freight-out) |
| 6130 | Return Shipping | Expense | Inbound return labels |

**Note**: Outbound shipping is an operating expense, NOT COGS. Some brands net it against Shipping Revenue (4020). Either treatment is acceptable — just be consistent.

### Operating Expenses — Platform & Technology

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 6200 | Shopify Subscription | Expense | Monthly platform fee |
| 6210 | Payment Processing Fees | Expense | Stripe 2.9% + $0.30 per transaction |
| 6220 | Software Subscriptions | Expense | QBO, ReCharge, Klaviyo, analytics tools |
| 6230 | Domain & Hosting | Expense | Annual domain, CDN if applicable |

### Operating Expenses — General & Administrative

| Account # | Account Name | Type | Notes |
|-----------|-------------|------|-------|
| 6300 | Insurance — Product Liability | Expense | Required for supplement brands |
| 6310 | Legal & Professional | Expense | CPA fees, legal review, label compliance |
| 6320 | Regulatory & Compliance | Expense | FDA compliance consulting, if not in COGS |
| 6330 | Bank Fees | Expense | Wire fees, account maintenance |
| 6340 | Office & Admin | Expense | Miscellaneous operating costs |

### QBO Class Tracking

In addition to the chart of accounts, use QBO **Classes** to tag transactions by dimension without creating sub-accounts:

| Class | Purpose |
|-------|---------|
| **By Product Line** | If multiple SKUs (e.g., Original, Keto Blend, Athletic) |
| **By Channel** | DTC vs Wholesale vs Amazon (if multi-channel later) |

---

## 4. Inventory Accounting

### Method: FIFO (First-In, First-Out)

[Confidence: A | Source: Standard for perishable goods; aligns with 3PL physical rotation (FEFO — First-Expired, First-Out)]

**Why FIFO for supplements:**
- Products have 2-year shelf life — FIFO prevents expired inventory sitting behind newer stock
- 3PLs physically rotate using FEFO (mirrors FIFO for single-product brands)
- Matches physical flow to accounting flow — no discrepancies

**Alternative (Weighted Average Cost)**: Simpler but masks cost trends and doesn't match physical flow. Not recommended for expiry-sensitive products.

### Landed Cost Calculation

| Cost Component | Example (per unit) | Treatment |
|----------------|-------------------|-----------|
| CM product cost | $15.00 | Inventory (capitalize) |
| CM markup/handling | $2.00 | Inventory (capitalize) |
| Freight-in (CM → 3PL) | $1.50 | Inventory (capitalize) |
| Packaging materials | $1.50 | Inventory (capitalize) |
| **Total Landed Cost** | **$20.00** | **COGS when sold** |

[Confidence: B | Source: HYP-004 uses $18-20 COGS from Biocean supplier quotes. Breakdown is estimated.]

### Inventory Journal Entries

**Receive inventory from CM:**
```
Debit:  1200 Inventory — Finished Goods    $10,000
Credit: 2000 Accounts Payable              $10,000
```

**Sell product to customer:**
```
Debit:  5000 COGS — Product                $20.00
Credit: 1200 Inventory — Finished Goods    $20.00
```

**Write off expired inventory:**
```
Debit:  5040 Loss on Expired Inventory     $500
Credit: 1200 Inventory — Finished Goods    $500
```

### Expiry & Spoilage

- Budget 3-5% spoilage into financial projections
- If loss is immaterial: debit COGS (5040), credit Inventory
- If loss is material: use separate P&L line item "Loss on Expired Inventory" below gross profit
- **Document**: Batch numbers, expiry dates, photos of disposal, quantity destroyed
- **Tax deduction**: Generally deductible with proper documentation — confirm with CPA

[Confidence: A | Source: GAAP inventory write-off standards, IRS deductibility rules for destroyed inventory]

---

## 5. Subscription Revenue Recognition

### The Problem

Customer pays $50.15 on January 1 for a monthly subscription. Product ships January 5. When is revenue recognized?

### The Answer (ASC 606)

Revenue is recognized when the **performance obligation is satisfied** — i.e., when the product is delivered to the customer (or shipped, depending on contract terms).

[Confidence: A | Source: ASC 606 five-step model; applies to all businesses regardless of size]

**For IonWave's subscription model:**

1. Customer billed on Day 1 → **Deferred Revenue** (liability)
2. Product ships on Day 5 → Revenue recognized, Deferred Revenue reduced

**Journal entries:**

**Customer billed (Day 1):**
```
Debit:  1010 Stripe Balance                $50.15
Credit: 2200 Deferred Revenue              $50.15
```

**Product ships (Day 5):**
```
Debit:  2200 Deferred Revenue              $50.15
Credit: 4000 Product Revenue — Subscription $50.15
```

### Practical Simplification

For a single-product monthly subscription where billing and shipping happen within 1-5 days:
- **Acceptable shortcut**: Recognize revenue at billing date (immaterial timing difference)
- **Better practice**: Recognize at shipment date (proper ASC 606 compliance)
- **Required for audit**: Recognize at delivery date with proper deferred revenue tracking

[Confidence: B | Source: ASC 606 practical expedients for immaterial timing differences]

**Synder handles this**: When configured correctly, Synder can recognize subscription revenue at the correct point (billing, shipment, or delivery) and automatically create deferred revenue entries.

---

## 6. Monthly Bookkeeping Checklist

[Confidence: B | Source: Danilo tab 533 (8-item checklist) expanded with DTC-specific items from research]

### Weekly Tasks (Every Friday — 30 min)

| # | Task | Tool | Why |
|---|------|------|-----|
| W1 | Review bank balance and pending payouts | QBO + Stripe dashboard | Cash visibility — catch anomalies early |
| W2 | Review 13-week cash flow forecast | Google Sheets | Anticipate shortfalls 4-6 weeks ahead |
| W3 | Spot-check Synder sync | QBO | Catch transaction errors before month-end |

### Monthly Tasks (First week of following month — 3-4 hours)

| # | Task | Tool | Owner | Why |
|---|------|------|-------|-----|
| M1 | Reconcile all bank accounts | QBO | Bookkeeper/Founder | Ensure every transaction categorized |
| M2 | Reconcile Stripe/PayPal payouts | QBO + Synder | Bookkeeper | Match payouts to orders |
| M3 | Reconcile inventory count | QBO + 3PL report | Bookkeeper | Verify book value matches physical count |
| M4 | Record COGS for month | QBO | Bookkeeper | Match product costs to revenue |
| M5 | Review deferred revenue balance | QBO | Bookkeeper | Ensure subscription revenue properly recognized |
| M6 | Accrue unpaid expenses | QBO | Bookkeeper | CM invoices, 3PL fees not yet billed |
| M7 | Update return reserve | QBO | Bookkeeper | Adjust based on actual return rate |
| M8 | Review and categorize uncategorized transactions | QBO | Bookkeeper | Zero uncategorized items |
| M9 | Record sales tax collected vs remitted | QBO + TaxJar/Shopify Tax | Bookkeeper | Reconcile liability |
| M10 | Generate financial statements (P&L, Balance Sheet, Cash Flow) | QBO | Bookkeeper | Ready for MBR (see business_review_cadence.md) |
| M11 | Calculate unit economics by channel | Spreadsheet | Founder | CAC, LTV, ROAS — see unit_economics_tracking.md |
| M12 | Set aside tax reserve (25-30% of net profit) | Bank transfer | Founder | Avoid quarterly estimated tax surprises |

### Quarterly Tasks

| # | Task | Tool | Why |
|---|------|------|-----|
| Q1 | File quarterly estimated tax payment | IRS EFTPS | Avoid underpayment penalties |
| Q2 | File sales tax returns (states where nexus crossed) | TaxJar/Shopify Tax | Compliance |
| Q3 | Review chart of accounts | QBO | Add/remove accounts as business evolves |
| Q4 | Physical inventory audit (or 3PL count reconciliation) | 3PL + QBO | Catch shrinkage, expiry, discrepancies |

### Annual Tasks

| # | Task | Tool | Why |
|---|------|------|-----|
| A1 | 1099 filing (contractors >$600) | QBO or CPA | IRS requirement |
| A2 | Annual tax return | CPA | File by March 15 (S-Corp) or April 15 (LLC) |
| A3 | Review insurance coverage | Broker | Product liability, general liability |
| A4 | Review software stack | — | Upgrade/downgrade based on needs |
| A5 | Annual planning process | See business_review_cadence.md | Strategic planning cycle |

---

## 7. Common Financial Mistakes to Avoid

[Confidence: B | Source: Aggregated from multiple DTC financial operations sources]

### The Top 10 for Year 1

| # | Mistake | IonWave Mitigation |
|---|---------|-------------------|
| 1 | **Poor bookkeeping / delayed financial reporting** — books closed weeks after month-end | Synder auto-sync + monthly checklist above. Target: books closed by 5th of following month. |
| 2 | **Ignoring cash flow** — 82% of small businesses fail from cash flow, not profitability | Weekly cash review (W2). 13-week rolling forecast. |
| 3 | **Not tracking CAC by channel** — can't optimize what you can't measure | Chart of accounts separates ad spend by channel (6000-6020). See unit_economics_tracking.md. |
| 4 | **Gross margin miscalculation** — forgetting payment fees, packaging, freight | Landed cost calculation (Section 4) includes ALL cost components. |
| 5 | **Confusing cash and accrual** — showing profit on P&L with no cash in bank | Accrual P&L + separate cash flow monitoring. Both reviewed in MBR. |
| 6 | **Overstocking inventory** — ties up cash, risk of expiry | Demand forecasting from Month 3. Safety stock = 2-4 weeks. |
| 7 | **Sales tax non-compliance** — collecting but not remitting, missing nexus thresholds | Shopify Tax from Day 0. TaxJar when crossing 5+ states. |
| 8 | **Not reviewing financial statements** — flying blind | Monthly Business Review — see business_review_cadence.md. |
| 9 | **No tax planning** — profitable on paper, no cash saved for taxes | 25-30% tax reserve set aside monthly (M12 in checklist). |
| 10 | **Using generalist accountant** — misses DTC/ecommerce nuances | Hire ecommerce-specialized bookkeeper/CPA by Month 6 or $100K revenue. |

### Supplement-Specific Mistakes

| # | Mistake | Mitigation |
|---|---------|-----------|
| 11 | Not budgeting for third-party testing ($500-1500/batch) | Include in COGS (5050) or operating expenses. Budget before first order. |
| 12 | Not accounting for expiry losses (3-5%) | Reserve for Expired Inventory (account 1220). Budget in projections. |
| 13 | Underestimating regulatory costs | Budget $2-5K/year for label reviews, FDA compliance consulting. |

---

## 8. When to Hire Financial Help

[Confidence: C | Source: DTC industry benchmarks, fractional CFO firm guidance]

| Stage | Revenue | Who to Hire | Cost | What They Do |
|-------|---------|-------------|------|-------------|
| **Pre-launch** | $0 | Founder does books (QBO + Synder) | $0 (time only) | Basic bookkeeping, reconciliation |
| **Early revenue** | $0-50K/mo | Part-time bookkeeper | $300-800/mo | Monthly close, reconciliation, reporting |
| **Growth** | $50-200K/mo | Ecommerce bookkeeper + CPA for tax | $800-2000/mo | Full monthly close, tax planning, compliance |
| **Scale** | $200K+/mo | Fractional CFO + bookkeeper | $2000-5000/mo | Strategic finance, forecasting, fundraising support |

**Key trigger**: When founder time on bookkeeping exceeds 4 hours/week, hire help. Financial time is better spent on strategy (reviewing numbers) than operations (entering numbers).

---

## Intelligence Gaps

| Gap | Priority | Validation Path | Current Grade |
|-----|----------|----------------|---------------|
| Synder vs A2X real-world performance with ReCharge subscriptions | **CRITICAL** | **Pre-launch**: Set up both in trial mode, test with 10 sample transactions before committing. The connector is the single point of failure for all financial reporting — getting it wrong means retroactive cleanup. | C |
| Optimal QBO plan at launch (Essentials vs Plus) | MEDIUM | Test inventory features in QBO Plus trial | C |
| DTC-specialized bookkeeper/CPA rates in IonWave's market | LOW | Get 3 quotes from ecommerce bookkeeping services (Bench, Finaloop, local) | D |
| Third-party testing: COGS vs operating expense (industry standard) | LOW | Check 10-K filings of public supplement companies (NBTY, GNC) | D |


---

### 📄 business_review_cadence.md

# Business Review Cadence — M25: Financial Operations

**TUP**: M25
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-007 (Timeline to $30K MRR), HYP-008 (Capital Sufficiency)
**Danilo Source**: ops_model_v10_dump/536_monthly_business_review.json (2 rows), 537_quarterly_planning.json (31 rows), 538_annual_planning_process.json (29 rows)
**Cross-Reference**: M35 (Execution Plans), M30 (Analytics), M3 (Financial Model)

---

## Purpose

Define IonWave's business review rhythm: what gets reviewed when, by whom, and what decisions follow. Three Danilo tabs merged here (MBR, QBR, Annual) into a single cadence system. The MBR (2 rows in Danilo) was actually the most detailed — a full 10-section, 80-minute meeting agenda packed into raw text. QBR (31 rows) provided an OKR framework. Annual (29 rows) provided a planning timeline.

**Core principle**: Reviews are not bureaucracy — they're the feedback loop. Without a cadence, founders either never look at numbers (fly blind) or look at the wrong numbers at the wrong time. The goal is the minimum review structure that catches problems before they become crises.

**Scope boundary**: This file covers the *financial and strategic* review cadence. Operational reviews (inventory, fulfilment, customer service) live in M35 (Execution Plans). Analytics dashboards and KPI definitions live in M30 (Analytics). This file is the *meeting structure and decision framework*.

---

## 1. Review Cadence Overview

| Cadence | Duration | Participants | Purpose | First Instance |
|---------|----------|-------------|---------|---------------|
| **Weekly Cash Check** | 15 min | Founder (solo) | Cash flow pulse, ad spend check | Week 1 |
| **Monthly Business Review (MBR)** | 60-80 min | Founder + Advisor/Partner | Performance vs plan, course corrections | Month 2 |
| **Quarterly Business Review (QBR)** | 2-3 hours | Founder + Key Stakeholders | Strategic review, OKR reset, resource allocation | Quarter 2 |
| **Annual Planning** | 2-3 days (over 8 weeks) | Founder + Studio/Investors | Vision, goals, budget, milestones | Year 2 |

### Phase-Gating

**Pre-revenue (Month 0-1)**: Weekly Cash Check only. Nothing to review yet — focus on launch.

**Early revenue (Month 2-6)**: Weekly Cash Check + Monthly MBR. This is the survival phase — every month matters. MBR is the most important meeting.

**Growth (Month 6-12)**: Add Quarterly QBR. Enough data for quarterly strategic decisions.

**Scale (Month 12+)**: Full cadence including Annual Planning. Business is mature enough for long-horizon planning.

---

## 2. Weekly Cash Check (15 min, Every Friday)

[Confidence: B | Source: DTC cash management best practices. 82% of small business failures are cash flow related.]

### Agenda

| # | Check | Source | What You're Looking For |
|---|-------|--------|------------------------|
| 1 | Current bank balance | QBO / Bank app | Enough to cover next 2 weeks of obligations? |
| 2 | Pending Stripe payouts | Stripe dashboard | Any holds or delays? |
| 3 | This week's ad spend vs budget | Meta/Google Ads Manager | Overspend? Underspend? |
| 4 | This week's revenue vs last week | Shopify dashboard | Trend direction |
| 5 | Upcoming obligations (next 2 weeks) | QBO A/P | CM invoice due? 3PL bill? Tax payment? |

### 13-Week Cash Flow Forecast

Maintain a rolling 13-week (one quarter) cash forecast in Google Sheets:

```
Columns: Week 1, Week 2, ... Week 13
Rows:
  Starting Cash Balance
  + Revenue (collected, not earned)
  − Ad Spend
  − CM/Inventory Payments
  − 3PL/Fulfilment
  − Software Subscriptions
  − Payroll/Contractor
  − Tax Payments
  − Other
  = Ending Cash Balance
```

**Example (Month 3, base case)** *(Dialogue upgrade U5)*:

| Row | Week 1 | Week 2 | Week 3 | Week 4 |
|-----|--------|--------|--------|--------|
| Starting Cash | $18,000 | $16,850 | $15,700 | $15,250 |
| + Revenue (Stripe payouts) | $1,500 | $1,600 | $1,700 | $1,800 |
| − Ad Spend | $1,250 | $1,250 | $750 | $1,250 |
| − CM/Inventory | $0 | $0 | $0 | $0 |
| − 3PL/Fulfilment | $400 | $400 | $400 | $400 |
| − Software (QBO, ReCharge, Klaviyo, Shopify) | $0 | $0 | $1,000 | $0 |
| − Contractors | $0 | $0 | $0 | $0 |
| − Tax payments | $0 | $0 | $0 | $0 |
| − Other | $0 | $0 | $0 | $100 |
| **Ending Cash** | **$16,850** | **$15,700** | **$15,250** | **$15,300** |

*Note: CM invoice ($5K-10K) hits quarterly — model those weeks explicitly. Revenue ramps weekly as subscriber base grows.*

**[TRACK B — requires human]**: Build this as a Google Sheets template with formulas (rolling 13 weeks, auto-calculates ending balances, conditional formatting for <$5K threshold).

**Update**: Every Friday during Weekly Cash Check
**Alert threshold**: If any week in the forecast shows <$5K cash balance, flag immediately

[Confidence: B | Source: Standard startup cash management tool. 13-week is standard because it covers one fiscal quarter of visibility.]

---

## 3. Monthly Business Review — MBR (60-80 min)

[Confidence: B | Source: Danilo tab 536 (detailed 10-section agenda), expanded with hypothesis system integration]

### Pre-Meeting Prep (30 min before MBR)

The MBR is only useful if the data is ready. Before the meeting:

| # | Task | Owner | Source |
|---|------|-------|--------|
| 1 | Close books for prior month | Bookkeeper/Founder | QBO (see bookkeeping_setup.md checklist) |
| 2 | Generate P&L, Balance Sheet, Cash Flow Statement | QBO | Standard financial statements |
| 3 | Calculate unit economics by channel | Founder | See unit_economics_tracking.md |
| 4 | Pull ad performance summary | Founder | Meta/Google Ads Manager |
| 5 | Pull subscription metrics | Founder | ReCharge dashboard |
| 6 | Pull customer feedback highlights | Founder | Shopify reviews, email replies, support tickets |

### MBR Agenda (10 Sections)

#### Section 1: Executive Summary (5 min)

One-paragraph state of the business. Written before the meeting by the founder.

Template:
> "In [Month], we generated $[X] revenue ([+/-]% vs prior month, [+/-]% vs plan). We acquired [N] new customers at $[X] blended CAC. MRR is $[X] ([+/-]% vs target). The key win was [X]. The key concern is [Y]. Cash runway is [N] months."

#### Section 2: Scorecard vs Targets (15 min)

The heart of the MBR. Compare actuals to targets for every key metric.

**Survival Five (Month 2-6)** *(Dialogue upgrade U3)*: For a solo founder, track only these 5 metrics in early MBRs. Everything else is either derived from these or doesn't change month-to-month at early stage.

| # | Metric | Target | Why It's Survival-Critical |
|---|--------|--------|---------------------------|
| 1 | **Cash Runway** | ≥6 months | You die without cash. Check first. |
| 2 | **Blended CAC** | ≤$38 | Determines if acquisition works at all. |
| 3 | **MRR** | Growing m/m | Progress toward $30K target (HYP-007). |
| 4 | **Monthly Churn** | ≤12% | The silent killer — catches product problems. |
| 5 | **Subscription Attach** | ≥45% | Determines LTV profile of customer base. |

**Full Scorecard (Month 6+)**: Expand to full 10-metric view when data is mature enough for trend analysis.

| Metric | Target | Actual | Delta | Status | Hypothesis |
|--------|--------|--------|-------|--------|------------|
| **Revenue** | $[X] | $[X] | [+/-]% | 🟢/🟡/🔴 | HYP-007 |
| **Orders** | [N] | [N] | [+/-]% | 🟢/🟡/🔴 | — |
| **New Customers** | [N] | [N] | [+/-]% | 🟢/🟡/🔴 | — |
| **Blended CAC** | $35 | $[X] | [+/-]$ | 🟢/🟡/🔴 | HYP-001 |
| **Subscription Attach Rate** | 50% | [X]% | [+/-]% | 🟢/🟡/🔴 | HYP-002 |
| **Monthly Churn** | ≤12% | [X]% | [+/-]% | 🟢/🟡/🔴 | HYP-003 |
| **Gross Margin** | 67% | [X]% | [+/-]% | 🟢/🟡/🔴 | HYP-004 |
| **LTV:CAC** | ≥3.0x | [X]x | [+/-] | 🟢/🟡/🔴 | HYP-005 |
| **MRR** | $[X] | $[X] | [+/-]% | 🟢/🟡/🔴 | HYP-007 |
| **Cash Runway** | ≥6 months | [N] months | — | 🟢/🟡/🔴 | HYP-008 |

**Status key**:
- 🟢 On track (within 10% of target)
- 🟡 Watch (10-25% off target)
- 🔴 Off track (>25% off target or past kill criteria)

#### Section 3: What Worked (5 min)

List 2-3 wins from the month. Be specific:
- "Meta Prospecting creative angle #3 (problem-aware hook) delivered $28 CAC vs $42 average"
- "Subscription attach rate hit 56% after subscription-first checkout redesign"

#### Section 4: What Didn't Work (5 min)

List 2-3 things that underperformed. Be honest:
- "Google Non-Brand campaigns burned $1,200 at $65 CAC — paused"
- "Email welcome flow had 2% click rate (industry avg is 8-12%)"

#### Section 5: Key Learnings (5 min)

What did we learn that changes our approach going forward?
- Not just "what happened" but "what this means for next month"
- Link to hypothesis updates if a learning affects a hypothesis

#### Section 6: Customer Insights (10 min)

| Source | Insight | Action |
|--------|---------|--------|
| Reviews | [Quote or summary] | [What to do about it] |
| Support tickets | [Pattern or theme] | [What to do about it] |
| Survey responses | [Data point] | [What to do about it] |
| Churn reasons | [Top 3 cancellation reasons] | [Retention intervention] |

**Why this section matters**: Unit economics are lagging indicators. Customer feedback is a leading indicator. If customers are unhappy, churn will increase next month — you want to catch it here, not in next month's scorecard.

#### Section 7: Competitive Landscape (5 min)

Quick scan: Any competitor moves worth noting? New products, pricing changes, ad creative shifts?
- Cross-reference: M26 (Competitive Intel) monitoring system
- Skip this section if nothing notable happened

#### Section 8: Next Month Priorities (10 min)

| Priority | Owner | Target | Completion Criteria |
|----------|-------|--------|-------------------|
| 1. [Top priority] | [Name] | [Measurable target] | [How we know it's done] |
| 2. [Second priority] | [Name] | [Measurable target] | [How we know it's done] |
| 3. [Third priority] | [Name] | [Measurable target] | [How we know it's done] |

**Rule**: Maximum 3 priorities. More than 3 = no priorities.

#### Section 9: Resource Needs (5 min)

| Resource | Why Needed | Cost | Decision |
|----------|-----------|------|----------|
| [Tool/person/budget] | [Why] | [$X] | Approved / Deferred / Declined |

#### Section 10: Open Discussion (10 min)

Unstructured time for questions, concerns, ideas that don't fit elsewhere.

### MBR Output

After every MBR, create a brief written record (5 min to write):
1. **3-sentence summary** of business state
2. **Scorecard** (Section 2 table — copy/paste)
3. **Top 3 priorities** for next month (Section 8)
4. **Decisions made** (approvals, kills, pivots)
5. **Hypothesis updates** (if any metric triggered a hypothesis revision)

Store in: `tracking/MBR_Log.md` or equivalent

---

## 4. Quarterly Business Review — QBR (2-3 hours)

[Confidence: B | Source: Danilo tab 537 (OKR framework + resource allocation), adapted for early-stage DTC]

### Pre-QBR Prep

| # | Task | Time | Source |
|---|------|------|--------|
| 1 | Aggregate 3 months of MBR scorecards | 30 min | MBR logs |
| 2 | Calculate quarterly trends (are metrics improving?) | 30 min | QBO + spreadsheet |
| 3 | Review hypothesis registry for changes | 15 min | data/hypotheses/registry.json |
| 4 | Draft OKR proposals for next quarter | 45 min | Founder reflection |

### QBR Agenda

#### Part 1: Quarter in Review (45 min)

**Quarterly Scorecard** (aggregate of 3 MBRs):

| Metric | Q Target | Q Actual | Trend (improving/flat/declining) | Notes |
|--------|----------|----------|--------------------------------|-------|
| Revenue | $[X] | $[X] | [↑/→/↓] | |
| New Customers | [N] | [N] | [↑/→/↓] | |
| Blended CAC | $35 | $[X] | [↑/→/↓] | Lower is better |
| Subscription Attach | 50% | [X]% | [↑/→/↓] | |
| Monthly Churn | ≤12% | [X]% | [↑/→/↓] | Lower is better |
| MRR | $[X] | $[X] | [↑/→/↓] | |
| Cash Balance | $[X] | $[X] | — | |

**Hypothesis Status Review**: Which hypotheses moved from ASSUMED to TESTING? Any grade upgrades? Any kill criteria triggered?

#### Part 2: OKRs — Objectives & Key Results (45 min)

**Framework** (from Danilo tab 537):

Set 2-3 Objectives for next quarter, each with 2-3 Key Results.

**Template:**

> **Objective 1**: [Qualitative goal — what we want to achieve]
> - KR 1.1: [Quantitative measure] — Current: [X], Target: [Y]
> - KR 1.2: [Quantitative measure] — Current: [X], Target: [Y]
> - KR 1.3: [Quantitative measure] — Current: [X], Target: [Y]

**Example (Quarter 2):**

> **Objective 1**: Validate unit economics and achieve sustainable CAC
> - KR 1.1: Blended CAC ≤$38 (from current $[X])
> - KR 1.2: LTV:CAC ≥2.8x sustained for 30 days
> - KR 1.3: 3+ creative angles tested with ≥100 conversions each
>
> **Objective 2**: Build subscription retention foundation
> - KR 2.1: Month 1 churn ≤15% across all cohorts
> - KR 2.2: Save flow live in Shopify, recovering ≥15% of cancellation attempts
> - KR 2.3: Welcome email flow achieving ≥30% open rate and ≥8% click rate

**OKR rules:**
- Maximum 3 Objectives
- Maximum 3 Key Results per Objective
- Key Results must be quantitative and measurable
- 70% achievement = good (OKRs should be stretchy)
- Review and score previous quarter's OKRs before setting new ones

#### Part 3: Resource Allocation (30 min)

**Resource buckets** (from Danilo tab 537):

| Resource | This Quarter | Next Quarter | Change | Rationale |
|----------|-------------|-------------|--------|-----------|
| **Ad Budget** | $[X]/mo | $[X]/mo | [+/-]% | [Why changing] |
| **Founder Time** | [X] hrs/week on [area] | [X] hrs/week on [area] | — | [Where to shift focus] |
| **Tools/Software** | $[X]/mo total | $[X]/mo total | [+/-] | [New tools added/removed] |
| **Outsourcing** | $[X]/mo | $[X]/mo | [+/-] | [Freelancers, agencies] |

#### Part 4: Strategic Bets (15 min)

From Danilo tab 537 — each quarter, identify 1-2 "strategic bets" to test:

| Bet | Description | Investment | Success Criteria | Kill Criteria | Timeline |
|-----|------------|-----------|-----------------|---------------|----------|
| Bet 1 | [What we're trying] | [$X + time] | [How we know it worked] | [How we know to stop] | [Weeks/months] |
| Bet 2 | [What we're trying] | [$X + time] | [How we know it worked] | [How we know to stop] | [Weeks/months] |

**Examples:**
- "Test TikTok organic for 60 days — post 5x/week, measure follower growth and site traffic"
- "Run Reddit engagement experiment in r/keto — 30 days genuine contribution, then measure referral traffic"

#### Part 5: Risks to Monitor (15 min)

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|-----------|-------|
| [Risk description] | H/M/L | H/M/L | [What we do if it happens] | [Who monitors] |

**Standing risks for IonWave:**
- CAC drift above $45 → reduce ad spend, test new channels
- Churn above 15% → product investigation, retention sprint
- Cash runway below 3 months → pause growth spending, initiate fundraise
- Supplier disruption → identify backup supplier per M6
- Regulatory action → FDA compliance review per M7

### QBR Output

1. **Previous quarter OKR scorecard** (scored 0-1.0 per KR)
2. **Next quarter OKRs** (approved)
3. **Resource allocation changes** (approved)
4. **Strategic bets** (committed)
5. **Risk register** (updated)
6. **Hypothesis updates** (if any)

---

## 5. Annual Planning Process (2-3 days over 8 weeks)

[Confidence: B | Source: Danilo tab 538 (8-week timeline + 7 plan components), adapted for early-stage DTC]

### When to Start Annual Planning

**Note**: For Year 1, annual planning is premature — focus on MBRs and QBRs. This section becomes relevant for Year 2 planning (starting ~November of Year 1).

### 8-Week Planning Timeline (from Danilo)

| Week | What | Who | Output |
|------|------|-----|--------|
| **Nov Week 1** | Year in review — what happened | Founder | Review document |
| **Nov Week 2** | Market/competitive analysis | Founder | Market update |
| **Nov Week 3** | Draft goals and priorities | Founder | Draft plan |
| **Nov Week 4** | Budget planning | Founder + Studio/Advisor | Draft budget |
| **Dec Week 1** | Strategy session | Founder + Studio/Advisor | Aligned plan |
| **Dec Week 2** | Finalize plan and budget | Founder + Studio/Advisor | Final plan |
| **Dec Week 3** | Communicate to team/stakeholders | Founder | Shared plan |
| **Jan Week 1** | Execute | Founder | Action |

### 7 Plan Components (from Danilo)

| # | Component | Question It Answers | Example |
|---|-----------|-------------------|---------|
| 1 | **Vision** | Where are we going? (North star) | "IonWave is the trusted marine plasma brand for health-conscious adults" |
| 2 | **Goals** | What will we achieve this year? (3-5 big goals) | "$500K ARR, 2,000 active subscribers, 3 SKUs" |
| 3 | **Priorities** | What matters most? (Ranked) | "1. Retention 2. Channel diversification 3. Product line expansion" |
| 4 | **Initiatives** | How will we achieve goals? (Key projects) | "Launch email nurture revamp, test Google Ads, develop keto-specific SKU" |
| 5 | **Budget** | What resources do we need? | "Marketing $X/mo, Operations $X/mo, Product dev $X" |
| 6 | **Milestones** | How will we track progress? (Quarterly) | "Q1: $100K ARR, Q2: $200K ARR, Q3: $350K ARR, Q4: $500K ARR" |
| 7 | **Risks** | What could go wrong? (And mitigation) | "Supply chain disruption → backup supplier by Q2" |

### Strategic Questions (Start/Stop/Continue)

From Danilo's Annual Planning tab — answer these during Nov Week 1:

- What did we learn this year?
- What's changed in the market?
- What's our biggest opportunity?
- What's our biggest risk?
- What should we **START** doing?
- What should we **STOP** doing?
- What should we **CONTINUE** doing?
- What resources do we need?
- What does success look like Dec 31?

---

## 6. Hypothesis Integration

### How Reviews Connect to the Hypothesis System

The business review cadence is the primary mechanism for hypothesis validation. Every MBR scorecard tests multiple hypotheses simultaneously:

| Hypothesis | MBR Metric | Kill Criteria (from registry) | When to Escalate |
|-----------|-----------|------------------------------|-------------------|
| HYP-001 (CAC) | Blended CAC | >$50 after $3K spend | Immediately — affects all downstream |
| HYP-002 (Sub Rate) | Subscription Attach | <35% after 100 orders | MBR discussion, funnel redesign |
| HYP-003 (Churn) | Monthly Churn | >15% in first 2 cohorts | MBR discussion, product investigation |
| HYP-004 (Margin) | Gross Margin | COGS >$25 | QBR — supplier negotiation |
| HYP-005 (LTV) | LTV:CAC Ratio | <2.5x after 6 months | QBR — strategic review |
| HYP-007 (Timeline) | MRR | <$5K by Month 6 | QBR — strategy pivot |
| HYP-008 (Capital) | Cash Runway | <3 months | Immediately — fundraise trigger |

### Escalation Protocol

When a kill criterion is triggered:

1. **MBR-level** (CAC, churn, sub rate): Discuss in next MBR. Set 30-day action plan.
2. **QBR-level** (LTV:CAC, timeline): Discuss in next QBR. Consider strategy pivot.
3. **Immediate** (cash runway <3 months, CAC >$50 with no improvement): Emergency session. Don't wait for next review.

---

## Intelligence Gaps

| Gap | Priority | Validation Path | Current Grade |
|-----|----------|----------------|---------------|
| Optimal MBR format for solo founder (60 min may be too long for one person) | MEDIUM | Run first 3 MBRs, assess which sections add value | C |
| OKR scoring methodology (how strict?) | LOW | Adopt Google's 70% = good standard, adjust after first quarter | C |
| Annual planning relevance for Year 1 (likely premature) | LOW | Skip annual planning in Year 1, revisit at Month 10 | B |
| Integration between MBR log and hypothesis validation_log.json | MEDIUM | Define automated or manual sync process | D |


---

### 📄 dialogue_summary.md

# Persona Dialogue Summary — M25: Financial Operations

**TUP**: M25
**Dialogue Date**: 2026-02-06
**TUP Version**: 1.0.0
**Protocol**: TWP-001 v2.0.0, Phase 6
**AI Model**: claude-opus-4-6

---

## Personas

| Persona | Role | Lens |
|---------|------|------|
| **Skeptical Investor** | Financial grounding | "Show me evidence, not estimates. Would I write a check based on this?" |
| **Operations Expert** | Operational reality | "What breaks at scale? Where are the single points of failure?" |
| **Growth Engineer** | Unit economics focus | "What's the unit economics of this? What's the compounding mechanism?" |

---

## Round Log

### ROUND 1
- **CHALLENGE** (Skeptical Investor): REC-001 margin resolution is a dodge — redefining the problem rather than resolving it. Which number is right for payback decisions?
- **RESPONSE** (Growth Engineer): Both are right for different decisions. Contribution margin for channel payback, gross margin for P&L reporting.
- **SYNTHESIS** (Operations Expert): Content buries the lead. Add explicit callout: "use contribution margin for channel decisions, gross margin for P&L."
- **OUTCOME**: UPGRADED
- **ACTION**: U1 — Added explicit "Which margin for which decision" callout to unit_economics_tracking.md Section 2.

### ROUND 2
- **CHALLENGE** (Operations Expert): Synder recommendation at B confidence — has anyone tested it with ReCharge + Shopify + QBO? Connector is single point of failure.
- **RESPONSE** (Skeptical Investor): Intelligence gap acknowledges this but is tagged LOW priority. Should be HIGH — first 3 months set the foundation.
- **SYNTHESIS** (Growth Engineer): Upgrade gap to HIGH. Add pre-launch validation step: test both connectors with 10 sample transactions.
- **OUTCOME**: UPGRADED
- **ACTION**: U2 — Upgraded connector gap to CRITICAL in bookkeeping_setup.md. Added pre-launch validation step.

### ROUND 3
- **CHALLENGE** (Growth Engineer): MBR tracks 10 metrics. Too many for a solo founder in Month 2-6. What are the 5 that matter?
- **RESPONSE** (Operations Expert): Survival Five: Cash runway, Blended CAC, MRR, Monthly churn, Subscription attach rate.
- **SYNTHESIS** (Skeptical Investor): Add "Survival Five" condensed scorecard for Month 2-6 in MBR section.
- **OUTCOME**: UPGRADED
- **ACTION**: U3 — Added "Survival Five" condensed scorecard for Month 2-6 to business_review_cadence.md.

### ROUND 4
- **CHALLENGE** (Skeptical Investor): 40+ accounts in chart of accounts is over-engineered for a pre-revenue startup. Day 1 doesn't need all of these.
- **RESPONSE** (Growth Engineer): Disagree partially — right structure from start is cheaper. But agree Day 1 needs subset.
- **SYNTHESIS** (Operations Expert): Add "Day 1 Essentials" subset (18 accounts). Full chart stays as reference architecture.
- **OUTCOME**: UPGRADED
- **ACTION**: U4 — Added "Day 1 Essentials" 18-account subset to bookkeeping_setup.md Section 3.

### ROUND 5
- **CHALLENGE** (Operations Expert): 13-week cash flow forecast described but no template. Solo founder won't build from scratch.
- **RESPONSE** (Growth Engineer): OpKit opportunity — provide ready-to-use template.
- **SYNTHESIS** (Skeptical Investor): Google Sheets template is Track B. For now, add complete row structure with example numbers.
- **OUTCOME**: UPGRADED
- **ACTION**: U5 — Added example 13-week forecast with Month 3 base case numbers to business_review_cadence.md. Flagged Sheets template as Track B.

### ROUND 6
- **CHALLENGE** (Growth Engineer): Last-click attribution undercredits awareness channels for subscription-first brand.
- **RESPONSE** (Skeptical Investor): Multi-touch is a luxury. Last-click for tactical, post-purchase survey for strategic.
- **SYNTHESIS** (Operations Expert): Content already covers this adequately. Minor clarification.
- **OUTCOME**: RESOLVED
- **ACTION**: U6 (minor) — Added first-click vs last-click guidance sentence.

### ROUND 7
- **CHALLENGE** (Skeptical Investor): OKRs are corporate theater for a solo founder.
- **RESPONSE** (Operations Expert): Value is the quarterly goal-setting discipline, not the OKR format.
- **SYNTHESIS** (Growth Engineer): Substance is correct. Renaming cosmetic. Keep as-is.
- **OUTCOME**: RESOLVED
- **ACTION**: None — content is adequate.

### ROUND 8
- **CHALLENGE** (Operations Expert): Annual planning deferred to Year 2 but Month 6 is the real first strategic planning moment.
- **RESPONSE** (Growth Engineer): Month 6 QBR serves as Year 1 mid-year strategic review.
- **SYNTHESIS** (Skeptical Investor): Content's phase-gating handles this implicitly.
- **OUTCOME**: RESOLVED
- **ACTION**: None — already addressed.

---

## Saturation Log

| Round | Outcome | Saturation Signal |
|-------|---------|-------------------|
| 1 | UPGRADED | — |
| 2 | UPGRADED | — |
| 3 | UPGRADED | — |
| 4 | UPGRADED | — |
| 5 | UPGRADED | — |
| 6 | RESOLVED | Signal 1 |
| 7 | RESOLVED | Signal 2 |
| 8 | RESOLVED | Signal 3 — **SATURATED** |

**Saturation reached**: Round 8 (3 consecutive RESOLVED rounds). Hard stop not required.

---

## Upgrades Applied

| ID | File | Change | Round |
|----|------|--------|-------|
| U1 | unit_economics_tracking.md | Added "Which margin for which decision" callout | R1 |
| U2 | bookkeeping_setup.md | Upgraded Synder/A2X gap to CRITICAL with pre-launch validation | R2 |
| U3 | business_review_cadence.md | Added "Survival Five" condensed MBR scorecard for Month 2-6 | R3 |
| U4 | bookkeeping_setup.md | Added "Day 1 Essentials" 18-account chart of accounts subset | R4 |
| U5 | business_review_cadence.md | Added 13-week cash forecast with example numbers + Track B flag | R5 |
| U6 | unit_economics_tracking.md | Added first-click vs last-click attribution guidance | R6 |

---

## Unresolved Gaps

None. All challenges either resolved with existing evidence or upgraded with new content.

---

## What Would Have Been Missed

Without persona dialogue:

1. **Margin decision confusion** (U1): The content presented three margin scenarios but didn't tell the reader which to use when. An operator would have guessed, potentially making channel decisions on gross margin (wrong) or P&L reporting on contribution margin (wrong).

2. **Connector as single point of failure** (U2): The intelligence gap existed but was underprioritzed. A solo founder would have picked Synder based on the recommendation, discovered issues 3 months in, and faced retroactive cleanup.

3. **Analysis paralysis from 10-metric MBR** (U3): A solo founder running a 60-minute meeting with themselves reviewing 10 metrics would either abandon the process (too much) or miss the critical 5 in the noise.

4. **Over-engineered Day 1 setup** (U4): A founder would open the 40+ account chart, feel overwhelmed, and either set up all of them (unnecessary complexity) or skip it entirely (no structure).

5. **Missing cash forecast template** (U5): Describing a forecast without a template is like describing a recipe without ingredients — the founder would have to build it from scratch, likely wouldn't, and would miss the cash flow pulse.


---

### 📄 opkit_financial_ops.md

# OpKit OK-M25-001: Financial Operations Playbook

**OpKit ID**: OK-M25-001
**TUP Origin**: M25 (Financial Operations)
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Purpose**: Reusable production bundle for setting up bookkeeping, tracking unit economics, and running business reviews for any DTC brand.
**Applicability**: Any DTC subscription brand (Shopify-based) in Year 0-2. Supplement-specific details are marked and can be swapped for any product category.

---

## Instructions

### How to Use This OpKit for Any Trade

**Step 1: Assess the brand's stage**
- Pre-revenue? → Focus on bookkeeping setup (Day 1 Essentials) and Weekly Cash Check only
- Early revenue (<$50K/mo)? → Add monthly checklist and MBR
- Growth ($50K-200K/mo)? → Add QBR, full chart of accounts, unit economics dashboard

**Step 2: Customize the chart of accounts**
- Start with the 18 Day 1 Essentials accounts
- Replace IonWave-specific COGS accounts with your product's cost structure
- Add marketing expense accounts per your channel mix (Meta, Google, TikTok, etc.)
- Add product-line sub-accounts when you have 2+ SKUs

**Step 3: Set up the software stack**
- Accounting: QuickBooks Online (or Xero if non-US)
- Connector: Test both Synder and A2X with 10 sample transactions before committing
- Sales tax: Start with Shopify Tax built-in, upgrade to TaxJar at 5+ state nexus
- Subscription: Use whatever subscription platform the brand uses (ReCharge, Bold, Loop)

**Step 4: Establish the review cadence**
- Week 1: Start Weekly Cash Check (15 min/Friday)
- Month 2: Start Monthly Business Review using Survival Five scorecard
- Month 6: Start Quarterly Business Review using OKR framework
- Year 2: Start Annual Planning using 8-week cycle

**Step 5: Build the unit economics dashboard**
- Define channels (paid, organic, referral, email, etc.)
- Calculate CAC, LTV, LTV:CAC, payback period per channel
- Set kill criteria per channel
- Review monthly — scale winners, kill losers

**Step 6: Run persona dialogue**
- Select 3 personas relevant to the brand's financial context
- Recommended: Skeptical Investor + Operations Expert + Growth Engineer
- Run 4-8 rounds per TWP-001 Phase 6 protocol
- Apply upgrades to content

**Step 7: Self-grade**
- Use rubric below
- Be honest — inflated grades undermine the system

**Step 8: Register**
- Create _meta.json
- Update manifest.json
- Update opkits/registry.json

---

## Grading Rubric

| Grade | Evidence Coverage | Actionability | Reusability |
|-------|------------------|---------------|-------------|
| **A (9-10)** | All financial areas covered with A/B-grade evidence. Real data from post-launch operations. Connector tested and validated. | Founder can execute from Day 0 with zero additional research. Templates are copy-paste ready. | Works for any DTC brand with minimal customization. |
| **B (7-8.9)** | Most areas at B-grade or better. Pre-launch assumptions clearly marked. Key intelligence gaps identified with validation paths. | Founder can execute from Day 0 with minor research on 2-3 items. Checklists and templates present. | Works for most DTC brands. Some product-specific details need swapping. |
| **C (5-6.9)** | Coverage adequate but gaps at D-grade. Some sections thin or generic. Confidence grades may be generous. | Founder needs significant additional research before executing. Templates are frameworks, not ready-to-use. | Requires substantial customization for different product categories. |
| **D (3-4.9)** | Major gaps. Multiple sections at D-grade or void. Danilo's shell not substantially improved. | Content informs but doesn't enable execution. No ready-to-use templates. | IonWave-specific with limited reuse potential. |
| **F (<3)** | Danilo shell unchanged or barely improved. No evidence, no sources, no confidence grades. | Not actionable. | Not reusable. |

---

## Graded Example: IonWave (Trade #84)

**Grade**: B+ (8.8/10)

**Strengths**:
- Highly actionable — Day 1 Essentials, monthly checklist, Survival Five scorecard are immediately executable
- Excellent confidence honesty — dual-margin treatment of REC-001 rather than picking sides
- Strong research grounding — web research on Shopify+QBO integration, sales tax, ASC 606, inventory accounting
- Dialogue produced 6 upgrades including critical connector testing priority elevation

**Weaknesses**:
- Pre-launch — all unit economics values are assumptions (will become A-grade post-launch)
- 3PL costs estimated, not quoted
- Connector recommendation (Synder) not yet validated with real transactions
- Annual planning section is thin (appropriately — premature for Year 1)

**What would upgrade to A**:
- Post-launch actual data replacing all D-grade assumptions
- Synder vs A2X validated with real ReCharge transactions
- 3PL costs from actual quotes
- First 3 MBRs completed and reviewed for format effectiveness

---

## Scaffold

### Bookkeeping Setup Scaffold

```markdown
# Bookkeeping & Accounting Setup — [TUP_ID]: [TUP_NAME]

## 1. Accounting Method
[Accrual / Cash — state choice and why]

## 2. Software Stack
### Primary Accounting Software
[QBO / Xero / Wave — state choice, plan, monthly cost]

### Connector
[Synder / A2X / other — test both before committing]

### Sales Tax
[Phase-gated: Shopify Tax → TaxJar → Avalara]

### Other Tools
[Table of tools with purpose, cost, and when to add]

## 3. Chart of Accounts
### Day 1 Essentials (15-20 accounts)
[Minimal set needed at launch]

### Full Chart (reference)
[Complete chart organized by: Assets, Liabilities, Equity, Revenue, COGS, OpEx]

## 4. Inventory Accounting
[FIFO/Weighted Average, landed cost calculation, journal entries, expiry handling]

## 5. Revenue Recognition
[ASC 606 treatment for subscription + one-time, journal entries, practical simplification]

## 6. Monthly Checklist
[Weekly tasks, monthly tasks, quarterly tasks, annual tasks]

## 7. Common Mistakes
[Top 10 + product-category-specific mistakes]

## 8. When to Hire
[Stage-gated: solo → bookkeeper → CPA → fractional CFO]
```

### Unit Economics Tracking Scaffold

```markdown
# Unit Economics Tracking — [TUP_ID]: [TUP_NAME]

## 1. Channel Economics Dashboard
[Table: Channel, Target CAC, Target LTV, LTV:CAC, Status]

## 2. Payback Period Analysis
[Formula, scenarios at different margin assumptions, sensitivity table]

## 3. Monthly Reporting
[What to calculate, attribution methodology, tools]

## 4. Scale/Hold/Kill Framework
[Decision rules per channel with time thresholds]
```

### Business Review Cadence Scaffold

```markdown
# Business Review Cadence — [TUP_ID]: [TUP_NAME]

## 1. Cadence Overview
[Table: Weekly/Monthly/Quarterly/Annual with duration, participants, purpose]

## 2. Weekly Cash Check (15 min)
[5-item checklist, 13-week forecast template]

## 3. Monthly Business Review (60-80 min)
[Survival Five (early stage) + Full Scorecard (growth stage), 10-section agenda, output template]

## 4. Quarterly Business Review (2-3 hours)
[Quarter review, OKR framework, resource allocation, strategic bets, risk register]

## 5. Annual Planning (8 weeks)
[Timeline, 7 plan components, Start/Stop/Continue questions]

## 6. Hypothesis Integration
[How reviews connect to hypothesis validation]
```


---

### 📄 unit_economics_tracking.md

# Unit Economics Tracking — M25: Financial Operations

**TUP**: M25
**Version**: 1.0.0
**Date**: 2026-02-06
**Author**: Caio, Claude (collaborative)
**AI Model**: claude-opus-4-6
**Status**: AI Draft
**Hypothesis Links**: HYP-001 (CAC), HYP-002 (Subscription Attach Rate), HYP-003 (Churn), HYP-004 (Gross Margin), HYP-005 (LTV)
**Danilo Source**: ops_model_v10_dump/534_unit_economics_by_channel.json (7 rows), 535_payback_period_analysis.json (8 rows)
**Cross-Reference**: M3 (Financial Model), M10 (Pricing & Offer), M13 (Media Buying), M30 (Analytics)

---

## Purpose

Define how IonWave tracks and reports unit economics by channel. This is the **measurement** system, not the **strategy** (M10 sets strategy, M3 models it, M25 tracks it). Two Danilo tabs merged here: Channel Economics (534, 7 rows — a thin CAC/LTV table) and Payback Period Analysis (535, 8 rows — a formula + example).

**Core principle**: Unit economics are the vital signs of the business. If you can't see them in real-time, you can't make real-time decisions. The goal is a dashboard that any operator can read in 5 minutes and know whether each channel is working.

---

## 1. Channel Economics Dashboard

### The Tracking Table

This table is a **reporting template**, updated monthly. The values below are **targets/assumptions** from the hypothesis system — they will be replaced with actuals post-launch.

[Confidence: D for all values — these are pre-launch assumptions. Will become A/B-grade once populated with actual data.]

| Channel | Target CAC | Target LTV | LTV:CAC | Status | Update Frequency |
|---------|-----------|-----------|---------|--------|-----------------|
| **Meta — Prospecting** | $40-45 | $106 (blended) | 2.4-2.7x | 🟡 Assumed | Weekly |
| **Meta — Retargeting** | $15-20 | $130+ | 6.5-8.7x | 🟡 Assumed | Weekly |
| **Google — Brand** | $10-15 | $130+ | 8.7-13x | 🟡 Assumed | Weekly |
| **Google — Non-Brand** | $30-40 | $106 (blended) | 2.7-3.5x | 🟡 Assumed | Monthly |
| **Influencer/Creator** | $25-35 | $120 | 3.4-4.8x | 🟡 Assumed | Monthly |
| **Organic/SEO** | $0 (time cost) | $130+ | ∞ (unpaid) | 🟡 Assumed | Monthly |
| **Referral** | $10-20 | $130+ | 6.5-13x | 🟡 Assumed | Monthly |
| **Email/SMS** | $0 (retention) | N/A (retention) | N/A | 🟡 Assumed | Weekly |

**Status key**: 🟢 Validated (actual data), 🟡 Assumed (hypothesis), 🔴 Kill zone (LTV:CAC <2.5x)

### Danilo's Original vs. What We Track

Danilo's tab 534 listed these values:

| Channel | Danilo CAC | Danilo LTV | Danilo LTV:CAC | Issue |
|---------|-----------|-----------|----------------|-------|
| Meta Prospecting | $45 | $130 | 2.9x | LTV assumes Danilo's margin, not HYP-004 |
| Meta Retargeting | $20 | $145 | 7.3x | Same |
| Google Brand | $15 | $150 | 10x | Same |
| Influencer | $30 | $140 | 4.7x | Same |
| Organic | $0 | $160 | ∞ | Same |

**Key difference**: Danilo's LTV calculations use an unexplained higher LTV. The Bootstrap hypothesis system (HYP-005) uses $106 blended LTV at 67% margin. We use the hypothesis-system values as the baseline and will validate with real data.

### How to Calculate Each Metric

**CAC (Customer Acquisition Cost):**
```
CAC = Total Channel Spend / New Customers Acquired from Channel
```
- Include: Ad spend, platform fees, influencer payments, referral credits
- Exclude: Organic content creation time (not a cash cost in early stage)
- **Source**: Meta Ads Manager, Google Ads, UTM attribution in GA4

**LTV (Customer Lifetime Value):**
```
Subscriber LTV = (AOV × Gross Margin) / Monthly Churn Rate
One-Time LTV = AOV × Gross Margin × Repeat Purchase Rate
Blended LTV = (Sub LTV × Sub %) + (One-Time LTV × One-Time %)
```
- **AOV**: Average Order Value from Shopify
- **Gross Margin**: From P&L (COGS ÷ Revenue). Target 67% one-time, 60% subscription per HYP-004/ISS-001
- **Churn**: From cohort analysis (target ≤12% per HYP-003)
- **Sub %**: From checkout data (target 50% per HYP-002)

**LTV:CAC Ratio:**
```
LTV:CAC = Blended LTV / Blended CAC
```
- **Target**: ≥3.0x (healthy)
- **Minimum viable**: 2.5x (break-even after OpEx)
- **Kill threshold**: <2.5x sustained for 60 days → investigate or kill channel

---

## 2. Payback Period Analysis

### The Formula

[Confidence: A | Source: Standard DTC unit economics formula]

```
Payback Period (months) = CAC / Monthly Gross Profit per Customer
```

Where:
```
Monthly Gross Profit = Monthly Revenue per Customer × Gross Margin
```

### Dual-Scenario Analysis

**REC-001 Margin Dispute Note**: Danilo's tab 535 uses 45% gross margin. The Bootstrap hypothesis system (HYP-004) uses 67%. The origin of Danilo's 45% is unexplained and may include fully-loaded costs beyond COGS. We present both scenarios.

#### Scenario A: Bootstrap Margin (67% — HYP-004)

[Confidence: B | Source: Biocean supplier quotes ($18-20 COGS at $59 price)]

| Customer Type | Monthly Revenue | Gross Margin | Monthly GP | CAC | Payback Period |
|--------------|----------------|-------------|------------|-----|---------------|
| **Subscriber** | $50.15 | 60% (after 15% discount) | $30.09 | $35 | **1.2 months** |
| **One-Time** | $59.00 | 67% | $39.53 | $35 | **0.9 months** (single purchase) |
| **Blended** (60/40 sub/OTP) | $53.69 | 63% | $33.82 | $35 | **1.0 months** |

#### Scenario B: Danilo Margin (45% — unexplained)

[Confidence: D | Source: Danilo tab 535. Origin of 45% is undocumented. May include fulfilment, platform fees, or other costs beyond COGS.]

| Customer Type | Monthly Revenue | Gross Margin | Monthly GP | CAC | Payback Period |
|--------------|----------------|-------------|------------|-----|---------------|
| **Subscriber** | $50.15 | 45% | $22.57 | $35 | **1.6 months** |
| **One-Time** | $59.00 | 45% | $26.55 | $35 | **1.3 months** (single purchase) |
| **Blended** (60/40 sub/OTP) | $53.69 | 45% | $24.16 | $35 | **1.4 months** |

#### Scenario C: Contribution Margin (including fulfillment + platform fees)

[Confidence: C | Source: Estimated contribution margin deducting 3PL fees (~$5/order) and payment processing (~3%)]

| Customer Type | Revenue | COGS | Fulfilment | Platform Fees | Contribution | CAC | Payback |
|--------------|---------|------|------------|--------------|-------------|-----|---------|
| **Subscriber** | $50.15 | $20.00 | $5.00 | $1.50 | $23.65 (47%) | $35 | **1.5 months** |
| **One-Time** | $59.00 | $20.00 | $5.00 | $1.77 | $32.23 (55%) | $35 | **1.1 months** |
| **Blended** | $53.69 | $20.00 | $5.00 | $1.61 | $27.08 (50%) | $35 | **1.3 months** |

**Insight**: Danilo's 45% margin may actually be closer to **contribution margin** (Scenario C at 47-50%) than gross margin. This would explain the discrepancy — Danilo included fulfilment and platform costs that Bootstrap treats as OpEx below the gross margin line.

**Resolution recommendation**: Use Scenario A (67% gross margin) for P&L reporting. Use Scenario C (contribution margin) for channel-level payback analysis. This resolves REC-001 for M25 without changing either assumption — they measure different things.

> **Which margin for which decision** *(Dialogue upgrade U1)*:
> - **Gross margin (67%)** → P&L reporting, investor reporting, HYP-004 validation
> - **Contribution margin (47-50%)** → Channel payback decisions, scale/hold/kill calls, media buying optimization
> - **Never mix them** — comparing gross margin payback from one channel to contribution margin payback from another produces nonsense

### Payback Sensitivity Table

[Confidence: B | Source: Mathematical sensitivity analysis using HYP-001 range ($30-45 CAC)]

| CAC | Contribution Margin 47% | Contribution Margin 50% | Contribution Margin 55% |
|-----|------------------------|------------------------|------------------------|
| $30 | 1.3 months | 1.1 months | 0.9 months |
| $35 | 1.5 months | 1.3 months | 1.1 months |
| $40 | 1.7 months | 1.5 months | 1.2 months |
| $45 | 1.9 months | 1.7 months | 1.4 months |

**Reading**: All scenarios show payback under 2 months — this is healthy for DTC supplement. The critical risk is not payback period but **churn**: if customers cancel before payback, the math breaks.

### Kill Criteria

| Metric | Healthy | Watch | Kill |
|--------|---------|-------|------|
| **Payback period** | <2 months | 2-3 months | >3 months |
| **LTV:CAC** | >3.0x | 2.5-3.0x | <2.5x |
| **Channel CAC** | <$40 | $40-50 | >$50 sustained |
| **Blended CAC** | <$35 | $35-42 | >$42 sustained |

---

## 3. Monthly Unit Economics Reporting

### What to Calculate Every Month

| Metric | Formula | Source | Hypothesis Link |
|--------|---------|--------|----------------|
| **Blended CAC** | Total marketing spend / new customers | Ads Manager + Shopify | HYP-001 |
| **CAC by channel** | Channel spend / channel-attributed customers | Ads Manager + UTM | HYP-001 |
| **AOV** | Total revenue / total orders | Shopify | — |
| **Subscription attach rate** | Sub orders / total orders | Shopify + ReCharge | HYP-002 |
| **Monthly churn** | Cancelled subs / active subs at month start | ReCharge | HYP-003 |
| **Gross margin** | (Revenue − COGS) / Revenue | QBO P&L | HYP-004 |
| **Contribution margin** | (Revenue − COGS − Fulfilment − Platform Fees) / Revenue | QBO + manual calc | — |
| **Blended LTV** | (Sub LTV × sub%) + (OTP LTV × otp%) | Calculated | HYP-005 |
| **LTV:CAC** | Blended LTV / Blended CAC | Calculated | HYP-005/HYP-001 |
| **Payback period** | Blended CAC / Monthly contribution | Calculated | — |
| **MRR** | Active subscribers × subscription price | ReCharge | HYP-007 |
| **Revenue per visitor** | Total revenue / unique visitors | GA4 + Shopify | — |

### Attribution Methodology

**Primary**: UTM-based last-click attribution (GA4)
- Every ad, email, and social link gets UTM parameters per M16 (Content & SEO) UTM discipline
- `utm_source` = platform, `utm_medium` = type, `utm_campaign` = campaign_id

**Secondary**: Post-purchase survey ("How did you hear about us?")
- Captures word-of-mouth and offline channels that UTM misses
- Required for HYP-006 (Organic/Referral Lift) validation

**Limitation**: Multi-touch attribution is aspirational for early stage. Start with last-click, add incrementality testing at $10K+/month ad spend.

**First-click vs last-click** *(Dialogue upgrade U6)*: Use last-click for tactical ad optimization (what Meta/Google report natively). Use post-purchase survey for strategic channel allocation — this captures first-touch awareness channels that last-click misses (e.g., someone discovers IonWave via TikTok but converts via Google brand search).

[Confidence: C | Source: Standard DTC attribution methodology. Last-click undercounts awareness channels but is the simplest starting point.]

---

## 4. When to Scale, Hold, or Kill a Channel

### Decision Framework

[Confidence: B | Source: Standard DTC channel optimization framework]

```
Monthly channel review:

IF LTV:CAC > 3.0x AND payback < 2 months:
  → SCALE: Increase budget 20-30% next month

IF LTV:CAC 2.5-3.0x AND payback < 3 months:
  → HOLD: Optimize creative/targeting before scaling

IF LTV:CAC < 2.5x for 30 days:
  → WATCH: Reduce to test budget, diagnose (creative fatigue? audience exhaustion? attribution error?)

IF LTV:CAC < 2.5x for 60 days:
  → KILL: Pause channel. Reallocate budget to performing channels.
```

**Exception**: Brand-new channels get a 30-day learning period before applying kill criteria. Meta algorithm needs ~50 conversions to optimize.

---

## Intelligence Gaps

| Gap | Priority | Validation Path | Current Grade |
|-----|----------|----------------|---------------|
| REC-001 margin dispute resolution (are Danilo's figures contribution margin?) | HIGH | Ask Danilo for the calculation behind 45% | D |
| Attribution accuracy with iOS privacy changes | MEDIUM | Test Meta Conversions API + server-side tracking setup | C |
| Actual fulfillment cost per order (3PL quotes needed) | HIGH | Get quotes from ShipBob, Fulfil, or other 3PLs | D |
| Multi-touch attribution tool (Triple Whale, Northbeam, etc.) | LOW | Evaluate at $10K+/mo ad spend | D |


---

## 🔗 Dependencies & Relationships

### Feeds Into
- m3
- m30
- m35

### Requires
- m0

---

## ⚠️ Intelligence Gaps

- **Synder vs A2X real-world performance with ReCharge subscriptions**
  - Priority: CRITICAL
- **REC-001 margin dispute origin (is Danilo's 45% contribution margin?)**
  - Priority: HIGH
- **Actual 3PL fulfillment cost per order**
  - Priority: HIGH
- **Multi-touch attribution tool selection**
  - Priority: LOW

---

## 🎯 Next Actions

Pre-launch: test Synder vs A2X with ReCharge sample transactions. Get 3PL cost quotes. Set up QBO with Day 1 Essentials chart of accounts.

### Key Blockers
- REC-001 margin dispute (45% vs 67%) — treated as dual scenario, not resolved

---

## 🧰 OpKits

- OK-M25-001

---

---

_Report generated: 2026-02-09 17:49:45_

_Source: `data\m25`_