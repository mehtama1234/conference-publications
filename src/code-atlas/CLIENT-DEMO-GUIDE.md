# Client Demo Guide

The demos should be reusable proof tools, not one-off visual explainers.

Each production-grade client demo needs five parts:

- Client challenge: the real failure the client recognizes from their system.
- Protected thing: what must stay true when the method is used.
- Allowed change: what the method is allowed to vary, compress, score, sample, or update.
- Evidence packet: the measured result that supports or falsifies the claim.
- Adapter boundary: the place where toy data is replaced by client logs, artifacts, tests, or model outputs.

## Demo Tiers

Tier 1 is the current public demo: browser-only, first-principles, safe to show in a workshop.

Tier 2 replaces knobs with a small client-shaped fixture: sample tasks, traces, logs, artifacts, or benchmark rows.

Tier 3 connects to client systems through adapters: evaluation runs, CI logs, model checkpoints, telemetry exports, or audit datasets.

## Reuse Pattern

Start with the concept demo, then replace only the data source:

```js
import { buildEvidencePacket, riskAdjustedValue } from "./client-demo-kit.js";

const value = riskAdjustedValue({
  gain: measuredAccuracyLift,
  cost: normalizedLatencyCost,
  failureRisk: measuredToolFailureRisk
});

const packet = buildEvidencePacket({
  claim: "One more tool call is worth it for high-doubt cases.",
  protectedThing: "Answer quality target",
  allowedChange: "Tool-call budget",
  observedResult: value,
  failureCase: "Accuracy rises while cost rises faster"
});
```

The client should see the same story in every demo:

1. Here is the everyday version of the problem.
2. Here is what must stay the same.
3. Here is what we are allowed to change.
4. Here is the failure case the paper is designed to catch.
5. Here is the measured evidence that would prove the method helped.

## First Ten Client Adaptations

- Trace information: replace toy sliders with paired prompts, trace diffs, and answer diffs.
- Tool-cost tradeoffs: replace toy cost with API cost, latency, failure rate, and answer lift.
- Artifact-native judging: replace toy defects with broken UI states, failing tests, citation gaps, or proof-checker failures.
- Stand-in score drift: replace toy score with the client metric and an independent audit target.
- Rare-risk sampling: replace toy rarity with incident rates, edge workflows, or adversarial cases.
- Context compression: replace toy clues with long records and full-vs-short answer agreement.
- Numerical compression: replace toy precision with hardware kernels, latency, memory, and regression suites.
- Sample-making paths: replace toy coverage with domain-specific modes and independent validity checks.
- Movement rulers: replace toy step size with checkpoint diffs and behavior-regression results.
- Same-evidence cause stories: replace toy assumptions with treatment, outcome, background facts, and sensitivity checks.
