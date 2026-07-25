# When Attributes Disagree: Gradient Conflict in Image Aesthetic Assessment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GrIs035ec3
- Authors: Ye Wang; Maocai Dai; Jiang Xie; Xiuli Bi; Fei Tao; Xiao Li; Hong Yu
- Primary area: applications->computer_vision
- Keywords: Image Aesthetic Assessment;Sensitivity-Guided Learning;Optimization Interference
- Source URL: https://openreview.net/forum?id=GrIs035ec3
- PDF URL: https://openreview.net/pdf?id=GrIs035ec3

## Abstract

Image Aesthetic Assessment (IAA) predicts an image’s overall aesthetic score, yet aesthetic is influenced by multiple attributes whose relative importance varies with image content and usage scenarios. Under end-to-end training with only overall-score supervision, attribute signals are blended, which can cause gradient conflict across samples dominated by different attributes, resulting in gradient cancellation and persistent systematic bias. To address these issues, we propose AGREE (Attribute-guided Gradient Routing for Establishing Agreement), which learns attribute-specific subspaces and performs gradient routing based on sample-wise attribute sensitivity estimated via perturbation analysis. AGREE further reduces feature coupling across attributes with semantic anchors and improves robustness via error-aware reweighting. Experiments on AVA, LAPIS, AADB, TAD66K, and PARA show consistent improvements over diverse IAA baseline models, and AGREE is plug-and-play for existing end-to-end IAA methods without modifying their original architectures. To our knowledge, this work is among the early efforts in IAA to systematically study gradient conflict and provide an effective solution. The code is available at https://dahat364.github.io/AGREE/.

## One-Sentence Claim

AGREE improves image aesthetic assessment by routing gradients through attribute-specific subspaces based on sample-wise attribute sensitivity.

## Problem

Overall-score supervision blends multiple aesthetic attributes, causing gradient conflict and cancellation when different samples depend on different attributes.

## Core Contribution

The paper identifies gradient conflict in IAA and proposes Attribute-guided Gradient Routing for Establishing Agreement.

## Method

AGREE estimates sample-wise attribute sensitivity through perturbation analysis, learns attribute-specific subspaces, routes gradients accordingly, reduces feature coupling with semantic anchors, and uses error-aware reweighting for robustness.

## Experiments and Evidence

The abstract reports consistent improvements over diverse IAA baselines on AVA, LAPIS, AADB, TAD66K, and PARA, with plug-and-play compatibility for existing end-to-end IAA models.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: attribute definitions, perturbation sensitivity reliability, semantic anchor construction, and robustness to subjective/cultural aesthetic variation.

## Deep Themes

- Subjective visual judgments have competing attribute gradients.
- Fine-grained attribute routing can reduce optimization interference.
- Overall labels can hide systematic bias from blended latent criteria.

## Subthemes

- Image aesthetic assessment.
- Gradient conflict.
- Attribute sensitivity.
- Semantic anchors.
- Error-aware reweighting.
- Subjective perception.

## Connections to Other Papers

Connects to UniPercept, EEmo-Logic, VALUEFLOW, and subjective construct measurement papers through multidimensional human judgments.

## Notes for Cross-Paper Synthesis

AGREE adds an attribute-conflict theme: subjective evaluation models need to separate latent criteria before optimizing a single score.
