# On the Power of Source Screening for Learning Shared Feature Extractors

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: dTMrITkTr5
- Authors: Muxing Wang; Connor Mclaughlin; Lili Su
- Primary area: theory->learning_theory
- Keywords: shared representation learning; linear subspace; column selection; statistical rate
- Source URL: https://openreview.net/forum?id=dTMrITkTr5
- PDF URL: https://openreview.net/pdf?id=dTMrITkTr5

## Abstract

Learning with shared representation is widely recognized as an effective way to separate commonalities from heterogeneity across various heterogeneous sources.  Most existing work includes all related data sources via simultaneously training a common feature extractor and source-specific heads. It is well understood that data sources with low relevance or poor quality may hinder representation learning. In this paper, we further dive into the question of which data sources should be learned jointly by focusing on the traditionally deemed "good" collection of sources, in which individual sources have similar relevance and qualities with respect to the true underlying common structure. Towards tractability, we focus on the linear setting where sources share a low-dimensional subspace. We find that source screening can play a central role in statistically optimal subspace estimation. We show that, for a broad class of problem instances, training on a carefully selected subset of sources suffices to achieve minimax optimality, even when a substantial portion of data is discarded. We formalize the notion of an informative subpopulation, develop algorithms and practical heuristics for identifying such subsets, and validate their effectiveness through both theoretical analysis and empirical evaluations on synthetic and real-world datasets.

## One-Sentence Claim

For shared representation learning, carefully screening sources can achieve minimax-optimal subspace estimation even after discarding substantial data from seemingly good sources.

## Problem

Shared representation learning trains a common feature extractor across heterogeneous sources, usually using all related sources with source-specific heads. Low-relevance or poor-quality sources are known to hurt, but even among sources that look similarly relevant, not all may be equally informative for estimating the shared structure.

The paper asks which sources should be jointly learned when sources share a low-dimensional subspace.

## Core Contribution

The paper shows source screening can be central to statistically optimal subspace estimation. For a broad class of instances, training on a carefully selected subset of sources achieves minimax optimality even when much data is discarded.

It formalizes informative subpopulations, develops algorithms and practical heuristics to identify them, and validates the approach theoretically and empirically on synthetic and real datasets.

## Method

The theory studies a linear shared-subspace setting. Sources differ in how informative they are about the true common structure. Source screening selects a subset whose geometry/statistics best identify the shared subspace.

The algorithms and heuristics operationalize informative-subpopulation selection before or during shared feature learning.

## Experiments and Evidence

Evidence reported in the abstract:

- Linear shared low-dimensional subspace theory.
- Minimax-optimal estimation using screened source subsets.
- Substantial data can be discarded without losing optimality.
- Formal informative-subpopulation notion.
- Algorithms and practical heuristics for source identification.
- Synthetic and real-world empirical validation.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: source-selection criteria, rates, real datasets, and robustness to nonlinear representation learning.

## Limits and Failure Modes

- Linear subspace assumptions may not transfer directly to deep feature learning.
- Screening can discard sources that matter for fairness or rare subpopulations.
- Informative-source identification may itself require enough data per source.
- Distribution shifts after screening could change which sources are useful.

## Deep Themes

**More related data is not always better.** Even acceptable sources can hurt or be redundant for shared structure.

**Data selection operates at source level.** The unit of curation is a dataset/source, not only an example.

**Statistical optimality can require discarding data.** Screening improves rates by focusing on informative subpopulations.

## Subthemes

- Shared representation learning.
- Source screening.
- Low-dimensional shared subspaces.
- Informative subpopulations.
- Minimax subspace estimation.

## Connections to Other Papers

Connects to MTS Difficulty, HOBIT, Bayesian Truthful Valuation, MFedPBA, FedPissa, and data-market papers. It also links to federated/multisource learning where client or source relevance governs aggregation.

## Notes for Cross-Paper Synthesis

Source Screening sharpens the data-governance theme: selecting which sources to trust can be as important as selecting which examples to train on.
