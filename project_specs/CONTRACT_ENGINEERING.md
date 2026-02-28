# Contract Engineering: Bilateral TUPs and the Contract Stack

**Version**: 1.0.0
**Author**: Danilo (essay), Caio + Claude (integration notes)
**Date Created**: 2026-02-17
**Last Updated**: 2026-02-17
**AI Model**: claude-opus-4-20250514
**Purpose**: Reference document for Danilo's contract engineering essay and its relationship to Studio 3 system architecture
**Status**: Active
**Source**: Danilo's essay on contract engineering (February 2026)
**Related**: Systems_Architecture_Standards.md, INTEGRATION_DESIGN_PRINCIPLES.md, M39 theoretical_foundations.md

---

## Source Essay: Core Argument

Danilo's essay introduces **contract engineering** — the practice of making every business boundary legible by designing bilateral commitments (structured as TUPs) at each one.

### Key Moves

1. **Every relationship is a boundary** — between company and customer, employee, investor, advisor, deployer, vendor, co-founder. Each boundary has obligations flowing in both directions.

2. **A contract makes a boundary legible** — not a legal contract, but a structural one. A defined commitment from both sides: what each party delivers, receives, quality standard, timeline, and consequences for non-delivery.

3. **Most boundaries are illegible** — commitments are implicit, scattered across multiple documents, asymmetric, and buried. Nobody designed the boundary as a single coherent bilateral contract. They accreted policies and hoped the pile would add up.

4. **The TUP is the universal unit of contract engineering** — any bilateral commitment structured clearly enough that both sides can read it, hold each other to it, and know when it's been met or violated.

5. **The contract stack** — every business is a stack of bilateral TUPs. The stack of TUPs is the complete contractual architecture of the business. TUPs chain: customer TUP obligations become employee TUP deliverables, which become deployer TUP standards, which become investor TUP milestones.

6. **The customer TUP as product** — a visible, readable bilateral commitment at point of purchase replaces reviews and social proof as the trust signal. The contract IS the proof of trustworthiness.

---

## TUP Types Introduced

| TUP Type | Boundary | Company Commits To | Other Party Commits To |
|----------|----------|-------------------|----------------------|
| **Customer TUP** | Company ↔ Customer | Product spec, shipping SLA, quality standard, refund/replacement policy | Payment, accurate info, return conditions |
| **Employee TUP** | Company ↔ Employee | Role scope, compensation, success criteria, review cadence, consequence structure | Output quality, availability, professional conduct, knowledge transfer |
| **Investor TUP** | Founder ↔ Investor | Capital allocation (specific milestones), reporting cadence, decision-making structure | Capital, participation commitment, non-interference scope, follow-on framework |
| **Oracle TUP** | Project ↔ Advisor | Briefing materials, bounded queries, evaluation process | Introductions, vision input, credibility signaling |
| **Deployer TUP** | Client ↔ Deployer | Inputs, access, timely feedback, payment | Defined content types, SLAs per content type, grading, penalties |

---

## Contract Stack Architecture

The essay describes TUPs as chaining — each TUP's outputs become another TUP's inputs:

```
Customer TUP (what we promise customers)
    ↓ creates obligations that...
Employee TUP (employee deliverables must support customer promises)
    ↓ creates obligations that...
Deployer TUP (external talent must meet standards supporting employee TUP)
    ↓ creates obligations that...
Investor TUP (milestones = aggregations of deployer + employee TUP completions)
```

**Stack coherence check**: Does every commitment in TUP A have a supporting commitment in TUP B? If not, the stack is broken.

**Example of broken stack**: Customer TUP promises same-day replacement, but Employee TUP doesn't include inventory management as a deliverable. Structural gap — no amount of hustle fixes it.

---

## Relationship to Existing System Architecture

### Direct Connections

| Essay Concept | Existing Element | Nature of Connection |
|---|---|---|
| Bilateral TUP | TUP (glossary, manifest.json) | **Expansion** — current TUPs are knowledge containers; essay redefines as bilateral commitment units |
| Boundaries | Alexander Property 2 (M39) | **Convergence** — M39 already defines boundaries as operational primitive |
| Contract Stack chaining | `feeds_into` in manifest.json | **Structural parallel** — dependency chains already model TUP-to-TUP connections |
| Legibility | Bohm's Implicate/Explicate (M39) | **Same move** — making implicit commitments explicit = unfolding implicate order |
| Coordination infrastructure | Integration Design Principles | **Same goal** — high-phi architecture = legible contract stack |
| Oracle TUP | Venture Partner role (glossary) | **Formalization** — VP/advisor role exists; essay gives it TUP structure |

### What's Genuinely New

- **Bilaterality as formal property** — current TUPs are one-directional knowledge containers. Essay adds the second direction: what the OTHER party commits to.
- **Contract Stack as system concept** — the full set of bilateral TUPs as coordination architecture.
- **Customer TUP at point of purchase** — no current IonWave deliverable captures this.
- **Stack coherence checking** — does promise to customer X have supporting commitment from employee Y?
- **Consequence structure** — each TUP specifies what happens when either side doesn't deliver.

### What Was Already Latent

- Operator Management Overview already describes bilateral operator-Studio relationship (equity, vesting, milestones) — but not as a formal TUP.
- M39 boundaries (Alexander Property 2) already identifies boundary definition as operational practice.
- Dependency chains in manifest.json already model TUP-to-TUP chaining.

---

## Integration Notes

### Ontological Primitive Candidate

The essay's core concept — the **Bilateral Contract** — is a candidate for the 13th ontological primitive in Systems_Architecture_Standards.md. See that document for the formal primitive definition.

### Operationalization Questions (Open)

1. **What does a bilateral TUP look like as an artifact?** Is it a document? A structured data object? A dashboard view? Generated by Claude?
2. **Who writes it?** Does each party draft their side? Does the system generate it from existing commitments?
3. **Where does it live?** In the passet? As a separate contract registry? Embedded in existing TUPs?
4. **How is it enforced?** Manual review? Automated triggers (controller-like)? Smart contract parallels?
5. **How does it evolve?** Temporal boundary — when is each bilateral TUP reviewed, renewed, or retired?
6. **Customer-facing version**: How does the customer TUP get surfaced at checkout? UX implications.

---

## Version History

**v1.0.0 (2026-02-17)**:
- Initial registration of Danilo's contract engineering essay as project reference
- Mapped connections to existing system architecture
- Identified genuinely new vs. latent concepts
- Opened operationalization questions for discussion
