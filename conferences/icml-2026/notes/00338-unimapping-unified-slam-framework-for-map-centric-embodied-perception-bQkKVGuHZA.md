# UniMapping: Unified SLAM Framework for Map-Centric Embodied Perception

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: bQkKVGuHZA
- Authors: Xiaze Zhang; Ziheng Ding; Yuejie Zhang; lifeng chen; Rui Feng
- Primary area: applications->robotics
- Keywords: SLAM;Scene Understanding;Neural Descriptor Map;Embodied AI
- Source URL: https://openreview.net/forum?id=bQkKVGuHZA
- PDF URL: https://openreview.net/pdf?id=bQkKVGuHZA

## Abstract

Simultaneous Localization and Mapping (SLAM) is increasingly expected to provide reusable spatial representations for downstream perception. However, existing approaches often struggle with scale-consistency and producing maps that lack the geometric fidelity required for reliable perception. We propose _UniMapping_, a unified SLAM framework that constructs a persistent neural-descriptor map from multimodal observations. We introduce a **Spatial-Aware Deformable Transformer** that injects explicit geometric inductive bias to ensure scale-invariant feature extraction, alongside a **Spatial Fusion** strategy that decouples feature aggregation from temporal sequences. Extensive experiments on both indoor and outdoor benchmarks demonstrate competitive SLAM performance. Notably, our method significantly enhances downstream tasks (mAP +3.1% and mIoU +7.1%) by leveraging accumulated multi-view context.

## One-Sentence Claim

UniMapping builds persistent neural-descriptor maps from multimodal observations so SLAM representations become reusable, scale-consistent substrates for embodied perception.

## Problem

SLAM is increasingly expected to support downstream perception, not only localization and mapping. Existing approaches can struggle with scale consistency and insufficient geometric fidelity, producing maps that are not reliable for later perception tasks.

The paper asks how to make maps central reusable representations for embodied AI.

## Core Contribution

The paper proposes UniMapping, a unified SLAM framework that constructs a persistent neural-descriptor map from multimodal observations. It introduces:

- A Spatial-Aware Deformable Transformer with explicit geometric inductive bias for scale-invariant feature extraction.
- A Spatial Fusion strategy that decouples feature aggregation from temporal sequences.

The method achieves competitive SLAM performance and improves downstream perception with accumulated multi-view context.

## Method

UniMapping extracts geometry-aware features from multimodal observations, stores them in a persistent neural-descriptor map, and fuses spatial evidence independently of strict temporal order. The deformable Transformer uses spatial structure to stabilize scale across views.

Downstream tasks then query or use the accumulated map rather than relying on single-frame features.

## Experiments and Evidence

Evidence reported in the abstract:

- Indoor and outdoor SLAM benchmarks.
- Competitive SLAM performance.
- Downstream mAP improvement of 3.1 percent.
- Downstream mIoU improvement of 7.1 percent.
- Multi-view context accumulated in a neural-descriptor map.
- Spatial-aware deformable Transformer and Spatial Fusion.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, sensors/modalities, map representation, runtime, and downstream tasks.

## Limits and Failure Modes

- Persistent neural maps may accumulate errors under long trajectories.
- Scale consistency can fail under poor calibration or dynamic scenes.
- Downstream gains depend on task and map-query interface.
- Memory and update costs for large environments need inspection.

## Deep Themes

**Maps are becoming learned memory.** SLAM outputs are persistent neural descriptors for downstream perception.

**Embodied perception needs multi-view accumulation.** Single-frame understanding misses stable spatial context.

**Geometry-aware Transformers support spatial consistency.** Attention is adapted to mapping geometry rather than generic sequence modeling.

## Subthemes

- Neural-descriptor maps.
- Map-centric embodied perception.
- Spatial-aware deformable Transformer.
- Scale-invariant feature extraction.
- Temporal-decoupled spatial fusion.

## Connections to Other Papers

Connects to Holi-Spatial, SceneSmith, RelaxFlow, Latent Action Supervision, and continual VLA learning through embodied spatial data and robotics. It also links to DLMR because both use persistent structured memory for multimodal reasoning.

## Notes for Cross-Paper Synthesis

UniMapping reinforces the embodied-memory theme: spatial intelligence depends on persistent world representations that downstream models can reuse.
