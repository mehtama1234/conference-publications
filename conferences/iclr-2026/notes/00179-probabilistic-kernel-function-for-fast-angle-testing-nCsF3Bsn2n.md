# Probabilistic Kernel Function for Fast Angle Testing

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: nCsF3Bsn2n
- Authors: Kejing Lu; Chuan Xiao; Yoshiharu Ishikawa
- Primary area: other topics in machine learning (i.e., none of the above)
- Keywords: Randomized algorithm;Locality Sensitive Hashing;Directional statistics
- Source URL: https://openreview.net/forum?id=nCsF3Bsn2n
- PDF URL: https://openreview.net/pdf?id=nCsF3Bsn2n

## Abstract

In this paper, we study the angle testing problem in high-dimensional Euclidean spaces and propose two projection-based probabilistic kernel functions, one designed for angle comparison and the other for angle thresholding. Unlike existing approaches that rely on random projection vectors drawn from Gaussian distributions, our approach leverages reference angles and employs a deterministic structure for the projection vectors. Notably, our kernel functions do not require asymptotic assumptions, such as the number of projection vectors tending to infinity, and can be both theoretically and experimentally shown to outperform Gaussian-distribution-based kernel functions. We further apply the proposed kernel function to Approximate Nearest Neighbor Search (ANNS) and demonstrate that our approach achieves a 2.5X-3X higher query-per-second (QPS) throughput compared to the state-of-the-art graph-based search algorithm HNSW.

## One-Sentence Claim

The paper improves high-dimensional angle testing with deterministic-reference probabilistic kernels that outperform Gaussian random-projection kernels and accelerate approximate nearest-neighbor search.

## Problem

Angle comparison and thresholding are core operations in high-dimensional retrieval and similarity search. Existing randomized projection kernels often use Gaussian projection vectors and may require asymptotic assumptions or many projections for accuracy.

## Core Contribution

The paper proposes two projection-based probabilistic kernel functions: one for angle comparison and one for angle thresholding. Unlike Gaussian random projections, the kernels use reference angles and deterministic projection structure, with non-asymptotic theoretical and empirical advantages.

## Method

The method constructs projection vectors from a deterministic reference-angle structure, then maps high-dimensional vectors into probabilistic kernel evaluations for angle comparison or threshold tests. The kernels are integrated into approximate nearest-neighbor search.

## Experiments and Evidence

The abstract reports theoretical and experimental superiority over Gaussian-projection-based kernels and 2.5x-3x higher QPS throughput than HNSW in approximate nearest-neighbor search.

## Limits and Failure Modes

Retrieval gains may depend on dimension, angular distribution, index construction, recall targets, and dataset geometry. Deterministic reference structures may be less robust to unusual data distributions. Full-text review should check error bounds, recall/latency tradeoffs, memory use, datasets, and comparison configuration against tuned HNSW.

## Deep Themes

- Fast geometric primitives for retrieval.
- Non-asymptotic randomized-style kernels.
- Deterministic projection design.
- Angle testing as infrastructure for vector search.

## Subthemes

- Angle comparison kernels.
- Angle thresholding kernels.
- Locality-sensitive hashing alternatives.
- Directional statistics.
- High-QPS approximate nearest-neighbor search.

## Connections to Other Papers

Connects to retrieval and representation-geometry papers through vector similarity infrastructure, to systems papers through query throughput, and to theory-engineering papers where better geometric primitives change practical search performance.

## Notes for Cross-Paper Synthesis

This paper is infrastructure-level: faster and more accurate angle tests can improve any system dependent on high-dimensional similarity, including retrieval, alignment, and memory.
