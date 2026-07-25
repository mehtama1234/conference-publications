# Manifold-Aware Perturbations for Constrained Generative Modeling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: UPiyC9W4ms
- Authors: Katherine Keegan; Lars Ruthotto
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: generative modeling;manifold constraints;diffusion models;normalizing flows
- Source URL: https://openreview.net/forum?id=UPiyC9W4ms
- PDF URL: https://openreview.net/pdf?id=UPiyC9W4ms

## Abstract

Generative models have enjoyed widespread success in a variety of applications. However, they encounter inherent mathematical limitations in modeling distributions where samples are constrained by equalities, as is frequently the setting in scientific domains. In this work, we develop a computationally cheap, mathematically justified, and highly flexible distributional modification for combating known pitfalls in equality-constrained generative models. We propose perturbing the data distribution in a constraint-aware way such that the new distribution has support matching the ambient space dimension while still implicitly incorporating underlying manifold geometry. Through theoretical analyses and empirical evidence on several representative tasks, we illustrate that our approach consistently enables data distribution recovery and stable sampling with both diffusion models and normalizing flows.

## One-Sentence Claim

Equality-constrained generative modeling can be stabilized by perturbing data distributions in a constraint-aware way that expands support to ambient dimension while preserving manifold geometry.

## Problem

Diffusion models and normalizing flows often assume data distributions with support compatible with the ambient space. Scientific data, however, frequently lies on equality-constrained manifolds. This creates mathematical difficulties for likelihoods, score estimation, sampling, or recovery when the target distribution is singular relative to ambient measure.

The paper asks how to modify such distributions cheaply and flexibly so standard generative models can learn them without ignoring the underlying constraints.

## Core Contribution

The paper proposes manifold-aware perturbations: a distributional modification that gives the perturbed distribution ambient-dimensional support while implicitly retaining the geometry of the equality-constrained manifold.

The approach is described as computationally cheap, mathematically justified, and compatible with both diffusion models and normalizing flows. Theory and experiments show improved data distribution recovery and stable sampling.

## Method

The method perturbs samples in a constraint-aware manner rather than adding isotropic ambient noise. The perturbation is designed so the model sees a full-dimensional distribution, avoiding singular-support pathologies, while the perturbation structure reflects the constraint manifold.

This creates a bridge between mathematically constrained data and off-the-shelf generative modeling machinery.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical analysis of the proposed distributional modification.
- Empirical tests on several representative equality-constrained tasks.
- Consistent data distribution recovery.
- Stable sampling with diffusion models and normalizing flows.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: constraint classes, perturbation construction, recovery guarantees, benchmark tasks, and how samples are projected or evaluated against constraints.

## Limits and Failure Modes

- Perturbation scale likely controls a tradeoff between numerical stability and constraint fidelity.
- Equality constraints must be known or estimable; hidden constraints are harder.
- Implicitly preserving manifold geometry may not be enough for strict feasibility if downstream applications require exact constraints.
- High-curvature or boundary-heavy manifolds may need special handling.

## Deep Themes

**Make singular structure learnable by changing the distribution, not the whole model.** The paper modifies data support so existing generative families can operate.

**Scientific generative modeling needs geometry-aware noise.** Perturbations are not generic regularization; they encode constraint geometry.

**Ambient-space convenience must be reconciled with manifold truth.** The central move is to make training numerically tractable without discarding equality constraints.

## Subthemes

- Equality-constrained generative modeling.
- Manifold-aware distributional smoothing.
- Diffusion and flow compatibility.
- Stable sampling from near-manifold distributions.
- Scientific constraints as generative-model priors.

## Connections to Other Papers

Connects to Flowers, WLA/ERA5-Latent, TD3B, and other scientific ML papers where physical or mathematical structure changes the learning objective. It also links to representation-geometry and equivariance papers such as RECM and ENGNN because all manage the gap between ambient coordinates and intrinsic structure.

## Notes for Cross-Paper Synthesis

This paper adds to a deep geometry theme: many 2026 methods succeed by identifying the intrinsic structure that standard models flatten away, then adding a minimal correction so generic learning machinery respects that structure.
