# HELIX: Hybrid Encoding with Learnable Identity and Cross-dimensional Synthesis for Time Series Imputation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: FN20iuPnEU
- Authors: Fengming Zhang; Wenjie Du; Huan Zhang; Ke Yu; Shen Qu
- Primary area: deep_learning->sequential_models_time_series
- Keywords: Time Series;Imputation;Missing Data;Attention Model;Deep Learning
- Source URL: https://openreview.net/forum?id=FN20iuPnEU
- PDF URL: https://openreview.net/pdf?id=FN20iuPnEU

## Abstract

Time series imputation benefits from leveraging cross-feature correlations, yet existing attention-based methods re-discover feature relationships at each layer, lacking persistent anchors to maintain consistent representations. To address this, we propose HELIX, which assigns each feature a learnable feature identity, a persistent embedding that captures intrinsic semantic properties throughout the network. Unlike graph-based methods that rely on predefined topology and assume homogeneous spatial relationships, HELIX learns arbitrary feature dependencies end-to-end from temporal co-variation, naturally handling datasets where features mix spatial locations with semantic variables. Integrated with hybrid temporal-feature attention, HELIX achieves the state-of-the-art performance, surpassing all 16 baselines on 5 public datasets across 21 experimental settings in our evaluation. Furthermore, our mechanistic analysis reveals that HELIX aligns learned feature identities and dependencies with latent physical and semantic structure progressively across layers, demonstrating that it more effectively translates cross-feature structure into imputation accuracy.

## One-Sentence Claim

HELIX improves time-series imputation by giving each feature a persistent learnable identity and combining it with hybrid temporal-feature attention.

## Problem

Attention-based imputation methods often rediscover feature relationships at each layer, lacking persistent anchors for stable cross-feature representations.

## Core Contribution

The paper introduces learnable feature identities that preserve intrinsic feature semantics throughout the network while learning arbitrary dependencies from temporal co-variation.

## Method

HELIX assigns each feature a persistent embedding and integrates it with hybrid temporal-feature attention, avoiding predefined graph topology and handling mixed spatial and semantic variables.

## Experiments and Evidence

The abstract reports state-of-the-art performance over 16 baselines on 5 public datasets across 21 settings, plus mechanistic evidence that feature identities align with latent physical and semantic structure over layers.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: missingness patterns, feature-identity initialization, attention architecture, and robustness under distribution shift.

## Deep Themes

- Persistent feature identities can stabilize cross-dimensional time-series learning.
- Imputation benefits from learned semantic structure rather than predefined topology.
- Mechanistic analysis can validate whether learned dependencies match physical structure.

## Subthemes

- Time-series imputation.
- Learnable feature identity.
- Cross-feature attention.
- Missing data.
- Latent physical structure.
- Hybrid encoding.

## Connections to Other Papers

Connects to TSFM redundancy, cross-domain saliency, and time-series foundation-model work through interpretable sequence/feature structure.

## Notes for Cross-Paper Synthesis

HELIX strengthens the feature-identity theme: stable per-variable anchors can make learned temporal dependencies more coherent and interpretable.
