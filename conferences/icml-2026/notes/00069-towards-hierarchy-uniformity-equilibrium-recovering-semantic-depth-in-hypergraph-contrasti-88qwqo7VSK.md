# Towards Hierarchy–Uniformity Equilibrium: Recovering Semantic Depth in Hypergraph Contrastive Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 88qwqo7VSK
- Authors: Ruiting Zhao; Ming Li; Lixin Cui; Lu Bai; Feilong Cao; Ke Lv; Pietro Lio
- Primary area: deep_learning->graph_neural_networks
- Keywords: Hypergraph learning;Hypergraph neural networks;Hypergraph contrastive learning
- Source URL: https://openreview.net/forum?id=88qwqo7VSK
- PDF URL: https://openreview.net/pdf?id=88qwqo7VSK

## Abstract

Hypergraph contrastive learning is an effective paradigm for representation learning on higher-order relational data, yet existing methods largely ignore that hyperedges link nodes with multi-level semantics. Standard contrastive objectives emphasize instance discrimination via hyperspherical uniformity and tend to push embeddings apart in an indiscriminate manner. We show that this leads to a *Hierarchy–Uniformity Conflict*, whose geometric manifestation is *Semantic Flattening*, where the semantic depth of hyperedges collapses into a nearly flat cloud of instances. To address this issue, we introduce **HyperDepth**, a hypergraph contrastive learning framework that moves representations towards a hierarchy–uniformity equilibrium by jointly coordinating spectral and geometric signals. HyperDepth employs a decoupled spectral encoding scheme with adaptive gating so that high-frequency components focus on local instance discrimination while low-frequency components capture global hierarchical structure. On top of this, an energy-based hierarchical alignment module attaches a learnable prototype tree to the representation space and minimizes an interpretable energy functional to recover the semantic depth of hyperedges. Theoretically, under a mild frequency-separation assumption, we show that the local contrastive and global hierarchical objectives operate on orthogonal spectral components and admit equilibrium embeddings that preserve semantic depth while still retaining instance-level discrimination. Experiments on 15 hypergraph datasets and 17 supervised and self-supervised baselines, spanning homophilic and heterophilic regimes, show that HyperDepth attains strong performance with the best average rank.

## One-Sentence Claim

HyperDepth repairs hypergraph contrastive learning by balancing instance-level uniformity with hierarchy-preserving semantic depth.

## Problem

Standard hypergraph contrastive objectives push embeddings apart for instance discrimination but can flatten multi-level hyperedge semantics into a shallow point cloud.

## Core Contribution

The paper identifies a Hierarchy-Uniformity Conflict and proposes HyperDepth, a framework that coordinates spectral and geometric signals to recover semantic depth while preserving contrastive discrimination.

## Method

HyperDepth uses decoupled spectral encoding with adaptive gating: high-frequency components support local instance discrimination, while low-frequency components encode global hierarchical structure. An energy-based hierarchical alignment module attaches a learnable prototype tree to the representation space.

## Experiments and Evidence

The abstract reports theoretical equilibrium guarantees under a frequency-separation assumption and experiments on 15 hypergraph datasets against 17 supervised and self-supervised baselines, with strong average-rank performance across homophilic and heterophilic regimes.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: the exact energy functional, prototype-tree learning stability, sensitivity to the frequency-separation assumption, and dataset-specific hierarchy annotations.

## Deep Themes

- Contrastive uniformity can erase structured semantic depth.
- Spectral decomposition can separate local discrimination from global hierarchy.
- Graph representation learning is moving from flat instance separation toward geometry-aware semantics.

## Subthemes

- Hypergraph contrastive learning.
- Semantic flattening.
- Hierarchy-uniformity equilibrium.
- Spectral gating.
- Prototype trees.
- Higher-order relational data.

## Connections to Other Papers

Connects to LOES, SVD interpretability, and spectral causal-discovery papers through spectral geometry as an explanatory and corrective tool. It also links to representation-learning papers that treat geometry as the object to preserve.

## Notes for Cross-Paper Synthesis

HyperDepth adds a semantic-geometry warning: representation objectives that improve separability may still destroy the hierarchy needed for downstream reasoning.
