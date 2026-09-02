# Concept Depth Audit

This audit compares the first-principles concept articles against the deeper theme pages.

The major issue is not paper coverage. The paper atlas is complete at 781 entries, and the major theme pages now link back to concept articles. The issue is depth consistency: most concept articles are still compact sketches, while pages such as `long-context-foundation-models.html` are full theme treatments.

## Depth Standard

A first-principles concept article should not be only a short summary. It should explain:

- the real problem in plain language;
- the concrete object being changed, measured, preserved, or checked;
- what must stay fixed;
- what may change;
- why the method family should work;
- what evidence would prove the claim;
- how shallow versions of the claim fail;
- which named papers show the concept from different angles;
- how the concept connects back to theme, math, and paper layers.

## Current Finding

All 25 concept pages have now crossed the current depth floor of roughly 1,400+ words with a deeper article structure:

- `evaluation-is-becoming-execution.html`: 2,133 words, 11 h2 sections.
- `agent-trajectory-is-the-object.html`: 2,041 words, 11 h2 sections.
- `feedback-signals-under-optimization-pressure.html`: 1,757 words, 11 h2 sections.
- `long-context-is-memory-design.html`: 1,738 words, 10 h2 sections.
- `data-as-training-pressure.html`: 1,617 words, 11 h2 sections.
- `grounding-as-evidence-preservation.html`: 1,597 words, 11 h2 sections.
- `compression-preserves-or-destroys-capability.html`: 1,511 words, 11 h2 sections.
- `boundaries-permissions-and-delegated-authority.html`: 1,471 words, 11 h2 sections.
- `human-facing-ai-is-hidden-state-estimation.html`: 1,464 words, 11 h2 sections.
- `formal-artifacts-need-native-checkers.html`: 1,448 words, 11 h2 sections.
- `synthetic-data-as-evidence-or-contamination.html`: 1,439 words, 11 h2 sections.
- `spectra-rank-and-subspaces-as-working-objects.html`: 1,439 words, 11 h2 sections.
- `scientific-generation-must-preserve-the-native-object.html`: 1,429 words, 11 h2 sections.
- `test-time-compute-is-a-policy.html`: 1,429 words, 10 h2 sections.
- `safety-is-an-invariant-under-pressure.html`: 1,427 words, 10 h2 sections.
- `theory-is-useful-when-it-names-the-bottleneck.html`: 1,424 words, 10 h2 sections.
- `uncertainty-as-a-decision-object.html`: 1,422 words, 11 h2 sections.
- `world-models-are-only-useful-if-actions-stay-true.html`: 1,420 words, 11 h2 sections.
- `privacy-and-unlearning-are-recoverable-information-claims.html`: 1,419 words, 10 h2 sections.
- `causality-starts-where-prediction-stops.html`: 1,412 words, 10 h2 sections.
- `retrieval-is-a-hypothesis-about-missing-evidence.html`: 1,412 words, 10 h2 sections.
- `efficiency-changes-the-algorithm.html`: 1,410 words, 10 h2 sections.
- `multimodal-models-need-modality-contracts.html`: 1,407 words, 10 h2 sections.
- `robotics-turns-perception-into-commitment.html`: 1,405 words, 11 h2 sections.
- `graph-learning-is-controlled-evidence-movement.html`: 1,402 words, 11 h2 sections.

Final validation: 25 concept pages detected, 25 at or above the 1,400-word floor, 0 HTML parse errors, and 0 broken local links from the concept pages. Representative desktop and mobile screenshots were rendered through Playwright for evaluation, graph learning, robotics, formal artifacts, long context, and data pressure. The contact-sheet review found coherent hero wrapping, stat grids, and first-section layout on both desktop and mobile. Render artifacts are in `.artifacts/concept-render-review/`.

## Concept Pages Deepened

Completed set:

- `agent-trajectory-is-the-object.html`
- `long-context-is-memory-design.html`
- `evaluation-is-becoming-execution.html`
- `feedback-signals-under-optimization-pressure.html`
- `test-time-compute-is-a-policy.html`
- `grounding-as-evidence-preservation.html`
- `data-as-training-pressure.html`
- `compression-preserves-or-destroys-capability.html`
- `retrieval-is-a-hypothesis-about-missing-evidence.html`
- `safety-is-an-invariant-under-pressure.html`
- `privacy-and-unlearning-are-recoverable-information-claims.html`
- `efficiency-changes-the-algorithm.html`
- `multimodal-models-need-modality-contracts.html`
- `causality-starts-where-prediction-stops.html`
- `scientific-generation-must-preserve-the-native-object.html`
- `uncertainty-as-a-decision-object.html`
- `synthetic-data-as-evidence-or-contamination.html`
- `boundaries-permissions-and-delegated-authority.html`
- `robotics-turns-perception-into-commitment.html`
- `world-models-are-only-useful-if-actions-stay-true.html`
- `graph-learning-is-controlled-evidence-movement.html`
- `formal-artifacts-need-native-checkers.html`
- `theory-is-useful-when-it-names-the-bottleneck.html`
- `spectra-rank-and-subspaces-as-working-objects.html`
- `human-facing-ai-is-hidden-state-estimation.html`

## Upgrade Template

Each upgraded concept article should include:

1. Opening problem boxes.
2. Core first-principles explanation.
3. Concrete object section.
4. Anatomy table.
5. Paper lens table.
6. Method logic section.
7. Failure map.
8. Evidence standard.
9. Cross-atlas connection.
10. Footer reader path.

## Completion Check

The concept layer should be considered depth-consistent when:

- all 25 concept pages parse as HTML;
- every concept page has a reader path to concept program, math concepts, and paper atlas;
- every concept page has at least 8 main sections or an equivalent dense structure;
- every concept page has a concrete object section, paper lens, failure map, and evidence standard;
- every concept page has no broken local links;
- rendered spot checks show the pages remain readable on desktop and mobile.

Current status: satisfied for the concept layer by the validation and rendered review above.
