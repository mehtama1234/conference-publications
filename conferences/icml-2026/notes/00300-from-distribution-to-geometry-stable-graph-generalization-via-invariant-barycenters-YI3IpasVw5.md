# From Distribution to Geometry: Stable Graph Generalization via Invariant Barycenters

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YI3IpasVw5
- Authors: Hangyuan Du; Rong Wang; Weihong Zhang; Lu Bai; Yu Xie; Liang Bai; Wenjian Wang
- Primary area: deep_learning->graph_neural_networks
- Keywords: Graph neural networks;Out-of-Distribution generalization;invariant learning
- Source URL: https://openreview.net/forum?id=YI3IpasVw5
- PDF URL: https://openreview.net/pdf?id=YI3IpasVw5

## Abstract

Graph neural networks (GNNs) excel in graph analyzing tasks but often suffer from poor generalization under Out-of-Distribution (OOD) scenarios. Although this problem has attracted increasing attention, most solutions primarily rely on empirical designs, lacking effective mechanisms to characterize and quantify invariance for graph representation learning. To address these limitations, we propose DIGL, a novel graph learning method that improves the OOD generalization of GNNs. Our work makes an initial attempt to geometrize invariance for graphs by introducing computational optimal transport (OT) theory to characterize invariance principle. Specifically, we formulate the underlying invariant prototype shared by graphs across different environments as a distribution barycenter, and consider graph representations in each specific environment as distortions of the prototype. Building on this idea, we establish an invariant learning framework to promote the model to learn purely invariant graph representations for downstream tasks. Moreover, we derive a unified optimization objective for model implementation and provide theoretical analysis to justify our method. Extensive experiments on a broad range of benchmark datasets demonstrate the superior generalization ability of our method compared with baseline methods under various OOD settings.

## One-Sentence Claim

DIGL geometrizes graph invariance by modeling the shared OOD-stable prototype across environments as an optimal-transport distribution barycenter.

## Problem

GNNs often generalize poorly under out-of-distribution shifts. Many graph OOD methods rely on empirical designs without a clear mechanism for characterizing or quantifying invariance in graph representations.

The paper asks how to turn graph invariance into a geometric object that can guide learning across environments.

## Core Contribution

The paper introduces DIGL, a graph learning method that uses computational optimal transport to characterize the invariance principle. It formulates the invariant prototype shared by graphs across environments as a distribution barycenter, while environment-specific graph representations are distortions of that prototype.

It derives a unified optimization objective and provides theoretical analysis, then shows improved OOD generalization across benchmarks.

## Method

DIGL maps graph representations into distributions and uses OT barycenters to estimate a shared invariant prototype. Learning encourages representations to align with this prototype while removing environment-specific distortions.

The method operationalizes invariance as geometry: stable information is the barycentric structure common across shifted graph environments.

## Experiments and Evidence

Evidence reported in the abstract:

- Computational OT formulation of graph invariance.
- Unified optimization objective.
- Theoretical analysis justifying the method.
- Extensive experiments over broad benchmark datasets.
- Superior generalization under various OOD settings compared with baselines.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: graph benchmarks, environment definitions, OT solver, barycenter computation cost, and invariance metrics.

## Limits and Failure Modes

- OT barycenter computation can be costly for large graphs or many environments.
- Invariance assumptions may fail if the label mechanism changes across environments.
- Environment annotations or partitions may be required.
- Over-removing environment-specific variation can discard useful predictive signal.

## Deep Themes

**OOD invariance can be geometric.** DIGL represents stable graph structure as a distribution barycenter.

**Environment variation becomes distortion around a prototype.** This gives a concrete object for separating invariant and spurious factors.

**Optimal transport is a reusable representation tool.** OT moves beyond matching distributions into defining invariance principles.

## Subthemes

- Graph OOD generalization.
- Invariant barycenters.
- OT-based representation learning.
- Environment-specific distortions.
- Geometrized invariance principle.

## Connections to Other Papers

Connects to FlashSinkhorn, IDCD, HAMC, PSAHS, and ENGNN through graph/multiview geometry and optimal transport. It also links to DISCO and causal robustness papers because invariance is used to remove unstable environment dependence.

## Notes for Cross-Paper Synthesis

DIGL closes this stub block with a clean example of the distribution-to-geometry trend: stable generalization is represented as an invariant geometric prototype rather than an empirical regularizer alone.
