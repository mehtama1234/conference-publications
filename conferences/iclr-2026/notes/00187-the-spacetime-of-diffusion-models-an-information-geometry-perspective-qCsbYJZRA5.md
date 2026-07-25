# The Spacetime of Diffusion Models: An Information Geometry Perspective

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: qCsbYJZRA5
- Authors: Rafal Karczewski; Markus Heinonen; Alison Pouplin; Søren Hauberg; Vikas K Garg
- Primary area: generative models
- Keywords: diffusion models;information geometry
- Source URL: https://openreview.net/forum?id=qCsbYJZRA5
- PDF URL: https://openreview.net/pdf?id=qCsbYJZRA5

## Abstract

We present a novel geometric perspective on the latent space of diffusion models. We first show that the standard pullback approach, utilizing the deterministic probability flow ODE decoder, is fundamentally flawed. It provably forces geodesics to decode as straight segments in data space, effectively ignoring any intrinsic data geometry beyond the ambient Euclidean space. Complementing this view, diffusion also admits a stochastic decoder via the reverse SDE, which enables an information geometric treatment with the Fisher-Rao metric. However, a choice of $\mathbf{x}_T$ as the latent representation collapses this metric due to memorylessness. We address this by introducing a latent spacetime $\mathbf{z}=(\mathbf{x}_t,t)$ that indexes the family of denoising distributions $p(\mathbf{x}_0 | \mathbf{x}_t)$ across all noise scales, yielding a nontrivial geometric structure. We prove these distributions form an exponential family and derive simulation-free estimators for curve lengths, enabling efficient geodesic computation. The resulting structure induces a principled Diffusion Edit Distance, where geodesics trace minimal sequences of noise and denoise edits between data. We also demonstrate benefits for transition path sampling in molecular systems, including constrained variants such as low-variance transitions and region avoidance. Code is available at: https://github.com/rafalkarczewski/spacetime-geometry.

## One-Sentence Claim

Diffusion latent geometry becomes meaningful when represented as spacetime pairs `(x_t, t)`, enabling Fisher-Rao geodesics and a principled Diffusion Edit Distance.

## Problem

Standard pullback geometry through deterministic probability-flow ODE decoders can collapse diffusion latent geometry into straight data-space segments, ignoring intrinsic data structure. Using only terminal noise `x_T` as the latent also collapses stochastic-decoder Fisher-Rao geometry because of memorylessness.

## Core Contribution

The paper introduces latent spacetime `z=(x_t,t)` as the representation for diffusion geometry, proves denoising distributions form an exponential family, derives simulation-free curve-length estimators, and defines Diffusion Edit Distance through geodesics of noise/denoise edits.

## Method

The method views each spacetime point as indexing a denoising distribution `p(x_0 | x_t)`. It equips this family with information-geometric structure via the Fisher-Rao metric, estimates curve lengths without simulation, and computes geodesics that describe minimal edit paths. It also applies constrained variants to molecular transition path sampling.

## Experiments and Evidence

The abstract reports benefits for molecular transition path sampling, including low-variance transitions and region avoidance. The main evidence is theoretical: flaws in deterministic pullback geometry, exponential-family structure, and efficient geodesic estimators.

## Limits and Failure Modes

Information geometry may be expensive or hard to approximate accurately for large diffusion models. Practical value depends on estimator variance, discretization, and how edit distance correlates with semantic similarity. Full-text review should check proofs, estimator assumptions, molecular benchmarks, and comparisons with interpolation or optimal-transport distances.

## Deep Themes

- Information geometry of generative models.
- Diffusion latent spacetime.
- Geodesic edit distances.
- Molecular transition path sampling.

## Subthemes

- Fisher-Rao metric for reverse SDE decoders.
- Probability-flow ODE geometry failure.
- Exponential-family denoising distributions.
- Simulation-free curve length estimation.
- Region-avoidant diffusion paths.

## Connections to Other Papers

Connects to quotient-space diffusion and RoSE through geometry-aware generative modeling, to protein/molecular generation papers through scientific transition paths, and to representation-geometry themes where latent space needs task-appropriate metrics.

## Notes for Cross-Paper Synthesis

This paper argues that representation choice determines whether geometry is meaningful. A latent coordinate alone may be insufficient; time/noise scale is part of the semantic state.
