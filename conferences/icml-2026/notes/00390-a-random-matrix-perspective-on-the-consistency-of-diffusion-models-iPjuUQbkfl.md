# A Random Matrix Perspective on the Consistency of Diffusion Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: iPjuUQbkfl
- Authors: Binxu Wang; Jacob A Zavatone-Veth; Cengiz Pehlevan
- Primary area: deep_learning->theory
- Keywords: random matrix theory;diffusion model;flow matching;probability flow ode;deterministic equivalence;Balakrishnan identity;consistency;bias variance
- Source URL: https://openreview.net/forum?id=iPjuUQbkfl
- PDF URL: https://openreview.net/pdf?id=iPjuUQbkfl

## Abstract

Diffusion models trained on different, non-overlapping subsets of a dataset often produce strikingly similar outputs when given the same noise seed. We trace this consistency to a simple linear effect: the shared Gaussian statistics across splits already predict much of the generated images. To formalize this, we develop a random matrix theory (RMT) framework that quantifies how finite datasets shape the expectation and variance of the learned denoiser and sampling map in the linear setting. For expectations, sampling variability acts as a renormalization of the noise level through a self-consistent relation $\sigma^2\to\kappa(\sigma^2)$, explaining why limited data overshrink low-variance directions and pull samples toward the dataset mean. For fluctuations, our variance formulas reveal three key factors behind cross-split disagreement: \textit{anisotropy} across eigenmodes, \textit{inhomogeneity} across inputs, and overall scaling with dataset size. Extending deterministic-equivalence tools to fractional matrix powers further allows us to analyze entire sampling trajectories. The theory sharply predicts the behavior of linear diffusion models, and we validate its predictions on UNet and DiT architectures in their non-memorization regime, identifying where and how samples deviates across training data split. This provides a principled baseline for reproducibility in diffusion training, linking spectral properties of data to the stability of generative outputs.

## One-Sentence Claim

Random matrix theory explains why diffusion models trained on disjoint data splits can generate similar outputs: shared Gaussian statistics dominate much of the learned denoising map in non-memorization regimes.

## Problem

Diffusion models trained on different non-overlapping subsets often produce similar outputs from the same noise seed. This consistency is surprising because the training data differ, and it raises questions about reproducibility, memorization, and dataset-dependent variance.

The paper asks which data spectral properties determine the expectation and fluctuation of learned denoisers and sampling trajectories.

## Core Contribution

The paper develops an RMT framework for linear diffusion models that quantifies how finite datasets shape the expectation and variance of the learned denoiser and sampling map. It shows that sampling variability renormalizes noise level through a self-consistent sigma-squared to kappa relation, causing overshrinkage of low-variance directions and drift toward the dataset mean.

For fluctuations, it identifies anisotropy across eigenmodes, input inhomogeneity, and dataset-size scaling as drivers of cross-split disagreement. It extends deterministic-equivalence tools to fractional matrix powers to analyze full sampling trajectories.

## Method

The theory studies linear denoisers and sampling maps under finite dataset sampling. Random matrix tools compute deterministic equivalents for expectations and variances, including trajectory-level quantities via fractional matrix powers.

The paper then validates predictions on UNet and DiT architectures in non-memorization regimes to see where the linear theory remains predictive.

## Experiments and Evidence

Evidence reported in the abstract:

- RMT framework for expectation and variance of learned denoisers and sampling maps.
- Self-consistent noise-renormalization relation sigma^2 -> kappa(sigma^2).
- Variance formulas identifying anisotropy, input inhomogeneity, and dataset size as disagreement factors.
- Analysis of entire sampling trajectories.
- Sharp predictions for linear diffusion models.
- Validation on UNet and DiT architectures in non-memorization regimes.
- Identification of where samples deviate across data splits.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: linear model assumptions, validation datasets, and non-memorization criterion.

## Limits and Failure Modes

- Linear diffusion theory may not capture strongly nonlinear or memorizing regimes.
- Gaussian-statistics explanations may understate semantic or architectural effects.
- Dataset mean attraction can be task-dependent and may not explain all consistency.
- Validation on UNet/DiT needs careful interpretation because theory is approximate there.

## Deep Themes

**Generative consistency has spectral roots.** Shared covariance and eigenstructure can dominate sample behavior across dataset splits.

**Finite data renormalizes sampling dynamics.** Limited data effectively changes the noise scale and shrinks low-variance directions.

**Reproducibility can be quantified.** The paper links cross-run agreement to analyzable variance terms.

## Subthemes

- Random matrix theory for diffusion.
- Cross-split generation consistency.
- Noise-level renormalization.
- Spectral anisotropy and variance.
- Non-memorization regime analysis.

## Connections to Other Papers

Connects to KPE/KTS, Weak Diffusion Priors, MOG, Flow Matching, and LM Memorization Capacity. It adds a spectral reproducibility lens to the corpus's generative-model trajectory and memorization themes.

## Notes for Cross-Paper Synthesis

This paper deepens the generative-model theory theme: diffusion behavior can often be explained by data spectrum and finite-sample effects before invoking richer semantic explanations.
