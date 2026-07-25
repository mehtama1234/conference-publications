# Depth Anything 3: Recovering the Visual Space from Any Views

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: yirunib8l8
- Authors: Haotong Lin; Sili Chen; Jun Hao Liew; Donny Y. Chen; Zhenyu Li; Yang Zhao; Sida Peng; Hengkai Guo; Xiaowei Zhou; Guang Shi; Jiashi Feng; Bingyi Kang
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Depth Estimation
- Source URL: https://openreview.net/forum?id=yirunib8l8
- PDF URL: https://openreview.net/pdf?id=yirunib8l8

## Abstract

We present Depth Anything 3 (DA3), a model that predicts spatially consistent geometry from an arbitrary number of visual inputs, with or without known camera poses. 
In pursuit of minimal modeling, DA3 yields two key insights:
a single plain transformer (e.g., vanilla DINOv2 encoder) is sufficient as a backbone without architectural specialization, and a singular depth-ray prediction target obviates the need for complex multi-task learning. Through our teacher-student training paradigm, the model achieves a level of detail and generalization on par with Depth Anything 2 (DA2).
We establish a new visual geometry benchmark covering camera pose estimation, any-view geometry and visual rendering. On this benchmark, DA3 sets a new state-of-the-art across all tasks, surpassing prior SOTA VGGT by an average of 35.7\% in camera pose accuracy and 23.6\% in geometric accuracy. Moreover, it outperforms DA2 in monocular depth estimation. All models are trained exclusively on public academic datasets.

## One-Sentence Claim

Depth Anything 3 recovers spatially consistent visual geometry from arbitrary numbers of posed or unposed views using a minimal transformer-based model and a single depth-ray prediction target.

## Problem

Visual geometry systems often rely on specialized architectures, multiple task heads, or assumptions about known camera poses and fixed view counts. A general visual-space recovery model should handle arbitrary inputs while remaining simple and generalizable.

## Core Contribution

The paper contributes DA3, a minimal model for any-view geometry that uses a plain transformer backbone and a singular depth-ray target. It also establishes a new benchmark covering camera pose estimation, any-view geometry, and visual rendering.

## Method

DA3 uses a teacher-student training paradigm and a vanilla transformer-style encoder such as DINOv2. Instead of multi-task learning, it predicts depth rays as the unifying geometry target, allowing one model to work with arbitrary visual inputs with or without known camera poses.

## Experiments and Evidence

The abstract reports state-of-the-art results across all tasks in the new visual geometry benchmark, surpassing prior SOTA VGGT by 35.7% in camera pose accuracy and 23.6% in geometric accuracy. It also reports better monocular depth estimation than Depth Anything 2, with all models trained only on public academic datasets.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect benchmark composition, exact pose and geometry metrics, performance under dynamic scenes, reflective/transparent surfaces, sparse views, unknown intrinsics, and whether public academic datasets cover deployment diversity. Minimal modeling may hide heavy teacher or data engineering.

## Deep Themes

- Unified visual geometry recovery.
- Minimal architecture for multi-view spatial reasoning.
- Depth rays as a common prediction target.
- Public-data training for geometry foundation models.

## Subthemes

- Depth estimation.
- Camera pose estimation.
- Any-view geometry.
- Visual rendering.
- Teacher-student training.

## Connections to Other Papers

Connects to Visual Planning through image-native spatial reasoning, to MetaEmbed through compact multimodal representation design, and to RealPDEBench/PhyWorldBench through benchmarks that test physical or geometric consistency rather than only appearance.

## Notes for Cross-Paper Synthesis

DA3 reinforces the modality-native representation pattern: visual tasks benefit from intermediate targets that preserve geometry directly. Its minimalism also matches a growing preference for fewer specialized heads when one well-chosen target can organize multiple tasks.
