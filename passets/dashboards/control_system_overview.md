# IonWave Control System — Architecture Overview

**Version**: 1.0.0
**Created**: 2026-02-12
**Purpose**: Explain how controllers, parameters, and reactive protocols work together to maintain operational health
**Audience**: Operator, CM, Studio 3, MSO
**Status**: Active

---

## System Architecture

The IonWave operational control system implements a **closed-loop control architecture** based on Studio 3's ontological primitives (Systems_Architecture_Standards.md).

### Core Components

```
┌──────────────────────────────────────────────────────────────┐
│                     DATA SOURCES (APIs)                      │
│  Shopify  │  Meta Ads  │  Bank/Plaid  │  3PL  │  Support   │
└─────────────────────────┬────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────┐
│              DATA PIPELINE (Google Apps Script)               │
│  Runs daily at 6:00 AM, syncs data to Google Sheet          │
└─────────────────────────┬────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                    METRICS (Measured Values)                  │
│  Revenue, Orders, AOV, ROAS, CPA, CTR, Cash, Inventory, etc.│
└─────────────────────────┬────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                  CONTROLLERS (Monitoring Logic)               │
│  12 controllers execute 5-step loop:                         │
│  1. SENSE (read metric)                                      │
│  2. COMPARE (metric vs parameter threshold)                  │
│  3. DETECT (is deviation outside tolerance?)                 │
│  4. ACT (if yes → trigger Reactive Protocol)                 │
│  5. REPORT (log event to Meta-Control)                       │
└─────────────────────────┬────────────────────────────────────┘
                          │
                ┌─────────┴─────────┐
                │                   │
            🟢 GREEN            🔴 RED
        (no action)        (deviation detected)
                │                   │
                │                   ▼
                │              [REACTIVE PROTOCOLS]
                │                   │
                └───────────────────┴──────────────┐
                                                   │
                                                   ▼
┌──────────────────────────────────────────────────────────────┐
│                  OBSERVERS (Composite Estimators)             │
│  Weekly aggregation of multiple signals into health score:   │
│  • Trade Health Observer (OBS-001)                           │
│    Inputs: Margin, Unit Econ, Lift, Recurrence, Drift, etc. │
│    Output: Composite health score (Strong/Healthy/At Risk)   │
│  • Purpose: Portfolio-level oversight (CM/GM), not ops       │
└─────────────────────────┬────────────────────────────────────┘
                          │
                          ▼
                │                   │
                │                   ▼
                │    ┌──────────────────────────────────┐
                │    │  REACTIVE PROTOCOLS (Actions)    │
                │    │  15 protocols execute corrective │
                │    │  steps to return system to green │
                │    └────────────┬─────────────────────┘
                │                 │
                │                 ▼
                │    ┌──────────────────────────────────┐
                │    │  LOGGING (for Meta-Control)      │
                │    │  Capture: trigger, action, result│
                │    └────────────┬─────────────────────┘
                │                 │
                └─────────────────┴───────────────────────┐
                                                          │
                                                          ▼
┌──────────────────────────────────────────────────────────────┐
│              META-CONTROL (System Learning)                   │
│  Quarterly review: Tune parameters, update protocols,        │
│  add/remove controllers based on performance logs            │
└──────────────────────────────────────────────────────────────┘
```

---

## The Control Loop (5-Step Function)

Every controller executes this loop **daily** (or weekly for periodic controllers):

### 1. SENSE - Read Metric

**What happens**: Controller queries data source (Google Sheet populated by Google Apps Script)

**Example**: C-005 (ROAS Controller) reads yesterday's ROAS from Meta Ads data

**Data**: `ROAS = 2.1x` (platform-reported)

---

### 2. COMPARE - Metric vs Parameter

**What happens**: Controller compares measured value to parameter thresholds from parameter_registry.md

**Example**: C-005 compares ROAS to thresholds:
- `ROAS_GREEN = >2.5x`
- `ROAS_YELLOW = 1.5x - 2.5x`
- `ROAS_RED = <1.5x`

**Comparison**: `2.1x` falls in YELLOW range (1.5x - 2.5x)

---

### 3. DETECT - Deviation?

**What happens**: Controller determines status and whether to trigger action

**Logic**:
```
IF ROAS >= 2.5x:
  status = 🟢 Green
  action = none

IF 1.5 <= ROAS < 2.5x:
  status = 🟡 Yellow
  action = flag for review (no protocol trigger yet)

IF ROAS < 1.5x:
  status = 🔴 Red
  action = TRIGGER REACTIVE PROTOCOL
```

**Result**: Status = 🟡 Yellow, no protocol trigger (just monitoring)

---

### 4. ACT - Trigger Reactive Protocol (if red)

**What happens**: If status = 🔴 Red, controller calls corresponding Reactive Protocol

**Example** (hypothetical: ROAS = 1.3x instead):
```
IF ROAS < 1.5x:
  status = 🔴 Red
  TRIGGER RP-005 (ROAS Recovery Protocol)

  IF consecutive_red_days >= 3:
    TRIGGER RP-006 (Ad Spend Pause - CRITICAL)
```

**Action**: Reactive Protocol executes steps to fix issue (see reactive_protocols.md)

---

### 5. REPORT - Log Event

**What happens**: Controller logs status + action taken to Meta-Control layer

**Log Entry**:
```
Date: 2026-02-12
Controller: C-005 (ROAS Threshold)
Metric: ROAS = 2.1x
Status: 🟡 Yellow
Action: None (monitoring)
Reactive Protocol: N/A
Resolution: N/A
```

**Purpose**: Meta-Control reviews logs quarterly to tune parameters and protocols

---

## Example Scenario: ROAS Drops Below 1.5x

**Day 1 (Feb 12)**:
1. **SENSE**: C-005 reads ROAS = 1.3x from Meta Ads data
2. **COMPARE**: 1.3x < 1.5x threshold (RED)
3. **DETECT**: Deviation detected, status = 🔴 Red
4. **ACT**: Trigger RP-005 (ROAS Recovery Protocol)
5. **REPORT**: Log event to controller_logs/

**RP-005 Execution** (Operator):
- **Step 1**: Diagnostic (10 min) → Identify underperforming campaigns
- **Step 2**: Campaign analysis (15 min) → Sort by ROAS, pause bottom 30%
- **Step 3**: Creative review (15 min) → Launch 3 new creative angles
- **Step 4**: Audience analysis (15 min) → Check for saturation, expand targeting
- **Step 5**: Corrective actions (4 hours) → New creatives live, audience expansion active

**Day 2 (Feb 13)**:
1. **SENSE**: C-005 reads ROAS = 1.4x (still red, but improving)
2. **COMPARE**: 1.4x < 1.5x (RED)
3. **DETECT**: Deviation persists, consecutive_red_days = 2
4. **ACT**: Continue RP-005, monitor closely
5. **REPORT**: Log Day 2 status

**Day 3 (Feb 14)**:
1. **SENSE**: C-005 reads ROAS = 2.3x (new creatives performing!)
2. **COMPARE**: 2.3x is YELLOW (1.5-2.5x)
3. **DETECT**: Deviation reduced, status = 🟡 Yellow
4. **ACT**: None (recovery in progress, exit RP-005)
5. **REPORT**: Log recovery, RP-005 success

**Day 4 (Feb 15)**:
1. **SENSE**: C-005 reads ROAS = 2.7x
2. **COMPARE**: 2.7x > 2.5x (GREEN)
3. **DETECT**: System healthy
4. **ACT**: None
5. **REPORT**: Log green status, RP-005 completed successfully

**Meta-Control Learning**:
- RP-005 worked (ROAS recovered in 3 days via creative refresh + audience expansion)
- Creative fatigue was root cause (CTR also dropped, C-007 fired concurrently)
- **Update**: Add creative rotation cadence to prevent future fatigue (proactive vs reactive)

---

## Controllers vs Observers

### Controllers (Single-Metric Monitoring)
**Purpose**: Monitor individual operational metrics, trigger immediate corrective action

**Characteristics**:
- **Frequency**: Daily (continuous) or weekly (periodic)
- **Inputs**: Single metric (e.g., ROAS, revenue, cash runway)
- **Logic**: Compare metric to threshold → trigger reactive protocol if exceeded
- **Owner**: Operator (executes protocols), CM (oversight)
- **Use Case**: Operational firefighting, tactical responses

**Example**: C-005 (ROAS Controller)
- Monitors: Daily ROAS from Meta Ads
- Threshold: Red if <1.5x
- Action: Triggers RP-005 (ROAS Recovery Protocol)
- Purpose: Immediate response to ad performance degradation

---

### Observers (Composite State Estimators)
**Purpose**: Aggregate multiple signals into portfolio-level health assessment

**Characteristics**:
- **Frequency**: Weekly (or monthly for portfolio-wide observers)
- **Inputs**: Multiple metrics (7+ signals weighted and combined)
- **Logic**: Calculate composite score → map to categorical assessment (Strong/Healthy/At Risk)
- **Owner**: CM (monitors), GM (strategic decisions), MSO (tunes weights)
- **Use Case**: Strategic oversight, trend detection, portfolio health

**Example**: OBS-001 (Trade Health Observer)
- Monitors: 7 signals (Margin, Unit Economics, Lift, Recurrence, Drift, Cash, Risk)
- Formula: H = 5M + 4U + 3L + 2R - X(f+c+r)
- Output: Score 0-140 → Strong/Healthy/At Risk/Critical
- Purpose: Weekly portfolio health check for GM review

---

### Key Differences

| Dimension | Controllers | Observers |
|-----------|-------------|-----------|
| **Inputs** | Single metric | Multiple metrics (weighted composite) |
| **Frequency** | Daily/weekly | Weekly/monthly |
| **Output** | Binary (green/yellow/red) | Categorical + score (Strong/Healthy/At Risk) |
| **Action** | Triggers reactive protocols | Informs strategic decisions, may trigger escalation |
| **Owner** | Operator + CM | CM + GM + MSO |
| **Scope** | Operational (tactical) | Portfolio (strategic) |
| **Example** | C-005 ROAS Controller | OBS-001 Trade Health Observer |

---

### Integration

**Controllers feed Observers**:
- C-005 (ROAS) → feeds into OBS-001 "Lift Velocity" component
- C-009 (Cash Runway) → feeds into OBS-001 "Cash Constraints" component
- C-011 (MER) → feeds into OBS-001 "Unit Economics" component

**Workflow**:
1. **Daily**: Controllers monitor operations → flag immediate issues → operator executes reactive protocols
2. **Weekly**: Observer aggregates controller signals + additional data → produces composite health score → CM reviews → GM makes strategic decisions

**Example Flow**:
- Day 1: C-005 fires (ROAS red), operator executes RP-005 (creative refresh)
- Day 2-7: C-005 monitoring, ROAS recovers to yellow/green
- Monday Week 2: OBS-001 calculates, sees "Lift Velocity" declining (despite ROAS recovery) → flags structural creative fatigue trend → CM schedules strategic review with operator on creative process improvements

---

## Controller Types

### Continuous Controllers (11 of 12)
**Frequency**: Daily (via 6:00 AM sync)

**Controllers**:
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

**Purpose**: Monitor daily operations, catch issues quickly (before they become existential)

---

### Periodic Controllers (1 of 12)
**Frequency**: Weekly (Monday 6:00 AM)

**Controllers**:
- C-011: MER (Marketing Efficiency Ratio)

**Purpose**: Business-level health check (uses 7-day aggregates, less noisy than daily ROAS)

---

## Parameter Types (by Variability Index)

### VI-1 (Immutable)
**None in IonWave system** (architectural constants would be VI-1, e.g., "a day = 24 hours")

---

### VI-2 (Stable)
**Frequency**: Modified only during governance review (annual or major pivot)

**Parameters**:
- AOV_TARGET: $44 (tied to product pricing)
- RUNWAY_GREEN/YELLOW/RED: 60/30/14 days (universal operating principle)
- MER_TARGET: 2.5x (tied to unit economics)

**Why stable**: These reflect fundamental business model assumptions (pricing, unit economics). Changes rarely.

**Update trigger**: Product pricing change, unit economics pivot, business model shift

---

### VI-3 (Slow-moving)
**Frequency**: Revised when cohort data shows drift (quarterly review)

**Parameters**:
- REVENUE/ORDER/NEW_CUSTOMER tolerance bands: ±15% green, -30% red
- ROAS_TARGET: 2.5x (adjusted based on LTV data)
- CPA_TARGET: $45 (adjusted based on LTV data)

**Why slow-moving**: Based on statistical baselines (DTC industry norms, cohort LTV). Adjust when data proves thresholds too tight/loose.

**Update trigger**: Cohort analysis shows LTV change, DTC benchmarks shift, controller fires too often/rarely

---

### VI-4 (Adaptive)
**Frequency**: Frequently tuned, Trade-specific

**Parameters**:
- NEW_CUSTOMER_FLOOR: 3/day (ICL-1) → 10/day (ICL-2) → 20/day (ICL-3)
- BURN_BASELINE: $300/day (ICL-0) → $500/day (ICL-1) → $800/day (ICL-2)
- INVENTORY reorder points: 14/7/3 days (adjusted per sell-through velocity)
- CTR_GREEN/YELLOW/RED: Adjusted per creative type, audience maturity

**Why adaptive**: These change as business scales (customer volume increases, burn rate increases, inventory velocity changes).

**Update trigger**: Phase transition (ICL-0 → ICL-1), sell-through rate changes, creative performance evolves

---

### VI-5 (Fully Local)
**Frequency**: Operator discretion within guardrails

**None in current system** (would be tactical decisions like "which creative angle to test next")

---

## Reactive Protocol Urgency Levels

### P0 (CRITICAL - Immediate Action)
**Response Time**: <1 hour

**Protocols**:
- RP-006: Ad Spend Pause (ROAS <1.5x for 3+ days)
- RP-010: Cash Crisis (<30 days runway)
- RP-011: Existential Cash (<14 days runway)
- RP-015: Stockout Prevention (<3 days inventory)

**Characteristics**: Business-threatening, requires immediate operator attention, escalates to CM/Studio 3

---

### P1 (Urgent - Same Day)
**Response Time**: <4 hours

**Protocols**:
- RP-001: Revenue Recovery
- RP-002: Order Volume Investigation
- RP-003: Acquisition Funnel Diagnostic
- RP-005: ROAS Recovery
- RP-007: CPA Optimization
- RP-008: Creative Fatigue
- RP-009: Audience Expansion
- RP-014: Emergency Reorder

**Characteristics**: Operational issues, fixable with quick action, can worsen if ignored

---

### P2 (Important - Within 24 hours)
**Response Time**: <24 hours

**Protocols**:
- RP-004: AOV Structural Analysis
- RP-012: Burn Rate Audit

**Characteristics**: Diagnostic protocols, not immediately threatening, need investigation

---

## Dashboard Integration

### Daily Pulse Dashboard (daily_pulse.md)

**What it shows**:
- Metric values (revenue, orders, ROAS, etc.)
- Status indicators (🟢🟡🔴) generated by controllers
- "Fires & Issues" checklist (active red flags)
- "One Thing to Fix Today" (highest priority reactive protocol)

**How it works**:
1. **6:00 AM**: Google Apps Script syncs API data → Google Sheet
2. **6:05 AM**: Controllers execute (compare metrics to parameters)
3. **6:10 AM**: Dashboard updated with status indicators
4. **6:15 AM**: If 🔴 Red → Email/Slack alert sent to operator
5. **8:00 AM**: Operator reviews dashboard, executes reactive protocol if needed

**Example Dashboard (Feb 12, 2026)**:
```
### 💰 Revenue & Orders (Yesterday: Feb 11)
| Metric | Value | vs 7-Day Avg | Status |
|--------|-------|--------------|--------|
| Revenue | $1,247 | +2% | 🟢 |
| Orders | 28 | +5% | 🟢 |
| New Customers | 19 | +3% | 🟢 |

### 📈 Ad Performance
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| ROAS | 2.1x | >2.5x | 🟡 |  ← C-005 YELLOW
| CPA | $38 | <$45 | 🟢 |
| CTR | 1.3% | >1.0% | 🟢 |

### 🚨 Fires & Issues
**Active Issues**: None
All systems operational. ROAS below target but not critical.

### 🎯 One Thing to Fix Today
**No critical issues. Focus on**:
> Monitor ROAS closely. If drops below 1.5x, trigger RP-005 (ROAS Recovery).
```

---

## Meta-Control Layer

**Purpose**: The system learns and improves itself

**Frequency**: Quarterly (or after 10+ triggers of any protocol)

**Process**:
1. **Collect Logs**: Controller trigger frequency, reactive protocol outcomes
2. **Operator Feedback**: Survey after each protocol ("Was this useful?")
3. **Analyze Patterns**: Which controllers are noisy? Which miss issues?
4. **Propose Adjustments**: New thresholds, new protocols, retired controllers
5. **Test**: Replay historical data with new parameters
6. **Deploy**: Update registries, notify operator
7. **Monitor**: Track improvement over 30 days

**Example Meta-Control Actions**:

**Scenario 1: Controller Fires Too Often**
- C-007 (CTR Controller) fires 15 times in 30 days (50% of days)
- Operator feedback: "Most alerts were false positives, CTR recovered next day"
- **Meta-Control Action**: Loosen CTR_RED from <0.5% to <0.4% (tighter threshold)
- **Result**: C-007 fires 3 times in next 30 days (10%, more useful signals)

**Scenario 2: Controller Never Fires**
- C-010 (Burn Rate Controller) fires 0 times in 90 days
- CM review: Burn rate spiked 2x but stayed within +30% threshold
- **Meta-Control Action**: Tighten BURN_RED from +30% to +20%
- **Result**: C-010 fires when burn spikes, RP-012 (Burn Rate Audit) catches overspending earlier

**Scenario 3: Missing Controller**
- Operator reports: "Product page conversion rate dropped 50%, no alert"
- Gap identified: No controller monitoring conversion rate
- **Meta-Control Action**: Create C-013 (Conversion Rate Controller) with parameters:
  - `CVR_GREEN = >3.0%`
  - `CVR_YELLOW = 2.0-3.0%`
  - `CVR_RED = <2.0%`
  - Triggers RP-016 (Conversion Rate Diagnostic - new protocol)
- **Result**: Conversion rate issues caught before revenue drops

---

## System Maturity Roadmap

### Phase 1: Manual (Weeks 1-4, ICL-0)
**Current State**: Operator manually checks dashboard, executes protocols

**Activities**:
- Operator reviews daily_pulse.md every morning
- Manually calculates status indicators (🟢🟡🔴)
- Executes reactive protocols when thresholds crossed
- Logs outcomes in controller_logs/

**Automation**: None (full manual)

**Purpose**: Validate thresholds, test protocols, build muscle memory

---

### Phase 2: Semi-Automated (Weeks 5-12, ICL-1-2)
**Target State**: Controllers execute automatically, operator receives alerts

**Activities**:
- Google Apps Script syncs data daily (6:00 AM)
- Controllers execute automatically (compare metrics to parameters)
- Email/Slack alerts sent if 🔴 Red detected
- Operator executes reactive protocols
- Logs automatically captured

**Automation**: Data sync + controller execution + alerting

**Purpose**: Reduce operator cognitive load, catch issues faster

---

### Phase 3: Fully Automated (Weeks 13+, ICL-3+)
**Future State**: Some reactive protocols execute automatically

**Activities**:
- Controllers execute + alert (same as Phase 2)
- **New**: Simple protocols auto-execute (e.g., RP-006 Ad Spend Pause = auto-pause campaigns if ROAS <1.5x for 3 days)
- Operator notified of auto-actions, can override
- Complex protocols still require operator (RP-010 Cash Crisis, RP-013 Business Model Review)

**Automation**: Data sync + controllers + alerting + simple reactive protocols

**Purpose**: Proactive protection (auto-pause losing ads before too much cash burned)

---

## Success Metrics (for Control System)

**The control system is successful if**:

1. **Early Detection**: Issues caught in YELLOW (warning) before becoming RED (crisis)
   - **Target**: 70%+ of issues resolved at yellow, never reach red

2. **Fast Resolution**: Reactive protocols resolve issues quickly
   - **Target**: 80%+ of protocols resolve within 48 hours

3. **Low False Positive Rate**: Alerts are actionable, not noise
   - **Target**: 90%+ of red alerts require action (not false positives)

4. **Operator Confidence**: Operator trusts system to flag real issues
   - **Target**: 95%+ operator satisfaction ("this alert was useful")

5. **Meta-Control Improvement**: System gets better over time
   - **Target**: Controller effectiveness improves 10%+ per quarter (fewer false positives, faster resolution)

---

## Quick Reference

### For Operators

**Daily Question**: "What's the status?"
1. Open daily_pulse.md
2. Scan status indicators (🟢🟡🔴)
3. If all green: Proceed with planned work
4. If any yellow: Monitor closely, may need action today
5. If any red: Read "One Thing to Fix Today", execute reactive protocol

**Red Flag Response**:
1. Identify which controller fired (C-001 through C-012)
2. Read corresponding reactive protocol (RP-001 through RP-015)
3. Execute steps, document in controller_logs/
4. Update daily_pulse.md when resolved

---

### For CMs (Oversight)

**Weekly Question**: "Is the operator catching issues?"
1. Review controller_logs/ for past week
2. Check: How many red flags? How quickly resolved?
3. Check: Any repeated issues (same controller firing weekly)?
4. If repeated: Trigger Meta-Control review (parameter tuning needed)

**Monthly Question**: "Is the control system effective?"
1. Analyze: Controller trigger frequency (too often = noise, too rare = missing issues)
2. Analyze: Reactive protocol success rate (resolving issues vs escalating)
3. Propose: Parameter adjustments, new controllers, protocol updates

---

### For MSO (Meta-Control)

**Quarterly Question**: "How can we improve the system?"
1. Collect: 90 days of controller logs
2. Analyze: Patterns (which controllers noisy, which protocols effective)
3. Survey: Operator feedback ("which alerts were useful?")
4. Propose: Updated parameters, new controllers, revised protocols
5. Test: Replay historical data with new settings
6. Deploy: Update registries, notify operator
7. Monitor: Track improvement next quarter

---

## Related Documents

**Core System**:
- `/passets/dashboards/controller_registry.md` — 12 controller definitions
- `/passets/dashboards/parameter_registry.md` — Numeric thresholds and tolerances
- `/passets/dashboards/reactive_protocols.md` — 15 corrective action procedures
- `/passets/dashboards/daily_pulse.md` — Daily dashboard (displays controller outputs)

**Data Pipeline**:
- `/passets/dashboards/data_pipeline_spec.md` — API → Google Apps Script → Google Sheet

**Architectural Foundation**:
- `/standards/Systems_Architecture_Standards.md` — Ontological primitives (Controllers, Parameters, Protocols)

**Strategic Context**:
- `/data/m3/unit_economics.md` — Source of ROAS, CPA, AOV targets
- `/data/m30/dashboards_and_reporting.md` — MVD metric definitions

---

## Version History

**v1.0.0 (2026-02-12)**:
- Initial control system overview
- 5-step controller loop documented
- Example scenario (ROAS recovery) illustrated
- Controller types, parameter VI levels, protocol urgency levels defined
- Dashboard integration explained
- Meta-Control process documented
- System maturity roadmap (manual → semi-automated → fully automated)
- Success metrics established
- Quick reference guides for Operator, CM, MSO

---

**Questions? Issues?**
- Log in `/passets/decisions/decision_log.md`
- Escalate to CM or MSO for system improvements
