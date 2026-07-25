# TD-JEPA: Latent-predictive Representations for Zero-Shot Reinforcement Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: SzXDuBN8M1
- Authors: Marco Bagatella; Matteo Pirotta; Ahmed Touati; Alessandro Lazaric; Andrea Tirinzoni
- Primary area: reinforcement learning
- Keywords: zero-shot reinforcement learning;unsupervised reinforcement learning;self-predictive representations;joint embedding predictive architecture
- Source URL: https://openreview.net/forum?id=SzXDuBN8M1
- PDF URL: https://openreview.net/pdf?id=SzXDuBN8M1

## Abstract

Latent prediction–where agents learn by predicting their own latents–has emerged as a powerful paradigm for training general representations in machine learning. In reinforcement learning (RL), this approach has been explored to define auxiliary losses for a variety of settings, including reward-based and unsupervised RL, behavior cloning, and world modeling. While existing methods are typically limited to single-task learning, one-step prediction, or on-policy trajectory data, we show that temporal difference (TD) learning enables learning representations predictive of long-term latent dynamics across multiple policies from offline, reward-free transitions. Building on this, we introduce TD-JEPA, which leverages TD-based latent-predictive representations into unsupervised RL. TD-JEPA trains explicit state and task encoders, a policy-conditioned multi-step predictor, and a set of parameterized policies directly in latent space. This enables zero-shot optimization of any reward function at test time. Theoretically, we show that an idealized variant of TD-JEPA avoids collapse with proper initialization, and learns encoders that capture a low-rank factorization of long-term policy dynamics, while the predictor recovers their successor features in latent space. Empirically, TD-JEPA matches or outperforms state-of-the-art baselines on locomotion, navigation, and manipulation tasks across 13 datasets in ExoRL and OGBench, especially in the challenging setting of zero-shot RL from pixels.

## One-Sentence Claim

TD-JEPA learns reward-free multi-policy latent dynamics with temporal-difference prediction, enabling zero-shot optimization of arbitrary test-time rewards.

## Problem

Latent prediction is useful for representation learning, but RL variants are often tied to single tasks, one-step prediction, on-policy data, or specific reward functions.

Zero-shot RL needs representations that capture long-term dynamics across policies from offline transitions, before the test-time reward is known.

## Core Contribution

The paper introduces TD-JEPA, which brings TD-based latent-predictive representations into unsupervised RL.

It trains state and task encoders, a policy-conditioned multi-step predictor, and parameterized policies directly in latent space, supporting zero-shot reward optimization.

## Method

TD-JEPA uses temporal-difference learning to predict long-term latent dynamics across multiple policies from offline, reward-free data.

The idealized theory shows that with proper initialization, the method avoids collapse, learns a low-rank factorization of long-term policy dynamics, and recovers successor features in latent space.

## Experiments and Evidence

The abstract reports experiments on locomotion, navigation, and manipulation across 13 datasets in ExoRL and OGBench.

TD-JEPA matches or outperforms state-of-the-art baselines, especially for zero-shot RL from pixels.

## Limits and Failure Modes

Zero-shot reward optimization depends on whether offline transitions cover policies relevant to future rewards. Latent collapse, distribution shift, and reward functions requiring unobserved behaviors remain risks.

Because this note is abstract-only, details still need checking: encoder architecture, policy parameterization, TD objective, initialization condition, datasets, reward evaluation protocol, and pixel-based ablations.

## Deep Themes

- Reward-free representation learning for control: agents learn dynamics before knowing the task.
- Long-term latent prediction: TD learning extends JEPA-style prediction beyond one-step objectives.
- Successor features in latent space: representation theory connects predictive latents to classical RL structure.
- Zero-shot RL from pixels: visual control benefits from policy-conditioned predictive representations.

## Subthemes

- Temporal-difference JEPA.
- Unsupervised RL.
- Successor features.
- Offline reward-free transitions.

## Connections to Other Papers

This connects to GLANCE, Linear Recurrent Memory, MSP, and other representation-for-control papers.

It also relates to Koopman representation work because both learn latent dynamics that support downstream prediction or control.

## Notes for Cross-Paper Synthesis

TD-JEPA reinforces the latent-dynamics theme: reusable control capability comes from representing long-term dynamics, not just immediate observations.
