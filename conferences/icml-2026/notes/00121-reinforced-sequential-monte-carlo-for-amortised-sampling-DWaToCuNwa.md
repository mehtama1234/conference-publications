# Reinforced Sequential Monte Carlo for Amortised Sampling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: DWaToCuNwa
- Authors: Sanghyeok Choi; Sarthak Mittal; Víctor Elvira; Jinkyoo Park; Esmeralda S. Whitammer
- Primary area: probabilistic_methods->monte_carlo_and_sampling_methods
- Keywords: Amortised samplers;diffusion samplers;sequential Monte Carlo;entropy-regularised RL;GFlowNets
- Source URL: https://openreview.net/forum?id=DWaToCuNwa
- PDF URL: https://openreview.net/pdf?id=DWaToCuNwa

## Abstract

This paper proposes a synergy of amortised and particle-based methods for sampling from distributions defined by unnormalised density functions. We state a connection between sequential Monte Carlo (SMC) and neural sequential samplers trained by maximum-entropy reinforcement learning (MaxEnt RL), wherein learnt sampling policies and value functions define proposal kernels and twist functions. Exploiting this connection, we introduce an off-policy RL training procedure for the sampler that uses samples from SMC -- using the learnt sampler as a proposal -- as a behaviour policy that better explores the target distribution. We describe techniques for stable joint training of proposals and twist functions and an adaptive weight tempering scheme to reduce training signal variance. Furthermore, building upon past attempts to use experience replay to guide the training of neural samplers, we derive a way to combine historical samples with annealed importance sampling weights within a replay buffer. On synthetic multi-modal targets (in both continuous and discrete spaces) and the Boltzmann distribution of alanine dipeptide conformations, we demonstrate improvements in approximating the true distribution as well as training stability compared to both amortised and Monte Carlo methods.

## One-Sentence Claim

Reinforced SMC combines neural amortized samplers with particle-based sequential Monte Carlo by training proposal and twist functions through off-policy maximum-entropy RL.

## Problem

Amortized samplers can be efficient but poorly explore difficult unnormalized targets, while Monte Carlo methods can be robust but expensive and less reusable across samples.

## Core Contribution

The paper connects SMC with MaxEnt RL-trained neural sequential samplers, then uses SMC samples as behavior-policy data for improving amortized sampling.

## Method

Learned sampling policies define proposal kernels and learned value functions define twist functions. The method trains proposals and twists jointly, uses adaptive weight tempering to reduce variance, and combines replay-buffer historical samples with annealed importance weights.

## Experiments and Evidence

The abstract reports improved target-distribution approximation and training stability on synthetic multimodal continuous/discrete targets and Boltzmann sampling for alanine dipeptide conformations.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: variance-control ablations, replay buffer bias, target classes, scaling behavior, and comparison to diffusion samplers/GFlowNets.

## Deep Themes

- Sampling can blend amortized policies with particle correction.
- RL and SMC are converging as tools for unnormalized distributions.
- Replay and tempering can stabilize neural samplers.

## Subthemes

- Sequential Monte Carlo.
- Amortized sampling.
- MaxEnt RL.
- Twist functions.
- Annealed importance sampling.
- Boltzmann distributions.

## Connections to Other Papers

Connects to Autoregressive Boltzmann Generators, Rex, and scientific sampling papers through probabilistic inference for physical distributions.

## Notes for Cross-Paper Synthesis

This paper reinforces the sampler-infrastructure theme: generative and scientific models increasingly depend on hybrid learned/classical sampling machinery.
