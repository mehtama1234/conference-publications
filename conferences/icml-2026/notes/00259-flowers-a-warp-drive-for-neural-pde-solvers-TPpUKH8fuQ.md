# Flowers: A Warp Drive for Neural PDE Solvers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: TPpUKH8fuQ
- Authors: Till Muser; Alexandra Spitzer; Matti Lassas; Maarten V. de Hoop; Ivan Dokmanić
- Primary area: deep_learning->everything_else
- Keywords: AI4Science;SciML;PDEs;Operator Learning;Flows;Waves;Fluid Dynamics
- Source URL: https://openreview.net/forum?id=TPpUKH8fuQ
- PDF URL: https://openreview.net/pdf?id=TPpUKH8fuQ

## Abstract

We introduce Flower, a neural architecture for learning PDE solution operators built entirely from multihead warps. Aside from pointwise channel mixing and a multiscale scaffold, Flowers use no Fourier multipliers, no dot-product attention, and no convolutional mixing. Each head predicts a displacement field and warps the mixed input features. Motivated by physics and computational efficiency, displacements are predicted pointwise, without any spatial aggregation, and nonlocality enters *only* through sparse sampling at source coordinates, *one* per head. Stacking warps in multiscale residual blocks yields Flowers, which implement adaptive, global interactions at linear cost. We theoretically motivate this design through three complementary lenses: flow maps for conservation laws, waves in inhomogeneous media, and a kinetic-theoretic continuum limit. Flowers achieve excellent performance on a broad suite of 2D and 3D time-dependent PDE benchmarks, particularly flows and waves. A compact 17M-parameter model consistently outperforms Fourier, convolution, and attention-based baselines of similar size, while a 150M-parameter variant improves over recent transformer-based foundation models with much more parameters, data, and training compute.

## One-Sentence Claim

Flowers replace Fourier, attention, and convolutional mixing with stacked multihead feature warps, yielding adaptive global PDE interactions at linear cost.

## Problem

Neural PDE solvers need to model nonlocal interactions in flows, waves, and other time-dependent systems. Existing operator-learning architectures often rely on Fourier multipliers, convolutions, or attention. These can be powerful, but they may impose costly or mismatched mixing patterns, especially for adaptive propagation phenomena in heterogeneous media.

The paper asks whether spatial interaction can be built from learned warping operations that better match physical transport and wave propagation while remaining computationally efficient.

## Core Contribution

The paper introduces Flower, a neural operator architecture built around multihead warps:

- Each head predicts a displacement field.
- Mixed input features are sampled at displaced source coordinates.
- Displacements are predicted pointwise, without spatial aggregation.
- Nonlocality enters through sparse source-coordinate sampling, one source per head.
- Multiscale residual stacking turns these local warp heads into adaptive global interactions.

The result is a PDE solver family that avoids Fourier multipliers, dot-product attention, and convolutional spatial mixing while claiming strong accuracy and linear cost.

## Method

Flowers combine pointwise channel mixing, learned displacement fields, sparse coordinate sampling, and multiscale residual blocks. The physical motivation is that many PDE dynamics can be understood through flow maps, wave travel through inhomogeneous media, and kinetic transport limits.

Architecturally, each head acts like a learned transport operator: it decides where information should be pulled from, then warps features accordingly. Stacked over scales, these sparse learned transports create long-range dependencies without dense attention.

## Experiments and Evidence

Evidence reported in the abstract:

- Broad 2D and 3D time-dependent PDE benchmarks.
- Strong results particularly on flows and waves.
- A 17M-parameter model outperforming Fourier, convolutional, and attention baselines of similar size.
- A 150M-parameter variant outperforming recent transformer-based foundation models that use more parameters, data, and training compute.
- Theoretical motivation from conservation-law flow maps, inhomogeneous wave propagation, and kinetic continuum limits.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark names, boundary-condition handling, interpolation scheme, stability over rollout horizons, and exact compute comparisons.

## Limits and Failure Modes

- Warping depends on interpolation and coordinate sampling quality; sharp discontinuities or complex boundaries may be challenging.
- Pointwise displacement prediction may underfit cases where displacement itself requires nonlocal context.
- The abstract emphasizes flows and waves; other PDE classes may benefit less.
- Claims against foundation models require careful normalization for training data, resolution, rollout horizon, and compute.

## Deep Themes

**Physics-inspired operators can replace generic token mixing.** The architecture turns transport/warping into the primitive interaction rather than applying attention or convolution by default.

**Sparse adaptive nonlocality is a recurring efficiency pattern.** Flowers use one source coordinate per head, echoing broader attempts to get global effects without dense quadratic interactions.

**Operator learning is moving toward mechanism-matched architectures.** The design is justified through PDE flow maps and wave propagation, not only benchmark performance.

## Subthemes

- Learned displacement fields as PDE interaction primitives.
- Multiscale residual composition for global reach.
- Linear-cost neural operators.
- Flow and wave dynamics as architecture guides.
- Sparse sampling as controlled nonlocality.

## Connections to Other Papers

Connects to WLA/ERA5-Latent, PWC-Diff, SDEVI, and other scientific ML papers that encode physical structure into learned representations. It also links to efficiency papers such as WBMM and WeDLM because the contribution is partly about replacing costly generic mixing with a hardware- or dynamics-aligned primitive.

## Notes for Cross-Paper Synthesis

Flowers strengthen the cross-corpus theme that scientific foundation models are not merely larger Transformers. Many 2026 papers seek domain-native primitives: warps for PDEs, latent climate fields for weather, wireless priors for radio signals, and directional transition objectives for molecular control.
