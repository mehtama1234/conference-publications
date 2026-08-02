# Client Demo Guide

The demos should be reusable proof tools, not one-off visual explainers.

Start with `COURSE-MAP.md` when reviewing the course as a whole. It gives the
reading order, the shared proof shape, and the simple mastery test for the ten
topics.

## Course-Wide Plain-English Standard

The course should not sound like a list of paper keywords. It should teach one
basic habit in everyday words:

Before trusting any method, ask what real thing it is trying to protect.

That real thing can be a working page, a correct answer, a saved fact, a safe
rare case, a cause claim, a model behavior, a generated design, or a business
decision. The method is useful only if that thing still holds when the system is
changed, compressed, optimized, scored, sampled, or trained.

The writing should therefore move slowly and concretely:

1. Name the object people can inspect.
2. Name what must stay true.
3. Name what is allowed to change.
4. Name the failure that would fool a shallow check.
5. Name the evidence that would make the claim believable.

Avoid shortcut words when an everyday sentence would be clearer. Do not say a
demo is about "alignment," "robustness," "optimization," "topology," or
"causality" unless the next sentence explains the object in normal language.
For example:

- Instead of "the trace is faithful," say "the middle work changes at the place
  where the task fact changed."
- Instead of "the metric is misaligned," say "the score went up while the real
  thing people wanted got worse."
- Instead of "the topology is preserved," say "the shape was bent or stretched,
  but the hole, connection, or boundary that decides the answer stayed the
  same."
- Instead of "the intervention identifies the effect," say "the test changed
  one thing while holding the rival explanations still enough to compare them."

This is the reason topology belongs in the same spirit as the AI demos.
Topology asks what survives when the surface details change. A shape can be
stretched, bent, or redrawn, but some facts can stay fixed: whether it has one
piece or two, whether it has a hole, whether one part surrounds another, whether
two paths are connected. That is the same first question the course asks of
every method: which facts are surface details, and which facts must survive?

The same pattern appears across fields:

- In software, colors and layout may change, but the user path must still work.
- In medicine, a model score may change, but the patient outcome is the thing
  that matters.
- In finance, daily averages may look fine, but rare loss under stress must be
  visible.
- In robotics, a plan may look smooth, but the robot must still avoid collision
  and finish the task.
- In science, several stories may fit the same records, so the claim must not
  say more than the evidence forces.
- In geometry and topology, coordinates may move, but holes, boundaries,
  connected parts, and inside-outside relationships may be the protected facts.

The final test for the writing is simple: a smart non-specialist should be able
to explain why the demo matters without repeating a buzzword. If they can say
"this shows what has to stay true, what changed, and what failure it catches,"
the writing is doing its job.

Each production-grade client demo needs five parts:

- Client challenge: the real failure the client recognizes from their system.
- Protected thing: what must stay true when the method is used.
- Allowed change: what the method is allowed to vary, compress, score, sample, or update.
- Evidence packet: the measured result that supports or falsifies the claim.
- Adapter boundary: the place where toy data is replaced by client logs, artifacts, tests, or model outputs.

The important rule is that the demo must not merely visualize a paper keyword.
It must create a small falsifiable test. A client should be able to say:

- "This is the object in my system."
- "This is the thing I cannot allow to change."
- "This is the thing I am willing to change."
- "This is the failure I am worried about."
- "This evidence would convince me or tell me the method failed."

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

The course chapter for each topic lives in `chapters/*.md`. Keep those chapters
plain enough to read without the browser demo. They should answer:

- Why would a normal person care about this failure?
- What object is being protected?
- What surface details are allowed to move?
- What shallow test would miss the failure?
- Where does the same pattern appear outside AI, including topology or
  geometry when the idea is about preserved structure?

The starter fixture file is `fixtures/client-shaped-fixtures.json`. Keep the
same shape and replace the rows with client records. Each row should be plain
enough for a non-specialist stakeholder to inspect:

- input: the record, prompt, artifact, or case being tested.
- method: what the system did or what comparison was run.
- evidence: the concrete observation that supports or weakens the claim.
- result: the decision the evidence allows.

## Depth Bar

Do not call a demo production-ready until it passes these checks:

- The demo names a concrete object, not an abstract field.
- The protected thing is measurable before and after the method.
- The allowed change is small enough that a user understands the comparison.
- The failure case can actually happen in the client's workflow.
- The evidence uses client-shaped data, not only hand-picked examples.
- The result can be wrong. A demo that always says the method works is not proof.

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
