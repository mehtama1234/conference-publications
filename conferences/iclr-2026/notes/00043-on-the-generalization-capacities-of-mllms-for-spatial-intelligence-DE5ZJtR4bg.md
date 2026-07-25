# On the Generalization Capacities of MLLMs for Spatial Intelligence

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: DE5ZJtR4bg
- Authors: Gongjie Zhang; Wenhao Li; Quanhao Qian; Jiuniu Wang; Deli Zhao; Shijian Lu; Ran Xu
- Primary area: foundation or frontier models, including LLMs
- Keywords: 3D Computer Vision;Multimodal Large Language Model;Spatial Intelligence;Embodied AI
- Source URL: https://openreview.net/forum?id=DE5ZJtR4bg
- PDF URL: https://openreview.net/pdf?id=DE5ZJtR4bg

## Abstract

Multimodal Large Language Models (MLLMs) that directly process RGB inputs for tasks like 3D localization and navigation have shown remarkable potential. However, we argue that these ``RGB-only'' approaches are fundamentally flawed in their ability to generalize across cameras. By ignoring camera parameters, they entangle an object's physical properties with the camera's perspective, creating an irresolvable ambiguity. We show this leads MLLMs to overfit to the training camera distribution, rather than learning true and generalizable 3D geometric principles. To address this, we propose Camera-Aware MLLM framework for spatial MLLMs. It learns generalizable spatial reasoning by: (i) injecting camera intrinsics via a dense embedding that conditions each visual token; (ii) introducing a camera-aware data augmentation strategy that synthetically varies camera parameters, forcing the model to disentangle camera properties from scene content; and (iii) distilling geometric priors from a 3D vision foundation model. Extensive experiments demonstrate that camera-aware MLLMs substantially outperform their naive counterparts, particularly in cross-camera generalization tests on spatially-grounded tasks, indicating that camera-awareness is not only beneficial but also a prerequisite for robust and generalizable spatial intelligence in MLLMs.

## One-Sentence Claim

Spatial MLLMs need camera-aware inputs because RGB-only training entangles object geometry with camera perspective and fails to generalize across cameras.

## Problem

MLLMs are increasingly used for 3D localization and navigation from RGB inputs. But RGB-only approaches ignore camera intrinsics, making physical object properties ambiguous with camera perspective.

This causes models to overfit the training-camera distribution rather than learn generalizable 3D geometric principles.

## Core Contribution

The paper proposes a Camera-Aware MLLM framework for spatial reasoning.

It injects camera intrinsics through dense embeddings that condition each visual token, uses camera-aware augmentation to vary camera parameters, and distills geometric priors from a 3D vision foundation model.

## Method

Camera intrinsics are encoded densely and attached to visual tokens so the model can interpret pixels relative to the camera model.

Synthetic augmentation varies camera parameters to force disentanglement between camera properties and scene content. Distillation from a 3D vision foundation model supplies additional geometric priors.

## Experiments and Evidence

The abstract reports substantial improvements over naive RGB-only MLLMs, especially on cross-camera generalization for spatially grounded tasks.

It argues camera-awareness is a prerequisite for robust generalizable spatial intelligence in MLLMs.

## Limits and Failure Modes

Camera-aware methods depend on accurate camera intrinsics, which may be missing or noisy in real deployments. Distilled 3D priors may also inherit limitations of the teacher model.

Because this note is abstract-only, details still need checking: task suite, camera distributions, dense embedding design, augmentation ranges, teacher model, and robustness to calibration error.

## Deep Themes

- Geometry-aware multimodal reasoning: visual tokens need camera context to support 3D inference.
- Disentangling viewpoint from object properties: generalization requires explicit camera factors.
- Spatial intelligence beyond RGB: raw pixels are insufficient for embodied generalization.
- Foundation-model distillation for geometry: 3D priors can be transferred into MLLMs.

## Subthemes

- Camera intrinsics embeddings.
- Cross-camera generalization.
- Camera-aware augmentation.
- 3D foundation model distillation.

## Connections to Other Papers

This connects to PanoWorld-X, SplAttN, VectorWorld, MomaGraph, and GLANCE through geometry-aware embodied AI.

It also relates to MetaphorVU and PRISM because structured intermediate representations help models generalize beyond surface pixels.

## Notes for Cross-Paper Synthesis

This paper reinforces the geometry-aware representation theme: spatial generalization requires making camera and scene factors explicit.
