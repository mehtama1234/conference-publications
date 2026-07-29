# Next Conference World Goal

## Current State

The current readiness report has:

- 66 adapter artifacts.
- 33 local world-package projections.
- 8 runtime adapter families.
- Complete family contract-smoke coverage.
- 17 source-specific package projections.
- 14 source-specific no-heavy-run adapter smokes: `OpenApps`,
  `Agent-Data-Protocol`, `TerminalTraj`, `Gaia2-ARE`, `Swing-Bench`,
  `AlgoVeri`, `SimuHome`, `UI-Venus-VenusBench-Mobile`, `MC-Search`,
  `ScaleCUA`, `CyberGym`, `BIRD-Interact`, `VERINA`, `RealPDEBench`.
- 14 evidence/gate receipts for the same source-specific bridges.
- 1 first heavy-run receipt candidate for `Agent-Data-Protocol`.
- 1 policy/export decision receipt for `Agent-Data-Protocol`.
- 1 dataset review matrix for `Agent-Data-Protocol`.
- 1 dataset approval receipt-template set for `Agent-Data-Protocol`.
- 1 generated ADP approval override template with 280 editable receipt entries.
- 16 inventory projections that still need source-specific runtime wiring.
- 0 projection errors.

Every runtime adapter family now has a first concrete source-specific bridge:

- `OpenApps`: browser GUI.
- `Agent-Data-Protocol`: trajectory/data.
- `MC-Search`: second trajectory/data bridge.
- `ScaleCUA`: second browser/GUI bridge and first cross-platform CUA bridge.
- `CyberGym`: second terminal/sandbox bridge.
- `BIRD-Interact`: second external environment/user-database loop bridge.
- `VERINA`: second formal-proof bridge.
- `RealPDEBench`: second scientific simulator bridge.
- `TerminalTraj`: terminal/sandbox.
- `Gaia2-ARE`: external environment loop.
- `Swing-Bench`: repository/CI.
- `AlgoVeri`: formal proof.
- `SimuHome`: scientific/device simulator.
- `UI-Venus-VenusBench-Mobile`: mobile GUI/emulator.

`Agent-Data-Protocol` is now the selected first heavy-run lane. The receipt is
partially cleared: local fixture/schema validation passed with 289 checks in the
temporary `litellm` execution environment. The policy/export decision receipt
allows local fixture evidence for adapter contract validation only. It is still
blocked for hosted dataset conversion, downstream reuse, SFT export, and broader
training export until license/privacy/split/training-export approvals exist.
The dataset review matrix now repeats that status per ADP dataset, so the next
approval work has explicit rows to clear instead of one global statement. The
approval receipt-template set now creates the blocked receipts that each row
must complete, and the generated override template is the file reviewers can
edit and feed back into the CLI.

The ADP lane now also has governed approval-chain artifacts for the first
dataset, `AlienKevin_SWE-ZERO-12M-trajectories`:

- hosted conversion receipt candidate
- verifier evidence receipt
- privacy/policy evidence candidate
- split integrity evidence candidate
- approval evidence bundle
- refreshed approval-chain review packet
- license approval request packet
- reviewer decision receipt path
- guarded approval decision apply path
- next-request-after-apply preview path

The current tracked implementation head for this lane is `mystuff@6a85112d4`
(`Refresh ADP approval chain evidence refs`). The current conference tracking
head is `conference-publications@0cec949` (`Record ADP approval chain evidence
refresh`).

## Next Goal

The next concrete goal is:

> Make `Agent-Data-Protocol` the first production-grade AIDF conference gym lane
> end to end: raw corpus assessment -> canonical AIDF gym package -> governed
> hosted/full conversion -> deterministic verifier evidence -> real approval
> chain -> agent benchmark run -> durable workbench/readback report.

In simple words, the inventory phase proved that AIDF can describe conference
gym worlds. The production phase should prove that one lane can survive the
whole operational path without fake approvals, local-only state, or benchmark
claims that outrun evidence.

## What To Do Next

### 1. Drive The Real ADP Approval Chain

Current observed status:

- local ADP validation passed: 289 checks, 0 failures
- `litellm` is available in the temp execution venv used for the receipt
- training export remains blocked until license, privacy, split-integrity, and
  export approvals are recorded
- local fixture evidence is allowed only for adapter contract validation
- dataset review rows exist for ADP local fixtures
- blocked approval receipt templates exist for each ADP dataset
- a generated override template exists at
  `agent-data-protocol-approval-overrides.template.json`
- evidence bundle exists at `adp-approval-evidence-bundle.json`
- approval-chain review packet exists at
  `adp-approval-chain-review-packet.json`
- next reviewer receipt is
  `dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`
- current approved receipt count is `0`
- current blocked receipt count is `280`
- production, promotion, and training export remain `false`

The next output must be a real reviewer decision for the first license review.
If the reviewer approves it, apply exactly that decision through the guarded
apply path, then request the next receipt in the chain. If the reviewer rejects
it or asks for more evidence, keep the source template blocked and record the
reason as evidence.

### 2. Complete Governed Conversion And Validation

For the selected ADP dataset, finish the non-approval engineering evidence that
can be produced before training/export is allowed:

- full hosted conversion manifest or an explicit blocked-hosting receipt
- deterministic schema validation receipt
- provenance and source hash receipt
- sample-to-full split integrity receipt
- verifier execution receipt for converted traces
- replay/determinism evidence where applicable
- quality assessment for task diversity, trace validity, and failure modes

These receipts may support review, but they must not flip production,
promotion, or training export by themselves.

### 3. Run The First Agent Benchmark Only After Gates Clear

The first benchmark claim should be narrow and auditable:

- one approved ADP dataset
- one fixed agent configuration
- one reproducible run command
- trace export
- verifier result
- quality assessment summary
- failure-mode summary
- explicit claim boundary that separates benchmark execution from production
  promotion

## Recommended First Move

Do not switch lanes yet. Continue with `Agent-Data-Protocol` until one dataset
has real license, privacy/policy, split-integrity, hosted-conversion, and
training-export decisions recorded or explicitly rejected. The immediate blocker
is the real reviewer decision for
`dataset_license_review_approval:AlienKevin_SWE-ZERO-12M-trajectories`.
