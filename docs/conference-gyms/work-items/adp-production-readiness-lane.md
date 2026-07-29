# Agent-Data-Protocol Production-Readiness Lane

Status: `proposed_first_meaty_goal`

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

- Parse every dataset decision from `agent-data-protocol-approval-overrides.template.json`.
- Return all `56` dataset rows through the conference-gym BFF readback, with filtering/pagination if needed.
- Show rollups for approved, blocked, invalid, and next-blocker counts.
- Add a write path that appends an audit row for each approval override and revalidates the full template after each write.
- Add tests proving incomplete approvals block export and out-of-order training export approval is rejected.

## Acceptance Gates

- `python3 -m json.tool docs/conference-gyms/2026-assessment/conference-world-adapter-readiness.json`
- `python3 -m json.tool docs/conference-gyms/2026-assessment/agent-data-protocol-approval-overrides.template.json`
- AIDF unit tests for `conference_world_heavy_run_promotion_lane.py`
- BFF tests for conference-gym workbench readback and approval entry write
- Web-prod test showing the ADP lane remains blocked with `280` blocked receipts before review

## Next Move

Implement the full `56`-dataset approval matrix readback in `mystuff`, then regenerate and copy the updated ADP lane artifacts into this conference repo snapshot.
