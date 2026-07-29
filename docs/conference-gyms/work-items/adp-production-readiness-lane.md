# Agent-Data-Protocol Production-Readiness Lane

Status: `in_progress`

## Goal

Turn `Agent-Data-Protocol` into the first production-grade AIDF conference-world lane:

`local conference repo assessment -> AIDF world package -> hosted/full dataset conversion -> validated traces -> dataset-level approvals -> verifier/readiness receipts -> durable web-prod readback`

Training export stays fail-closed until every required dataset receipt is explicitly approved.

## Current State

- Snapshot source: `docs/conference-gyms/2026-assessment/conference-world-adapter-readiness.json`
- Approval template: `docs/conference-gyms/2026-assessment/agent-data-protocol-approval-overrides.template.json`
- Local source repo: `/home/manishmehta/ui-projects/gyms/Agent-Data-Protocol`
- Selected lane: `Agent-Data-Protocol`
- Runtime family: `raw_atif_standard_sft_conversion_adapter`
- Dataset count: `56`
- Required dataset approval receipts: `280`
- Approved dataset approval receipts: `0`
- Blocked dataset approval receipts: `280`
- Current heavy-run receipt count: `1`
- Production allowed: `false`
- Promotion allowed: `false`
- Training export allowed: `false`

## Existing AIDF Seams

- BFF route: `/home/manishmehta/ui-projects/mystuff/bff/routes/conference_gyms.py`
- BFF readback service: `/home/manishmehta/ui-projects/mystuff/bff/services/conference_gym_workbench_readback.py`
- ADP approval validation/write module: `/home/manishmehta/ui-projects/mystuff/packages/aidf-source-intake-runtime/src/aidf_source_intake_runtime/conference_world_heavy_run_promotion_lane.py`
- Web fixture readback: `/home/manishmehta/ui-projects/mystuff/apps/web-prod/public/fixtures/conference-gyms/`
- Heavy-run lane artifacts: `/home/manishmehta/ui-projects/mystuff/artifacts/conference-world-heavy-run-promotion-lane/`

## Production Definition Of Done

1. Ingest all `56` ADP dataset rows into a durable approval matrix, not only the `3` sampled operator-packet rows.
2. Persist reviewer decisions for all five required receipt kinds per dataset:
   `dataset_license_review_approval`, `privacy_or_policy_review_approval`, `split_integrity_manifest`, `hosted_dataset_conversion_receipt`, and `training_export_approval`.
3. Keep `training_export_allowed=false` unless each dataset has license, privacy/policy, split integrity, hosted conversion, and training export approval receipts.
4. Run hosted/full dataset conversion evidence for at least one governed ADP dataset before claiming heavy-run readiness.
5. Emit deterministic validation receipts for schema, provenance, conversion manifest, sample trace integrity, and verifier output.
6. Surface the same lane state through BFF/web-prod readback, including blocked receipt counts and the next actionable blocker.
7. Preserve production and promotion gates as `false` until reviewer approvals and heavy-run validation receipts are complete.

## First Engineering Slice

Build the durable ADP approval matrix readback:

- Done: parse every dataset decision from `agent-data-protocol-approval-overrides.template.json`.
- Done: return all `56` dataset rows through the conference-gym BFF readback.
- Done: show rollups for approved, blocked, stage, receipt-kind, and next-blocker counts.
- Existing: approval writes append an audit row and revalidate the full template after each write.
- Done: tests prove incomplete approvals block export and out-of-order training export approval is rejected.

Implementation commit: `mystuff@27d5ba7f7` (`Expose full ADP approval matrix readback`)

Current implementation evidence:

- Runtime builder: `build_conference_world_adp_approval_matrix_readback`
- BFF field: `adp_approval_matrix`
- Real `/gyms` template readback: `56` dataset rows, `280` approval receipt rows, `0` approved, `280` blocked, `training_export_allowed=false`

## Hosted Conversion Receipt Candidate

- Done: generated the first governed ADP hosted-conversion receipt candidate for `AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-hosted-conversion-receipt-candidate.json`
- Implementation commit: `mystuff@0a9b0cce3` (`Add ADP hosted conversion receipt candidate`)
- Evidence captured: conversion manifest, schema refs, sample row counts, sample trace identity integrity, source/provenance hashes, verifier command.
- Current receipt status: `blocked`
- Hosted conversion completed: `false`
- Training export allowed: `false`
- Production allowed: `false`

## Acceptance Gates

- `python3 -m json.tool docs/conference-gyms/2026-assessment/conference-world-adapter-readiness.json`
- `python3 -m json.tool docs/conference-gyms/2026-assessment/agent-data-protocol-approval-overrides.template.json`
- AIDF unit tests for `conference_world_heavy_run_promotion_lane.py`
- BFF tests for conference-gym workbench readback and approval entry write
- Web-prod test showing the ADP lane remains blocked with `280` blocked receipts before review

## Next Move

Execute the ADP verifier command for the selected dataset and attach the verifier output as reviewed evidence; then begin the ordered dataset approval chain without approving training export.
