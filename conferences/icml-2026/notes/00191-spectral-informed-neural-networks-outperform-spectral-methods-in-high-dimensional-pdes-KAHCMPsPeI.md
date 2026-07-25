# Spectral-Informed Neural Networks Outperform Spectral methods in High-dimensional PDEs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: KAHCMPsPeI
- Authors: Tianchi Yu; Ivan Oseledets
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Spectral method;Physics-informed neural networks;Spectral-informed neural networks;High-dimensional PDEs.
- Source URL: https://openreview.net/forum?id=KAHCMPsPeI
- PDF URL: https://openreview.net/pdf?id=KAHCMPsPeI

## Abstract

For low-dimensional problems ($d\leq3$), spectral methods can achieve exceptionally high accuracy. For middle-dimensional problems ($4 \leq d \lesssim 10$), spectral methods remain feasible through specific techniques such as sparse grids or hyperbolic cross. However, for high-dimensional problems ($d\gg 10$), spectral methods suffer frome the curse of dimensionality. Physics-informed neural networks (PINNs) have emerged as a promising approach to overcome this challenge, offering scalability to high dimensions, but often suffer from limited accuracy and efficiency. Recently proposed spectral-informed neural networks (SINNs) combine spectral methods with PINNs, operating directly in the spectral domain to avoid spatial derivative computations and to reduce memory consumption. In this work, we introduce Modified SINNs, which integrate coefficient decay scaling and basis embeddings motivated by harmonic analysis to enhance accuracy in high-dimensional problems and enable accurate approximation of unknown spectral coefficients. Numerical experiments on steady and time-dependent partial differential equations demonstrate that Modified SINNs outperform sparse grid spectral methods on middle-dimensional problems with incomplete spectral information and achieve superior accuracy compared to PINNs on high-dimensional problems.

## One-Sentence Claim

Modified Spectral-Informed Neural Networks combine harmonic-analysis-inspired spectral structure with PINN scalability to outperform spectral methods and PINNs on higher-dimensional PDEs.

## Problem

Classical spectral methods are highly accurate in low dimensions but suffer from the curse of dimensionality, while PINNs scale to high dimensions but often lack accuracy and efficiency.

## Core Contribution

The paper introduces Modified SINNs with coefficient decay scaling and basis embeddings that improve spectral-domain neural approximation of unknown coefficients in high-dimensional PDEs.

## Method

Modified SINNs operate in the spectral domain to avoid spatial derivative computation and reduce memory use, then add harmonic-analysis-motivated coefficient scaling and basis embeddings to better approximate incomplete or unknown spectral information.

## Experiments and Evidence

The abstract reports numerical experiments on steady and time-dependent PDEs where Modified SINNs beat sparse-grid spectral methods in middle-dimensional settings with incomplete spectral information and outperform PINNs in high-dimensional regimes.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: PDE families, dimension ranges, boundary conditions, basis choices, training stability, and comparison fairness against tuned spectral/PINN baselines.

## Deep Themes

- Hybridizing classical numerical structure with neural scalability.
- Spectral-domain learning can avoid expensive derivative computation.
- High-dimensional scientific ML depends on preserving analytic priors.

## Subthemes

- High-dimensional PDEs.
- Spectral methods.
- Physics-informed neural networks.
- Harmonic analysis.
- Basis embeddings.
- Scientific computing.

## Connections to Other Papers

Connects to GFG, CoCLD, and SDEVI through scientific dynamics modeling, and to theory/prior papers that use mathematical structure to improve neural approximation.

## Notes for Cross-Paper Synthesis

Modified SINNs add a scientific-computing example of the hybrid-prior theme: neural models work best when they inherit the right structure from established numerical methods.
