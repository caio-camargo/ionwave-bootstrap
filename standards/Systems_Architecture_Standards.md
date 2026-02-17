# Systems Architecture Standards

**Version**: 1.0.0
**Author**: Caio, Claude (extracted from Sprint_STAGE_5)
**Date Created**: 2026-02-06
**Last Updated**: 2026-02-06
**AI Model**: claude-sonnet-4-5-20250929
**Purpose**: Formal definitions of Studio 3's ontological primitives and system architecture elements
**Status**: Active
**Source**: Extracted from `Caio __ Danilo, Rhen Sprint_STAGE_5.md`

---

## Overview

This document defines the formal ontological primitives that structure Studio 3's system architecture. These primitives provide a consistent vocabulary for discussing system design, control mechanisms, and operational interfaces.

**12 Ontological Primitives**: Architecture, Interface Definitions, Protocols, Parameters, Controllers, Observers, Passets, Void Space, Content, OpKit, Metric, Meta-Control

**Core Principle**: The system operates through formal **protocols** (how work happens), constrained by **parameters** (numeric bounds), monitored by **controllers** (deviation detection), and improved by **meta-control** (system learning).

---

## Ontological Primitives

### 1. Architecture

**Definition**: The structural components of the system that define what exists.

Architecture is stable and evolves rarely. It expresses the "shape" of the system:

- **Machines** - Discrete operational stages (e.g., Imagination, Implementation, Live Environment)
- **Passet Structure** - Standardized information containers
- **Roles** - Actors who execute protocols (Operator, CM, GM, Meta Standards Officer, Venture Partner)
- **Meta-Control System** - How control elements are monitored and updated

**Characteristics**:
- Architecture describes existence and boundaries of components
- Changes to architecture are rare and require high-level approval
- Architecture hosts Interface Definitions

### 2. Interface Definitions

**Definition**: Specifications for the structure of information at system boundaries.

Interface Definitions determine what must exist for a protocol to run, and what form outputs must take.

**Types**:
- **Passet schemas** - Folder structure, void spaces, content types
- **Dashboards** - Tracking layouts and visualization formats
- **Document formats** - Standardized templates and metadata requirements

**Characteristics**:
- Semi-stable: versioned, but expected to evolve through Meta-Control
- Define structure, not behavior (behavior is defined by Protocols)
- Are constrained by Architecture
- Constrain Protocols

### 3. Protocols

**Definition**: The minimal executable unit of work in the system. Every action occurs through a Protocol.

**Protocol Types**:

#### Process Protocols
Continuous SOPs executed inside Machines. They chain, branch, and can be nested.

**Example**: Daily check-in cadence, deliverable submission order, handoff procedures

#### Gate Protocols
Boundary procedures that return pass / fail / recycle and route entities into the next Process chain.

**Example**: Imagination Gate Assessment, Launch Assessment

#### Reactive Protocols
Executed when a monitored metric deviates from its parameter range; triggered by Controllers.

**Example**: Budget overrun response, performance recovery plan

#### Meta-Control Protocols
The system's learning layer: they revise Protocols, Parameters, and Interface Definitions themselves.

**Example**: Quarterly protocol audit, parameter tuning review

**Characteristics**:
- Express behavior, not structure or numeric tolerances
- Use Parameters for numeric constraints
- Are constrained by Interface Definitions
- Can trigger other Protocols

**Every Protocol has**:
- **ID** - Unique identifier (e.g., P-001, G-001, R-001, MC-001)
- **Type** - Process / Gate / Reactive / Meta-Control
- **Trigger** - What initiates execution
- **Owner Role** - Responsible party
- **Inputs** - Required information (Passets, metrics, parameters)
- **Steps** - Ordered actions
- **Controllers** - Checks within the protocol
- **Outputs** - Results (updated Passets, state transitions, decisions)
- **Failure Modes** - What can go wrong and linked Reactive Protocol

### 4. Parameters

**Definition**: Numeric values, thresholds, and tolerance ranges that shape how protocols run.

**Examples**:
- Budget caps ($10,000 ad testing budget)
- Pass/fail thresholds (ROAS ≥ 2.0)
- Tolerance bands (inventory reorder at ≤21 days supply)
- Cadence windows (Imagination Sprint = 14 days)
- Viability targets (100+ ads minimum)

**Characteristics**:
- Parameters are not architecture and not protocol logic
- They are the dials that tune the system
- Used by Protocols
- Enforced by Controllers

**Variability Index (VI)**: Every parameter carries a VI rating (1-5) indicating how stable it is:

- **VI 1 - Immutable** - Architectural constants, never change
- **VI 2 - Stable** - Expected to remain unchanged, modified only during governance review
- **VI 3 - Slow-moving** - Revised when cohort data shows drift (e.g., ad volumes)
- **VI 4 - Adaptive** - Frequently tuned values (e.g., reorder points per Trade)
- **VI 5 - Fully Local** - Trade-level discretion within guardrails (e.g., ad angles)

**Parameter Attachment**: Parameters attach to the thing they constrain:
- Architecture Elements (Machines, Passets, Interfaces)
- Protocols (Process, Gate, Reactive)
- Controllers
- Trade Instances

### 5. Controllers

**Definition**: Monitoring mechanisms that compare metrics to parameters and trigger Reactive Protocols when tolerances are exceeded.

**Function**:
1. **Sense** - Read Metric
2. **Compare** - Metric vs Parameter
3. **Detect** - Deviation?
4. **Act** - If deviation → call Reactive Protocol
5. **Report** - Log event to Meta-Control layer

**Controller Types**:

#### Continuous Controllers
High-frequency, near real-time checks (daily/weekly).

**Examples**: ROAS trending below threshold, CAC spike, inventory reaching reorder point

#### Periodic Controllers
Triggered by time schedules.

**Examples**: Monthly business review, quarterly financial snapshot, planning cycle renewal

#### Event Controllers
Triggered by specific events.

**Examples**: Operator misses check-in, supplier fails to deliver, payment processor flags account

#### Structural Controllers
Operate on system artifacts rather than business performance.

**Examples**: Passet completeness checks, OpKit version mismatches, documentation drift

**Characteristics**:
- Controllers are not Protocols - they are monitoring mechanisms that call Protocols
- Primarily executed by CMs
- Attach to Machines, Passets, Trade Instances, or Studio-Level Oversight
- Report upward to Meta-Control
- Trigger Reactive Protocols

### 6. Observers

**Definition**: Composite state estimators that aggregate multiple metrics (signals) into a single legible assessment or score.

**Function**:
1. **Aggregate** - Combine multiple input signals (metrics)
2. **Weight** - Apply importance weighting to each signal
3. **Calculate** - Produce composite score or state estimate
4. **Classify** - Map score to categorical assessment (e.g., "Strong", "Healthy", "At Risk")
5. **Diagnose** - Provide fault-tree patterns to explain the assessment

**Difference from Controllers**:
- **Controller**: Monitors single metric → compares to threshold → triggers protocol
- **Observer**: Monitors multiple metrics → produces composite state → informs strategic decisions

**Observer Types**:

#### Continuous Observers
Calculate composite score on regular cadence (daily/weekly/monthly).

**Examples**: Trade Health Observer, PMF Observer, Portfolio Health Observer

#### Diagnostic Observers
Analyze patterns across metrics to identify root causes.

**Examples**: Churn Risk Observer (combines retention, engagement, support tickets, NPS)

**Characteristics**:
- Observers do not trigger Reactive Protocols directly (they inform Controllers or dashboards)
- Primarily executed by CM (portfolio oversight) or MSO (system health)
- Attach to Trade Instances or Portfolio-Level Oversight
- Report to Meta-Control for weighting adjustments
- May feed into Controllers (e.g., Trade Health Observer output becomes input to C-013)

**Observer Schema**:
Every Observer has:
- **ID** - Unique identifier (e.g., OBS-001, OBS-002)
- **Name** - Descriptive name (e.g., "Trade Health Observer")
- **Type** - Continuous / Diagnostic
- **Input Signals** - List of metrics with weights
- **Calculation Method** - Formula or algorithm
- **Output** - Score range and categorical mappings
- **Diagnostic Patterns** - Fault trees for interpretation
- **Frequency** - How often calculated
- **Owner Role** - Who monitors the output
- **Use Case** - When to reference this observer

**First Instance**: Computational PMF Observer (M0 OpKit)
- **10 input signals**: Sean Ellis score (25%), Retention M2 (20%), Organic % (15%), NPS (15%), CAC trend (10%), Referral % (5%), Explanation cost, Price sensitivity, Inbound growth, Time to value
- **Score bands**: 0-30 (No PMF), 30-50 (Early PMF), 50-70 (Achieved PMF), 70+ (Strong PMF)
- **5 diagnostic patterns**: Missing core value, weak retention, poor word-of-mouth, unsustainable CAC, unclear positioning
- **Purpose**: Early thesis-level assessment of product-market fit

**Second Instance**: Trade Health Observer (for Live Trades)
- **7 input signals**: Margin Stability, Unit Economics, Lift Velocity, Revenue Recurrence, Operator Drift, Cash Constraints, Risk Exposure
- **Formula**: H = 5M + 4U + 3L + 2R - X(f+c+r) where each component is normalized 0-10 scale
- **Score bands**: <20 (Critical), 20-40 (At Risk), 40-60 (Healthy), 60+ (Strong)
- **Purpose**: Portfolio-level monitoring of Trade operational health

### 7. Passets

**Definition**: Structured information containers (Drive folders) that define inputs and outputs for each Machine. The Trade exists and is visible to the Studio in the form of Passets.

**Structure**:
- Created empty (void spaces + content types)
- Filled through Process Protocols
- Either frozen or kept live based on role

**Key Passet Types**:

#### Meta Passet
Studio-only control and memory layer. Never freezes, continuously updated. Operator never sees it.

#### Imagination Passet
Strategic planning and business architecture. Staged → filled → frozen at Imagination Gate.

#### Implementation Passet
Turn validated strategy into launch-ready business. Staged → filled → frozen at Launch Assessment.

#### Live Trade Passet
Operational cockpit for running business. Created at launch, continuously updated, persists until exit.

#### Fundraising Passet
Convert validated performance into investor-ready materials. Staged → filled → frozen after close.

**Characteristics**:
- Passets are the Studio's primary interface layer
- Standardized schemas ensure consistency
- Void spaces are filled with Content Instances
- Some freeze (historical record), others stay live (operational)

### 8. Void Space

**Definition**: A box where something goes - a blank to be filled with content. Standardizes structures and relationships according to content type.

**Characteristics**:
- Passets contain Void Spaces
- Content fills Void Spaces
- Ensures consistent structure across all Trades

### 9. Content

**Definition**: What goes in a void space.

**Content Types**:
- **Fixed** - Same in every instance (e.g., standard template text)
- **Fixed Type** - Same kind, varying per instance (e.g., a spreadsheet, an image)
- **Variable Type** - Could be different formats (e.g., text doc or multimedia presentation)

**Content Instance**: A specific version of a content type created for a particular passet (e.g., "Strategic-Foundation-Analysis-Jan2025.pdf")

### 10. OpKit

**Definition**: Production support bundle containing everything needed to produce high-quality deliverables. Scaffolds execution for specific Passet deliverables.

**OpKit Types**:

#### Production OpKit
For repeatedly created deliverables across multiple Trades.

**Contains**: Instructions, Template, Graded Examples (A/B/C), Rubric

**Example**: Strategic Thesis OpKit, Market Landscape Map OpKit

#### Foundation OpKit
For singular evolving foundational documents.

**Contains**: Target document, Brief, Design rationale, Historical record

**Example**: Documentation Standards OpKit, Protocol Creation OpKit

**Characteristics**:
- OpKits translate abstract intent ("what must exist") into executable form ("how it is made, to what standard")
- Attached to deliverables by folder or tag
- Stored in Content Library (read-only for Operators/CMs)
- Only modifiable through Meta-Control

### 11. Metric

**Definition**: A measured value tracked over time. The raw input to Controllers.

**Characteristics**:
- Metrics are observed values (e.g., ROAS = 2.3, CAC = $45)
- Parameters are target values or thresholds (e.g., ROAS ≥ 2.0, CAC ≤ $50)
- Controllers compare Metrics to Parameters

**Relationship**:
```
Metric (measured) → Controller (compares to) → Parameter (threshold)
  → If deviation → Reactive Protocol
```

### 12. Meta-Control

**Definition**: The Studio's architectural mechanism for supervising the system itself. Operates on the rules that operate on Trades, not on Trades directly.

**Functions**:

#### Protocol Governance
Evaluates performance of Protocols across cohorts. Updates or replaces protocols when systemic drift appears.

#### Parameter Tuning
Reviews parameters at VI 3-5. Adjusts numeric values when repeated deviations indicate misalignment.

#### Controller Oversight
Supervises portfolio of controllers:
- Determines which metrics require controllers
- Detects controllers that fire too often (overly tight parameters)
- Detects controllers that rarely fire (overly loose parameters)
- Creates new controllers / retires ineffective ones

#### Interface Definition Maintenance
Modifies Passet schemas, void spaces, templates when patterns indicate interface structure is misaligned.

**Characteristics**:
- Executed primarily by Meta Standards Officer (MSO)
- Uses inputs from Reactive Protocol logs, system reviews, cross-Trade pattern analysis
- Produces updated protocols, tuned parameters, revised controllers, modified interfaces
- Changes propagate forward into next cohort

---

## System Relationships

The primitives relate hierarchically:

```
Architecture → hosts → Interface Definitions
Interface Definitions → constrain → Protocols
Protocols → use → Parameters
Parameters → are enforced by → Controllers
Controllers → trigger → Reactive Protocols
Reactive Protocols → return system to → Parameter tolerances
Meta-Control → modifies → Protocols, Parameters, Interface Definitions
```

**Control Flow**:
```
[Process Protocols] → forward execution
         ↓
[Gate Protocols] → pass/fail/recycle decisions
         ↓
[Controllers] → monitor metrics vs parameters
         ↓
[Reactive Protocols] → corrections when out of bounds
         ↓
[Meta-Control] → learns from patterns, tunes system
```

---

## Application to IonWave Bootstrap

**Current State**:
- **Passets**: Represented as structured JSON data layer (`data/` folder structure)
- **Interface Definitions**: Document metadata standards, deliverable structure standards
- **Protocols**: Implicit in process documents (e.g., Competitive Intelligence Protocol)
- **Parameters**: Quality scores, confidence grades (A/B/C/D)
- **Controllers**: Formalized in `/passets/dashboards/controller_registry.md` (12 controllers for operational monitoring)
- **Observers**: Computational PMF Observer (M0 OpKit), Trade Health Observer (to be implemented)
- **OpKits**: Registry established in `/data/opkits/registry.json` (9 OpKits mapped to TUPs)
- **Meta-Control**: Partially implemented through versioning, session logs, decision tracking

**Next Evolution**:
As the Bootstrap system matures toward full Studio 3 operation, these primitives will become more formalized with explicit Protocol IDs, Controller definitions, Parameter registries, and Meta-Control processes.

---

## Version History

**v1.0.0 (2026-02-06)**:
- Initial extraction from Sprint_STAGE_5 document
- Formalized 11 ontological primitives
- Added system relationships diagram
- Added application notes for IonWave Bootstrap context

**v1.1.0 (2026-02-12)**:
- Added Observer primitive (12th primitive, from REC-002c decision)
- Observer definition: composite state estimators that aggregate multiple metrics
- Differentiated Observers from Controllers (composite vs single-metric monitoring)
- Examples: Computational PMF Observer (M0), Trade Health Observer (OBS-001)
- Updated numbering for subsequent primitives (Passets now #7, Meta-Control now #12)
- Updated application notes: Controllers formalized, Observers with Trade Health implementation
