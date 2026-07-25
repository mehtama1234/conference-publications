# TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: K8UWWJUNYf
- Authors: Chonghao Zhong; Linfeng Shi; Chen Hua; Tiecheng Sun; Hao Zhao; Binhang Yuan; Chaojian Li
- Primary area: general_machine_learning->hardware_and_software
- Keywords: 3D Gaussian Splatting;Machine Learning Systems
- Source URL: https://openreview.net/forum?id=K8UWWJUNYf
- PDF URL: https://openreview.net/pdf?id=K8UWWJUNYf

## Abstract

Training 3D Gaussian Splatting (3DGS) at billion-primitive scale is fundamentally memory-bound: each Gaussian primitive carries a large attribute vector, and the aggregate parameter table quickly exceeds GPU capacity, limiting prior systems to tens of millions of Gaussians on commodity single-GPU hardware. We observe that 3DGS training is inherently sparse and trajectory-conditioned: each iteration activates only the Gaussians visible from the current camera batch, so GPU memory can serve as a working-set cache rather than a persistent parameter store. Building on this insight, we introduce TideGS, an out-of-core training framework that manages parameters across an SSD-CPU-GPU hierarchy via three synergistic techniques: block-virtualized geometry for SSD-aligned spatial locality, a hierarchical asynchronous pipeline to overlap I/O with computation, and trajectory-adaptive differential streaming that transfers only incremental working-set deltas between iterations. Experiments show that TideGS enables training with over one billion Gaussians on a single 24-GB GPU while achieving the best reconstruction quality among evaluated single-GPU baselines on large-scale scenes, scaling beyond prior out-of-core baselines (e.g., ~100M Gaussians) and standard in-memory training (e.g., ~11M Gaussians). Project page: https://sponge-lab.github.io/TideGS/

## One-Sentence Claim

TideGS trains over one billion 3D Gaussian Splatting primitives on a single 24GB GPU by treating GPU memory as a sparse trajectory-conditioned working-set cache.

## Problem

3DGS training is memory-bound because each primitive has a large attribute vector, so billion-scale scenes exceed GPU capacity and prior single-GPU systems are limited to much smaller primitive counts.

## Core Contribution

The paper introduces an out-of-core 3DGS training system that exploits visibility sparsity and camera-trajectory locality across an SSD-CPU-GPU memory hierarchy.

## Method

TideGS uses block-virtualized geometry for SSD-aligned spatial locality, hierarchical asynchronous I/O-compute pipelining, and trajectory-adaptive differential streaming that transfers only incremental working-set deltas between iterations.

## Experiments and Evidence

The abstract reports training more than one billion Gaussians on a single 24GB GPU, achieving the best reconstruction quality among evaluated single-GPU baselines on large scenes, and scaling beyond prior out-of-core roughly 100M-Gaussian and in-memory roughly 11M-Gaussian baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: scene datasets, throughput, SSD requirements, cache miss behavior, convergence effects, comparison hardware, and whether sparse visibility assumptions hold for unusual trajectories.

## Deep Themes

- Systems design can unlock scale by exploiting sparsity in training access patterns.
- Memory hierarchy becomes an algorithmic resource for large 3D representations.
- Trajectory-conditioned working sets are central for scalable spatial learning.

## Subthemes

- 3D Gaussian Splatting.
- Out-of-core optimization.
- SSD-CPU-GPU hierarchy.
- Sparse visibility.
- Asynchronous pipelines.
- Large-scale scene reconstruction.

## Connections to Other Papers

Connects to VGGT-Motion, 3ViewSense, and XR-1 through spatial/embodied representation, and to efficiency papers where capability depends on systems-level resource orchestration.

## Notes for Cross-Paper Synthesis

TideGS adds a systems-scale spatial theme: physical-scene modeling may advance as much through memory and dataflow design as through new model architectures.
