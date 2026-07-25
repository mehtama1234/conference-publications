# Recurrent Equivariant Constraint Modulation: Learning Per-Layer Symmetry Relaxation from Data

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: STeISpzNSd
- Authors: Stefanos Pertigkiozoglou; Mircea Petrache; Shubhendu Trivedi; Kostas Daniilidis
- Primary area: deep_learning
- Keywords: Equivariant Networks;Constraint Relaxation;Approximate Equivariant Networks;Geometric Deep Learning
- Source URL: https://openreview.net/forum?id=STeISpzNSd
- PDF URL: https://openreview.net/pdf?id=STeISpzNSd

## Abstract

Equivariant neural networks exploit underlying task symmetries to improve generalization, but strict equivariance constraints can induce more complex optimization dynamics that can hinder learning. Prior work addresses these limitations by relaxing strict equivariance during training, but typically relies on prespecified, explicit, or implicit target levels of relaxation for each network layer, which are task-dependent and costly to tune. We propose Recurrent Equivariant Constraint Modulation (RECM), a layer-wise constraint modulation mechanism that learns appropriate relaxation levels solely from the training signal and the symmetry properties of each layer's input-target distribution, without requiring any prior knowledge about the task-dependent target relaxation level. We demonstrate that under the proposed RECM update, the relaxation level of each layer provably converges 
to a value upper-bounded by its symmetry gap, namely the degree to which its input-target distribution deviates from exact symmetry. Consequently, layers processing symmetric distributions recover full equivariance, while those with approximate symmetries retain sufficient flexibility to learn non-symmetric solutions when warranted by the data. Empirically, RECM outperforms prior methods across diverse exact and approximate equivariant tasks, including the challenging molecular conformer generation on the GEOM-Drugs dataset.

## One-Sentence Claim

RECM learns per-layer equivariance relaxation levels from data, recovering full equivariance when symmetry is exact and retaining flexibility when symmetry is approximate.

## Problem

Strict equivariance can improve generalization but complicate optimization, while prior relaxation methods require task-dependent per-layer target levels that are costly to tune.

## Core Contribution

The paper introduces recurrent layer-wise constraint modulation whose relaxation level provably converges below each layer's symmetry gap, requiring no prior target relaxation knowledge.

## Method

RECM updates relaxation levels using the training signal and the symmetry properties of each layer's input-target distribution, allowing symmetric layers to become fully equivariant and approximate-symmetry layers to learn non-symmetric solutions as needed.

## Experiments and Evidence

The abstract reports improvements over prior methods across exact and approximate equivariant tasks, including molecular conformer generation on GEOM-Drugs.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: symmetry-gap estimation, recurrent update stability, task suite, group actions, computational overhead, and behavior when symmetry changes during training.

## Deep Themes

- Symmetry constraints should be data-adaptive rather than fixed.
- Approximate equivariance needs layer-specific flexibility.
- Geometric priors can be relaxed without abandoning guarantees.

## Subthemes

- Equivariant networks.
- Constraint relaxation.
- Geometric deep learning.
- Symmetry gap.
- Molecular conformer generation.
- Layer-wise modulation.

## Connections to Other Papers

Connects to Riemannian metric matching, FlatLand, Modified SINNs, and geometry-aware papers through adaptive use of mathematical structure.

## Notes for Cross-Paper Synthesis

RECM adds an adaptive-prior theme: the right inductive bias may vary by layer and data regime, so constraints should be learned where symmetry is only approximate.
