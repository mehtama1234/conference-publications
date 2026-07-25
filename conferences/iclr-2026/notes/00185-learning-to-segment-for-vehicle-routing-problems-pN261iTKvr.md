# Learning to Segment for Vehicle Routing Problems

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: pN261iTKvr
- Authors: Wenbin Ouyang; Sirui Li; Yining Ma; Cathy Wu
- Primary area: optimization
- Keywords: Learning-Guided Optimization;Vehicle Routing Problem
- Source URL: https://openreview.net/forum?id=pN261iTKvr
- PDF URL: https://openreview.net/pdf?id=pN261iTKvr

## Abstract

Iterative heuristics are widely recognized as state-of-the-art for Vehicle Routing Problems (VRPs). In this work, we exploit a critical observation: a large portion of the solution remains stable, i.e., unchanged across search iterations, causing redundant computations, especially for large-scale VRPs with long subtours. To address this, we pioneer the formal study of the First-Segment-Then-Aggregate
(FSTA) decomposition technique to accelerate iterative solvers. FSTA preserves stable solution segments during the search, aggregates nodes within each segment into fixed hypernodes, and focuses the search only on unstable portions. Yet, a key challenge lies in identifying which segments should be aggregated. To this end, we introduce Learning-to-Segment (L2Seg), a novel neural framework to intelligently
differentiate potentially stable and unstable portions for FSTA decomposition. We present three L2Seg variants: non-autoregressive (globally comprehensive but locally indiscriminate), autoregressive (locally refined but globally deficient), and their synergy. Empirical results on CVRP and VRPTW show that L2Seg accelerates state-of-the-art solvers by 2x to 7x. We further provide in-depth analysis showing why synergy achieves the best performance. Notably, L2Seg is compatible with traditional, learning-based, and hybrid solvers, while supporting various VRPs.

## One-Sentence Claim

L2Seg accelerates iterative vehicle-routing solvers by learning which stable route segments can be aggregated into hypernodes while preserving search over unstable portions.

## Problem

State-of-the-art VRP heuristics repeatedly update solutions, but much of a route can remain stable across iterations. Recomputing over stable subtours wastes time, especially in large instances, yet identifying which segments are safe to aggregate is nontrivial.

## Core Contribution

The paper formalizes First-Segment-Then-Aggregate decomposition for VRPs and introduces Learning-to-Segment, a neural framework that predicts stable versus unstable portions. It provides non-autoregressive, autoregressive, and synergistic variants compatible with traditional, learning-based, and hybrid solvers.

## Method

FSTA preserves predicted stable route segments, aggregates each segment into a fixed hypernode, and focuses iterative search on unstable parts of the solution. L2Seg learns the segmentation decision, with non-autoregressive models offering global coverage, autoregressive models offering local refinement, and a combined approach balancing both.

## Experiments and Evidence

On CVRP and VRPTW, L2Seg reportedly accelerates state-of-the-art solvers by 2x to 7x. The paper includes analysis explaining why the synergistic variant performs best and claims support for multiple VRP variants and solver families.

## Limits and Failure Modes

Incorrectly aggregating unstable segments can block improvements or trap search in suboptimal regions. Generalization may depend on instance size, customer distribution, constraints, and solver dynamics. Full-text review should check segment-prediction accuracy, solution-quality tradeoffs, overhead, compatibility claims, and behavior on highly dynamic or constrained VRPs.

## Deep Themes

- Learning-guided decomposition for combinatorial optimization.
- Stability detection in iterative search.
- Solver acceleration through partial aggregation.
- Hybrid neural-classical routing methods.

## Subthemes

- First-Segment-Then-Aggregate.
- Stable subtour preservation.
- Hypernode aggregation.
- Non-autoregressive versus autoregressive segmentation.
- CVRP and VRPTW acceleration.

## Connections to Other Papers

Connects to AutoEP and DMS through learned control of optimization processes, to LeanHammer through neural components inside classical workflows, and to generative/offline decision papers where learned modules guide search without replacing the solver.

## Notes for Cross-Paper Synthesis

L2Seg shows a pragmatic hybrid pattern: use learning to identify where expensive classical search is unnecessary, then let the solver focus on the uncertain parts.
