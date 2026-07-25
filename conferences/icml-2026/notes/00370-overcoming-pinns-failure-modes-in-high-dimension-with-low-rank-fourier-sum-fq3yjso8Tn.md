# Overcoming PINNs Failure Modes In High Dimension With Low-Rank Fourier Sum

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fq3yjso8Tn
- Authors: Natan Kaminsky; Daniel Freedman; Kira Radinsky
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: partial differential equations;physics informed neural networks;high dimension;failure modes
- Source URL: https://openreview.net/forum?id=fq3yjso8Tn
- PDF URL: https://openreview.net/pdf?id=fq3yjso8Tn

## Abstract

Physics-informed neural networks (PINNs) can be unreliable on PDEs with oscillatory, multiscale, stiff, or long-time solutions, and these difficulties worsen in high dimensions where collocation-based training yields large numerical integration error and high-variance gradients. We propose Low-Rank Fourier Sums (LoRFS), representing the solution as a low-rank sum of separable Fourier expansions (products of one-dimensional Fourier series across coordinates). This makes high-frequency structure explicit and enables closed-form evaluation of common physics-based objectives and their gradients (e.g., $L^2$ residual and variational losses), replacing sampling-based collocation estimates with analytic loss evaluation and eliminating sampling noise. We further provide theoretical results that clarify why LoRFS is particularly well suited to high-dimensional regimes. Across canonical PINN failure-mode benchmarks and their high-dimensional extensions, LoRFS consistently outperforms strong PINN baselines and remains stable in regimes where competing methods degrade.

## One-Sentence Claim

Low-Rank Fourier Sums avoid key high-dimensional PINN failure modes by representing PDE solutions analytically as separable Fourier expansions with closed-form physics losses.

## Problem

PINNs struggle on oscillatory, multiscale, stiff, and long-time PDEs, and the problems worsen in high dimensions. Collocation-based training introduces numerical integration error and high-variance gradients, making optimization unstable exactly where scientific workloads need reliability.

The paper asks whether a more structured function class can replace noisy sampling-based physics losses in high-dimensional PDE solving.

## Core Contribution

The contribution is Low-Rank Fourier Sums, a representation of PDE solutions as low-rank sums of separable Fourier expansions, where each term is a product of one-dimensional Fourier series across coordinates.

This representation makes high-frequency structure explicit and enables closed-form evaluation of common physics objectives and gradients, including L2 residual and variational losses. The result is analytic loss evaluation instead of collocation estimates.

## Method

LoRFS parameterizes the solution with separable Fourier factors and low-rank summation. Because derivatives and integrals of Fourier terms can be evaluated analytically, the method computes physics losses and gradients without sampling collocation points.

The theory explains why the representation is especially suitable in high dimensions, where separability and low rank reduce the curse of dimensionality for certain PDE structure.

## Experiments and Evidence

Evidence reported in the abstract:

- Canonical PINN failure-mode benchmarks and high-dimensional extensions.
- Stable performance on oscillatory, multiscale, stiff, or long-time solution regimes.
- Consistent outperformance over strong PINN baselines.
- Closed-form evaluation of L2 residual and variational losses and gradients.
- Theoretical results supporting high-dimensional suitability.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: PDE classes, rank requirements, boundary-condition handling, and compute scaling.

## Limits and Failure Modes

- Low-rank separable Fourier structure may not fit PDE solutions with strong localized or irregular features.
- Boundary conditions and complex domains can be harder than rectangular/separable settings.
- High-frequency explicitness may increase parameter sensitivity or require careful rank selection.
- Analytic losses are only available when the PDE/objective aligns with the representation.

## Deep Themes

**Structure beats generic collocation in high dimensions.** The method replaces stochastic sampling with analytic objectives where the function class allows it.

**Scientific ML is moving toward problem-native bases.** Fourier separability encodes PDE structure more directly than generic neural networks.

**Failure-mode benchmarks matter.** The paper targets regimes where standard PINNs are known to degrade, not only easy PDE demonstrations.

## Subthemes

- Low-rank separable Fourier expansions.
- Analytic physics loss evaluation.
- High-dimensional PDE solving.
- PINN failure modes.
- Sampling-noise elimination.

## Connections to Other Papers

Connects to ReViT, Dirac-Frenkel-Onsager dynamics, NeuronCtrl, Jacobi Spectral Reconstruction, and scientific generative-control papers. It fits the broader theme of replacing generic neural approximation with structure matched to physical systems.

## Notes for Cross-Paper Synthesis

LoRFS strengthens the scientific-ML theme: when the domain has exploitable analytic structure, the best neural-adjacent method may be a structured representation that avoids noisy generic training altogether.
