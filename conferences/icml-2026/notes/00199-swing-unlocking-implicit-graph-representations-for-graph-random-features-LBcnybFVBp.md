# SWING: Unlocking Implicit Graph Representations for Graph Random Features

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LBcnybFVBp
- Authors: Alessandro Manenti; Kumar Avinava Dubey; Arijit Sehanobish; Cesare Alippi; Krzysztof Marcin Choromanski
- Primary area: general_machine_learning->scalable_algorithms
- Keywords: Graph Random Features;Scalability;Implicit Graphs;Graph Kernels
- Source URL: https://openreview.net/forum?id=LBcnybFVBp
- PDF URL: https://openreview.net/pdf?id=LBcnybFVBp

## Abstract

We propose SWING: Space Walks for Implicit Network Graphs, a new class of algorithms for computations involving Graph Random Features on graphs given by implicit representations (i-graphs), where edge-weights are defined as bi-variate functions of feature vectors in the corresponding nodes. Those classes of graphs include several prominent examples, such as: *$\epsilon$-neighborhood* graphs, used on regular basis in machine learning. Rather than conducting walks on graphs' nodes, those methods rely on walks in continuous spaces, in which those graphs are embedded. To accurately and efficiently approximate original combinatorial calculations, SWING applies customized Gumbel-softmax sampling mechanism with linearized kernels, obtained via random features coupled with importance sampling techniques. This mechanism is of its own interest. SWING relies on the deep connection between implicitly defined graphs and Fourier analysis, presented in this paper. SWING is accelerator-friendly and does not require input graph materialization. We provide detailed analysis of SWING and complement it with thorough experiments on different classes of i-graphs.

## One-Sentence Claim

SWING computes graph random features on implicitly defined graphs by replacing node walks with continuous-space walks, avoiding graph materialization.

## Problem

Many useful graphs are defined implicitly by feature-based edge-weight functions, but materializing them for graph random feature computations is costly or infeasible at scale.

## Core Contribution

The paper introduces Space Walks for Implicit Network Graphs, connecting implicit graphs to Fourier analysis and using random-feature linearized kernels with importance sampling for efficient approximation.

## Method

SWING performs walks in the continuous embedding space rather than over graph nodes, using customized Gumbel-softmax sampling and linearized kernels to approximate combinatorial graph calculations on accelerator-friendly hardware.

## Experiments and Evidence

The abstract reports detailed analysis and experiments across different classes of implicit graphs, emphasizing accelerator-friendly computation without input graph materialization.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: graph classes, approximation error bounds, sampling variance, accelerator benchmarks, comparison to materialized graph kernels, and behavior with sparse/discontinuous edge functions.

## Deep Themes

- Implicit graph structure can be exploited without explicit graph construction.
- Fourier/random-feature machinery can approximate combinatorial graph operations.
- Scalability often comes from changing the computational representation.

## Subthemes

- Graph random features.
- Implicit graphs.
- Fourier analysis.
- Gumbel-softmax sampling.
- Importance sampling.
- Accelerator-friendly graph algorithms.

## Connections to Other Papers

Connects to graph and scalable-algorithm papers, and to Riemannian metric matching through graph-free geometric computation in high-dimensional data.

## Notes for Cross-Paper Synthesis

SWING adds another graph-free scalability theme: when the graph is implicit in features, the algorithm should operate in that feature space rather than instantiate the full combinatorial object.
