# DTO-KD: Dynamic Trade-off Optimization for Effective Knowledge Distillation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: QMItTyQW92
- Authors: Zeeshan Hayder; Ali Cheraghian; Lars Petersson; Mehrtash Harandi; Richard Hartley
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Knowledge Distillation
- Source URL: https://openreview.net/forum?id=QMItTyQW92
- PDF URL: https://openreview.net/pdf?id=QMItTyQW92

## Abstract

Knowledge Distillation (KD) is a widely adopted framework for compressing large models into compact student models by transferring knowledge from a high-capacity teacher. Despite its success, KD presents two persistent challenges: (1) the trade-off between optimizing for the primary task loss and mimicking the teacher's outputs, and (2) the gradient disparity arising from architectural and representational mismatches between teacher and student models. In this work, we propose Dynamic Trade-off Optimization for Knowledge Distillation (DTO-KD), a principled multi-objective optimization formulation of KD that dynamically balances task and distillation losses at the gradient level. Specifically, DTO-KD resolves two critical issues in gradient-based KD optimization: (i) gradient conflict, where task and distillation gradients are directionally misaligned, and (ii) gradient dominance, where one objective suppresses learning progress on the other. Our method adapts per-iteration trade-offs by leveraging gradient projection techniques to ensure balanced and constructive updates. We evaluate DTO-KD on large-scale benchmarks including ImageNet-1K for classification and COCO for object detection. Across both tasks, DTO-KD consistently outperforms prior KD methods, yielding state-of-the-art accuracy and improved convergence behavior. Furthermore, student models trained with DTO-KD exceed the performance of their non-distilled counterparts, demonstrating the efficacy of our multi-objective formulation for KD.

## One-Sentence Claim

DTO-KD formulates knowledge distillation as multi-objective gradient optimization that dynamically balances task and teacher-mimicry losses to avoid conflict and dominance.

## Problem

Knowledge distillation must optimize the primary task while also matching teacher outputs. These objectives can conflict, especially when teacher and student architectures or representations differ.

Static loss weights can allow one objective to dominate or push gradients in opposing directions, slowing convergence or reducing final student quality.

## Core Contribution

The paper introduces Dynamic Trade-off Optimization for Knowledge Distillation.

DTO-KD dynamically adjusts per-iteration tradeoffs at the gradient level, addressing gradient conflict and gradient dominance through projection techniques.

## Method

DTO-KD treats task learning and distillation as a multi-objective optimization problem.

At each iteration, it analyzes task and distillation gradients, projects or balances them to encourage constructive updates, and prevents either objective from suppressing the other.

## Experiments and Evidence

The abstract reports evaluations on ImageNet-1K classification and COCO object detection.

DTO-KD consistently outperforms prior distillation methods, improves convergence behavior, and trains student models that exceed the performance of non-distilled counterparts.

## Limits and Failure Modes

Gradient-level balancing may add computational overhead and may depend on stable gradient estimates. It may also behave differently for language models or self-supervised objectives than for vision classification/detection.

Because this note is abstract-only, details still need checking: projection algorithm, compute overhead, teacher/student architectures, loss formulations, hyperparameters, and failure cases when teacher quality is poor.

## Deep Themes

- Distillation as multi-objective optimization: teacher matching and task performance are distinct objectives requiring dynamic mediation.
- Gradient conflict diagnostics: optimization geometry exposes why static KD weights fail.
- Adaptive training tradeoffs: per-iteration balancing replaces fixed handcrafted schedules.
- Compression without student degradation: distillation aims to make smaller models better than ordinary training, not merely cheaper.

## Subthemes

- Knowledge distillation.
- Gradient projection.
- Task-distillation tradeoff.
- Gradient dominance.

## Connections to Other Papers

This connects to WSM, RAIN-Merging, SafeDPO, and Train-before-Test through behavior transfer and adaptation while preserving target performance.

It also relates to optimization papers that treat gradient geometry as the right level for intervention.

## Notes for Cross-Paper Synthesis

DTO-KD adds to the adaptive-objective theme: fixed loss mixtures are giving way to gradient-aware control of competing learning goals.
