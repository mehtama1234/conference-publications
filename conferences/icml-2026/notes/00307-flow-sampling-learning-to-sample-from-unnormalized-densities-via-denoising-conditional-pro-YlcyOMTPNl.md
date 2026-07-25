# Flow Sampling : Learning to Sample from Unnormalized Densities via Denoising Conditional Processes

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YlcyOMTPNl
- Authors: Aaron J Havens; Brian Karrer; Neta Shaul
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Diffusion samplers;Boltzmann Sampling;Flow Matching;Unnormalized density sampling;diffusion models
- Source URL: https://openreview.net/forum?id=YlcyOMTPNl
- PDF URL: https://openreview.net/pdf?id=YlcyOMTPNl

## Abstract

Sampling from unnormalized densities is analogous to the generative modeling problem, but the target distribution is defined by a known energy function instead of data samples. Because evaluating the energy function is often costly, a primary challenge is to learn an efficient sampler. We introduce Flow Sampling, a framework built on diffusion models and flow matching for the data-free setting. Our training objective is conditioned on a noise sample and regresses onto a denoising diffusion drift constructed from the energy function. In contrast, diffusion models' objective is conditioned on a data sample and regresses onto a noising diffusion drift. We utilize the interpolant process to minimize the number of energy function evaluations during training, resulting in an efficient and scalable method for sampling unnormalized densities. Furthermore, our formulation naturally extends to Riemannian manifolds, enabling diffusion-based sampling in geometries beyond Euclidean space. We derive a closed-form formula for the conditional drift on constant curvature manifolds, including hyperspheres and hyperbolic spaces. We evaluate Flow Sampling on synthetic energy benchmarks, small peptides, large-scale amortized molecular conformer generation, and distributions supported on the sphere, demonstrating strong empirical performance.

## One-Sentence Claim

Flow Sampling trains diffusion/flow-matching samplers for unnormalized energy densities by regressing denoising conditional drifts while minimizing expensive energy evaluations.

## Problem

Sampling from unnormalized densities appears in Boltzmann sampling and molecular modeling, where the target is defined by an energy function rather than data samples. Energy evaluations can be costly, so samplers must be efficient to train and deploy.

The paper asks how to adapt diffusion and flow matching to the data-free setting where the only target information is an energy function.

## Core Contribution

The paper introduces Flow Sampling, a framework for learning samplers from unnormalized densities. Its objective conditions on a noise sample and regresses onto a denoising diffusion drift constructed from the energy function, contrasting with standard diffusion models that condition on data and regress noising drifts.

It uses an interpolant process to reduce the number of energy-function evaluations. The formulation also extends to Riemannian manifolds and derives closed-form conditional drifts on constant-curvature manifolds such as spheres and hyperbolic spaces.

## Method

Flow Sampling builds a denoising conditional process from the known energy. Training learns the drift field needed to move noise toward samples from the unnormalized target. The interpolant process amortizes or reduces energy calls during training.

For non-Euclidean targets, the method adapts the drift formula to manifold geometry, including closed forms for constant curvature spaces.

## Experiments and Evidence

Evidence reported in the abstract:

- Synthetic energy benchmarks.
- Small peptide sampling.
- Large-scale amortized molecular conformer generation.
- Distributions supported on the sphere.
- Riemannian manifold extension with closed-form drifts on hyperspheres and hyperbolic spaces.
- Strong empirical performance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: energy-call counts, baselines, conformer metrics, manifold implementation, and scalability limits.

## Limits and Failure Modes

- Energy functions may be expensive or noisy enough that drift construction remains costly.
- Learned samplers can bias rare modes if training coverage is weak.
- Manifold extensions may require exact geometry and tractable exponential/log maps.
- Molecular energy landscapes can have many metastable states that stress amortized samplers.

## Deep Themes

**Generative modeling and energy-based sampling are converging.** Flow Sampling applies diffusion/flow matching ideas when the target is known by energy, not data.

**Energy calls are the scarce resource.** The algorithm is shaped around minimizing expensive target evaluations.

**Geometry matters for sampling domains.** Riemannian extensions make the sampler respect non-Euclidean support.

## Subthemes

- Unnormalized density sampling.
- Denoising conditional processes.
- Flow matching without data samples.
- Riemannian diffusion drifts.
- Molecular conformer generation.

## Connections to Other Papers

Connects to Dimension-Free Diffusion Sampling, SRMC, Manifold Perturbations, TD3B, and scientific generative modeling. It also links to Flowers and DIGL through geometry-aware operators on non-Euclidean or structured domains.

## Notes for Cross-Paper Synthesis

Flow Sampling adds a major scientific-generation pattern: use learned flows not only to imitate datasets but to amortize expensive physical or energy-defined sampling problems.
