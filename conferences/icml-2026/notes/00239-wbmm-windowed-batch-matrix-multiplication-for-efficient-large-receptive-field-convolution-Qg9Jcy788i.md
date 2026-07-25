# WBMM: Windowed Batch Matrix Multiplication for Efficient Large Receptive Field Convolution

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Qg9Jcy788i
- Authors: Wan Song; Wei Zhou; Rui Wang; Jun Yu; Toru Kurihara; Jiajia Xu; Shu Zhan
- Primary area: deep_learning->algorithms
- Keywords: Large Kernel Depthwise Convolution;Batch Matrix Multiplication;Efficient Training and Inference;Reparameterization
- Source URL: https://openreview.net/forum?id=Qg9Jcy788i
- PDF URL: https://openreview.net/pdf?id=Qg9Jcy788i

## Abstract

Large kernel depthwise convolutions achieve strong performance but suffer from significant degradation as kernel size grows due to irregular memory access from gather-based computation; while Large Kernel Acceleration (LKA) helps on small feature maps, it becomes counterproductive on large feature maps, even slower than non-accelerated implementations. We propose Windowed Batch Matrix Multiplication (WBMM), which partitions input into contiguous windows and indexes a compact relative position bias table to construct weight matrices, enabling regular memory access via batched matrix multiplication. This yields a unique property: WBMM's throughput improves with larger windows, opposite to depthwise convolutions that degrade with larger kernels. Operator-level benchmarks show WBMM with $14 \times 14$ windows outperforms $5 \times 5$ depthwise convolution baselines in speed while providing a $7.8\times$ larger per-layer receptive field. Combined with inter-block cross-window communication and hierarchical window reparameterization, WBMM achieves comparable or higher accuracy on ImageNet-1K, COCO, and ADE20K with $1.31$--$1.88\times$ training speedup, and demonstrates consistent advantages across GPU, CPU, and edge devices without requiring specialized acceleration kernels. Our code is available at https://github.com/wansong-s/WBMM.

## One-Sentence Claim

WBMM accelerates large-receptive-field convolution by replacing irregular gather-based depthwise convolution with windowed batched matrix multiplication and compact relative-position weights.

## Problem

Large-kernel depthwise convolutions have strong receptive-field benefits but suffer degraded throughput as kernel size grows due to irregular memory access, and existing LKA can be counterproductive on large feature maps.

## Core Contribution

The paper introduces Windowed Batch Matrix Multiplication, plus cross-window communication and hierarchical window reparameterization, to make large receptive fields efficient across hardware without specialized kernels.

## Method

WBMM partitions inputs into contiguous windows, indexes compact relative-position bias tables to construct weight matrices, and executes regular batched matrix multiplication whose throughput improves with larger windows.

## Experiments and Evidence

The abstract reports that 14x14 WBMM beats 5x5 depthwise convolution speed while providing 7.8x larger per-layer receptive field, and achieves comparable or higher accuracy on ImageNet-1K, COCO, and ADE20K with 1.31-1.88x training speedups across GPU, CPU, and edge devices.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model architectures, inference latency, memory overhead, window-size sensitivity, edge-device details, and comparison to optimized vendor kernels.

## Deep Themes

- Algorithmic reformulation can convert irregular memory access into dense hardware-friendly computation.
- Receptive-field scaling depends on data layout, not only model design.
- Efficient operators can improve both training speed and hardware portability.

## Subthemes

- Large-kernel convolution.
- Batch matrix multiplication.
- Reparameterization.
- Relative-position weights.
- Efficient training/inference.
- Vision backbones.

## Connections to Other Papers

Connects to ECHO, TideGS, and systems-efficiency papers through hardware-aware reformulations that unlock scale without special accelerators.

## Notes for Cross-Paper Synthesis

WBMM adds a low-level systems theme: changing the primitive operation can make previously expensive architectural ideas practical.
