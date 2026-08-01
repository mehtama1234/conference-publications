# Code Atlas

This folder contains small end-user-friendly demos that mirror the math atlas.
Each demo is intentionally tiny: it shows the promise, the user-controlled
knob, the failure case, and the evidence that would prove the idea.

Open the browser UI:

```bash
xdg-open src/code-atlas/index.html
```

No package install is required. The first batch covers ten subthemes:

- `agents-reasoning/trace-information/ragen2-style-trace-dependence`
- `agents-reasoning/tool-cost-tradeoffs/paretopo-style-tool-value`
- `evaluation-safety/artifact-native-judging/webdevjudge-style-artifact-check`
- `evaluation-safety/stand-in-score-drift/rlvepsr-style-reward-pressure`
- `evaluation-safety/rare-risk-sampling/rare-event-analysis-stress-sampling`
- `data-systems/context-compression/thinkv-style-rare-clue-retention`
- `data-systems/numerical-compression/liftquant-style-behavior-preservation`
- `physical-generative/sample-making-paths/falcon-style-path-coverage`
- `theory-training-rules/movement-rulers/adam-style-movement-ruler`
- `causality-scientific/same-evidence-cause-stories/distributional-equivalence-toy`

## Demo Contract

Every demo should keep this shape:

- Promise: what should stay true.
- Knob: what the user can change.
- Failure: what breaks when the wrong thing is measured or preserved.
- Proof: what observation would make the claim believable.

These are not full paper reproductions. They are first-principles executable
examples that make the claim testable before later work adds original-author
code adapters or deeper reproductions.

## Production Reuse

The browser page is the workshop layer. The reusable source layer is:

- `client-demo-kit.js`: shared scoring and evidence helpers.
- `fixtures/client-shaped-fixtures.json`: small example records that show the
  data shape each demo expects.
- `CLIENT-DEMO-GUIDE.md`: the path from toy demo to client adapter.
- `themes/.../README.md`: per-theme source folders where client fixtures,
  original-author adapters, or deeper reproductions can be added.

A production client demo should not ask the client to trust the paper label.
It should show a familiar failure, name what must stay true, change one
controlled thing, and produce an evidence packet that supports or falsifies the
claim.

## Fixture Rule

Every demo needs at least two records:

- one record where the method should hold,
- one record where the hidden failure appears.

The point is not to make the method look good. The point is to make the
failure visible enough that a client can recognize whether the method applies
to their system.
