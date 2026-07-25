# Universal Redundancies in Time Series Foundation Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: DyA4KHj1wy
- Authors: Anthony Bao; Venkata Hasith Vattikuti; Jeffrey B. Lai; William Gilpin
- Primary area: deep_learning->sequential_models_time_series
- Keywords: foundation models;time series;interpretability
- Source URL: https://openreview.net/forum?id=DyA4KHj1wy
- PDF URL: https://openreview.net/pdf?id=DyA4KHj1wy

## Abstract

Time Series Foundation Models (TSFMs) leverage extensive pretraining to accurately predict unseen time series during inference, without the need for task-specific fine-tuning. Through large-scale evaluations of standard benchmarks, we find that leading transformer-based TSFMs exhibit redundant components in their intermediate layers. We introduce a set of tools for mechanistic interpretability of TSFMs, including ablations of specific components and direct logit attribution on the residual stream. Our findings are consistent across several leading TSFMs with diverse architectures, and across a diverse set of real-world and synthetic time-series datasets. We discover that all models in our study are robust to ablations of entire layers. Furthermore, we develop a theoretical framework framing transformers as kernel regressors, motivating a purely intrinsic strategy for ablating heads based on the stable rank of the per-head projection matrices. Using this approach, we uncover the specific heads responsible for degenerate phenomena widely observed in TSFMs, such as parroting of motifs from the context and seasonality bias. Our study sheds light on the universal properties of this emerging class of architectures for continuous-time sequence modeling.

## One-Sentence Claim

Leading time-series foundation models contain universal intermediate-layer redundancies that can be exposed with mechanistic tools and stable-rank-based head ablations.

## Problem

TSFMs perform well without task-specific fine-tuning, but their internal mechanisms, redundant components, and failure modes such as motif parroting or seasonality bias remain poorly understood.

## Core Contribution

The paper introduces mechanistic interpretability tools for TSFMs, including component ablations, direct logit attribution on residual streams, and a kernel-regression theory motivating intrinsic head ablations.

## Method

It evaluates multiple transformer-based TSFMs across real and synthetic datasets, ablates layers and heads, and uses stable rank of per-head projection matrices to identify intrinsically redundant or degenerate components.

## Experiments and Evidence

The abstract reports that all studied models are robust to entire-layer ablations and that specific heads drive degenerate phenomena such as context motif parroting and seasonality bias.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model list, benchmark coverage, ablation protocols, stable-rank thresholds, and predictive impact after component removal.

## Deep Themes

- Foundation-model redundancy appears beyond language and vision.
- Time-series transformers can be interpreted through residual-stream and kernel-regression views.
- Degenerate forecast behavior may localize to specific heads.

## Subthemes

- Time-series foundation models.
- Mechanistic interpretability.
- Layer/head ablation.
- Stable rank.
- Motif parroting.
- Seasonality bias.

## Connections to Other Papers

Connects to Activation Oracles, SVD interpretability, cross-domain saliency, and FlexRank through internal redundancy and component-level interpretability.

## Notes for Cross-Paper Synthesis

This paper adds time-series evidence to the redundancy theme: large pretrained sequence models may contain removable layers and specialized degenerate heads.
