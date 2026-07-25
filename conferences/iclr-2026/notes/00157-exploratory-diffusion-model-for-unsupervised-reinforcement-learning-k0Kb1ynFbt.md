# Exploratory Diffusion Model for Unsupervised Reinforcement Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: k0Kb1ynFbt
- Authors: Chengyang Ying; Huayu Chen; Xinning Zhou; Zhongkai Hao; Hang Su; Jun Zhu
- Primary area: reinforcement learning
- Keywords: reinforcement learning;diffusion policy;unsupervised reinforcement learning;exploration
- Source URL: https://openreview.net/forum?id=k0Kb1ynFbt
- PDF URL: https://openreview.net/pdf?id=k0Kb1ynFbt

## Abstract

Unsupervised reinforcement learning (URL) pre-trains agents by exploring diverse states in reward-free environments, aiming to enable efficient adaptation to various downstream tasks. Without extrinsic rewards, prior methods rely on intrinsic objectives, but heterogeneous exploration data demand strong modeling capacity for both intrinsic reward design and policy learning. We introduce the **Ex**ploratory **D**iffusion **M**odel (**ExDM**), which leverages the expressive power of diffusion models to fit diverse replay-buffer distributions, thus providing accurate density estimates and a score-based intrinsic reward that drives exploration into under-visited regions. This mechanism substantially broadens state coverage and yields robust pre-trained policies. Beyond exploration, ExDM offers theoretical guarantees and practical algorithms for fine-tuning diffusion policies under limited interactions, overcoming instability and computational overhead from multi-step sampling. Extensive experiments on Maze2d and URLB show that ExDM achieves superior exploration and faster downstream adaptation, establishing new state-of-the-art results, particularly in environments with complex structure or cross-embodiment settings.

## One-Sentence Claim

ExDM uses diffusion density modeling of replay buffers to produce score-based intrinsic rewards and diffusion-policy fine-tuning procedures that improve unsupervised exploration and downstream adaptation.

## Problem

Unsupervised RL must explore reward-free environments broadly enough to support later task adaptation. Prior intrinsic-reward and policy-learning methods struggle when replay data are heterogeneous and environments have complex structure, because they need both accurate density estimation and expressive policies.

## Core Contribution

The paper introduces the Exploratory Diffusion Model, which fits diverse replay-buffer distributions with diffusion models, turns density/score information into an intrinsic reward for under-visited regions, and provides theory plus practical algorithms for limited-interaction fine-tuning of diffusion policies.

## Method

ExDM trains a diffusion model on replay-buffer states or trajectories to estimate distributional structure. A score-based intrinsic reward pushes exploration toward low-density regions, broadening state coverage. For downstream use, the method fine-tunes diffusion policies while addressing instability and overhead from multi-step diffusion sampling.

## Experiments and Evidence

Experiments on Maze2d and URLB reportedly show stronger exploration, faster downstream adaptation, and state-of-the-art results, especially in complex-structure and cross-embodiment settings.

## Limits and Failure Modes

Diffusion modeling can be computationally expensive, and exploration quality may depend on replay-buffer diversity, state representation, and density-estimation calibration. The abstract does not specify how score rewards avoid novelty traps or how sampling overhead is reduced in each setting. Full-text review should check ablations against count-based, contrastive, and skill-discovery URL baselines.

## Deep Themes

- Generative models as exploration engines.
- Density estimation as an intrinsic reward primitive.
- Diffusion policies moving from generation into control.
- Unsupervised pretraining for fast downstream adaptation.

## Subthemes

- Score-based novelty rewards.
- Replay-buffer distribution modeling.
- Diffusion-policy fine-tuning under limited interaction.
- Cross-embodiment unsupervised RL.
- Exploration in structured environments.

## Connections to Other Papers

Connects to mean-flow and diffusion action-generation papers through generative policies for control, to offline reward/policy-search work through decision generation beyond static data, and to broader test-time/process optimization themes where learned generative models provide search or exploration structure.

## Notes for Cross-Paper Synthesis

ExDM turns generative modeling into a control prior: the model is useful because it estimates where the agent has been and how to move beyond that support. It fits the larger pattern of using distribution models to guide search, exploration, or policy improvement.
