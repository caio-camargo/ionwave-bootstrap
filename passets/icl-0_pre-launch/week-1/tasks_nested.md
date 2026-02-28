# Week 1 Tasks — Pre-Launch Foundation (Nested Structure)

**Time Block**: ICL-0 Week 1 (Launch - 17 weeks)
**Phase**: Pre-Launch Foundation
**Status**: Template

---

## Task Structure Notes

**Nesting System**:
- **Level 0**: Role section (## CoS / Founder)
- **Level 1**: Parent task (### IMP-M2-001)
- **Level 2**: Subtask checklist (- [ ] File Certificate of Incorporation)
- **Level 3**: Sub-subtask details (  - Company name: IonWave, Inc.)

**Claude Flattening**:
When operator asks "What's next?", Claude can present:
- "Your next task is IMP-M2-001: File Delaware C-Corp. First step: Check name availability."

Backend maintains full nested detail for reference.

---

## CoS / Founder

### IMP-M2-001: File Delaware C-Corp Incorporation
**Source**: M2: Entity & Legal (M2-04-Entity-Formation-Guide)
**Owner**: CoS / Founder [TBD]
**Due**: Week 1, Day 3
**Dependencies**: None
**Status**: Not Started
**Estimated Time**: 2-3 hours

**Subtasks**:
- [ ] **1.1: Check name availability**
  - [ ] Search Delaware Division of Corporations database
  - [ ] Primary check: "IonWave, Inc."
  - [ ] Backup check: "IonWave Labs, Inc."
  - [ ] Backup check: "IonWave Health, Inc."
  - [ ] Document result: [Available / Taken]

- [ ] **1.2: Check trademark conflicts**
  - [ ] Search USPTO trademark database (tmsearch.uspto.gov)
  - [ ] Search term: "IonWave"
  - [ ] Review Class 5 (supplements) registrations
  - [ ] Document result: [Clear / Conflicts found]

- [ ] **1.3: Check domain availability**
  - [ ] Check ionwave.com availability
  - [ ] Check ionwave.co, .health, .io as backups
  - [ ] Do NOT purchase yet (wait for entity confirmation)
  - [ ] Document result: [Available / Price]

- [ ] **1.4: File Certificate of Incorporation**
  - [ ] Go to Delaware online filing system (icis.corp.delaware.gov)
  - [ ] Select: "File a New Business Entity"
  - [ ] Select entity type: "Corporation (General)"
  - [ ] Complete form fields:
    - [ ] Company name: [from 1.1]
    - [ ] Authorized shares: 10,000,000
    - [ ] Par value: $0.0001
    - [ ] Registered agent: [Northwest Registered Agent OR ZenBusiness]
    - [ ] Registered agent address: [provided by agent service]
    - [ ] Incorporator name: [Founder name]
    - [ ] Incorporator address: [Founder address]
  - [ ] Select filing speed:
    - [ ] Standard ($89, 2-3 business days) — RECOMMENDED for Week 1
    - [ ] 24-hour ($189)
    - [ ] Same-day ($279)
  - [ ] Pay filing fee
  - [ ] Receive confirmation email
  - [ ] Save filing receipt (PDF)

- [ ] **1.5: Receive filed Certificate**
  - [ ] Wait for filing confirmation (2-3 days for standard)
  - [ ] Download filed Certificate of Incorporation (PDF)
  - [ ] Note state file number: [___________]
  - [ ] Store in: `/passets/icl-0_pre-launch/legal-docs/certificate-of-incorporation.pdf`

**Cost**: $89-279 (filing) + $125-199/yr (registered agent) = $214-478 total

**Notes**:

**Reflection** (complete when done):
1. Name conflicts encountered: [None / Details]
2. Filing speed chosen: [Standard / 24hr / Same-day] because: _______
3. Learnings: _______

**Verified**: ☐ (matches M2 specification)

---

### IMP-M2-002: Obtain Federal EIN
**Source**: M2: Entity & Legal
**Owner**: CoS / Founder [TBD]
**Due**: Week 1, Day 3
**Dependencies**: IMP-M2-001 (C-Corp filed)
**Status**: Not Started
**Estimated Time**: 30 minutes

**Subtasks**:
- [ ] **2.1: Gather required information**
  - [ ] Company legal name: [from IMP-M2-001]
  - [ ] State file number: [from IMP-M2-001]
  - [ ] Business address: [registered agent address]
  - [ ] Responsible party name: [Founder name]
  - [ ] Responsible party SSN: [needed for application]

- [ ] **2.2: Apply online**
  - [ ] Go to IRS.gov
  - [ ] Navigate: Business > Employer ID Number (EIN) > Apply Online
  - [ ] Complete Form SS-4 online:
    - [ ] Legal structure: Corporation
    - [ ] Reason: Started new business
    - [ ] Business start date: [incorporation date]
    - [ ] Principal activity: Manufacturing (supplements)
    - [ ] Number of employees: 0 (initially)
  - [ ] Submit application
  - [ ] Receive EIN immediately (9-digit number)

- [ ] **2.3: Store EIN securely**
  - [ ] Record EIN: [__-_______]
  - [ ] Download EIN confirmation letter (PDF)
  - [ ] Store in: `/passets/icl-0_pre-launch/legal-docs/ein-confirmation.pdf`
  - [ ] Add to 1Password vault: "IonWave-Tax-Info"

**Cost**: $0

**Notes**: EIN needed for: bank account (Week 2), tax filings, hiring, payment processing

**Verified**: ☐

---

### IMP-M2-003: File BOI Report with FinCEN
**Source**: M2: Entity & Legal
**Owner**: CoS / Founder [TBD]
**Due**: Week 1, Day 5
**Dependencies**: IMP-M2-001, IMP-M2-002
**Status**: Not Started
**Estimated Time**: 45 minutes

**Subtasks**:
- [ ] **3.1: Gather beneficial owner information**
  - [ ] For each person with >25% ownership OR substantial control:
    - [ ] Full legal name
    - [ ] Date of birth
    - [ ] Residential address (not P.O. box)
    - [ ] ID document: Driver's license OR passport
    - [ ] ID document number
    - [ ] ID document issuing jurisdiction

- [ ] **3.2: File BOI report**
  - [ ] Go to FinCEN.gov
  - [ ] Navigate: Beneficial Ownership Information Reporting
  - [ ] Click "File a BOI Report"
  - [ ] Company information:
    - [ ] Legal name: [from IMP-M2-001]
    - [ ] EIN: [from IMP-M2-002]
    - [ ] Jurisdiction: Delaware
    - [ ] Formation date: [from IMP-M2-001]
  - [ ] Beneficial owner information:
    - [ ] Add each owner (from 3.1)
    - [ ] Upload ID document image for each
  - [ ] Review and submit
  - [ ] Receive confirmation number: [____________]

- [ ] **3.3: Store confirmation**
  - [ ] Download confirmation PDF
  - [ ] Store in: `/passets/icl-0_pre-launch/legal-docs/boi-confirmation.pdf`
  - [ ] Set calendar reminder: Update BOI if ownership changes

**Cost**: $0

**CRITICAL**: Deadline is 90 days from formation. Penalty: $500/day for non-filing.

**Verified**: ☐

---

### IMP-M5-001: Lock Final Formulation Specification
**Source**: M5: Formulation
**Owner**: CoS (coordinating with formulator)
**Due**: Week 1, Day 5
**Dependencies**: None (parallel to entity formation)
**Status**: Not Started
**Estimated Time**: 3-4 hours

**Subtasks**:
- [ ] **5.1: Confirm core electrolyte profile**
  - [ ] Sodium: 1,000 mg (natural chloride, ocean-sourced)
    - [ ] Verify source: Deep ocean water (>600m depth)
    - [ ] Confirm ionic form (not synthetic compound)
  - [ ] Potassium: 200 mg (natural chloride/sulfate blend)
    - [ ] Verify natural source
  - [ ] Magnesium: 60 mg (natural chloride/sulfate blend)
    - [ ] Verify natural source
  - [ ] Calcium: 2-5% DV (natural carbonate/chloride)
    - [ ] Confirm from ocean source (not added)
  - [ ] Chloride: ~1,540 mg (natural counter-ion)
  - [ ] Ratio check: Na:K:Mg = 17:3:1 ✓

- [ ] **5.2: Confirm trace mineral spectrum**
  - [ ] Verify 78-mineral ocean-sourced claim
  - [ ] Confirm source: Marine plasma extract
  - [ ] Request supplier documentation of mineral profile
  - [ ] Confirm pre-chelation by phytoplankton (marine biocenosis)

- [ ] **5.3: Request Certificate of Analysis (CoA)**
  - [ ] Request from supplier: Full mineral analysis
  - [ ] Request: Heavy metal testing results
    - [ ] Lead: <0.5 ppm (FDA limit)
    - [ ] Mercury: <0.1 ppm (FDA limit)
    - [ ] Cadmium: <0.5 ppm (FDA limit)
    - [ ] Arsenic: <0.2 ppm (FDA limit)
  - [ ] Request: Microbial testing (E. coli, Salmonella, yeast, mold)
  - [ ] Expected delivery: Week 2
  - [ ] Store in: `/passets/icl-0_pre-launch/product/coa/`

- [ ] **5.4: Verify processing standards**
  - [ ] Confirm microfiltration: 0.22µm
  - [ ] Confirm cold sterilization (preserves ionic state)
  - [ ] Confirm no synthetic additives
  - [ ] Confirm GMP (Good Manufacturing Practice) certification

- [ ] **5.5: Lock formulation document**
  - [ ] Create final formulation spec document
  - [ ] Include: Core profile + trace minerals + processing + CoA requirements
  - [ ] Founder sign-off: [________] Date: [____]
  - [ ] Store in: `/passets/icl-0_pre-launch/product/formulation-locked-v1.0.pdf`
  - [ ] **NO CHANGES AFTER THIS POINT** (delays supplier sourcing Week 2-4)

**Cost**: $0 (specification review)

**Departure to Imagination Passet**:
→ `/reference/m5-formulation-guide.md`
→ Section: "Core Electrolyte Profile"
→ Key: Na:K:Mg 17:3:1 targets keto/fasting populations

**Notes**:

**Reflection**:
1. Any formulation changes from initial concept? [Yes / No] Details: _______
2. Supplier confidence level: [High / Medium / Low]
3. CoA expected date: [____]

**Verified**: ☐ (matches M5 specification)

---

### IMP-M9-001: Set Up Shopify Store (Foundation)
**Source**: M9: Ecommerce Infrastructure
**Owner**: CoS / Founder [TBD]
**Due**: Week 1, Day 7
**Dependencies**: IMP-M2-001 (entity), IMP-M2-002 (EIN)
**Status**: Not Started
**Estimated Time**: 2-3 hours

**Subtasks**:
- [ ] **9.1: Create Shopify account**
  - [ ] Go to shopify.com
  - [ ] Click "Start free trial"
  - [ ] Email: [business email, not personal]
  - [ ] Store name: ionwave (will become ionwave.myshopify.com)
  - [ ] Set password (store in 1Password)
  - [ ] Complete account setup

- [ ] **9.2: Configure store settings**
  - [ ] Navigate: Settings > Store details
  - [ ] Legal business name: IonWave, Inc.
  - [ ] Store industry: Health & wellness > Vitamins & supplements
  - [ ] Store currency: USD
  - [ ] Store email: support@ionwave.com (set up in Week 2)
  - [ ] Time zone: [Select based on operations]
  - [ ] Unit system: Imperial
  - [ ] Weight unit: Ounces

- [ ] **9.3: Choose Shopify plan**
  - [ ] Start with: Shopify Basic ($39/mo)
  - [ ] Rationale: Sufficient for launch, upgrade to Shopify ($105/mo) at $5K/mo revenue
  - [ ] Note: 14-day free trial, then billing starts

- [ ] **9.4: Select and install theme**
  - [ ] Navigate: Online Store > Themes
  - [ ] Select: Dawn (free Shopify theme)
  - [ ] Rationale:
    - [ ] Free (no $180-350 theme cost)
    - [ ] Fast (performance-optimized)
    - [ ] Conversion-optimized layout
    - [ ] Mobile-first design
  - [ ] Click "Customize" to enter theme editor
  - [ ] Save as "Dawn - IonWave v1.0"

- [ ] **9.5: Install Google Analytics 4**
  - [ ] Navigate: Settings > Apps and sales channels
  - [ ] Search: "Google Analytics"
  - [ ] Install official Google channel app
  - [ ] Connect Google Analytics account
  - [ ] Create GA4 property: "IonWave Website"
  - [ ] Copy Measurement ID: G-___________
  - [ ] Verify tracking: Visit store, check Real-Time report in GA

- [ ] **9.6: Install Meta Pixel**
  - [ ] Navigate: Settings > Apps and sales channels
  - [ ] Search: "Facebook & Instagram"
  - [ ] Install official Meta channel app
  - [ ] Connect Meta Business Manager account
  - [ ] Create pixel: "IonWave Pixel"
  - [ ] Copy Pixel ID: ___________
  - [ ] Verify tracking: Use Meta Pixel Helper Chrome extension

- [ ] **9.7: Configure basic shipping (placeholder)**
  - [ ] Navigate: Settings > Shipping and delivery
  - [ ] Add shipping zone: United States
  - [ ] Set rate: Flat rate $5.95 (PLACEHOLDER - finalize in Week 4)
  - [ ] Note: Full shipping config (free over $X, 3PL integration) in Week 4

**Cost**: $39/mo (Shopify Basic)

**Notes**: This is FOUNDATION only. Full ecommerce (payment processing, checkout optimization, subscription app) = Week 3-4.

**Departure to Imagination Passet**:
→ `/reference/m9-ecommerce-guide.md`
→ Section: "Week 1 Setup Sequence"
→ Key: Don't over-build. Week 1 = account + theme + pixels ONLY.

**Reflection**:
1. Theme selection reasoning: _______
2. GA4 and Meta Pixel verified working: [Yes / No]
3. Any setup issues: _______

**Verified**: ☐ (matches M9 Week 1 setup)

---

## Formulator / Product Consultant

### IMP-M5-002: Provide Bioavailability Documentation
**Source**: M5: Formulation (M5-Scientific-Substantiation)
**Owner**: Formulator / Consultant [TBD]
**Due**: Week 1, Day 7
**Dependencies**: IMP-M5-001 (formulation locked)
**Status**: Not Started
**Estimated Time**: 4-6 hours (consultant work)

**Subtasks**:
- [ ] **5.2.1: Document ionic mineral bioavailability**
  - [ ] Claim: 66-90%+ absorption for ionic minerals
  - [ ] Provide: Peer-reviewed citations (3-5 studies)
  - [ ] Compare: vs synthetic mineral salts (30-50% absorption)
  - [ ] Format: Citation + key finding + confidence grade

- [ ] **5.2.2: Document ocean-sourced mineral efficacy**
  - [ ] Marine plasma research citations
  - [ ] Phytoplankton pre-chelation mechanism
  - [ ] Natural ionic form bioavailability
  - [ ] Format: Literature review (2-3 pages)

- [ ] **5.2.3: Flag substantiation gaps**
  - [ ] Identify: Claims lacking peer-reviewed support
  - [ ] Identify: Trace mineral absorption rates (likely gap)
  - [ ] Identify: Specific 78-mineral health benefits (likely gap)
  - [ ] Recommend: Conservative claim language for gaps

- [ ] **5.2.4: Create substantiation document**
  - [ ] Compile all citations into master document
  - [ ] Organize by claim type:
    - [ ] Structure/function claims (allowed)
    - [ ] Disease claims (NOT allowed without FDA approval)
    - [ ] Nutrient content claims (must match label)
  - [ ] Flag high-risk claims for FDA/FTC review
  - [ ] Format: PDF, ready for legal review (Week 2)
  - [ ] Store in: `/passets/icl-0_pre-launch/product/scientific-substantiation.pdf`

**Cost**: $0 (if included in formulation contract) or $500-1500 (consultant fee)

**Notes**: This document gates FDA compliance checklist (Week 2) and marketing claim approval.

**Verified**: ☐ (documentation meets M5 scientific substantiation standards)

---

## Designer / Brand Consultant

### IMP-M8-001: Kickoff Brand Identity Project
**Source**: M8: Brand Identity (M8-Project-Brief)
**Owner**: Designer / Brand Consultant [TBD]
**Due**: Week 1, Day 7 (kickoff only)
**Dependencies**: IMP-M5-001 (formulation - needed for positioning)
**Status**: Not Started
**Estimated Time**: 2 hours (kickoff meeting)

**Subtasks**:
- [ ] **8.1: Schedule kickoff meeting**
  - [ ] Date: Week 1, Day 5-7
  - [ ] Duration: 90-120 minutes
  - [ ] Attendees: Founder(s) + Designer
  - [ ] Agenda:
    - [ ] Product positioning (15 min)
    - [ ] Target customer review (15 min)
    - [ ] Brand archetype alignment (30 min)
    - [ ] Competitive brand analysis (20 min)
    - [ ] Timeline and deliverables (10 min)
    - [ ] Q&A (10 min)

- [ ] **8.2: Review formulation positioning**
  - [ ] Core differentiator: 78 ocean-sourced minerals (vs 3-4 synthetic)
  - [ ] Secondary: Natural ionic forms, pre-chelated by phytoplankton
  - [ ] Tertiary: Science-backed, peer-review quality standards
  - [ ] Market positioning: Premium ($40-50 vs $20-30 competitors)

- [ ] **8.3: Review target customer (M27 ICP)**
  - [ ] Primary: Keto/low-carb dieters (electrolyte-deficient)
  - [ ] Secondary: Fasting practitioners (need electrolyte replacement)
  - [ ] Tertiary: Performance athletes (optimal hydration)
  - [ ] Psychographics: Health-conscious, science-curious, skeptical of supplements

- [ ] **8.4: Align on brand archetype**
  - [ ] Discuss: Sage (knowledge-driven) vs Challenger (disrupt industry)
  - [ ] Founder preference: [Sage / Challenger / Hybrid]
  - [ ] Tone: [Educational-authoritative / Bold-contrarian / Scientific-trustworthy]
  - [ ] Document decision: _______

- [ ] **8.5: Review competitive brand landscape**
  - [ ] LMNT: Bold, challenger, orange/black, founder-driven
  - [ ] Liquid I.V.: Mainstream, colorful, hydration-focused
  - [ ] Ultima: Natural, clean, muted tones
  - [ ] IonWave positioning: [Differentiation strategy]

- [ ] **8.6: Set delivery timeline**
  - [ ] Week 2: Logo concepts (3 options) for review
  - [ ] Week 3: Final logo + color palette + typography system
  - [ ] Week 4: Brand guidelines PDF (10-15 pages)
  - [ ] Deliverable format: Figma (editable) + PDF export
  - [ ] File formats: SVG (logo), PNG (social), EPS (print)

- [ ] **8.7: Clarify brand guidelines scope**
  - [ ] Logo (primary + variations)
  - [ ] Color palette (primary + secondary + neutrals)
  - [ ] Typography (headings + body + web fonts)
  - [ ] Photography style (examples/references)
  - [ ] Voice and tone guidelines
  - [ ] Do's and don'ts
  - [ ] NOT INCLUDED: Package design (separate project, Week 6-8)

**Cost**: $0 (kickoff is part of brand package)

**Notes**: Brand delivery NOT Week 1. This is kickoff only. Design work happens Week 2-4.

**Reflection**:
1. Brand archetype chosen: _______
2. Key differentiation from LMNT: _______
3. Founder excitement level: [High / Medium / Low]

**Verified**: ☐

---

## Lawyer (External)

### IMP-M2-006: Prepare Corporate Governance Documents
**Source**: M2: Entity & Legal (M2-04-Entity-Formation-Guide)
**Owner**: Lawyer (external) [TBD]
**Due**: Week 1, Day 5
**Dependencies**: IMP-M2-001 (C-Corp filed)
**Status**: Not Started
**Estimated Time**: 6-10 hours (legal work)

**Subtasks**:
- [ ] **2.6.1: Draft Bylaws**
  - [ ] Standard Delaware C-Corp bylaws template
  - [ ] Customize: Board size (1-3 directors initially)
  - [ ] Customize: Officer titles (President/CEO, Secretary, Treasurer)
  - [ ] Customize: Quorum requirements
  - [ ] Customize: Shareholder meeting rules
  - [ ] Review with founder(s)

- [ ] **2.6.2: Draft Restricted Stock Purchase Agreements (RSPAs)**
  - [ ] One RSPA per founder
  - [ ] Include: Number of shares, purchase price ($0.0001/share)
  - [ ] Include: Vesting schedule (4-year monthly, 1-year cliff)
  - [ ] Include: Repurchase right on unvested shares
  - [ ] Include: IP assignment provision
  - [ ] Include: At-will employment acknowledgment
  - [ ] Review with each founder

- [ ] **2.6.3: Draft Board Consent (organizational meeting resolutions)**
  - [ ] Resolution: Adopt Bylaws
  - [ ] Resolution: Elect officers
  - [ ] Resolution: Authorize stock issuance (10M shares)
  - [ ] Resolution: Adopt ESOP (stock option plan, 1.5M shares reserved = 15% fully-diluted)
  - [ ] Resolution: Select fiscal year (calendar year)
  - [ ] Resolution: Authorize bank account
  - [ ] Resolution: Approve RSPAs
  - [ ] Resolution: Ratify pre-incorporation actions
  - [ ] Format for signature (DocuSign or wet signature)

- [ ] **2.6.4: Draft 83(b) election forms**
  - [ ] One form per founder
  - [ ] IRS format (exact template, no deviations)
  - [ ] Pre-fill: Founder name, # shares, purchase price, FMV
  - [ ] Instructions: File within 30 days via certified mail
  - [ ] Include: Cover letter, return receipt form

- [ ] **2.6.5: Draft IP assignment agreements**
  - [ ] Assign all founder IP to company
  - [ ] Include: Past work-product (if relevant to business)
  - [ ] Include: Future work-product
  - [ ] Carve-outs: Personal projects unrelated to business
  - [ ] One agreement per founder

- [ ] **2.6.6: Prepare stock certificate template**
  - [ ] Option A: Paper certificates (physical stock certificate design)
  - [ ] Option B: Uncertificated shares (no physical certificate, electronic only)
  - [ ] Recommendation: Uncertificated (simpler, modern practice)
  - [ ] If certificated: Design template with company name, seal, signature lines

- [ ] **2.6.7: Deliver incorporation package**
  - [ ] All documents compiled in single folder
  - [ ] Execution checklist (what to sign, when, how)
  - [ ] Filing instructions (83(b) certified mail)
  - [ ] Store in: `/passets/icl-0_pre-launch/legal-docs/incorporation-package/`
  - [ ] Schedule: Review call with founder(s) to explain documents

**Cost**: $1,500-3,000 (startup law firm incorporation package)

**Alternative**: Clerky ($2,500 all-in for incorporation + docs, no lawyer review)

**Notes**: If using Clerky or similar, lawyer review may not be needed. DIY = higher risk of errors.

**Verified**: ☐

---

## Week 1 Summary

**Total Tasks**: 10 parent tasks, 65 subtasks
**Roles**: 4 (CoS/Founder, Formulator, Designer, Lawyer)
**Critical Path**: IMP-M2-001 → 002 → 003 → 004 → 005 (entity formation chain)
**Parallel Tracks**: Formulation (M5), Brand Kickoff (M8), Shopify (M9)

**Completion Checklist** (High-Level):
- [ ] C-Corp formed in Delaware
- [ ] EIN obtained from IRS
- [ ] BOI report filed with FinCEN
- [ ] Organizational meeting held (board resolutions signed)
- [ ] Founder stock issued (RSPAs executed)
- [ ] 83(b) elections prepared (DEADLINE: Day 35!)
- [ ] Formulation locked and documented
- [ ] Brand project kicked off (design starts Week 2)
- [ ] Shopify account created and configured

**Key Risks**:
1. **🚨 83(b) DEADLINE**: 30 days from stock purchase. Missing = $10K-50K+ tax bill. SET CALENDAR ALERT NOW.
2. **Formulation lock**: Changes after Week 1 delay supplier (Week 2-4) and production (Week 6-8).
3. **Entity name conflicts**: Have 2-3 backup names ready before filing.
4. **BOI filing**: New requirement (2024+). $500/day penalty for non-filing. Don't skip.

**Time Investment**:
- CoS/Founder: 20-30 hours
- Formulator: 4-6 hours
- Designer: 2 hours (kickoff)
- Lawyer: 6-10 hours

**Budget**:
- Entity formation: $214-478
- Legal docs: $1,500-3,000 (or $0 DIY)
- Brand: $0 (deposit paid Week 0, work starts Week 2)
- Formulator: $0 (included in contract)
- Shopify: $39
- Misc: $50
- **TOTAL**: $1,803-3,567 (or $303-567 if DIY legal)

**Week 2 Preview**:
- Bank account opening (requires all Week 1 entity docs)
- Supplier outreach (M6) - needs formulation from Week 1
- Logo concepts review (M8) - designer delivers 3 options
- FDA compliance checklist (M7) - needs substantiation from Week 1

**Integration Check** (per Integration Principles):
- ✅ Embed Action: Subtasks have specific steps, not just goals
- ✅ Self-Awareness: Completion checklist shows overall progress
- ✅ Adjacent Reflection: Reflection prompts on each task
- ✅ Accumulation: Notes field creates thinking record
- ✅ Structured Departures: Bridge document references for deep dives
- ✅ Isomorphic Structure: Week-by-week matches operational cadence
