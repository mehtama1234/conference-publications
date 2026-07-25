# On Efficient Scaling of GNNs via IO-Aware Layers Implementations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: w6JVbu7VFo
- Authors: Daria Fomina; Daniil Krasylnikov; Alexey Boykov; Andrey Dolgovyazov; Vyacheslav Zhdanovskiy; Fedor Velikonivtsev
- Primary area: general_machine_learning->hardware_and_software
- Keywords: Graph Neural Networks;Acceleration;IO;Hardware-aware implementation;CUDA;Efficiency;Graphs;Graph Machine Learning
- Source URL: https://openreview.net/forum?id=w6JVbu7VFo
- PDF URL: https://openreview.net/pdf?id=w6JVbu7VFo

## Abstract

Graph Neural Networks (GNNs) are bottlenecked by sparse, irregular memory access. Popular frameworks such as DGL and PyTorch Geometric support general message passing, but complex layers often materialize edge-wise intermediates, increasing memory traffic and limiting scalability on large graphs.
We take an I/O- and arithmetic-intensity--centric view and show that widely used layers fall into three kernel families: SpMM-based convolutions, reduction-based aggregations, and attention-based layers (GATv2/Graph Transformer). For each family, we develop GPU kernels that reduce data movement, improve locality, and remain robust across realistic graphs. We also study graph reordering and find that its impact depends on the kernel mapping: it benefits neighbor-parallel (gather-dominated) kernels more consistently than feature-parallel designs.
Empirically, our fused attention kernels reach up to **3.9**$\times$ speedup for Graph Transformer (median **1.6**$\times$), with Tensor Core (block-sparse) variants up to **7.3**$\times$ on locally dense graphs; for GATv2 we reach up to **8.5**$\times$ speedup (median **2.0**$\times$) while reducing peak memory by up to **76**$\times$ (median **6**$\times$). Our degree-aware reduction kernels achieve up to **10**$\times$ speedup (median **2.6**$\times$). For SpMM-based layers, properly cached cuSPARSE achieves up to **8**$\times$ speedup over DGL and outperforms evaluated custom baselines in the majority of evaluations. We release our implementations as drop-in replacements in our [GitHub repository](https://github.com/yandex-research/On-Efficient-Scaling-Of-GNNs) to support reproducible, hardware-aware GNN acceleration.

## One-Sentence Claim

GNN scalability improves substantially when common graph layers are implemented as IO-aware GPU kernel families rather than generic message-passing programs that materialize edge-wise intermediates.

## Problem

Large graph neural networks are constrained less by nominal arithmetic and more by sparse, irregular memory movement. General frameworks such as DGL and PyTorch Geometric expose flexible message-passing abstractions, but that flexibility often creates costly intermediate tensors and poor locality.

The practical problem is that a layer can be mathematically simple yet operationally slow because it maps badly to GPU memory hierarchy, graph sparsity, and degree distributions.

## Core Contribution

The paper gives an IO- and arithmetic-intensity view of widely used GNN layers. It groups layers into SpMM-based convolutions, reduction-based aggregations, and attention-based layers, then designs GPU implementations for each group that reduce memory traffic and improve locality.

The contribution is not a new GNN model. It is a systems reinterpretation of existing GNN layers that turns graph-layer structure into drop-in hardware-aware kernels.

## Method

The method analyzes layer computation by kernel family. For SpMM-style layers, it emphasizes properly cached cuSPARSE use. For reduction layers, it uses degree-aware reductions. For attention layers such as GATv2 and Graph Transformer, it uses fused attention kernels and Tensor Core/block-sparse variants when local density makes them effective.

The paper also studies graph reordering and separates its effects by kernel mapping: gather-heavy neighbor-parallel kernels benefit more consistently than feature-parallel designs.

## Experiments and Evidence

The abstract reports large speed and memory improvements across realistic graphs. Fused attention kernels reach up to 3.9x speedup for Graph Transformer with median 1.6x, and Tensor Core/block-sparse variants reach up to 7.3x on locally dense graphs. For GATv2, the kernels reach up to 8.5x speedup with median 2.0x and reduce peak memory by up to 76x with median 6x.

Degree-aware reduction kernels reach up to 10x speedup with median 2.6x. For SpMM-based layers, cached cuSPARSE reaches up to 8x speedup over DGL and beats evaluated custom baselines in most evaluations.

## Limits and Failure Modes

The gains depend on layer family, graph structure, local density, and kernel mapping. Graph reordering is not uniformly useful, and Tensor Core/block-sparse gains appear strongest when graphs have suitable local density.

Because this note is abstract-only, details still need checking: benchmark graph suite, hardware, batch construction, exact baselines, preprocessing costs, numerical equivalence, and integration constraints for dynamic or sampled GNN training.

## Deep Themes

- IO-aware ML systems: bottlenecks move from FLOPs to memory traffic and locality.
- Abstraction penalty: generic message passing can hide expensive materialization.
- Kernel-family decomposition: optimization becomes tractable when layers are grouped by operational structure.
- Hardware-aware graph learning: graph algorithms must be designed with sparsity layout and GPU mapping in mind.

## Subthemes

- Fused attention for graph transformers.
- Degree-aware reductions for irregular aggregation.
- Cached vendor libraries can beat custom kernels when the mapping is right.
- Graph reordering is kernel-dependent rather than universally beneficial.

## Connections to Other Papers

This connects to KDE kernel algebra, FFCC, EcoVLA, and LiftQuant through the broader efficiency theme: capability can be unlocked by targeting the actual computational bottleneck rather than changing the high-level model.

It also relates to DroneDINO and ScaleMoE because both treat routing and locality as systems-level choices that affect usable scale.

## Notes for Cross-Paper Synthesis

This paper is a strong example of implementation-aware scaling. The relevant abstraction is not "GNN layer" but the data-movement pattern induced by the layer on real hardware.
