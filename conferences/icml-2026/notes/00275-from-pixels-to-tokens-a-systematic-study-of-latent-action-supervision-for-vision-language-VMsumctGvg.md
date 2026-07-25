# From Pixels to Tokens: A Systematic Study of Latent Action Supervision for Vision-Language-Action Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: VMsumctGvg
- Authors: Yihan Lin; Haoyang Li; Yang Li; Haitao Shen; Yihan Zhao; Chao Shao; Jing Zhang
- Primary area: applications->robotics
- Keywords: Vision-Language-Action (VLA);Latent Actions;Robot Manipulation
- Source URL: https://openreview.net/forum?id=VMsumctGvg
- PDF URL: https://openreview.net/pdf?id=VMsumctGvg

## Abstract

Latent actions serve as an intermediate representation that enables consistent modeling of vision-language-action (VLA) models across heterogeneous datasets. However, approaches to supervising VLAs with latent actions are fragmented and lack a systematic comparison. This work structures the study of latent action supervision from two perspectives: (i) regularizing the trajectory via image-based latent actions, and (ii) unifying the target space with action-based latent actions. Under a unified VLA baseline, we instantiate and compare four representative integration strategies. Our results reveal a formulation-task correspondence: image-based latent actions benefit long-horizon reasoning, whereas action-based latent actions excel at complex motor coordination. Furthermore, we find that directly supervising the VLM with discrete latent action tokens yields the most effective performance. Finally, our experiments offer initial insights into the benefits of latent action supervision in mixed-data, suggesting a promising direction for VLA training.

## One-Sentence Claim

Latent action supervision improves VLA training, with image-based latent actions helping long-horizon reasoning and discrete action-token supervision best unifying heterogeneous robot-control data.

## Problem

Vision-language-action models are trained across heterogeneous robotic datasets with different action spaces, observations, and task structures. Latent actions can provide an intermediate representation, but existing supervision strategies are fragmented and not systematically compared.

The paper asks how latent action supervision should be integrated into VLAs and which formulations help which kinds of robotic tasks.

## Core Contribution

The paper structures latent action supervision along two axes:

- Image-based latent actions regularize trajectories.
- Action-based latent actions unify the target action space.

Under a unified VLA baseline, it instantiates and compares four integration strategies. It finds a formulation-task correspondence: image-based latent actions benefit long-horizon reasoning, action-based latent actions help complex motor coordination, and directly supervising the VLM with discrete latent action tokens gives the strongest performance.

## Method

The method is a systematic comparison rather than a single new architecture. The authors build a unified VLA baseline and vary how latent actions are derived and injected into training.

Discrete latent action tokens turn action supervision into a language-model-like target, letting the VLM model action abstractions with the same token machinery used for text.

## Experiments and Evidence

Evidence reported in the abstract:

- Four representative latent-action integration strategies compared under one baseline.
- Image-based latent actions improve long-horizon reasoning.
- Action-based latent actions improve complex motor coordination.
- Direct supervision with discrete latent action tokens is most effective overall.
- Mixed-data experiments suggest latent action supervision helps heterogeneous VLA training.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: robot benchmarks, latent-action tokenizer, baseline architecture, dataset mixture, and metrics for reasoning versus coordination.

## Limits and Failure Modes

- Discrete latent actions can bottleneck fine motor control if tokenization is too coarse.
- Task-formulation correspondence may depend on benchmark selection.
- Mixed-data benefits may require careful balancing across robot embodiments and domains.
- Latent actions are only useful if they remain grounded in executable control.

## Deep Themes

**Robotic control needs intermediate action languages.** Latent tokens provide a shared representation between pixels, language, and heterogeneous low-level actions.

**Different tasks prefer different abstractions.** Long-horizon reasoning and motor coordination do not benefit equally from the same latent-action formulation.

**Tokenization is expanding beyond text.** VLA models increasingly treat actions as discrete symbols inside multimodal sequence modeling.

## Subthemes

- Image-based versus action-based latent actions.
- Discrete latent action tokens.
- Mixed-data VLA training.
- Long-horizon reasoning versus motor coordination.
- Unified action target spaces.

## Connections to Other Papers

Connects to EcoVLA, DLMR, LatentLM, and multimodal latent-interface papers. It also links to behavioral cloning for scientific annotation because both study process/action trajectories as supervision rather than only final outputs.

## Notes for Cross-Paper Synthesis

This paper extends the latent-interface theme into robotics: actions become tokens, trajectory structure becomes supervision, and heterogeneous datasets are unified through learned intermediate control vocabularies.
