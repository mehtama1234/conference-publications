# ADP License Reviewer Brief

Status: `ready_for_reviewer_evidence_check`

## Review Target

- Source repo: `Agent-Data-Protocol`
- Dataset: `AlienKevin_SWE-ZERO-12M-trajectories`
- Receipt: `dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`
- Requested reviewer role: `dataset_license_reviewer`

## Reviewer Decision Options

- `approved`
- `rejected`
- `needs_more_evidence`

## Evidence Summary

- Evidence files: `7`
- Evidence file hashes: `7`
- Missing evidence files: `0`
- Evidence manifest: `artifacts/conference-world-heavy-run-promotion-lane/adp-license-reviewer-evidence-manifest.json`
- Handoff packet: `artifacts/conference-world-heavy-run-promotion-lane/adp-license-reviewer-handoff-packet.json`
- Preflight: `artifacts/conference-world-heavy-run-promotion-lane/adp-license-reviewer-handoff-preflight.json`

## Evidence Files

| Evidence | SHA-256 |
| --- | --- |
| `/home/manishmehta/ui-projects/gyms/Agent-Data-Protocol/datasets/AlienKevin_SWE-ZERO-12M-trajectories/metadata.json` | `sha256:744d7215d007c1f92ebb59bcc38a949c7871ab17edfde229a2b8b5fdf07662a6` |
| `artifacts/conference-world-heavy-run-promotion-lane/adp-hosted-conversion-receipt-candidate.json` | `sha256:599a002f135f3cc040d33c2a02c40ff5c91c5fa0d44fb181654986e089b7d634` |
| `artifacts/conference-world-heavy-run-promotion-lane/adp-license-review-dossier.json` | `sha256:61bed0eb7c0dcd8c8e00c104265b82dab8d37daffa585615dfe8ae3498b1dbad` |
| `artifacts/conference-world-heavy-run-promotion-lane/adp-license-reviewer-decision-template.json` | `sha256:a7525434ca8e531bf70ba00b2c070c0d17fd4aa17a1cf7397d97720995681e8b` |
| `artifacts/conference-world-heavy-run-promotion-lane/adp-license-reviewer-handoff-packet.json` | `sha256:7779a92696228276c1ee398bc5d1e236520a2b6c17a8da1f02c3c997bedcc468` |
| `artifacts/conference-world-heavy-run-promotion-lane/adp-license-reviewer-handoff-preflight.json` | `sha256:3326a5b03783307a927bb429fa3965c45ac110f9d26725a96fdf12b09649422b` |
| `artifacts/conference-world-heavy-run-promotion-lane/adp-verifier-evidence-receipt.json` | `sha256:de0f52253d74cea2816816a4b0488a89ab9e264b0b563732434ae4c03d216320` |

## Checks To Perform

1. Confirm the dataset metadata and source terms support this governed validation lane.
2. Confirm the hosted conversion candidate identifies the dataset, inputs, hashes, and blocked export gates.
3. Confirm verifier evidence shows deterministic local fixture validation for this dataset.
4. Fill the decision template only after human review.
5. Run the handoff preflight before recording a decision receipt.

## Gate State

- Reviewer decision recorded: `false`
- Approval template mutation: `false`
- Approval entry write allowed: `false`
- Training export allowed: `false`
- Production allowed: `false`
- Current blocker: `actual_human_license_review_required`

This brief does not approve the dataset, record a reviewer decision, mutate the approval template, or authorize export, benchmark execution, or production promotion.
