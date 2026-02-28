# TUP M9: Ecommerce Infra

**Status:** unknown | **Quality:** N/A/10 | **Version:** N/A
**Cluster:** BCL-6 (N/A)

---

## 📋 Overview


---

## 📁 Content Files


---

## 🔧 Structured Data

_JSON files converted to human-readable format_

_No JSON files in this TUP._

---

## 📝 Narrative Content

### 📄 dialogue_summary.md

# M9 Ecommerce Infrastructure — Dialogue Summary

## Metadata
- **TUP**: M9 (Ecommerce Infra)
- **Cluster**: BCL-6 (Operations & Infrastructure)
- **Date**: 2026-02-09
- **Rounds**: 6 (saturation at Round 6)
- **Personas**: 3

## Personas

| Persona | Expertise | Bias/Lens |
|---------|-----------|-----------|
| Technical Shopify Architect | 8 years building D2C stores, performance obsessed | Speed, code quality, technical debt avoidance |
| Bootstrapped D2C Founder | Launched 3 supplement brands, budget-constrained | Pragmatism, speed to launch, ROI focus |
| Ecommerce Security Consultant | Former CISO, advises startups | Practical security, realistic threat model |

## Upgrades Applied (14)

| # | Upgrade | Target File |
|---|---------|-------------|
| U1 | Theme performance budget (8 apps, 500KB JS, 3 external scripts) | tech_stack_and_tools.md |
| U2 | Week 1 Setup Sequence (Day 1-7 strict order) | store_setup_and_launch.md |
| U3 | Ad account hijacking prevention | operations_governance.md |
| U4 | Consent management (Consent Mode v2, CCPA) | tracking_and_attribution.md |
| U5 | Monthly Tool ROI Review | tech_stack_and_tools.md |
| U6 | Theme backup protocol (before every app install) | operations_governance.md |
| U7 | Shopify-specific speed killers (Liquid render, app residue) | store_setup_and_launch.md |
| U8 | Subscription UX pattern (toggle > dropdown, 15-20% lift) | store_setup_and_launch.md |
| U9 | Collaborator account audit | operations_governance.md |
| U10 | "Do Not Install" app list | tech_stack_and_tools.md |
| U11 | Phase-gated governance (essentials only pre-launch) | operations_governance.md |
| U12 | Meta daily spend cap at 2x normal budget | tracking_and_attribution.md |
| U13 | Checkout extensibility note (Extensions > checkout.liquid) | store_setup_and_launch.md |
| U14 | UTM builder template (Google Sheet) | tracking_and_attribution.md |

## Unresolved Debates
None — all personas reached consensus.

## Key Themes
1. **Phase-gate everything**: Don't build enterprise infrastructure for pre-launch startup
2. **Performance has a budget**: Hard limits on apps, JS, external scripts
3. **Security is practical**: Focus on actual D2C threats (phishing, ad hijacking), not theoretical
4. **Launch speed > perfection**: Week 1 setup sequence forces action over preparation
5. **Subscription UX is revenue**: Toggle pattern directly impacts HYP-003 (40% subscription rate)


---

### 📄 operations_governance.md

# M9 — Operations Governance

> A disorganized business looks unprofessional, wastes time, and creates risk. Structure is free — use it.

## Source

Danilo tabs: 291 (Security Checklist), 293 (Folder Structure Map), 294 (Asset Naming Convention)

---

## Security Checklist

### Account Security (Non-Negotiable)

| # | Task | Priority | Status |
|---|------|----------|--------|
| 1 | Install password manager (1Password or Bitwarden) | P0 | ☐ |
| 2 | Unique password for EVERY account — no exceptions | P0 | ☐ |
| 3 | Enable 2FA on all critical accounts (see list below) | P0 | ☐ |
| 4 | Store recovery codes in separate secure location | P0 | ☐ |
| 5 | Review and remove unused account access quarterly | P1 | ☐ |

### 2FA Required Accounts

These accounts MUST have 2FA enabled before launch:

| Account | Why It's Critical | 2FA Method |
|---------|------------------|------------|
| **Business email (Google Workspace)** | Gateway to ALL account resets | Authenticator app (NOT SMS) |
| **Shopify** | Store access, customer data, revenue | Authenticator app |
| **Bank accounts** | Money | Bank's native 2FA |
| **Meta Business Manager** | Ad spend, pixel data | Authenticator app |
| **Google Ads** (if applicable) | Ad spend | Google's native 2FA |
| **Domain registrar** | Domain = business identity | Authenticator app |
| **Stripe** (if separate from Shopify) | Payment processing | Authenticator app |
| **Recharge/Skio** | Subscription customer data | If available |

**2FA hierarchy**: Hardware key (YubiKey) > Authenticator app (Google Authenticator, Authy) > SMS. Never use SMS for critical accounts — SIM swapping is real.

### Data Security

| # | Rule | Rationale |
|---|------|-----------|
| 1 | Customer data stored ONLY in secure systems (Shopify, Klaviyo, Recharge) | These have SOC 2 compliance. Spreadsheets don't |
| 2 | NO customer data in spreadsheets or local files | One laptop theft = data breach |
| 3 | Credit card data NEVER stored — Shopify Payments/Stripe handles this | PCI compliance is their problem, not yours |
| 4 | Regular backups of critical data (weekly export from Shopify) | Shopify isn't going down, but export your customer/order data monthly |
| 5 | Encryption enabled where possible (FileVault on Mac, BitLocker on Windows) | Full-disk encryption on all devices with business data |

### Access Control

| # | Rule | Implementation |
|---|------|---------------|
| 1 | Principle of least privilege | Contractors get access ONLY to tools they need. Nothing more |
| 2 | Separate admin accounts from daily-use | Admin email for business-critical, personal email for daily tools |
| 3 | Remove access IMMEDIATELY when someone leaves | Within 24 hours. No exceptions. Change shared passwords |
| 4 | Document who has access to what | Use credential register in tech_stack_and_tools.md |
| 5 | Review access list quarterly | Calendar reminder: Jan 1, Apr 1, Jul 1, Oct 1 |

### Incident Response Protocol

If you suspect a breach or unauthorized access:

| Step | Action | Timeline |
|------|--------|----------|
| **1. CONTAIN** | Change passwords on ALL affected accounts. Revoke all third-party access. Enable lockdown mode | Immediately (within 1 hour) |
| **2. ASSESS** | What was accessed? Customer data? Financial data? Payment info? How did they get in? | Within 24 hours |
| **3. NOTIFY** | Legal counsel first. Then affected customers if PII was exposed (required by CCPA/GDPR). Contact Shopify support | Within 72 hours (GDPR requirement) |
| **4. FIX** | Close the vulnerability. Update all passwords. Add 2FA where missing. Review all access | Within 1 week |
| **5. DOCUMENT** | Record what happened, how you responded, what changed. Add to security audit trail | Within 2 weeks |

**Reality for solo founders**: You probably won't have a sophisticated breach. The most likely scenarios are: (1) reused password gets compromised in a data breach, (2) phishing email tricks you into giving up credentials, (3) a contractor you gave access to goes rogue. 2FA + unique passwords prevents 90% of these.

### Ad Account Hijacking Prevention (U3)

The **#1 actual threat for D2C brands** is Meta Business Manager hijacking. Attackers send phishing emails that look identical to "Your ad was rejected" or "Account verification required." If your ad account gets hijacked, they drain your credit card running crypto/scam ads — often thousands of dollars in hours.

**Prevention rules**:
1. **NEVER click links in Meta support emails** — Always navigate directly to business.facebook.com
2. **Set a daily ad spend cap** at 2x your normal budget (see tracking_and_attribution.md U12) — limits damage if hijacked
3. **Set an account-level spending limit** — hard cap that requires manual reset
4. **Enable login alerts** for Meta Business Manager — you get notified of any new login
5. **Use a separate browser profile** for ad accounts — prevents cookie/session theft from casual browsing
6. **Never grant admin access** to Meta BM unless absolutely necessary — use partial permissions

**If hijacked**:
1. Immediately pause ALL campaigns from Ads Manager (if you still have access)
2. Contact Meta Business Support (priority: "My account was compromised")
3. Change password and revoke all sessions
4. Contact your bank to dispute unauthorized charges
5. Review and remove any unknown admin users

### Theme Backup Protocol (U6)

**Before installing ANY new Shopify app**, export your current theme:

1. Go to Shopify Admin → Online Store → Themes
2. Click "..." on your live theme → "Download theme file"
3. Save as: `Theme_[ThemeName]_v[#]_[YYYYMMDD].zip` in `04_Operations/` on Drive
4. THEN install the app
5. If the app breaks your theme or kills speed, you can restore the backup instantly

**Why this matters**: Apps can corrupt themes. A clean backup saves days of debugging. Takes 30 seconds. No excuse not to do it.

### Collaborator Account Audit (U9)

Developers and agencies often get added as **Collaborator accounts** (separate from Staff accounts) and these persist indefinitely — even years after a project ends.

**Quarterly audit**:
1. Go to Shopify Admin → Settings → Users and Permissions
2. Check **Staff** section — remove anyone who shouldn't have access
3. Check **Collaborator** section — this is where forgotten access hides
4. Remove any collaborator who is not actively working on your store
5. Document any remaining collaborators in the credential register with their access level and review date

---

## Folder Structure Map

### Google Drive Organization

```
IonWave/
├── 00_Strategy/
│   ├── Ops Model (master spreadsheet/IonWave Bootstrap)
│   ├── Business Plan
│   └── Investor Materials
│
├── 01_Brand/
│   ├── Brand_Book_v[#].pdf
│   ├── Logo_Files/
│   │   ├── Img_Logo_Primary_v1.svg
│   │   ├── Img_Logo_White_v1.svg
│   │   └── Img_Logo_Icon_v1.svg
│   ├── Color_Palette/
│   └── Typography/
│
├── 02_Creative/
│   ├── Ads/
│   │   ├── Static/        (Ad_Static_Hook[#]_[Angle]_v[#].png)
│   │   ├── Video/         (Vid_[Type]_[Length]_v[#].mp4)
│   │   └── Archive/       (Dated subfolders: YYYY-MM/)
│   ├── Landing_Pages/     (LP_[Name]_[Section]_v[#].fig)
│   ├── Email/             (Email_[Flow]_[#]_v[#].html)
│   └── Photography/       (Img_[Type]_[Descriptor]_v[#].jpg)
│
├── 03_Marketing/
│   ├── Campaign_Reports/  (Doc_CampaignReport_YYYYMMDD.pdf)
│   ├── Competitor_Research/
│   └── Swipe_File/        (Inspiration, competitor screenshots)
│
├── 04_Operations/
│   ├── Suppliers/         (Doc_SupplierQuote_YYYYMMDD.pdf)
│   ├── 3PL/               (Contracts, SOPs, SLAs)
│   ├── Inventory/         (Inventory counts, reorder triggers)
│   └── Support/           (Templates, macros, escalation docs)
│
├── 05_Finance/
│   ├── Invoices/          (Doc_Invoice_[Vendor]_YYYYMMDD.pdf)
│   ├── Reports/           (Monthly P&L, cash flow)
│   └── Projections/       (Financial models, scenarios)
│
├── 06_Legal/
│   ├── Contracts/         (Doc_Contract_[Party]_YYYYMMDD.pdf)
│   ├── Compliance/        (FDA, FTC, supplement regulations)
│   └── IP/                (Trademarks, patents if applicable)
│
├── 07_Evidence/
│   ├── Screenshots/       (SS_[What]_YYYYMMDD.png)
│   ├── Screen_Recordings/ (SR_[What]_YYYYMMDD.mp4)
│   └── Audit_Trail/       (Decision logs, change records)
│
└── 08_Archive/
    └── Old_Versions/      (Dated subfolders: YYYY-MM/)
```

### Folder Rules

1. **9 top-level folders maximum** — If you need a new category, it probably fits in an existing one
2. **No files in root** — Everything goes in a subfolder
3. **Archive, don't delete** — Move old versions to 08_Archive with date
4. **Consistent naming** — Follow Asset Naming Convention below
5. **Weekly cleanup** — 5 minutes every Friday: file anything in Downloads or Desktop

---

## Asset Naming Convention

### General Format

```
[Type]_[Category]_[Descriptor]_[Version]_[Date]
```

### By Asset Type

| Type | Format | Example |
|------|--------|---------|
| **Ads** | `Ad_[Format]_[Hook#]_[Angle]_v[#]` | `Ad_Static_Hook3_Minerals_v2` |
| **Videos** | `Vid_[Type]_[Length]_v[#]` | `Vid_VSL_60s_v1` |
| **Emails** | `Email_[Flow]_[#]_v[#]` | `Email_Welcome_01_v3` |
| **Landing Pages** | `LP_[Name]_[Section]_v[#]` | `LP_Main_Hero_v2` |
| **Images** | `Img_[Type]_[Descriptor]_v[#]` | `Img_Product_Lifestyle_v1` |
| **Documents** | `Doc_[Type]_[Date]` | `Doc_SupplierQuote_20260115` |
| **Screenshots** | `SS_[What]_[Date]` | `SS_AdPerformance_20260115` |
| **Screen Recordings** | `SR_[What]_[Date]` | `SR_CheckoutFlow_20260208` |

### Naming Rules

1. **No spaces** — Use underscores: `Ad_Static_Hook3` not `Ad Static Hook3`
2. **No special characters** except underscore `_` and hyphen `-`
3. **Always include version number** — `v1`, `v2`, etc. Even first version is `v1`
4. **Date format: YYYYMMDD** — `20260115` not `01-15-26` or `Jan 15`
5. **Keep names under 50 characters** — Long enough to be descriptive, short enough to read
6. **Be descriptive but concise** — `Ad_Static_Hook3_Minerals_v2` tells you everything
7. **Lowercase for consistency** — Exception: proper nouns in descriptors

### Version Control Rules

- **v1, v2, v3** — Sequential, never skip numbers
- **Old versions**: Move to 08_Archive or subfolder `_Archive/`
- **Working files**: Prefix with `WIP_` (e.g., `WIP_Ad_Static_Hook4_v1`)
- **Final/approved files**: No prefix (clean name = approved)
- **Never use "final"** — `Ad_Hero_FINAL_v2_FINAL_REAL.png` is a meme for a reason. Use version numbers

### Campaign Naming Convention (Ads)

For ad platform campaigns, maintain consistent naming:

```
[Platform]_[Objective]_[Audience]_[Creative]_[Date]

Meta_Prospecting_Interest-Health_Hook3-Static_202602
Meta_Retargeting_ViewContent-7d_UGC-Testimonial_202602
Google_Brand_Branded-Terms_Text_202602
TikTok_Prospecting_Lookalike-1pct_Creator-Jessica_202602
```

This naming convention ensures:
- You can filter by platform, objective, or audience in analytics
- UTM parameters stay consistent (utm_campaign matches campaign name)
- Reporting is clear without needing to open the ad platform

---

## Phase-Gated Governance (U11)

Not everything in this document applies from Day 1. Over-organizing before launch is a form of procrastination.

### Month 0-1 (Pre-Launch + Launch): Essentials ONLY

- ✅ Password manager installed + 2FA on all critical accounts
- ✅ Folder structure created in Drive
- ✅ Naming convention understood and applied
- ✅ Theme backup taken before app installs
- ✅ Ad spend caps set

### Month 2-3: Add Operational Cadence

- ✅ Monthly Tool ROI Review starts (tech_stack_and_tools.md)
- ✅ Weekly operational hygiene routine
- ✅ Monthly security/tracking checks
- ✅ Credential register fully populated

### Month 3+: Unlock Full Governance

- ✅ Quarterly security audits
- ✅ Contractor onboarding/offboarding checklists
- ✅ Full operational hygiene calendar
- ✅ Collaborator account audits

**The rule**: If you don't have revenue yet, you don't need quarterly security audits. Launch first, organize second. But password manager + 2FA + ad spend caps are NON-NEGOTIABLE from Day 0.

---

## Operational Hygiene Calendar

> **Note**: Daily routine starts at launch. Weekly starts Month 1. Monthly starts Month 2. Quarterly starts Month 3.

### Daily (5 min)

- [ ] Check MVD metrics (see M30 Daily Pulse)
- [ ] Monitor customer support inbox
- [ ] Review any ad platform alerts/flags

### Weekly (30 min — Friday)

- [ ] File any loose documents using naming convention
- [ ] Review and respond to all customer reviews
- [ ] Check page speed on homepage and PDP
- [ ] Clear browser cache and downloads folder
- [ ] Back up any critical local files to Drive

### Monthly (1 hour — First Monday) — *Starts Month 2*

- [ ] Export Shopify customer and order data backup
- [ ] Review installed apps — uninstall unused
- [ ] Check all tracking pixels are firing correctly
- [ ] Review access permissions (who has access to what)
- [ ] Archive old creative assets to 08_Archive
- [ ] Update credential register if any passwords changed
- [ ] Tool ROI Review — justify every paid tool in one sentence (U5)

### Quarterly (2 hours) — *Starts Month 3*

- [ ] Full security audit: all accounts have 2FA, passwords rotated for shared accounts
- [ ] Access review: remove anyone who shouldn't have access
- [ ] Collaborator account audit: check Shopify Settings → Users → Collaborator section (U9)
- [ ] App audit: justify every installed Shopify app
- [ ] Folder cleanup: archive old projects, rename inconsistent files
- [ ] Review folder structure — add new subfolders if needed (but try not to)
- [ ] Speed audit: full PageSpeed Insights on all key pages

---

## Contractor/Team Onboarding Checklist

When bringing someone new onto the project:

| # | Task | Notes |
|---|------|-------|
| 1 | Create their access list (which tools, what permission level) | Document in credential register |
| 2 | Grant access to approved tools ONLY | Least privilege — they can request more |
| 3 | Share folder structure map | They need to know where things go |
| 4 | Share asset naming convention | Non-negotiable. Renamed files = wasted time |
| 5 | Share UTM convention (if marketing) | Inconsistent UTMs break attribution |
| 6 | Set up their 2FA on all granted accounts | Verify before they start working |
| 7 | Brief on security policies | Especially: no customer data in spreadsheets |
| 8 | Calendar their access review date | 90-day review or end of contract, whichever is sooner |

### Offboarding Checklist

| # | Task | Timeline |
|---|------|----------|
| 1 | Revoke access to ALL tools | Within 24 hours |
| 2 | Change shared passwords they had access to | Within 24 hours |
| 3 | Transfer ownership of assets they created | Before access revoked |
| 4 | Update credential register | Same day |
| 5 | Verify no personal accounts linked to business tools | Within 48 hours |
| 6 | Archive their work folder | Within 1 week |

---

## Recovery Protocol

If operational governance lapses (you missed weeks of filing, naming is inconsistent, etc.):

### Priority 1: Security (Do This First)
1. Verify 2FA on all critical accounts (15 min)
2. Check for any unauthorized access (15 min)
3. Update any passwords that are > 6 months old (30 min)

### Priority 2: Tracking (Do This Second)
1. Verify all pixels are firing (15 min)
2. Run Meta Pixel Helper on key pages (10 min)
3. Compare Shopify orders vs platform-reported conversions (10 min)

### Priority 3: Organization (Do This When Possible)
1. File unfiled documents using naming convention (30 min)
2. Rename any incorrectly named files (30 min)
3. Archive old versions (15 min)
4. Update credential register (15 min)

**Graceful degradation** (per M30): Security and tracking are NON-NEGOTIABLE. Organization can always be recovered. A messy folder structure doesn't kill a business — a security breach does.


---

### 📄 opkit_ecommerce_infrastructure.md

# OpKit: Ecommerce Infrastructure Setup (OK-M9-001)

> A complete playbook for setting up a D2C ecommerce store from zero to launch on Shopify.

## Metadata

- **OpKit ID**: OK-M9-001
- **TUP**: M9 (Ecommerce Infra)
- **Type**: Production
- **Version**: 1.0.0
- **Quality Grade**: 8.5/10
- **Created**: 2026-02-09

---

## Instructions (14 Steps)

### Step 1: Define Your Platform Strategy
Choose your ecommerce platform. For D2C consumable brands at $0-$50K MRR, Shopify is the default recommendation (operational simplicity, native payments, best app ecosystem). Only consider alternatives if you have specific requirements Shopify can't meet.

### Step 2: Set Your Performance Budget
Before touching anything, establish hard limits: maximum 8 apps, 500KB JavaScript budget, 3 external scripts, 2 custom fonts. Write these down. Enforce them ruthlessly.

### Step 3: Select Your Core Stack
Choose the non-negotiable tools for launch (see `tech_stack_and_tools.md`). For subscription D2C: Shopify + subscription app + email platform + reviews + analytics + ad pixel + payment processor. Budget: $50-130/mo.

### Step 4: Follow the Week 1 Setup Sequence
Use the Day 1-7 strict priority order (see `store_setup_and_launch.md`). Do not spend weeks on theme customization before products are uploaded. Speed to launch > perfection.

### Step 5: Set Up Tracking Architecture
Implement pixel + server-side (hybrid) tracking from Day 1. Meta Pixel + CAPI, GA4, subscription events. Establish MER as your primary efficiency metric, not platform ROAS (see `tracking_and_attribution.md`).

### Step 6: Configure Subscription-First UX
If your brand has a subscription model, make it the default purchase option. Use toggle (not dropdown), show subscription price first, one-time as secondary. This directly impacts subscription conversion rate.

### Step 7: Implement Security Essentials
Password manager, 2FA on all critical accounts, ad spend caps. These are Day 0 requirements, not "nice to haves." See `operations_governance.md`.

### Step 8: Complete Pre-Launch Testing
Run the full testing protocol: test orders (desktop + mobile), email flows, subscription orders, page speed check (≥70 on PageSpeed Insights), tracking verification. All P0 tests must pass before launch.

### Step 9: Launch
Follow the launch sequence: remove password, verify organic checkout first, turn on paid traffic Day 2-3. Do NOT run ads before verifying checkout works.

### Step 10: Establish Operational Cadence
Daily: 5-min MVD check + support inbox. Weekly: file cleanup + speed check. Monthly (starting Month 2): Tool ROI review + app audit + tracking check.

### Step 11: Phase-Gate Your Tool Growth
Don't add Growth Stack tools until unlock triggers are met (see `tech_stack_and_tools.md`). Each new tool must prove ROI before the next gets added.

### Step 12: Monitor Consent & Compliance
Implement cookie consent banner. Configure Consent Mode v2 for GA4. Ensure CCPA compliance if targeting US audiences.

### Step 13: Grade Your Setup
Use the rubric below to assess your implementation quality.

### Step 14: Iterate
Monthly speed audits, quarterly security reviews, ongoing tool ROI assessment. Remove tools that don't earn their place.

---

## Grading Rubric

| Grade | Score | Criteria |
|-------|-------|----------|
| **A** | 9-10 | All Core Stack tools configured with server-side tracking. Performance budget enforced. Subscription-first UX. Full security setup. Page speed ≥ 80. All pre-launch tests pass. Consent management active. |
| **B** | 7-8 | Core Stack complete. Browser pixel tracking (CAPI optional). Subscription configured but UX not optimized. Security essentials done. Page speed 60-79. Most tests pass. |
| **C** | 5-6 | Store functional but gaps: missing subscription setup, no server-side tracking, security incomplete, page speed 40-59, some tests skipped. |
| **D** | 3-4 | Store live but major issues: no tracking verification, no 2FA, too many apps (>12), page speed <40, no test orders run. |
| **F** | 0-2 | Store not functional or critical security gaps (no password manager, no 2FA, shared credentials). |

---

## Scaffold (4 Files)

Any D2C brand can start from these templates:

1. **`tech_stack_and_tools.md`** — Phase-gated tool selection (Core → Growth → Scale) with performance budget, cost tracking, credential management, "Do Not Install" list
2. **`store_setup_and_launch.md`** — Week 1 setup sequence, 8-section checklist, subscription UX pattern, page speed targets (CWV 2026), launch sequence
3. **`tracking_and_attribution.md`** — MER as north star, pixel + CAPI setup, UTM taxonomy, attribution model comparison, consent management, ad spend safety
4. **`operations_governance.md`** — Security checklist, folder structure, naming conventions, phase-gated governance, operational cadence

---

## IonWave Graded Example

**Trade**: IonWave Trade #84
**Quality**: 8.5/10
**Key Decisions**:
- Shopify Basic at launch ($29/mo), upgrade at ~$10K MRR
- Recharge/Skio for subscriptions (core to model)
- MER as primary metric (not ROAS) — aligned with M30
- 8-app maximum at launch, 500KB JS budget
- Week 1 setup sequence (7 days to launch)
- Subscription-first UX (toggle, not dropdown)
- Consent Mode v2 from Day 1
- Meta daily spend cap at 2x normal budget

---

## Adaptation Guide

### For Non-Subscription D2C Brands
- Remove subscription setup section (Step 6)
- Core Stack cost drops to ~$70/mo (no Recharge/Skio)
- Subscription UX pattern doesn't apply
- Focus on AOV optimization (bundles, upsells) instead

### For Multi-SKU Brands (10+ Products)
- Collection page optimization becomes critical (pagination, filtering)
- Product tagging system needs more structure
- Inventory management tool moves to Core Stack (not Growth)
- Speed budget is harder to maintain — stricter image optimization required

### For International D2C
- Shopify Markets for multi-currency/multi-language
- Consent Mode v2 is mandatory (not optional)
- Shipping configuration is more complex
- Tax settings need country-specific rules

### For Marketplace-First Brands
- Shopify may not be Day 1 platform (Amazon/Etsy first)
- Tracking setup changes significantly (marketplace pixels, not your own)
- Security focus shifts to marketplace account protection
- Folder structure and naming still apply universally

---

## Universal Principles

1. **Launch speed > perfection** — A live store generating data beats a perfect store generating nothing
2. **Performance has a budget** — Hard limits on apps, JavaScript, fonts. Enforce ruthlessly
3. **MER is truth** — Platform ROAS lies post-iOS 14.5. Use MER for business decisions
4. **Phase-gate everything** — Don't build $50K MRR infrastructure for a pre-launch startup
5. **Security is Day 0** — Password manager + 2FA + ad spend caps before anything else
6. **Every tool must earn its place** — Monthly ROI review. Can't articulate value in one sentence? Cancel
7. **Subscription-first UX** — If you have subscriptions, the entire purchase experience revolves around them


---

### 📄 store_setup_and_launch.md

# M9 — Store Setup & Launch

> Launch fast, iterate faster. A live store generating data beats a perfect store generating nothing.

## Source

Danilo tabs: 286 (Store Setup Checklist), 289 (Page Speed Checklist), 290 (Page Speed Checklist1)

---

## Week 1 Setup Sequence (U2)

Don't spend 3 weeks "getting ready." Follow this strict priority order:

| Day | Focus | Key Tasks | Gate |
|-----|-------|-----------|------|
| **Day 1** | Account + Domain | Create Shopify, buy domain, set up business email, connect DNS | Domain resolving + SSL active |
| **Day 2** | Products | Upload product listings, images, descriptions, SKUs, variants | At least 1 product live in admin |
| **Day 3** | Payments + Subscription | Shopify Payments, Shop Pay, PayPal, Recharge/Skio setup | Test transaction successful |
| **Day 4** | Tracking | Meta Pixel + CAPI, GA4, Klaviyo integration | All pixels verified firing |
| **Day 5** | Theme + Polish | Dawn theme customization, brand colors, logo, navigation, legal pages | Store looks professional |
| **Day 6** | Testing | Full test orders (desktop + mobile), email flows, subscription, speed check | All P0 tests pass |
| **Day 7** | Launch | Remove password, verify, go live. NO ADS Day 1 — verify organic checkout | Store is live |

**The rule**: A live store generating data beats a perfect store generating nothing. You can polish AFTER launch. Do not let typography choices delay your launch by 2 weeks.

---

## Store Setup Master Checklist

### 1. Account & Domain Setup

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 1.1 | Create Shopify account (Basic plan, annual billing) | P0 | $29/mo. Use business email, not personal |
| 1.2 | Purchase custom domain | P0 | Buy through Shopify OR transfer existing. .com preferred |
| 1.3 | Connect domain to Shopify | P0 | Update DNS, verify SSL auto-provisions (48hr) |
| 1.4 | Set up business email (Google Workspace) | P0 | hello@, support@, team@ minimum |
| 1.5 | Configure store timezone and currency | P1 | Match your primary market |
| 1.6 | Set up Google Workspace / business email | P1 | Required before any tool signups |

**Gate**: Do not proceed to Theme until domain is resolving and SSL is active.

### 2. Theme & Design

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 2.1 | Install Dawn theme (free) or approved premium theme | P0 | Dawn is optimized for speed. Premium themes: Prestige, Impact, Sense |
| 2.2 | Upload logo (SVG preferred, PNG fallback) | P0 | Follow asset naming: Img_Logo_Primary_v1.svg |
| 2.3 | Configure brand colors in theme settings | P0 | Match brand book (M11). Primary, secondary, accent, background, text |
| 2.4 | Set up typography (max 2 fonts) | P1 | Each font = ~50-100KB load time. System fonts are fastest |
| 2.5 | Configure header/footer navigation | P1 | Keep nav simple: Shop, About, FAQ, Contact. No mega-menus at launch |
| 2.6 | Set up favicon (32x32 PNG) | P1 | Small detail, big professionalism signal |

**Speed consideration**: Every custom font and image adds load time. Dawn's default is already optimized — customize minimally at launch.

### 3. Product Setup

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 3.1 | Create product listings with full descriptions | P0 | Title, description, images, price, compare-at price, SKU |
| 3.2 | Upload product images (min 4 per product) | P0 | Hero, ingredients, lifestyle, size reference. WebP format, <200KB each |
| 3.3 | Set up product variants if applicable | P0 | Size, flavor, quantity. Use Shopify's native variant system |
| 3.4 | Configure inventory tracking | P0 | Track quantity, set low-stock alerts (M24 alignment) |
| 3.5 | Set up collections (manual + automated) | P1 | "All Products", "Best Sellers", "Subscriptions" at minimum |
| 3.6 | Add product tags for filtering | P1 | Standardize: type_supplement, flavor_unflavored, size_30day |
| 3.7 | Set up product reviews (Judge.me) | P1 | Install app, configure auto-request email (7 days post-delivery) |
| 3.8 | Create bundle/multi-pack products if applicable | P2 | Only if pricing strategy includes bundles (see M25) |

**IonWave-specific**: Supplement products MUST include supplement facts image, ingredient list in description, and any required disclaimers. Check FDA/FTC compliance (M22).

### 4. Checkout & Payments

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 4.1 | Activate Shopify Payments | P0 | Eliminates extra transaction fees. Requires EIN/SSN verification |
| 4.2 | Enable Shop Pay | P0 | Highest-converting accelerated checkout. 1.91x higher conversion vs guest |
| 4.3 | Enable PayPal | P0 | ~10-15% of customers prefer it. Free to activate |
| 4.4 | Configure checkout settings | P0 | Guest checkout ON, email marketing opt-in, order notes OFF |
| 4.5 | Set up shipping rates | P0 | Free shipping threshold recommended (e.g., $49+). Flat rate below threshold |
| 4.6 | Configure tax settings | P0 | Auto-calculate US tax. Verify nexus states. Consider Avalara if complex |
| 4.7 | Set up abandoned checkout recovery | P1 | Shopify native (1 email) + Klaviyo flows (3-email sequence, see M17) |
| 4.8 | Test checkout flow end-to-end | P0 | Place a real test order. Verify email confirmations. Test on mobile |

**Critical**: Test the FULL checkout on mobile before launch. 70%+ of D2C traffic is mobile.

### 5. Subscription Setup

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 5.1 | Install Recharge or Skio | P0 | This is core to the IonWave model — not optional |
| 5.2 | Configure subscription plans (frequency options) | P0 | 30-day default, 45-day and 60-day options. 30-day as pre-selected |
| 5.3 | Set subscription discount (10-15% off one-time) | P0 | Industry standard. Test 10% vs 15% once traffic allows (M14) |
| 5.4 | Configure customer portal (manage/pause/skip) | P0 | Self-service reduces support load. Allow pause but make cancel require reason |
| 5.5 | Set up dunning management (failed payments) | P1 | 3 retry attempts over 7 days. SMS + email notification on failure |
| 5.6 | Make subscription the DEFAULT purchase option | P0 | One-time should be available but subscription pre-selected on PDP |
| 5.7 | Implement subscription-first UX pattern (see below) | P0 | Toggle > dropdown. Subscription price shown first |

**IonWave target**: 40% subscription rate (HYP-003). The entire product page should be designed around subscription as the primary action.

#### Subscription UX Pattern (U8)

The product page purchase widget should follow this exact pattern:

```
┌─────────────────────────────────────┐
│  ● Subscribe & Save 15%    $41.65   │  ← PRE-SELECTED, prominent
│    Delivered every 30 days           │
│    [Toggle: 30 / 45 / 60 days]      │
│                                      │
│  ○ One-time purchase       $49.00   │  ← Secondary, less prominent
└─────────────────────────────────────┘
        [ ADD TO CART ]
```

**Key UX rules**:
1. **Subscription price shown FIRST** — the savings are the first thing they see
2. **Toggle, NOT dropdown** — toggles convert 15-20% better than dropdowns for binary choices
3. **Show savings as both % and $** — "$41.65 (Save $7.35)" is more concrete than "Save 15%"
4. **One-time shown as strikethrough or secondary** — visually communicate it's not the recommended option
5. **Subscription pre-selected** — buyer has to actively choose NOT to subscribe

### 6. Apps & Integrations

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 6.1 | Install Klaviyo (email) | P0 | Connect Shopify integration immediately. Sync customers + orders |
| 6.2 | Install Judge.me (reviews) | P0 | Free tier. Auto-request review emails |
| 6.3 | Install Meta Pixel + CAPI | P0 | See tracking_and_attribution.md for full setup |
| 6.4 | Install GA4 | P0 | Enhanced ecommerce tracking. Server-side recommended |
| 6.5 | Install Recharge/Skio (subscription) | P0 | If not done in Step 5 |
| 6.6 | Connect 3PL integration | P1 | ShipBob, ShipStation, or similar. Order auto-sync (M24) |

**App discipline**: Maximum 8-10 apps at launch. Every app adds JavaScript, slows the store, and increases complexity. Audit quarterly — if you haven't used it in 30 days, uninstall.

### 7. Legal & Policies

| # | Task | Priority | Notes |
|---|------|----------|-------|
| 7.1 | Create Privacy Policy | P0 | Shopify generates a template. Customize for your data practices |
| 7.2 | Create Terms of Service | P0 | Include subscription terms, auto-renewal disclosure |
| 7.3 | Create Refund/Return Policy | P0 | 30-day money-back guarantee recommended for supplements |
| 7.4 | Create Shipping Policy | P0 | Processing time, shipping methods, delivery estimates by region |
| 7.5 | Add FDA disclaimer | P0 | "These statements have not been evaluated by the FDA..." — required for supplements |
| 7.6 | Configure cookie consent banner | P1 | Required for GDPR/CCPA. Use Shopify's built-in or free app. Decline cookies by default |

**Supplement-specific**: Consult legal counsel for supplement claims compliance. FTC guidelines apply to all marketing materials, ads, and product descriptions. See M22 (Legal/Compliance) for full framework.

### 8. Pre-Launch Testing Protocol

| # | Test | Pass Criteria | Notes |
|---|------|---------------|-------|
| 8.1 | Place test order (full checkout) | Order completes, confirmation email received | Use Shopify's Bogus Gateway or real card with immediate refund |
| 8.2 | Place test subscription order | Subscription created, portal accessible | Verify customer can manage/pause/cancel |
| 8.3 | Mobile checkout test | Full flow works on iPhone + Android | Test on actual devices, not just browser resize |
| 8.4 | Email flow test | Welcome, order confirm, shipping confirm all fire | Trigger each Klaviyo flow. Check formatting |
| 8.5 | Page speed test | All pages score ≥ 70 on PageSpeed Insights | See Page Speed section below |
| 8.6 | Broken link check | Zero 404 errors | Click every link on every page |
| 8.7 | Cross-browser test | Works on Chrome, Safari, Firefox | Safari matters most (iPhone) |
| 8.8 | Payment test | Shopify Payments + PayPal both process | Test both payment methods |
| 8.9 | Tracking verification | Meta Pixel, GA4, Klaviyo all firing events | Use Meta Pixel Helper, GA4 DebugView |

**Launch rule**: ALL P0 tests must pass before going live. No exceptions.

---

## Page Speed Targets & Optimization

### Core Web Vitals Targets (2026 Standards)

| Metric | Target (Good) | Needs Improvement | Poor |
|--------|--------------|-------------------|------|
| **LCP** (Largest Contentful Paint) | ≤ 2.5s | 2.5s - 4.0s | > 4.0s |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms - 500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | ≤ 0.1 | 0.1 - 0.25 | > 0.25 |

> **Note**: INP replaced FID (First Input Delay) in March 2024. INP measures responsiveness across ALL interactions, not just the first one. It's a harder standard — expect lower scores initially.

### Additional Speed Targets

| Metric | Target |
|--------|--------|
| Time to First Byte (TTFB) | < 200ms |
| First Contentful Paint (FCP) | < 1.8s |
| Total page load time | < 3s |
| PageSpeed Insights score | ≥ 70 (mobile) |

### Why Speed Matters for D2C

- 1-second delay = ~7% fewer conversions
- 40% of visitors abandon sites that take > 3 seconds
- Google uses Core Web Vitals as a ranking factor
- Mobile users (70%+ of D2C traffic) expect < 3 second loads
- Every 100ms improvement in LCP = ~0.4% more conversions

### Speed Testing Tools

| Tool | URL | Use For |
|------|-----|---------|
| **PageSpeed Insights** | pagespeed.web.dev | Primary test tool (Google's own) |
| **GTmetrix** | gtmetrix.com | Detailed waterfall analysis |
| **WebPageTest** | webpagetest.org | Advanced testing, multiple locations |
| **Chrome DevTools** | Built into Chrome | Real-time debugging, network tab |

**Testing cadence**: Test after every theme change, app install, or content update. Monthly baseline check minimum.

### Speed Optimization Checklist

#### Images (Biggest Impact)

- [ ] Compress ALL images before upload (TinyPNG, ShortPixel, or Squoosh)
- [ ] Use WebP format (30-50% smaller than JPEG/PNG) — Shopify auto-converts if supported
- [ ] Lazy load images below the fold (Shopify themes handle this natively)
- [ ] Specify image dimensions in HTML (prevents CLS)
- [ ] Hero images: max 200KB. Product images: max 150KB each
- [ ] Use responsive images (srcset) — Dawn theme does this automatically

#### Code & Scripts

- [ ] Minify CSS and JavaScript (theme-level, usually automatic)
- [ ] Remove unused CSS/JS from uninstalled apps (apps often leave residual code)
- [ ] Defer non-critical JavaScript (analytics, chat widgets, etc.)
- [ ] Reduce redirects (each redirect = 100-300ms added)
- [ ] Limit custom fonts to 2 max (consider system font stack)

#### Hosting & Infrastructure

- [ ] Use Shopify's built-in CDN (automatic, no action needed)
- [ ] Enable browser caching (Shopify handles this)
- [ ] GZIP compression (automatic on Shopify)

#### Third-Party Scripts & Apps

- [ ] Audit ALL installed apps — remove unused ones immediately
- [ ] Limit third-party scripts to essential only (each script = 50-200ms)
- [ ] Load chat widgets lazily (only on pages where needed)
- [ ] Load review widgets asynchronously
- [ ] Test speed BEFORE and AFTER every new app install

**The #1 speed killer on Shopify**: Too many apps. Each app injects JavaScript. 10 apps can add 2-3 seconds of load time. Ruthlessly uninstall anything you're not actively using.

#### Shopify-Specific Speed Killers (U7)

Generic advice like "minify CSS" doesn't help on Shopify (it's automatic). These are the ACTUAL Shopify speed killers:

| Killer | Impact | Fix |
|--------|--------|-----|
| **Too many Liquid render loops** | 200-500ms added per nested loop | Limit collection pages to 12-16 products per page. Use pagination, not "load more" |
| **Apps injecting into theme.liquid** | Each injection = synchronous blocking script | Check theme.liquid for `{% render 'app-...' %}` lines. Remove any from uninstalled apps |
| **Unoptimized collection pages** | Loading 50+ product images at once | Paginate at 16. Use lazy loading. Don't load all variants' images |
| **Third-party chat widgets (Intercom, Drift)** | 200-400ms, loads on every page | Load lazily, only on pages where needed (support page, checkout) |
| **Residual app code** | Uninstalled apps leave CSS/JS behind | After uninstalling ANY app: check theme.liquid, check assets/, check snippets/ for remnants |
| **Custom fonts from external CDNs** | DNS lookup + download per font | Use fonts from Shopify's built-in font library (preloaded) or system font stack |

**Post-app-install protocol**: ALWAYS run PageSpeed Insights BEFORE and AFTER installing a new app. If the score drops by more than 5 points, that app is too expensive for its benefit.

### Monthly Speed Audit Protocol

1. Run PageSpeed Insights on: Homepage, PDP, Collection page, Cart, Checkout
2. Record scores in M30 dashboard (monthly tracking)
3. If any page drops below 70: identify cause (usually a new app or unoptimized image)
4. Fix within 7 days
5. Re-test to confirm fix

---

## Launch Sequence

### T-7 Days: Final Prep

- [ ] All P0 checklist items complete
- [ ] Product listings finalized with images
- [ ] Subscription configured and tested
- [ ] Email flows active (Welcome, Abandoned Cart, Order Confirmation)
- [ ] Tracking pixels verified (Meta, GA4, TikTok)
- [ ] Legal pages published

### T-1 Day: Go/No-Go

- [ ] Full test order placed and confirmed
- [ ] Mobile checkout verified on real devices
- [ ] Page speed ≥ 70 on all key pages
- [ ] Klaviyo flows tested and active
- [ ] Inventory confirmed with 3PL (M24)
- [ ] Customer support email monitored

### Launch Day

- [ ] Remove password protection from store
- [ ] Verify all pages load correctly
- [ ] Place first real order yourself (confirms everything works)
- [ ] Monitor Meta Pixel Helper for event firing
- [ ] Monitor GA4 Realtime for traffic
- [ ] Have support email open all day
- [ ] Do NOT run ads on Day 1 — verify organic checkout works first

### T+1 Day: Post-Launch Verification

- [ ] Review all orders processed
- [ ] Verify email flows triggered correctly
- [ ] Check subscription orders created properly
- [ ] Review page speed under real traffic
- [ ] Fix any issues found
- [ ] THEN turn on paid traffic (Day 2-3)

---

## Common Launch Mistakes (Avoid These)

1. **Launching without mobile testing** — 70%+ traffic is mobile. If mobile checkout is broken, you lose most of your revenue
2. **Too many apps at launch** — Kills speed. Start with 6-8, add more only when needed
3. **No abandoned cart recovery** — You WILL lose 70% of carts. Recovery emails recapture 5-15%
4. **Subscription not pre-selected** — If one-time is default, most buyers won't switch to subscription
5. **Running ads before checkout is verified** — Burning money. Verify organic checkout first
6. **Skipping page speed check** — A slow store silently kills conversion. You won't see it in analytics
7. **No test order on mobile** — Desktop checkout working ≠ mobile checkout working
8. **Launching Friday/weekend** — Launch Tuesday-Wednesday. You need weekday support available for issues
9. **Building on checkout.liquid** — Shopify is deprecating checkout.liquid in favor of Checkout Extensions (powered by Shopify Functions). Any checkout customization (post-purchase upsells, custom fields) should use Extensions, not legacy scripts. This doesn't affect basic launches, but avoid installing apps that modify checkout.liquid (U13)


---

### 📄 tech_stack_and_tools.md

# M9 — Tech Stack & Tools

> Every tool must earn its place. If it doesn't directly drive revenue, reduce cost, or save time — kill it.

## Source

Danilo tabs: 285 (Tech Stack), 288 (Tool Stack Architecture), 292 (Tool Login Credentials)

## Tool Selection Criteria

Before adding ANY tool, answer:

1. **Does it solve a problem I have TODAY?** (Not "might need someday")
2. **Can I measure its ROI within 30 days?**
3. **Does it integrate natively with Shopify?** (API > manual export)
4. **What's the exit cost?** (Data portability, contract lock-in)
5. **Will I actually use it?** (Better to master 5 tools than half-use 15)

**Rule**: No tool gets added during Month 1 unless it's in Core Stack. Growth Stack unlocks at Month 2+. Scale Stack unlocks at $10K+ MRR.

### Theme Performance Budget (U1)

Before installing any app or script, check against these hard limits:

| Budget Item | Limit | Why |
|-------------|-------|-----|
| Total installed apps | **8 max at launch** | Each app injects JS. 10+ apps = 2-3s added load time |
| Total JavaScript payload | **500KB max** (compressed) | Above this, mobile users on 3G suffer. Check in Chrome DevTools → Network → JS |
| External scripts | **3 max** (non-Shopify domains) | Each external script = DNS lookup + connection = 100-300ms |
| Custom fonts | **2 max** | Each font file = 50-100KB. System font stack is fastest |

**Enforcement rule**: If a new app would push you over ANY budget limit, something existing must be removed first. No exceptions. Dawn 2.0+ has built-in sections everywhere — this eliminates the need for most page builder apps.

---

## Phase 0: Core Stack (Launch — $50-100/mo)

These are non-negotiable. You cannot launch without them.

| Tool | Purpose | Cost | Why This One |
|------|---------|------|-------------|
| **Shopify Basic** | Storefront + checkout | $29/mo (annual) | Industry standard for D2C. 2.9% + $0.30 per transaction with Shopify Payments. Eliminates 3rd-party gateway fee |
| **Recharge** or **Skio** | Subscription management | $99/mo + 1.25% | Recharge = market leader, more integrations. Skio = better UX, passwordless login. Either works — pick one and commit |
| **Klaviyo** | Email marketing | Free <250 contacts | Best-in-class Shopify integration. Predictive analytics included. Grows with you — don't switch later |
| **Judge.me** | Reviews/UGC | Free (basic) | Lightweight, fast. Free tier covers launch. Auto-request emails. SEO-friendly structured data |
| **GA4** | Web analytics | Free | Non-negotiable. Server-side tracking setup recommended (see tracking_and_attribution.md) |
| **Meta Ads Manager** | Paid acquisition | Free (ad spend separate) | Primary paid channel for D2C supplement. Pixel + CAPI required |
| **Shopify Payments** | Payment processing | 2.9% + $0.30 | Eliminates extra transaction fees. Includes Shop Pay (highest-converting accelerated checkout) |

**Total Core Stack**: ~$130/mo + transaction fees
**What you DON'T need yet**: SMS, helpdesk, loyalty, A/B testing, advanced analytics

---

## Phase 1: Growth Stack (Month 2+ / First 100 Orders)

Add these one at a time. Each must prove ROI before the next gets added.

| Tool | Purpose | Cost | Unlock Trigger |
|------|---------|------|---------------|
| **Postscript** or **Attentive** | SMS marketing | $25+/mo | Email list > 500 AND email revenue > 20% of total |
| **Microsoft Clarity** | Heatmaps + session replay | Free | First 1,000 sessions. Replaces Hotjar for free |
| **Shopify A/B testing app** | Conversion optimization | $74+/mo (Shoplift/Intelligems) | Only after 500+ monthly sessions. Statistical significance requires traffic |
| **Triple Whale** or **Northbeam** | Multi-touch attribution | $100-300/mo | Ad spend > $3K/mo. Below this, MER + UTMs is sufficient |
| **Gorgias** | Customer support helpdesk | $50/mo | Support volume > 20 tickets/week. Before this, shared inbox works |
| **Canva Pro** | Creative design | $15/mo | When free tier limits hit. Usually Month 2-3 |

**Total Growth Stack**: +$150-300/mo on top of Core
**Decision rule**: Don't add a Growth tool until the unlock trigger is met

---

## Phase 2: Scale Stack ($10K+ MRR)

| Tool | Purpose | Cost | Unlock Trigger |
|------|---------|------|---------------|
| **Smile.io** or **Yotpo** | Loyalty program | $49+/mo | Repeat purchase rate > 25% AND 1,000+ customers |
| **Privy** or **Justuno** | Pop-ups + on-site conversion | Free-$30/mo | Traffic > 5,000/mo AND conversion rate plateauing |
| **Rebuy** or **Also Bought** | Product recommendations | $99+/mo | AOV optimization becomes priority, 3+ SKUs |
| **Richpanel** or **Gorgias Pro** | Advanced support + self-service | $100+/mo | Support team > 1 person |
| **Server-side GTM** | Enhanced tracking | $50-150/mo (GCP hosting) | When ad spend > $5K/mo and attribution accuracy is critical |

**Total Scale Stack**: +$300-600/mo
**Note**: Shopify plan upgrade to "Shopify" ($79/mo) makes sense at ~$10K MRR for lower transaction fees (2.7% vs 2.9%)

---

## Cost Summary by Phase

| Phase | Monthly Cost | Revenue Target |
|-------|-------------|----------------|
| Launch (Month 0-1) | $50-130/mo | Pre-revenue → first sales |
| Growth (Month 2-6) | $200-400/mo | $1K-10K MRR |
| Scale (Month 6-12) | $500-1,000/mo | $10K-50K MRR |
| Mature (Year 2+) | $1,000-2,500/mo | $50K+ MRR |

**Critical rule**: Tech spend should NEVER exceed 5% of revenue. If it does, you're over-tooled.

### Monthly Tool ROI Review (U5)

Starting **Month 2**, review every paid tool monthly:

| Tool | Monthly Cost | What It Produced This Month | One-Sentence ROI |
|------|-------------|----------------------------|-----------------|
| [tool] | $[cost] | [specific output] | [justify or cancel] |

**The one-sentence test**: If you can't articulate the ROI of a paid tool in one sentence, cancel it today. Zombie subscriptions are the #1 silent budget killer for solo founders.

---

## Shopify Plan Comparison (2026)

| Feature | Basic ($29/mo) | Shopify ($79/mo) | Advanced ($299/mo) |
|---------|---------------|-------------------|---------------------|
| Online credit card rate | 2.9% + $0.30 | 2.7% + $0.30 | 2.5% + $0.30 |
| 3rd-party gateway fee | 2.0% | 1.0% | 0.6% |
| Staff accounts | 2 | 5 | 15 |
| Reports | Basic | Standard | Advanced + custom |
| Shipping discount | Up to 77% | Up to 88% | Up to 88% |
| Annual billing discount | ~25% | ~25% | ~25% |

**IonWave recommendation**: Start Basic. Upgrade to Shopify at ~$10K MRR (the 0.2% transaction fee savings pays for the plan at ~$25K/mo GMV).

---

## Deprecated / Avoid

| Tool | Status | Replacement |
|------|--------|-------------|
| Google Optimize | **Shut down Sep 2023** | Shoplift ($74/mo) or Intelligems ($74/mo) for Shopify-native A/B testing |
| Hotjar (paid) | Unnecessary cost | Microsoft Clarity (free, same features) |
| Mailchimp | Poor Shopify integration | Klaviyo (purpose-built for ecommerce) |
| WordPress/WooCommerce | Wrong platform | Shopify (operational simplicity for solo founder) |
| Custom-built solutions | Premature optimization | Use SaaS until $100K+ MRR |

### "Do Not Install" List (U10)

These apps are popular but either redundant with Shopify-native features or not worth the speed cost:

| App Category | Why NOT to Install | What to Use Instead |
|-------------|-------------------|-------------------|
| **SEO apps** (Yoast, SEO Manager) | Shopify handles meta titles, descriptions, sitemaps, canonical URLs natively. These apps add JS for marginal benefit | Shopify's built-in SEO fields. Manual sitemap submission in Google Search Console |
| **Currency converters** | Shopify Markets handles multi-currency natively (on Shopify plan and above) | Shopify Markets (included in plan) |
| **Social proof pop-ups** ("X just bought...") | Annoying UX, minimal conversion lift (<0.5% in most tests), adds 100-200ms load time | Product reviews (Judge.me) provide authentic social proof |
| **Page builder apps** | Dawn 2.0+ has sections everywhere. Page builders add massive JS overhead | Use Dawn's native section editor |
| **Image sliders/carousels** | Users don't interact with them. They slow pages and push content below fold | Static hero image with clear CTA |
| **"Speed optimization" apps** | Ironic — most add their own JS. Shopify's built-in CDN/compression is sufficient | Follow the Speed Optimization Checklist in store_setup_and_launch.md |

---

## Tool Credential Management

### Credential Register Template

| Tool | URL | Email | Password Location | 2FA Enabled | Owner | Recovery Method |
|------|-----|-------|-------------------|-------------|-------|----------------|
| Shopify | admin.shopify.com | [email] | 1Password | Yes | Operator | Recovery codes in vault |
| Klaviyo | klaviyo.com | [email] | 1Password | Yes | Operator | |
| Meta Business | business.facebook.com | [email] | 1Password | Yes | Operator | Business Manager admin |
| GA4 | analytics.google.com | [email] | 1Password | Yes | Operator | Google account recovery |
| Stripe | dashboard.stripe.com | [email] | 1Password | Yes | Studio | |
| Recharge/Skio | [url] | [email] | 1Password | Yes | Operator | |
| 3PL Portal | [url] | [email] | 1Password | No → Fix | Operator | |
| Domain Registrar | [url] | [email] | 1Password | Yes | Studio | |
| Canva | canva.com | [email] | 1Password | No | Operator | |

### Credential Security Rules

1. **Password manager is mandatory** — 1Password, Bitwarden, or equivalent. No exceptions
2. **Unique password per account** — Never reuse passwords across tools
3. **2FA on ALL critical accounts** — Shopify, email, bank, ads, domain. Non-negotiable
4. **Quarterly access review** — Remove unused accounts, rotate passwords for shared accounts
5. **Separate admin from daily-use** — Use a dedicated admin email for business-critical accounts
6. **Document who has access to what** — Update credential register when team changes
7. **Recovery codes stored offline** — Print or store in separate secure location from passwords

### If Someone Leaves the Team

1. Revoke access to ALL tools within 24 hours
2. Change shared passwords
3. Review and update credential register
4. Check for any personal accounts linked to business tools
5. Transfer ownership of any assets they created

---

## Integration Architecture

```
                    ┌──────────────┐
                    │   SHOPIFY    │ ← Source of truth for orders, products, customers
                    │   (Store)    │
                    └──────┬───────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
     ┌──────▼──────┐ ┌────▼─────┐ ┌──────▼──────┐
     │  Recharge/  │ │ Shopify  │ │   Klaviyo   │
     │    Skio     │ │ Payments │ │   (Email)   │
     │(Subscript.) │ │ ($$)     │ │             │
     └─────────────┘ └──────────┘ └─────────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
     ┌──────▼──────┐ ┌────▼─────┐ ┌──────▼──────┐
     │  Meta Ads   │ │   GA4    │ │   3PL       │
     │  (Acquire)  │ │(Measure) │ │  (Fulfill)  │
     └─────────────┘ └──────────┘ └─────────────┘
```

**Data flow principle**: Shopify is the hub. Every tool connects TO Shopify, not to each other. This prevents data sync nightmares and makes tool swaps painless.

---

## Decision Log

| Decision | Rationale | Date |
|----------|-----------|------|
| Shopify over WooCommerce | Operational simplicity, native payments, ecosystem | Workshop |
| Klaviyo over Mailchimp | Purpose-built ecommerce, predictive analytics, Shopify-native | Workshop |
| Microsoft Clarity over Hotjar | Free, same core features, no reason to pay | Workshop |
| Recharge/Skio over custom | Subscription is core to IonWave model — needs dedicated tool | Workshop |
| Start Basic, upgrade later | 0.2% fee difference doesn't justify $50/mo until ~$25K GMV | Workshop |


---

### 📄 tracking_and_attribution.md

# M9 — Tracking & Attribution

> You can't optimize what you can't measure. But measuring the wrong thing is worse than measuring nothing.

## Source

Danilo tab: 287 (Tracking Setup)

## Cross-TUP Alignment

- **M30** (Analytics & Dashboards): MER is the primary efficiency metric, NOT ROAS (see M30 U2)
- **M14** (Testing & CRO): A/B test tracking requires consistent event taxonomy
- **M17** (Email): Klaviyo attribution vs UTM attribution — understand both

---

## North Star Metric: MER (Marketing Efficiency Ratio)

```
MER = Total Revenue / Total Marketing Spend
```

**Why MER, not ROAS?**

| Metric | Formula | Post-iOS 14.5 Accuracy | Use For |
|--------|---------|----------------------|---------|
| **MER** (primary) | Total Revenue / Total Ad Spend | ~95% (uses actual revenue) | Business-level efficiency. The metric that matters |
| **Platform ROAS** (context only) | Platform-Reported Revenue / Platform Spend | 60-80% (over-reports 20-40%) | Relative campaign comparison WITHIN a platform. Never trust absolute values |
| **Blended ROAS** | Same as MER but branded differently | ~95% | If you see "blended ROAS" anywhere, it means MER. Use MER for clarity |
| **GA4 ROAS** | GA4-Attributed Revenue / Spend | 70-85% (under-reports) | Under-counts due to cookie blocking, consent, ad blockers |

**Decision rule**: When platform ROAS and MER disagree, MER wins. Period. Platform ROAS is useful only for comparing Campaign A vs Campaign B on the SAME platform.

---

## Tracking Architecture

### Pixel + Server-Side (Hybrid Approach)

Post-iOS 14.5, browser-only tracking captures 40-70% of conversions. Server-side tracking recovers this to 85-98%.

```
┌──────────────┐         ┌──────────────┐
│   Browser     │         │   Server     │
│   (Pixel)     │         │   (CAPI)     │
│               │         │              │
│ Meta Pixel    │         │ Meta CAPI    │
│ GA4 gtag      │         │ GA4 MP       │
│ TikTok Pixel  │         │ TikTok EAPI  │
└──────┬───────┘         └──────┬───────┘
       │                        │
       │   Deduplication        │
       │   (event_id match)     │
       └────────┬───────────────┘
                │
         ┌──────▼──────┐
         │  Platform   │
         │  (receives  │
         │  both, de-  │
         │  duplicates)│
         └─────────────┘
```

**Critical**: Both browser pixel AND server-side MUST fire. They use matching `event_id` parameters so platforms deduplicate automatically. If one path is blocked (ad blocker, iOS), the other recovers the event.

---

## Meta Pixel + Conversions API Setup

### Browser Pixel Setup

| # | Task | Status |
|---|------|--------|
| 1 | Create Meta Pixel in Events Manager | ☐ |
| 2 | Install pixel on Shopify (Settings → Customer Events → Meta) | ☐ |
| 3 | Verify pixel fires on all pages (use Meta Pixel Helper extension) | ☐ |
| 4 | Configure standard events: ViewContent, AddToCart, InitiateCheckout, Purchase | ☐ |
| 5 | Set up custom event: SubscriptionCreated (for subscription tracking) | ☐ |
| 6 | Verify Aggregated Event Measurement (AEM) priority: Purchase > InitiateCheckout > AddToCart > ViewContent | ☐ |
| 7 | Verify domain in Meta Business Settings | ☐ |

### Conversions API (Server-Side) Setup

| # | Task | Status |
|---|------|--------|
| 1 | Enable Shopify's native Meta CAPI integration (Settings → Customer Events) | ☐ |
| 2 | Verify Event Match Quality (EMQ) score ≥ 6.0 (target ≥ 8.0) | ☐ |
| 3 | Match parameters: email, phone, fbp, fbc, external_id | ☐ |
| 4 | Verify deduplication: event_id matches between pixel and CAPI | ☐ |
| 5 | Test with Meta Events Manager → Test Events tool | ☐ |
| 6 | Monitor EMQ weekly for first month, then monthly | ☐ |

**EMQ targets**: 6.0 = minimum acceptable. 8.0 = good. 9.0+ = excellent. Below 6.0 = ad optimization severely degraded.

### Implementation Options

| Method | Cost | Complexity | Best For |
|--------|------|-----------|----------|
| **Shopify native Meta integration** | Free | Low | Launch. Start here |
| **Shopify app (Conversios, Tracklution)** | $30-100/mo | Low | If native integration EMQ is < 6.0 |
| **Google Server-side Tag Manager (sGTM)** | $50-150/mo (GCP) | High | $5K+ ad spend/mo, need full control |

**IonWave recommendation**: Start with Shopify's native Meta integration. It handles CAPI automatically. Only upgrade to sGTM when ad spend exceeds $5K/mo and attribution accuracy becomes critical.

---

## GA4 Setup

| # | Task | Status |
|---|------|--------|
| 1 | Create GA4 property (Analytics → Admin → Create Property) | ☐ |
| 2 | Install GA4 on Shopify (Settings → Customer Events → Google) | ☐ |
| 3 | Enable Enhanced Ecommerce events | ☐ |
| 4 | Configure key events: purchase, add_to_cart, begin_checkout, view_item | ☐ |
| 5 | Set up custom dimensions: subscription_status, order_type, customer_type | ☐ |
| 6 | Link Google Ads account (if running Google Ads) | ☐ |
| 7 | Verify data in GA4 Realtime report | ☐ |
| 8 | Set up data retention: 14 months (max free tier) | ☐ |

### GA4 Known Limitations

- Under-reports conversions by 10-25% (ad blockers, consent, cookie expiry)
- Last-click attribution by default (misses top-of-funnel impact)
- Data processing delay: 24-48 hours for some reports
- Consent Mode v2 required for EU traffic (impacts data completeness)
- Free tier: 14-month data retention only

**Use GA4 for**: User behavior analysis, site search, content performance, organic channel analysis.
**Don't use GA4 for**: Absolute revenue numbers (use Shopify) or ad efficiency (use MER).

---

## TikTok Pixel + Events API Setup

| # | Task | Status |
|---|------|--------|
| 1 | Create TikTok Pixel in TikTok Ads Manager | ☐ |
| 2 | Install via Shopify integration (Shopify App Store → TikTok) | ☐ |
| 3 | Configure events: ViewContent, AddToCart, CompletePayment | ☐ |
| 4 | Enable Events API (server-side) through Shopify integration | ☐ |

**Note**: TikTok tracking is lower priority than Meta/GA4. Install if running TikTok ads, otherwise defer.

---

## UTM Parameter Structure

### Standard UTM Taxonomy

| Parameter | Format | Example |
|-----------|--------|---------|
| `utm_source` | Platform name (lowercase) | `meta`, `google`, `tiktok`, `klaviyo`, `organic` |
| `utm_medium` | Channel type | `paid_social`, `paid_search`, `email`, `sms`, `organic_social` |
| `utm_campaign` | Campaign name | `launch_promo`, `retargeting_30d`, `welcome_flow` |
| `utm_content` | Creative/variant identifier | `hook1_lifestyle`, `ugc_testimonial_v2`, `email_hero_a` |
| `utm_term` | Keyword or audience | `interest_fitness`, `lookalike_1pct`, `brand_search` |

### UTM Rules

1. **Always lowercase** — `Meta` ≠ `meta` in analytics. Pick one (lowercase)
2. **No spaces** — Use underscores: `welcome_flow` not `welcome flow`
3. **Be specific but consistent** — Same campaign = same UTM everywhere
4. **Document in a UTM log** — Spreadsheet tracking all active UTMs prevents duplicates
5. **Never UTM internal links** — UTMs on your own site pages break attribution

### Example URLs

```
# Meta prospecting ad
https://ionwave.com?utm_source=meta&utm_medium=paid_social&utm_campaign=launch_prospecting&utm_content=hook3_minerals_static_v2&utm_term=interest_health

# Klaviyo welcome email
https://ionwave.com?utm_source=klaviyo&utm_medium=email&utm_campaign=welcome_flow&utm_content=email_02_benefits

# TikTok ad
https://ionwave.com?utm_source=tiktok&utm_medium=paid_social&utm_campaign=launch_ugc&utm_content=creator_jessica_60s_v1
```

---

## Attribution Model Comparison

| Source | Method | Accuracy (Post-iOS 14.5) | Over/Under Reports | Use For |
|--------|--------|--------------------------|--------------------|---------|
| **Shopify** | Last-click | Medium | Under-reports paid (credits direct/organic) | Order of record. Revenue source of truth |
| **Meta Ads** | 7-day click / 1-day view | Low-Medium | Over-reports 20-40% (view-through inflation) | Relative campaign comparison only |
| **GA4** | Last-click (default) | Medium | Under-reports 10-25% (ad blockers, consent) | User behavior, organic channels |
| **Triple Whale** | Multi-touch (pixel-based) | Medium-High | Most balanced but not perfect | Worth it at $3K+/mo ad spend |
| **MER** (calculated) | Total Revenue / Total Spend | Highest | N/A — it's actual numbers | THE metric. Always calculate |

### When Sources Disagree (They Always Will)

**Scenario**: Meta says ROAS = 4.0x. GA4 says ROAS = 1.8x. MER = 2.5x.

**What's happening**: Meta over-attributes (counts view-through), GA4 under-attributes (misses blocked users). MER is the actual business result.

**Decision framework**:
1. **Business health decisions** → Use MER
2. **Campaign optimization** (which ad is better?) → Use platform metrics for relative comparison
3. **Channel budget allocation** → Use MER + incrementality testing (turn off a channel for 7 days, measure MER impact)
4. **Reporting to stakeholders** → Use MER with platform context

### Awareness vs. Conversion Attribution

| Type | Answers | Measured By | Example |
|------|---------|------------|---------|
| **Awareness** | "How did you first hear about us?" | Post-purchase survey | "I saw a TikTok video" |
| **Conversion** | "What drove you to buy today?" | UTM / last-click | utm_source=meta (clicked a retargeting ad) |

**Why they disagree**: A customer discovers you on TikTok (awareness), browses your site 3 times over 2 weeks, then clicks a Meta retargeting ad and buys (conversion). TikTok gets awareness credit. Meta gets conversion credit. Both are correct — they measure different things.

**Decision rule for channel investment**: 60% weight awareness (survey), 40% weight conversion (UTM). Use this blended view for budget allocation. For campaign-level optimization within a channel, use UTM-only.

---

## Daily Metrics to Track

### Phase 1 (Months 1-3): MVD — 7 Metrics Only

Per M30, solo founders track ONLY these 7 metrics daily:

| Metric | Source | Target | Cadence |
|--------|--------|--------|---------|
| **Revenue** | Shopify | Growing weekly | Daily |
| **Orders** | Shopify | Growing weekly | Daily |
| **Ad Spend** | Meta/Google | Within budget | Daily |
| **CAC** | Calculated (Spend/New Customers) | < $45 (HYP-001) | Daily |
| **Subscription Rate** | Recharge/Skio | > 40% (HYP-003) | Daily |
| **Cash Balance** | Bank account | > 30 days runway | Daily |
| **MER** | Calculated (Revenue/Total Spend) | > 2.0x | Daily |

### Phase 2 (Months 3-6): Add

- AOV (Shopify)
- Email revenue % (Klaviyo)
- Churn rate (Recharge/Skio)
- LTV:CAC ratio (calculated)

See M30 (dashboards_and_reporting.md) for full phase-gated metric progression.

---

## Tracking Verification Checklist

Run this verification after initial setup AND after any tracking changes:

| # | Check | Tool | Pass Criteria |
|---|-------|------|---------------|
| 1 | Meta Pixel fires on all pages | Meta Pixel Helper (Chrome ext) | Green icon, no errors |
| 2 | Meta Purchase event fires on order confirmation | Place test order, check Events Manager | Event appears within 5 min |
| 3 | Meta CAPI events received | Events Manager → Test Events | Server events appear alongside browser events |
| 4 | EMQ score ≥ 6.0 | Events Manager → Data Sources | Score displayed per event |
| 5 | GA4 receives real-time data | GA4 → Realtime report | Events appear as you browse |
| 6 | GA4 purchase event fires | Place test order, check GA4 | purchase event with revenue |
| 7 | UTM parameters carry through | Click a UTM link, check GA4 source/medium | Correct attribution in Realtime |
| 8 | Klaviyo receives order data | Klaviyo → Analytics → Dashboard | Order appears within 15 min |
| 9 | Subscription events tracked | Create test subscription | Recharge/Skio event in Klaviyo |
| 10 | No duplicate events | Events Manager → Overview | Event count matches Shopify orders (±5%) |

**Monthly tracking health check**: Compare Shopify orders vs Meta reported conversions vs GA4 purchases. If any source deviates by > 20%, investigate immediately.

---

## Consent Management (U4)

### Why This Matters (Even for US-Only Brands)

- **Consent Mode v2** is required for any EU traffic (even incidental)
- **California CCPA** requires opt-out capability for California residents
- Implementing consent now future-proofs you as regulations expand
- GA4 uses consent signals for **behavioral modeling** — without consent signals, GA4 can't model missing data

### Implementation

| Regulation | Requirement | Implementation |
|-----------|-------------|----------------|
| **GDPR (EU)** | Opt-in required before any tracking | Cookie consent banner with granular choices. No cookies fire until consent given |
| **CCPA (California)** | Opt-out right. Can track by default but must offer "Do Not Sell" | "Do Not Sell My Personal Information" link in footer. Honor opt-out requests |
| **General best practice** | Decline cookies by default on banner | Shopify's built-in cookie banner or free app (Pandectes, Consentmo) |

### GA4 Consent Mode v2

GA4 supports two consent signals:
- `analytics_storage` — controls GA4 cookies
- `ad_storage` — controls advertising cookies (Meta, Google Ads)

When a user declines consent, GA4 still collects anonymized pings and uses **behavioral modeling** to estimate conversions. This recovers ~70% of lost data vs. no consent mode at all.

**Setup**: Configure in Google Tag Manager or Shopify's native Google integration. Set default state to `denied` for EU visitors, `granted` for US visitors.

### Impact on Tracking Accuracy

| Consent Status | Meta CAPI | GA4 | Shopify |
|---------------|-----------|-----|---------|
| Full consent | Full tracking | Full tracking | Always full (first-party) |
| Partial consent | Server-side still fires (CAPI) | Modeled data (~70% recovery) | Always full |
| No consent | Server-side only | Minimal (basic pageviews only) | Always full |

**This is why MER matters**: Shopify revenue is always 100% accurate regardless of consent. MER (Revenue / Spend) doesn't depend on pixel tracking.

---

## UTM Builder Template (U14)

Create a Google Sheet with these columns to prevent UTM inconsistency:

| Column | Auto-populated? | Example |
|--------|----------------|---------|
| Campaign Name | Manual | launch_prospecting |
| utm_source | Dropdown: `meta`, `google`, `tiktok`, `klaviyo`, `organic` | meta |
| utm_medium | Dropdown: `paid_social`, `paid_search`, `email`, `sms`, `organic_social` | paid_social |
| utm_campaign | Manual (match campaign name) | launch_prospecting |
| utm_content | Manual | hook3_minerals_static_v2 |
| utm_term | Manual (optional) | interest_health |
| **Generated URL** | Formula: `=CONCATENATE(base_url, "?utm_source=", B2, "&utm_medium=", C2, "&utm_campaign=", D2, "&utm_content=", E2, IF(F2="", "", CONCATENATE("&utm_term=", F2)))` | Full URL |

**Dropdown enforcement** prevents the #1 UTM mistake: `Meta` vs `meta` vs `facebook` vs `fb` becoming four different sources in your analytics.

Store this sheet in `03_Marketing/` in Drive.

---

## Ad Spend Safety (U12)

### Meta Daily Spend Cap

Set a **hard daily spend cap at 2x your normal daily budget** in Meta Ads Manager:

- Normal daily budget: $50 → Set cap at $100
- Normal daily budget: $100 → Set cap at $200
- This cap is a SAFETY NET against runaway spend or account hijacking

**Where to set**: Meta Ads Manager → Account Settings → Ad Account → Spending Limit

Also set:
- **Campaign-level daily budget** (your actual budget)
- **Account-level spending limit** (cumulative cap, e.g., $3,000/mo)
- **Payment threshold notifications** (alert at 80% of limit)

---

## Common Tracking Mistakes

1. **Trusting platform ROAS as absolute truth** — It's directional only. MER is truth
2. **Not setting up server-side tracking** — You're losing 30-60% of conversion data. Unacceptable for paid acquisition
3. **Inconsistent UTMs** — `Meta` vs `meta` vs `facebook` = three different sources in your analytics. Standardize
4. **UTMs on internal links** — Breaks session attribution. Only UTM external traffic sources
5. **Ignoring EMQ score** — Below 6.0, Meta can't optimize your ads properly. Fix immediately
6. **Over-tracking early** — 50 custom events with 100 monthly orders = noise. Start with standard events only
7. **Not testing after changes** — Every app install, theme change, or pixel update can break tracking. Always verify


---

## 🔗 Dependencies & Relationships

### Feeds Into
- _No downstream dependencies_

### Requires
- _No upstream dependencies_

---

## ⚠️ Intelligence Gaps

- All targets are pre-launch estimates
- Subscription UX conversion lift (15-20%) is industry directional, not IonWave-specific
- Headless/composable commerce intentionally excluded (premature for target operator)

---

## 🎯 Next Actions

_No next actions documented._


---

---

_Report generated: 2026-02-09 17:49:46_

_Source: `data\m9`_