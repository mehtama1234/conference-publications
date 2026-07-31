# Handwritten Conference Theme Page Plan

## Objective

Turn the conference theme site from generated evidence pages into a readable field map of ICML/ICLR research directions. The finished site should help someone understand what problem each theme is trying to solve, why the problem matters, what technical approaches the papers use, and how the papers relate to one another.

This is not a template cleanup. The target is hand-written synthesis at paragraph depth across all 64 theme pages and all named paper entries.

## Current State

- The site has 64 theme pages in `docs/conference-themes/site/themes/`.
- The pages are live locally at `http://127.0.0.1:8765/`.
- `main` contains the source site.
- `gh-pages` contains a static-only copy intended for GitHub Pages.
- The first fully rewritten page is `evaluation-benchmarks-and-measurement.html`.
- The public GitHub Pages URL is still returning 404 until repository Pages settings are enabled for the `gh-pages` branch.

## What A Finished Theme Page Must Do

Each theme page should answer five questions in plain language:

1. What is the real problem this theme is trying to solve?
2. Why did this problem become important now?
3. What are the main approaches papers use?
4. Where do the approaches disagree or make different tradeoffs?
5. What does the theme imply about the direction of the field?

The writing standard is first-principles and conceptual. Avoid conference-summary filler such as "novel framework", "comprehensive benchmark", "robust method", or "important direction" unless the sentence explains what the method actually changes.

## Required Page Structure

Each rewritten page should contain:

- A concise theme title and subtitle.
- A first-principles problem statement.
- A big-picture synthesis section that connects the papers into one field-level story.
- Three to seven subthemes, each with a real conceptual explanation.
- A paper treatment section under each subtheme.
- A closing section explaining what the theme says about ICML/ICLR as a whole.
- A full paper inventory so no evidence disappears while richer writing is added.

## Required Paper Paragraph Standard

Each paper paragraph should explain:

- The concrete object being studied: model, task, environment, dataset, verifier, theorem, optimizer, robot, system, or interface.
- The failure mode or limitation the paper is responding to.
- The approach used by the paper.
- Why that approach matters beyond the paper itself.
- How it relates to neighboring papers in the same subtheme.

A good paper paragraph should be understandable without already knowing the paper. It should not merely restate the title.

Example target shape:

> CyberGym treats cybersecurity evaluation as an executable environment problem rather than a question-answering problem. The core issue is that a model can describe a vulnerability without being able to exploit, patch, or validate it in a realistic workflow. The benchmark therefore gives the agent tools, state, and tasks whose success can be checked by consequences in the environment. This matters because it moves evaluation from "did the model sound right" to "did the system state change correctly", which is the same measurement logic needed for browser, code, database, and security agents.

## Rewrite Batches

### Batch 1: Foundation Pages

These pages define the vocabulary for the rest of the site and should be rewritten first:

- `evaluation-benchmarks-and-measurement.html` - done as the first handwritten pass.
- `reasoning-planning-and-tool-use.html`
- `llm-agents-and-process-diagnostics.html`
- `agent-infrastructure-risk.html`
- `software-and-code-intelligence.html`
- `developer-tools-and-reliability.html`

### Batch 2: Safety, Robustness, And Governance

These pages explain how the field handles failure, misuse, privacy, and reliability:

- `robustness-safety-privacy-and-unlearning.html`
- `robustness-and-distribution-shift.html`
- `societal-impacts-and-governance.html`
- `alignment-preference-optimization-and-feedback.html`
- `data-governance-and-curation.html`
- `data-quality-governance-and-curation.html`

### Batch 3: Multimodal, Embodied, And Physical AI

These pages connect perception, action, robotics, and physical-world modeling:

- `multimodal-and-embodied-models.html`
- `robotics-and-embodied-ai.html`
- `robotics-and-control.html`
- `adaptation-and-continual-control.html`
- `foundation-models-beyond-text.html`
- `scientific-and-physical-domain-generation.html`

### Batch 4: Reasoning, Structure, And Memory

These pages explain how models represent long chains, symbolic structure, retrieval, and uncertainty:

- `long-context-and-long-horizon-generation.html`
- `long-context-foundation-models.html`
- `retrieval-and-information-access.html`
- `hybrid-neural-symbolic-systems.html`
- `program-synthesis-and-verification.html`
- `probabilistic-inference-and-uncertainty.html`
- `sequence-modeling.html`

### Batch 5: Optimization, Scaling, And Systems

These pages explain the machinery underneath training and inference:

- `optimization-and-training-dynamics.html`
- `theory-and-optimization.html`
- `theory-unifies-engineering-practice.html`
- `theory-follows-deployment-needs.html`
- `test-time-scaling-and-inference-control.html`
- `inference-time-model-control.html`
- `systems-and-infrastructure.html`
- `scientific-computing-and-hardware.html`
- `numerical-ml-systems.html`
- `sparse-and-modular-computation.html`
- `efficiency-as-capability-enabler.html`
- `efficient-adaptation.html`

### Batch 6: Learning Under Shift, Time, Graphs, And Domains

These pages cover generalization, temporal structure, relational structure, and domain science:

- `domain-adaptation-and-distribution-shift.html`
- `continual-learning.html`
- `federated-and-distributed-learning.html`
- `time-series-and-dynamical-systems.html`
- `time-series-and-forecasting.html`
- `graph-learning.html`
- `graph-and-relational-learning.html`
- `causality.html`
- `causality-and-causal-discovery.html`
- `scientific-discovery-and-causal-inference.html`
- `scientific-and-healthcare-ml.html`
- `healthcare-and-education-agents.html`

### Batch 7: Generative Modeling, Cognition, And Remaining Cross-Cuts

These pages finish the map and resolve overlap between generated themes:

- `generative-modeling.html`
- `generative-modeling-for-decision-making.html`
- `structured-generative-modeling.html`
- `diffusion-language-models.html`
- `cognitive-science-and-human-modeling.html`
- `neuroscience-and-cognition.html`
- `representation-geometry.html`
- `interpretability-as-intervention.html`
- `foundation-model-evaluation.html`
- `open-science-infrastructure.html`
- `deployment-constraints-reshape-methods.html`
- `multi-agent-systems.html`
- `robust-optimization-and-decision-making.html`

## Production Workflow

For each page:

1. Read the current HTML page and its evidence rows.
2. Identify the actual subthemes from the listed papers.
3. Rewrite the page by hand, preserving navigation and site styling.
4. Give anchor papers paragraph-level treatment.
5. Keep a complete paper inventory at the bottom until every paper has a rich paragraph.
6. Validate the HTML parser accepts the page.
7. Check the page on the local server.
8. Commit to `main`.
9. Copy the updated static page to `gh-pages`.
10. Push both branches.

## Acceptance Criteria

The site is production-ready when:

- All 64 pages have handwritten conceptual introductions.
- Every page has explicit subthemes with rich explanations.
- Every named paper has at least one paragraph, not a one-line label.
- The pages do not sound generated or interchangeable.
- The navigation and local static site work.
- `main` and `gh-pages` are both pushed.
- GitHub Pages serves the site publicly from the `gh-pages` branch.

## Next Concrete Step

Rewrite `reasoning-planning-and-tool-use.html` next. It is the natural follow-on to evaluation because it explains what agents are trying to do before the evaluation page explains how their behavior is measured.
