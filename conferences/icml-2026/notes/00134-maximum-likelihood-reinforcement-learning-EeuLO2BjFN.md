# Maximum Likelihood Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: EeuLO2BjFN
- Authors: Fahim Tajwar; Guanning Zeng; Yueer Zhou; Yuda Song; Daman Arora; Yiding Jiang; Jeff Schneider; Ruslan Salakhutdinov; Haiwen Feng; Andrea Zanette
- Primary area: deep_learning->large_language_models
- Keywords: Maximum Likelihood;Reinforcement Learning;Large Language Models;Reasoning;Diversity
- Source URL: https://openreview.net/forum?id=EeuLO2BjFN
- PDF URL: https://openreview.net/pdf?id=EeuLO2BjFN

## Abstract

Reinforcement learning (RL) is the method of choice for training models in setups where the objective function can only be evaluated by sampling from the model. Our key observation is that when the feedback is terminal and binary, models implicitly induce a likelihood over correct rollouts. Maximum likelihood would be the natural framework in such settings, but RL is used instead as a workaround to the non-differentiability. We prove that the standard, expected-reward RL formulation is only a first-order approximation of the likelihood. To remedy this mismatch, we introduce **Maximum Likelihood Reinforcement Learning (MaxRL)**, a compute-indexed family of sample-based objectives that interpolate between expected-reward RL and maximum likelihood as sampling compute is scaled. The resulting objective is a one-line change to standard RL implementations. MaxRL Pareto-dominates existing methods in all tested models and tasks, achieves up to $\mathbf{20\times}$ gains in test-time scaling efficiency over GRPO, and scales more favorably with additional training data and compute.

## One-Sentence Claim

MaxRL treats binary terminal-feedback RL as likelihood maximization over correct rollouts, interpolating between expected-reward RL and maximum likelihood as sampling compute increases.

## Problem

Expected-reward RL is widely used for sample-evaluated objectives, but with terminal binary feedback it is only a first-order approximation to the likelihood of correct rollouts.

## Core Contribution

The paper introduces Maximum Likelihood Reinforcement Learning, a compute-indexed objective family that is a one-line change to standard RL implementations.

## Method

MaxRL adjusts the sample-based RL objective so that increasing sampling compute moves the objective toward maximum likelihood over successful trajectories rather than expected reward alone.

## Experiments and Evidence

The abstract reports Pareto dominance over tested methods, up to 20x gains in test-time scaling efficiency over GRPO, and better scaling with added training data and compute.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: objective formula, binary-feedback assumptions, task suite, diversity effects, and compatibility with dense/graded rewards.

## Deep Themes

- RL objectives for reasoning may be approximating a more natural likelihood target.
- Sampling compute changes the right training objective.
- Binary success feedback can support likelihood-style optimization.

## Subthemes

- Reinforcement learning.
- Maximum likelihood.
- Binary terminal rewards.
- Test-time scaling efficiency.
- GRPO comparison.
- Reasoning diversity.

## Connections to Other Papers

Connects to RGR-GRPO, DR Tulu, TTT-Discover, and reward-modeling papers through rethinking RL objectives for LLM reasoning.

## Notes for Cross-Paper Synthesis

MaxRL adds an objective-mismatch theme: standard RL may be a convenient approximation rather than the best target for binary-success reasoning tasks.
