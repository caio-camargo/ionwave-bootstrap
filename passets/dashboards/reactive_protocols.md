# Reactive Protocols — IonWave Operational Response Procedures

**Version**: 1.0.0
**Created**: 2026-02-12
**Purpose**: Standardized responses when controllers detect metric deviations
**Source**: controller_registry.md + Systems_Architecture_Standards.md
**Owner Role**: Operator (executes), CM (oversees), MSO (tunes)

---

## Overview

**Reactive Protocols** are triggered automatically when Controllers detect that a metric has exceeded its parameter tolerance. They are the "Act" step in the controller loop:

```
Controller Detects Deviation → Reactive Protocol Executes → System Returns to Green
```

Every Reactive Protocol follows a standard structure:
- **ID**: Unique identifier (RP-001, RP-002, etc.)
- **Trigger**: Which controller calls it, what threshold crossed
- **Owner**: Who executes (Operator, Media Buyer, etc.)
- **Urgency**: P0 (CRITICAL - immediate), P1 (urgent - same day), P2 (important - within 24 hrs)
- **Steps**: Ordered diagnostic and corrective actions
- **Success Criteria**: How to know when to exit protocol
- **Escalation**: When to alert CM / Studio 3 / Venture Partner
- **Logging**: What to document for Meta-Control learning

---

## Revenue & Growth Reactive Protocols

### RP-001: Revenue Recovery Protocol

**Trigger**: C-001 (Revenue Deviation Controller) detects revenue <-30% vs 7-day avg OR <$100 absolute
**Owner**: Operator
**Urgency**: P1 (Urgent - investigate within 2 hours)

**Steps**:

1. **Verify Data Integrity** (5 min)
   - [ ] Check Shopify dashboard: Does revenue match daily_pulse.md?
   - [ ] Check for sync errors: Did Google Apps Script fail?
   - [ ] If data error: Fix sync, re-run controller, exit protocol

2. **Diagnostic Checklist** (10 min)
   - [ ] **Site availability**: Is website up? (check ispwn.com or UptimeRobot)
   - [ ] **Payment processor**: Stripe/PayPal accepting payments?
   - [ ] **Ad spend**: Did ads stop running? (check Meta Ads Manager)
   - [ ] **Product availability**: Is product showing "out of stock"?
   - [ ] **Pricing error**: Did product price change accidentally?

3. **Identify Root Cause** (10 min)
   Based on diagnostic, determine primary issue:
   - **Site down** → Escalate to tech support (hosting provider)
   - **Payment processor issue** → Contact Stripe/PayPal support immediately
   - **Ad spend paused** → Investigate why (budget cap? account issue? see RP-005)
   - **Stockout** → See RP-015 (Stockout Prevention)
   - **No obvious cause** → Proceed to Step 4

4. **Traffic Analysis** (15 min)
   - [ ] Check Google Analytics: Sessions vs yesterday, vs 7-day avg
   - [ ] Check Meta Ads: Impressions, clicks vs baseline
   - [ ] Check email performance: Recent campaign underperform?
   - [ ] Hypothesis: Traffic dropped OR conversion rate dropped

5. **Conversion Funnel Check** (10 min)
   - [ ] Shopify Analytics → Conversion rate: Today vs 7-day avg
   - [ ] Add-to-cart rate: Normal or declining?
   - [ ] Checkout abandonment: Spike vs normal?
   - [ ] If conversion rate dropped >20%: Likely site UX issue or payment processor

6. **Corrective Actions**
   Based on root cause:
   - **Site issue**: Fix immediately, alert customers via email/social
   - **Payment issue**: Switch to backup processor OR alert customers
   - **Traffic issue**: See RP-005 (ROAS Recovery) or RP-009 (Audience Expansion)
   - **Conversion issue**: Review recent site changes, A/B test checkout flow

7. **Document & Report**
   - [ ] Log root cause in `/passets/dashboards/controller_logs/RP-001-[date].md`
   - [ ] Update daily_pulse.md "One Thing to Fix Today"
   - [ ] If revenue recovers next day: Exit protocol, mark resolved
   - [ ] If revenue stays low 2+ days: Escalate to CM

**Success Criteria**: Revenue returns to >-15% vs 7-day avg for 2 consecutive days

**Escalation Triggers**:
- Revenue <$100 for 2+ consecutive days → Alert CM + Studio 3 (business model failure signal)
- Root cause requires tech expertise beyond operator → Escalate to tech vendor
- Root cause unknown after 2 hours → Request CM support

**Logging**: Document in controller_logs/ folder with root cause, corrective action, time to resolution

---

### RP-002: Order Volume Investigation Protocol

**Trigger**: C-002 (Order Volume Controller) detects orders <-30% vs 7-day avg OR <5 orders/day
**Owner**: Operator
**Urgency**: P1

**Steps**:

1. **Cross-Check Revenue** (2 min)
   - [ ] Is revenue also down? (see RP-001 if yes)
   - [ ] Is AOV unusually high? (fewer orders but larger basket = okay)
   - [ ] If revenue normal but orders low: Bulk order or multi-unit purchases

2. **Order Composition Analysis** (10 min)
   - [ ] Shopify: Check recent orders for patterns
   - [ ] Are orders mostly 2-packs or 3-packs? (drives down order count, up AOV)
   - [ ] Are orders mostly single units? (normal pattern)
   - [ ] Unusual: Large wholesale/B2B order? (1 order = $500+)

3. **Traffic vs Conversion** (10 min)
   - [ ] Google Analytics: Sessions down?
   - [ ] Shopify: Conversion rate down?
   - [ ] Identify: Traffic issue (see RP-005, RP-009) OR conversion issue

4. **Corrective Actions**
   - **Bulk order anomaly**: Flag as one-time event, no action
   - **Traffic down**: See RP-005 (ROAS Recovery) or RP-009 (Audience Expansion)
   - **Conversion down**: Review checkout flow, payment options, shipping costs

**Success Criteria**: Order volume returns to >-15% vs 7-day avg

**Escalation**: If orders <5/day for 3+ consecutive days → Alert CM (acquisition funnel broken)

---

### RP-003: Acquisition Funnel Diagnostic

**Trigger**: C-003 (New Customer Acquisition Controller) detects new customers <-30% vs 7-day avg OR <3/day
**Owner**: Operator + Media Buyer
**Urgency**: P1

**Steps**:

1. **Verify New vs Repeat Split** (5 min)
   - [ ] Shopify: What % of orders are from new customers?
   - [ ] Baseline: 60-70% new, 30-40% repeat (healthy DTC mix)
   - [ ] If new customer % dropped: Acquisition issue (proceed)
   - [ ] If new customer % normal: Order volume issue (see RP-002)

2. **Ad Performance Check** (10 min)
   - [ ] Meta Ads Manager: Click volume vs baseline
   - [ ] CTR: Normal or declining? (see RP-008 if declining)
   - [ ] CPA: Spiking? (see RP-007 if yes)
   - [ ] Hypothesis: Ad funnel broken (low CTR, high CPA, low conversions)

3. **Landing Page Analysis** (10 min)
   - [ ] Google Analytics: Landing page bounce rate
   - [ ] Time on page: Normal or declining?
   - [ ] Hypothesis: Landing page underperforming (poor UX, slow load, messaging mismatch)

4. **Corrective Actions**
   - **Ad issue**: See RP-005 (ROAS Recovery), RP-008 (Creative Fatigue), RP-009 (Audience Expansion)
   - **Landing page issue**: A/B test new headlines, images, CTAs
   - **Offer issue**: Test discount code, free shipping threshold, bundle deals

**Success Criteria**: New customer acquisition returns to >-15% vs 7-day avg

**Escalation**: If new customers <3/day for 5+ consecutive days → Alert CM + Studio 3 (growth stalled)

---

### RP-004: AOV Structural Analysis

**Trigger**: C-004 (AOV Controller) detects AOV <$35 OR >$55
**Owner**: Operator
**Urgency**: P2

**Steps**:

1. **Identify Direction** (2 min)
   - [ ] AOV too low (<$35): Discount abuse or pricing error
   - [ ] AOV too high (>$55): Bulk orders or cart manipulation

2. **Low AOV Diagnostic** (if <$35)
   - [ ] Check discount codes: Any codes giving >20% off?
   - [ ] Check product pricing: Did price accidentally change to <$30?
   - [ ] Check order composition: Are customers only buying single units at discount?
   - [ ] **Corrective action**: Disable excessive discount codes, fix pricing errors

3. **High AOV Diagnostic** (if >$55)
   - [ ] Check recent orders: Are there bulk/wholesale orders?
   - [ ] Check cart: Are customers stacking 3+ units?
   - [ ] **Assessment**: High AOV is typically good (flag as positive anomaly, no action)

**Success Criteria**: AOV returns to $37-51 range (green band)

**Escalation**: If AOV <$30 for 3+ days → Pricing model broken, alert CM

---

## Ad Performance Reactive Protocols

### RP-005: ROAS Recovery Protocol

**Trigger**: C-005 (ROAS Controller) detects ROAS <1.5x for 1-2 consecutive days
**Owner**: Media Buyer (or Operator if pre-hire)
**Urgency**: P0 (CRITICAL if 2+ days, P1 if 1 day)

**Steps**:

1. **Immediate Diagnostic** (10 min)
   - [ ] Meta Ads Manager: Which campaigns underperforming?
   - [ ] Check: CTR declining? (creative fatigue, see RP-008)
   - [ ] Check: CPA spiking? (audience saturation, see RP-007)
   - [ ] Check: Ad frequency >5? (audience fatigue, see RP-009)

2. **Campaign-Level Analysis** (15 min)
   - [ ] Sort campaigns by ROAS (best to worst)
   - [ ] Identify: Which campaigns are <1.5x ROAS?
   - [ ] Identify: Which campaigns are >2.5x ROAS? (working creatives/audiences)
   - [ ] Action: Pause underperforming campaigns, increase budget on winners

3. **Creative Performance Review** (15 min)
   - [ ] Meta Ads Manager: Sort ads by ROAS
   - [ ] Identify: Which creatives are <1.5x ROAS?
   - [ ] Check: Are top creatives >7 days old? (creative fatigue risk)
   - [ ] Action: Pause poor performers, launch 3 new creative angles (see M12 creative playbook)

4. **Audience Analysis** (15 min)
   - [ ] Check: Are winning audiences from Day 1-7 still performing?
   - [ ] Check: Ad frequency per audience segment
   - [ ] Hypothesis: Audience saturation if frequency >5 + ROAS declining
   - [ ] Action: Expand targeting (see RP-009)

5. **Corrective Actions Priority**
   - **First 2 hours**: Pause bottom 30% of campaigns by ROAS
   - **Next 4 hours**: Launch 3 new creative angles (hooks, formats, offers)
   - **Next 24 hours**: Expand audiences (lookalikes, interests, cold prospecting)
   - **Target**: Return to ROAS >2.0x within 72 hours

**Success Criteria**: ROAS >2.0x for 2 consecutive days

**Escalation Triggers**:
- ROAS <1.5x for 3 consecutive days → Trigger RP-006 (Ad Spend Pause - CRITICAL)
- ROAS <1.0x (losing money) → Immediately reduce ad spend 50%, alert CM

**Logging**: Document which campaigns paused, which creatives launched, audience changes

---

### RP-006: Ad Spend Pause Protocol (CRITICAL)

**Trigger**: C-005 (ROAS Controller) detects ROAS <1.5x for 3+ consecutive days
**Owner**: Operator (executes), CM + Studio 3 (approve)
**Urgency**: P0 (CRITICAL - execute within 1 hour)

**Steps**:

1. **Immediate Spend Reduction** (15 min)
   - [ ] Meta Ads Manager: Reduce daily budget by 80% (e.g., $500/day → $100/day)
   - [ ] Keep only top-performing campaigns (ROAS >2.5x)
   - [ ] Pause all campaigns with ROAS <2.0x
   - [ ] **Rationale**: Stop burning cash while diagnosing root cause

2. **Emergency Diagnostic** (30 min)
   - [ ] Run RP-005 (ROAS Recovery) full diagnostic
   - [ ] Hypothesis: Creative fatigue + audience saturation + landing page issue?
   - [ ] Identify: Is this fixable in 7 days? Or structural business model issue?

3. **Recovery Plan** (60 min)
   - [ ] If fixable: Document 7-day recovery plan (new creatives, audiences, landing pages)
   - [ ] If structural: Alert CM + Studio 3 for business model review (see RP-013)

4. **CM/Studio 3 Approval**
   - [ ] Present recovery plan to CM
   - [ ] Decision: Execute recovery OR pause ads entirely for 14 days (creative rebuild)

5. **Execute Recovery** (7 days)
   - [ ] Day 1-2: Build 10 new creative angles (see M12)
   - [ ] Day 3-4: Launch new creatives at $50/day budget per angle
   - [ ] Day 5-7: Scale winners, kill losers, target ROAS >2.0x

**Success Criteria**: ROAS >2.0x sustained for 5 consecutive days → Resume normal ad spend

**Escalation**: If ROAS doesn't recover after 7 days → Trigger RP-013 (Business Model Review)

**Logging**: Full diagnostic report + recovery plan + daily ROAS tracking during recovery period

---

### RP-007: CPA Optimization Protocol

**Trigger**: C-006 (CPA Controller) detects CPA >$60
**Owner**: Media Buyer
**Urgency**: P1

**Steps**:

1. **Campaign Segmentation** (10 min)
   - [ ] Meta Ads Manager: Sort campaigns by CPA (low to high)
   - [ ] Identify: Which campaigns have CPA >$60?
   - [ ] Action: Pause campaigns with CPA >$75 immediately

2. **Conversion Rate Analysis** (15 min)
   - [ ] Shopify: Landing page conversion rate vs baseline
   - [ ] Hypothesis: CPA spike = traffic quality down OR landing page broken
   - [ ] If conversion rate normal: Traffic quality issue (see Step 3)
   - [ ] If conversion rate down: Landing page issue (see Step 4)

3. **Traffic Quality Diagnostic** (if conversion rate normal)
   - [ ] Meta Ads: Check audience targeting (too broad? wrong interests?)
   - [ ] Check ad placements: Are ads showing on low-quality placements (Audience Network)?
   - [ ] Action: Tighten targeting, exclude Audience Network, focus on Feed + Stories

4. **Landing Page Diagnostic** (if conversion rate down)
   - [ ] Google Analytics: Bounce rate, time on page
   - [ ] Test: Is checkout flow working? (place test order)
   - [ ] Check: Did shipping costs increase? Payment options removed?
   - [ ] Action: Fix UX issues, A/B test new headlines, simplify checkout

**Success Criteria**: CPA <$50 for 3 consecutive days

**Escalation**: If CPA >$75 for 5+ days → Pause ads, trigger RP-006 (Ad Spend Pause)

---

### RP-008: Creative Fatigue Protocol

**Trigger**: C-007 (CTR Controller) detects CTR <0.5% for 3 consecutive days
**Owner**: Media Buyer + Creative team
**Urgency**: P1

**Steps**:

1. **Creative Performance Audit** (15 min)
   - [ ] Meta Ads Manager: Sort ads by CTR (high to low)
   - [ ] Identify: Which creatives have CTR <0.5%?
   - [ ] Check: How long have these creatives been running? (>14 days = fatigue likely)
   - [ ] Action: Pause all creatives with CTR <0.6% AND age >14 days

2. **Creative Refresh Plan** (2 hours)
   - [ ] Review M12 (Ad Creative Playbook) for new angles
   - [ ] Brainstorm: 5 new hooks (e.g., "Feel the difference in 20 minutes")
   - [ ] Format: Test new formats (UGC video, carousel, static image)
   - [ ] Action: Produce 10 new creative variants (5 hooks × 2 formats)

3. **Rapid Testing** (48 hours)
   - [ ] Launch 10 new creatives at $20/day budget each
   - [ ] Monitor: CTR after 24 hours, 48 hours
   - [ ] Kill: Creatives with CTR <0.7% after 48 hours
   - [ ] Scale: Creatives with CTR >1.2% (increase to $50/day)

4. **Audience Consideration**
   - [ ] If CTR low across ALL creatives: Audience issue (see RP-009)
   - [ ] If only some creatives low CTR: Creative issue (normal fatigue)

**Success Criteria**: Portfolio CTR >0.8% with at least 3 creatives >1.0% CTR

**Escalation**: If CTR <0.5% persists after creative refresh → Audience saturation (RP-009)

---

### RP-009: Audience Expansion Protocol

**Trigger**: C-008 (Ad Frequency Controller) detects frequency >5 for 3+ consecutive days
**Owner**: Media Buyer
**Urgency**: P1

**Steps**:

1. **Audience Saturation Diagnosis** (10 min)
   - [ ] Meta Ads Manager: Check frequency per campaign
   - [ ] Check: Are high-frequency campaigns also declining ROAS?
   - [ ] Check: Are high-frequency campaigns also declining CTR?
   - [ ] Hypothesis: Audience seeing ads too often → fatigue → poor performance

2. **Immediate Audience Rotation** (30 min)
   - [ ] Pause campaigns with frequency >6
   - [ ] Duplicate campaigns with new audiences:
     - Lookalike audiences (1%, 2%, 3% from customer list)
     - Interest expansion (related supplements, keto, fasting, performance)
     - Cold prospecting (broad targeting, 25-55 age)
   - [ ] Launch 3 new audience campaigns at $50/day each

3. **Creative Refresh for New Audiences** (2 hours)
   - [ ] Tailor creatives to new audiences:
     - Lookalikes: Testimonials, social proof ("Join 10,000+ customers")
     - Interest expansion: Educational content ("Why electrolytes matter for keto")
     - Cold prospecting: Strong hooks, problem-solution format
   - [ ] Action: Produce 6 new creatives (2 per audience type)

4. **Scaling Logic** (7 days)
   - [ ] Day 1-3: Test new audiences at $50/day
   - [ ] Day 4-5: Scale winners (ROAS >2.5x, CTR >1.0%) to $100/day
   - [ ] Day 6-7: Kill losers (ROAS <2.0x, CTR <0.7%)
   - [ ] Target: 50% of spend on new audiences by Day 7

**Success Criteria**: Average frequency <4 AND ROAS >2.5x across portfolio

**Escalation**: If audience expansion doesn't improve ROAS → Landing page issue (RP-005) or business model issue (RP-013)

---

## Cash & Runway Reactive Protocols

### RP-010: Cash Crisis Protocol

**Trigger**: C-009 (Cash Runway Controller) detects runway <30 days
**Owner**: Operator + CM + Studio 3
**Urgency**: P0 (CRITICAL - immediate action)

**Steps**:

1. **Emergency Cash Flow Review** (1 hour)
   - [ ] List all expenses: Fixed (payroll, tools, rent) vs variable (ad spend, inventory)
   - [ ] List all revenue sources: Product sales, any receivables, credit lines
   - [ ] Calculate: How to extend runway from 30 days to 60 days?

2. **Immediate Expense Cuts** (Decision within 24 hours)
   - [ ] **Ad spend**: Reduce by 50% immediately (unless ROAS >3.0x)
   - [ ] **Contractors**: Defer non-critical work, reduce hours by 30%
   - [ ] **Tools/subscriptions**: Cancel non-essential (keep Shopify, Meta, bank)
   - [ ] **Inventory**: Pause next order if >30 days supply on hand
   - [ ] Target: Reduce burn rate by 40%

3. **Revenue Acceleration** (Parallel track)
   - [ ] **Discounts**: Run 20% off sale (increase conversion rate, liquidate inventory)
   - [ ] **Email**: 3 email blasts to customer list (reactivation campaign)
   - [ ] **Upsells**: Add cross-sells, bundles at checkout
   - [ ] Target: Increase revenue by 30% in next 14 days

4. **Fundraising Plan** (3-5 days)
   - [ ] Update financial model: New burn rate, new revenue forecast
   - [ ] Calculate: How much to raise? (6 months runway minimum)
   - [ ] Outreach: Existing investors, Venture Partner network
   - [ ] Target: Term sheet within 30 days

5. **CM + Studio 3 Decision Point** (72 hours)
   - [ ] If runway extends to 45+ days via cuts + revenue acceleration: Continue operating
   - [ ] If runway still <30 days after actions: Decision to wind down OR emergency fundraise

**Success Criteria**: Runway >45 days within 14 days

**Escalation Triggers**:
- Runway <14 days → Trigger RP-011 (Existential Cash Protocol)
- Unable to cut expenses OR accelerate revenue → Wind-down discussion with Studio 3

**Logging**: Daily cash balance tracking, expense cuts documented, revenue actions tracked

---

### RP-011: Existential Cash Protocol (CRITICAL)

**Trigger**: C-009 detects runway <14 days
**Owner**: Studio 3 + Venture Partner (decision authority), Operator (executor)
**Urgency**: P0 (EXISTENTIAL - decision within 48 hours)

**Steps**:

1. **Emergency Meeting** (Within 24 hours)
   - [ ] Attendees: Operator, CM, Studio 3, Venture Partner
   - [ ] Agenda: Cash status, options, decision

2. **Option Analysis** (2 hours)
   - [ ] **Option A: Emergency Fundraise**
     - Source: Bridge round from existing investors, personal loans, credit line
     - Amount: $50K minimum (90 days runway)
     - Timeline: 7 days to close
     - Likelihood: [Assess]
   - [ ] **Option B: Fire Sale**
     - Liquidate inventory at cost (20-30% off)
     - Suspend ad spend, reduce to skeleton crew
     - Extend runway to 45 days, attempt slow-burn profitability
   - [ ] **Option C: Wind Down**
     - Refund customers, sell remaining inventory
     - Pay creditors, close entity
     - Operator transitions out, learnings documented

3. **Decision** (Studio 3 + VP authority)
   - [ ] Unanimous decision required
   - [ ] If Option A: Execute emergency fundraise (7-day timeline)
   - [ ] If Option B: Execute fire sale + slow-burn pivot
   - [ ] If Option C: Execute orderly wind-down (30-day timeline)

4. **Execution** (Per chosen option)
   - [ ] Document decision in `/passets/decisions/decision_log.md`
   - [ ] Communicate to team, customers, investors (as appropriate)
   - [ ] Execute chosen path with daily check-ins

**Success Criteria**: If Option A/B → Runway >60 days. If Option C → Orderly wind-down complete.

**Logging**: Full decision rationale, stakeholder communications, daily progress updates

---

### RP-012: Burn Rate Audit Protocol

**Trigger**: C-010 (Burn Rate Controller) detects burn >+30% vs baseline
**Owner**: Operator
**Urgency**: P2

**Steps**:

1. **Expense Breakdown** (30 min)
   - [ ] Bank statement: Categorize all expenses (ad spend, tools, payroll, inventory, misc)
   - [ ] Compare: This week vs baseline week (when burn was normal)
   - [ ] Identify: Which category spiked?

2. **Spike Investigation** (30 min)
   - [ ] **Ad spend spike**: Intentional scale? Or accidental (budget cap removed)?
   - [ ] **Payroll spike**: Contractor overages? Bonus paid?
   - [ ] **Inventory spike**: Reorder paid early?
   - [ ] **Tools spike**: New subscription added?
   - [ ] **Misc spike**: One-time expense (legal, accounting)?

3. **Corrective Action**
   - [ ] If intentional (planned scale): Update burn baseline, no action
   - [ ] If unintentional: Reverse change, return to baseline
   - [ ] If one-time: Flag as non-recurring, monitor next week

**Success Criteria**: Burn rate returns to ±15% of baseline

**Escalation**: If burn spike is recurring (3+ weeks) → Update baseline OR cut expenses

---

## Operations Reactive Protocols

### RP-013: Business Model Review Protocol

**Trigger**: C-011 (MER Controller) detects MER <1.8x for 2+ consecutive weeks
**Owner**: Operator + CM + Studio 3
**Urgency**: P0 (CRITICAL - business model viability in question)

**Steps**:

1. **Unit Economics Deep Dive** (4 hours)
   - [ ] Review M3 (Unit Economics) assumptions
   - [ ] Calculate: Current CAC, LTV, gross margin, MER
   - [ ] Compare: Actual vs model (where are gaps?)

2. **Root Cause Analysis**
   - [ ] **CAC too high**: Ad performance poor (ROAS <2.0x sustained)
   - [ ] **LTV too low**: Repeat purchase rate below model (30% assumed, actual <20%)
   - [ ] **Gross margin eroded**: Product cost increased, shipping cost increased
   - [ ] **Organic revenue declining**: SEO/email/referral not scaling as expected

3. **Scenario Modeling** (2 hours)
   - [ ] Scenario A: Fix CAC (improve ROAS to 2.5x) → What MER?
   - [ ] Scenario B: Fix LTV (increase repeat rate to 40%) → What MER?
   - [ ] Scenario C: Increase price (from $40 to $45) → What MER?
   - [ ] Identify: Which lever(s) can realistically move?

4. **Decision Point** (Studio 3 authority)
   - [ ] If fixable via operational improvements (better ads, better retention): Execute 30-day sprint
   - [ ] If fixable via pricing change: Test price increase (A/B test)
   - [ ] If not fixable: Consider pivot (new product, new market) or wind-down

5. **30-Day Sprint** (if fixable)
   - [ ] Focus: Fix highest-impact lever (CAC OR LTV OR margin)
   - [ ] Weekly check-ins: MER trending toward 2.5x?
   - [ ] Day 30: Re-assess, continue OR pivot

**Success Criteria**: MER >2.0x sustained for 4 consecutive weeks

**Escalation**: If MER <1.8x after 30-day sprint → Wind-down discussion (see RP-011 Option C)

**Logging**: Full unit economics analysis, scenario models, decision rationale, weekly MER tracking

---

### RP-014: Emergency Reorder Protocol

**Trigger**: C-012 (Inventory Controller) detects <7 days inventory remaining
**Owner**: Operator + Supply Chain coordinator
**Urgency**: P1 (Urgent - place order within 24 hours)

**Steps**:

1. **Inventory Verification** (15 min)
   - [ ] 3PL dashboard: Confirm current inventory units
   - [ ] Calculate: Sell-through rate (7-day avg orders/day)
   - [ ] Confirm: Days remaining = units / sell-through rate

2. **Supplier Contact** (30 min)
   - [ ] Email + call supplier: Request expedited production
   - [ ] Ask: Can we reduce lead time from 35 days to 21 days? (extra cost?)
   - [ ] Ask: Can we split order? (partial shipment in 14 days, rest in 35 days?)

3. **Order Placement** (1 hour)
   - [ ] Order quantity: 90 days supply (based on current sell-through + 20% buffer)
   - [ ] Example: 30 units/day sell-through × 90 days = 2,700 units
   - [ ] Payment: Wire transfer (faster than ACH)
   - [ ] Shipping: Air freight if <14 days inventory (expensive but necessary)

4. **Ad Spend Modulation** (Parallel track)
   - [ ] If inventory <5 days: Reduce ad spend by 50% (slow sales until restock)
   - [ ] If inventory <3 days: Pause ad spend entirely (see RP-015)

5. **Customer Communication**
   - [ ] If stockout likely: Add "Pre-Order" option to site (ships in 21-35 days)
   - [ ] Email list: "Limited stock - order now OR pre-order for next batch"

**Success Criteria**: Order placed, delivery ETA confirmed, inventory >14 days within 30 days

**Escalation**: If inventory <3 days → Trigger RP-015 (Stockout Prevention - CRITICAL)

**Logging**: Supplier communication, order details, delivery tracking

---

### RP-015: Stockout Prevention Protocol (CRITICAL)

**Trigger**: C-012 detects <3 days inventory remaining
**Owner**: Operator
**Urgency**: P0 (CRITICAL - immediate action)

**Steps**:

1. **Immediate Ad Spend Pause** (15 min)
   - [ ] Meta Ads Manager: Pause all campaigns immediately
   - [ ] Rationale: Preserve inventory for existing traffic (organic, email)
   - [ ] Exception: Keep retargeting ads running (for cart abandoners)

2. **Website Updates** (30 min)
   - [ ] Add banner: "Low stock - order now or join waitlist"
   - [ ] Product page: Add "Only X units left" urgency messaging
   - [ ] Checkout: Remove discount codes (maximize margin on final units)

3. **Waitlist Setup** (1 hour)
   - [ ] Add Shopify app: Waitlist (e.g., Back in Stock app)
   - [ ] Email capture: "Get notified when we restock"
   - [ ] Rationale: Capture demand during stockout period

4. **Emergency Supplier Escalation** (Same day)
   - [ ] Execute RP-014 (Emergency Reorder) if not already done
   - [ ] Request: Air freight (7-10 day delivery vs 14-21 day ocean)
   - [ ] Cost: ~3x normal shipping, but avoids lost revenue

5. **Customer Communication** (24 hours)
   - [ ] Email customers who attempted to order: "We're out of stock, here's waitlist link"
   - [ ] Social media: "Huge demand! Restocking in 14 days, join waitlist"
   - [ ] Transparency: "Overwhelmed by your support, working to restock ASAP"

6. **Revenue Contingency**
   - [ ] If stockout >7 days: Consider running ads for pre-orders (ships in 21-35 days)
   - [ ] Discount: 10% off pre-orders (incentive to wait)
   - [ ] Cash flow: Pre-order revenue helps fund restock order

**Success Criteria**: Inventory restocked, ad spend resumed, waitlist converted

**Escalation**: If stockout >14 days → Revenue impact, alert CM + Studio 3 (supply chain failure)

**Logging**: Stockout duration, waitlist signups, pre-order revenue, customer feedback

---

## Meta-Control: Reactive Protocol Performance Review

**Frequency**: Quarterly (or after 10+ triggers of any protocol)

**Process**:

1. **Trigger Log Analysis** (CM + MSO)
   - [ ] Review: How many times did each protocol trigger?
   - [ ] Review: What was average time to resolution?
   - [ ] Review: What was success rate (resolved vs escalated)?

2. **Operator Feedback** (Survey after each protocol execution)
   - [ ] "Was this protocol helpful? (Yes / No)"
   - [ ] "What steps were unclear or missing?"
   - [ ] "What would improve this protocol?"

3. **Pattern Detection**
   - [ ] If RP-X triggers >5 times/quarter: Systemic issue OR parameter too tight
   - [ ] If RP-X never triggers: Parameter too loose OR controller not needed
   - [ ] If RP-X triggers but doesn't resolve: Protocol ineffective, needs revision

4. **Protocol Updates** (MSO authority)
   - [ ] Add steps based on operator feedback
   - [ ] Remove redundant steps
   - [ ] Adjust escalation triggers
   - [ ] Update success criteria
   - [ ] Version update in this document

**Output**: Updated reactive_protocols.md with improved procedures

---

## Version History

**v1.0.0 (2026-02-12)**:
- Initial reactive protocol suite
- 15 protocols defined (RP-001 through RP-015)
- Structured format: Trigger, Owner, Urgency, Steps, Success Criteria, Escalation, Logging
- Linked to controllers (C-001 through C-012)
- Meta-control review process established

---

## Related Documents

- **Controllers**: `/passets/dashboards/controller_registry.md` (triggers these protocols)
- **Parameters**: `/passets/dashboards/parameter_registry.md` (defines thresholds that trigger protocols)
- **Dashboard**: `/passets/dashboards/daily_pulse.md` (displays controller status)
- **M3 Unit Economics**: `/data/m3/unit_economics.md` (source of viability thresholds)
- **M12 Creative Playbook**: `/data/m12/` (referenced in RP-008 Creative Fatigue)
