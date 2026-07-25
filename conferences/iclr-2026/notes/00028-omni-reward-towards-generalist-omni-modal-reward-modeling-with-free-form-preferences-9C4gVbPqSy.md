# Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 9C4gVbPqSy
- Authors: Zhuoran Jin; Hongbang Yuan; Kejian Zhu; Jiachun Li; Pengfei Cao; Yubo Chen; Kang Liu; Jun Zhao
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Omni-Modal Models;Reward Models;Alignment
- Source URL: https://openreview.net/forum?id=9C4gVbPqSy
- PDF URL: https://openreview.net/pdf?id=9C4gVbPqSy

## Abstract

Reward models (RMs) play a critical role in aligning AI behaviors with human preferences, yet they face two fundamental challenges: (1) Modality Imbalance, where most RMs are mainly focused on text and image modalities, offering limited support for video, audio, and other modalities; and (2) Preference Rigidity, where training on fixed binary preference pairs fails to capture the complexity and diversity of personalized preferences. To address the above challenges, we propose Omni-Reward, a step toward generalist omni-modal reward modeling with support for free-form preferences, consisting of: (1) Evaluation: We introduce Omni-RewardBench, the first omni-modal RM benchmark with free-form preferences, covering nine tasks across five modalities including text, image, video, audio, and 3D; (2) Data: We construct Omni-RewardData, a multimodal preference dataset comprising 248K general preference pairs and 69K instruction-tuning pairs for training generalist omni-modal RMs; (3) Model: We propose Omni-RewardModel, which includes both discriminative and generative RMs, and achieves strong performance on Omni-RewardBench as well as other widely used reward modeling benchmarks.

## One-Sentence Claim

Omni-Reward expands reward modeling beyond rigid text/image pairwise preferences to free-form preference evaluation across text, image, video, audio, and 3D tasks.

## Problem

Reward models are central to aligning AI behavior, but current RMs are imbalanced across modalities and often focus on text and image. They also rely heavily on fixed binary preference pairs.

This creates two gaps: limited support for video, audio, 3D, and other modalities, and limited ability to represent personalized or free-form preferences.

## Core Contribution

The paper introduces an omni-modal reward-modeling stack: Omni-RewardBench, Omni-RewardData, and Omni-RewardModel.

Omni-RewardBench covers nine tasks across five modalities with free-form preferences. Omni-RewardData contains 248k general preference pairs and 69k instruction-tuning pairs. Omni-RewardModel includes discriminative and generative reward models.

## Method

The authors define benchmark tasks and free-form preference formats across text, image, video, audio, and 3D. They collect multimodal preference and instruction data to train generalist RMs.

They train both discriminative and generative reward-model variants and evaluate them on Omni-RewardBench and other reward-modeling benchmarks.

## Experiments and Evidence

The abstract reports strong performance on Omni-RewardBench and widely used reward-modeling benchmarks.

The concrete dataset evidence is 248k general preference pairs and 69k instruction-tuning pairs spanning five modalities and nine tasks.

## Limits and Failure Modes

Free-form preferences are harder to normalize and compare than fixed binary choices. Modality coverage may still be uneven, and reward models can inherit annotator or benchmark biases.

Because this note is abstract-only, details still need checking: preference schema, data sources, modality/task balance, annotator protocol, model architecture, and robustness to contradictory personalized preferences.

## Deep Themes

- Generalist reward modeling: alignment signals must span all modalities users interact with.
- Preference expressivity: free-form preferences capture richer values than binary pairwise labels.
- Omni-modal alignment infrastructure: benchmark, data, and model must be co-designed.
- Discriminative and generative reward models: reward modeling itself can be formulated in multiple styles.

## Subthemes

- Text/image/video/audio/3D reward evaluation.
- Free-form preference conditioning.
- Multimodal preference datasets.
- Generalist RM benchmarks.

## Connections to Other Papers

This connects to RACO, FRABench/UFEval, and multimodal evaluation papers through richer preference and criteria modeling.

It also relates to GLANCE, avatar generation, and video/world models because multimodal systems need reward signals that cover visual, audio, embodied, and temporal outputs.

## Notes for Cross-Paper Synthesis

Omni-Reward extends the alignment theme from text-centric preference optimization to generalist multimodal preference modeling.
