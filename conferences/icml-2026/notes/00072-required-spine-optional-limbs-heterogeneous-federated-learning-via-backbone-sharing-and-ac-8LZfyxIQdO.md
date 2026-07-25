# Required Spine Optional Limbs: Heterogeneous Federated Learning via Backbone-sharing and Activation-guided Selection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 8LZfyxIQdO
- Authors: Mingsheng Cao; Hongliang Chen; Ming Hu; Fei Gao; Qiaolong Ding; Wenke Huang; Xiaofei Xie; Junlong Zhou
- Primary area: applications->computer_vision
- Keywords: Federated Learning; Device Heterogeneity
- Source URL: https://openreview.net/forum?id=8LZfyxIQdO
- PDF URL: https://openreview.net/pdf?id=8LZfyxIQdO

## Abstract

Although Federated Learning (FL) offers advantages in privacy-preserving for cross-device collaborative learning, its practical deployment remains severely constrained by heterogeneous hardware resources and non-IID (non-independent and identically distributed) data across devices. Sub-model extraction has emerged as a widely adopted strategy for enabling collaborative training among devices with heterogeneous models. However, existing sub-model extraction methods in FL typically rely on coarse-grained stochastic selection or rigid rule-based neuron selection, which severely limits training performance. Specifically, stochastic strategies lead to severe parameter conflicts under non-IID data distributions, while rule-based approaches lack diversity in neuron selection per device, preventing comprehensive parameter optimization. To address this problem, this paper presents a novel sub-model extraction-based FL framework, named SpineFL, which adopts a backbone-sharing mechanism and an activation-guided pruning strategy for sub-model extraction. Specifically, SpineFL decomposes each global model layer into two portions: i) a mandatory backbone shared by all the sub-models to maintain model generalization, and ii) a dynamic portion for sub-model extraction. SpineFL adopts the activation-guided selection strategy to probabilistically select neurons according to their activation frequency from the dynamic portion to generate sub-model, where neurons exhibiting higher historical activation are more likely to be included, thereby simultaneously addressing parameter conflicts while preserving selection diversity. Experimental results demonstrate that compared with state-of-the-art heterogeneous FL methods, SpineFL can achieve up to 3.28% accuracy improvement.

## One-Sentence Claim

SpineFL improves heterogeneous federated learning by sharing a mandatory backbone while selecting optional neurons through activation-guided sub-model extraction.

## Problem

Cross-device federated learning faces both hardware heterogeneity and non-IID data, while existing sub-model extraction methods either create parameter conflicts or restrict neuron diversity.

## Core Contribution

The paper introduces SpineFL, a heterogeneous FL framework that decomposes layers into shared backbone and dynamic portions, using activation histories to guide probabilistic neuron selection.

## Method

Each global layer is split into a required spine shared by all devices and optional dynamic neurons. Devices sample from the dynamic portion according to historical activation frequency, balancing common generalization with diverse, device-adapted parameter optimization.

## Experiments and Evidence

The abstract reports up to 3.28% accuracy improvement over state-of-the-art heterogeneous FL methods.

## Limits and Failure Modes

ArXiv search failed with rate-limit/service errors for this batch, so this note is abstract-only. Details still need checking: how activation frequencies are aggregated privately, communication overhead, model families, and non-IID severity.

## Deep Themes

- Federated learning needs architecture-level adaptation to device heterogeneity.
- Shared cores and optional capacity can balance generalization with personalization.
- Activation statistics can guide sub-model allocation.

## Subthemes

- Heterogeneous federated learning.
- Sub-model extraction.
- Backbone sharing.
- Activation-guided pruning.
- Non-IID data.
- Device constraints.

## Connections to Other Papers

Connects to EcoVLA, OmniFit, TACO, and hybrid sequence models through adaptive resource allocation. It also links to privacy/deployment papers because FL constraints are both statistical and systems-level.

## Notes for Cross-Paper Synthesis

SpineFL contributes a shared-spine/optional-capacity pattern: deployed collaborative models may need a stable common core plus adaptive local structure.
