# EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7kH5uphAes
- Authors: Yuting Huang; Leilei Ding; Zhipeng Tang; Zenghuan Zhu; Jiajun Deng; Xinrui Lin; Shuo Liu; Haojie Ren; Jianmin Ji; Yanyong Zhang
- Primary area: applications->robotics
- Keywords: Efficient VLA;Efficient LLM;Dynamic Pruning
- Source URL: https://openreview.net/forum?id=7kH5uphAes
- PDF URL: https://openreview.net/pdf?id=7kH5uphAes

## Abstract

While Vision-Language-Action (VLA) models hold promise in embodied intelligence, their large parameter counts lead to substantial inference latency that hinders real-time manipulation, motivating parameter sparsification. However, as the environment evolves during VLA execution, the optimal sparsity patterns change accordingly. Static pruning lacks the adaptability required for environment dynamics, whereas fixed-interval dynamic layer pruning suffers from coarse granularity and high retraining overheads. To bridge this gap, we propose **EcoVLA**, a training-free, plug-and-play adaptive pruning framework that supports orthogonal combination with existing VLA acceleration methods. EcoVLA comprises two components: **E**nvironment-aware **A**daptive **P**runing (**EAP**) and **I**nterleaved **I**nference **O**rchestration (**$I^2O$**). EAP is a lightweight adaptive channel pruning method that incorporates the temporal consistency of the physical environment to update sparsity patterns. $I^2O$ leverages the FLOPs bubbles inherent in VLA inference to schedule the pruning method in parallel, ensuring negligible impact on latency. Evaluated on diverse VLA models and benchmarks, EcoVLA delivers state-of-the-art performance, achieving up to 1.60$\times$ speedup with only a 0.4% drop in success rate, and further reaches 2.18$\times$ speedup with only a 0.5% degradation when combined with token pruning. We further validate the effectiveness of EcoVLA on real-world robots. Our code is available [here](https://github.com/Echo-hyt/Ecovla).

## One-Sentence Claim

EcoVLA speeds up VLA inference by adapting pruning patterns to the evolving environment and scheduling pruning work inside inference FLOP bubbles.

## Problem

VLA models are too slow for real-time manipulation, but static pruning cannot adapt to changing embodied environments and fixed-interval dynamic pruning is coarse and retraining-heavy.

## Core Contribution

The paper proposes EcoVLA, a training-free plug-and-play adaptive pruning framework combining Environment-aware Adaptive Pruning and Interleaved Inference Orchestration.

## Method

EAP updates channel sparsity patterns using temporal consistency in the physical environment. I2O schedules pruning in parallel with existing VLA inference bubbles so adaptive pruning adds negligible latency overhead.

## Experiments and Evidence

The abstract reports up to 1.60x speedup with 0.4% success-rate drop, and 2.18x speedup with 0.5% degradation when combined with token pruning, plus validation on real-world robots.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: how environment consistency is measured, supported VLA backbones, real-robot task diversity, and interaction with other acceleration methods.

## Deep Themes

- Embodied efficiency must adapt to changing environments.
- Training-free acceleration is valuable for deployable robot policies.
- Inference scheduling can exploit idle compute structure, not only reduce model size.

## Subthemes

- Efficient VLA inference.
- Adaptive channel pruning.
- Environment-aware sparsity.
- Inference orchestration.
- Real-time robotic manipulation.
- Token-pruning composition.

## Connections to Other Papers

Connects to SCALE, BehaviorVLA, and HDFlow through deployable embodied control. It also links to LiftQuant and low-precision papers as efficiency work that is constrained by real runtime behavior.

## Notes for Cross-Paper Synthesis

EcoVLA adds an embodied-efficiency theme: robot-model compression cannot be static because perception/action context changes during execution.
