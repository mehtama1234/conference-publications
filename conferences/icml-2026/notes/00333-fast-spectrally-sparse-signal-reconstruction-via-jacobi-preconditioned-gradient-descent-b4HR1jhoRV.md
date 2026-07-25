# Fast Spectrally Sparse Signal Reconstruction via Jacobi-Preconditioned Gradient Descent

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: b4HR1jhoRV
- Authors: Jian-Feng Cai; Xueyang Quan; Yang Wang; Jiaxi Ying
- Primary area: optimization->nonconvex
- Keywords: Low Rank Matrix; Hankel Matrix; Riemannian Optimization; Compressed Sensing
- Source URL: https://openreview.net/forum?id=b4HR1jhoRV
- PDF URL: https://openreview.net/pdf?id=b4HR1jhoRV

## Abstract

Spectrally sparse signal reconstruction arises in a wide range of applications and can be formulated as a low-rank Hankel matrix completion problem. We develop a Jacobi-preconditioned gradient descent method that preserves the low per-iteration complexity of first-order algorithms while achieving linear convergence at a rate independent of the condition number. By introducing a generator that maps factor-based iterates to matrix space, we establish equivalence with manifold-based methods, enabling direct convergence analysis while avoiding the need to define distances under complex-symmetric factorization ambiguity. Extensive experiments demonstrate that the proposed algorithm outperforms state-of-the-art methods in both iteration count and computational time across a broad range of problem settings.

## One-Sentence Claim

Jacobi-preconditioned gradient descent reconstructs spectrally sparse signals via low-rank Hankel completion with condition-number-independent linear convergence and low first-order cost.

## Problem

Spectrally sparse signal reconstruction appears in compressed sensing and related applications and can be formulated as low-rank Hankel matrix completion. First-order methods are cheap per iteration but can suffer condition-number-dependent convergence, while manifold methods can be harder to analyze under factorization ambiguity.

The paper asks how to get fast convergence without giving up low per-iteration complexity.

## Core Contribution

The paper develops a Jacobi-preconditioned gradient descent method that preserves first-order efficiency while achieving linear convergence independent of condition number.

It introduces a generator mapping factor-based iterates to matrix space, establishing equivalence with manifold-based methods. This enables convergence analysis while avoiding distances under complex-symmetric factorization ambiguity.

## Method

The method operates in a factorized representation of the low-rank Hankel matrix but analyzes iterates through a generator in matrix space. Jacobi preconditioning rescales updates to neutralize conditioning effects.

By proving equivalence with manifold methods, the paper imports convergence tools while keeping the practical algorithm simple.

## Experiments and Evidence

Evidence reported in the abstract:

- Linear convergence at a rate independent of condition number.
- Low per-iteration complexity like first-order algorithms.
- Generator-based equivalence to manifold methods.
- Avoidance of complex-symmetric factorization distance issues.
- Extensive experiments across broad problem settings.
- Better iteration counts and computational time than state-of-the-art methods.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: sampling assumptions, noise robustness, benchmark signals, and exact runtime comparisons.

## Limits and Failure Modes

- Guarantees likely depend on incoherence or sampling assumptions common in matrix completion.
- Spectral sparsity assumptions may not hold for broadband signals.
- Preconditioning effectiveness may depend on accurate diagonal scaling.
- Noisy or model-mismatched settings need full-paper inspection.

## Deep Themes

**Preconditioning can remove apparent hardness.** The condition-number dependence is addressed by changing the geometry of gradient descent.

**Factorized algorithms need matrix-space analysis.** The generator bypasses ambiguous factor distances.

**Classical signal models still drive ML optimization advances.** Hankel low-rank structure remains a powerful prior.

## Subthemes

- Spectrally sparse reconstruction.
- Low-rank Hankel completion.
- Jacobi preconditioning.
- Riemannian/manifold equivalence.
- Condition-number-independent convergence.

## Connections to Other Papers

Connects to Lottery Prior, Manifold Perturbations, FlowOptimizer, and BCO theory through structured inverse/optimization problems. It also links to PRISM and gauge papers because factorization ambiguity is handled through geometry-aware analysis.

## Notes for Cross-Paper Synthesis

This paper adds to a recurring optimization lesson: many hard dynamics become tractable once the update geometry matches the representation's invariances.
