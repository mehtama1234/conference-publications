# VGGT-Motion: Motion-Aware Calibration-Free Monocular SLAM for Long-Range Consistency

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GyRMbsYFiG
- Authors: Zhuang Xiong; Chen Zhang; Qingshan Xu; Wenbing Tao
- Primary area: applications->computer_vision
- Keywords: Monocular SLAM;Calibration-Free;Vision Foundation Models;Long-Range Consistency;Autonomous Driving
- Source URL: https://openreview.net/forum?id=GyRMbsYFiG
- PDF URL: https://openreview.net/pdf?id=GyRMbsYFiG

## Abstract

Despite recent progress in calibration-free monocular SLAM via 3D vision foundation models, scale drift remains severe on long sequences. Motion-agnostic partitioning breaks contextual coherence and causes zero-motion drift, while conventional geometric alignment is computationally expensive. To address these issues, we propose VGGT-Motion, a calibration-free SLAM system for efficient and robust global consistency over kilometer-scale trajectories. Specifically, we first propose a motion-aware submap construction mechanism that uses optical flow to guide adaptive partitioning, prune static redundancy, and encapsulate turns for stable local geometry. We then design an anchor-driven direct Sim(3) registration strategy. By exploiting context-balanced anchors, it achieves search-free, pixel-wise dense alignment and efficient loop closure without costly feature matching. Finally, a lightweight submap-level pose graph optimization enforces global consistency with linear complexity, enabling scalable long-range operation. Experiments show that VGGT-Motion markedly improves trajectory accuracy and efficiency, achieving state-of-the-art performance in zero-shot, long-range calibration-free monocular SLAM.

## One-Sentence Claim

VGGT-Motion improves calibration-free monocular SLAM by using motion-aware submaps, anchor-driven dense Sim(3) registration, and lightweight pose graph optimization for long-range consistency.

## Problem

3D vision foundation model SLAM still suffers scale drift on long monocular sequences, while motion-agnostic partitioning and conventional alignment either break coherence or cost too much.

## Core Contribution

The paper introduces a calibration-free monocular SLAM system designed for efficient kilometer-scale global consistency.

## Method

VGGT-Motion uses optical flow for adaptive submap partitioning, static redundancy pruning, and turn encapsulation; context-balanced anchors enable search-free pixel-wise dense Sim(3) registration and loop closure; submap pose graph optimization enforces global consistency with linear complexity.

## Experiments and Evidence

The abstract reports state-of-the-art zero-shot long-range calibration-free monocular SLAM with improved trajectory accuracy and efficiency.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, kilometer-scale metrics, dynamic object handling, optical-flow failure modes, and autonomous-driving deployment assumptions.

## Deep Themes

- Vision foundation models need motion-aware structure for long-range geometry.
- Calibration-free SLAM can combine learned 3D priors with efficient geometric registration.
- Long-horizon spatial consistency depends on submap construction.

## Subthemes

- Monocular SLAM.
- Calibration-free vision.
- Optical flow.
- Sim(3) registration.
- Pose graph optimization.
- Autonomous driving.

## Connections to Other Papers

Connects to SpatioLM, SAW-Bench, DreamDojo, and embodied/spatial intelligence papers through physical geometry and long-range visual consistency.

## Notes for Cross-Paper Synthesis

VGGT-Motion adds a long-range-spatial-consistency theme: foundation-model perception must still be organized by motion and geometry to support navigation.
