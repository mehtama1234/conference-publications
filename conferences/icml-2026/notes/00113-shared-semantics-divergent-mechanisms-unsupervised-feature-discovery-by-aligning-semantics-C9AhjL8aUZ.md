# Shared Semantics, Divergent Mechanisms: Unsupervised Feature Discovery by Aligning Semantics and Mechanisms

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: C9AhjL8aUZ
- Authors: Hyunjin Cho; Youngji Roh; Jaehyung Kim
- Primary area: deep_learning->large_language_models
- Keywords: Circuit Analysis;Interpretability;Clustering;Rate-Distortion Theory
- Source URL: https://openreview.net/forum?id=C9AhjL8aUZ
- PDF URL: https://openreview.net/pdf?id=C9AhjL8aUZ

## Abstract

As large language models are increasingly deployed in high-stakes settings, there is a growing need for tools that audit not only model outputs but also the internal computations that produce them.
Circuit analysis is a central approach in mechanistic interpretability, but it is typically target-conditioned, explaining a single prompt paired with a chosen completion.
This target-conditioned setup can obscure heterogeneity across a model's continuation distribution.
We introduce distribution-level unsupervised feature discovery, which clusters sampled continuations using both semantic content and sequence-level mechanistic attributions, without manually specifying target outputs.
Our method represents each continuation with a semantic embedding and a prefix-to-continuation attribution signature, then optimizes a rate-distortion objective that trades off semantic coherence, mechanistic consistency, and cluster granularity.
Across clustering and steering analyses, the discovered clusters expose continuation modes that single-view baselines miss and provide interventional evidence that cluster signatures correspond to actionable mechanistic factors.
Overall, our approach complements circuit analysis and behavioral evaluation by providing a scalable audit of the mechanisms underlying a model’s continuation distribution.

## One-Sentence Claim

Distribution-level feature discovery clusters LLM continuations by both semantic content and mechanistic attribution signatures, revealing modes missed by single-view analyses.

## Problem

Target-conditioned circuit analysis explains one prompt-completion pair, but can hide heterogeneous mechanisms across the model's full continuation distribution.

## Core Contribution

The paper introduces unsupervised feature discovery that aligns semantic embeddings with sequence-level mechanistic attributions using a rate-distortion objective.

## Method

It samples continuations, represents each with a semantic embedding and prefix-to-continuation attribution signature, and clusters them while trading off semantic coherence, mechanistic consistency, and cluster granularity.

## Experiments and Evidence

The abstract reports clustering and steering analyses where discovered clusters expose continuation modes missed by baselines, with interventional evidence that cluster signatures are actionable mechanistic factors.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: attribution method, rate-distortion hyperparameters, sampling sensitivity, steering intervention design, and scalability.

## Deep Themes

- Interpretability should audit distributions of possible continuations, not only selected targets.
- Semantic sameness can hide mechanistic diversity.
- Feature discovery benefits from aligning behavior and internal computation.

## Subthemes

- Mechanistic interpretability.
- Circuit analysis.
- Unsupervised feature discovery.
- Rate-distortion clustering.
- Continuation distributions.
- Steering interventions.

## Connections to Other Papers

Connects to SVD interpretability, activation oracles, shared feature discovery, and LOES through scalable internal-mechanism auditing.

## Notes for Cross-Paper Synthesis

This paper adds a distribution-level interpretability theme: auditing only one completion can miss the mechanisms governing nearby alternatives.
