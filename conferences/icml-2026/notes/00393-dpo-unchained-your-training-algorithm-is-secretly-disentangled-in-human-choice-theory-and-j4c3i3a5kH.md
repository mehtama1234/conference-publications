# DPO Unchained: Your Training Algorithm is Secretly Disentangled in Human Choice Theory (and Its Loss' Convexity is Dispensable)

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: j4c3i3a5kH
- Authors: Wenxuan Zhou; Shujian Zhang; brice magdalou; John Wheatley Lambert; Ehsan Amid; Richard Nock; Andrew Hard
- Primary area: theory->learning_theory
- Keywords: Direct Preference Optimization;Proper Loss Functions;Stochastic Choice Theory
- Source URL: https://openreview.net/forum?id=j4c3i3a5kH
- PDF URL: https://openreview.net/pdf?id=j4c3i3a5kH

## Abstract

Normative theories allow one to elicit key parts of a ML algorithm from first principles, which is crucial at a time of championed scrutiny for ML work. Direct Preference Optimization (DPO) cleverly bypasses reward modeling by making an explicit link with a specific normative model of human choice. Our paper elevates this connection to the full generality of DPO's normative framework. Getting there requires reworking social choice theory's textbook path for a better RLHF/ML fit. It elevates the connection to a remarkably broad viewpoint on preference optimization, considering the current panorama of DPO follow-ups. It also unveils unexpected riches for ML, chief among which the support for *non-convex* losses, the fact that *any* compliant ML analytical choice can be embedded with *any* human choice model, and a normative framework's umbrella wide enough to safeguard DPO's *extensions* (margins, length correction, ...). A *toy* experiment ``far away'' from the DPO crowd is given.

## One-Sentence Claim

DPO and its extensions can be understood through a broad human-choice-theory framework where convexity is not essential and compliant ML losses can pair with many choice models.

## Problem

DPO bypasses explicit reward modeling by tying preference optimization to a normative model of human choice. But the landscape of DPO variants has expanded, and the underlying normative assumptions are often narrow or implicit.

The paper asks how general the DPO-choice-theory connection really is, and which analytical choices are necessary versus dispensable.

## Core Contribution

The paper broadens DPO's normative framework using a reworked version of social choice theory adapted for RLHF and ML. It claims support for non-convex losses, embedding of compliant ML analytical choices with human choice models, and coverage of DPO extensions such as margins and length correction.

The central message is that DPO-style algorithms are more disentangled than they appear: the ML loss design and human choice model can be paired flexibly under a normative umbrella.

## Method

The method is theoretical and normative. It formalizes the relationship between preference optimization losses and stochastic or social choice models, then analyzes which properties are required for compatibility.

Rather than treating the standard DPO loss as uniquely justified, it identifies a larger family of loss/choice-model combinations.

## Experiments and Evidence

Evidence reported in the abstract:

- Generalized normative framework for DPO and follow-ups.
- Support for non-convex losses.
- Claim that compliant ML analytical choices can be embedded with human choice models.
- Coverage of extensions such as margins and length correction.
- A toy experiment outside the usual DPO setting.

Source depth is abstract/metadata only; full-paper reading is needed to validate definitions of compliant losses, choice models, and practical consequences.

## Limits and Failure Modes

- A broad normative framework may not identify which choice model fits real annotator behavior.
- Non-convex support can expand design space while increasing optimization risk.
- Toy experiments may not establish practical RLHF gains.
- The abstraction may be hard to operationalize without guidance on model selection.

## Deep Themes

**Preference optimization is normative modeling.** Losses encode assumptions about human choice, not just optimization convenience.

**DPO is a design family, not one algorithm.** The paper emphasizes modularity between choice model and analytical loss.

**Convexity may be a convenience, not a foundation.** The theory suggests wider loss classes can still be choice-theoretically meaningful.

## Subthemes

- Direct Preference Optimization.
- Human choice theory.
- Proper/non-convex losses.
- Normative RLHF foundations.
- Margins and length correction.

## Connections to Other Papers

Connects to RePO, Critique-GRPO, PRISM, Weak-Strong Verification, and alignment-feedback work. It complements RePO's claim that preference signals need richer behavioral interpretation.

## Notes for Cross-Paper Synthesis

DPO Unchained adds a theoretical alignment layer: post-training objectives should be inspected as models of human choice, not treated as neutral loss functions.
