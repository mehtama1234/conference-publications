# Adaptive Policy Backbone via Shared Network

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: KhAUoBv0dJ
- Authors: Bumgeun Park; Donghwan Lee
- Primary area: reinforcement_learning
- Keywords: Reinforcement Learning;Deep Reinforcement Learning;Adaptation
- Source URL: https://openreview.net/forum?id=KhAUoBv0dJ
- PDF URL: https://openreview.net/pdf?id=KhAUoBv0dJ

## Abstract

Reinforcement learning (RL) has achieved impressive results across various domains, yet the resulting policies often fail to generalize beyond the specific tasks encountered during training. This lack of robustness limits their deployment in real-world scenarios where diverse and unpredictable task demands exist. In this work, we provide a theoretical analysis of policy networks under Markov Decision Processes (MDPs) and demonstrate that adapting only the linear layers placed before and after a policy backbone is sufficient for task adaptation. Based on this insight, we propose the Adaptive Policy Backbone (APB), which consists of a frozen backbone paired with lightweight, task-specific pre- and post-backbone linear layers. Our results demonstrate that learning only these lightweight task-specific linear layers is sufficient to achieve performance on par with standard RL, even when the backbone is randomly initialized. Furthermore, we find that this structural constraint can enhance the generalization capability of the resulting policies. This advantage extends to out-of-distribution tasks, where representative meta-RL baselines often struggle.

## One-Sentence Claim

Adaptive Policy Backbone shows that adapting lightweight pre- and post-backbone linear layers around a frozen policy backbone can match standard RL while improving task generalization.

## Problem

RL policies often specialize to training tasks and fail under diverse or unpredictable deployment demands, limiting robustness in real-world settings.

## Core Contribution

The paper provides theoretical analysis under MDPs showing that adaptation of only linear layers surrounding a policy backbone can be sufficient, then proposes APB as a lightweight task-adaptation architecture.

## Method

APB freezes a shared backbone and learns task-specific linear layers before and after it. The abstract emphasizes that this can work even when the backbone is randomly initialized, implying the structural constraint itself drives useful adaptation.

## Experiments and Evidence

The abstract reports performance on par with standard RL, improved generalization, and advantages on out-of-distribution tasks where representative meta-RL baselines struggle.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: MDP assumptions, task families, backbone sizes, random-backbone evidence, comparison baselines, and whether linear adapters suffice for high-dimensional robotics.

## Deep Themes

- Task adaptation can be localized around a shared representation.
- Structural constraints may improve RL generalization.
- Lightweight adaptation is useful even outside language-model PEFT.

## Subthemes

- Reinforcement learning.
- Policy backbones.
- Linear adapters.
- Out-of-distribution tasks.
- Meta-RL comparison.
- Robust policy generalization.

## Connections to Other Papers

Connects to Posterior Behavioral Cloning, Nevo-CRL, and LiME through lightweight adaptation and reuse of fixed internal capacity.

## Notes for Cross-Paper Synthesis

APB adds an RL-specific adapter theme: generalization can improve when task-specific learning is constrained to small interfaces around a shared policy core.
