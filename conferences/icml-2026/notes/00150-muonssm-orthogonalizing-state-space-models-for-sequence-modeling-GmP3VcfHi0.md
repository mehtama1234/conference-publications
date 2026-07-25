# MuonSSM: Orthogonalizing State Space Models for Sequence Modeling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GmP3VcfHi0
- Authors: Thai Khanh Nguyen; Vo Ngoc Bich Uyen; Thieu Vo; Tan Minh Nguyen; Cuong Pham
- Primary area: deep_learning->sequential_models_time_series
- Keywords: State Space Models;Geometric Conditioning;Momentum-Augmented Dynamics;Associative Memory;Long-Sequence Modeling
- Source URL: https://openreview.net/forum?id=GmP3VcfHi0
- PDF URL: https://openreview.net/pdf?id=GmP3VcfHi0

## Abstract

State space models (SSMs) have emerged as efficient linear-time alternatives to attention for long-sequence modeling. However, existing SSMs often suffer from instability and memory degradation over extended horizons due to poorly conditioned first-order updates and unbalanced update geometry. We introduce MuonSSM, a general framework that stabilizes SSM training by explicitly conditioning the geometry of memory updates rather than the recurrent transition matrix. MuonSSM augments SSMs with a momentum-based pathway and a lightweight Newton-Schulz transformation on low-rank input injections, yielding bounded and spectrally conditioned updates while preserving parallel scan complexity. Theory shows that MuonSSM improves gradient propagation, mitigates spectral amplification, and enriches memory representations over long horizons. Extensive experiments across language, vision, and time-series benchmarks show consistent gains in accuracy, robustness, and long-context performance when integrated into diverse SSM backbones. These results establish geometric conditioning of updates as a principled pathway to stable, scalable sequence modeling.

## One-Sentence Claim

MuonSSM stabilizes state-space models by geometrically conditioning memory updates with momentum pathways and Newton-Schulz transformations while preserving parallel scan efficiency.

## Problem

SSMs are efficient for long sequences but can suffer instability and memory degradation from poorly conditioned first-order updates and unbalanced update geometry.

## Core Contribution

The paper proposes a general framework for conditioning SSM update geometry rather than only the recurrent transition matrix.

## Method

MuonSSM adds a momentum-based pathway and applies a lightweight Newton-Schulz transformation to low-rank input injections, producing bounded spectrally conditioned updates while retaining parallel scan complexity.

## Experiments and Evidence

The abstract reports theoretical improvements in gradient propagation and spectral amplification, plus accuracy, robustness, and long-context gains across language, vision, and time-series benchmarks when integrated into diverse SSM backbones.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: Newton-Schulz cost, backbone coverage, long-context lengths, stability proofs, and sensitivity to low-rank choices.

## Deep Themes

- Sequence-model stability can be improved by conditioning memory update geometry.
- Momentum and orthogonalization can enrich long-horizon memory.
- SSMs are being refined as scalable alternatives to attention.

## Subthemes

- State space models.
- Orthogonalization.
- Newton-Schulz transforms.
- Momentum dynamics.
- Long-sequence modeling.
- Associative memory.

## Connections to Other Papers

Connects to hybrid sequence models, RFA, SSO, and long-context efficiency papers through geometrically conditioned sequence modeling.

## Notes for Cross-Paper Synthesis

MuonSSM reinforces the geometry-of-updates theme: stable long-context models depend on how memory is updated, not only on architecture class.
