# Walrus: A Cross-domain Foundation Model for Continuum Dynamics

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kcyOjXoUZu
- Authors: Michael McCabe; Payel Mukhopadhyay; Tanya Marwah; Bruno Régaldo-Saint Blancard; François Rozet; Cristiana Diaconu; Lucas Thibaut Meyer; Kaze W. K. Wong; Mohammad-Hadi Sotoudeh; Alberto Bietti; Irina Espejo Morales; Rio Alexa Fear; Siavash Golkar; Tom Hehir; Keiya Hirashima; Geraud Krawezik; Francois Lanusse; Rudy Morel; Ruben Ohana; Liam Holden Parker; Mariel Pettee; Jeff Shen; Kyunghyun Cho; Miles Cranmer; Shirley Ho
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: continuum dynamics;physics;PDEs;foundation model;stability;distributed training;fluids
- Source URL: https://openreview.net/forum?id=kcyOjXoUZu
- PDF URL: https://openreview.net/pdf?id=kcyOjXoUZu

## Abstract

Foundation models have transformed machine learning for language and vision, but achieving comparable impact in physical simulation remains a challenge. Data heterogeneity and unstable long-term dynamics inhibit learning from sufficiently diverse dynamics, while varying resolutions and dimensionalities challenge efficient training on modern hardware. Through empirical and theoretical analysis, we incorporate new approaches to mitigate these obstacles, including a harmonic-analysis–based stabilization method, load-balanced distributed 2D-3D training strategies, and compute-adaptive tokenization. Using these tools, we develop Walrus, a transformer-based foundation model developed primarily for fluid-like continuum dynamics. Walrus is pretrained on nineteen diverse scenarios spanning astrophysics, geoscience, rheology, plasma physics, acoustics, and classical fluids. Experiments show that Walrus outperforms prior foundation models on both short- and long-term prediction horizons on downstream tasks and across the breadth of pretraining data, while ablation studies confirm the value of our contributions to forecast stability, training throughput, and transfer performance over conventional approaches.

## One-Sentence Claim

Walrus is a cross-domain Transformer foundation model for fluid-like continuum dynamics, using stabilization, 2D-3D distributed training, and adaptive tokenization to improve transfer and long-horizon prediction.

## Problem

Foundation models have transformed language and vision, but physical simulation remains difficult because dynamics data are heterogeneous, long-term rollouts can be unstable, and resolutions/dimensionalities vary across domains.

The paper asks how to pretrain one model across many continuum-dynamics regimes without losing stability or hardware efficiency.

## Core Contribution

The contribution is Walrus, a Transformer-based foundation model for continuum dynamics pretrained on 19 diverse scenarios spanning astrophysics, geoscience, rheology, plasma physics, acoustics, and classical fluids.

The paper introduces harmonic-analysis-based stabilization, load-balanced distributed 2D-3D training strategies, and compute-adaptive tokenization to address stability, throughput, and heterogeneous-resolution challenges.

## Method

Walrus tokenizes continuum fields in a compute-adaptive way, trains across 2D and 3D scenarios with load balancing, and incorporates stabilization inspired by harmonic analysis to improve long-term forecasting.

The architecture is Transformer-based and targets fluid-like physical fields across domains rather than a single PDE benchmark.

## Experiments and Evidence

Evidence reported in the abstract:

- Pretraining on 19 diverse continuum-dynamics scenarios.
- Domains include astrophysics, geoscience, rheology, plasma physics, acoustics, and classical fluids.
- Outperforms prior foundation models on short- and long-term prediction horizons.
- Stronger performance across downstream tasks and pretraining-data breadth.
- Ablations confirm benefits for forecast stability, training throughput, and transfer performance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: datasets, tokenization scheme, stability method, and downstream benchmarks.

## Limits and Failure Modes

- Fluid-like continuum focus may not transfer to discontinuous, contact-rich, or particle systems.
- Cross-domain pretraining can hide uneven performance across rare regimes.
- Long-horizon stability may still degrade outside pretraining distributions.
- Large distributed training may be difficult to reproduce.

## Deep Themes

**Scientific foundation models need stability machinery.** Long-horizon dynamics require more than scaling data and Transformer size.

**Heterogeneous physics requires adaptive tokenization.** Variable resolution and dimensionality become core modeling problems.

**Cross-domain simulation is a systems problem.** Load balancing and distributed 2D-3D training are part of the model recipe.

## Subthemes

- Continuum-dynamics foundation model.
- Harmonic-analysis stabilization.
- 2D-3D distributed training.
- Compute-adaptive tokenization.
- Fluid-like physical forecasting.

## Connections to Other Papers

Connects to LASER, ReViT, LoRFS, Generative Filtering, NeuronCtrl, and Dirac-Frenkel-Onsager dynamics. It represents the large-scale foundation-model version of the scientific-ML thread.

## Notes for Cross-Paper Synthesis

Walrus shows scientific foundation models becoming full-stack efforts: data heterogeneity, numerical stability, tokenization, and distributed training all have to be solved together.
