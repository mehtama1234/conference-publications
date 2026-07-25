# Deep Flow Networks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Z7rhDaBvBo
- Authors: Ozan Candogan; Ayoub Foussoul
- Primary area: deep_learning
- Keywords: Discrete Function Approximators;M-convex;Network flow;Deep Learning;Deep Flow Networks
- Source URL: https://openreview.net/forum?id=Z7rhDaBvBo
- PDF URL: https://openreview.net/pdf?id=Z7rhDaBvBo

## Abstract

We introduce Deep Flow Networks (DFNs), a new class of discrete function approximators. DFNs are inspired by and generalize minimum-cost flow value functions that map node imbalances on a subset of nodes to the optimal flow cost. Such functions are known to be M-convex (Murota2003) and admit efficient optimization.
On the theoretical side, we prove that DFNs are universal approximators for discrete functions on $\mathbb{Z}^d$ that admit convex extensions to $\mathbb{R}^d$, and characterize their optimization complexity in terms of their deviation from the M-convex regime. Guided by these results, we develop a practical DFN implementation for learning from data. Finally, we evaluate our implementation empirically on data from different ground-truth functions, showing that DFNs achieve strong approximation accuracy while being substantially faster to optimize than benchmark approaches.

## One-Sentence Claim

Deep Flow Networks are discrete function approximators inspired by minimum-cost flow value functions, with universal approximation for convex-extendable integer-domain functions and efficient optimization near the M-convex regime.

## Problem

Many learning problems involve discrete functions on integer grids, where continuous neural approximators may ignore useful combinatorial convexity. Minimum-cost flow value functions have strong structure, including M-convexity and efficient optimization, but are not usually treated as a deep-learning function class.

The paper asks whether flow-inspired discrete approximators can combine expressive learning with tractable optimization.

## Core Contribution

The paper introduces Deep Flow Networks, a new class of discrete function approximators generalizing minimum-cost flow value functions. It proves DFNs are universal approximators for discrete functions on Z^d that admit convex extensions to R^d.

It also characterizes optimization complexity in terms of deviation from the M-convex regime and develops a practical implementation for learning from data.

## Method

DFNs map node imbalances on selected nodes to optimal flow costs, then generalize this minimum-cost-flow structure into a learnable architecture. The theory uses M-convexity as the tractable core and measures how far learned functions deviate from that regime.

The practical implementation fits DFNs to data and exploits the flow-inspired structure for faster optimization.

## Experiments and Evidence

Evidence reported in the abstract:

- Universal approximation for discrete functions with convex extensions.
- Optimization-complexity characterization by deviation from M-convexity.
- Practical DFN learning implementation.
- Empirical evaluation on data from different ground-truth functions.
- Strong approximation accuracy and substantially faster optimization than benchmark approaches.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: architecture definition, benchmark functions, optimization algorithms, and expressivity limits for non-convex-extendable functions.

## Limits and Failure Modes

- Universality is restricted to discrete functions admitting convex extensions.
- Optimization benefits may degrade far from M-convex structure.
- Flow-network parameterization may be less natural for arbitrary discrete domains.
- Practical scaling depends on graph/network size and solver details.

## Deep Themes

**Combinatorial structure can be a neural architecture.** DFNs embed minimum-cost-flow geometry into the function class.

**Discrete learning benefits from convexity-aware design.** The model's optimization is explained by distance from M-convexity.

**Expressivity and tractability are linked through structure.** The paper does not maximize generic neural capacity; it chooses a structured class with useful guarantees.

## Subthemes

- Discrete function approximation.
- Minimum-cost flow value functions.
- M-convexity.
- Convex extensions of integer-domain functions.
- Optimization complexity by structural deviation.

## Connections to Other Papers

Connects to BTT Algorithms, Exact GNN Algorithms, and graph/flow theory work through discrete optimization structure. It also links to FlowOptimizer and Flow Sampling through flow-inspired computational primitives in different domains.

## Notes for Cross-Paper Synthesis

DFNs add to the theme of importing mature mathematical objects into neural design: flow value functions become learnable modules with built-in optimization behavior.
