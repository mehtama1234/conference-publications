# Efficient Diffusion Models under Nonconvex Equality and Inequality constraints via Landing

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 6VEqdKmfKh
- Authors: Kijung Jeon; Michael Muehlebach; Molei Tao
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: constrained diffusion models;nonconvex constraints;underdamped Langevin dynamics;landing mechanism
- Source URL: https://openreview.net/forum?id=6VEqdKmfKh
- PDF URL: https://openreview.net/pdf?id=6VEqdKmfKh

## Abstract

Generative modeling within constrained sets is essential for scientific and engineering applications involving physical, geometric, or safety requirements (e.g., molecular generation, robotics). We present a unified framework for constrained diffusion models on generic nonconvex feasible sets $\Sigma$ that simultaneously enforces equality and inequality constraints throughout the diffusion process. Our framework incorporates both overdamped and underdamped dynamics for forward and backward sampling. A key algorithmic innovation is a computationally efficient landing mechanism that replaces costly and often ill-defined projections onto $\Sigma$, ensuring feasibility without iterative Newton solves or projection failures. By leveraging underdamped dynamics, we accelerate mixing toward the prior distribution, effectively alleviating the high simulation costs typically associated with constrained diffusion. Empirically, this approach reduces function evaluations and memory usage during both training and inference while preserving sample quality. On benchmarks featuring equality and mixed constraints, our method achieves comparable sample quality to state-of-the-art baselines while significantly reducing computational cost, providing a practical and scalable solution for diffusion on nonconvex feasible sets.

## One-Sentence Claim

Landing-based constrained diffusion efficiently samples within nonconvex feasible sets by enforcing equality and inequality constraints without expensive projection solves.

## Problem

Scientific and engineering generation often requires physical, geometric, or safety constraints, but constrained diffusion on nonconvex feasible sets can be costly because projections may be expensive, ill-defined, or fail.

## Core Contribution

The paper presents a unified constrained diffusion framework for generic nonconvex feasible sets with both equality and inequality constraints, using a landing mechanism and overdamped/underdamped dynamics.

## Method

The landing mechanism replaces iterative projection onto the feasible set during forward/backward diffusion. Underdamped dynamics accelerate mixing toward the prior, reducing simulation cost while maintaining feasibility.

## Experiments and Evidence

The abstract reports comparable sample quality to state-of-the-art baselines on equality and mixed-constraint benchmarks, while reducing function evaluations and memory during training and inference.

## Limits and Failure Modes

ArXiv searches for this batch hit HTTP 429, so no local PDF is available yet. Details still need checking: exact landing update, constraint regularity assumptions, benchmark domains, and behavior with tight or nearly infeasible constraints.

## Deep Themes

- Generative models for science must respect feasibility throughout sampling.
- Projection-free constraint handling can make constrained generation practical.
- Diffusion research is moving from unconstrained image generation toward constrained scientific and engineering design.

## Subthemes

- Constrained diffusion.
- Nonconvex feasible sets.
- Equality and inequality constraints.
- Landing dynamics.
- Underdamped Langevin dynamics.
- Projection-free sampling.

## Connections to Other Papers

Connects to quotient-space diffusion, protein generation, and latent spherical flow policy through geometry-aware generation. It also links to HDFlow and robotics papers where generated plans must remain feasible.

## Notes for Cross-Paper Synthesis

This paper adds a constraint-first generative modeling theme: sample quality is not enough when domains impose hard physical or safety feasibility requirements.
