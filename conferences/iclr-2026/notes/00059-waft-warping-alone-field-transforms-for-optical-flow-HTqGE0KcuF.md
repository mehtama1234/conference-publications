# WAFT: Warping-Alone Field Transforms for Optical Flow

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: HTqGE0KcuF
- Authors: Yihan Wang; Jia Deng
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Optical Flow; Computer Vision; Warping; Dense Correspondences
- Source URL: https://openreview.net/forum?id=HTqGE0KcuF
- PDF URL: https://openreview.net/pdf?id=HTqGE0KcuF

## Abstract

We introduce Warping-Alone Field Transforms (WAFT), a simple and effective
method for optical flow. WAFT is similar to RAFT but replaces cost volume with
high-resolution warping, achieving better accuracy with lower memory cost. This
design challenges the conventional wisdom that constructing cost volumes is nec-
essary for strong performance. WAFT is a simple and flexible meta-architecture
with minimal inductive biases and reliance on custom designs. Compared with
existing methods, WAFT ranks 1st on Spring, Sintel, and KITTI benchmarks,
achieves the best zero-shot generalization on KITTI, while being up to 4.1× faster
than methods with similar performance. Code and model weights will be available
upon acceptance.

## One-Sentence Claim

WAFT shows high-resolution warping can replace cost volumes in optical flow, improving accuracy and memory efficiency while retaining a simple meta-architecture.

## Problem

Optical flow methods often rely on cost volumes to compare dense correspondences. Cost volumes are powerful but memory-intensive and architecturally heavy.

The paper challenges the assumption that cost-volume construction is necessary for top optical-flow performance.

## Core Contribution

The paper introduces Warping-Alone Field Transforms, WAFT, an optical-flow approach similar to RAFT but replacing cost volumes with high-resolution warping.

The contribution is a simpler, flexible architecture with fewer custom inductive biases and lower memory cost.

## Method

WAFT uses high-resolution warping operations to iteratively align features and estimate dense flow. It removes the explicit cost-volume component common in RAFT-like systems.

This makes the architecture lighter and faster while preserving strong correspondence estimation.

## Experiments and Evidence

The abstract reports rank 1 performance on Spring, Sintel, and KITTI benchmarks.

WAFT achieves best zero-shot generalization on KITTI and is up to 4.1x faster than methods with similar performance.

## Limits and Failure Modes

Warping-only designs may struggle with very large displacements, occlusions, or repetitive textures if the warping initialization is poor.

Because this note is abstract-only, details still need checking: architecture, training data, benchmark splits, memory measurements, runtime setup, and ablations against cost-volume variants.

## Deep Themes

- Rethinking canonical modules: cost volumes may not be essential for optical flow.
- Warping as sufficient correspondence engine: high-resolution alignment can carry dense matching.
- Simplicity and speed: reducing architectural machinery can improve both performance and efficiency.
- Generalization through reduced bias: fewer custom designs may improve zero-shot transfer.

## Subthemes

- Optical flow.
- High-resolution warping.
- RAFT without cost volume.
- Dense correspondence generalization.

## Connections to Other Papers

This connects to FlashVID, IO-aware GNN kernels, and FFDP through replacing expensive intermediate structures with more efficient operations.

It also relates to video generation and motion attribution papers because accurate motion estimation underlies temporal visual modeling.

## Notes for Cross-Paper Synthesis

WAFT adds an architectural minimalism theme: sometimes a dominant intermediate representation can be removed if the remaining operation captures the needed structure.
