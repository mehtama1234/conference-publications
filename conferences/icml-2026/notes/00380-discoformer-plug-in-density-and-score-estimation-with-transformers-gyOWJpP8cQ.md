# DiScoFormer: Plug-In Density and Score Estimation with Transformers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: gyOWJpP8cQ
- Authors: Vasily Ilin; Peter Sushko; Ranjay Krishna
- Primary area: general_machine_learning->kernel_methods
- Keywords: density estimation;score estimation;transformers;kernel methods;equivariant networks;nonparametric statistics
- Source URL: https://openreview.net/forum?id=gyOWJpP8cQ
- PDF URL: https://openreview.net/pdf?id=gyOWJpP8cQ

## Abstract

Estimating probability density and its score from samples remains a core problem in generative modeling, Bayesian inference, and kinetic theory. Existing methods are bifurcated: classical kernel density estimators (KDE) generalize across distributions but suffer from the curse of dimensionality, while modern neural score models achieve high precision but require retraining for every target distribution. We introduce DiScoFormer (Density and Score Transformer), a ``train-once, infer-anywhere" equivariant Transformer that maps i.i.d. samples to both density values and score vectors, generalizing across distributions and sample sizes. Analytically, we prove that self-attention can recover normalized KDE, establishing it as a functional generalization of kernel methods; empirically, individual attention heads learn multi-scale, kernel-like behaviors. The model converges faster and achieves higher precision than KDE for density estimation, and provides a high-fidelity plug-in score oracle for score-debiased KDE, Fisher information computation, and Fokker-Planck-type PDEs.

## One-Sentence Claim

DiScoFormer trains one equivariant Transformer to map samples to density and score estimates across distributions, acting as a reusable neural generalization of KDE.

## Problem

Density and score estimation are central to generative modeling, Bayesian inference, and kinetic theory. Classical KDE generalizes across distributions but scales poorly with dimension, while neural score models can be accurate but usually require retraining for each target distribution.

The paper asks whether a model can be trained once and then act as a plug-in density/score estimator for new sample sets and sample sizes.

## Core Contribution

The contribution is DiScoFormer, an equivariant Transformer that maps i.i.d. samples to density values and score vectors for new distributions. Analytically, the paper proves self-attention can recover normalized KDE, positioning attention as a functional generalization of kernel methods.

Empirically, attention heads learn multi-scale kernel-like behavior, and the model provides a high-fidelity plug-in score oracle for downstream statistical and PDE tasks.

## Method

DiScoFormer treats a sample set as an exchangeable input and uses equivariant self-attention to aggregate sample information. The model outputs density and score estimates at query points or sample locations while generalizing across distributions.

The theoretical bridge to KDE explains how attention can implement kernel-like weighting, while learned heads can adapt bandwidths or scales beyond fixed classical kernels.

## Experiments and Evidence

Evidence reported in the abstract:

- Train-once, infer-anywhere density and score estimation.
- Generalization across distributions and sample sizes.
- Proof that self-attention can recover normalized KDE.
- Attention heads learn multi-scale kernel-like behaviors.
- Faster convergence and higher precision than KDE for density estimation.
- Plug-in score oracle for score-debiased KDE, Fisher information computation, and Fokker-Planck-type PDEs.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: dimensionality, training distribution family, query interface, and score-estimation calibration.

## Limits and Failure Modes

- Generalization depends on whether training distribution families cover test distributions.
- High-dimensional score estimation may still be difficult outside learned regimes.
- Equivariance handles sample exchangeability but not all domain symmetries.
- Plug-in downstream use may be sensitive to score bias in tails or low-density regions.

## Deep Themes

**Attention can subsume classical estimators.** The paper makes a direct bridge from KDE to self-attention.

**Train-once statistical operators are emerging.** DiScoFormer learns an estimator that operates on new datasets rather than a model tied to one dataset.

**Density and score become reusable infrastructure.** Plug-in scores support inference, information computation, and PDE dynamics.

## Subthemes

- Equivariant set Transformer.
- Density and score estimation.
- Attention as learned KDE.
- Multi-scale kernel heads.
- Plug-in statistical operators.

## Connections to Other Papers

Connects to Distribution Transformers, Auxiliary MCMC, Jacobi Spectral Reconstruction, LoRFS, and probabilistic inference papers. It also links to theory-unifies-practice work because it connects attention mechanisms to classical kernel estimation.

## Notes for Cross-Paper Synthesis

DiScoFormer reinforces a major pattern: Transformers are increasingly treated as reusable algorithmic operators over structured inputs, not only as sequence models trained for one task.
