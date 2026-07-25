# Certifying Capabilities from Finite Tests: When Is It Possible?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: cNCWYrSV5R
- Authors: Changlong Wu; Jin Sima; Wojciech Szpankowski
- Primary area: theory->learning_theory
- Keywords: Evaluation as inference;Generalizability;Minimax bounds;$\chi^2$ divergence;Property testing
- Source URL: https://openreview.net/forum?id=cNCWYrSV5R
- PDF URL: https://openreview.net/pdf?id=cNCWYrSV5R

## Abstract

Modern foundation models are evaluated through broad capabilities such as arithmetic, reasoning, safety, and robustness, yet it remains unclear in a principled sense when *finite tests* can meaningfully certify such claims. We develop a rigorous theory of capability evaluation by formalizing evaluation as inference over a task family and asking when guarantees over the full family can be inferred from a strict subset of tests. We analyze two canonical regimes. In stochastic multi-environment evaluation, we characterize when uniform certification is possible across multiple environments and show that the sample complexity is governed by a $\chi^2$-radius of the environment family, yielding near-optimal evaluation protocols with matching lower bounds under a natural overlap condition. In contrast, for worst-case, rule-like capabilities, we establish fundamental impossibility results. Even for structured model classes such as Boolean circuits of bounded size, black-box evaluation cannot, in general, certify global properties. Together, these results provide a principled framework for understanding when finite evaluation can and cannot certify capabilities.

## One-Sentence Claim

Finite capability tests can certify stochastic multi-environment performance under overlap and chi-square-radius control, but cannot generally certify worst-case rule-like capabilities by black-box evaluation.

## Problem

Foundation models are evaluated for broad capabilities such as reasoning, safety, robustness, and arithmetic using finite test suites. But finite tests only cover a strict subset of task families, and it is unclear when they justify claims about the full family.

The paper asks when evaluation can be treated as valid inference and when certification is impossible.

## Core Contribution

The paper formalizes capability evaluation as inference over task families. In stochastic multi-environment evaluation, it characterizes when uniform certification is possible and shows sample complexity is governed by a chi-square radius of the environment family, with near-optimal protocols and matching lower bounds under overlap.

For worst-case rule-like capabilities, it proves fundamental impossibility results: even bounded-size Boolean circuits cannot generally have global properties certified by black-box finite tests.

## Method

The method uses minimax inference and property testing. It distinguishes stochastic environments, where distributional overlap enables extrapolation from finite samples, from worst-case rule-like settings, where adversarially hidden failures make black-box certification impossible.

Chi-square divergence measures how far environments can be while still supporting transfer of evaluation evidence.

## Experiments and Evidence

Evidence reported in the abstract is theoretical:

- Formal evaluation-as-inference framework.
- Stochastic multi-environment certification characterization.
- Sample complexity governed by chi-square radius.
- Near-optimal protocols and matching lower bounds under overlap.
- Impossibility for worst-case rule-like capabilities.
- Impossibility even for bounded-size Boolean circuits under black-box evaluation.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact task-family formalism, overlap condition, and implications for practical benchmark design.

## Limits and Failure Modes

- The theory may abstract away adaptive benchmark contamination and model updating.
- Chi-square radius may be hard to estimate for real task families.
- Impossibility results do not preclude white-box, formal, or restricted-domain certification.
- Practical benchmarks still need operational heuristics when full certification is impossible.

## Deep Themes

**Evaluation is statistical inference.** Benchmark scores certify capabilities only under task-family assumptions.

**Worst-case capability claims are often impossible from finite black-box tests.** Some claims need formal verification or narrower scope.

**Distributional overlap is the currency of generalization from tests.** Chi-square radius quantifies certification difficulty.

## Subthemes

- Capability certification.
- Evaluation as inference.
- Chi-square environment radius.
- Property-testing impossibility.
- Black-box evaluation limits.

## Connections to Other Papers

Connects to HypoSpace, CausalGame, BrokenMath, Monitoring Monitorability, VenusBench-Mobile, and benchmark-methodology papers. It also provides theory behind why many new benchmarks expose failures rather than certify broad competence.

## Notes for Cross-Paper Synthesis

This paper provides a meta-evaluation anchor: many corpus benchmarks should be read as evidence under assumptions, not as universal capability certificates.
