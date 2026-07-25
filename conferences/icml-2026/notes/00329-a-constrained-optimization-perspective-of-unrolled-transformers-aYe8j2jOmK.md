# A Constrained Optimization Perspective of Unrolled Transformers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aYe8j2jOmK
- Authors: Javier Porras-Valenzuela; Samar Hadou; Alejandro Ribeiro
- Primary area: deep_learning->robustness
- Keywords: constrained learning;unrolled neural networks;transformers
- Source URL: https://openreview.net/forum?id=aYe8j2jOmK
- PDF URL: https://openreview.net/pdf?id=aYe8j2jOmK

## Abstract

We introduce a constrained optimization framework for training transformers that behave like optimization descent algorithms. Specifically, we enforce layerwise descent constraints on the objective function and replace standard empirical risk minimization (ERM) with a primal-dual training scheme. This approach yields models whose intermediate representations decrease the loss monotonically in expectation across layers. We apply our method to both unrolled transformer architectures and conventional pretrained transformers on tasks of video denoising and text classification. Across these settings, we observe that constrained transformers achieve stronger robustness to perturbations and maintain higher out-of-distribution generalization, while preserving competitive in-distribution performance.

## One-Sentence Claim

Training Transformers with layerwise descent constraints makes their intermediate representations behave like optimization iterates, improving robustness and OOD generalization.

## Problem

Transformers are powerful but their intermediate computations are not explicitly constrained to improve an objective layer by layer. Standard empirical risk minimization only supervises final outputs, which may allow brittle internal trajectories under perturbations or distribution shift.

The paper asks whether enforcing optimization-descent behavior across layers can make Transformers more robust.

## Core Contribution

The paper introduces a constrained optimization framework for training Transformers that behave like descent algorithms. It enforces layerwise descent constraints on an objective and replaces ERM with a primal-dual training scheme.

The resulting models have intermediate representations that decrease loss monotonically in expectation across layers. Applied to unrolled Transformer architectures and conventional pretrained Transformers, the approach improves perturbation robustness and OOD generalization while preserving competitive in-distribution performance.

## Method

The method formulates training with constraints requiring each layer's representation to reduce the objective in expectation. A primal-dual procedure optimizes the task loss while enforcing these descent constraints.

This makes the depth dimension act more like iterations of an optimization algorithm.

## Experiments and Evidence

Evidence reported in the abstract:

- Layerwise descent constraints.
- Primal-dual training replacing standard ERM.
- Monotonic expected loss decrease across intermediate layers.
- Experiments on video denoising and text classification.
- Stronger robustness to perturbations.
- Higher OOD generalization with competitive in-distribution performance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: objective definition, constraint satisfaction metrics, architectures, and perturbation/OOD benchmarks.

## Limits and Failure Modes

- Descent constraints may reduce flexibility for tasks where intermediate loss is not well-defined.
- Primal-dual training can be sensitive to constraint weights and optimization stability.
- Expected monotonicity may not guarantee per-example monotonic behavior.
- Applying this to very large LLMs may be costly.

## Deep Themes

**Network depth can be treated as optimization time.** Transformer layers become constrained descent steps.

**Internal trajectories matter for robustness.** The model is trained to improve progressively, not just land on the right final answer.

**Classical constrained optimization can regularize deep models.** Primal-dual structure replaces unconstrained ERM.

## Subthemes

- Unrolled Transformers.
- Layerwise descent constraints.
- Primal-dual training.
- Robust intermediate representations.
- OOD generalization through optimization behavior.

## Connections to Other Papers

Connects to FlowOptimizer, PAVE, NeuronCtrl, and Local Diffusion Composition through field/trajectory constraints. It also links to NAD and ReQAT because all focus on internal process states, not only final outputs.

## Notes for Cross-Paper Synthesis

This paper adds a strong process-shaping theme: robustness can come from constraining how representations evolve layer by layer.
