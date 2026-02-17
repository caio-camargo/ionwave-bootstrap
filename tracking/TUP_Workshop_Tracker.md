# TUP Workshop Tracker
**Version**: 1.1.0
**Author**: Caio, Claude (collaborative)
**Date Created**: 2026-02-06
**AI Model**: claude-opus-4-6
**Purpose**: Track progress workshopping all 41 TUPs from preliminary to production quality
**Status**: Active

---

## Overview

**Total TUPs**: 41
**Workshopped**: 34 (M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24, M25, M26, M27, M28, M29, M30, M31, M35, M39)
**Remaining**: 7
**Deferred**: 2 (BCL-7: M32, M33) + 1 (M37: AI & Automation)
**Active Queue**: 30

**Total Danilo content tabs across all TUPs**: ~683
**Average content tabs per TUP**: ~17

### What "Workshopping" a TUP means

This is NOT mechanical migration. Each TUP requires creative/analytical work:

1. **Read Danilo's structure** — P (Project Plan), C (Contract), IP (Industry Perspectives), V (Verification) + content tabs
2. **Read Bootstrap material** — archived XLSX, analysis deliverables, tracking logs
3. **Workshop the subject matter** — fill Danilo's void spaces with quality content, validate assumptions, grade evidence
4. **Build the OpKit(s)** — reusable production bundle so any future Trade can execute this TUP excellently
5. **Produce outputs** — JSON data layer + analysis deliverables + OpKit registration

### Dual Output Per TUP

| Output | What it is | Who it's for |
|--------|-----------|--------------|
| **IonWave Content** | Filled void spaces, graded evidence, validated assumptions | IonWave Trade #84 |
| **OpKit** | Instruction + graded examples + rubric + 95% scaffold | All future Trades in the Studio 3 system |

---

## Effort Classification

| Effort | Description | Est. Time | Criteria |
|--------|-------------|-----------|----------|
| **S** | Small — few content tabs (<8), narrow scope, mostly structural | ~30 min | <8 Danilo tabs, 0-1 Bootstrap sources |
| **M** | Medium — moderate content tabs (8-15), substantive analysis needed | ~1-2 hrs | 8-15 Danilo tabs, 1-2 Bootstrap sources |
| **L** | Large — many content tabs (15-25), multi-source, deep analysis | ~2-4 hrs | 15-25 Danilo tabs, 2+ Bootstrap sources, cross-dependencies |
| **XL** | Extra Large — massive tab count (25+) or critical blockers | ~4+ hrs | 25+ tabs, unresolved conflicts, human data needed |

---

## Progress by Cluster

### BCL-0: Thesis & Meta (MERGE) — 2/5 done (40%)
*Decision: Bootstrap canon for analytics, Danilo for frameworks*

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| **M0** | Trade Thesis | — | L | **DONE** | **4 OpKits registered** | 01, 37, 23 | Quality 6.5/10 |
| M34 | Trade Architecture | 25 | L | NOT STARTED | TBD | 29 | Meta TUP: scorecards, ODD maps, glossary, verification framework. Larger than expected. |
| M38 | Strategic Frameworks | 44 | XL | NOT STARTED | TBD | 37, 01 | **Massive**: games, paradigm shifts, eigenforms, anti-fragility, OpKit library itself lives here |
| **M39** | **Conceptual & Philosophical Foundations** | 14 | M | **DONE** (7.5/10) | **OK-M39-001** | ops_model_v10_dump (908-919) | 14 content tabs + Danilo vision → 6 files (theoretical_foundations 540 lines, operational_protocols 640 lines, advisor_strategy 420 lines, textbook_ma_strategy 370 lines, love_as_mutual_information 320 lines, workshop_summary 160 lines) + dialogue (7 rounds, 12 upgrades) + OpKit. Theoretical foundations: Christopher Alexander (15 Properties of Life), David Bohm (implicate/explicate order), Giulio Tononi (IIT, mutual information), W. Ross Ashby (Law of Requisite Variety). Operational protocols: 75 Questions (context transfer), 5-6 Bullets (compression), 3-Gate Review (parallel validation), Virtual Twin (Claude as Trade twin), Verification Strategy (4 trust dimensions), Pattern Language Application (OpKit extraction). Novel concepts: Requisite variety via TUP decomposition (41 TUPs match 41 market dimensions), love as mutual information (high-MI teams), aliveness scoring (Alexander's 15 properties), implicate/explicate ratio (76% unfolded). Evidence: Theory B-grade (well-sourced), operational translations C/D-grade (logical but unvalidated). Maturity: Experimental (requires cross-Trade testing to upgrade to Proven → Canonical). Blockers: All protocols untested, Virtual Twin requires full TUP context (M5-M37), advisor procurement requires network mapping, cross-Trade validation blocked, risk of over-theory/under-execution. OpKit: First purely meta-level OpKit (BCL-0) — generalizable framework for grounding ANY Trade operations in deep theory. |
| M40 | Navigation & Command | 18 | L | NOT STARTED | TBD | 24 | Command center, role entry points, phase checklists, cognitive load |

**Cluster progress**: 2/5 DONE (40%) — M0 + M39 complete, M34/M38/M40 remaining
**Cluster estimate**: 1XL + 2L remaining = ~10 hrs (M39 done, saved 2 hrs)
**Revised recommendation**: M34/M38 are massive meta-system TUPs (defer until execution TUPs complete). M40 Navigation is next logical step (sequencing + command center).

---

### BCL-1: Product & Science (DANILO CANON) — 4/4 COMPLETE ✅

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| **M5** | **Formulation** | 15 | L | **DONE** (8.5/10) | **OK-M5-001** | 05A, 05B, 36 | 15→5 files (formulation_specification 323 lines, scientific_substantiation 628 lines, product_development 577 lines, usage_protocols_and_stacking 557 lines, dialogue_summary 162 lines). Green-field build with 2026 industry research (5 web searches: marine plasma bioavailability, ocean vs synthetic electrolytes, Quinton clinical research, FDA DSHEA claims, magnesium forms). Core electrolyte profile (Na 1000mg, K 200mg, Mg 60mg — LMNT-validated ratios), 78-trace-mineral substantiation reality check (only 20 elements biochemically required, rest marketing claim), ocean-sourced ionic minerals bioavailability (66-90%+ vs synthetic 9-105% variable), quality markers (CoA requirements, heavy metal limits <10ppb As/<5ppb Pb/<3ppb Hg, microbiological <10 CFU/mL), taste engineering (unflavored purist → lemon-lime mass market → variety SKUs), stability validation (18-24 month shelf life, moisture sensitivity, packaging PET/ALU/PE laminate), cost breakdown ($0.48-0.72 COGS target $0.55), FDA/FTC compliance (structure/function claims, required disclaimers), competitive positioning (IonWave vs LMNT/Liquid IV/Seaonic/Quinton). 6 rounds, 22 upgrades (marine biocenosis reality check, bioavailability trade-off analysis, heavy metal testing every batch, microplastic testing protocol, hangover disclaimer, ACE inhibitor warning, RCT outcome scenarios, adverse event surveillance). Exceptional confidence honesty (9.5/10 — A/B/C/D grades + [VOID — requires CoA] for ALL supplier-dependent data). M6/M7 integration (supplier vetting framework, claims compliance). Vision: "Most scientifically rigorous electrolyte formulation that could withstand peer review." Supplier-dependent: ALL exact trace mineral amounts require Week 1-2 CoA validation. Pre-launch blockers: taste testing (Week 3-4, 50-100 users), stability testing (Month 3-6 accelerated), bioavailability RCT (Q3 2026, $50-150K). **BCL-1 now 4/4 COMPLETE (100%)** — M5/M6/M7/M8 all done. |
| **M6** | **Supply Chain** | 13 | M | **DONE** (8.4/10) | **OK-M6-001** | 05B | 13→4 files. Green-field build (no Bootstrap data, industry research only). Supplier vetting (Biocean/Actimar/Quinton targets, evaluation scorecard, outreach templates), ocean sourcing (marine plasma depth strategy 20-30m vs deep ocean 600m+, NATURA 2000 France, Bay of Biscay), COA framework (FDA + Prop 65 limits, batch tracking, recall protocol), restock formula (21-day safety stock Phase 1, M13 ad spend integration). 6 rounds, 12 upgrades (5 critical: kill criteria, COGS thresholds, backup activation, lead time validation, M13 cross-ref). All supplier data [VOID — requires Week 1-2 outreach]. |
| **M7** | **Regulatory & FDA** | 11 | M | **DONE** (8.7/10) | **OK-M7-001** | 17 | 11→2 comprehensive files (FDA/FTC framework 41 pages + claims guidance/audit 39 pages). Embedded expert dialogue (Regulatory Attorney + FTC Enforcement Officer). FDA DSHEA framework (pre-market, labeling, cGMP, adverse events, 2026 disclaimer update), FTC advertising (substantiation, consumer reviews +340% enforcement, influencer disclosure), 50+ claims examples (structure/function vs disease), substantiation hierarchy, IonWave M11/M15 audit (7 violations flagged: 3 fake testimonials, unsubstantiated bioavailability, $420K-$2M FTC exposure), compliance calendar (12-month gates), pre-launch audit checklist, competitor framework. P0 corrections: 4 hours, $0 cost. Attorney review recommended ($5K-$10K). OpKit: 6-step pre-launch framework for any supplement brand. |
| **M8** | **Brand Identity** | 16 | L | **DONE** (7.8/10) | **OK-M8-001** | 09, 05A | 16→7 files + dialogue + workshop summary + OpKit. Positioning ('accessible marine plasma' Phase 1 → 'complete mineralization' Phase 2+), voice (Informed Guide archetype, 5 principles, 6 contexts), packaging (sachet/box/mailer, FDA compliance, Prop 65, unboxing with progress tracker), naming (IonWave evaluation, domain/trademark strategy), messaging (brand story, awareness ladder, 3 taglines, 5 social pillars), visual identity (logo/typography/color/photo briefs), industry perspectives (LMNT/AG1/Momentous/Quinton audit, 3 contrarian takes), 3-phase brand evolution model. 9 rounds, 5 upgrades (sachet/box split, CoA escalation, absorption claims softened, tagline context separation, progress tracker added). 6 CRITICAL blockers: logo, photography, CoA, Prop 65, trademark, domain. Quality 7.8/10: strong strategic foundation with typical pre-launch execution gaps. |

**✅ BCL-1 COMPLETE!** All 4 TUPs done: M5, M6, M7, M8. This is the 3rd fully complete cluster (after BCL-4 and BCL-5). IonWave is launch-ready for: core product formulation (M5), supply chain (M6), regulatory compliance (M7), and brand identity (M8). Critical path items: supplier CoA (Week 1-2), taste testing (Week 3-4), logo/photography/domain (Week 1-3).

---

### BCL-2: Money & Legal — 4/4 COMPLETE ✅
*Decision: REC-001 RESOLVED via dual-scenario modeling approach*

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| **M2** | **Entity & Legal** | 15 | L | **DONE** (8.2/10) | **OK-M2-001** | 17, 33 | 15→22 files. Phase-gated entity architecture (C-Corp → Holding Co → DAO LLC), IP-at-parent LVMH strategy, SAFE stacking dilution warning, Section 351/368 tax restructuring risk, health data DPIA for CPPA 2026, privacy-as-brand-value positioning. 6 rounds, 8 upgrades. All 5 IP sections complete. 2 hypothesis connections: HYP-004 (Gross Margin) via tax/insurance overhead impact. |
| **M3** | **Financial Model** | 15 | XL | **DONE** (8.2/10) | **OK-M3-001** | 06, 08 | 15→20 files. **REC-001 ROOT CAUSE IDENTIFIED**: 40% vs 67% gap = definitional (product GM 67% vs fully-loaded GM 40%). Bridge: 67% - fulfillment 7-12% - shipping 6-10% - payment 3.4% - returns 5-7% - chargebacks 0.3-0.5% = 34-45% fully-loaded. Dual-scenario modeling (Conservative 42%/Realistic 60%/Optimistic 67%) across all 8 margin-dependent outputs. Novel contributions: bifurcation-linked scenario planning (6 decision points), kill criteria integrated sensitivity analysis (GM = #1 driver, $122K Y1 swing), phase-gated financial reporting. Key finding: at 40% GM, business CANNOT break even with paid acquisition (negative effective margin when ad spend 50% of revenue); subscription renewals are path to viability (920 subs at M12 = $46K MRR, zero CAC). 8 rounds, 7 upgrades. 3 personas (Startup CFO, Financial Modeler, D2C Operator). REC-001 remains BLOCKER for final lock pending 3 decisions: (1) fulfillment strategy (self vs 3PL: 10-15% margin swing), (2) shipping absorption policy (6-10% swing), (3) return rate confirmation with actuals (5-7% swing). |
| **M4** | **Fundraising & Investors** | 9 | M | **DONE** (8.3/10) | **OK-M4-001** | 20 | 9→5 files (fundraising_strategy 650 lines, pitch_deck_framework 430 lines, investor_relations 550 lines, term_sheet_and_negotiation 520 lines, diligence_and_exit 470 lines) + dialogue + self-grade. All 9 Danilo tabs were high quality with directly usable content (Investor FAQ, 15-slide pitch deck EXCELLENT A-grade, Backup Funding Plan, CRM 7-stage framework, Investor Update Template, Negotiation Playbook, Term Sheet Guide, Exit Preparation, Diligence Answers). 2026 D2C fundraising research (5 web searches: Carta Q3 2025 pre-seed data, SAFE vs priced equity trends, D2C valuation, micro-seed dynamics, pitch deck best practices). $30-50K SAFE at $250-500K cap strategy, 7-week validation sprint as de-risking pitch, warm intro tactics (10-20x more effective than cold), SAFE structure (post-money cap-only, 92% market standard), investor archetype targeting (friends/family + angels, not VCs), backup funding plan (crowdfunding, RBF, bootstrap, operator buy-in, strategic partnership), exit scenarios (PE $6-9M at 4-6x EBITDA Year 3-5, strategic $8-15M, operator buyout 1.5-3x early, distributions 20-40% Year 2+). Novel concept: Trade-as-pitch (investors interact with Claude vs static deck) is experimental (D-grade confidence) — recommend testing with 3-5 friendly investors before scaling. 6 intelligence gaps flagged (investor response data VOID, micro-raise comparables C-grade, Trade-as-pitch validation D-grade, TAM/SAM/SOM C-grade, SAFE liquidity C-grade, Brazil-US legal C-grade). 4 key blockers: pre-revenue status (HIGH), investor interest unknown (HIGH), solo founder risk (MEDIUM), M3 margin dispute REC-001 (RESOLVED — pitch deck uses conservative 60-65% margin with sensitivity disclosure). Hypothesis cross-ref: HYP-003 (churn/retention drives exit valuation), HYP-006 (marine plasma differentiation is pitch foundation). Feeds into: M2 (cap table, SAFE legal docs, trademark for IP), M3 (unit economics, 3-year projections, use of funds, exit valuation), M5 (Biomarine as moat). |
| **M25** | **Financial Ops** | 6 | S | **DONE** (8.8/10) | **OK-M25-001** | — | 3 content files + OpKit + dialogue. Dual-margin REC-001 treatment. Day 1 Essentials chart of accounts. Survival Five MBR. |

**✅ BCL-2 COMPLETE!** All 4 TUPs done: M2, M3, M4, M25. This is the **5th fully complete cluster** (after BCL-1, BCL-3, BCL-4, BCL-5). IonWave is launch-ready for: entity/legal foundation (M2), complete financial model (M3), fundraising playbook (M4), and financial operations (M25). Average cluster quality: 8.4/10. REC-001 margin dispute resolved via dual-scenario modeling — root cause identified as definitional difference (product GM 67% vs fully-loaded GM 40%), with transparent handling across all financial outputs.

---

### BCL-3: DR & Creative (DANILO CANON) — 5/5 COMPLETE ✅

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| **M11** | **VSL Production** | 14 | M | **DONE** (9.2/10) | **OK-M11-001** | 09 | 14→8 files. VSL-as-Trade framework, 10 hook library, FTC compliance rigor, testing kill criteria (min 10 purchases), winner rate 10-20%, platform allocation (50% Meta / 35% YouTube / 15% TikTok), fictional testimonials flagged, bioavailability substantiation gap. 6 rounds, 15 upgrades. |
| **M12** | **Ad Creative** | 26 | XL | **DONE** (8.2/10) | **OK-M12-001** | 10A, 10B | 26→22 files (18 content + dialogue + OpKit). 3-tier creative replenishment (derivatives/new concepts/high-production), 5-indicator fatigue detection matrix, engineering-driven testing hierarchy (angle → hook → format), quarterly library maintenance, brand voice 3-phase maturation (Challenger → Expert → Leader), comprehensive FTC compliance. D2C Creative Director + Performance Media Buyer + UGC Creator personas. 10 rounds, 10 upgrades. Cross-integrated with M11/M13/M14/M15/M23/M27. |
| **M13** | **Media Buying** | 14 | M | **DONE** (10.0/10) | **OK-M13-001** | 12 | 14→14 files. Bootstrap File 12 (5 sheets) + 2026 CPM research. Tiered scaling (20%/30%/40-50% by volume), Pixel+CAPI attribution (EMQ >7.0), channel P&L (contribution margin > CAC), 4-phase diversification (<50% single platform), creative fatigue 2-4 weeks, tracking validation checkpoints. 12 rounds, 9 upgrades. **Perfect score.** |
| **M14** | **Testing** | 7 | S | **DONE** (7.5/10) | **OK-M14-001** | 10B | 6 content files + OpKit. Near green-field build. Google Optimize replaced. 4 rounds, 9 upgrades. |
| **M15** | **Landing Pages & Conversion** | 18 | L | **DONE** (8.2/10) | **OK-M15-001** | 11A, 11B | 18→5 files. 8 funnel architectures, conversion equation, FTC/DSHEA/Prop 65 compliance, subscription-first checkout, Shop Pay priority. 6 rounds, 25 upgrades (3 critical). |

**✅ BCL-3 COMPLETE!** All 5 TUPs done: M11, M12, M13, M14, M15. This is the **4th fully complete cluster** (after BCL-4, BCL-5, BCL-1). IonWave is launch-ready for: full DR creative pipeline (VSL production M11, ad creative M12, media buying M13, testing M14, landing pages M15). Average cluster quality: 8.6/10.

---

### BCL-4: Retention & Lifecycle (DANILO CANON) — 5/6 done

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| M17 | Email & SMS | 11 | M | **DONE** (8.4/10) | OK-M17-001 | 11B, 27 | 27 source files → 9 output files. Full email sequences with copy. Discount defense, FTC compliance, Founder Mode build order. |
| M18 | Email Lifecycle Flows | 12 | M | **DONE** | 8.7/10 | OK-M18-001 | Corrected name (was "SMS"). 4 output files: welcome_and_nurture, cart_recovery, post_purchase_and_retention, winback_and_lifecycle. 14 dialogue upgrades. Completes BCL-4. |
| **M19** | **Customer Lifecycle & CRM** | 13 | M | **DONE** | **1 OpKit** (OK-M19-001) | 27 | Quality 8.4/10. 4 content files + OpKit + dialogue. Model-as-CRM architecture, non-linear lifecycle paths, Minimum Viable CRM (3 Day-1 flows), at-risk sub-segmentation (Product/Budget/Attention), churn risk formula, confidence intervals, founder daily check-in, customer-count tool triggers, seasonality. |
| **M20** | **Support** | 9 | S | **DONE** | **1 OpKit** (OK-M20-001) | 27 | Quality 8.6/10. 3 content files + OpKit + dialogue. Founder Mode/Team Mode escalation, chargeback monitoring, behavioral activation, FDA adverse event protocol, minimum viable support stack. |
| **M21** | **Subscriptions** | 5 | S | **DONE** | **1 OpKit** (OK-M21-001) | 07 | Quality 8.0/10. 5 content files + OpKit + dialogue summary. |
| **M22** | **Referral & Community** | 6 | S | **DONE** | **1 OpKit** (OK-M22-001) | 14 | Quality 7.0/10. 6 content files + OpKit + dialogue summary. Referral, community, UGC. |

**Cluster estimate**: 1M = ~1 hr remaining
**✅ BCL-4 COMPLETE!** All 6 TUPs done: M17, M18, M19, M20, M21, M22. M18 corrected from "SMS" to "Email Lifecycle Flows" — the actual email content within M17's flow architecture. BCL-4 is the 2nd fully complete cluster (after BCL-5).

---

### BCL-5: Growth & Market (DANILO CANON) — 7/7 COMPLETE
*Analytical layer preserved per REC-007*

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| **M26** | Competitive Intel | 11 | L | **DONE** | **1 OpKit** (CI Protocol) | 02 | Quality 5.5/10 |
| **M27** | Customer Research | 30 | L | **DONE** | **2 OpKits** (ICP + VOC) | 03A, 03B | Quality 6.5/10 |
| **M10** | **Pricing & Offer** | 6 | S | **DONE** | **1 OpKit** (OK-M10-001) | 07 | Quality 7.4/10. 6 content files + OpKit + dialogue summary. Subscription-first pricing, wave-gated SKU expansion. |
| **M16** | **Content & SEO** | 9 | M | **DONE** | **1 OpKit** (OK-M16-001) | 13 | Quality 8.4/10. 7 content files + OpKit + dialogue summary. 9 Danilo tabs (225 rows) → 7 files. HARO replaced. YMYL/E-E-A-T. Founder Mode cadence. Marine plasma = uncontested keywords. |
| **M23** | **Influencer & Creator** | 15 | L | **DONE** (8.0/10) | **1 OpKit** (OK-M23-001) | 25 | Quality 8.0/10. 15 Danilo tabs (377 rows) → 7 production files. Heavy deduplication (500/508, 501/509, 503/511 near-duplicates). Key: attribution framework (direct+indirect), pre-launch FTC compliance package (GATING requirement), Phase 0/1/2 budget distinction, vetting scorecard (7 criteria, min 3.5/5), IonWave-specific influencer map (Huberman/DeLauer/Berry targets), contract templates, content retirement policy. |
| M28 | Market Expansion | 20 | L | **DONE** | **8.3** | 21 | Expansion paths, Amazon, B2B, constraint scenarios. 20→9 files. 14 dialogue upgrades. OK-M28-001 |
| **M29** | **PR & Communications** | 7 | S | **DONE** | **1 OpKit** (OK-M29-001) | 13 | Quality 7.6/10. 4 content files + OpKit + dialogue summary. 7 Danilo tabs (208 rows) → 4 files. Tabs 621+622 merged. Weekly PR time budget capped. Tiered media targets. Founder Mode video/podcast phasing. Supplement-specific crisis playbook. |

**Cluster estimate**: COMPLETE (0 hrs remaining)
**BCL-5 COMPLETE!** All 7 TUPs done: M10, M16, M23, M26, M27, M28, M29. First full cluster completed (after BCL-4 which has M19 outstanding in Session E).

---

### BCL-6: Operations & Infra (DANILO CANON) — 6/8 done (75%)

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| M1 | Labor Chain & Deployment | 16 | L | DONE | 8.6/10 | 16, 35 | Role engineering (7 dimensions), labor sequencing, overdetermined coordination, operator system, Trustee framework, CM grading |
| M9 | Ecommerce Infra | 10 | M | **DONE** (8.5/10) | **OK-M9-001** | 31 | 10→4 files. Week 1 Setup Sequence, theme perf budget, MER>ROAS, subscription UX, Consent Mode v2, ad hijacking prevention. 6 rounds, 14 upgrades. |
| M24 | Fulfillment & Inventory | 10 | M | **DONE** (8.4/10) | **OK-M24-001** | 15 (unavailable) | 10→4 files. Green-field build. Phase-gated fulfillment (self→3PL→multi-node), supplement compliance (FDA/FEFO/temperature), subscription demand modeling with cohort decay, launch ops (soft launch+war room+72hr+first 10), contract negotiation checklist. 6 rounds, 27 upgrades. |
| M30 | Analytics & Dashboards | 9 | M | **DONE** (8.2/10) | **OK-M30-001** | 18, 34 | 9→4 files. MVD (7 metrics), existential vs monitoring kill criteria, MER>ROAS, attribution model, phase-gated analytics, graceful degradation. 6 rounds, 13 upgrades. |
| **M31** | **Hiring** | 31 | XL | **DONE** (8.0/10) | **OK-M31-001** | 16 (archived) | 31→5 files (hiring strategy, processes, job specs, compensation, industry perspectives). Green-field build (File 16 not used). 6 rounds, 6 upgrades: PM Competence Framework (18-question scorecard >60 before ad spend prevents $5-10K waste), operator equity 10-25% with dilution waterfall, 3-4 PM maximum constraint (anti-scaling), pipeline-building 4-6 weeks early (achievable 2-4 week hire timeline), hybrid creative sprint model (remote 90% + co-locate 3-5 days every 6-8 weeks = $2-6K/year quality investment), community engagement sourcing playbook (Trends.vc/Discord lurk→contribute→DM). Job specs for 11 roles (operator, Creative/Ops/Growth PMs, Head of Ops, CM, CEO/CFO/VP) phase-gated by MRR ($0/$15-25K/$30-50K/$75-150K+ triggers). CEO/CFO/VP marked Phase 3+ post-PMF. Novel: PM competence prevents waste, operator equity model balances cash conservation + ownership, 3-4 PM constraint simplifies before scaling. |
| **M35** | **Execution Plans & Rhythms** | 25 | L | **DONE** (8.2/10) | **OK-M35-001** | 04, 28, 31 (archived) | 25→5 files (30/90/365 plans, operating rhythms, meeting templates, phase checklists/SOPs, detailed timelines). Green-field build (no Bootstrap sources). Industry research A-grade (Amazon WBR, First Round PMF, D2C 2026). IonWave C/D-grade (pre-launch). 6 rounds, 8 upgrades: CAC phasing, supplier pre-work (Week -2 CoA), MBR scaling (60 min solo/90 min team), dual LTV gate (LTV:CAC >3.0 + Month 3 retention >60%), 3PL timing (quotes Month 3, trigger 150/month OR >10 hrs/week), kill discipline (WBR forcing function), crisis mode (circuit breaker), hour-by-hour Week 1. 2 unresolved gaps (burnout, market saturation). Novel: choreography framework (feed-forward loops), phase-gated strictness (objective gates), crisis mode protocol, pre-launch supplier work. OpKit: 12-step universal framework with scaffolds. |
| M36 | Operational Infra | 43 | XL | NOT STARTED | TBD | 19, 28 | **Biggest non-governance TUP**: knowledge mgmt, risk, RACI, quality |
| M37 | AI & Automation | 5 | S | DEFERRED | TBD | 19 | **Deferred**: content is self-referential (our AI ops process). Better to write after 10+ sessions of actual practice rather than speculate now. Revisit after Wave 5+. |

**Cluster estimate**: 2XL + 2L + 2M + 1S = ~14 hrs remaining (M9, M24, M30 done)
**Low-hanging fruit?** M37 deferred. M1 (16 tabs, L) is the next most accessible. M31/M36 are massive — defer.

---

### BCL-7: Governance & School (DEFERRED) — 0/2

| TUP | Name | Danilo Tabs | Effort | Status | OpKit Status | Bootstrap Sources | Notes |
|-----|------|-------------|--------|--------|-------------|-------------------|-------|
| M32 | School Model | 20 | L | DEFERRED | TBD | 35 | School architecture, enrollment, curriculum, TUP portfolio |
| M33 | Governance & CM | 46 | XL | DEFERRED | TBD | 23, 30, 32, 33 | **Largest TUP** (46 tabs): CM rulebook, grading, audit, controls |

**Cluster estimate**: 1XL + 1L = ~8 hrs (DEFERRED)

---

## Summary Scoreboard (Revised with Danilo Tab Data)

| Cluster | Total | Done | Remaining | Content Tabs | Est. Hours | Priority | Blocked? |
|---------|-------|------|-----------|-------------|------------|----------|----------|
| BCL-4 Retention & Lifecycle | 6 | 6 | 0 | — | — | **✅ COMPLETE** (1st cluster done) | No |
| BCL-5 Growth & Market | 7 | 7 | 0 | — | — | **✅ COMPLETE** (2nd cluster done) | No |
| BCL-1 Product & Science | 4 | 4 | 0 | — | — | **✅ COMPLETE** (3rd cluster done) | No |
| BCL-3 DR & Creative | 5 | 5 | 0 | — | — | **✅ COMPLETE** (4th cluster done) | No |
| BCL-2 Money & Legal | 4 | 4 | 0 | — | — | **✅ COMPLETE** (5th cluster done) | No |
| BCL-0 Thesis & Meta | 5 | 1 | 4 | 99 | ~12 | 6th — M39 only, defer rest | No |
| BCL-6 Operations & Infra | 8 | 6 | 2 | 148 | ~8 | M1 (8.6), M9 (8.5), M24 (8.4), M30 (8.2), M35 (8.2), M31 (8.0) done. Next: M36 (M37 deferred) | No |
| BCL-7 Governance & School | 2 | 0 | 2 | 66 | ~8 | DEFERRED | By decision |
| **TOTAL** | **41** | **34** | **7 active + 3 deferred** | **~683** | **~21 hrs** | | |

---

## Recommended Workshop Order (Low-Hanging Fruit First)

### Wave 1 — Smallest TUPs First (~1.5 hrs)
**M21** (Subscriptions, 5 tabs), **M22** (Referral, 6 tabs), **M10** (Pricing, 6 tabs)
*Rationale: All ≤6 Danilo tabs. Quick wins to build momentum and refine the workshop process. M37 (AI & Automation) removed — deferred because content is self-referential and better written after more operational experience.*

### Wave 2 — Small TUPs (~2 hrs remaining)
~~**M14** (Testing, 7 tabs)~~ **DONE**, **M29** (PR, 7 tabs), ~~**M16** (Content & SEO, 8 tabs)~~ **DONE**, ~~**M25** (Bookkeeping, 6 tabs)~~ **DONE**
*Rationale: All ≤8 tabs. M14/M16/M25 completed. M29 remains.*

### Wave 3 — BCL-4 Mediums (~2.5 hrs remaining)
~~**M20** (Support, 9 tabs)~~ **DONE**, ~~**M17** (Email, 11 tabs)~~ **DONE** (8.4/10), ~~**M18** (Email Lifecycle Flows, 12 tabs)~~ **DONE** (8.7/10) — **BCL-4 COMPLETE** ✅
*Rationale: Completes BCL-4 (first full cluster done). Lifecycle cluster is cohesive.*

### Wave 4 — BCL-4/5/6 Mediums (~2 hrs)
~~**M19** (Customer Lifecycle, 13 tabs)~~ ✅ DONE (8.4/10), **M9** (Ecommerce Infra, 10 tabs), **M24** (Fulfillment, 10 tabs)
*Rationale: Moderate complexity, self-contained operational TUPs.*

### Wave 5 — BCL-3 Core (~5 hrs)
**M11** (VSL, 14 tabs), **M13** (Media Buying, 14 tabs), **M15** (Landing Pages, 18 tabs)
*Rationale: Creative pipeline minus M12 (26 tabs, save for later).*

### Wave 6 — Larger TUPs (~8 hrs)
**M5** (Formulation, 15 tabs), **M6** (Supply Chain, 13 tabs), **M7** (Regulatory, 11 tabs), **M8** (Brand Identity, 16 tabs)
*Rationale: BCL-1 Product & Science complete. Domain-heavy, benefits from M0/M26/M27 context.*

### Wave 7 — Remaining Mediums/Large (~6 hrs)
**M4** (Fundraising, 9 tabs), **M23** (Influencer, 15 tabs), **M30** (Analytics, 9 tabs), **M39** (Conceptual, 12 tabs)
*Rationale: Mixed cluster grab bag of moderate TUPs.*

### Wave 8 — Large Complex TUPs (~10 hrs)
**M1** (Labor, 16 tabs), **M28** (Market Expansion, 20 tabs), **M40** (Navigation, 18 tabs), **M2** (Entity & Legal, 15 tabs)
*Rationale: Cross-cutting TUPs with dependencies.*

### Wave 9 — XL TUPs (~12 hrs)
**M12** (Ad Creative, 26 tabs), **M35** (Execution Plans, 25 tabs), **M34** (Trade Architecture, 25 tabs), **M31** (Hiring, 30 tabs)
*Rationale: Large TUPs requiring sustained focus. Schedule as dedicated sessions.*

### Wave 10 — Critical Path + System (~12 hrs, UNBLOCK FIRST)
**M3** (Financial Model, 15 tabs — needs REC-001 resolution), **M38** (Strategic Frameworks, 44 tabs), **M36** (Operational Infra, 43 tabs)
*Rationale: M3 blocked by margin dispute. M38/M36 are the two largest non-governance TUPs.*

### Wave 11 — Governance (when ready)
**M32** (School Model, 20 tabs), **M33** (Governance & CM, 46 tabs)
*Rationale: Deferred by decision. M33 is the single largest TUP in the system.*

---

## OpKit Tracking Summary

| Status | Count | TUPs |
|--------|-------|------|
| **Registered** | 33 OpKits across 29 TUPs | M0 (4), M1 (1), M2 (1), M3 (1), M4 (1), M5 (1), M6 (1), M7 (1), M8 (1), M9 (1), M10 (1), M11 (1), M12 (1), M13 (1), M14 (1), M15 (1), M16 (1), M17 (1), M18 (1), M19 (1), M20 (1), M21 (1), M22 (1), M23 (1), M24 (1), M25 (1), M26 (1), M27 (2), M28 (1), M29 (1), M30 (1) |
| **TBD** | 24 TUPs | All remaining — OpKits identified during workshop |
| **OpKit Library** | 1 | Lives in M38 (ops_model_v10_dump/opkit_library) |

**Rule**: Every TUP workshop must produce at least 1 OpKit. The OpKit is the reusable artifact that makes the system scale beyond IonWave.

---

## Change Log

| Date | Session | Change |
|------|---------|--------|
| 2026-02-11 | M2 workshop | M2 Entity & Legal workshopped: 15 Danilo tabs → 22 total files (15 content + 5 supporting + 2 system registrations), quality 8.2/10, OK-M2-001 registered, 6-round dialogue to saturation (8 upgrades, 3 consecutive RESOLVED). Content tabs: legal_checklist (formation sequence, cost estimates, priority ordering), tax_and_entity_structure (Delaware C-Corp recommendation, DAO-compatible phased architecture, 83(b)/QSBS/NOLs, Studio 4 holding company analysis), cap_table (pre-seed structure, ESOP design, dilution waterfall, hygiene rules), entity_formation_guide (ODD-5 Week 1-4 execution, common mistakes), governance_overview (ODD-6 phase-gated governance Founder→Full+DAO, DAO firewall principle), board_of_directors (evolution 1→5-7 seats, meeting ops, compensation, protections), advisory_board (4-6 slots mapped to IonWave domains, FAST agreements, scoring criteria), trademark_ip_registration (USPTO filing, asset inventory, trade secrets, holding company IP licensing architecture), terms_of_service (FTC Negative Option Rule, DSHEA disclaimer, subscription terms), privacy_policy (GDPR+CCPA+24-state compliance, health data DPIA requirement, CMP comparison, BIPA warning), cookie_policy_gdpr (cookie inventory, Consent Mode v2, GPC signal, dark patterns avoidance), insurance_checklist (4-tier priority matrix, supplement carriers, budget projections), bank_account_setup (Mercury/Relay/Brex 2026 comparison, account structure, payment integration, security), equity_strategy (SAFE vs convertible notes, SAFE stacking dilution warning, vesting, DAO token integration), what_if_sued (8 litigation scenarios: product liability/FTC/Prop 65/subscription/trademark/employment/data breach/co-founder, emergency contacts, legal budget). Supporting: ip_m2_industry_perspectives (all 5 IP sections complete), opkit_entity_legal (OK-M2-001 with 12-step instructions, A-F rubric, scaffold, universal principles), _dialogue_summary (6 rounds, Corporate Attorney/Startup CFO/E-commerce Compliance Counsel), _quality_assessment (8.2/10), _meta. System: opkits/registry (OK-M2-001), manifest (M2 migrated, quality 8.2, count 23→24). Key innovations: phase-gated entity architecture (C-Corp Phase 1 → Holding Co Phase 2 → DAO LLC Phase 3, planned Day 1 executed incrementally), IP-at-parent-level LVMH-inspired strategy (IP ownership holding company, licensed to operating entities), SAFE stacking dilution warning (post-money SAFEs additive not averaged, counterintuitive dilution), Section 351/368 restructuring tax risk (tax-free reorganization NOT automatic), health data DPIA requirement (product quizzes collecting health data = mandatory DPIA under CPPA 2026), privacy-as-brand-value positioning (GDPR-level privacy as trust signal, not minimum compliance), CRITICAL decision gates (founder equity split + holding company must be decided BEFORE first SAFE issuance). Dialogue upgrades (8): holding company timing/costs, SAFE pro-rata preservation, Section 351 tax trap, health data DPIA, founder equity decision gate escalated CRITICAL, foreign qualification deferred, DAO veto mechanism deferred Phase 3, marine plasma insurance pricing requires actual quotes. Hypothesis cross-ref: HYP-004 (Gross Margin Sustainability) via entity tax structure (C-Corp 21% rate), insurance costs as fixed overhead, legal compliance costs — M10 flagged HYP-004 needs revision 67%→62-64% blended margin; M2 legal/insurance costs additional overhead factored into contribution margin. **BCL-2 now 2/4 done (50%)** — M2, M25 complete; M3, M4 still blocked by REC-001. 28 TUPs workshopped (29 including M0), 32 OpKits registered. |
| 2026-02-11 | M5 registration | M5 Formulation registration update: Workshop was completed 2026-02-10 (quality 8.5/10) but not yet registered in system. Updated manifest.json (m5 status not_migrated→migrated, migrated_tups 21→22, added full metadata), opkits/registry.json (registered OK-M5-001 with full description), TUP_Workshop_Tracker.md (workshopped 26→27, BCL-1: 3/4→4/4 COMPLETE, OpKits 29→30, Summary Scoreboard updated — BCL-1 now 3rd fully complete cluster after BCL-4 and BCL-5), SESSION_LOG.md entry. M5 delivers: 5 content files (2,247 total lines), 6-round dialogue (22 upgrades), OK-M5-001 OpKit. Key: exceptional confidence honesty (9.5/10 — all supplier-dependent data marked [VOID — requires CoA]), ocean-sourced vs synthetic electrolytes comparison (bioavailability 66-90%+ vs 9-105%), 78-trace-mineral reality check (only 20 elements biochemically required), FDA/FTC compliance integration, M6 supplier vetting integration. Pre-launch blockers: supplier CoA (Week 1-2), taste testing (Week 3-4, 50-100 users), stability testing (Month 3-6), bioavailability RCT (Q3 2026, $50-150K). **BCL-1 now 4/4 COMPLETE (100%)** — IonWave launch-ready for formulation, supply chain, regulatory, and brand identity. |
| 2026-02-10 | M8 workshop | M8 Brand Identity workshopped (Phases 8-11 completion): 16 Danilo tabs → 7 content files (brand_strategy, brand_voice_tone, packaging_design, brand_naming_domain, brand_messaging_storytelling, remaining_brand_systems, industry_perspectives) + dialogue_summary (9 rounds, 5 upgrades) + m8_workshop_summary + OK-M8-001 OpKit. Quality 7.8/10. Key: Positioning ('accessible marine plasma' Phase 1 → 'complete mineralization' Phase 2+), Informed Guide voice archetype (5 principles: science-backed not academic, explain don't gatekeep, transparency-first, conversational-professional, evidence-grounded), packaging system (sachet/box/mailer, FDA compliance checklist, Prop 65 strategy, unboxing progress tracker), brand naming evaluation (IonWave trademark/domain strategy), messaging architecture (brand story, awareness ladder, 3 tagline variants by context, 5 social pillars), visual identity system (logo/typography/color/photo briefs), 3-phase brand evolution model (Challenger → Category Ownership → Market Leader), competitor audit (LMNT/AG1/Momentous/Quinton positioning map), 3 contrarian takes, industry perspectives (D2C supplement branding 2026). Research: 4 web searches (D2C brand identity 2026, marine plasma branding, packaging design, competitive voice analysis). Personas: Brand Strategist, CPG Designer, Copywriter. 5 dialogue upgrades: (U1) sachet vs box messaging split for positioning flexibility (sachet evergreen, box flexible), (U2) Supplement Facts Panel escalated to CRITICAL blocker (not Phase 2 upgrade), (U3) absorption claims softened (98% vs 10-15% → 'highly bioavailable ionic form'), (U4) tagline separated by context (ads='78 Minerals. 30 Seconds. Zero BS.' vs packaging='Complete Mineralization, Simplified.'), (U5) inside lid progress tracker added (30-day checklist). 6 CRITICAL blockers flagged: logo, photography, CoA, Prop 65, trademark, domain. Intelligence gaps documented with upgrade paths (14 gaps: 6 CRITICAL, 4 HIGH, 4 MEDIUM). **BCL-1 now 3/4 complete (75%)** — M6/M7/M8 done, only M5 (Formulation) remains. 26 TUPs done, 29 OpKits registered. |
| 2026-02-10 | M13 workshop | M13 Media Buying workshopped: Bootstrap File 12 (5 sheets) + 2026 research → 14 production files, quality 10.0/10 (**perfect score**), OK-M13-001 registered, 12-round dialogue to saturation (9 upgrades, 0 unresolved). Personas: Performance Media Buyer, Attribution Engineer, D2C CFO. Key: 2026 CPM benchmarks (Meta $7-15, TikTok $4-20, YouTube $3.53-7.10, Google $2.54-36.82 — all A-grade sourced), post-iOS 14.5 attribution stack (Pixel+CAPI dual tracking, EMQ >7.0, server-side tools: Elevar/Triple Whale/Northbeam/Cometly, MER framework M30 integration), tiered scaling rates by conversion volume (<30=20%, 30-100=30%, 100+=40-50%), channel profitability P&L model (contribution margin > raw CAC, working capital formula for negative-CM scaling), 4-phase diversification plan (<50% single platform by Month 12), creative fatigue timelines (2-4 weeks industry standard, frequency-driven monitoring), tracking validation checkpoints (Day 1-2 post-scaling prevents $10K+ waste on broken attribution), attribution gap decision framework (20-60% divergence = unclear signal vs >60% = investigate), Advantage+ Campaign Budget adoption tiers ($500/$3K/$5K+ spend thresholds), cold start protocol (bridges first_100_ads bootstrap phase to winning_ad_iterations scale phase), automated rules (kill <1 conv/$30 spend, surf scaling ROAS >3.0). 9 critical dialogue upgrades: U1 tiered scaling rates (CFO: "don't scale fixed 20% at 100+ conversions"), U2 attribution gap thresholds (Eng: "20-60% is unclear not broken"), U3 EMQ monitoring + iOS 17 LTP realistic expectations, U4 cold start protocol (Buyer: "how do you actually execute first_100_ads?"), U5 cash flow implications (CFO: working capital formula), U6 tracking validation checkpoints (Eng: Day 1-2 audit gates), U7 frequency-driven fatigue monitoring (Buyer: shifts budget 30-60 days early), U8 diversification profitability gate (CFO: "don't scale negative-CM channels"), U9 Advantage+ tiers (Buyer: budget-based adoption). Bootstrap File 12 Quality Score methodology elevated to universal customer acquisition framework. BCL-3 now 4/5 (80% complete — only M12 26-tab XL remains). 23 TUPs done, 27 OpKits registered. |
| 2026-02-10 | M11 cleanup | M11 administrative cleanup (interrupted session from 2026-02-09): cleared ACTIVE_WORK.md claim, added SESSION_LOG.md entry, updated TUP_Workshop_Tracker.md (BCL-3 now 3/5, 22 TUPs done, 26 OpKits). M11 quality 9.2/10 — highest to date. |
| 2026-02-09 | M15 workshop | M15 Landing Pages & Conversion workshopped: 18 Danilo tabs (~738 rows) → 5 production files, quality 8.2/10, OK-M15-001 registered, 6-round dialogue to saturation (25 upgrades, 3 critical, 23 applied). Heavy deduplication (Psychology ×3, Headlines ×3, Templates ×3, Checkout ×3). Key innovations: 8 funnel architectures (A-H including LP+VSL Hybrid), conversion equation (Desire − Friction − Anxiety), 5-second test methodology, comprehensive FTC/DSHEA/Prop 65 compliance framework, subscription-first checkout with Shop Pay priority (50% conversion lift), sensitivity analysis for funnel economics (pessimistic/realistic/optimistic), modular LP design for creative fatigue (2-4 week cycles), server-side tracking requirement (client-side misses 15-25%), Emma Relief as cautionary reference (replicate funnel structure, avoid aggressive practices — BBB F rating). 3 CRITICAL compliance upgrades: FTC negative option rule (Jan 2024 revision), California Prop 65 CoA testing for marine plasma, FTC click-to-cancel rule (2025). 7 corrections: fictional testimonials flagged (Marcus T., Jennifer R., David K.), 98% bioavailable claim needs citation, 10,000+ optimizers is pre-launch fiction, 127 reviews / 4.8 stars placeholder (FTC violation risk), René Quinton blood plasma claim oversimplified, guarantee language fixed, heavy deduplication consolidated. BCL-3 now 2/5 complete. M1 HYP-001 hypothesis index references added (carried from prior session). |
| 2026-02-09 | M9 workshop | M9 Ecommerce Infrastructure workshopped: 10 Danilo tabs (274 rows) → 4 production files, quality 8.5/10, OK-M9-001 registered, 6-round dialogue to saturation (14 upgrades, 0 unresolved). Tabs 285/288 merged (duplicate tool stacks), tabs 289/290 merged (duplicate page speed checklists). Key innovations: theme performance budget (8 apps max, 500KB JS, 3 external scripts — hard limits enforced), Week 1 Setup Sequence (Day 1-7 strict priority order — prevents 3-week launch delays), subscription-first UX pattern (toggle > dropdown, subscription price shown first, 15-20% conversion lift), MER>ROAS alignment with M30 (corrected Danilo tab 287 "blended ROAS" north star), Shopify-specific speed killers (Liquid render loops, app residue in theme.liquid, collection pagination — not generic web advice), ad account hijacking prevention (#1 real threat for D2C: Meta phishing, spend caps at 2x daily budget), Consent Mode v2 from Day 1 (future-proofs GDPR/CCPA, enables GA4 behavioral modeling), "Do Not Install" app list (SEO apps, currency converters, social proof pop-ups — all redundant with Shopify native), monthly Tool ROI Review starting Month 2 (one-sentence ROI test for every paid tool), phase-gated governance (essentials only pre-launch, unlock quarterly audits at Month 3), theme backup protocol (export before every app install), collaborator account audit (quarterly check Settings → Users → Collaborator section), checkout extensibility note (Extensions over checkout.liquid), UTM builder template (Google Sheet with dropdowns to prevent inconsistency). Research-verified: Shopify 2026 pricing ($29/$79/$299), Core Web Vitals 2026 (INP replaced FID March 2024), Shoplift/Intelligems as Google Optimize replacements, server-side tracking best practices (Meta CAPI, sGTM). BCL-6 now 2/8 complete. |
| 2026-02-08 | M30 workshop | M30 Analytics & Dashboards workshopped: 9 Danilo tabs (~161 rows) → 4 production files, quality 8.2/10, OK-M30-001 registered, 6-round dialogue to saturation (13 upgrades, 0 unresolved). Tabs 629/630/631 merged (dashboard duplicates). Key: Minimum Viable Dashboard (MVD) — only 7 metrics for Phase 1 solo founder (Revenue, Orders, Ad Spend, CAC, Subscription Rate, Cash, MER), MER elevated as primary efficiency metric over ROAS (platform ROAS overstates 20-40% post-iOS 14.5), existential vs monitoring kill criteria classification (3 existential: Cash Runway, CAC, Contribution Margin; 9 monitoring: everything else), awareness vs conversion attribution model (survey = how they found you, UTM = what drove the click; disagreement = multi-touch not error), simplified early-stage MBR (4 questions, 1 hour max for Months 1-3), V0 Master Consistency Check elevated to first validation rule (kill criteria source of truth must match monitoring thresholds), subscription conversion diagnostic decision tree (visibility → pricing → product confidence → trust), Google Sheets MVD template as OpKit deliverable, data source hierarchy with known limitations column (GA4 under-reports 10-25%, Meta over-reports 20-40%), email revenue % phase-gated to Month 3+ (requires 1K+ subscribers), vanity metrics ban list for Phase 1 (followers, pageviews, engagement rate), graceful degradation policy (daily pulse is non-negotiable, everything else can be recovered), monthly hypothesis prompt (one sentence per critical HYP). First BCL-6 TUP completed (1/8). |
| 2026-02-08 | M28 workshop | M28 Market Expansion workshopped: 20 Danilo tabs (~464 rows) → 9 production files, quality 8.3/10, OK-M28-001 registered, 7-round dialogue to saturation (14 upgrades, 0 unresolved). Tabs 606/607 merged (Amazon duplicates), 608/609/610 absorbed into Amazon and channel playbooks. Key: anti-cannibalization price parity strategy (D2C subscription always best deal > Amazon S&S > wholesale MAP), Amazon cold start 4-phase plan (seed from D2C → long-tail PPC → Vine → broaden), MAP pricing policy ($44.10 floor), B2B auto-reorder for gym accounts (60-70% churn without), moonshot activation lock (<$50K MRR = READ-ONLY), white-label guardrails (never hero SKU, 1K min volume, territory exclusions), B2B unit economics model (LTV:CAC 13.2x at 80% retention), subscription conversion sensitivity (viable to 30%, crisis at <20%), SEO sequencing revised (Phase 2 Month 3-6 not pre-launch), planned vs unplanned channel concentration distinction, VOC pipeline for measurable product triggers, quarterly product iteration cycle with reformulation gates (60% blind test threshold), retail capital requirements ($50-200K+ per tier), multi-touch attribution model (simple Day 1 stack). **BCL-5 NOW COMPLETE (7/7).** First full cluster finished. |
| 2026-02-08 | M23 workshop | M23 Influencer & Creator workshopped: 15 Danilo tabs (377 rows) → 7 production files, quality 8.0/10, OK-M23-001 registered, 8-round dialogue to saturation (6 upgrades, 0 unresolved). Heavy deduplication (tabs 500/508, 501/509, 503/511, 505/506/514 were near-duplicates). Key: attribution framework (direct code redemptions + indirect branded search lift), pre-launch FTC compliance package as GATING requirement (4 components: talking points, prohibited claims, monitoring, violation response), Phase 0/1/2 budget distinction (Phase 0 = product seeding COGS only, Phase 1 = UGC creators IS the ad creative budget, Phase 2 = paid influencer deals gated by >1.5x ROAS), weighted vetting scorecard (7 criteria, min 3.5/5.0), IonWave influencer map (Tier 1 dream: Huberman/Attia, Tier 2 achievable: DeLauer/Berry, Tier 3 micro: volume seeding), pre-outreach competitive screening (15-min check per target), contract templates (influencer + creator with supplement compliance), content retirement policy (semi-annual audit), revised repurposing multiplier (6-10, not 8-12) with compliance checkpoints on derivatives. BCL-5 now 6/7 — only M28 remains. |
| 2026-02-07 | M19 workshop | M19 Customer Lifecycle & CRM workshopped: 13 Danilo tabs (232 rows) → 4 production files, quality 8.4/10, OK-M19-001 registered, 5-round dialogue to saturation (8 upgrades, 0 unresolved). Key: "Model IS the CRM" architecture (every TUP is a CRM node), non-linear lifecycle paths (shortcuts, oscillations, skips), Minimum Viable CRM (3 Day-1 flows, 8-11 hours vs. 3 weeks), at-risk sub-segmentation (Product/Budget/Attention with distinct interventions), churn risk score formula at two complexity levels (Phase 1 simple ratio + Phase 2 four-signal weighted model), confidence intervals on cohort data (50 customers = ±14% CI), customer-count tool triggers (500+ for analytics, not revenue-based), founder daily 5-minute CRM check-in protocol, phase-gated CRM stack (5 phases by customer count), dual-layer segmentation (behavioral + RFM), seasonality in churn metrics with 3-month rolling averages. BCL-4 now 5/6 complete. |
| 2026-02-07 | M17 workshop | M17 Email & SMS workshopped: 27 Danilo source files (~600+ rows, 11 content tab groups) → 9 production files, quality 8.4/10, OK-M17-001 registered, 7-round dialogue to saturation (5 upgrades, 0 unresolved). Exceptionally rich source material with production-quality email copy for 4 major sequences. Key: Founder Mode build order (3 flows at launch), discount defense policy (different incentive types per flow, no stacking, time-gated escalation), FTC compliance checklist for supplement health claims, segmentation trigger thresholds (don't segment until data warrants), maintenance time budget (1.5-4 hrs/month for 3-12 flows), source of truth policy (markdown = blueprint, Klaviyo = live), SMS deferred to Month 3+ (collect opt-ins from Day 1), box insert kit from Day 1 ($0.50-0.70/package). M17 absorbed SMS scope from M18 — M18 may be reduced. |
| 2026-02-07 | M20 workshop | M20 Customer Support workshopped: 9 Danilo tabs (204 rows) → 3 production files, quality 8.6/10, OK-M20-001 registered, 8-round dialogue to saturation (6 upgrades, 0 unresolved). Key: Founder Mode vs Team Mode escalation phase-gating, chargeback monitoring (Stripe 0.75% threshold as existential risk), behavioral activation criteria (4 measurable criteria, self-report removed as gating), minimum viable support stack ($60/mo vs $1,300/mo), FDA adverse event protocol (A-grade compliance), open-ended-first win/loss survey methodology with decision triggers, expected outcomes timeline for marine plasma, 6 support macros including adverse reaction escalation. |
| 2026-02-07 | M29 workshop | M29 PR & Communications workshopped: 7 Danilo tabs (208 rows) → 4 production files, quality 7.6/10, OK-M29-001 registered, 5-round dialogue to saturation (5 upgrades, 0 unresolved). Key: weekly PR time budget capped (2-3 hrs/week Phase 1), tiered media targets (achievable + aspirational), Founder Mode video phasing (defer YouTube to Month 4-6, podcast to Month 8+), supplement-specific crisis playbook (FTC, adverse reactions, ad account bans, competitive claim copying), minimum viable press pitch checklist, tabs 621+622 merged into single crisis_playbook.md. |
| 2026-02-06 | M25 workshop | M25 Financial Operations workshopped: 6 Danilo tabs (105 rows) → 3 production files, quality 8.8/10, OK-M25-001 registered, 8-round dialogue to saturation (6 upgrades, 0 unresolved). Green-field build (no Bootstrap sources). Key: dual-margin REC-001 treatment (gross margin for P&L, contribution margin for channel decisions), Day 1 Essentials 18-account chart, Survival Five condensed MBR scorecard (Month 2-6), phase-gated sales tax strategy, 13-week cash forecast with example numbers, Synder/A2X connector gap elevated to CRITICAL pre-launch validation. |
| 2026-02-06 | M16 workshop | M16 Content & SEO workshopped: 9 Danilo tabs (225 rows) → 7 production files, quality 8.4/10, OK-M16-001 registered, 8-round dialogue to saturation (5 upgrades, 4 unresolved). Key: HARO replaced with Qwoted/Featured.com, YMYL/E-E-A-T infrastructure for supplement content, Founder Mode publishing cadence (2 posts/month), marine plasma as uncontested SEO territory, native ads phase-gated as optional, Google Merchant Center free listings added, publishing sequence corrected (pillar first, comparisons after trust). |
| 2026-02-06 | M14 workshop | M14 Testing & Optimization workshopped: 7 tabs → 6 files (3 near-duplicate tabs consolidated), quality 7.5/10, OK-M14-001 registered, 4-round dialogue to saturation (9 upgrades, 0 unresolved). Near green-field build. Key: Google Optimize replaced, two-stage kill criteria, traffic-based methodology, tool spend ≤5% discipline, passive audience learning from Meta breakdowns. |
| 2026-02-06 | M22 workshop | M22 Referral & Community workshopped: 6 tabs filled, quality 7.0/10, OK-M22-001 registered, 4-round dialogue to saturation (6 upgrades, 0 unresolved). Key: LMNT comparative claim removed (legal risk), Geneva discontinued, Loop/Smile integration flagged CRITICAL. |
| 2026-02-06 | M10 workshop | M10 Pricing & Offer workshopped: 6 tabs filled, quality 7.4/10, OK-M10-001 registered, 8-round dialogue to saturation (4 upgrades, 0 unresolved) |
| 2026-02-06 | #8 | v1.0.0 → v1.1.0: Added Danilo content tab counts, OpKit tracking column, revised effort estimates (45→74 hrs), reordered waves by actual tab count, added dual-output framework |
| 2026-02-06 | #8 | Created tracker v1.0.0 with effort estimates and workshop waves |
