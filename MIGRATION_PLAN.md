# Folder Migration Plan - Three System Separation

**Date**: 2026-02-12
**Purpose**: Separate Imagination System, Implementation System, and Reusable Frameworks

---

## Target Structure

```
G:/Drives compartilhados/Studio 3/
├── ImagGen/                                    # REUSABLE SYSTEM (permanent)
│   ├── protocols/
│   ├── opkits/
│   │   ├── templates/
│   │   └── reference_models/
│   ├── standards/
│   ├── systems/
│   └── README.md
│
├── Trades/
│   └── 084_IonWave/
│       ├── Imagination/                        # STUDIO WORKSPACE
│       │   ├── workspace/
│       │   │   ├── data/
│       │   │   ├── analysis/
│       │   │   ├── tracking/
│       │   │   └── SESSION_LOG.md
│       │   ├── outputs/
│       │   │   ├── tup_content/
│       │   │   └── opkits/
│       │   └── meta/
│       │       ├── workshop_protocols/
│       │       ├── quality_assessments/
│       │       └── decisions/
│       └── Implementation/                     # OPERATOR RECEIVES
│           ├── strategic/
│           ├── product/
│           ├── growth/
│           ├── retention/
│           ├── operations/
│           ├── opkits/
│           └── OPERATOR_START_HERE.md
│
└── Archive/
    └── IonWave_Bootstrap_Pre_Migration/        # Current folder (backup)
```

---

## Migration Mapping

### TO: ImagGen/ (Reusable System)

| Current Location | Destination | Type | Notes |
|-----------------|-------------|------|-------|
| `processes/TUP_Workshop_Protocol.md` | `ImagGen/protocols/` | Workshop protocol | Core reusable protocol |
| `processes/JSON_Migration_Guide.md` | `ImagGen/protocols/` | Workshop protocol | |
| `processes/Dependency_Map.md` | `ImagGen/protocols/` | Reference | |
| `ci-protocol/` | `ImagGen/protocols/ci_protocol/` | Example protocol | Worked example of TWP |
| `standards/` | `ImagGen/standards/` | Standards | All quality standards |
| `systems/` | `ImagGen/systems/` | System docs | Ontological primitives |
| `core/02_Glossary.md` | `ImagGen/core/` | Core doc | |
| `core/03_What_We_Did.md` | `ImagGen/core/` | Core doc | |
| `core/04_Working_Principles_updated.md` | `ImagGen/core/` | Core doc | |
| `data/m14/` (scaffold only) | `ImagGen/opkits/templates/m14/` | Template | Generic scaffold |
| `data/m16/` (scaffold only) | `ImagGen/opkits/templates/m16/` | Template | |
| `data/m14/` (IonWave content) | `ImagGen/opkits/reference_models/ionwave/m14/` | Reference | Graded example |
| `data/opkits/registry.json` | `ImagGen/opkits/registry_template.json` | Template | Generic registry structure |

### TO: Trades/084_IonWave/Imagination/workspace/

| Current Location | Destination | Type | Notes |
|-----------------|-------------|------|-------|
| `data/` | `workspace/data/` | TUP data | All 41 TUPs |
| `IonWave/*.md` | `workspace/analysis/` | Analysis deliverables | Strategic analyses |
| `tracking/` | `workspace/tracking/` | Tracking logs | 42 TUP tracking files |
| `SESSION_LOG.md` | `workspace/SESSION_LOG.md` | Session history | |
| `ACTIVE_WORK.md` | `workspace/ACTIVE_WORK.md` | Coordination | |

### TO: Trades/084_IonWave/Imagination/meta/

| Current Location | Destination | Type | Notes |
|-----------------|-------------|------|-------|
| `protocols/` | `meta/workshop_protocols/` | Workshop decisions | CSP-001, case studies |
| `tracking/Reconciliation_Decision_Log.md` | `meta/decisions/` | Decisions | |
| `tracking/Open_Questions.md` | `meta/decisions/` | Decisions | |
| `data/hypotheses/validation_log.json` | `meta/quality_assessments/` | Validation | |
| `data/*/dialogue_summary.md` | `meta/quality_assessments/` | Dialogue logs | All persona dialogue summaries |

### TO: Trades/084_IonWave/Implementation/

| Current Location | Destination | Type | Notes |
|-----------------|-------------|------|-------|
| `data/m0_trade_thesis/` | `strategic/m0_trade_thesis/` | Strategic content | |
| `data/m26_competitive_intel/` | `strategic/m26_competitive_intel/` | Strategic content | |
| `data/m27_customer_research/` | `strategic/m27_customer_research/` | Strategic content | |
| `data/m5_formulation/` | `product/m5_formulation/` | Product content | BCL-1 |
| `data/m6/` | `product/m6_supply_chain/` | Product content | BCL-1 |
| `data/m7/` | `product/m7_regulatory/` | Product content | BCL-1 |
| `data/m8/` | `product/m8_brand_identity/` | Product content | BCL-1 |
| `data/m13/` | `growth/m13_media_buying/` | Growth content | BCL-5 |
| `data/m14/` | `growth/m14_testing/` | Growth content | BCL-3 |
| `data/m16/` | `growth/m16_content_seo/` | Growth content | BCL-5 |
| (Continue for all 41 TUPs...) | | | |

### ARCHIVE: IonWave_Bootstrap_Pre_Migration/

| Current Location | Action | Notes |
|-----------------|--------|-------|
| Entire current folder | Copy to Archive/ | Complete backup before migration |

---

## Files to Create

### New Files for ImagGen/

1. `ImagGen/README.md` - How to start a new Trade Imagination session
2. `ImagGen/protocols/index.json` - Protocol registry
3. `ImagGen/opkits/README.md` - How to use OpKits
4. `ImagGen/SYSTEM_ARCHITECTURE.md` - Overview of the Imagination system

### New Files for Trades/084_IonWave/

1. `Imagination/_passet_meta.json` - Passet metadata
2. `Imagination/README.md` - Studio workspace guide
3. `Imagination/outputs/EXTRACTION_GUIDE.md` - How to extract for Implementation
4. `Implementation/OPERATOR_START_HERE.md` - Operator entry point
5. `Implementation/_passet_meta.json` - Passet metadata

---

## Migration Execution Order

1. **Create backup** - Copy entire current folder to Archive/
2. **Create new directories** - ImagGen/, Trades/084_IonWave/
3. **Extract reusable system** - Populate ImagGen/
4. **Restructure workspace** - Populate Imagination/workspace/
5. **Extract meta** - Populate Imagination/meta/
6. **Prepare implementation** - Populate Implementation/ (organized by BCL)
7. **Create new entry points** - README files
8. **Validate migration** - Check all files moved correctly
9. **Update git** - Stage changes, commit migration

---

## Validation Checklist

- [ ] ImagGen/ contains ONLY reusable components (no IonWave-specific content except in reference_models/)
- [ ] Imagination/workspace/ contains ALL working files (data, tracking, session logs)
- [ ] Imagination/meta/ contains ONLY studio-facing documentation (not shown to Operator)
- [ ] Implementation/ contains ONLY clean deliverables (no workshop artifacts)
- [ ] Can lift ImagGen/ → new Trade folder and start fresh
- [ ] Operator can read Implementation/ without seeing workshop process
- [ ] All files accounted for (nothing lost in migration)

---

## Rollback Plan

If migration fails:
1. Delete new directories (ImagGen/, Trades/)
2. Copy Archive/IonWave_Bootstrap_Pre_Migration/ back to working location
3. Resume from current structure
