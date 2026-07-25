# Simple Algorithms for Bad Triangle Transversals with Applications to Correlation Clustering

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Yq66fTPjHn
- Authors: Florian Adriaens; Nikolaj Tatti
- Primary area: optimization->discrete_and_combinatorial_optimization
- Keywords: correlation clustering;strong triadic closure;bad triangle transversals;approximation algorithms
- Source URL: https://openreview.net/forum?id=Yq66fTPjHn
- PDF URL: https://openreview.net/pdf?id=Yq66fTPjHn

## Abstract

The Bad Triangle Transversal (BTT) problem asks for the smallest set of edges that need to be removed from a given signed graph, so that the resulting graph does not have a bad triangle. Here, a bad triangle is a triangle with exactly one negative edge.
Several 2-approximations for BTT are proposed in this paper. On the hardness side, we show that BTT is NP-hard to approximate with factor better than $\frac{2137}{2136}$ on complete graphs. Our reduction also works for Correlation Clustering (CC), the Cluster Deletion problem (CD) and the Minimum Strong Triadic Closure problem (MinSTC). Lastly, we show that the BTT and CC optima are within a factor of 3/2 in complete graphs, by describing a pivot procedure that transforms transversals into clusters.

## One-Sentence Claim

Bad Triangle Transversal admits simple 2-approximation algorithms and is tightly related to correlation clustering, cluster deletion, and minimum strong triadic closure.

## Problem

In signed graphs, a bad triangle has exactly one negative edge. The Bad Triangle Transversal problem asks for the smallest edge set to remove so no bad triangles remain. This structure is central to correlation clustering and triadic closure problems.

The paper asks for simple approximation algorithms and hardness relationships for BTT and related clustering problems.

## Core Contribution

The paper proposes several 2-approximation algorithms for BTT. On the hardness side, it shows BTT is NP-hard to approximate within a factor better than 2137/2136 on complete graphs.

The same reduction applies to Correlation Clustering, Cluster Deletion, and Minimum Strong Triadic Closure. The paper also proves that BTT and correlation-clustering optima are within a factor of 3/2 on complete graphs via a pivot procedure transforming transversals into clusters.

## Method

The method is combinatorial optimization. It designs approximation procedures for removing edges that hit all bad triangles, proves hardness by reduction, and relates BTT solutions to clustering solutions with a pivot transformation.

The complete-graph setting reveals structural equivalences between edge deletion for consistency and partitioning for correlation clustering.

## Experiments and Evidence

Evidence reported in the abstract is theoretical:

- Several 2-approximation algorithms for BTT.
- NP-hardness of approximation better than 2137/2136 on complete graphs.
- Reduction also applies to CC, CD, and MinSTC.
- 3/2-factor relationship between BTT and CC optima on complete graphs.
- Pivot procedure converting transversals to clusters.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: algorithm variants, proof conditions, graph classes beyond complete graphs, and whether empirical evaluation exists.

## Limits and Failure Modes

- Approximation factors may be loose for practical graphs.
- Complete-graph hardness and equivalence results may not transfer directly to sparse graphs.
- The abstract does not mention scalability or implementation experiments.
- Edge-removal objectives may not capture weighted or noisy real-world signed networks.

## Deep Themes

**Graph inconsistency can be localized in forbidden motifs.** Bad triangles are the primitive obstruction.

**Clustering and deletion problems share hidden structure.** BTT becomes a bridge among correlation clustering, cluster deletion, and triadic closure.

**Simple approximation algorithms still matter.** The contribution emphasizes clean guarantees rather than complex heuristics.

## Subthemes

- Bad triangle transversals.
- Signed graph consistency.
- Correlation clustering reductions.
- Strong triadic closure.
- Pivot transformations.

## Connections to Other Papers

Connects to DIGL, DeepWalk Trajectory, Exact GNN Algorithms, and graph-learning papers through graph structure and clustering. It also links to theory papers where identifying the right primitive obstruction leads to sharper guarantees.

## Notes for Cross-Paper Synthesis

BTT adds a classical combinatorial counterpart to neural graph work: before learning on graphs, understand which structural inconsistencies define the task.
