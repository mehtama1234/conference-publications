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

## Verifier Evidence Receipt

- Done: executed `python3 scripts/check_sample_fixtures.py --dataset AlienKevin_SWE-ZERO-12M-trajectories` in `/home/manishmehta/ui-projects/gyms/Agent-Data-Protocol`.
- Output: `ok AlienKevin_SWE-ZERO-12M-trajectories`
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-verifier-evidence-receipt.json`
- Implementation commit: `mystuff@86988ba22` (`Record ADP verifier evidence receipt`)
- Current receipt status: `passed`
- Sample evidence: `3` raw rows, `3` ATIF rows, `3` STD rows
- Sample trace integrity: `passed`
- Hosted conversion completed: `false`
- Training export allowed: `false`
- Production allowed: `false`

## Approval Chain Review Packet

- Done: generated the ordered approval-chain review packet for `AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-approval-chain-review-packet.json`
- Implementation commit: `mystuff@e22d236e6` (`Add ADP approval chain review packet`)
- Current packet status: `ready_for_reviewer`
- Next review receipt: `dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`
- Next review status: `ready_for_review`
- Approved receipt count: `0`
- Blocked receipt count: `5`
- Training export allowed: `false`
- Production allowed: `false`

## License Approval Request Packet

- Done: generated the approval request packet for `dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-license-approval-request-packet.json`
- Implementation commit: `mystuff@f9f8648a7` (`Add ADP license approval request packet`)
- Current request status: `awaiting_reviewer_decision`
- Reviewer decision recorded: `false`
- Requested reviewer role: `dataset_license_reviewer`
- Training export allowed: `false`
- Production allowed: `false`

## License Review Dossier

- Done: generated a non-mutating reviewer dossier for `dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-license-review-dossier.json`
- Implementation/artifact commit: `mystuff@dc99f3fcc` (`Add ADP license review dossier`)
- BFF field: `adp_license_review_dossier`
- Runtime builder: `build_conference_world_adp_license_review_dossier`
- Dossier status: `ready_for_license_reviewer`
- Evidence checks: license metadata review, hosted conversion candidate review, verifier evidence review.
- Allowed reviewer decisions: `approved`, `rejected`, `needs_more_evidence`
- Reviewer decision recorded: `false`
- Template mutation: `false`
- Training export allowed: `false`
- Production allowed: `false`

## License Reviewer Decision Template

- Done: generated a fillable, non-mutating decision template for `dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-license-reviewer-decision-template.json`
- BFF field: `adp_license_reviewer_decision_template`
- Runtime builder: `build_conference_world_adp_license_reviewer_decision_template`
- Template status: `ready_for_reviewer_input`
- Decision receipt endpoint: `POST /api/conference-gyms/approval-decision-receipt`
- Decision receipt body fields: `approval_request_packet_ref`, `output_ref`, `reviewer_ref`, `approval_authority_ref`, `decision`, `reason`, `evidence_refs`
- Decision validation: `decision` must be one of the allowed decisions, `reason` must be non-empty, and `evidence_refs` must be a non-empty subset of the template review evidence refs.
- Required reviewer fields: `reviewer_ref`, `approval_authority_ref`, `decision`, `reason`, `evidence_refs`
- Allowed reviewer decisions: `approved`, `rejected`, `needs_more_evidence`
- Reviewer decision recorded: `false`
- Template mutation: `false`
- Approval entry write allowed: `false`
- Training export allowed: `false`
- Production allowed: `false`
- Current blocker: `actual_human_license_review_required`

## License Reviewer Handoff Packet

- Done: generated an operator handoff packet for the first ADP dataset license review.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-license-reviewer-handoff-packet.json`
- BFF field: `adp_license_reviewer_handoff_packet`
- Runtime builder: `build_conference_world_adp_license_reviewer_handoff_packet`
- Packet status: `ready_for_human_license_review`
- Includes: dossier ref, decision template ref, fillable decision request, evidence checks, pre-submit checks, and post-submit checks.
- Reviewer decision recorded: `false`
- Template mutation: `false`
- Approval entry write allowed: `false`
- Training export allowed: `false`
- Production allowed: `false`
- Current blocker: `actual_human_license_review_required`

## License Reviewer Handoff Preflight

- Done: added a non-mutating preflight validator for a filled license reviewer decision request.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-license-reviewer-handoff-preflight.json`
- BFF field: `adp_license_reviewer_handoff_preflight`
- BFF endpoint: `POST /api/conference-gyms/license-reviewer-handoff-preflight`
- Runtime builder: `build_conference_world_adp_license_reviewer_handoff_preflight`
- Default preflight status: `blocked`
- Current blockers: `reviewer_ref_missing`, `approval_authority_ref_missing`, `decision_not_allowed`, `decision_reason_missing`
- Would record decision receipt: `false`
- Would write decision receipt: `false`
- Would mutate approval template: `false`
- Training export allowed: `false`
- Production allowed: `false`
- Current blocker: `filled_reviewer_decision_request_not_ready`

## Reviewer Decision Receipt Path

- Done: added a reviewer decision receipt path for the license approval request.
- Implementation commit: `mystuff@e9dfa14d1` (`Add ADP approval decision receipt path`)
- BFF endpoint: `POST /api/conference-gyms/approval-decision-receipt`
- Runtime builder: `build_conference_world_adp_approval_decision_receipt`
- Supported decisions: `approved`, `rejected`, `needs_more_evidence`
- Template mutation: `false`
- Approval write still requires a separate preview/write action.
- Training export allowed: `false`
- Production allowed: `false`

## Approval Decision Apply Path

- Done: added a guarded apply path for an approved reviewer decision receipt.
- Implementation commit: `mystuff@14ee82cc7` (`Add ADP approval decision apply path`)
- BFF endpoint: `POST /api/conference-gyms/approval-decision-apply`
- Runtime builder: `build_conference_world_adp_apply_approval_decision_receipt`
- Applies decisions: only `decision_recorded` receipts whose decision is `approved`
- Rejected or incomplete decisions mutate template: `false`
- Apply path delegates to the existing approval-entry write validator and audit log.
- Test posture: temp approval template copies only; no real ADP approval template mutation.
- Training export allowed: `false`
- Production allowed: `false`

## Next Request After Apply Preview

- Done: added a non-mutating progression preview for the next reviewer request after one approved decision is applied to a temporary template copy.
- Implementation commit: `mystuff@9fd60ab7b` (`Preview ADP next approval request after apply`)
- BFF endpoint: `POST /api/conference-gyms/approval-next-request-after-apply-preview`
- Runtime builder: `build_conference_world_adp_next_request_after_apply_preview`
- Preview behavior: applies the approved decision only to a temporary approval template copy, then reuses the approval-chain and approval-request builders.
- Expected next receipt after the first license approval: `privacy_or_policy_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`
- Source approval template mutation: `false`
- Training export allowed: `false`
- Production allowed: `false`

## Privacy/Policy Evidence Candidate

- Done: added deterministic local sample scanning evidence for `privacy_or_policy_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-privacy-policy-evidence-candidate.json`
- Implementation commit: `mystuff@991401279` (`Add ADP privacy policy evidence candidate`)
- BFF field: `adp_privacy_policy_evidence_candidate`
- Runtime builder: `build_agent_data_protocol_privacy_policy_evidence_candidate`
- Scanned refs: metadata, sample raw, sample ATIF, and sample STD fixtures.
- Sample scan completed: `true`
- High-risk finding count: `0`
- Medium-risk finding count: `0`
- Current receipt status: `blocked`
- Privacy/policy approval recorded: `false`
- Training export allowed: `false`
- Production allowed: `false`

## Split Integrity Evidence Candidate

- Done: added local sample split integrity evidence for `split_integrity_manifest:AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-split-integrity-evidence-candidate.json`
- Implementation commit: `mystuff@ca068e813` (`Add ADP split integrity evidence candidate`)
- BFF field: `adp_split_integrity_evidence_candidate`
- Runtime builder: `build_agent_data_protocol_split_integrity_evidence_candidate`
- Sample row counts: raw `3`, ATIF `3`, STD `3`
- Sample row counts match: `true`
- Sample trace integrity: `passed`
- Full dataset split executed: `false`
- Current receipt status: `blocked`
- Split integrity approval recorded: `false`
- Training export allowed: `false`
- Production allowed: `false`

## Approval Evidence Bundle

- Done: added a durable evidence bundle that maps ADP approval receipt kinds to concrete artifact refs.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-approval-evidence-bundle.json`
- Implementation commit: `mystuff@ea6349748` (`Attach ADP quality evidence to training export review`)
- BFF field: `adp_approval_evidence_bundle`
- Runtime builder: `build_agent_data_protocol_approval_evidence_bundle`
- Bundle status: `ready_for_approval_chain`
- Evidence mapped for: dataset license, privacy/policy, split integrity, hosted conversion, and training export receipts.
- Training export review evidence now includes `adp-quality-assessment-evidence-candidate.json`.
- Approval receipts approved: `false`
- Training export allowed: `false`
- Production allowed: `false`

## Approval Chain Evidence Refresh

- Done: refreshed `adp-approval-chain-review-packet.json` from `adp-approval-evidence-bundle.json`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-approval-chain-review-packet.json`
- Implementation/artifact commit: `mystuff@ea6349748` (`Attach ADP quality evidence to training export review`)
- Privacy/policy evidence now cites `adp-privacy-policy-evidence-candidate.json`.
- Split integrity evidence now cites `adp-split-integrity-evidence-candidate.json`.
- Hosted conversion evidence now also cites `adp-split-integrity-evidence-candidate.json`.
- Training export evidence now cites hosted conversion, verifier, privacy/policy, split integrity, and quality assessment evidence.
- Current next reviewer receipt remains `dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`.
- Training export allowed: `false`
- Production allowed: `false`

## Quality Assessment Evidence Candidate

- Done: added deterministic local sample quality assessment evidence for `AlienKevin_SWE-ZERO-12M-trajectories`.
- Snapshot artifact: `docs/conference-gyms/2026-assessment/adp-quality-assessment-evidence-candidate.json`
- Implementation/artifact commit: `mystuff@acb9d9657` (`Correct ADP quality expectation totals`)
- BFF field: `adp_quality_assessment_evidence_candidate`
- Runtime builder: `build_agent_data_protocol_quality_assessment_evidence_candidate`
- Sample row counts: raw `3`, ATIF `3`, STD `3`
- Sample row counts match: `true`
- Sample trace integrity: `passed`
- Quality finding: sample metadata expectations pass using ADP's total-based checks: STD steps `43 >= 35`, STD tool calls `35 >= 30`, and SDK messages `78 >= 70`.
- Current receipt status: `blocked`
- Benchmark execution allowed: `false`
- Training export allowed: `false`
- Production allowed: `false`

## Acceptance Gates

- `python3 -m json.tool docs/conference-gyms/2026-assessment/conference-world-adapter-readiness.json`
- `python3 -m json.tool docs/conference-gyms/2026-assessment/agent-data-protocol-approval-overrides.template.json`
- AIDF unit tests for `conference_world_heavy_run_promotion_lane.py`
- BFF tests for conference-gym workbench readback and approval entry write
- Web-prod test showing the ADP lane remains blocked with `280` blocked receipts before review

## Next Move

Fill the non-mutating license reviewer decision template after actual human review, then record the decision through `POST /api/conference-gyms/approval-decision-receipt`. If approved, apply only that recorded license decision through `POST /api/conference-gyms/approval-decision-apply`, then use `adp-approval-evidence-bundle.json` to drive the next governed reviewer requests as the approval chain advances.
