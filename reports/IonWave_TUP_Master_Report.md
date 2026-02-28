# IonWave Trade #84 - Master TUP Report

**Generated:** 2026-02-09
**Project:** IonWave Bootstrap (Studio 3 Imagination Generation System)
**Total Migrated TUPs:** 19
**System Version:** TUP-based architecture v1.0

---

## 📊 Executive Summary

This comprehensive report aggregates all completed Trade Unit Projects (TUPs) for IonWave Trade #84, a marine plasma electrolyte supplement DTC business. Each TUP has been workshopped using the TUP Workshop Protocol (TWP-001 v2.0.0), including expert persona dialogue, confidence grading, and OpKit generation.

### Quality Overview

| Quality Tier | Count | TUPs |
|--------------|-------|------|
| **High (8.0+)** | 3 | M27 (8.5), M26 (8.2), M21 (8.0) |
| **Good (7.0-7.9)** | 1 | M10 (7.4) |
| **Moderate (6.0-6.9)** | 1 | M0 (6.5) |
| **Not Graded** | 14 | M9, M14, M16-M20, M22-M25, M28-M30 |

**Total Content:** ~1.5MB of human-readable TUP documentation across 19 projects

---

## 🎯 Business Hypotheses System

The IonWave business model is built on 19 testable hypotheses (9 top-level + 10 sub-hypotheses). These hypotheses link directly to TUP content and drive validation tracking.

### Hypothesis Registry Summary

**Total Hypotheses:** 19 (9 parent + 10 children)
**By State:**
- ASSUMED: 19
- TESTING: 0
- VALIDATED: 0
- INVALIDATED: 0

**By Severity:**
- CRITICAL: 4
- HIGH: 4
- MEDIUM: 8
- LOW: 3

**By Confidence Grade:**
- A-grade: 0
- B-grade: 1 (HYP-004: Gross Margin - 67%)
- C-grade: 5 (HYP-001, HYP-002, HYP-003.1, HYP-007, HYP-008)
- D-grade: 13

### Critical Hypotheses

#### HYP-001: Customer Acquisition Cost (CAC)
- **Value:** $35 (range: $30-45)
- **Grade:** C
- **Severity:** CRITICAL
- **Status:** ASSUMED
- **Description:** Can acquire customers at ≤$40 CAC through Meta ads and optimize to ≤$35 within 6 months
- **Kill Criteria:** CAC >$60 for 14 days (existential)
- **Referenced in:** 14 documents (M14, M17, M23, M30, M9 primary)

#### HYP-002: Subscription Attach Rate
- **Value:** 50% (target: 60%)
- **Grade:** C
- **Severity:** HIGH
- **Status:** ASSUMED
- **Description:** ≥50% of first-time customers will opt for subscription
- **Kill Criteria:** <35% after first 100 orders
- **Referenced in:** 14 documents (M10, M21, M17, M9, M28 primary)

#### HYP-003: Monthly Subscriber Churn Rate
- **Value:** 12% (risk range: 8-15%)
- **Grade:** D (composite 1.40/4.0, approaching C)
- **Severity:** HIGH → CRITICAL
- **Status:** ASSUMED (decomposed into 4 sub-hypotheses)
- **Description:** Subscriber churn will be ≤12% per month
- **Kill Criteria:** >15% for 2 consecutive months
- **Sub-hypotheses:**
  - HYP-003.1: Product Efficacy (40% weight, C-grade via Seaonic proxy)
  - HYP-003.2: Early-Life Churn (30% weight, D-grade)
  - HYP-003.3: Retention Infrastructure (20% weight, D-grade)
  - HYP-003.4: Consumption-Cadence Match (10% weight, D-grade)
- **Referenced in:** 13 documents (M21, M17, M19, M20, M30 primary)

#### HYP-004: Gross Margin Sustainability
- **Value:** 67% ($20 COGS at $59 price)
- **Grade:** B
- **Severity:** MEDIUM
- **Status:** ASSUMED
- **Description:** Can maintain 65-69% gross margin at scale
- **Kill Criteria:** COGS >$25 makes unit economics non-viable
- **Open Issue:** ISS-001 - 67% margin target unachievable with subscription pricing (needs revision to 62-64% blended)
- **Referenced in:** 11 documents (M10, M24, M25, M28 primary)

#### HYP-005: Blended Customer Lifetime Value (LTV)
- **Value:** $106 (range: $64-$159)
- **Grade:** D
- **Severity:** CRITICAL
- **Status:** ASSUMED
- **Description:** Blended LTV (60% subscribers, 40% one-time) will be ≥$106
- **Kill Criteria:** LTV:CAC <2.5x after 6 months
- **Dependency:** Derived from HYP-001, HYP-002, HYP-003, HYP-004
- **Referenced in:** 8 documents (M10, M17, M19, M21 primary)

#### HYP-006: Organic & Referral Lift
- **Value:** 10% (range: 5-20%)
- **Grade:** D (composite 1.0/5.0)
- **Severity:** MEDIUM
- **Status:** ASSUMED (decomposed into 5 sub-hypotheses)
- **Description:** 10% of customer volume from organic/referral sources
- **Sub-hypotheses:**
  - HYP-006.1: Referral Program (35% weight, 3-4% volume, D-grade)
  - HYP-006.2: SEO & Content (25% weight, 2-3% volume, D-grade)
  - HYP-006.3: Influencer Seeding (20% weight, 2-3% volume, D-grade)
  - HYP-006.4: PR & Earned Media (10% weight, 1-2% volume, D-grade)
  - HYP-006.5: Community & WOM (10% weight, 1-2% volume, D-grade)
- **Referenced in:** 13 documents (M22, M23, M28, M29, M16 primary)

#### HYP-007: Timeline to $30K MRR
- **Value:** 18 months (range: 6-24+ months)
- **Grade:** C
- **Severity:** CRITICAL
- **Status:** ASSUMED
- **Description:** IonWave will reach $30K MRR within 18 months (revised from 12 months)
- **Validation Checkpoints:** $8-10K MRR by Month 6, $20K+ by Month 12
- **Referenced in:** 8 documents (Financial Model, M25, M30 primary)

#### HYP-008: Capital Sufficiency
- **Value:** $75-100K total (staged: $30-50K initial + $40-50K follow-on at Month 6)
- **Grade:** C
- **Severity:** CRITICAL
- **Status:** ASSUMED
- **Description:** Staged capital raise will fund path to $30K MRR
- **Kill Criteria:** Can't raise follow-on at Month 6 → slow bootstrap (24-30mo) or kill
- **Referenced in:** 7 documents (Financial Model, M25, M30 primary)

#### HYP-009: Pre-Launch Demand Generation
- **Value:** 500+ qualified leads pre-launch
- **Grade:** D
- **Severity:** MEDIUM
- **Status:** ASSUMED
- **Description:** Pre-launch waitlist and community building will generate 500+ qualified leads
- **Surfaced by:** CSP-001 (speed compression scenario)
- **Referenced in:** 1 document (CSP-001 case study)

---

## 📁 TUP Inventory

### BCL-0: Strategic Foundation

#### M0 - Trade Thesis
- **Status:** Migrated | **Quality:** 6.5/10 | **Version:** 1.4.0
- **Cluster:** BCL-0 (Strategic Foundation)
- **Sheet Count:** 5 files
- **Workshop:** 2026-02-04 to 2026-02-06
- **Personas:** Skeptical Investor, Customer Anthropologist, Competitive Strategist
- **Dialogue:** 8 rounds, saturated, 5 upgrades, 3 resolved
- **Key Outputs:**
  - Strategic thesis (thesis.json) - CANONICAL
  - Assumptions register (6 assumptions)
  - Interview insights synthesis (20 LMNT proxy insights)
  - Narrative hypotheses table (6 hypotheses with Evidence For/Against)
  - ODD-1 Complete Thesis (v0, SUPERSEDED but retained for TAM/SAM/SOM)
- **Key Findings:**
  - Narrow marine plasma positioning validated by Porter's + ICP
  - Sub-segment sized at $300K-$1.5M (thesis reframed)
  - Right to Win: marine plasma positioning (singular, not multiple)
  - Capital tension flagged (no financial model linked)
  - $30K MRR Year 1 target needs validation
- **Feeds Into:** M26, M27, M5, M3, M35
- **Requires:** None (foundational)
- **Next Action:** Build/audit M3 Financial Model; validate $30K MRR Year 1 target; research Female Wellness ICP; collect fasting-specific VOC

---

### BCL-1: Product & Supply

#### M5 - Formulation
- **Status:** Not Migrated
- **Cluster:** BCL-1 (Product & Supply)
- **Source Files:** 05a_product_strategy, 05b_formulation_supply, 36_reference_specifications

---

### BCL-2: Finance & Legal

#### M2 - Entity & Legal
- **Status:** Not Migrated
- **Cluster:** BCL-2 (Finance & Legal)
- **Source Files:** 17_legal_compliance, 33_governance_structure

#### M3 - Financial Model
- **Status:** Not Migrated
- **Cluster:** BCL-2 (Finance & Legal)
- **Source Files:** 06_unit_economics, 08_financial_model

#### M4 - Fundraising
- **Status:** Not Migrated
- **Cluster:** BCL-2 (Finance & Legal)
- **Source Files:** 20_fundraising

---

### BCL-3: Infrastructure

#### M9 - Ecommerce Infrastructure
- **Status:** Migrated | **Quality:** Not Graded | **Version:** 1.0.0
- **Cluster:** BCL-3 (Infrastructure)
- **Content:** Store setup, tracking & attribution, tech stack, operations governance
- **Key Outputs:**
  - Subscription-first UX pattern (toggle > dropdown, 15-20% lift)
  - Meta Pixel + CAPI hybrid setup (85-98% conversion recovery vs 40-70% browser-only)
  - MER as north star metric
  - Week 1 Setup Sequence prevents launch delay
  - Phase-gated governance (essentials pre-launch, unlock quarterly)
- **Critical:** Theme performance budget (8 apps max, 500KB JS limit) prevents speed-kills-conversion death spiral
- **Hypotheses:** HYP-001 (tracking accuracy), HYP-002 (subscription UX)

#### M24 - Fulfillment & Inventory
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-3 (Infrastructure)
- **Content:** 3PL selection, inventory management, launch operations, international scaling
- **Key Outputs:**
  - Phase-gated fulfillment (self → 3PL → multi-node)
  - Two-stream demand model (subscription cohort decay + one-time ad-driven)
  - Statistical safety stock formula
  - Free shipping economics ($5-8/order margin impact)
  - Launch day war room protocol (T-48 to T+12hr)
- **Critical:** Contract negotiation highest-ROI task, temperature excursion protocol supplement-specific
- **Hypotheses:** HYP-002 (cohort decay model), HYP-004 (3PL fees + shipping margin impact)

#### M25 - Financial Operations
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-3 (Infrastructure)
- **Content:** Bookkeeping setup, unit economics tracking, business review cadence
- **Key Outputs:**
  - QBO + Synder stack
  - Chart of accounts (Day 1 Essentials: 18 accounts)
  - Subscription revenue recognition (ASC 606)
  - Unit economics dashboard with kill criteria
  - MBR Survival Five (Month 2-6: Cash, CAC, MRR, Churn, Sub Rate)
- **Critical:** Gross margin for P&L, contribution margin for channel decisions — never mix
- **Hypotheses:** HYP-001, HYP-002, HYP-003, HYP-004, HYP-005, HYP-007, HYP-008 (all monitored via MBR)

#### M30 - Analytics & Dashboards
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-3 (Infrastructure)
- **Content:** Data dictionary (50+ metrics), kill criteria & validation, dashboards & reporting
- **Key Outputs:**
  - Hypothesis monitoring table (maps all 8 HYPs to metrics, targets, kill thresholds)
  - 3 existential kill criteria (Cash, CAC, Contribution Margin)
  - 9 monitoring kill criteria with escalation protocol
  - MVD (7 metrics) for solo founder
  - MER > ROAS principle (platform ROAS overstates 20-40%)
- **Critical:** Solo founder tracking 50 metrics = tracking zero. MVD beats enterprise dashboards.
- **Hypotheses:** All 8 hypotheses have monitoring infrastructure defined here

---

### BCL-4: Retention & Lifecycle

#### M17 - Email & SMS
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-4 (Retention & Lifecycle)
- **Content:** Email flow architecture, post-purchase sequence, abandoned cart, welcome series, win-back
- **Key Outputs:**
  - 12 automated email flows with build order
  - 7-email post-purchase onboarding (Day 0 → Day 30)
  - Replenishment reminder at Day 21 (subscription conversion touchpoint)
  - 4-email win-back sequence (Day 60-105, 5-10% recovery rate)
  - Maintenance time budget: 1.5-4 hrs/month
- **Revenue Target:** 30-40% of total revenue from email by Month 7-12
- **Critical:** Discount escalation across flows creates arbitrage risk (mitigated by different incentive types + time-gating)
- **Hypotheses:** HYP-001 ($0 marginal CAC), HYP-002 (subscription conversion), HYP-003 (churn prevention), HYP-005 (LTV driver)

#### M18 - Email Lifecycle Flows
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-4 (Retention & Lifecycle)

#### M19 - Customer Lifecycle & CRM
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-4 (Retention & Lifecycle)
- **Content:** CRM architecture, lifecycle stages & segmentation, LTV & cohort analysis, metrics & dashboards
- **Key Outputs:**
  - Model-as-CRM philosophy (10-stage lifecycle with tab mapping)
  - Customer data model (19 fields)
  - Dual-layer segmentation (behavioral + RFM)
  - At-risk sub-segments (Product/Budget/Attention)
  - Cohort-based LTV with confidence intervals
- **Critical:** Cohort sample sizes need confidence intervals (50 customers = ±14% CI)
- **Hypotheses:** HYP-001 (attribution), HYP-002 (segment migration tracking), HYP-003 (churn visible in cohorts), HYP-005 (LTV tracking)

#### M20 - Customer Support
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-4 (Retention & Lifecycle)
- **Content:** Support operations, customer feedback system, customer success playbook
- **Key Outputs:**
  - 4-tier escalation framework (Founder/Team Mode)
  - NPS tracking + action playbook
  - Expected outcomes timeline (addresses product efficacy perception)
  - At-risk signals with intervention playbook
  - 11-star experience framework
- **Critical:** Chargeback monitoring is existential risk (Stripe 0.75% threshold)
- **Hypotheses:** HYP-003 (support quality → voluntary churn), HYP-003.1 (activation → efficacy perception), HYP-005 (service recovery → advocacy)

#### M21 - Subscription & Retention
- **Status:** Migrated | **Quality:** 8.0/10 | **Version:** 1.0.0
- **Cluster:** BCL-4 (Retention & Lifecycle)
- **Workshop:** 2026-02-06
- **Personas:** Skeptical Investor, Growth Engineer, Category Expert (DTC Subscription)
- **Dialogue:** 6 rounds, saturated, 3 upgrades, 0 unresolved
- **Quality Rationale:** Strong industry evidence (B-grade), honest confidence grading, actionable playbook with implementation timeline. Weakness: no IonWave-specific data (pre-launch), depletion messaging at D-grade.
- **Key Outputs:**
  - **subscription_platform.json:** Platform comparison (Recharge, Skio, Stay AI, Loop). **Recommendation: Loop Subscriptions** (free up to 50 subs, then $99/mo + 0.75%). Invalidates Danilo's Skio recommendation ($100 → $599/mo = 6x increase).
  - **subscription_psychology.md:** Why people subscribe/cancel supplements. Subscription driver rankings (convenience > savings > consistency > identity > belonging). Cancellation reasons ranked (too much product 20-30%, not seeing results 15-25%, too expensive 15-20%). **6x LTV multiplier** (subscribers $159 vs one-time $26).
  - **churn_prediction.json:** Industry retention curve (Month 1: 82-88%, Month 3: 60-70%, Month 6: 45-55%, Month 12: 30-40%). 9 churn prediction signals with intervention timelines. Composite risk scoring (CRITICAL/HIGH/MEDIUM/LOW tiers). Dunning model (55-70% recovery rate).
  - **retention_playbook.md:** 15-tactic prioritized retention playbook (3 tiers). Tier 1 expected to reduce churn from 15-20% to 10-12%. Implementation timeline. Anti-patterns section.
  - **win_back_offer_ladder.md:** Education-first win-back strategy. **Replaces Danilo's discount ladder** (10%→30%). Pre-cancellation save flow + post-cancellation 8-step sequence over 180 days. Addresses 70-80% of churn reasons vs 15-20% for discounts.
  - **opkit_subscription_retention.md:** Reusable Subscription & Retention Design Kit for any DTC consumable Trade.
- **Intelligence Gaps:**
  - Marine plasma time-to-value unknown (CRITICAL)
  - Loop Subscriptions pricing/integration not independently verified
  - Depletion messaging needs legal/regulatory review
  - No IonWave-specific churn data (expected pre-launch)
- **Feeds Into:** M3 (Financial Model — churn rate affects LTV:CAC), M19 (Customer Lifecycle — retention curve)
- **Requires:** M0 (Trade Thesis — DONE)
- **Next Action:** Collect actual IonWave churn data post-launch. Mine Seaonic reviews for time-to-value (upgrades HYP-003.1).
- **Hypotheses:** HYP-002, HYP-003, HYP-003.1-003.4, HYP-005
- **OpKit:** OK-M21-001

---

### BCL-5: Growth & Market

#### M10 - Pricing & Offer
- **Status:** Migrated (workshopped) | **Quality:** 7.4/10 | **Version:** 1.0.0
- **Cluster:** BCL-5 (Growth & Market)
- **Workshop:** 2026-02-06
- **Personas:** Skeptical Investor, Growth Engineer, Brand Strategist
- **Dialogue:** 8 rounds, saturated, 4 upgrades, 0 unresolved
- **Quality Rationale:** Strong evidence base from existing project data (financial model, competitive intel, M21). Confidence limited by PT-001 still running and lack of real customer data. All claims properly graded. Dialogue produced 4 upgrades including HYP-004 revision flag.
- **Content:** Offer strategy, price testing framework, product customization, SKU architecture, product roadmap, upsell page copy
- **Key Outputs:**
  - Subscription-first pricing architecture ($59 base, 15% subscription discount = $50.15)
  - Wave-gated SKU roadmap (Wave 1: unflavored base → Wave 2: flavored variants)
  - Price testing framework (PT-001: $49 vs $59 still running)
  - Bundle strategy
- **Critical Blocker:** PT-001 ($49 vs $59) still running — entire pricing architecture conditional on result. Follow-on capital needed for Wave 2 SKU expansion.
- **Intelligence Gaps:**
  - PT-001 not concluded — base price uncertain
  - No segment-specific pricing data
  - Bundle conversion data missing
  - Flavored production COGS not confirmed
  - Customer demand for flavored marine plasma untested
- **Feeds Into:** M3, M15, M12, M21
- **Requires:** M0, M26, M27
- **Next Action:** Await PT-001 completion. If $59 wins, architecture confirmed. If $49 wins, revision needed across all tabs.
- **Hypotheses:** HYP-002 (subscription conversion), HYP-004 (margin), HYP-005 (LTV), HYP-003.4 (cadence)
- **OpKit:** OK-M10-001

#### M14 - Testing & Optimization
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-5 (Growth & Market)
- **Content:** A/B testing framework, creative testing protocol, audience testing strategy, testing infrastructure
- **Key Outputs:**
  - Traffic-based testing methodology
  - Two-stage kill criteria (leading indicators Day 3, conversion Day 5-7 with 50+ click minimum)
  - Meta campaign structure
  - Test log (PT-000 completed: $49 vs $39, +23% RPV directional; PT-001 active: $49 vs $59)
  - Creative testing queue (CT-001, CT-002)
- **Critical:** Tool spend must never exceed 5% of ad budget. Passive audience learning from Meta breakdowns replaces dedicated audience tests at low traffic.
- **Hypotheses:** HYP-001 (CAC validation via creative testing), HYP-002 (subscription layout tests), HYP-004 (price testing)

#### M22 - Referral & Community
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-5 (Growth & Market)
- **Content:** Referral program, community strategy, UGC creator program
- **Key Outputs:**
  - $10/$10 store credit referral program (phased: manual → Smile.io → optimize)
  - Referral CAC $13.40 vs $35 paid (62% reduction)
  - Referrer retention effect (2-4x higher LTV)
  - Community platform evaluation (email-first → Skool → Circle phasing)
  - UGC production system (budget tiers: $500 survival, $1K minimum viable testing)
- **Critical:** Referral amplifies PMF, doesn't create it. Loop+Smile integration unverified (CRITICAL gap).
- **Hypotheses:** HYP-006, HYP-006.1 (referral), HYP-006.5 (WOM)

#### M23 - Influencer & Creator
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-5 (Growth & Market)
- **Content:** Influencer & creator strategy, pipeline operations, influencer map, vetting scorecard
- **Key Outputs:**
  - Influencer vs creator distinction (audience reach vs content production)
  - Phase 0 product seeding (30-50 nanos, $0 marginal cost)
  - Hybrid deal structure (product + affiliate)
  - CPO target <$18 (below paid CAC)
  - Attribution framework (direct code use + indirect branded search lift)
  - IonWave-specific influencer map (3 tiers: dream/achievable/micro)
- **Critical:** Attribution undercounting is systematic — code-only ROAS kills working partnerships. FTC compliance package is GATING requirement before product seeding.
- **Hypotheses:** HYP-006, HYP-006.3 (influencer seeding), HYP-001 (blended CAC reduction)

#### M26 - Competitive Intelligence
- **Status:** Migrated | **Quality:** 8.2/10 | **Version:** 1.0.0
- **Cluster:** BCL-5 (Growth & Market)
- **Workshop:** 2026-02-02 to 2026-02-04
- **Protocol:** CI Protocol (precursor to TWP-001)
- **Dialogue:** 3 personas, saturated
- **Content:** Competitive intel.json, Porter's Five Forces, market landscape map, competitor brand audit, claims audit, monitoring framework
- **Key Outputs:**
  - **Porter's Five Forces:** Rising CPMs (27% YoY), supplier oligopoly (Actimar/Biocean), zero switching costs, low entry barriers, high substitute threat
  - **Market landscape map:** Marine plasma sub-segment sized at $300K-$1.5M (not $100M as originally assumed)
  - **Competitor swipe catalog:** LMNT, Liquid IV, AG1, Seaonic
  - **Contaminant limits:** Heavy metal regulatory thresholds
- **Critical Findings:**
  - Category creation framing vs. electrolyte sub-category (positioning tension)
  - Capital tension confirmed (rising CPMs compress CAC efficiency)
  - Seaonic appears capital-constrained (6+ years to reach $100-180K revenue)
- **Feeds Into:** M0, M27, M5
- **Hypotheses:** HYP-001 (CAC pressure), HYP-004 (supplier concentration risk), HYP-007 (timeline), HYP-008 (capital needs)

#### M27 - Customer Research
- **Status:** Migrated | **Quality:** 8.5/10 | **Version:** 1.0.0
- **Cluster:** BCL-5 (Growth & Market)
- **Workshop:** 2026-02-02 to 2026-02-05
- **Protocol:** TWP-001 v2.0.0
- **Dialogue:** 3 personas, saturated
- **Content:** ICP analysis, customer segmentation, psychographic profiles, VOC database, interview playbook
- **Key Outputs:**
  - **Customer Archetypes (3):**
    - Keto/Carnivore Adherent (identity-driven, high LTV $180-250)
    - Exhausted Professional (convenience-driven, moderate LTV $120-180)
    - Biohacker/Optimizer (performance-driven, highest LTV $180-250)
  - **Jobs to Be Done (3):**
    - Job 1: Keto support (electrolyte rebalancing)
    - Job 2: Fasted training (performance without breaking fast)
    - Job 3: Daily wellness (cognitive + energy baseline) — **highest subscription stickiness**
  - **VOC Database:** LMNT proxy data (20 verbatims), general electrolyte insights
  - **Interview playbook:** Question scripts, analysis framework
- **Critical:** All customer data is LMNT proxy (B-grade). No IonWave-specific customer data yet (expected pre-launch).
- **Intelligence Gaps:**
  - Marine plasma-specific customer feedback (CRITICAL)
  - Female Wellness ICP not researched
  - Fasting-specific VOC limited
- **Feeds Into:** M0, M10, M15, M12, M21, M22, M23
- **Hypotheses:** HYP-002 (subscription stickiness by segment), HYP-005 (segment LTV), HYP-006 (WOM potential)

#### M28 - Market Expansion
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-5 (Growth & Market)
- **Content:** Channel strategy, expansion paths, Amazon playbook, B2B wholesale, retail readiness, product development, moonshot lab, constraint scenarios
- **Key Outputs:**
  - **13-channel acquisition matrix** with 4-phase sequencing (D2C → Amazon → B2B → Retail)
  - **8-path expansion matrix** (recommended sequence: Amazon → B2B → Line Extensions → Retail → International)
  - **Amazon economics:** $12.20 net at 26% margin (vs 60-67% D2C)
  - **B2B unit economics:** $275/mo net margin, 13.2x LTV:CAC at 80% retention
  - **Retail margin waterfall:** 19% net margin after retailer cut (40%) + distributor (15-20%)
  - **4 extreme constraint scenarios** ($100M in 12mo, $100K MRR in 3mo, $0 marketing budget, 10hrs/week)
  - **Subscription conversion sensitivity:** Viable to 30%, YELLOW at 20%, crisis at 10%
- **Critical:** Amazon price parity required to protect D2C subscription. MAP pricing non-negotiable for wholesale. Moonshot lab locked until $50K MRR.
- **Hypotheses:** HYP-002 (subscription sensitivity), HYP-004 (channel margin structures), HYP-006 (channel diversification)

---

### BCL-6: Operations & Team

#### M1 - Labor Deployment
- **Status:** Not Migrated
- **Cluster:** BCL-6 (Operations & Team)
- **Source Files:** 16_team_organization, 35_training_enablement

---

### BCL-7: Content & Media

#### M16 - Content & SEO
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-7 (Content & Media)
- **Content:** SEO strategy, content strategy, keyword research, content calendar, link building
- **Key Outputs:**
  - SEO timeline calibrated for new domain (3-6 month ramp)
  - E-E-A-T infrastructure for YMYL content
  - 23 target keywords in 3 phases ("LMNT alternative" highest priority: 2,900 vol, low KD)
  - 5 pillar/cluster content models
  - 12-post launch sequence
  - AI-assisted YMYL content workflow with compliance layer
  - Conservative SEO ROI: $13,275 organic revenue at Month 24 vs $10,800 investment
- **Critical:** Publishing sequence matters — pillar page first, comparisons after trust established. Marine plasma = uncontested keyword territory.
- **Hypotheses:** HYP-006, HYP-006.2 (SEO channel), HYP-001 (organic traffic → lower blended CAC)

#### M29 - PR & Communications
- **Status:** Migrated | **Quality:** Not Graded
- **Cluster:** BCL-7 (Content & Media)
- **Content:** PR strategy, crisis playbook, podcast strategy, video strategy
- **Key Outputs:**
  - Future press release (working-backwards method)
  - Milestone press releases
  - Expert quote platforms
  - Podcast guesting strategy (Phase 3+, deferred)
  - Crisis communications (8 scenarios: FTC, adverse reactions, viral complaints, ad bans, supply chain, chargebacks, fake reviews, competitive claim copying)
  - 6-A crisis response framework
- **Weekly Time Budget:** 2-3 hrs/week Phase 1 (capped)
- **Critical:** PR's primary ROI is backlinks (SEO acceleration), not direct traffic. Minimum viable press pitch checklist gates outreach behind product traction.
- **Hypotheses:** HYP-006, HYP-006.4 (PR & earned media), HYP-001 (earned media = $0 marginal CAC)

---

## 🔗 Cross-TUP Dependencies

### Dependency Map (Selected Critical Paths)

**M0 (Trade Thesis) feeds into:**
- M26 (Competitive Intel) - validates positioning
- M27 (Customer Research) - ICP validation
- M5 (Formulation) - product requirements
- M3 (Financial Model) - revenue assumptions
- M10 (Pricing & Offer) - pricing strategy

**M3 (Financial Model) depends on:**
- M0 (Trade Thesis) - strategic assumptions
- M21 (Subscription & Retention) - churn rate
- M10 (Pricing & Offer) - pricing architecture
- M27 (Customer Research) - LTV by segment

**M21 (Subscription & Retention) feeds into:**
- M3 (Financial Model) - churn rate affects LTV:CAC
- M19 (Customer Lifecycle) - retention curve
- M17 (Email & SMS) - retention playbook implementation

**M30 (Analytics & Dashboards) monitors:**
- All 8 hypotheses via defined metrics, targets, kill thresholds

---

## 🚨 Critical Intelligence Gaps

### Existential Gaps (Block Progress)

1. **Marine plasma time-to-value unknown** (HYP-003.1)
   - **Severity:** CRITICAL
   - **Upgrade Path:** Mine Seaonic reviews + IonWave beta test (20-30 users, Day 7/14/30 tracking)
   - **Affected:** M21, M20, M27

2. **PT-001 price test not concluded** (HYP-004)
   - **Severity:** HIGH
   - **Upgrade Path:** Await test completion
   - **Affected:** M10 (entire pricing architecture conditional)

3. **No financial model linked to thesis** (HYP-007, HYP-008)
   - **Severity:** CRITICAL
   - **Upgrade Path:** Build/audit M3 Financial Model
   - **Affected:** M0, capital planning

4. **Loop Subscriptions integration not verified** (HYP-002)
   - **Severity:** HIGH
   - **Upgrade Path:** Verify Loop + Klaviyo integration depth, Smile.io compatibility
   - **Affected:** M21, M22

### High-Priority Gaps (Limit Confidence)

5. **No IonWave-specific customer data** (Multiple HYPs)
   - **Severity:** HIGH (expected pre-launch)
   - **Upgrade Path:** Post-launch: collect actual churn, CAC, subscription rate, LTV
   - **Affected:** M21, M27, M10, M19

6. **Depletion messaging legal review needed** (HYP-003.1)
   - **Severity:** MEDIUM (regulatory risk)
   - **Upgrade Path:** Legal/regulatory review of depletion claims
   - **Affected:** M21

7. **Female Wellness ICP not researched** (HYP-002, HYP-005)
   - **Severity:** MEDIUM
   - **Upgrade Path:** Research Female Wellness segment
   - **Affected:** M27, M0

8. **Seaonic review text not mined for time-to-value** (HYP-003.1)
   - **Severity:** MEDIUM
   - **Upgrade Path:** Mine Trustpilot/Amazon reviews (2-3 hrs, upgrades C→B)
   - **Affected:** M21, HYP-003.1

---

## 📈 Next Actions by Priority

### Month 0 (Pre-Launch)

1. **Build/audit M3 Financial Model** (links to M0 Trade Thesis)
2. **Complete PT-001 price test** ($49 vs $59 - affects M10 pricing architecture)
3. **Mine Seaonic reviews** for time-to-value data (upgrades HYP-003.1 C→B)
4. **Verify Loop + Klaviyo integration** (critical for M21 recommendation)
5. **Legal review of depletion messaging** (regulatory risk mitigation)

### Month 1-2 (Launch & Validation)

6. **CAC validation** via creative testing (HYP-001, M14 protocol)
7. **Subscription rate tracking** (first 100 orders, HYP-002)
8. **Launch day war room** (M24 protocol, $100-200 ad cap Day 1)
9. **Activate M17 email flows** (3 Day-1 flows: welcome, abandoned cart, post-purchase)
10. **Set up M30 MVD tracking** (7 metrics daily pulse)

### Month 2-6 (Early Growth & Iteration)

11. **Cohort churn tracking** (HYP-003 validation, need 60-90 days)
12. **Referral program launch** (M22, HYP-006.1)
13. **Influencer product seeding** (M23, Phase 0: 30-50 nanos)
14. **Month 6 checkpoint** (HYP-008: $8-10K MRR target, follow-on capital decision)
15. **SEO content ramp** (M16: 20+ articles in first 3 months)

### Month 6-12 (Scale & Optimize)

16. **LTV:CAC validation** (HYP-005, need 6-month cohorts)
17. **Amazon preparation** (M28: if $20K+ MRR, consider Phase 2)
18. **B2B outreach** (M28: if product-market fit confirmed)
19. **Line extension planning** (M28: if >50 customer demand requests)
20. **Annual planning** (M25 QBR framework)

---

## 🎓 OpKits Generated

OpKits are reusable production bundles that enable any future Trade to execute a TUP excellently.

| OpKit ID | TUP | Name | Registered |
|----------|-----|------|------------|
| OK-M21-001 | M21 | Subscription & Retention Design Kit | Yes |
| OK-M10-001 | M10 | Pricing & Offer Architecture Kit | Yes |
| OK-M22-001 | M22 | Referral, Community & UGC Kit | Yes |
| OK-M14-001 | M14 | Testing & Optimization Kit | Yes |
| OK-M16-001 | M16 | Content & SEO Kit | Yes |
| OK-M17-001 | M17 | Email Lifecycle Kit | Yes |
| OK-M19-001 | M19 | Customer Lifecycle & CRM Kit | Yes |
| OK-M20-001 | M20 | Customer Support Kit | Yes |
| OK-M23-001 | M23 | Influencer & Creator Kit | Yes |
| OK-M25-001 | M25 | Financial Operations Kit | Yes |
| OK-M28-001 | M28 | Market Expansion Kit | Yes |
| OK-M29-001 | M29 | PR & Communications Kit | Yes |
| OK-M30-001 | M30 | Analytics & Measurement Kit | Yes |
| OK-M9-001 | M9 | Ecommerce Infrastructure Kit | Yes |
| OK-M24-001 | M24 | Fulfillment & Inventory Kit | Yes |
| OK-M18-001 | M18 | Email Lifecycle Flows Kit | Yes |

**Total OpKits:** 16 registered

---

## 📚 Methodology & Quality Standards

### TUP Workshop Protocol (TWP-001 v2.0.0)

Every migrated TUP follows an 11-phase protocol:

1. **Load Context** - Read Danilo's TUP structure
2. **Gather Bootstrap Material** - Check existing work
3. **Workshop Checkpoint** - Align with operator on approach
4. **Research & Best Practices** - Industry benchmarks, reference models
5. **Fill the Void Spaces** - Produce content (Markdown + JSON)
6. **Expert Persona Dialogue** - Stress-test with 3 personas to saturation
7. **Self-Grade** - Honest quality assessment
8. **Build the OpKit** - Create reusable production bundle
9. **Register in System** - Update manifest, _meta.json
10. **Hypothesis Cross-Reference** - Link to business hypotheses
11. **Session Log** - Document what was done

### Source Quality Hierarchy

| Tier | Source Type | Confidence Floor |
|------|-------------|-----------------|
| 1 | Audited filings / official disclosures | A |
| 2 | Primary company pages (verified live) | A/B |
| 3 | Third-party corroboration (3+ sources agree) | B |
| 4 | Industry reports / analyst coverage | B/C |
| 5 | Single credible source | C |
| 6 | Social media / forums / reviews | C (B if 3+ corroborate) |
| 7 | Derived calculations | C/D |
| 8 | Industry benchmarks (generic) | C |
| 9 | Best guess / no source | D |

### Confidence Grading

- **A-grade:** Direct observation, verified primary sources, audited data
- **B-grade:** Strong proxy evidence, 3+ corroborating sources, validated benchmarks
- **C-grade:** Single credible source, industry benchmarks, unverified proxy
- **D-grade:** Educated guess, no validation, untested assumption

### Quality Scoring (X/10)

Average of 5 dimensions:
- Evidence Coverage (every tab filled with sourced content)
- Confidence Honesty (every grade defensible against source hierarchy)
- Upgrade Path Quality (every below-A item has actionable upgrade path)
- Actionability (content enables decisions)
- OpKit Reusability (works for any Trade in this domain)

---

## 🔄 System Evolution

### Constraint Scenario Protocol (CSP-001 & CSP-002)

Two hypotheses were decomposed using the Constraint Scenario Protocol:

**CSP-001 applied to HYP-006 (Organic Growth):**
- Decomposed into 5 sub-hypotheses (Referral, SEO, Influencer, PR, WOM)
- Surfaced HYP-009 (Pre-Launch Demand Generation)
- Reframed HYP-001 relationship from "mitigates" to "portfolio diversifies"

**CSP-002 applied to HYP-003 (Churn):**
- Decomposed into 4 sub-hypotheses (Product Efficacy, Early-Life Churn, Retention Infrastructure, Consumption-Cadence)
- Applied Seaonic proxy evidence to HYP-003.1 (upgraded D→C)
- Composite score improved from 1.0 to 1.40
- Key insight: "Churn is a product hypothesis in disguise"
- Established cross-hypothesis sub-link: HYP-003.1 → HYP-006.5

### Persona Dialogue Examples

**Common Personas Used:**
- Skeptical Investor (financial grounding, evidence demands)
- Growth Engineer (unit economics, compounding mechanisms)
- Category Expert (domain best practices)
- Customer Anthropologist (VOC, customer words)
- Competitive Strategist (market positioning)
- Operations Expert (scale failure points)
- Brand Strategist (brand coherence)

**Saturation Framework:**
- 3 consecutive RESOLVED rounds triggers saturation
- Last 2 UNRESOLVED gaps are restatements of documented gaps
- All 3 personas agree content is coherent
- Hard stop: 8 rounds maximum

---

## 📊 System Metrics

### Coverage Statistics

- **Total TUPs in System:** 41
- **Migrated TUPs:** 19 (46%)
- **Unmigrated TUPs:** 22 (54%)
- **Total Hypotheses:** 19 (9 parent + 10 children)
- **Hypotheses with >10 Document References:** 4 (HYP-001: 14, HYP-002: 14, HYP-003: 13, HYP-004: 11)
- **Total Hypothesis References Across All Documents:** 148+
- **Total OpKits Registered:** 16

### Confidence Distribution (Hypotheses)

- **A-grade:** 0 (0%)
- **B-grade:** 1 (5%) - HYP-004
- **C-grade:** 5 (26%) - HYP-001, HYP-002, HYP-003.1, HYP-007, HYP-008
- **D-grade:** 13 (68%)

**Average Confidence:** ~1.3/4.0 (D+ to C-)
**Target Confidence Post-Launch:** 2.5+/4.0 (C+ to B-)

### Quality Distribution (TUPs)

- **8.0+/10:** 3 TUPs (M27: 8.5, M26: 8.2, M21: 8.0)
- **7.0-7.9/10:** 1 TUP (M10: 7.4)
- **6.0-6.9/10:** 1 TUP (M0: 6.5)
- **Not Graded:** 14 TUPs

**Average Quality (Graded TUPs):** 7.7/10

---

## 🎯 Strategic Priorities

### Critical Path to Launch

1. ✅ **M0 Trade Thesis** - DONE (6.5/10)
2. ✅ **M26 Competitive Intel** - DONE (8.2/10)
3. ✅ **M27 Customer Research** - DONE (8.5/10)
4. ⏳ **M3 Financial Model** - NOT MIGRATED (BLOCKER)
5. ⏳ **M5 Formulation** - NOT MIGRATED
6. ✅ **M10 Pricing & Offer** - DONE (7.4/10, conditional on PT-001)
7. ✅ **M9 Ecommerce Infrastructure** - DONE
8. ✅ **M24 Fulfillment & Inventory** - DONE
9. ✅ **M17 Email & SMS** - DONE
10. ✅ **M21 Subscription & Retention** - DONE (8.0/10)

**Launch Readiness:** 8/10 critical TUPs complete. **Blockers:** M3 (Financial Model), M5 (Formulation).

### Post-Launch Validation Priorities

**Month 1-2 (Survival Metrics):**
- CAC ≤$40 (HYP-001)
- Subscription rate ≥45% (HYP-002)
- No major fulfillment failures (M24)

**Month 2-4 (Early Signals):**
- Month 1 churn ≤15% (HYP-003.2)
- MRR growth trajectory
- Email flow activation rates

**Month 6 (Checkpoint for Follow-On Capital):**
- $8-10K MRR (HYP-007)
- CAC ≤$38 (HYP-001)
- Churn ≤12% (HYP-003)
- LTV:CAC ≥2.8x (HYP-005)

**Month 12 (Scale Validation):**
- $20-25K MRR (HYP-007)
- Organic lift ≥5% (HYP-006)
- Cohort LTV data (6-month cohorts)

**Month 18 (Target Achievement):**
- $30K+ MRR (HYP-007)
- All 8 hypotheses validated or invalidated
- Decision: scale, pivot, or exit

---

## 📄 Report Generation

**Report Generated:** 2026-02-09
**Generated By:** `scripts/generate_tup_reports.py` (TUP Report Generator)
**Source Data:** `data/` directory (19 TUP folders with `_meta.json` + content files)
**Hypotheses Data:** `data/hypotheses/registry.json` + `index.json`
**Methodology:** TUP Workshop Protocol (TWP-001 v2.0.0)

**Related Documentation:**
- Individual TUP Reports: `reports/tup_reports/TUP_M{N}_*.md`
- TUP Report Generation Workflow: `processes/TUP_Report_Generation_Workflow.md`
- TUP Workshop Protocol: `processes/TUP_Workshop_Protocol.md`
- Hypothesis Registry: `data/hypotheses/registry.json`
- Manifest: `data/manifest.json`

---

**End of Master TUP Report**
