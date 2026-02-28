# Parameter Registry — IonWave Operational Thresholds

**Version**: 1.0.0
**Created**: 2026-02-12
**Purpose**: Numeric thresholds and tolerance ranges for controller monitoring
**Source**: M3 (Unit Economics), M30 (Analytics), controller_registry.md
**Owner Role**: Operator (uses), CM (tunes), MSO (governs)

---

## Overview

**Parameters** are the numeric dials that tune the control system. They define:
- **Target values** (goals to hit)
- **Green bands** (healthy operating range)
- **Yellow bands** (watch zones - flag but don't trigger protocols)
- **Red thresholds** (trigger Reactive Protocols)

Every parameter has a **Variability Index (VI)** rating:
- **VI-1**: Immutable (architectural constants, never change)
- **VI-2**: Stable (modified only during governance review)
- **VI-3**: Slow-moving (revised when cohort data shows drift)
- **VI-4**: Adaptive (frequently tuned, Trade-specific)
- **VI-5**: Fully local (operator discretion within guardrails)

---

## Revenue & Growth Parameters

### REV-001: Revenue Tolerance Bands

**Controller**: C-001 (Revenue Deviation Controller)
**Metric**: Daily net revenue
**Variability Index**: VI-3 (Slow-moving)

**Values**:
```
REVENUE_GREEN_BAND = ±15% of 7-day average
REVENUE_YELLOW_BAND = -15% to -30% of 7-day average
REVENUE_RED_THRESHOLD = -30%+ of 7-day average
REVENUE_ABSOLUTE_FLOOR = $100/day
```

**Rationale**:
- ±15% green band: Normal daily variance in DTC e-commerce
- -30% red threshold: Indicates systemic issue (ad failure, site down, payment processor issue)
- $100 floor: Below this = existential problem (fewer than 3 orders at $44 AOV)

**Tuning History**:
- v1.0.0 (2026-02-12): Initial values based on DTC industry benchmarks
- [Future updates logged here]

---

### REV-002: Order Volume Tolerance

**Controller**: C-002 (Order Volume Controller)
**Metric**: Daily order count
**Variability Index**: VI-3

**Values**:
```
ORDER_GREEN_BAND = ±15% of 7-day average
ORDER_YELLOW_BAND = -15% to -30% of 7-day average
ORDER_RED_THRESHOLD = -30%+ of 7-day average
ORDER_ABSOLUTE_FLOOR = 5 orders/day
```

**Rationale**:
- Mirrors revenue tolerance (orders drive revenue)
- 5 order floor: Minimum viable daily volume for Phase 1 (ICL-1 soft launch)
- Will increase to 20+ orders/day in ICL-3 (Scale phase)

**Phase-Specific Adjustments**:
- ICL-0/ICL-1 (Pre-launch, Soft Launch): 5 orders/day floor
- ICL-2 (Validation): 15 orders/day floor
- ICL-3+ (Scale): 30+ orders/day floor

---

### REV-003: New Customer Acquisition Tolerance

**Controller**: C-003 (New Customer Acquisition Controller)
**Metric**: Daily new customer count
**Variability Index**: VI-4 (Adaptive)

**Values**:
```
NEW_CUSTOMER_GREEN_BAND = ±15% of 7-day average
NEW_CUSTOMER_YELLOW_BAND = -15% to -30% of 7-day average
NEW_CUSTOMER_RED_THRESHOLD = -30%+ of 7-day average
NEW_CUSTOMER_FLOOR = 3 new customers/day (ICL-1)
```

**Rationale**:
- New customer acquisition is leading indicator of growth
- Floor adjusts per phase (3/day in soft launch, 15+/day in scale)
- More sensitive than order volume (repeat revenue masks acquisition issues)

**Phase-Specific Floors**:
- ICL-1 (Soft Launch): 3/day
- ICL-2 (Validation): 10/day
- ICL-3 (Scale): 20/day
- ICL-4 (Optimize): 30+/day

---

### REV-004: AOV Target and Tolerance

**Controller**: C-004 (AOV Deviation Controller)
**Metric**: Average Order Value
**Variability Index**: VI-2 (Stable - tied to product pricing)

**Values**:
```
AOV_TARGET = $44 (from M3 unit economics)
AOV_GREEN_BAND = $37.40 - $50.60 (±15%)
AOV_YELLOW_BAND = $35 - $37.40 OR $50.60 - $55
AOV_RED_THRESHOLD = <$35 OR >$55
```

**Rationale**:
- $44 target: Product price $40 + shipping/add-ons
- <$35 red flag: Excessive discounting or price erosion
- >$55 red flag: Bulk order anomaly or pricing error

**Pricing Tiers** (for reference):
- Single unit: $40
- 2-pack: $72 ($36 each, 10% discount)
- 3-pack: $102 ($34 each, 15% discount)
- Expected mix: 70% single, 25% 2-pack, 5% 3-pack → $44 blended AOV

**Update Trigger**: If product pricing changes, update AOV_TARGET within 24 hours.

---

## Ad Performance Parameters

### AD-001: ROAS Thresholds

**Controller**: C-005 (ROAS Threshold Controller)
**Metric**: Platform-reported ROAS (Meta Ads Manager)
**Variability Index**: VI-3 (Slow-moving - adjusted based on LTV data)

**Values**:
```
ROAS_TARGET = 2.5x
ROAS_GREEN = >2.5x
ROAS_YELLOW = 1.5x - 2.5x
ROAS_RED = <1.5x
ROAS_KILL_THRESHOLD = <1.5x for 3 consecutive days
```

**Rationale**:
- 2.5x target: Minimum profitable ROAS from M3 unit economics
- Accounts for 30% product cost, 20% ops overhead, 10% profit margin
- Platform ROAS overstates by 20-40% (iOS 14.5 attribution loss) → use MER for true efficiency

**ROAS vs MER**:
- **ROAS** (platform): Ad-attributed revenue only, overstates due to iOS 14.5
- **MER** (blended): Total revenue / ad spend, includes organic/email/repeat
- **Use ROAS for**: Ad optimization, creative testing, audience performance
- **Use MER for**: Business viability, unit economics validation, strategic decisions

**Kill Threshold Logic**:
- 1 day <1.5x: Flag, investigate
- 2 days <1.5x: Trigger RP-005 (ROAS Recovery)
- 3 days <1.5x: Trigger RP-006 (Ad Spend Pause - CRITICAL)

---

### AD-002: CPA Thresholds

**Controller**: C-006 (CPA Threshold Controller)
**Metric**: Cost Per Acquisition (ad spend / purchases)
**Variability Index**: VI-3

**Values**:
```
CPA_TARGET = $45 (from M3)
CPA_GREEN = <$45
CPA_YELLOW = $45 - $60
CPA_RED = >$60
```

**Rationale**:
- $45 target: From M3 unit economics (AOV $44, target CAC:LTV ratio 1:3)
- $60 red threshold: Breaks unit economics (1.35x CAC:AOV, unsustainable)
- Assumes 30% repeat purchase rate within 90 days (LTV = $57)

**LTV Sensitivity**:
- If 90-day repeat rate >40%: CPA can sustain up to $65
- If 90-day repeat rate <20%: CPA must stay <$40
- Update CPA_TARGET quarterly based on cohort LTV data

---

### AD-003: CTR Thresholds

**Controller**: C-007 (CTR Threshold Controller)
**Metric**: Click-Through Rate (clicks / impressions)
**Variability Index**: VI-4 (Adaptive - varies by creative, audience)

**Values**:
```
CTR_GREEN = >1.0%
CTR_YELLOW = 0.5% - 1.0%
CTR_RED = <0.5%
```

**Rationale**:
- 1.0% benchmark: DTC e-commerce average for cold traffic
- <0.5%: Creative fatigue, poor targeting, or saturated audience
- CTR correlates with CPA (low CTR → high CPA)

**Creative-Specific Adjustments**:
- New creative (Days 1-7): Expect 1.2-1.5% CTR (novelty boost)
- Mature creative (Days 30+): 0.8-1.0% acceptable
- Retargeting ads: 2.0%+ expected (warm audience)

**Trigger for Creative Refresh**: 3 consecutive days <0.7% CTR → retire creative, test new angle

---

### AD-004: Ad Frequency Thresholds

**Controller**: C-008 (Ad Frequency Controller)
**Metric**: Impressions / Reach (avg times user sees ad)
**Variability Index**: VI-4

**Values**:
```
FREQUENCY_GREEN = <3
FREQUENCY_YELLOW = 3 - 5
FREQUENCY_RED = >5
```

**Rationale**:
- Frequency <3: Healthy reach, audience not saturated
- Frequency 3-5: User seeing ad multiple times, monitor for fatigue
- Frequency >5: Audience saturation → expand targeting OR creative refresh

**Relationship to CTR**:
- High frequency + declining CTR = creative fatigue → new angle
- High frequency + stable CTR = engaged audience → scale spend

---

## Cash & Runway Parameters

### CASH-001: Runway Thresholds

**Controller**: C-009 (Cash Runway Controller)
**Metric**: Days of cash remaining (cash_balance / 7-day avg burn)
**Variability Index**: VI-2 (Stable - universal operating principle)

**Values**:
```
RUNWAY_GREEN = >60 days
RUNWAY_YELLOW = 30-60 days
RUNWAY_RED = <30 days
RUNWAY_KILL = <14 days
```

**Rationale**:
- 60 days: Healthy buffer for DTC business (covers 1 inventory cycle)
- 30 days: Planning mode (start fundraise OR cut costs OR accelerate revenue)
- 14 days: Existential crisis (emergency fundraise or wind-down decision)

**Why These Thresholds**:
- 30 days = minimum to execute emergency cost cuts
- 14 days = point of no return (payroll, supplier commitments can't be unwound)

**Escalation**:
- <60 days: Flag to operator
- <30 days: Alert CM + Studio 3
- <14 days: Emergency call with Studio 3 + Venture Partner

---

### CASH-002: Burn Rate Tolerance

**Controller**: C-010 (Burn Rate Spike Controller)
**Metric**: 7-day average daily burn rate
**Variability Index**: VI-4 (Adaptive - baseline changes per phase)

**Values**:
```
BURN_BASELINE = [Set per ICL phase, see below]
BURN_GREEN_BAND = ±15% of baseline
BURN_YELLOW_BAND = +15% to +30% of baseline
BURN_RED_THRESHOLD = +30%+ of baseline
```

**Phase-Specific Baselines** (from financial model):
- **ICL-0 (Pre-launch)**: $300/day (entity setup, initial inventory, branding)
- **ICL-1 (Soft Launch)**: $500/day (ad testing, customer acquisition)
- **ICL-2 (Validation)**: $800/day (scaled ad spend, team expansion)
- **ICL-3 (Scale)**: $1,500/day (full ad spend, inventory growth)
- **ICL-4+ (Optimize)**: Variable based on revenue (target 70% gross margin)

**Burn Composition** (ICL-1 example, $500/day):
- Ad spend: $300/day (60%)
- Ops overhead: $100/day (20% - tools, 3PL, support)
- Team: $100/day (20% - contractor hours)

**Update Frequency**: Recalculate baseline monthly based on actual spend + phase transitions.

---

## Operations Parameters

### OPS-001: MER (Marketing Efficiency Ratio) Thresholds

**Controller**: C-011 (MER Controller)
**Metric**: Total Revenue / Total Ad Spend (weekly calculation)
**Variability Index**: VI-2 (Stable - tied to unit economics)

**Values**:
```
MER_TARGET = 2.5x
MER_GREEN = >2.5x
MER_YELLOW = 1.8x - 2.5x
MER_RED = <1.8x
```

**Rationale**:
- 2.5x minimum: From M3 unit economics (same as ROAS target)
- MER <1.8x: Business model broken (losing money on blended basis)
- MER more conservative than ROAS (includes organic, no attribution inflation)

**Why MER Matters More Than ROAS**:
- **ROAS**: Platform-reported, overstates by 20-40%, ad-attributed only
- **MER**: Actual revenue / actual spend, includes all channels (organic, email, repeat)
- **Example**: ROAS 3.0x, but MER 2.0x → organic traffic declining, email underperforming

**Weekly Calculation** (Monday for previous 7 days):
```
MER = (Shopify revenue Days 1-7) / (Meta ad spend Days 1-7)
```

**Use Case**:
- ROAS for ad optimization (which creative, which audience)
- MER for business viability (is the business profitable on blended basis?)

---

### OPS-002: Inventory Reorder Points

**Controller**: C-012 (Inventory Stockout Controller)
**Metric**: Days of inventory remaining (units / 7-day avg sell-through)
**Variability Index**: VI-4 (Adaptive - adjusts per sell-through velocity)

**Values**:
```
INVENTORY_GREEN = >14 days supply
INVENTORY_YELLOW = 7-14 days supply
INVENTORY_RED = <7 days supply
INVENTORY_CRITICAL = <3 days supply
```

**Rationale**:
- 14 days buffer: Safety stock for unexpected demand spikes
- 7 days yellow: Plan reorder (lead time is 30-45 days from supplier)
- 3 days critical: Emergency mode (expedite order OR pause ad spend)

**Lead Time Assumptions**:
- Supplier production: 21 days
- Shipping (ocean freight): 14 days
- 3PL receiving: 2 days
- **Total lead time**: ~35-40 days

**Reorder Logic**:
```
Current inventory: 500 units
7-day avg sell-through: 25 units/day
Days remaining: 500 / 25 = 20 days

Status: 🟢 Green (>14 days)
Action: None (next check tomorrow)

[5 days later]
Current inventory: 375 units
7-day avg sell-through: 30 units/day (ad spend increased)
Days remaining: 375 / 30 = 12.5 days

Status: 🟡 Yellow (7-14 days)
Action: Place reorder immediately (40-day lead time means stockout risk)
```

**Seasonality Adjustment**:
- Q4 (Nov-Dec): Increase green threshold to 21 days (holiday demand spike)
- Q1 (Jan-Feb): Decrease to 10 days (post-holiday slowdown)

---

## Parameter Tuning Protocol

**Frequency**: Quarterly (or ad-hoc if repeated controller failures)

**Trigger Events**:
1. **Controller fires >20% of days**: Thresholds too tight → loosen yellow/red bands
2. **Controller never fires, but issues occur**: Thresholds too loose → tighten
3. **False positives**: Controller fires, Reactive Protocol finds no real issue → adjust metric or threshold
4. **Cohort data changes**: LTV increases → can tolerate higher CAC → adjust CPA_RED upward

**Tuning Process** (Meta-Control Protocol MC-001):
1. **Collect logs**: Controller trigger frequency, Reactive Protocol outcomes
2. **Operator feedback**: "Was this alert useful?" survey after each red flag
3. **Analyze patterns**: Which controllers are noisy? Which missed issues?
4. **Propose adjustments**: New threshold values, new VI ratings
5. **Test in sandbox**: Replay historical data with new thresholds
6. **Deploy**: Update parameter_registry.md, notify operator, update controllers
7. **Monitor**: Track improvement over next 30 days

**Owner**: Meta Standards Officer (MSO) + CM

**Input Sources**:
- Reactive Protocol trigger logs (`/passets/dashboards/controller_logs/`)
- Operator feedback forms
- Cross-Trade pattern analysis (compare IonWave thresholds to other Trades)

---

## Parameter Version Control

**All parameter changes are logged here with rationale.**

### v1.0.0 (2026-02-12) - Initial Values
- Set initial thresholds based on M3 unit economics + DTC industry benchmarks
- ROAS: 2.5x target (from M3)
- CPA: $45 target (from M3)
- Runway: 60/30/14 days (universal operating principle)
- MER: 2.5x target (same as ROAS, conservative)
- Inventory: 14/7/3 days (based on 35-day lead time)

### [Future Updates]
- v1.1.0 (YYYY-MM-DD): [Description of what changed and why]
- Example: "Increased CPA_RED from $60 to $65 based on 90-day cohort LTV data showing 45% repeat rate (was 30%)"

---

## Parameter Quick Reference Table

| Parameter ID | Name | Target | Green | Yellow | Red | VI | Controller |
|--------------|------|--------|-------|--------|-----|----|-----------|
| REV-001 | Revenue Tolerance | 7-day avg | ±15% | -15 to -30% | <-30% | VI-3 | C-001 |
| REV-002 | Order Volume | 7-day avg | ±15% | -15 to -30% | <-30% | VI-3 | C-002 |
| REV-003 | New Customers | 7-day avg | ±15% | -15 to -30% | <-30% | VI-4 | C-003 |
| REV-004 | AOV | $44 | $37-51 | $35-37, $51-55 | <$35, >$55 | VI-2 | C-004 |
| AD-001 | ROAS | 2.5x | >2.5x | 1.5-2.5x | <1.5x | VI-3 | C-005 |
| AD-002 | CPA | $45 | <$45 | $45-60 | >$60 | VI-3 | C-006 |
| AD-003 | CTR | 1.0% | >1.0% | 0.5-1.0% | <0.5% | VI-4 | C-007 |
| AD-004 | Frequency | <3 | <3 | 3-5 | >5 | VI-4 | C-008 |
| CASH-001 | Runway | 60+ days | >60 | 30-60 | <30 | VI-2 | C-009 |
| CASH-002 | Burn Rate | Phase baseline | ±15% | +15-30% | >+30% | VI-4 | C-010 |
| OPS-001 | MER | 2.5x | >2.5x | 1.8-2.5x | <1.8x | VI-2 | C-011 |
| OPS-002 | Inventory | 14+ days | >14 | 7-14 | <7 | VI-4 | C-012 |

---

## Related Documents

- **Controllers**: `/passets/dashboards/controller_registry.md` (uses these parameters)
- **Dashboard**: `/passets/dashboards/daily_pulse.md` (displays parameter-based status)
- **Unit Economics**: `/data/m3/unit_economics.md` (source of ROAS, CPA, AOV targets)
- **Analytics**: `/data/m30/dashboards_and_reporting.md` (MVD metric definitions)
- **Reactive Protocols**: `/passets/dashboards/reactive_protocols.md` (triggered when red thresholds crossed)

---

## Version History

**v1.0.0 (2026-02-12)**:
- Initial parameter registry
- 12 parameter sets defined (REV-001 through OPS-002)
- Phase-specific baselines documented
- Tuning protocol established
- Quick reference table added
