# Exchangeability of GNN Representations with Applications to Graph Retrieval

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: HQcCd0laFq
- Authors: Kartik Nair; Indradyumna Roy; Soumen Chakrabarti; Anirban Dasgupta; Abir De
- Primary area: learning on graphs and other geometries & topologies
- Keywords: GNN;Locality sensitive hashing
- Source URL: https://openreview.net/forum?id=HQcCd0laFq
- PDF URL: https://openreview.net/pdf?id=HQcCd0laFq

## Abstract

In this work, we discover a probabilistic symmetry, called as exchangeability in graph neural networks (GNNs). Specifically, we show that the trained node embedding computed using a large family of graph neural networks, learned under standard optimization tools,  are exchangeable random variables. This implies that the probability density of the node embeddings remains invariant with respect to a permutation applied on their dimension axis. This results in identical distribution across the elements of the graph representations.  Such a property enables approximation of transportation-based graph similarities by Euclidean similarities between order statistics. Leveraging this reduction, we propose a unified locality-sensitive hashing (LSH) framework that supports diverse relevance measures, including subgraph matching and graph edit distance. Experiments show that our method helps to do LSH more effectively than baselines.

## One-Sentence Claim

Trained GNN node-embedding coordinates are exchangeable random variables, enabling transportation-based graph similarities to be approximated by Euclidean similarities between order statistics for efficient graph retrieval.

## Problem

Graph retrieval often uses expensive similarity measures such as subgraph matching or graph edit distance. Efficient retrieval needs hashing or approximate similarity, but graph representations are structured and difficult to compare.

The problem is to find a symmetry or distributional property of GNN embeddings that makes graph similarity easier to approximate.

## Core Contribution

The paper identifies exchangeability in node embeddings learned by a broad family of GNNs under standard optimization.

Exchangeability means the density of embedding coordinates is invariant to dimension permutations, giving identical coordinate distributions. This permits approximation of transportation-based graph similarities by Euclidean similarities over order statistics.

## Method

The authors prove or characterize exchangeability for trained GNN node embeddings. They then sort or otherwise use order statistics of embedding coordinates to reduce graph similarity computation.

This reduction supports a unified locality-sensitive hashing framework for relevance measures including subgraph matching and graph edit distance.

## Experiments and Evidence

The abstract reports that the proposed LSH framework is more effective than baselines.

The main evidence is the discovered exchangeability property and its use for approximating diverse graph retrieval similarity measures.

## Limits and Failure Modes

Exchangeability may depend on architecture, optimization, normalization, and training distribution. Specialized positional encodings or asymmetric features may break coordinate symmetry.

Because this note is abstract-only, details still need checking: GNN families covered, proof assumptions, order-statistic construction, retrieval datasets, LSH parameters, and behavior under heterophily or attributed graphs.

## Deep Themes

- Probabilistic symmetry in learned representations: coordinate exchangeability creates algorithmic shortcuts.
- Representation geometry for retrieval: graph similarity can be reduced through embedding distribution structure.
- Order statistics as invariant summaries: sorting coordinates turns exchangeability into computation.
- Theory-to-indexing bridge: a learned-representation property enables locality-sensitive hashing.

## Subthemes

- Exchangeable GNN embeddings.
- Transportation similarity approximation.
- Graph edit distance retrieval.
- LSH for graph relevance.

## Connections to Other Papers

This connects to GraphGlue, CoCo, InfoNCE Gaussianity, and embedding-collapse work through probabilistic geometry of representations.

It also relates to KDE kernel algebra and systems-efficient retrieval because representation structure is exploited for faster search.

## Notes for Cross-Paper Synthesis

This paper adds a symmetry-for-retrieval theme: hidden distributional invariances in learned embeddings can make otherwise expensive graph comparisons tractable.
