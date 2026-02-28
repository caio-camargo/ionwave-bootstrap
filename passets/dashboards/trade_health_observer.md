# Trade Health Observer (OBS-001)

**Version**: 1.0.0
**Created**: 2026-02-12
**Type**: Continuous Observer (Weekly calculation)
**Purpose**: Portfolio-level composite health assessment for Live Trades
**Source**: Sprint_STAGE_5 Trade Health Formula
**Owner Role**: CM (monitors), GM (strategic decisions), MSO (tunes weights)

---

## Overview

The **Trade Health Observer** aggregates 7 operational signals into a single composite health score. This provides a **portfolio-level view** of Trade vitality for GM oversight, distinct from the **operational-level controllers** (C-001 through C-012) used by the operator.

**Original Formula** (Sprint_STAGE_5):
```
H = 5M + 4U + 3L + 2R - X(f+c+r)
```

**Problem**: Components (M, U, L, R, f, c, r) were conceptual, not operationalized.

**Solution**: Define each component as a **normalized 0-10 metric** with clear calculation method.

---

## Input Signals (7 Metrics)

### Positive Signals (Higher = Healthier)

#### M: Margin Stability (Weight: 5)
**What it measures**: Gross margin consistency over time

**Calculation**:
```
gross_margin = (revenue - COGS) / revenue
margin_trend = (current_month_margin - 3_month_avg_margin) / 3_month_avg_margin

IF gross_margin >= 0.60 AND margin_trend >= 0:
  M = 10 (Stable, high margin)
ELIF gross_margin >= 0.50 AND margin_trend >= -0.05:
  M = 8 (Healthy margin, slight decline acceptable)
ELIF gross_margin >= 0.40 AND margin_trend >= -0.10:
  M = 6 (Acceptable margin, watch decline)
ELIF gross_margin >= 0.30 AND margin_trend >= -0.15:
  M = 4 (Low margin, concerning decline)
ELIF gross_margin >= 0.20:
  M = 2 (Critical margin)
ELSE:
  M = 0 (Margin collapse)
```

**Data Sources**:
- Revenue: Shopify Admin API
- COGS: Manual entry (product cost + shipping + 3PL fees)

**IonWave Targets**:
- Target gross margin: 67% (from M3 unit economics)
- COGS breakdown: Product 30%, Shipping 15%, 3PL 5%, Payment processing 3%

---

#### U: Unit Economics (Weight: 4)
**What it measures**: CAC vs LTV health

**Calculation**:
```
CAC = total_ad_spend_90days / new_customers_90days
LTV = AOV × avg_orders_per_customer × gross_margin
LTV_CAC_ratio = LTV / CAC

IF LTV_CAC_ratio >= 3.0:
  U = 10 (Excellent unit economics)
ELIF LTV_CAC_ratio >= 2.5:
  U = 8 (Healthy unit economics)
ELIF LTV_CAC_ratio >= 2.0:
  U = 6 (Acceptable, but tight)
ELIF LTV_CAC_ratio >= 1.5:
  U = 4 (Unsustainable long-term)
ELIF LTV_CAC_ratio >= 1.0:
  U = 2 (Losing money on acquisition)
ELSE:
  U = 0 (Critical - each customer loses money)
```

**Data Sources**:
- CAC: Meta Ads API (spend) + Shopify (new customers)
- LTV: Shopify (AOV, repeat purchase rate, cohort analysis)

**IonWave Targets**:
- Target LTV:CAC = 3:1
- Target CAC: $45 (from M3)
- Target LTV: $135 (assumes 30% repeat rate within 90 days)

---

#### L: Lift Velocity (Weight: 3)
**What it measures**: Whether ad optimization is still improving ROAS

**Calculation**:
```
current_month_ROAS = revenue_30days / ad_spend_30days
prior_month_ROAS = revenue_30days_prior / ad_spend_30days_prior
ROAS_lift = (current_month_ROAS - prior_month_ROAS) / prior_month_ROAS

IF ROAS_lift >= 0.10:
  L = 10 (Strong lift, optimization working)
ELIF ROAS_lift >= 0.05:
  L = 8 (Modest lift, healthy improvement)
ELIF ROAS_lift >= 0:
  L = 6 (Flat, no degradation but no improvement)
ELIF ROAS_lift >= -0.05:
  L = 4 (Slight decline, creative fatigue possible)
ELIF ROAS_lift >= -0.10:
  L = 2 (Declining performance, needs intervention)
ELSE:
  L = 0 (Rapid decline, optimization broken)
```

**Data Sources**:
- ROAS: Meta Ads API (use MER for true efficiency, not platform ROAS)

**IonWave Targets**:
- Target MER: 2.5x (minimum viable)
- Expected lift: 5-10% month-over-month in Months 2-6 (creative testing phase)
- Plateau expected: Month 7+ (mature creative, slower lift)

---

#### R: Revenue Recurrence (Weight: 2)
**What it measures**: Repeat purchase ratio (subscription stickiness for DTC)

**Calculation**:
```
repeat_customer_rate_90days = repeat_customers_90days / total_customers_90days
subscription_retention_rate = active_subscribers_month_end / active_subscribers_month_start

IF repeat_customer_rate >= 0.40 OR subscription_retention >= 0.80:
  R = 10 (Excellent retention/recurrence)
ELIF repeat_customer_rate >= 0.30 OR subscription_retention >= 0.70:
  R = 8 (Healthy retention)
ELIF repeat_customer_rate >= 0.20 OR subscription_retention >= 0.60:
  R = 6 (Acceptable retention)
ELIF repeat_customer_rate >= 0.15 OR subscription_retention >= 0.50:
  R = 4 (Low retention, churn risk)
ELIF repeat_customer_rate >= 0.10:
  R = 2 (High churn, structural issue)
ELSE:
  R = 0 (No repeat business, one-time purchase model)
```

**Data Sources**:
- Shopify: Customer cohort analysis, orders_count per customer

**IonWave Targets**:
- Target repeat rate: 30% within 90 days (from M3)
- Subscription model: Not yet implemented (Phase 2 consideration)
- Repeat triggers: Email campaigns (30, 60, 90 days post-purchase)

---

### Negative Signals (Higher = Less Healthy)

#### f: Founder/Operator Drift (Weight: Included in X multiplier)
**What it measures**: How far execution has strayed from documented system

**Calculation**:
```
protocol_adherence_score = protocols_followed / protocols_required
deliverable_quality_score = avg_deliverable_grade (A=4, B=3, C=2, D=1)
check_in_consistency = check_ins_completed / check_ins_expected

operator_drift = 1 - ((protocol_adherence + deliverable_quality/4 + check_in_consistency) / 3)

IF operator_drift <= 0.10:
  f = 0 (Excellent adherence, no drift)
ELIF operator_drift <= 0.20:
  f = 2 (Minor drift, normal variance)
ELIF operator_drift <= 0.30:
  f = 4 (Moderate drift, coaching needed)
ELIF operator_drift <= 0.40:
  f = 6 (Significant drift, intervention required)
ELIF operator_drift <= 0.50:
  f = 8 (Severe drift, probationary status)
ELSE:
  f = 10 (System abandoned, wind-down consideration)
```

**Data Sources**:
- Protocol adherence: CM tracking (daily check-ins, gate assessments)
- Deliverable quality: CM grading logs
- Check-in consistency: P-012 Daily Check-In protocol execution logs

**IonWave Targets**:
- Target protocol adherence: 90%+ (some flexibility for edge cases)
- Target deliverable quality: B+ average (3.3/4.0)
- Target check-in consistency: 95%+ (daily operator engagement)

---

#### c: Cash Constraints (Weight: Included in X multiplier)
**What it measures**: Liquidity gaps choking growth

**Calculation**:
```
runway_days = cash_balance / (7_day_avg_burn_rate)
cash_constraint_severity = runway_constraint + growth_constraint

runway_constraint:
  IF runway_days >= 90: 0
  ELIF runway_days >= 60: 2
  ELIF runway_days >= 30: 5
  ELIF runway_days >= 14: 8
  ELSE: 10 (existential crisis)

growth_constraint (are we leaving money on the table due to cash?):
  IF ad_spend < optimal_ad_spend AND cash_is_bottleneck: +3
  IF inventory < reorder_point AND cash_is_bottleneck: +3
  ELSE: 0

c = MIN(runway_constraint + growth_constraint, 10)
```

**Data Sources**:
- Cash balance: Bank API (Stripe Treasury / Plaid)
- Burn rate: 7-day rolling average (from C-010 Burn Rate Controller)
- Optimal ad spend: Target based on ROAS performance (if ROAS >3.0x, could scale spend)

**IonWave Targets**:
- Target runway: 60+ days (green)
- Growth constraint: Should be $0 (fully funded growth)
- Red flag: Runway <30 days OR can't fund optimal ad spend due to cash

---

#### r: Risk Exposure (Weight: Included in X multiplier)
**What it measures**: Platform, supplier, compliance risks threatening continuity

**Calculation**:
```
risk_score = platform_risk + supplier_risk + compliance_risk

platform_risk (Meta, Shopify, payment processor):
  IF ad_account_disabled OR payment_processor_flagged: 10
  ELIF ad_account_restricted OR high_chargeback_rate (>1%): 5
  ELIF ad_frequency >5 (audience saturation): 2
  ELSE: 0

supplier_risk (3PL, ingredient supplier):
  IF supplier_delayed_30days+ OR stockout_occurred: 10
  ELIF supplier_delayed_14-29days OR inventory <7days: 5
  ELIF supplier_delayed_7-13days OR inventory <14days: 2
  ELSE: 0

compliance_risk (FDA, FTC, legal):
  IF FDA_warning_letter OR FTC_complaint: 10
  ELIF health_claims_unsubstantiated: 5
  ELIF labeling_issue_identified: 2
  ELSE: 0

r = MIN(platform_risk + supplier_risk + compliance_risk, 10)
```

**Data Sources**:
- Platform risk: Meta Ads Manager (account status, ad frequency), Shopify (chargeback rate)
- Supplier risk: 3PL inventory API, supplier communication logs
- Compliance risk: Manual tracking (FDA correspondence, FTC monitoring, legal reviews)

**IonWave Targets**:
- Target platform risk: 0 (no account issues, frequency <3)
- Target supplier risk: 0 (inventory >14 days, no delays)
- Target compliance risk: 0 (all claims substantiated, labeling compliant)

---

## Composite Health Score Calculation

### Formula Evolution

#### V1.0: Simple Weighted Sum (Sprint_STAGE_5 Origin)
```
H = 5M + 4U + 3L + 2R - 1.0(f + c + r)
```

**Issues Identified**:
1. **Positive/Negative Imbalance**: Max positive (140) >> Max negative (30), ratio 4.67:1
2. **Absurd edge case**: Perfect operations (M=U=L=R=10) + catastrophic risks (f=c=r=10) → H=110 (Strong!) ❌
3. **Doesn't capture compounding**: Two severe risks together aren't treated as worse than sum of parts
4. **No weak-link rule**: Critical component failures should dominate score regardless of other metrics

**Status**: Directionally true, not empirically validated. Preserved for reference.

---

#### V2.0: Weighted Sum + Critical Component Veto (Current Implementation)

**Rationale**: Mirrors "weak link rule" from Hypotheses Architecture Standards:
> "The composite score CANNOT exceed the grade of the highest-weighted sub-hypothesis if that sub-hypothesis is D-grade. A critical component at D undermines the whole."

Applied to Trade Health: A catastrophic risk (f≥8, c≥8, or r≥8) should force the Trade into Critical status regardless of how good operations look on paper. Operator abandonment (f=10), near-zero cash runway (c=10), or platform/supplier collapse (r=10) are existential threats that cannot be compensated by margin or unit economics.

**Formula**:
```python
# Step 1: Calculate base score with increased negative weight
H_base = 5*M + 4*U + 3*L + 2*R - 2.0*(f + c + r)

# Step 2: Apply critical component veto rules
if max(f, c, r) >= 8:
    # Any single catastrophic risk (score 8-10) → Force Critical
    H = min(H_base, 29)

elif (f >= 6 and c >= 6) or (f >= 6 and r >= 6) or (c >= 6 and r >= 6):
    # Two severe risks (score 6-7) compounding → Force At Risk ceiling
    # Rationale: Operator drift + cash crisis is worse than sum of parts
    H = min(H_base, 49)

elif max(f, c, r) >= 6:
    # One severe risk (score 6-7) alone → Force Healthy ceiling
    # Rationale: Cannot be "Strong" with severe operator drift, cash crisis, or platform risk
    H = min(H_base, 69)

else:
    # No severe risks → Base score stands
    H = H_base

# Step 3: Map to category
if H >= 70:   status = "Strong"
elif H >= 50: status = "Healthy"
elif H >= 30: status = "At Risk"
else:         status = "Critical"
```

**Key Changes from V1.0**:
1. **Increased negative multiplier**: 1.0 → 2.0 (makes risks count more)
2. **Catastrophic veto** (≥8): Forces Critical regardless of operations
3. **Compound veto** (two ≥6): Forces At Risk (recognizes compounding)
4. **Severe veto** (one ≥6): Forces Healthy ceiling (can't be Strong with severe issue)

**Veto Threshold Justification**:
- **Score 0-5**: Normal operational variance, no veto needed
- **Score 6-7**: Severe issue requiring intervention, veto to ceiling
- **Score 8-10**: Catastrophic/existential, veto to Critical

---

### Score Range (V2.0)

**Base Score Range**:
- **Minimum base**: -60 (if M=U=L=R=0 and f=c=r=10: 0 - 2.0×30 = -60)
- **Maximum base**: +140 (if M=U=L=R=10 and f=c=r=0: 140 - 0 = 140)
- **After veto**: Capped at 29, 49, or 69 depending on risk severity

**Typical Range**:
- Healthy operating Trades: 50-80
- At-Risk Trades: 30-49
- Critical Trades: <30

---

### Categorical Mapping

```
H >= 70: 🟢 Strong (Thriving Trade, minimal intervention)
H 50-69: 🟢 Healthy (Operating well, normal monitoring)
H 30-49: 🟡 At Risk (Needs attention, schedule review)
H 10-29: 🔴 Critical (Intervention required, probationary status)
H < 10:  🔴 Failing (Wind-down consideration)
```

---

### Caveats & Empirical Validation Required

**IMPORTANT**: V2.0 is a hypothesis requiring empirical validation. The veto thresholds (6, 8) and negative multiplier (2.0) are theoretically justified but **not tested against real Trade outcomes**.

**Validation Process** (Meta-Control responsibility):
1. **Collect 90 days of data**: Calculate both V1.0 and V2.0 scores weekly for all Live Trades
2. **Track outcomes**: Document which Trades stabilize, fail, recover, wind down
3. **Compare predictive accuracy**:
   - Did V2.0 correctly flag failing Trades earlier than V1.0?
   - Did V2.0 produce false positives (flagged Critical but Trade recovered)?
   - Did V2.0 miss failures (flagged Healthy but Trade collapsed)?
4. **Tune thresholds**:
   - If veto too aggressive (many false positives): Increase thresholds (6→7, 8→9)
   - If veto too permissive (missed failures): Decrease thresholds (6→5, 8→7)
   - If negative multiplier wrong: Adjust 2.0 → 1.5 or 2.5
5. **Document learnings**: Update formula weights quarterly based on cohort data

**Risk**: V2.0 may be overly conservative (too many Critical flags) or still too permissive. Meta-Control must tune based on real Trade performance data, not theory alone.

**Fallback**: If V2.0 proves unusable (too noisy, not predictive), revert to V1.0 and redesign from empirical data rather than theoretical principles.

---

## Example Calculations

### Example 1: Healthy IonWave Trade (Month 6)

**Positive Signals**:
- M = 8 (65% gross margin, stable)
- U = 8 (LTV:CAC = 2.8x)
- L = 6 (ROAS flat month-over-month, no degradation)
- R = 6 (25% repeat rate at 90 days)

**Negative Signals**:
- f = 2 (Operator adherence 85%, deliverable quality B+)
- c = 2 (Runway 65 days, fully funded growth)
- r = 2 (Ad frequency 3.5, inventory 12 days)

**Calculation (V2.0)**:
```
# Step 1: Base score
H_base = 5(8) + 4(8) + 3(6) + 2(6) - 2.0(2 + 2 + 2)
H_base = 40 + 32 + 18 + 12 - 12
H_base = 102 - 12 = 90

# Step 2: Check veto
max(f, c, r) = max(2, 2, 2) = 2 < 6
→ No veto applies

# Step 3: Final score
H = 90
```

**Assessment**: 🟢 **Strong** (Score: 90)
- Trade is thriving, minimal intervention needed
- Focus: Maintain current trajectory, explore expansion opportunities
- **V1.0 comparison**: Would also score Strong (96 vs 90), similar outcome

---

### Example 2: At-Risk IonWave Trade (Month 4)

**Positive Signals**:
- M = 6 (55% gross margin, declining 8% from last month)
- U = 6 (LTV:CAC = 2.2x, tightening)
- L = 4 (ROAS declined 6% month-over-month, creative fatigue)
- R = 4 (18% repeat rate, below target)

**Negative Signals**:
- f = 4 (Operator adherence 70%, missed 3 check-ins this month)
- c = 5 (Runway 40 days, yellow flag)
- r = 5 (Supplier delayed 10 days, inventory 9 days)

**Calculation (V2.0)**:
```
# Step 1: Base score
H_base = 5(6) + 4(6) + 3(4) + 2(4) - 2.0(4 + 5 + 5)
H_base = 30 + 24 + 12 + 8 - 28
H_base = 74 - 28 = 46

# Step 2: Check veto
max(f, c, r) = max(4, 5, 5) = 5 < 6
→ No veto applies

# Step 3: Final score
H = 46
```

**Assessment**: 🟡 **At Risk** (Score: 46)
- Trade is borderline, trending toward Critical if not addressed
- **Action**: Schedule review with CM, operator coaching session (urgent)
- **Focus**: Stabilize margin (pricing review), creative refresh (address ROAS decline), supplier coordination (inventory buffer)
- **V1.0 comparison**: Would score Healthy (60), V2.0 is more conservative and flags earlier (better early warning)

---

### Example 3: Critical IonWave Trade (Month 10)

**Positive Signals**:
- M = 4 (35% gross margin, eroded from 55% due to discount abuse)
- U = 4 (LTV:CAC = 1.6x, unsustainable)
- L = 2 (ROAS declined 12% month-over-month, optimization broken)
- R = 2 (12% repeat rate, high churn)

**Negative Signals**:
- f = 6 (Operator adherence 60%, deliverable quality C+, system drift)
- c = 8 (Runway 18 days, existential crisis)
- r = 8 (Ad account restricted, supplier delayed 35 days, stockout occurred)

**Calculation (V2.0)**:
```
# Step 1: Base score
H_base = 5(4) + 4(4) + 3(2) + 2(2) - 2.0(6 + 8 + 8)
H_base = 20 + 16 + 6 + 4 - 44
H_base = 46 - 44 = 2

# Step 2: Check veto
max(f, c, r) = max(6, 8, 8) = 8 >= 8
→ CATASTROPHIC VETO APPLIES
H = min(2, 29) = 2

# Step 3: Final score
H = 2
```

**Assessment**: 🔴 **Critical** (Score: 2, near Failing)
- Trade is in existential crisis, immediate intervention required
- **Veto trigger**: c=8 (18 days runway) + r=8 (platform + supplier failure) are catastrophic
- **Action**: Trigger RP-011 (Existential Cash Protocol), emergency GM meeting within 24 hours
- **Decision Point**: Probationary status, 30-day recovery plan OR wind-down
- **Root Causes**: Margin collapse (discount dependency), operator drift (system abandoned), cash crisis + supplier failure (compounding risks)
- **V1.0 comparison**: Would score 24 (Critical), V2.0 scores 2 (near Failing) - veto correctly emphasizes severity

---

### Example 4: V2.0 Veto Edge Case (Perfect Ops + Catastrophic Risk)

**Scenario**: Trade with excellent operations but operator has completely abandoned protocols

**Positive Signals**:
- M = 10 (70% gross margin, stable)
- U = 10 (LTV:CAC = 4.0x, excellent)
- L = 10 (ROAS improving 15% month-over-month)
- R = 10 (50% repeat rate, exceptional)

**Negative Signals**:
- f = 10 (Operator adherence 0%, completely abandoned system)
- c = 2 (Runway 65 days, healthy)
- r = 2 (No platform/supplier issues)

**Calculation (V2.0)**:
```
# Step 1: Base score
H_base = 5(10) + 4(10) + 3(10) + 2(10) - 2.0(10 + 2 + 2)
H_base = 50 + 40 + 30 + 20 - 28
H_base = 140 - 28 = 112

# Step 2: Check veto
max(f, c, r) = max(10, 2, 2) = 10 >= 8
→ CATASTROPHIC VETO APPLIES
H = min(112, 29) = 29

# Step 3: Final score
H = 29 (at Critical threshold)
```

**Assessment**: 🔴 **Critical** (Score: 29, exactly at threshold)
- **Paradox**: Metrics look perfect, but operator has abandoned the system
- **Veto rationale**: f=10 means operator is not following ANY protocols. The "perfect" metrics are likely:
  - Temporary (unsustainable tactics like heavy discounting)
  - Fabricated (operator cooking the books)
  - Accidental (temporary spike about to collapse)
- **Reality check**: An operator with 0% protocol adherence cannot sustain 70% margin, 4:1 LTV:CAC, and 15% ROAS lift. Something is wrong with the data or the operator is running a Ponzi scheme.
- **Action**: Emergency audit by CM + GM. Verify data integrity. Investigate operator behavior.
- **V1.0 comparison**: Would score 110 (Strong!) - completely misses the existential risk ❌

**This is why V2.0 exists**: To prevent absurd outcomes where a Trade with catastrophic risk appears healthy due to strong operations that are likely unsustainable or fraudulent.

---

## Diagnostic Patterns (Fault Trees)

### Pattern 1: Margin Erosion Spiral
**Signature**: M declining, U declining, c increasing
**Diagnosis**: Discount abuse or COGS inflation → margin compressed → CAC becomes unsustainable → cash burns faster
**Intervention**: RP-004 (AOV Structural Analysis), pricing audit, discount policy review

---

### Pattern 2: Creative Fatigue Death Spiral
**Signature**: L declining, U declining, f increasing
**Diagnosis**: ROAS degrading → CAC rising → operator panics, abandons system for "silver bullet" tactics → drift increases → performance worsens
**Intervention**: RP-008 (Creative Fatigue Protocol), operator coaching on patience, systematic creative refresh

---

### Pattern 3: Supplier Dependency Crisis
**Signature**: r spiking (supplier risk), c increasing (cash constraints), R declining (can't fulfill orders → churn)
**Diagnosis**: Single supplier failure → stockout → lost sales + customer churn → cash burn → can't afford backup supplier
**Intervention**: RP-015 (Stockout Prevention), supplier diversification plan, inventory buffer increase

---

### Pattern 4: Operator Burnout
**Signature**: f increasing steadily, L flat/declining (optimization stops), M declining (execution slips)
**Diagnosis**: Operator overwhelmed → stops following protocols → performance degrades → gets more overwhelmed
**Intervention**: Operator coaching, workload audit, consider hiring support (VA, contractor)

---

### Pattern 5: Compounding Risks
**Signature**: r >6, c >6, f >6 (all negative signals elevated simultaneously)
**Diagnosis**: Multiple crises compounding (e.g., ad account disabled + cash crisis + operator panic)
**Intervention**: Emergency triage, wind-down consideration if recovery plan unfeasible

---

## Observer Execution

### Frequency
**Weekly** (calculated Monday mornings, covering previous 7 days + rolling 30/90-day metrics)

### Workflow
1. **6:00 AM Monday**: Data sync (Google Apps Script pulls all metrics)
2. **6:30 AM Monday**: Observer calculates H score
3. **7:00 AM Monday**: CM reviews score + diagnostic patterns
4. **8:00 AM Monday**: If 🟡 or 🔴, CM schedules operator check-in
5. **9:00 AM Monday**: If 🔴, CM escalates to GM for review

### Integration with Controllers
- **Controllers (C-001 through C-012)**: Daily operational monitoring (operator-facing)
- **Observer (OBS-001)**: Weekly portfolio health (CM/GM-facing)
- **Relationship**: Controllers detect immediate issues (ROAS spike, stockout), Observer detects structural trends (margin erosion, operator drift)

---

## Dashboard Integration

### Weekly Trade Health Card (for CM/GM dashboard)

```
## IonWave Trade Health — Week of Feb 10-16, 2026

**Health Score**: 72 (🟢 Strong)

### Component Breakdown
| Signal | Value | Score (0-10) | Weight | Contribution |
|--------|-------|--------------|--------|--------------|
| Margin Stability (M) | 65% | 8 | 5 | +40 |
| Unit Economics (U) | 2.8x LTV:CAC | 8 | 4 | +32 |
| Lift Velocity (L) | +2% ROAS MoM | 6 | 3 | +18 |
| Revenue Recurrence (R) | 25% repeat | 6 | 2 | +12 |
| Operator Drift (f) | 85% adherence | 2 | -1.0 | -2 |
| Cash Constraints (c) | 65 days runway | 2 | -1.0 | -2 |
| Risk Exposure (r) | Freq 3.5, Inv 12d | 2 | -1.0 | -2 |

**Total**: 72 (Previous week: 68, +4 improvement)

### Trend
📈 Improving (ROAS recovery from creative refresh, margin stabilized)

### Diagnostic Pattern
None detected. All signals healthy.

### Action
Continue current trajectory. Monitor margin (watch for discount creep).
```

---

## Meta-Control (Quarterly Review)

### Formula Version Tracking

**V1.0** (Sprint_STAGE_5 origin):
- Simple weighted sum: `H = 5M + 4U + 3L + 2R - 1.0(f + c + r)`
- Status: Directionally true, not empirically validated
- Issue: Positive/negative imbalance allows absurd outcomes

**V2.0** (Current, 2026-02-12):
- Weighted sum + veto: `H_base = 5M + 4U + 3L + 2R - 2.0(f+c+r)` with catastrophic/compound/severe veto rules
- Status: Hypothesis requiring empirical validation
- Issue: May be overly conservative (unknown until tested)

---

### Weight and Veto Tuning Process

**Current parameters** (V2.0):
- Positive weights: M=5, U=4, L=3, R=2
- Negative multiplier: X=2.0
- Veto thresholds: Catastrophic ≥8, Severe ≥6, Compound (two ≥6)

**Empirical Validation Required** (First 90 days):

#### Data Collection
```
For each Live Trade, weekly:
1. Calculate H_v1 (V1.0 formula) and H_v2 (V2.0 formula)
2. Record categorical assessment: Strong/Healthy/At Risk/Critical
3. Document actual Trade status: Operating/Probation/Recovery/Failed/Wind-down
4. Log CM/GM interventions: What actions were taken, outcomes
```

#### Predictive Accuracy Analysis (Quarterly)

**Question 1: Did V2.0 flag failures earlier than V1.0?**
```
For Trades that failed:
- How many weeks before failure did V2.0 flag Critical?
- How many weeks before failure did V1.0 flag Critical?
- Lead time improvement = V2.0_weeks - V1.0_weeks

Target: V2.0 provides ≥2 weeks earlier warning than V1.0
```

**Question 2: False positive rate (too conservative)**
```
For Trades flagged Critical by V2.0:
- % that recovered without intervention (false alarm)
- % that required intervention but recovered (true positive)
- % that failed despite intervention (true positive, intervention failed)

Acceptable false positive rate: <20%
If >20%: Veto thresholds too aggressive, tune upward (6→7, 8→9)
```

**Question 3: False negative rate (too permissive)**
```
For Trades flagged Strong/Healthy by V2.0:
- % that failed within 30 days (missed early warning)
- Common pattern: Which signals (M/U/L/R/f/c/r) were overlooked?

Acceptable false negative rate: <5%
If >5%: Missing signals OR veto thresholds too permissive, tune downward (6→5, 8→7)
```

**Question 4: Veto trigger frequency**
```
How often does each veto trigger:
- Catastrophic (≥8): __% of weeks
- Compound (two ≥6): __% of weeks
- Severe (one ≥6): __% of weeks

If catastrophic triggers >30% of weeks: Threshold too low (normal operations hitting 8)
If catastrophic triggers <2% of weeks: Threshold too high (missing real crises)

Target: Catastrophic 5-10%, Compound 10-20%, Severe 20-30%
```

---

### Tuning Decision Matrix

#### Scenario 1: V2.0 too conservative (many false positives)
**Evidence**: >20% of Critical flags recover without intervention
**Action**:
- Increase veto thresholds: 6→7 (severe), 8→9 (catastrophic)
- OR reduce negative multiplier: 2.0→1.5
- Backtest on historical data before deploying

#### Scenario 2: V2.0 too permissive (missing failures)
**Evidence**: >5% of Strong/Healthy Trades fail within 30 days
**Action**:
- Decrease veto thresholds: 6→5 (severe), 8→7 (catastrophic)
- OR increase negative multiplier: 2.0→2.5
- OR add compound veto for (f≥5 AND c≥5) instead of (f≥6 AND c≥6)

#### Scenario 3: Specific signal not discriminating
**Evidence**: M (margin) always 7-9, never varies, doesn't predict outcomes
**Action**:
- Reduce weight: M=5→M=3
- OR refine calculation (maybe margin trend more important than absolute value)

#### Scenario 4: Missing critical signal
**Evidence**: Trades failing with pattern not captured by 7 signals
**Action**:
- Add 8th signal (e.g., NPS, support ticket volume, email engagement)
- Assign weight based on correlation with failure
- Adjust formula: `H = 5M + 4U + 3L + 2R + 1S - 2.0(f+c+r)` where S = new signal

#### Scenario 5: V2.0 not better than V1.0
**Evidence**: Similar predictive accuracy, but V2.0 more complex
**Action**:
- Revert to V1.0
- OR redesign from scratch using empirical clustering (ML approach: what combinations of signals actually predict failure?)

---

### Quarterly Review Checklist (MSO-led)

**Week 1: Data Collection**
- [ ] Extract 90 days of H_v1, H_v2 scores for all Live Trades
- [ ] Extract Trade outcome data (Operating/Failed/Wind-down)
- [ ] Extract CM intervention logs (what actions taken, when)

**Week 2: Analysis**
- [ ] Calculate false positive rate (Critical flags that recovered)
- [ ] Calculate false negative rate (Strong/Healthy that failed)
- [ ] Calculate lead time improvement (V2.0 vs V1.0 early warning)
- [ ] Analyze veto trigger frequency (catastrophic, compound, severe)

**Week 3: Proposal**
- [ ] Document findings: Is V2.0 better than V1.0?
- [ ] If yes: Propose parameter tuning (adjust thresholds, weights, multiplier)
- [ ] If no: Propose V3.0 or revert to V1.0
- [ ] Backtest proposal on historical data

**Week 4: Deployment**
- [ ] Update trade_health_observer.md with new formula version
- [ ] Communicate changes to CM + GM (what changed, why, what to expect)
- [ ] Monitor for 30 days, check if tuning improved predictive accuracy
- [ ] If regression: Rollback to previous version

---

### Long-Term Evolution (Meta-Control)

**Year 1 Goal**: Validate V2.0 formula, tune parameters quarterly
- Q1: Collect baseline data, no tuning (just monitor)
- Q2: First tuning based on 90 days of data
- Q3: Second tuning, assess improvement vs Q1 baseline
- Q4: Annual review, decide V3.0 or stabilize V2.0

**Year 2+ Goal**: Optimize for portfolio-level predictions
- Cross-Trade pattern analysis: Do certain signal combinations predict failure across all Trades?
- Cohort effects: Do early-stage Trades (ICL-1, ICL-2) need different weights than mature Trades (ICL-4+)?
- External factors: Market conditions, ad platform changes, regulatory shifts → add exogenous signals?

**Advanced**: Machine learning approach (if portfolio scales to 20+ Trades)
- Cluster analysis: What signal patterns distinguish Strong from Failed Trades?
- Logistic regression: What weights maximize predictive accuracy empirically?
- Replace hand-tuned formula with data-driven model
- Keep human-readable diagnostic patterns for CM/GM interpretation

---

## Related Documents

- **Controllers**: `/passets/dashboards/controller_registry.md` (daily operational monitoring)
- **Parameters**: `/passets/dashboards/parameter_registry.md` (controller thresholds)
- **Systems Architecture**: `/standards/Systems_Architecture_Standards.md` (Observer primitive definition)
- **Unit Economics**: `/data/m3/unit_economics.md` (source of LTV:CAC targets)
- **Sprint_STAGE_5**: Trade Health formula origin

---

## Version History

**v1.0.0 (2026-02-12)**:
- Initial Trade Health Observer specification
- Operationalized all 7 components (M, U, L, R, f, c, r) with actionable calculations
- Defined 0-10 normalization scales for each metric
- Created 5 diagnostic fault-tree patterns
- Mapped to categorical assessments (Strong/Healthy/At Risk/Critical/Failing)
- Weekly execution workflow defined
- Meta-Control weight tuning process established

**v2.0.0 (2026-02-12)**:
- **BREAKING CHANGE**: Replaced simple weighted sum with weighted sum + critical component veto
- **Rationale**: V1.0 formula allowed absurd outcomes (perfect ops + catastrophic risk = Strong)
- **Changes**:
  - Increased negative multiplier: 1.0 → 2.0 (risks count more)
  - Added catastrophic veto: max(f,c,r) ≥8 → force H ≤29 (Critical)
  - Added compound veto: two of (f,c,r) ≥6 → force H ≤49 (At Risk)
  - Added severe veto: one of (f,c,r) ≥6 → force H ≤69 (Healthy ceiling)
- **Example calculations updated**: All 4 examples show V1.0 vs V2.0 comparison
- **Caveats documented**: V2.0 is hypothesis requiring empirical validation
- **Validation process**: 90-day data collection, quarterly tuning, false positive/negative analysis
- **Meta-Control section expanded**: Tuning decision matrix, quarterly review checklist, long-term evolution roadmap
- **Status**: EXPERIMENTAL - may be too conservative, requires backtesting against real Trade outcomes

---

**Next Steps**:
1. Implement data collection for all 7 metrics (extend Google Apps Script)
2. Build Observer calculation logic (weekly cron job)
3. Add Trade Health Card to CM/GM dashboard
4. Collect 90 days of data, tune weights based on outcomes
5. Consider additional signals (e.g., NPS, support ticket volume, email engagement)
