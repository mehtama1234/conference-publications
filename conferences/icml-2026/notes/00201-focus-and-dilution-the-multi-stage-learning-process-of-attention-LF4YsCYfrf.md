# Focus and Dilution: The Multi-stage Learning Process of Attention

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LF4YsCYfrf
- Authors: Zheng-An Chen; Pengxiao Lin; Zhi-Qin John Xu; Tao Luo
- Primary area: deep_learning->theory
- Keywords: Attention mechanism;Training dynamics;Multi-stage analysis;Condensation
- Source URL: https://openreview.net/forum?id=LF4YsCYfrf
- PDF URL: https://openreview.net/pdf?id=LF4YsCYfrf

## Abstract

Transformer-based models have achieved remarkable success across a wide range of domains, yet our understanding of their training dynamics remains limited. In this work, we identify a recurrent focus–dilution cycle in attention learning and provide a rigorous explanation in a one-layer Transformer setting for Markovian data via gradient-flow analysis. Using stage-wise linearization around critical points, we show that a single focus–dilution cycle can be decomposed into a sequence of distinct stages. First, embedding and projection rapidly condense to a rank-one structure, while attention parameters remain effectively frozen. Then, the attention parameters begin to increase, inducing a frequency-driven focus toward high-frequency tokens. As attention continues to evolve, it generates next-order perturbations in embeddings, leading to a mass-redistribution mechanism that progressively dilutes this focus. Finally, small asymmetries among low-frequency tokens lift a degenerate critical point, opening new embedding directions and initiating the next cycle. Experiments on synthetic Markovian data as well as WikiText and TinyStories corroborate the predicted stages and cyclical dynamics.

## One-Sentence Claim

Attention learning follows recurrent focus-dilution cycles in which embeddings first condense, attention focuses on high-frequency tokens, and later perturbations redistribute mass to reopen new embedding directions.

## Problem

Transformers are widely used, but their training dynamics remain poorly understood, especially how attention and embeddings co-evolve over time.

## Core Contribution

The paper provides a rigorous gradient-flow explanation of focus-dilution cycles in a one-layer Transformer trained on Markovian data, supported by stage-wise linearization around critical points.

## Method

The analysis decomposes a cycle into stages: rapid rank-one condensation of embeddings/projections while attention is frozen, attention growth and frequency-driven focus, next-order embedding perturbations that dilute focus, and asymmetry-driven escape from degenerate critical points into new embedding directions.

## Experiments and Evidence

The abstract reports experiments on synthetic Markovian data, WikiText, and TinyStories that corroborate the predicted stages and cyclical dynamics.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: one-layer assumptions, Markovian data model, extension to deep Transformers, empirical diagnostics, and whether focus-dilution cycles predict downstream generalization.

## Deep Themes

- Transformer learning can be stage-wise and cyclical rather than monotonic.
- Frequency structure influences attention focus during training.
- Critical-point geometry shapes representation emergence.

## Subthemes

- Attention mechanism.
- Training dynamics.
- Gradient flow.
- Condensation.
- Markovian data.
- Rank-one structure.

## Connections to Other Papers

Connects to power-law compositional reasoning and NSE theory through staged capability emergence, and to PoPE/Robust Filter Attention through mechanistic analysis of attention behavior.

## Notes for Cross-Paper Synthesis

This paper adds a dynamics-of-learning theme: model capabilities may emerge through repeated phases of compression, focus, redistribution, and symmetry breaking.
