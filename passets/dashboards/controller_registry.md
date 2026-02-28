# Controller Registry — IonWave Operational Dashboard

**Version**: 1.0.0
**Created**: 2026-02-12
**Purpose**: Formal controller definitions for IonWave operational monitoring
**Source**: Systems_Architecture_Standards.md + daily_pulse.md
**Owner Role**: Chief of Staff (operator) + CM (oversight)

---

## Overview

**Controllers** are monitoring mechanisms that implement the control loop:
1. **Sense** - Read metric from data source
2. **Compare** - Metric vs Parameter threshold
3. **Detect** - Is deviation outside tolerance?
4. **Act** - If yes → trigger Reactive Protocol
5. **Report** - Log event to Meta-Control layer

This registry defines 12 controllers monitoring IonWave's operational health across 4 domains:
- Revenue & Growth (4 controllers)
- Ad Performance (4 controllers)
- Cash & Runway (2 controllers)
- Operations (2 controllers)

---

## Controller Definitions

### Revenue & Growth Controllers

#### C-001: Revenue Deviation Controller

**Type**: Continuous Controller
**Frequency**: Daily (via daily_pulse.md)
**Metric**: Net Revenue (yesterday)
**Data Source**: Shopify Admin API → `/admin/api/2024-01/orders.json?status=any&financial_status=paid`

**Parameters**:
- `REVENUE_GREEN_BAND`: ±15% of 7-day average
- `REVENUE_YELLOW_BAND`: -15% to -30% vs 7-day average
- `REVENUE_RED_THRESHOLD`: -30%+ vs 7-day average OR <$100 absolute
- `REVENUE_ABSOLUTE_FLOOR`: $100 (existential minimum)

**Control Logic**:
```
delta = (today_revenue - avg_7day) / avg_7day

IF delta within ±15%:
  status = 🟢 Green
  action = none

IF delta between -15% and -30%:
  status = 🟡 Yellow
  action = flag for review (no protocol trigger)

IF delta < -30% OR today_revenue < $100:
  status = 🔴 Red
  action = TRIGGER RP-001 (Revenue Recovery Protocol)
  report = log to Meta-Control
```

**Reactive Protocol**: RP-001 (Revenue Recovery Protocol)

**Owner**: Operator (daily check), CM (oversight)

**Variability Index**: VI-3 (Slow-moving - thresholds tuned quarterly based on growth trends)

---

#### C-002: Order Volume Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: Order count (yesterday)
**Data Source**: Shopify Admin API → order count

**Parameters**:
- `ORDER_GREEN_BAND`: ±15% of 7-day average
- `ORDER_YELLOW_BAND`: -15% to -30% vs 7-day average
- `ORDER_RED_THRESHOLD`: -30%+ vs 7-day average
- `ORDER_ABSOLUTE_FLOOR`: 5 orders/day (minimum viable)

**Control Logic**:
```
delta = (today_orders - avg_7day_orders) / avg_7day_orders

IF delta within ±15%:
  status = 🟢 Green

IF delta between -15% and -30%:
  status = 🟡 Yellow

IF delta < -30% OR today_orders < 5:
  status = 🔴 Red
  action = TRIGGER RP-002 (Order Volume Investigation Protocol)
```

**Reactive Protocol**: RP-002 (Order Volume Investigation Protocol)

**Owner**: Operator

**Variability Index**: VI-3

---

#### C-003: New Customer Acquisition Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: New customer count (yesterday)
**Data Source**: Shopify Customer API → filter by `orders_count=1`

**Parameters**:
- `NEW_CUSTOMER_GREEN_BAND`: ±15% of 7-day average
- `NEW_CUSTOMER_YELLOW_BAND`: -15% to -30% vs 7-day average
- `NEW_CUSTOMER_RED_THRESHOLD`: -30%+ vs 7-day average
- `NEW_CUSTOMER_FLOOR`: 3 new customers/day (Phase 1 minimum)

**Control Logic**:
```
delta = (today_new_customers - avg_7day) / avg_7day

IF delta within ±15%:
  status = 🟢 Green

IF delta between -15% and -30%:
  status = 🟡 Yellow

IF delta < -30% OR today_new_customers < 3:
  status = 🔴 Red
  action = TRIGGER RP-003 (Acquisition Funnel Diagnostic)
```

**Reactive Protocol**: RP-003 (Acquisition Funnel Diagnostic)

**Owner**: Operator + Media Buyer (if hired)

**Variability Index**: VI-4 (Adaptive - floor adjusts per growth phase)

---

#### C-004: AOV Deviation Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: Average Order Value (yesterday)
**Data Source**: Shopify → revenue / order_count

**Parameters**:
- `AOV_TARGET`: $44 (from M3 unit economics)
- `AOV_GREEN_BAND`: ±15% of target ($37.40 - $50.60)
- `AOV_YELLOW_BAND`: ±15-30% of target
- `AOV_RED_THRESHOLD`: <$35 OR >$55 (structural issue)

**Control Logic**:
```
IF $37.40 <= today_aov <= $50.60:
  status = 🟢 Green

IF $35 <= today_aov < $37.40 OR $50.60 < today_aov <= $55:
  status = 🟡 Yellow

IF today_aov < $35 OR today_aov > $55:
  status = 🔴 Red
  action = TRIGGER RP-004 (AOV Structural Analysis)
  note = "Low AOV may indicate discount abuse, high AOV may indicate bulk order anomaly"
```

**Reactive Protocol**: RP-004 (AOV Structural Analysis)

**Owner**: Operator

**Variability Index**: VI-2 (Stable - based on product pricing, rarely changes)

---

### Ad Performance Controllers

#### C-005: ROAS Threshold Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: ROAS (platform-reported, Meta Ads Manager)
**Data Source**: Meta Marketing API → `/act_{ad_account_id}/insights?fields=spend,purchase_roas`

**Parameters**:
- `ROAS_TARGET`: 2.5x (profitable baseline from M3)
- `ROAS_GREEN`: >2.5x
- `ROAS_YELLOW`: 1.5x - 2.5x (watch zone)
- `ROAS_RED`: <1.5x (unprofitable)
- `ROAS_KILL_THRESHOLD`: <1.5x for 3 consecutive days (existential risk)

**Control Logic**:
```
IF today_roas >= 2.5:
  status = 🟢 Green

IF 1.5 <= today_roas < 2.5:
  status = 🟡 Yellow
  note = "ROAS below target but not critical"

IF today_roas < 1.5:
  status = 🔴 Red
  action = TRIGGER RP-005 (ROAS Recovery Protocol)

  IF consecutive_red_days >= 3:
    action = TRIGGER RP-006 (Ad Spend Pause Protocol - CRITICAL)
```

**Reactive Protocols**:
- RP-005 (ROAS Recovery Protocol - creative refresh, audience adjustment)
- RP-006 (Ad Spend Pause Protocol - immediate spend stop)

**Owner**: Operator + Media Buyer

**Variability Index**: VI-3 (Slow-moving - adjusted based on cohort LTV data)

**Note**: ROAS is platform-reported and overstates by 20-40% due to iOS 14.5 attribution loss. Use MER (C-011) for true business efficiency.

---

#### C-006: CPA Threshold Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: Cost Per Acquisition (yesterday)
**Data Source**: Meta Marketing API → `spend / purchases`

**Parameters**:
- `CPA_TARGET`: $45 (from M3 unit economics)
- `CPA_GREEN`: <$45
- `CPA_YELLOW`: $45 - $60
- `CPA_RED`: >$60 (unsustainable)

**Control Logic**:
```
IF today_cpa < 45:
  status = 🟢 Green

IF 45 <= today_cpa <= 60:
  status = 🟡 Yellow

IF today_cpa > 60:
  status = 🔴 Red
  action = TRIGGER RP-007 (CPA Optimization Protocol)
```

**Reactive Protocol**: RP-007 (CPA Optimization Protocol)

**Owner**: Media Buyer (or Operator if pre-hire)

**Variability Index**: VI-3

---

#### C-007: CTR Threshold Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: Click-Through Rate (yesterday)
**Data Source**: Meta Marketing API → `clicks / impressions`

**Parameters**:
- `CTR_GREEN`: >1.0%
- `CTR_YELLOW`: 0.5% - 1.0%
- `CTR_RED`: <0.5% (creative fatigue or poor targeting)

**Control Logic**:
```
IF today_ctr >= 1.0:
  status = 🟢 Green

IF 0.5 <= today_ctr < 1.0:
  status = 🟡 Yellow

IF today_ctr < 0.5:
  status = 🔴 Red
  action = TRIGGER RP-008 (Creative Fatigue Protocol)
  note = "Low CTR indicates creative fatigue, audience saturation, or poor targeting"
```

**Reactive Protocol**: RP-008 (Creative Fatigue Protocol)

**Owner**: Media Buyer + Creative team

**Variability Index**: VI-4 (Adaptive - varies by creative angle, audience maturity)

---

#### C-008: Ad Frequency Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: Ad Frequency (avg impressions per unique user)
**Data Source**: Meta Marketing API → `impressions / reach`

**Parameters**:
- `FREQUENCY_GREEN`: <3
- `FREQUENCY_YELLOW`: 3 - 5
- `FREQUENCY_RED`: >5 (audience fatigue)

**Control Logic**:
```
IF today_frequency < 3:
  status = 🟢 Green

IF 3 <= today_frequency <= 5:
  status = 🟡 Yellow
  note = "Audience seeing ads multiple times - monitor for fatigue"

IF today_frequency > 5:
  status = 🔴 Red
  action = TRIGGER RP-009 (Audience Expansion Protocol)
  note = "High frequency = audience saturation, expand targeting"
```

**Reactive Protocol**: RP-009 (Audience Expansion Protocol)

**Owner**: Media Buyer

**Variability Index**: VI-4

---

### Cash & Runway Controllers

#### C-009: Cash Runway Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: Runway (days of cash remaining)
**Data Source**: Bank API (Stripe Treasury OR Plaid) → cash_balance / 7-day avg burn rate

**Parameters**:
- `RUNWAY_GREEN`: >60 days
- `RUNWAY_YELLOW`: 30-60 days (planning mode)
- `RUNWAY_RED`: <30 days (CRITICAL - immediate action required)
- `RUNWAY_KILL`: <14 days (existential crisis)

**Control Logic**:
```
runway_days = cash_balance / avg_7day_burn

IF runway_days > 60:
  status = 🟢 Green

IF 30 <= runway_days <= 60:
  status = 🟡 Yellow
  action = flag for review
  note = "Start planning: fundraise, cut costs, or accelerate revenue"

IF runway_days < 30:
  status = 🔴 Red
  action = TRIGGER RP-010 (Cash Crisis Protocol)

  IF runway_days < 14:
    action = TRIGGER RP-011 (Existential Cash Protocol - CRITICAL)
    escalate = Studio 3 + Venture Partner immediately
```

**Reactive Protocols**:
- RP-010 (Cash Crisis Protocol - expense audit, revenue acceleration)
- RP-011 (Existential Cash Protocol - emergency fundraise or wind-down decision)

**Owner**: Operator (daily check), Studio 3 / VP (if red)

**Variability Index**: VI-2 (Stable - 30 days is universally critical, 60 days is prudent buffer)

---

#### C-010: Burn Rate Spike Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: 7-day average burn rate
**Data Source**: Bank API → (cash_balance_7days_ago - cash_balance_today) / 7

**Parameters**:
- `BURN_BASELINE`: Expected burn rate from budget plan
- `BURN_GREEN_BAND`: ±15% of baseline
- `BURN_YELLOW_BAND`: +15% to +30% vs baseline
- `BURN_RED_THRESHOLD`: +30%+ vs baseline (unplanned spending)

**Control Logic**:
```
delta = (actual_burn - baseline_burn) / baseline_burn

IF delta within ±15%:
  status = 🟢 Green

IF delta between +15% and +30%:
  status = 🟡 Yellow
  note = "Burn rate elevated - review expense categories"

IF delta > +30%:
  status = 🔴 Red
  action = TRIGGER RP-012 (Burn Rate Audit Protocol)
```

**Reactive Protocol**: RP-012 (Burn Rate Audit Protocol)

**Owner**: Operator

**Variability Index**: VI-4 (Adaptive - baseline changes per growth phase)

---

### Operations Controllers

#### C-011: MER (Blended Efficiency) Controller

**Type**: Continuous Controller
**Frequency**: Weekly (calculated Monday for previous 7 days)
**Metric**: MER (Marketing Efficiency Ratio) = Total Revenue / Total Ad Spend
**Data Source**: Shopify (revenue) + Meta (ad spend)

**Parameters**:
- `MER_TARGET`: 2.5x (minimum viable from M3)
- `MER_GREEN`: >2.5x
- `MER_YELLOW`: 1.8x - 2.5x
- `MER_RED`: <1.8x (business model broken)

**Control Logic**:
```
mer = total_revenue_7days / total_ad_spend_7days

IF mer >= 2.5:
  status = 🟢 Green

IF 1.8 <= mer < 2.5:
  status = 🟡 Yellow
  note = "MER below target - organic traffic may be declining, or CAC rising"

IF mer < 1.8:
  status = 🔴 Red
  action = TRIGGER RP-013 (Business Model Review Protocol)
  note = "MER <1.8x indicates fundamental unit economics issue"
```

**Reactive Protocol**: RP-013 (Business Model Review Protocol)

**Owner**: Operator + Studio 3

**Variability Index**: VI-2 (Stable - based on unit economics, changes only if product/pricing changes)

**Why MER vs ROAS**: MER captures true business efficiency including organic traffic, email revenue, repeat purchases. ROAS is platform-reported and attribution-limited. Use MER for strategic decisions.

---

#### C-012: Inventory Stockout Controller

**Type**: Continuous Controller
**Frequency**: Daily
**Metric**: Days of inventory remaining (current stock / 7-day avg sell-through rate)
**Data Source**: 3PL Inventory API (ShipBob, Fulfil, etc.)

**Parameters**:
- `INVENTORY_GREEN`: >14 days supply
- `INVENTORY_YELLOW`: 7-14 days supply
- `INVENTORY_RED`: <7 days supply (stockout risk)
- `INVENTORY_CRITICAL`: <3 days supply (immediate reorder)

**Control Logic**:
```
days_remaining = current_inventory_units / avg_7day_sell_through

IF days_remaining > 14:
  status = 🟢 Green

IF 7 <= days_remaining <= 14:
  status = 🟡 Yellow
  action = flag for review
  note = "Plan reorder - lead time is 30-45 days from supplier"

IF days_remaining < 7:
  status = 🔴 Red
  action = TRIGGER RP-014 (Emergency Reorder Protocol)

  IF days_remaining < 3:
    action = TRIGGER RP-015 (Stockout Prevention Protocol - CRITICAL)
    note = "Consider pausing ad spend to preserve inventory"
```

**Reactive Protocols**:
- RP-014 (Emergency Reorder Protocol - expedited supplier order)
- RP-015 (Stockout Prevention Protocol - ad spend modulation, waitlist setup)

**Owner**: Operator + Supply Chain coordinator

**Variability Index**: VI-4 (Adaptive - reorder point adjusts based on sell-through velocity, seasonality)

---

## Controller Execution Schedule

### Daily Controllers (Run at 6:00 AM via automated sync)
- C-001: Revenue Deviation
- C-002: Order Volume
- C-003: New Customer Acquisition
- C-004: AOV Deviation
- C-005: ROAS Threshold
- C-006: CPA Threshold
- C-007: CTR Threshold
- C-008: Ad Frequency
- C-009: Cash Runway
- C-010: Burn Rate Spike
- C-012: Inventory Stockout

### Weekly Controllers (Run Monday 6:00 AM)
- C-011: MER (Blended Efficiency)

### Manual Override
Operator can force controller execution at any time via dashboard refresh or manual metric check.

---

## Controller Integration with Dashboard

**daily_pulse.md** displays controller outputs:
- Status indicators (🟢🟡🔴) = controller compare step result
- "One Thing to Fix Today" = highest priority red flag from controllers
- "Fires & Issues" checklist = active red controller detections

**Workflow**:
1. **6:00 AM**: Google Apps Script syncs data from APIs
2. **6:05 AM**: Controllers execute (compare metrics to parameters)
3. **6:10 AM**: Dashboard updated with status indicators
4. **6:15 AM**: If any 🔴 Red → Reactive Protocol triggered (email alert + Slack notification)
5. **8:00 AM**: Operator reviews dashboard, acts on "One Thing to Fix Today"

---

## Meta-Control Layer

**Controller Performance Review** (Quarterly):
1. **Too Sensitive**: Controller fires >20% of days → Yellow/Red thresholds too tight → Adjust parameters
2. **Too Permissive**: Controller never fires, but business shows issues → Thresholds too loose → Tighten
3. **False Positives**: Controller fires, Reactive Protocol finds no real issue → Metric misalignment → Revise controller logic
4. **Missed Issues**: Problem occurs but controller didn't fire → Add new controller OR adjust sensitivity

**Owner**: Meta Standards Officer (MSO) + CM

**Inputs**:
- Reactive Protocol trigger logs
- Operator feedback ("this alert was useless" / "this caught a real issue")
- Cross-Trade pattern analysis

**Outputs**:
- Updated parameter values
- New controllers (if gaps found)
- Retired controllers (if redundant)
- Revised controller logic

---

## Next Steps

**Phase 1: Parameter Values** (REQUIRED BEFORE LAUNCH)
- Set baseline values for VI-4 parameters (burn baseline, new customer floor, etc.)
- Document in `parameter_registry.md`

**Phase 2: Reactive Protocol Specs** (REQUIRED BEFORE LAUNCH)
- Define all 15 Reactive Protocols (RP-001 through RP-015)
- Document steps, owners, escalation triggers
- Store in `reactive_protocols.md`

**Phase 3: Automation** (Week 2-4 ICL-0)
- Build Google Apps Script to execute controllers
- Set up email/Slack alerts for red flags
- Test with dummy data before live launch

**Phase 4: Calibration** (Weeks 5-8 ICL-1)
- Run controllers daily, collect logs
- Tune parameters based on real performance
- Adjust thresholds to reduce noise, catch real issues

---

## Version History

**v1.0.0 (2026-02-12)**:
- Initial controller registry
- 12 controllers defined across 4 domains
- Formal Sense → Compare → Detect → Act → Report structure
- Integration with daily_pulse.md dashboard
- Parameter placeholders (values to be set in parameter_registry.md)
- Reactive Protocol stubs (to be detailed in reactive_protocols.md)

---

## Related Documents

- **Dashboard**: `/passets/dashboards/daily_pulse.md` (displays controller outputs)
- **Data Pipeline**: `/passets/dashboards/data_pipeline_spec.md` (feeds metrics to controllers)
- **Architecture**: `/standards/Systems_Architecture_Standards.md` (controller primitive definition)
- **Parameters**: `/passets/dashboards/parameter_registry.md` (threshold values) [TO BE CREATED]
- **Reactive Protocols**: `/passets/dashboards/reactive_protocols.md` (triggered actions) [TO BE CREATED]
