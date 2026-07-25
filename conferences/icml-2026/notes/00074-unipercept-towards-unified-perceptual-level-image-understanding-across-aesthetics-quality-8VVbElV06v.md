# UniPercept: Towards Unified Perceptual-Level Image Understanding across Aesthetics, Quality, Structure, and Texture

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 8VVbElV06v
- Authors: Shuo Cao; Jiayang Li; Xiaohui Li; Yuandong Pu; Kaiwen Zhu; Yuanting Gao; Siqi Luo; Yi Xin; Qi Qin; Yu Zhou; Xiangyu Chen; Wenlong Zhang; Bin Fu; Yu Qiao; Yihao Liu
- Primary area: applications->computer_vision
- Keywords: Multimodal Large Language Models;Perceptual Image Understanding;Reward Modeling
- Source URL: https://openreview.net/forum?id=8VVbElV06v
- PDF URL: https://openreview.net/pdf?id=8VVbElV06v

## Abstract

Multimodal large language models (MLLMs) have achieved remarkable progress in visual understanding tasks such as visual grounding, segmentation, and captioning. However, their ability to perceive perceptual-level image features remains limited. In this work, we present UniPercept-Bench, a unified framework for perceptual-level image understanding across three key domains: Aesthetics, Quality, Structure and Texture. We establish a hierarchical definition system and construct large-scale datasets to evaluate perceptual-level image understanding. Based on this foundation, we develop a strong baseline UniPercept trained via Domain-Adaptive Pre-Training and Task-Aligned RL, enabling robust generalization across both Visual Rating (VR) and Visual Question Answering (VQA) tasks. UniPercept outperforms existing MLLMs on perceptual-level image understanding and can serve as a plug-and-play reward model for text-to-image generation. This work defines perceptual-level image understanding in the era of MLLMs and, through the introduction of a comprehensive benchmark together with a strong baseline, provides a solid foundation for advancing perceptual-level multimodal image understanding.

## One-Sentence Claim

UniPercept defines and benchmarks perceptual-level image understanding across aesthetics, quality, structure, and texture, then trains a baseline that can also serve as a reward model.

## Problem

MLLMs perform well on semantic visual tasks but remain weak at perceptual-level judgments such as aesthetic quality, image quality, structure, and texture.

## Core Contribution

The paper introduces UniPercept-Bench with a hierarchical definition system and large-scale datasets, plus UniPercept trained with Domain-Adaptive Pre-Training and Task-Aligned RL.

## Method

The benchmark spans visual rating and visual question answering forms of perceptual judgment. The model is adapted to the perceptual domains through domain-specific pretraining and RL aligned to the target tasks.

## Experiments and Evidence

The abstract reports that UniPercept outperforms existing MLLMs on perceptual-level image understanding and can be used as a plug-and-play reward model for text-to-image generation.

## Limits and Failure Modes

ArXiv search failed with rate-limit/service errors for this batch, so this note is abstract-only. Details still need checking: dataset construction, human rating reliability, reward-model calibration, and coverage of perceptual cultures/preferences.

## Deep Themes

- Multimodal understanding is expanding from object semantics to perceptual judgment.
- Benchmarks increasingly define the target capability before optimizing models.
- Reward models for generation need richer perceptual criteria.

## Subthemes

- Perceptual image understanding.
- Aesthetics and quality assessment.
- Structure and texture reasoning.
- MLLM benchmarking.
- Visual rating and VQA.
- Text-to-image reward modeling.

## Connections to Other Papers

Connects to Copyright-Bench and other benchmark papers through realistic evaluation design. It also links to multimodal and generative-model papers where reward models guide image generation.

## Notes for Cross-Paper Synthesis

UniPercept adds a capability-definition theme: progress sometimes begins by naming and structuring an under-measured perceptual skill.
