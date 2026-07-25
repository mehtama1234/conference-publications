# Optimistic Task Inference for Behavior Foundation Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: m5byThUSNE
- Authors: Thomas Rupf; Marco Bagatella; Marin Vlastelica; Andreas Krause
- Primary area: reinforcement learning
- Keywords: Behavior Foundation Models;Zero-Shot Reinforcement Learning;Deep Reinforcement Learning;Fast Adaptation
- Source URL: https://openreview.net/forum?id=m5byThUSNE
- PDF URL: https://openreview.net/pdf?id=m5byThUSNE

## Abstract

Behavior Foundation Models (BFMs) are capable of retrieving high-performing policy for any reward function specified directly at test-time, commonly referred to as zero-shot reinforcement learning (RL). While this is a very efficient process in terms of compute, it can be less so in terms of data: as a standard assumption, BFMs require computing rewards over a non-negligible inference dataset, assuming either access to a functional form of rewards, or significant labeling efforts. To alleviate these limitations, we tackle the problem of task inference purely through interaction with the environment at test-time. We propose OpTI-BFM, an optimistic decision criterion that directly models uncertainty over reward functions and guides BFMs in data collection for task inference. Formally, we provide a regret bound for well- trained BFMs through a direct connection to upper-confidence algorithms for linear bandits. Empirically, we evaluate OpTI-BFM on established zero-shot benchmarks, and observe that it enables successor-features-based BFMs to identify and optimize an unseen reward function in a handful of episodes with minimal compute overhead.

## One-Sentence Claim

OpTI-BFM lets behavior foundation models infer unseen reward tasks through a handful of test-time environment interactions by using optimistic uncertainty-aware data collection.

## Problem

Behavior foundation models can retrieve policies for test-time reward functions, but standard zero-shot RL assumptions often require evaluating rewards over a sizable inference dataset or collecting substantial labels. That makes the approach data-inefficient when the reward is unknown, costly, or only discoverable through interaction.

## Core Contribution

The paper proposes OpTI-BFM, an optimistic task-inference criterion that models uncertainty over reward functions and chooses environment interactions that help identify the task. It connects well-trained BFMs to upper-confidence algorithms for linear bandits and provides a regret bound.

## Method

OpTI-BFM treats task inference as active data collection at test time. Instead of assuming full reward access over a dataset, it maintains reward-function uncertainty, uses optimism to guide episodes, and plugs the inferred task into successor-features-based BFMs for policy optimization.

## Experiments and Evidence

On established zero-shot RL benchmarks, the abstract reports that OpTI-BFM identifies and optimizes unseen reward functions in a handful of episodes with minimal compute overhead. The theoretical evidence is a regret bound derived through the connection to linear-bandit upper-confidence methods.

## Limits and Failure Modes

The guarantees likely depend on BFM quality, reward linearity or successor-feature assumptions, and calibrated uncertainty. Exploration could be unsafe or inefficient in real systems if task uncertainty is misspecified. Full-text review should check reward model class, episode budget, benchmark domains, comparison to passive task inference, and failure under sparse or deceptive rewards.

## Deep Themes

- Test-time task inference for foundation policies.
- Optimism under reward uncertainty.
- Data-efficient zero-shot RL.
- Bandit theory for behavior foundation models.

## Subthemes

- Successor-feature BFMs.
- Active reward identification.
- Upper-confidence decision criteria.
- Few-episode adaptation.
- Compute-light but data-aware test-time control.

## Connections to Other Papers

Connects to ExDM and AIGB-Pearl through decision-making with limited or offline feedback, to ranking-feedback learning through weak reward information, and to adaptation/control papers where test-time interaction replaces large supervised inference sets.

## Notes for Cross-Paper Synthesis

OpTI-BFM sharpens the distinction between compute-efficient and data-efficient adaptation. Foundation behavior models are only practically zero-shot if the task can be inferred cheaply from interaction.
