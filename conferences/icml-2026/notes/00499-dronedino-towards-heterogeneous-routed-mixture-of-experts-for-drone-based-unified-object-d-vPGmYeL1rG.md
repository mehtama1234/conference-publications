# DroneDINO: Towards Heterogeneous Routed Mixture of Experts for Drone-based Unified Object Detection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vPGmYeL1rG
- Authors: Dongdong Li; Rui Chen; Yan Fan; Yan Liu; Yangliu Kuai; Pengfei Zhu
- Primary area: applications->computer_vision
- Keywords: drone-based object detection;unified object detection;mixture-of-experts
- Source URL: https://openreview.net/forum?id=vPGmYeL1rG
- PDF URL: https://openreview.net/pdf?id=vPGmYeL1rG

## Abstract

Recently, the rapid development of low-altitude aerial applications has driven the need for drone-based unified detectors. In contrast to task-specific detectors that suffer from poor scalability across diverse scenarios, existing unified detectors leverage the Mixture-of-Experts (MoE) architecture to learn task-aware features from diverse datasets. However, the imbalanced multi-task data distribution leads to over-activation of experts for dominant tasks and under-activation for others. To enable balanced feature learning, this paper combines three detection paradigms (RGB, IR, and RGB-IR) into a unified framework termed DroneDINO. DroneDINO extends DINO by introducing heterogeneous routed MoEs that organize experts into three functional groups: shared, task-specific, and dynamic. Unlike conventional dynamic experts where the top-$k$ experts are activated for each input, the shared expert is activated for all inputs, while each task-specific expert is activated exclusively for the matching task. To ensure inputs are routed to appropriate experts and yield task-discriminative features, we propose a task-recognition auxiliary training strategy to penalize features with low task-discriminability. Experiments demonstrate the effectiveness and generalizability of DroneDINO, which consistently outperforms state-of-the-art unified and task-specific detectors across multiple drone-based detection benchmarks.

## One-Sentence Claim

DroneDINO improves unified drone object detection by routing RGB, IR, and RGB-IR inputs through shared, task-specific, and dynamic experts with auxiliary task-recognition supervision.

## Problem

Drone-based object detection must work across diverse low-altitude scenarios and sensing modalities. Task-specific detectors scale poorly, while unified MoE detectors can suffer from imbalanced multi-task data: dominant tasks over-activate experts and weaker tasks underuse capacity.

The challenge is to share features across modalities while preserving task-discriminative specialization and balanced expert utilization.

## Core Contribution

The paper introduces DroneDINO, extending DINO with heterogeneous routed MoEs for RGB, infrared, and RGB-IR detection. Experts are organized into shared, task-specific, and dynamic groups.

Unlike conventional top-k dynamic expert routing, the shared expert activates for all inputs, task-specific experts activate only for matching tasks, and dynamic experts provide flexible extra capacity. A task-recognition auxiliary objective encourages task-discriminative features and appropriate routing.

## Method

DroneDINO combines three detection paradigms in one framework. The routing design hard-codes some expert roles: universal sharing for common features, exclusive task experts for modality-specific features, and dynamic experts for input-dependent variation.

The auxiliary training strategy penalizes low task-discriminability, encouraging representations to route to suitable experts and avoid dominance by high-resource tasks.

## Experiments and Evidence

The abstract reports consistent outperformance over state-of-the-art unified and task-specific detectors across multiple drone-based detection benchmarks. It claims effectiveness and generalizability.

Full-paper reading should verify benchmark names, modality splits, expert utilization statistics, data imbalance levels, real-time constraints, and ablations for each expert group and auxiliary loss.

## Limits and Failure Modes

Task-specific routing assumes known modality/task labels. Performance under noisy metadata, sensor failures, or unseen modalities may require additional robustness.

MoE routing can still become imbalanced despite auxiliary losses, and drone deployment adds constraints such as onboard compute, changing altitude, weather, and motion blur.

## Deep Themes

- Heterogeneous MoE for multimodal detection: expert roles are structured by modality and task.
- Balanced capacity under data imbalance: routing design counters dominant-task overactivation.
- Unified detection across sensor paradigms: RGB, IR, and fused inputs share one architecture.
- Auxiliary task recognition as routing supervision: discriminability guides expert specialization.

## Subthemes

- Shared experts preserve cross-task commonality.
- Task-specific experts protect modality-specific features.
- Dynamic experts support input-dependent variation.
- Drone perception requires scalable unified detectors.

## Connections to Other Papers

DroneDINO connects to ScaleMoE, MoE compression, WestWorld, and WIRE through conditional capacity and domain-structured perception. It also relates to multimodal retrieval and concept binding because cross-modal features need both sharing and specialization.

It fits the broader systems theme that MoE must be routed according to meaningful heterogeneity, not just top-k load balancing.

## Notes for Cross-Paper Synthesis

The synthesis point is that MoE design is becoming semantic. Experts are assigned functional roles tied to modality and task to prevent data imbalance from dictating capacity allocation.
