# CLEAR: Context-Aware Learning with End-to-End Mask-Free Inference for Adaptive Video Subtitle Removal

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: HszNb2xE7P
- Authors: Qingdong He; Chaoyi Wang; Peng Tang; Yifan Yang; Xiaobin Hu
- Primary area: applications->computer_vision
- Keywords: Video subtitle removal
- Source URL: https://openreview.net/forum?id=HszNb2xE7P
- PDF URL: https://openreview.net/pdf?id=HszNb2xE7P

## Abstract

Video subtitle removal is essential for content localization and media re-editing, yet existing mask-guided diffusion methods face critical limitations: training inefficiency requiring extensive annotations and full model fine-tuning, inference complexity demanding explicit mask sequences, and static prior utilization unable to adapt to quality variations. We present CLEAR (Context-aware Learning for End-to-end Adaptive subtitle Removal), a lightweight adapter-based framework addressing these challenges through three technical innovations. First, self-supervised prior learning (Stage I) extracts occlusion guidance from video pairs using pixel differences as weak supervision, eliminating annotation dependency while learning generalizable subtitle features across languages. Second, LoRA-based adaptive refinement (Stage II) enables parameter-efficient training that preserves pre-trained visual priors while achieving true mask-free end-to-end inference without external detection modules. Third, adaptive focal weighting dynamically adjusts prior influence based on local quality assessment, effectively handling diverse subtitle styles and noisy guidance signals. Extensive experiments demonstrate CLEAR's superior performance in multilingual subtitle removal while requiring only 0.77% trainable parameters, establishing a new paradigm for efficient video text removal without inference-time mask dependencies.

## One-Sentence Claim

CLEAR removes video subtitles with a lightweight adapter framework that learns weak occlusion priors and performs end-to-end mask-free inference.

## Problem

Existing subtitle-removal systems often need annotated masks, full diffusion-model fine-tuning, and explicit mask sequences at inference, making them costly and brittle for multilingual media editing.

## Core Contribution

The paper proposes a parameter-efficient two-stage framework that replaces annotation-heavy mask guidance with self-supervised prior learning, LoRA refinement, and adaptive prior weighting.

## Method

CLEAR first learns occlusion guidance from video pairs using pixel differences as weak supervision. It then uses LoRA-based adaptive refinement to preserve pretrained visual priors while enabling mask-free inference. Adaptive focal weighting modulates prior influence based on local quality estimates to handle noisy guidance and varied subtitle styles.

## Experiments and Evidence

The abstract reports superior multilingual subtitle-removal performance while training only 0.77% of parameters and eliminating inference-time mask dependencies.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, video-pair construction, temporal consistency metrics, artifacts around complex backgrounds, multilingual coverage, and whether mask-free inference degrades on stylized subtitles.

## Deep Themes

- Weak supervision can replace expensive annotation for media restoration.
- Parameter-efficient adapters preserve visual priors while specializing behavior.
- Inference simplification is a key deployment objective, not just accuracy.

## Subthemes

- Video subtitle removal.
- LoRA adaptation.
- Self-supervised occlusion priors.
- Mask-free inference.
- Multilingual media editing.
- Adaptive quality weighting.

## Connections to Other Papers

Connects to adapter and efficient fine-tuning papers such as SmartFed, and to vision foundation model papers that preserve pretrained priors while adding lightweight task-specific control.

## Notes for Cross-Paper Synthesis

CLEAR adds an applied vision instance of the adapter-efficiency theme: deployment-ready systems reduce both training supervision and inference-time dependencies.
