# Just Noticeable Difference Modeling for Deep Visual Features

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: RxjGbyLFT1
- Authors: Rui Zhao; Wenrui Li; Lin Zhu; Yajing Zheng; Weisi Lin
- Primary area: applications->computer_vision
- Keywords: Just Noticeable Difference;Feature Quality Modeling
- Source URL: https://openreview.net/forum?id=RxjGbyLFT1
- PDF URL: https://openreview.net/pdf?id=RxjGbyLFT1

## Abstract

Deep visual features are increasingly used as the interface in vision systems, motivating the need to describe feature characteristics and control feature quality for machine perception. Just noticeable difference (JND) characterizes the maximum imperceptible distortion for images under human or machine vision. Extending it to deep visual features naturally meets the above demand by providing a task-aligned tolerance boundary in feature space, offering a practical reference for controlling feature quality under constrained resources. We propose FeatJND, a task-aligned JND formulation that predicts the maximum tolerable per-feature perturbation map while preserving downstream task performance. We propose a FeatJND estimator at standardized split points and validate it across image classification, detection, and instance segmentation. Under matched distortion strength, FeatJND-based distortions consistently preserve higher task performance than unstructured Gaussian perturbations, and attribution visualizations suggest FeatJND can suppress non-critical feature regions. As an application, we further apply FeatJND to token-wise dynamic quantization and show that FeatJND-guided step-size allocation yields clear gains over random step-size permutation and global uniform step size under the same noise budget. The source code is available at https://github.com/ruizhao26/FeatJND.

## One-Sentence Claim

FeatJND predicts task-aligned tolerable perturbation maps in deep visual feature space, enabling feature-quality control and better dynamic quantization under fixed noise budgets.

## Problem

Deep visual features increasingly serve as system interfaces, but there is little task-aligned way to describe how much feature distortion is tolerable for downstream machine perception.

## Core Contribution

The paper extends just noticeable difference modeling to deep features and proposes an estimator at standardized split points that predicts maximum per-feature perturbations preserving task performance.

## Method

FeatJND learns task-aligned perturbation tolerance maps, validates them across classification, detection, and instance segmentation, and uses them to allocate token-wise quantization step sizes.

## Experiments and Evidence

The abstract reports that FeatJND-based distortions preserve higher task performance than Gaussian perturbations under matched distortion strength, attribution suggests suppression of non-critical regions, and FeatJND-guided quantization improves over random or global uniform step-size allocation.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: backbones, split points, feature metrics, quantization settings, cross-task transfer, and whether human-perceptual JND analogies hold for machine features.

## Deep Themes

- Feature-space quality should be measured by downstream task tolerance.
- Quantization can allocate precision according to feature importance.
- Machine perception has its own just-noticeable-difference structure.

## Subthemes

- Deep visual features.
- Just noticeable difference.
- Feature quality modeling.
- Dynamic quantization.
- Task-aligned perturbations.
- Attribution visualization.

## Connections to Other Papers

Connects to WBMM, ECHO, and efficiency papers through resource-aware model execution, and to interpretability/attribution work through feature-importance maps.

## Notes for Cross-Paper Synthesis

FeatJND adds a tolerance-boundary theme: efficient perception systems should know which feature perturbations matter for the task and which can be safely compressed or distorted.
