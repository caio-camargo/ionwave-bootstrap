# TUP Enhanced Visualization Protocol (TEVP-001)

**Version**: 1.0.0
**Type**: Reporting Protocol
**Author**: Caio + Claude
**Date Created**: 2026-02-09
**Purpose**: Standard format for creating rich, context-heavy, human-readable TUP visualizations for operator review and execution
**Status**: Active

---

## Overview

The standard TUP aggregation (nested bullet lists from JSON) is comprehensive but lacks **context, reasoning, and actionability**. This protocol defines an enhanced visualization format that includes:

1. **Strategic reasoning** behind decisions
2. **Evidence grading** for each claim
3. **Visual diagrams** where helpful
4. **Cross-TUP dependencies** with conflict scenarios
5. **Risk tables** with mitigations
6. **Testing gates** and checklists
7. **Invalidation scenarios** (what would prove this wrong)
8. **Dialogue insights** from expert persona workshops

**Use this format when:**
- Creating operator review documents
- Documenting critical decisions for execution
- Preparing TUP content for stakeholder sharing
- Building implementation guides from TUP data

---

## Template Structure

### Section 1: Strategic Context (REQUIRED)

```markdown
## [TUP Section Name]

### Strategic Decision: [Decision Name]

**Hypothesis Tested:** HYP-XXX ([hypothesis name])
**Current Grade:** [A/B/C/D] ([reasoning for grade])
**Severity:** [CRITICAL/HIGH/MEDIUM/LOW] ([impact on business])

**Core Thesis:**
[1-3 sentence explanation of WHY this decision matters and what it enables/prevents]
```

**Purpose:** Anchors the reader immediately. They understand what's being decided, what it's testing, and why it matters.

**Example:**
```markdown
**Core Thesis:**
Subscribers deliver 6x LTV vs one-time buyers ($159 vs $26, per M21). Subscription revenue creates predictable cash flow and reduces reliance on paid acquisition. The product page must be architected to make subscription the default purchase path, not an afterthought.
```

---

### Section 2: Visual/Diagram (WHEN APPLICABLE)

Use ASCII diagrams, tables, or visual representations when:
- Illustrating a user flow or interface pattern
- Showing data comparisons
- Mapping a process or decision tree

**Example: Product Page Widget**
```
┌─────────────────────────────────────────────────────┐
│  ✓ Subscribe & Save 15%         $41.65/mo           │  ← PRE-SELECTED
│    Delivered every 30 days                           │
│    [30 days ▼] [45 days] [60 days]                  │
│                                                       │
│  ○ One-time purchase             $49.00              │  ← Secondary
└─────────────────────────────────────────────────────┘
```

**Guidelines:**
- Keep diagrams simple (ASCII works better than embedded images for markdown)
- Annotate with arrows/labels to highlight key elements
- Include inline reasoning annotations (← PRE-SELECTED)

---

### Section 3: Evidence-Backed Rules/Principles (REQUIRED FOR KEY DECISIONS)

For each major rule or principle, document:

```markdown
### Rule [N]: [Rule Name]

**Reasoning:** [Why this rule exists - behavioral/economic/strategic basis]

**Evidence:** [Source of the rule - studies, merchant data, theory]

**Grade:** [A/B/C/D] ([quality of evidence])

**Impact:** [Quantified impact if available, or qualitative]

**Caveat:** [Exceptions, limitations, or conditions where rule doesn't apply]
```

**Example:**
```markdown
### Rule 2: Toggle NOT dropdown

**Reasoning:** Toggles reduce cognitive load for binary choices. Dropdown adds friction (extra click + decision paralysis).

**Evidence:** Recharge/Skio merchant comparison data (2023-2024)

**Grade:** C (merchant-reported, not controlled study)

**Impact:** 15-20% higher conversion than dropdown (reported range)

**Caveat:** Effect diminishes if >2 frequency options. If adding 4+ frequencies, dropdown becomes necessary.
```

---

### Section 4: Alternatives Considered (REQUIRED FOR STRATEGIC DECISIONS)

```markdown
## Why This Pattern (vs Alternatives)

### Alternative 1: [Alternative Name]
❌ **Rejected.** [Reason + evidence]

### Alternative 2: [Alternative Name]
❌ **Rejected.** [Reason + evidence]

### Alternative 3: [Alternative Name]
✅ **Selected.** [Why this was chosen]
```

**Purpose:** Shows decision was considered carefully. Documents why other paths weren't taken (prevents re-litigating later).

---

### Section 5: Implementation Checklist (REQUIRED FOR EXECUTABLE CONTENT)

```markdown
## Implementation Checklist

### Platform/Tool Decision: [Tool Name]

**Why [Tool] over [Alternatives]:**
- ✅ [Reason 1]
- ✅ [Reason 2]
- ⚠️ **INTELLIGENCE GAP:** [Known unknowns]

### Configuration:

| Setting | Value | Reasoning |
|---------|-------|-----------|
| [Setting 1] | [Value] | [Why this value] |
| [Setting 2] | [Value] | [Why this value] |

**Reasoning on [Key Setting]:**
[Detailed explanation if needed]
```

**Purpose:** Operator can execute directly from this document. No guessing about settings or values.

---

### Section 6: Legal/Compliance (WHEN APPLICABLE)

```markdown
## Legal & Compliance Requirements

### [Domain]-specific disclosure ([Regulator]):
- ✅ [Requirement 1]
- ✅ [Requirement 2]

**Why this matters:**
[Consequences of non-compliance, with examples if possible]

**Reference:** [Link to compliance TUP or external resource]
```

**Example:**
```markdown
**Why this matters:**
FTC sued multiple supplement subscription brands 2022-2024 for "dark patterns" (hiding cancellation, unclear auto-renewal). Compliance is existential, not nice-to-have.
```

---

### Section 7: Success Metrics & Kill Criteria (REQUIRED)

```markdown
## Success Metrics & Kill Criteria

| Metric | Target | Floor (Yellow) | Kill (Red) | Source |
|--------|--------|----------------|------------|---------|
| [Metric 1] | [Target] | [Warning level] | [Kill threshold] | [TUP/HYP reference] |

### Interpretation:

**[Condition]** → [What it means and what to do]

**[Condition]** → [What it means and what to do]
```

**Purpose:** Clear thresholds prevent ambiguity. Operator knows exactly when to escalate/pivot/kill.

**Example:**
```markdown
**<35% attach rate after 100 orders** → Funnel broken. Check: (1) Is one-time pre-selected by mistake? (2) Discount too low? (3) Subscription messaging unclear?

**<30% attach rate** → Existential. Subscriber LTV assumption ($159) collapses. Revisit unit economics (M3).
```

---

### Section 8: Integration Points (REQUIRED)

```markdown
## Integration Points (Cross-TUP Dependencies)

### Feeds into:
- **[TUP ID] ([TUP Name])** → [What this TUP provides to that one]

### Depends on:
- **[TUP ID] ([TUP Name])** → [What this TUP needs from that one]

### Conflict if:
- [Scenario] → [What breaks]
```

**Purpose:** Makes dependencies explicit. Prevents breaking changes across TUPs.

---

### Section 9: Risks & Mitigations (REQUIRED FOR HIGH-IMPACT DECISIONS)

```markdown
## Known Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| **[Risk 1]** | [L/M/H] | [L/M/H/CRIT] | [How to prevent/handle] | [TUP/Person] |

**Worst-case scenario:**
[What happens if everything goes wrong + recovery path]
```

**Purpose:** Risk-aware execution. Nothing is assumed to "just work."

---

### Section 10: Testing Protocol (FOR LAUNCH-BLOCKING ITEMS)

```markdown
## Testing Protocol (Pre-Launch Quality Gate)

**These tests are BLOCKING. Do not launch until all pass.**

- [ ] **[Test 1]** → [Pass criteria]
- [ ] **[Test 2]** → [Pass criteria]

**Launch rule:** [Escalation path if tests fail]
```

**Purpose:** Non-negotiable quality gates. Prevents shipping broken implementations.

---

### Section 11: Dialogue Insights (RECOMMENDED)

```markdown
## Dialogue Insights (From [TUP ID] Workshop)

### Key insight from [Persona Name]:
"[Direct quote or paraphrase of key insight]"

### Key insight from [Persona Name]:
"[Direct quote or paraphrase of key insight]"
```

**Purpose:** Captures emergent wisdom from persona dialogue. Often reveals non-obvious considerations.

---

### Section 12: Invalidation Scenarios (RECOMMENDED)

```markdown
## What Would Invalidate This Approach?

### Scenario 1: [Failure Condition]
→ [What it means]

**Action:** [What to do if this happens]

### Scenario 2: [Failure Condition]
→ [What it means]

**Action:** [What to do if this happens]
```

**Purpose:** Humility about assumptions. Defines when to pivot vs. persist.

**Example:**
```markdown
### Scenario 1: Attach rate <30% after 100 orders
→ Subscription-first funnel isn't working. Possible causes:
1. Product not subscription-worthy (doesn't create habit/routine)
2. Messaging unclear (customers don't understand subscription value)

**Action:** Run PT-002 (subscription discount 10% vs 15% vs 20%). If attach rate still <30%, consider whether marine plasma creates enough recurring value for subscription model.
```

---

### Section 13: Version History & Related Docs (REQUIRED)

```markdown
## Version History

| Version | Date | Change | Actor |
|---------|------|--------|-------|
| 1.0.0 | YYYY-MM-DD | [What changed] | [Who made it] |

## Related Documents

- **[TUP ID] ([TUP Name])** → [Relationship]
- **[TUP ID] ([TUP Name])** → [Relationship]
```

**Purpose:** Audit trail. Reader knows what version they're looking at and where to find related context.

---

## Section Prioritization

Not every section is required for every TUP visualization. Use this guide:

| Section | Always | High-Impact | Medium-Impact | Low-Impact |
|---------|--------|-------------|---------------|------------|
| 1. Strategic Context | ✅ | ✅ | ✅ | ✅ |
| 2. Visual/Diagram | When helpful | When helpful | When helpful | When helpful |
| 3. Evidence-Backed Rules | ✅ | ✅ | Optional | Optional |
| 4. Alternatives Considered | ✅ | ✅ | Optional | Skip |
| 5. Implementation Checklist | ✅ | ✅ | ✅ | Optional |
| 6. Legal/Compliance | When applicable | When applicable | When applicable | When applicable |
| 7. Success Metrics & Kill Criteria | ✅ | ✅ | ✅ | Optional |
| 8. Integration Points | ✅ | ✅ | ✅ | Optional |
| 9. Risks & Mitigations | ✅ | ✅ | Optional | Skip |
| 10. Testing Protocol | For launch items | For launch items | Optional | Skip |
| 11. Dialogue Insights | ✅ | Recommended | Optional | Skip |
| 12. Invalidation Scenarios | ✅ | Recommended | Optional | Skip |
| 13. Version History | ✅ | ✅ | ✅ | ✅ |

**High-Impact:** Decisions affecting hypotheses, unit economics, or launch-blocking items
**Medium-Impact:** Important but not existential (can be fixed post-launch)
**Low-Impact:** Nice-to-have, optimization-focused

---

## Output Formats

### Format 1: Markdown (Default)
- **File extension:** `.md`
- **Best for:** Internal review, GitHub/GitLab, version control
- **Tooling:** Can be converted to .docx, .pdf, or HTML

### Format 2: Google Docs (Operator Review)
- **Process:** Export markdown → copy-paste into Google Docs or use Pandoc
- **Best for:** Collaborative editing, commenting, stakeholder sharing
- **Trade-off:** Loses some formatting (ASCII diagrams render as monospace)

### Format 3: Notion/Confluence (Knowledge Base)
- **Process:** Import markdown directly
- **Best for:** Linking across documents, embedding in broader knowledge base

---

## Worked Example

**See:** `reports/M9_Subscription_Funnel_GoogleDocs_Ready.md`

This file demonstrates the protocol applied to M9's subscription funnel architecture. It includes:
- Strategic context (HYP-002 testing)
- Visual widget mockup (ASCII diagram)
- 5 evidence-backed UX rules
- 3 rejected alternatives
- Implementation checklist for Loop Subscriptions
- Legal/FTC compliance requirements
- Success metrics with kill criteria
- Cross-TUP integration points
- Risk/mitigation table
- Pre-launch testing protocol
- Dialogue insights from 3 personas
- 3 invalidation scenarios
- Version history

**Total length:** ~400 lines, ~12-15 pages in Google Docs

---

## When to Use This Protocol

### Use TEVP-001 for:
1. **Critical launch decisions** (subscription funnel, pricing, platform choices)
2. **High-risk implementations** (legal/compliance, payment processing, ad tracking)
3. **Cross-TUP orchestration** (when multiple TUPs must work together)
4. **Stakeholder communication** (investors, advisors need context, not just data)
5. **Operator execution guides** (Danilo needs to implement directly from doc)

### Don't use TEVP-001 for:
1. **Simple data lookups** (use standard TUP aggregation)
2. **Low-impact optimizations** (standard report format sufficient)
3. **Exploratory research** (too much structure slows down discovery)

---

## Quality Checklist

Before publishing an enhanced visualization, verify:

- [ ] **Strategic context** clearly states hypothesis, grade, and thesis
- [ ] **Evidence grading** is honest (don't inflate C to B)
- [ ] **Alternatives considered** shows decision was deliberate
- [ ] **Implementation checklist** is executable (operator can act on it)
- [ ] **Kill criteria** are unambiguous (no "feel it out" metrics)
- [ ] **Integration points** identify breaking changes
- [ ] **Risks** include worst-case scenario + recovery path
- [ ] **Testing protocol** is blocking (not aspirational)
- [ ] **Invalidation scenarios** define when to pivot
- [ ] **Version history** is up-to-date

---

## Relationship to Other Protocols

| Protocol | Relationship |
|----------|-------------|
| **TUP Workshop Protocol (TWP-001)** | TEVP-001 is an *output format* for TWP-001 Phase 11 deliverables |
| **TUP Report Generation Workflow** | Standard aggregation = raw content; TEVP-001 = enhanced content |
| **Constraint Scenario Protocol (CSP-001)** | Invalidation scenarios borrow from CSP methodology |

**Workflow:**
1. Run **TWP-001** to workshop a TUP → Produces JSON + MD files
2. Run **standard aggregation** to create comprehensive reference doc
3. Apply **TEVP-001** to critical sections → Produces enhanced visualization for operator

---

## Maintenance

**Update TEVP-001 when:**
- New section types emerge as consistently useful
- Feedback reveals missing critical elements
- Format changes needed for different output targets (PDF, etc.)

**Version history:**
| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-02-09 | Initial protocol. Codifies enhanced visualization format used in M9 Subscription Funnel example. |

---

## Related Documents

- `processes/TUP_Workshop_Protocol.md` - Parent protocol for TUP content creation
- `processes/TUP_Report_Generation_Workflow.md` - Standard aggregation format
- `reports/M9_Subscription_Funnel_GoogleDocs_Ready.md` - Worked example of TEVP-001
- `standards/Deliverable_Structure_Standards.md` - Overall quality standards

---

**Protocol Owner:** Caio
**Last Reviewed:** 2026-02-09
**Next Review:** After 3 enhanced visualizations created (validate protocol effectiveness)
