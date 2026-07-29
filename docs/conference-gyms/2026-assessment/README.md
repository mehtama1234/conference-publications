# Conference Gym 2026 Assessment Snapshot

This directory preserves the production-readiness assessment for the local
conference gym workspace at `/home/manishmehta/ui-projects/gyms`.

The full local workspace is a multi-gigabyte collection of cloned benchmark and
environment repos, so this repo stores the durable assessment artifacts and a
manifest of the local source checkouts rather than vendoring every repo.

## Contents

- `CONFERENCE_WORLD_ANALYSIS.md` - ICML/ICLR world inventory, adapter coverage,
  roadmap, and cross-repo patterns.
- `WORLD_ANATOMY_MAP.md` - implementation-facing state/action/observation,
  verifier, runtime, and AIDF mapping notes.
- `AIDF_WORLD_IMPLEMENTATION_GAPS.md` - platform work implied by the assessment.
- `NEXT_CONFERENCE_WORLD_GOAL.md` - recommended next production-readiness goal.
- `WORLD_PACKAGE_INVENTORY.yaml` - structured world-package projection inventory.
- `conference-world-adapter-readiness.json` - machine-readable readiness rollup.
- `agent-data-protocol-approval-overrides.template.json` - ADP approval override
  template with dataset-level receipt entries.
- `adp-quality-assessment-evidence-candidate.json` - local sample quality
  assessment for the first governed ADP dataset; benchmark/export/production
  gates remain blocked.
- `adp-license-review-dossier.json` - non-mutating reviewer dossier for the
  first ADP dataset license approval request.
- `adp-license-reviewer-decision-template.json` - fillable reviewer decision
  template for the first ADP license approval request; it records no decision
  and keeps export/production gates blocked.
- `adp-license-reviewer-handoff-packet.json` - operator handoff packet that
  bundles the dossier, decision template, evidence checks, and submit-time
  guardrails for the first ADP license review.
- `adp-license-reviewer-handoff-preflight.json` - blocked preflight validation
  of the blank reviewer handoff request; it records no decision and writes no
  approval receipt.
- `adp-license-reviewer-evidence-manifest.json` - hash manifest for the first
  ADP license reviewer handoff evidence set; all referenced files are present.
- `adp-license-reviewer-brief.md` - human-readable license reviewer brief for
  the first ADP dataset; summarizes decision options, evidence hashes, and
  closed gates.
- `LOCAL_GYM_REPO_MANIFEST.json` / `.md` - local cloned repo names, remotes,
  commits, branches, and dirty state at snapshot time.
- `source-workspace-README.md` - README copied from the local gym workspace.

## Current Readiness Summary

- 33 local world-package projections.
- 66 adapter/readiness artifacts.
- 0 projection errors.
- 8 runtime adapter families covered.
- 14 source-specific no-heavy adapter smokes.
- 1 first heavy-run receipt candidate: `Agent-Data-Protocol`.
- 56 ADP datasets with 280 dataset-level approval receipts.
- 280 approval receipts remain blocked.
- Production and promotion remain blocked.

## Next Meaty Goal

Make one conference world family production-grade end to end. The recommended
first lane is `Agent-Data-Protocol`: clear or explicitly reject dataset-level
approvals, run hosted/full conversion, persist validation and export decisions,
and wire durable readback into the AIDF gym workbench.
