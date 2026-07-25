# LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lwOoBzJykL
- Authors: Zhuoyang Liu; Jiaming Liu; Hao Chen; Jiale Yu; Ziyu Guo; Chengkai Hou; Chenyang Gu; Xiangju Mi; Renrui Zhang; Kun Wu; Zhengping Che; Jian Tang; Pheng-Ann Heng; Shanghang Zhang
- Primary area: applications->robotics
- Keywords: Vision-language-action Model;Robotic manipulation;Latent Chain-of-Thought
- Source URL: https://openreview.net/forum?id=lwOoBzJykL
- PDF URL: https://openreview.net/pdf?id=lwOoBzJykL

## Abstract

Vision-Language-Action (VLA) models have recently shown strong generalization, with some approaches seeking to explicitly generate linguistic reasoning traces or predict future observations prior to execution. However, explicit reasoning typically incurs non-negligible inference latency, which constrains the temporal resolution required for robotic manipulation. Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable physical attributes. To mitigate these limitations, we propose LaST$_0$, a framework that enables efficient reasoning before acting through a Latent Spatio-Temporal Chain-of-Thought (CoT), capturing fine-grained physical and robotic dynamics that are often difficult to verbalize. Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations across time to enable temporally consistent implicit reasoning trajectories. Furthermore, LaST$_0$ adopts a dual-system architecture implemented via a Mixture-of-Transformers design, where a reasoning expert conducts low-frequency latent inference and an acting expert generates high-frequency actions conditioned on robotics-oriented latent representations. To facilitate coordination, LaST$_0$ is trained with heterogeneous operation frequencies, enabling adaptive switching during deployment. Across 10 real-world tasks spanning tabletop, mobile, and dexterous hand manipulation, LaST$_0$ improves mean success rates by 13%, 14% and 14% over prior SOTA VLA methods, respectively.

## One-Sentence Claim

LaST0 improves robotic VLA models by replacing slow linguistic reasoning traces with latent spatio-temporal reasoning over future visual dynamics, 3D structure, and proprioception.

## Problem

Robotic manipulation needs high-frequency action generation, but explicit linguistic reasoning adds latency and can bottleneck physical attributes that are difficult to verbalize. Predicting future observations helps, but reasoning only in text is poorly matched to fine-grained robot dynamics.

The paper asks how VLA models can reason before acting without sacrificing temporal resolution.

## Core Contribution

LaST0 introduces a Latent Spatio-Temporal Chain-of-Thought space for implicit robotic reasoning. It captures future visual dynamics, 3D structural information, and robot proprioceptive states across time.

It uses a dual-system Mixture-of-Transformers architecture: a low-frequency reasoning expert performs latent inference, while a high-frequency acting expert generates actions conditioned on robotics-oriented latent representations.

## Method

The model learns token-efficient latent reasoning trajectories that extend over time. It is trained with heterogeneous operation frequencies so the reasoning and acting experts can coordinate and switch adaptively during deployment.

This separates slow deliberation over latent dynamics from fast motor control.

## Experiments and Evidence

Evidence reported in the abstract:

- 10 real-world robotic tasks.
- Domains include tabletop, mobile, and dexterous hand manipulation.
- Mean success improvements of 13%, 14%, and 14% over prior SOTA VLA methods across those settings.
- Latent CoT over visual dynamics, 3D structure, and proprioception.
- Mixture-of-Transformers dual-system architecture.
- Heterogeneous operation-frequency training.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: robot platforms, task suite, latency measurements, and ablations.

## Limits and Failure Modes

- Latent reasoning is harder to inspect than language traces.
- Dual-frequency coordination may fail under sudden environment changes.
- Real-world gains may depend on task distribution and sensor quality.
- Learned latent dynamics can encode biases or errors not visible to operators.

## Deep Themes

**Robotic reasoning should be physical, not only linguistic.** Some manipulation-relevant attributes are better represented in latent spatio-temporal state.

**Deliberation and action need different clocks.** Low-frequency reasoning can guide high-frequency control.

**Implicit CoT trades interpretability for latency and embodiment.** The method optimizes for robotic timing constraints.

## Subthemes

- Latent spatio-temporal CoT.
- Vision-language-action models.
- Mixture-of-Transformers dual system.
- Heterogeneous frequency training.
- Real-world manipulation.

## Connections to Other Papers

Connects to EcoVLA, PACT, NeuronCtrl, LASER, and MoCA. It also contrasts with PLAINTAIN: one makes reasoning visible for user feedback, the other keeps reasoning latent for real-time control.

## Notes for Cross-Paper Synthesis

LaST0 adds a timing-aware embodiment theme: reasoning format should match the action domain's latency and observability constraints.
