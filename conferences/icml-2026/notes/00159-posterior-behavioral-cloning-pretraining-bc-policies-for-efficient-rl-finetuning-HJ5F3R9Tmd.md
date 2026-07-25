# Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: HJ5F3R9Tmd
- Authors: Andrew Wagenmaker; Perry Dong; Raymond Tsao; Chelsea Finn; Sergey Levine
- Primary area: reinforcement_learning
- Keywords: reinforcement learning;finetuning;pretraining;behavioral cloning
- Source URL: https://openreview.net/forum?id=HJ5F3R9Tmd
- PDF URL: https://openreview.net/pdf?id=HJ5F3R9Tmd

## Abstract

Standard practice across domains from robotics to language is to first pretrain a policy on a large-scale demonstration dataset, and then finetune this policy, typically with reinforcement learning (RL), in order to improve performance on deployment domains. This finetuning step has proved critical in achieving human or super-human performance, yet while much attention has been given to developing more effective finetuning algorithms, little attention has been given to ensuring the pretrained policy is an effective initialization for RL finetuning. In this work we seek to understand how the pretrained policy affects finetuning performance, and how to pretrain policies in order to ensure they are effective initializations for finetuning. We first show theoretically that standard behavioral cloning (BC) can fail to ensure coverage over the demonstrator's actions, a minimal condition necessary for effective RL finetuning. We then show that if, instead of exactly fitting the observed demonstrations, we train a policy to model the posterior distribution of the demonstrator's behavior given the demonstration dataset, we do obtain a policy that ensures coverage over the demonstrator's actions, enabling more effective finetuning. Furthermore, this policy achieves this while ensuring pretrained performance is no worse than that of the BC policy. We then show this approach is practically implementable with modern generative models and leads to significantly improved RL finetuning performance on both realistic robotic control benchmarks and real-world robotic manipulation tasks, as compared to standard behavioral cloning.

## One-Sentence Claim

Posterior Behavioral Cloning pretrains policies to cover the demonstrator's plausible action distribution, yielding better initializations for subsequent RL finetuning than standard BC.

## Problem

Policy pretraining is commonly optimized for imitation performance, but a policy that fits demonstrations too narrowly may lack action coverage needed for efficient RL improvement.

## Core Contribution

The paper identifies action-coverage as a missing criterion for BC pretraining and proposes modeling the posterior over demonstrator behavior as a way to preserve finetuning potential without sacrificing pretrained performance.

## Method

The authors prove that standard behavioral cloning can fail to cover demonstrator actions, then train a policy to model the posterior distribution of demonstrator behavior given the dataset. They implement this posterior policy with modern generative models before RL finetuning.

## Experiments and Evidence

The abstract reports theoretical coverage guarantees, no worse pretrained performance than BC, and significantly improved RL finetuning on realistic robotic control benchmarks and real-world robotic manipulation tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: posterior approximation method, demonstrator assumptions, RL algorithms used for finetuning, compute cost, benchmark diversity, and robustness to low-quality or multi-modal demonstrations.

## Deep Themes

- Pretraining objectives should optimize downstream adaptability, not only immediate imitation.
- Coverage and uncertainty are central to policy improvement.
- Generative modeling can preserve behavioral diversity for control.

## Subthemes

- Behavioral cloning.
- RL finetuning.
- Demonstration coverage.
- Posterior modeling.
- Robot manipulation.
- Offline-to-online policy improvement.

## Connections to Other Papers

Connects to VOTP and SOAR through feedback-efficient RL and curriculum/coverage design. It also parallels data-selection papers where the value of training data or pretraining behavior depends on downstream optimization dynamics.

## Notes for Cross-Paper Synthesis

This paper sharpens the corpus's pretraining-to-adaptation theme: the best initial model may be one that preserves useful uncertainty and option coverage, not one that collapses onto the highest-likelihood behavior.
