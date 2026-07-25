# A Scalable Distributed Framework for Multimodal GigaVoxel Image Registration

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 8dLexnao2h
- Authors: Rohit Jena; Vedant Zope; Pratik Chaudhari; James Gee
- Primary area: infrastructure, software libraries, hardware, systems, etc.
- Keywords: image registration;distributed optimization;CUDA kernels;neuroanatomy
- Source URL: https://openreview.net/forum?id=8dLexnao2h
- PDF URL: https://openreview.net/pdf?id=8dLexnao2h

## Abstract

In this work, we propose FFDP, a set of IO-aware non-GEMM fused kernels supplemented with a distributed framework for image registration at unprecedented scales. Image registration is an inverse problem fundamental to biomedical and life sciences, but algorithms have not scaled in tandem with image acquisition capabilities. Our framework complements existing model parallelism techniques proposed for large-scale transformer training by optimizing non-GEMM bottlenecks and enabling convolution-aware tensor sharding. We demonstrate unprecedented capabilities by performing multimodal registration of a 100μm ex-vivo human brain MRI volume at native resolution – an inverse problem more than 570× larger than a standard clinical datum in about a minute using only 8 A6000 GPUs. FFDP accelerates existing state-of-the-art optimization and deep learning registration pipelines by upto 6 − 7× while reducing peak memory consumption by 20 − 59%. Comparative analysis on a 250μm dataset shows that FFDP can fit upto 64× larger problems than existing SOTA on a single GPU, and highlights both the performance and efficiency gains of FFDP compared to SOTA image registration methods.

## One-Sentence Claim

FFDP scales multimodal gigavoxel image registration by combining IO-aware non-GEMM fused kernels with distributed convolution-aware tensor sharding.

## Problem

Biomedical image acquisition has outpaced image-registration algorithms. Registration is essential for life sciences and neuroanatomy, but native-resolution large-volume registration creates inverse problems too large for conventional pipelines.

The bottlenecks are non-GEMM operations, memory footprint, and sharding patterns not designed for convolution-heavy registration.

## Core Contribution

The paper proposes FFDP, a distributed framework and set of IO-aware fused kernels for large-scale image registration.

It complements transformer-style model parallelism by targeting non-GEMM bottlenecks and enabling convolution-aware tensor sharding.

## Method

FFDP introduces fused CUDA kernels for registration operations that are not dominated by GEMM. It distributes the registration computation with sharding aligned to convolutional access patterns.

The framework accelerates both optimization-based and deep-learning registration pipelines while lowering peak memory.

## Experiments and Evidence

The abstract reports multimodal registration of a 100 micrometer ex-vivo human brain MRI volume at native resolution, an inverse problem more than 570x larger than a standard clinical datum, in about one minute on 8 A6000 GPUs.

FFDP accelerates existing state-of-the-art registration pipelines by 6-7x, reduces peak memory by 20-59 percent, and fits up to 64x larger problems than existing SOTA on a single GPU in a 250 micrometer comparison.

## Limits and Failure Modes

The framework depends on GPU availability and on registration workloads matching its sharding and kernel assumptions. Biomedical registration quality also depends on modality similarity, deformation regularization, and ground-truth validation.

Because this note is abstract-only, details still need checking: registration objectives, kernel list, communication overhead, accuracy metrics, deformation constraints, and failure cases on noisy or highly nonrigid tissue.

## Deep Themes

- Scientific computing at acquisition scale: algorithms must match modern instrument resolution.
- IO-aware non-GEMM systems: not all ML-scale bottlenecks look like transformer matrix multiplication.
- Distributed inverse problems: model parallelism ideas transfer to biomedical optimization when adapted.
- Systems as scientific enabler: new biological analyses become possible when registration fits in memory and time.

## Subthemes

- Gigavoxel multimodal registration.
- Fused CUDA kernels.
- Convolution-aware tensor sharding.
- Neuroanatomy infrastructure.

## Connections to Other Papers

This connects to ICML IO-aware GNN kernels, KDE kernel algebra, FFCC, and EntroKV through systems work that targets the true bottleneck rather than the high-level model.

It also relates to PRISM and neuroscience papers because it supplies infrastructure for high-resolution brain data analysis.

## Notes for Cross-Paper Synthesis

FFDP adds a scientific-systems theme: progress on biomedical ML often requires low-level kernel and distribution work, not just better models.
