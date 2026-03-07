# Decision Pre-Answers: The Danilo Pass

**Purpose**: Pre-loaded answers for each open decision, written in the way Danilo is likely to think about them. When Danilo opens a session and asks about decisions, Claude should present these as "Here's how I think you'd answer this — confirm, adjust, or push back."

**Why this exists**: Danilo thinks at the meta-level. He asks "how do we create the requisite variety such that this adapts to all possible outcomes?" and "how do YOU think I'd answer that?" These pre-answers honor that by giving him something to react to rather than starting cold.

**How to use**: Present each pre-answer conversationally. Let Danilo confirm or modify. When he locks one, update PROJECT_NERVE_CENTER.md and the source file per the resolution format in CLAUDE.md.

---

## CRITICAL DECISIONS

### #1 — Gross Margin: 40% vs 67% (REC-001)

**The Danilo answer**: "Both numbers are right — they're measuring different things. Stop trying to pick one."

**Pre-answer**: Accept the dual-margin treatment as the permanent architecture. Product-level GM is ~60-67% (what the product actually makes before overhead). Fully-loaded GM is ~40% (after fulfillment, shipping absorption, returns). The financial model uses both: product GM for pricing decisions, fully-loaded GM for cash flow and break-even.

**Why this is his answer**: Danilo doesn't collapse a spectrum into a single number when the spectrum carries information. The tension between 40% and 67% isn't a bug — it's two valid lenses. The $88K swing matters for modeling, not for the decision itself. He'd say: "Model both, present both, let the investor choose which lens they care about."

**What locks it**: Confirm that M3 uses 60% as working baseline, with dual-margin reporting in all financial docs. Fulfillment strategy and shipping absorption policy set the actual floor — those are the real decisions hiding inside this one.

**Cascading unlocks**: M3 Financial Model lock, M11/M13 break-even CPA, M25 dual-margin treatment, investor pitch margin claims.

---

### #2 — Positioning-Economics Tension (Q9)

**The Danilo answer**: "You don't pick one positioning — you build a structure that transitions between them."

**Pre-answer**: Option 1 (category creation within category) with a phased evolution. Launch with marine plasma differentiation as the *ingredient story* but target the broader electrolyte market as the *customer pool*. The pitch is "better electrolytes via marine plasma" — not "join the marine plasma movement." As the brand matures, the positioning can narrow or widen based on what the data shows.

**Why this is his answer**: Danilo would reject the premise that positioning is a one-time, binary choice. He'd frame it as: "The positioning IS the marine plasma science story. The market IS the electrolyte buyer. These aren't in tension — one is the differentiation, the other is the addressable audience. LMNT doesn't position as 'an electrolyte' — they position as 'the electrolyte for people who know better.' We position as 'the electrolyte that's actually from the ocean.'" He'd also say the category creation play (Option 4) is something that happens *as a consequence* of execution, not as a strategy you fund upfront.

**What locks it**: Confirm that brand messaging leads with marine plasma science/origin story, targets electrolyte market broadly (LMNT switchers, Liquid IV upgraders, health-conscious consumers), and that positioning narrows or widens based on first 90 days of acquisition data.

**Cascading unlocks**: Product Strategy, Brand Messaging, Creative Strategy, Investor Narrative coherence.

---

### #3 — Capital Sufficiency + Revenue Target (Q10/Q11)

**The Danilo answer**: "The question isn't 'how much money' — it's 'what's the minimum viable experiment to know if this works.'"

**Pre-answer**: Option 3 (staged approach). Raise $30-50K. Use it to validate exactly two things: (1) can you acquire customers at a CPA that works, and (2) do they reorder. If yes, raise more. If no, you saved everyone's money. The $30K MRR target is a *direction*, not a commitment — reframe it as "$10K MRR milestone triggers next raise conversation."

**Why this is his answer**: Danilo wouldn't try to predict whether $30K or $150K is "enough" — he'd design the system so it doesn't matter. Raise small, test fast, compound if it works. He'd say: "The question 'is $30K enough?' is unanswerable because it depends on CAC, which we don't know until we spend. So spend $30K to learn CAC, and then the answer reveals itself." He'd also push back on $30K MRR as a Year 1 target — not because it's wrong, but because stating it as a hard target creates false precision. Better: "$10K MRR = proof of concept, $30K MRR = proof of scale, timeline TBD by data."

**What locks it**: Confirm staged raise approach ($30-50K initial), $10K MRR as first milestone, follow-on raise conversation triggered at milestone, and that the financial model runs three scenarios (conservative/baseline/optimistic) rather than committing to one.

**Cascading unlocks**: Fundraising (M4), Financial Model (M3), all downstream planning.

---

### #4 — Founder Equity Split (M2-DEC)

**The Danilo answer**: "How do we structure this so that the equity reflects actual contribution over time, not a guess we make today?"

**Pre-answer**: Use dynamic/milestone-based vesting rather than a fixed split. Set a provisional split now (likely 70/30 or 60/40 Danilo/Caio, reflecting Danilo's IP, capital, and vision contribution), but tie the final split to contribution milestones over the first 12-18 months. Standard 4-year vest, 1-year cliff for both founders. This lets you form the entity and issue the first SAFE without making a permanent bet on a relationship that hasn't been tested operationally.

**Why this is his answer**: Danilo wouldn't want to guess the "right" split — he'd want a structure that *discovers* the right split through execution. He'd also recognize that this decision has emotional weight and that getting it wrong early poisons everything downstream. A provisional split with milestone-based adjustment gives both founders optionality and makes the conversation about contribution mechanics rather than a negotiation.

**What locks it**: Agree on provisional split ratio, vesting schedule, cliff, and what milestones trigger adjustment conversations. Then form the entity.

**Cascading unlocks**: Entity formation, cap table, first SAFE, all equity-based compensation (MBA intern, VP, Operator).

---

### #5 — Studio 4 vs Standalone Entity (M2-DEC)

**The Danilo answer**: "Don't optimize for structure — optimize for speed to first SAFE. Which one gets us there faster?"

**Pre-answer**: Standalone entity (new Delaware C-Corp for IonWave). Studio 4 as a holding company adds a layer of complexity that slows down the first SAFE, confuses investors who want to invest in *this* product not a holding company, and creates tax/legal overhead that only pays off if you're running multiple ventures simultaneously. IonWave needs its own clean cap table.

**Why this is his answer**: Danilo has the instinct for holding-company structures (Studio 4 = portfolio of ventures), but he also knows that investors want clean, simple cap tables. He'd reason: "Studio 4 can hold Danilo's personal equity in IonWave without IonWave being a subsidiary. The holding company and the product company don't need to be structurally linked to achieve the portfolio vision." If Studio 4 is already a legal entity, Danilo's shares in IonWave can be held by Studio 4 — you get the same result without the structural complexity.

**What locks it**: Confirm standalone C-Corp for IonWave, Danilo's shares optionally held via Studio 4 as a personal vehicle, and that attorney review covers both structures to confirm this approach.

**Cascading unlocks**: Entity structure, cap table, investor legal docs, first SAFE.

---

### #6 — Cascade Approval Authority (DEC-CHAIN-003)

**The Danilo answer**: "Option B with a structural twist — Claude handles process, but the system itself creates the selection pressure."

**Pre-answer**: Option B (Claude-assisted autonomy) as the default, with Option D's insight (VP→Operator handoff gets a calibration session). But add one mechanism: require each node to produce a *written evaluation artifact* that Claude archives. The VA writes up why they chose this MBA intern. The MBA intern writes up why they chose this VP. These artifacts create an audit trail and — crucially — force the selector to articulate their reasoning, which improves selection quality even without a human reviewer.

**Why this is his answer**: Danilo wouldn't pick "fully autonomous" (too risky for a first edition) or "Caio as backstop" (creates a dependency that breaks the one-shot model). He'd want the *system* to create quality pressure without inserting a human bottleneck. Written evaluation artifacts do this — they're a forcing function that makes the selector accountable to their own reasoning, reviewable after the fact, and usable as training data for future cascade iterations.

He'd also say: "If the system works, great. If it doesn't, the evaluation artifacts tell us exactly where it broke and why." Requisite variety: the system adapts by learning from its own selection history.

**What locks it**: Confirm Claude-assisted autonomy + mandatory written evaluation artifact at each handoff + calibration session at VP→Operator handoff. No human approval gate at VA→MBA or MBA→VP, but full audit trail.

**Cascading unlocks**: Rollout recruiting cascade activation, quality control model for entire chain.

---

### #7 — Pre-Entity Equity Instruments (DEC-CHAIN-007)

**The Danilo answer**: "Promise letter now, convert to proper instruments the moment the entity exists. Don't let legal perfection block operational momentum."

**Pre-answer**: Use a formal promise letter (signed, with specific terms: equity %, vesting schedule, cliff, conversion trigger) that automatically converts to a proper equity grant upon entity formation. This is standard for pre-incorporation startups. It's not legally bulletproof, but it's sufficient to recruit an MBA intern and pitch a VP. The moment the entity forms (unlocked by Decision #4), batch-convert all promise letters into proper grants.

**Why this is his answer**: Danilo wouldn't accept "we can't offer equity because we don't have an entity yet" as a reason to delay the cascade. He'd find the lightest-weight instrument that creates genuine commitment without requiring the entity to exist. Promise letters are that instrument. He'd also say: "The person joining at this stage isn't joining for legal certainty — they're joining for the opportunity. The promise letter is a signal of seriousness, not a legal contract." But he'd want it signed and specific, not vague.

**What locks it**: Confirm promise letter approach, template with specific equity terms (amount from DEC-CHAIN-001/002), conversion clause triggered by entity formation, and that attorney review is scheduled post-entity to validate/convert.

**Cascading unlocks**: MBA and VP compensation, rollout cascade activation.

---

## HIGH PRIORITY DECISIONS

### #8 — Single SKU or Multiple Flavors (Q2)

**The Danilo answer**: "Launch single. The product IS the ocean. Flavoring it would undermine the thesis."

**Pre-answer**: Option 3 (launch single, add flavors in wave 2). The core differentiation is "this comes from the ocean." An unflavored marine plasma sachet IS the product thesis made tangible. Adding flavors before you know if people want the core product dilutes the signal. If unflavored works, you've proven the hardest thing (people will drink ocean minerals). If it doesn't, you learn that before investing in flavor R&D.

**Cascading unlocks**: Production planning, creative strategy, inventory planning, cash requirements.

---

### #9 — DTC-Only or Retail (Q3)

**The Danilo answer**: "DTC-only. We need the data. Retail gives you revenue but steals your learning."

**Pre-answer**: Option 1 (DTC-only for first 6-12 months). Danilo would reason that the entire cascade model depends on proving the Trade works — and "works" means knowing your customer acquisition cost, retention rate, and unit economics at a granular level. Retail obscures all of this. DTC gives you the data layer. Retail is a scale lever you pull after you've proven the model.

**Cascading unlocks**: Pricing, unit economics, packaging, cash flow.

---

### #10 — Canonical Home: GitHub vs Google Drive (DEC-2026-02-17-002)

**The Danilo answer**: "GitHub is the system of record. Drive is the collaboration surface. Stop trying to pick one."

**Pre-answer**: Hybrid, but with clear hierarchy. GitHub = canonical source of truth (all TUPs, specs, tracking, financial models). Google Drive = working surface for collaboration, drafts, and Danilo's raw input. Sync is one-directional: Drive → GitHub (Caio migrates finalized work). This is already basically how it works — just formalize it.

**Cascading unlocks**: Monitoring/automation system, all future workflow.

---

### #11 — Monitoring Architecture (DEC-2026-02-17-003)

**The Danilo answer**: "GitHub Actions. We're already there. Don't split the stack."

**Pre-answer**: GitHub Actions. The project lives in GitHub. The compliance agent runs on Claude. The monitoring should live where the data lives. Apps Script would require maintaining a second system with a different auth model and different deployment pipeline. GitHub Actions + Claude API = one stack.

**Cascading unlocks**: Automated reviews (WBR, MBR, parameter checks).

---

### #12 — VA Budget (DEC-CHAIN-005)

**The Danilo answer**: "$1,000/month retainer. Enough to be serious, not enough to attract someone who's just in it for the paycheck."

**Pre-answer**: Monthly retainer, $800-1,200/month range. 6-week engagement with clear deliverables. This is a standard VA rate for someone capable of doing structured outreach and pipeline management. Hourly creates misaligned incentives (padding hours). Retainer creates accountability.

**Cascading unlocks**: VA hiring, cascade activation.

---

### #13 — Chain Parallelization (DEC-CHAIN-004)

**The Danilo answer**: "Overlap allowed. Sequential is for systems that can't handle complexity. This one can."

**Pre-answer**: Overlapping allowed with one constraint: the next node can't *activate* (start their deliverable clock) until the current handoff is complete. But sourcing and warm-up can begin in parallel. This compresses the timeline from 6-9 months to 4-6 months without introducing the coordination complexity of full parallelization.

**Cascading unlocks**: Timeline compression (4-6 months vs 6-9 months).

---

### #14 — Fallback at MBA→VP Link (DEC-CHAIN-006)

**The Danilo answer**: "The emergency valve exists. Acknowledge it, don't pretend it doesn't. But give the system the full 12 weeks first."

**Pre-answer**: Sequential fallback protocol: (1) Give the MBA intern the full 12 weeks. (2) If no VP by week 8, expand search criteria. (3) If no VP by week 12, Danilo introduces his VP contact. This isn't "cheating" — it's the system having a fallback. The one-shot model is the *aspiration*; the fallback is the *safety net*. Document this openly in the cascade spec so everyone knows the rules.

**Cascading unlocks**: Risk mitigation for hardest cascade link.

---

### #15 — CM Authority Model Threshold (CM-DEC)

**The Danilo answer**: "Don't set a threshold. Let it emerge. When Caio starts dropping balls, that's when you know."

**Pre-answer**: Don't define an MRR threshold. Instead, define *signals* that trigger the conversation: (1) WBR reviews consistently late or skipped, (2) more than 3 open decisions older than 30 days, (3) Claude escalations not actioned within 48 hours, (4) Caio explicitly flags capacity. These are adaptive triggers rather than arbitrary revenue gates.

**Cascading unlocks**: Governance model scaling.

---

## MEDIUM PRIORITY (Confirm defaults or defer explicitly)

### #16 — Subscription Incentive (Q4)
**Default**: 15% discount (LMNT model). A/B test free shipping post-launch. **Danilo would say**: "Ship the obvious default, test later."

### #17 — Influencer Strategy (Q6)
**Default**: Micro-influencer focus (10K-50K). Better ROAS, lower risk, more authentic for a new brand. **Danilo would say**: "Micro. We don't have the budget for macro mistakes."

### #18 — MBA Equity Amount (DEC-CHAIN-001)
**Pre-answer**: 1-2% with same vesting structure as other equity grants. Enough to be meaningful, low enough to not dilute meaningfully at this stage.

### #19 — VP Equity Amount (DEC-CHAIN-002)
**Pre-answer**: 7-8% (midpoint of 5-10% range) with 4-year vest, 1-year cliff. Plus a small monthly retainer ($2-3K) to cover their time during the sourcing phase. The equity is the real pitch.

### #20 — HYP-004 Target Revision (ISS-001)
**Pre-answer**: Accept 62-64% as revised target. 67% was structurally unachievable with subscription discount baked in. This is just math — confirm and move on.

---

## How to Run the Decision Session with Danilo

When Danilo opens this project and asks about decisions:

1. **Start with the meta-frame**: "We've pre-loaded answers for all 20 open decisions based on how you typically think about these kinds of problems — adaptive structures, requisite variety, systems that learn. Your job is to confirm, adjust, or push back."

2. **Go in dependency order**, not priority order:
   - Start with #4 (equity split) and #5 (entity structure) — these unblock everything
   - Then #7 (pre-entity equity) — unblocks the cascade
   - Then #1 (margin) and #2 (positioning) — unblocks financial model and brand
   - Then #6 (approval authority) and #12-14 (cascade ops) — unblocks rollout
   - Then #3 (capital/revenue target) — this one benefits from all the others being resolved first

3. **Expect him to go meta**: He'll probably say something like "these are all the same question — how does the system discover its own answers?" That's correct. Frame the cascade as the discovery mechanism and these decisions as the initial conditions.

4. **Lock decisions in real-time**: As he confirms each one, update PROJECT_NERVE_CENTER.md and the source file immediately. Don't batch.

---

*Generated 2026-03-07 by Claude (Opus 4.6) based on analysis of PROJECT_NERVE_CENTER.md, Open_Questions.md, chain_specification.md, M2 _meta.json, and operator guidance on Danilo's thinking style.*
