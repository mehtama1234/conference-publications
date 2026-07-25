# mHC: Manifold-Constrained Hyper-Connections

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: mDhyxu8WRb
- Authors: Zhenda Xie; Yixuan Wei; Huanqi Cao; Chenggang Zhao; Chengqi Deng; Jiashi Li; Damai Dai; Huazuo Gao; Mingyu Xu; Kuai Yu; Liang Zhao; Shangyan Zhou; Zhean Xu; Zhengyan Zhang; Wangding Zeng; Shengding Hu; Yuqing Wang; Jingyang Yuan; Lean Wang; Wenfeng Liang
- Primary area: deep_learning->large_language_models
- Keywords: Residual Connection
- Source URL: https://openreview.net/forum?id=mDhyxu8WRb
- PDF URL: https://openreview.net/pdf?id=mDhyxu8WRb

## Abstract

Recently, studies exemplified by Hyper-Connections (HC) have extended the ubiquitous residual connection paradigm established over the past decade by expanding the residual stream width and diversifying connectivity patterns. While yielding substantial performance gains, this diversification fundamentally compromises the identity mapping property intrinsic to the residual connection, which causes severe training instability and restricted scalability, and additionally incurs notable memory access overhead. To address these challenges, we propose Manifold-Constrained Hyper-Connections (mHC), a general framework that projects the residual connection space of HC onto a specific manifold to restore the identity mapping property, while incorporating rigorous infrastructure optimization to ensure efficiency. Empirical experiments demonstrate that mHC is effective for training at scale, offering tangible performance improvements and superior scalability. We anticipate that mHC, as a flexible and practical extension of HC, will contribute to a deeper understanding of topological architecture design and suggest promising directions for the evolution of foundational models.

## One-Sentence Claim

mHC restores the identity-mapping stability of residual connections inside wider, more diverse Hyper-Connections by constraining the residual connection space to a manifold.

## Problem

Hyper-Connections extend residual streams by widening and diversifying connectivity, improving performance but weakening the identity mapping property that makes residual networks stable and scalable.

The result is training instability, restricted scalability, and extra memory access overhead.

## Core Contribution

The paper proposes Manifold-Constrained Hyper-Connections, a framework that projects HC residual connection space onto a specific manifold to restore identity mapping while retaining the expressive benefits of diversified connections.

It also includes infrastructure optimization so the architecture is efficient enough for scale.

## Method

mHC constrains the connection parameters or residual mixing space so that the identity path remains available and stable. The manifold projection acts as an architectural regularizer for topological connection design.

Efficiency optimizations reduce the memory access overhead introduced by more complex connectivity.

## Experiments and Evidence

Evidence reported in the abstract:

- Empirical experiments at training scale.
- Tangible performance improvements.
- Superior scalability over unconstrained Hyper-Connections.
- Restoration of identity mapping property.
- Infrastructure optimization for efficiency.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model sizes, manifold choice, memory overhead, and baseline HC variants.

## Limits and Failure Modes

- Manifold constraints may reduce the connectivity diversity that made HC useful.
- Benefits may depend on architecture scale and training recipe.
- Infrastructure optimizations can be implementation-specific.
- The topological interpretation needs full-paper detail to evaluate rigor.

## Deep Themes

**Residual identity is a scalability invariant.** Architectural novelty must preserve the stable path that lets deep networks train.

**Connectivity has geometry.** mHC treats residual connection patterns as a constrained manifold.

**Architecture and infrastructure are coupled.** More expressive connections need memory-aware implementation.

## Subthemes

- Hyper-Connections.
- Residual identity mapping.
- Manifold-constrained architecture.
- Topological connection design.
- Scalable LLM training.

## Connections to Other Papers

Connects to NorMuon, POET-X, Constrained Transformers, and Modern Conservation Laws. It belongs to the theory-shaped architecture/training stability cluster.

## Notes for Cross-Paper Synthesis

mHC reinforces that scalable foundation models often depend on preserving hidden invariants, here the identity path inside increasingly complex residual topology.
