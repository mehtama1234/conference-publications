# Distributional Inverse Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ZcnZ6vs4yX
- Authors: Feiyang Wu; Ye Zhao; Anqi Wu
- Primary area: reinforcement_learning->inverse
- Keywords: Inverse Reinforcement Learning;Neuroscience;Distributional Reinforcement Learning;Risk aware policy optimization;Behavior Analysis;Robotics
- Source URL: https://openreview.net/forum?id=ZcnZ6vs4yX
- PDF URL: https://openreview.net/pdf?id=ZcnZ6vs4yX

## Abstract

We propose a distributional framework for offline Inverse Reinforcement Learning (IRL) that jointly models uncertainty over reward functions and full distributions of returns. Unlike conventional IRL approaches that recover a deterministic reward estimate or match only expected returns, our method captures richer structure in expert behavior, particularly in learning the reward distribution, by minimizing first-order stochastic dominance (FSD) violations and thus integrating distortion risk measures (DRMs) into policy learning, enabling the recovery of both reward distributions and distribution-aware policies. This formulation is well-suited for behavior analysis and risk-aware imitation learning. Theoretical analysis show that the algorithm converge with $\mathcal{O}(\varepsilon^{-2})$ iteration complexity. Empirical results on synthetic benchmarks, real-world neurobehavioral data, and MuJoCo control tasks demonstrate that our method recovers expressive reward representations and achieves state-of-the-art imitation performance.

## One-Sentence Claim

Distributional IRL recovers reward distributions and risk-aware policies by matching full return distributions and minimizing first-order stochastic-dominance violations.

## Problem

Conventional inverse reinforcement learning often estimates a deterministic reward or matches expected returns. Expert behavior, however, can reflect uncertainty, risk sensitivity, and richer reward variability that expected-value matching hides.

The paper asks how offline IRL can model uncertainty over rewards and full return distributions for behavior analysis and risk-aware imitation.

## Core Contribution

The paper proposes a distributional offline IRL framework that jointly models uncertainty over reward functions and return distributions. It minimizes first-order stochastic dominance violations and integrates distortion risk measures into policy learning.

The method recovers both reward distributions and distribution-aware policies, with theoretical convergence at O(epsilon^-2) iteration complexity and strong empirical imitation performance.

## Method

The method estimates distributions rather than point rewards. FSD-violation minimization constrains learned policies/rewards so the induced return distributions respect expert preferences under stochastic dominance. Distortion risk measures then shape policy optimization according to risk attitudes.

This makes IRL suitable for behavior where the expert's objective is not captured by mean return alone.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical convergence with O(epsilon^-2) iteration complexity.
- Synthetic benchmark results.
- Real-world neurobehavioral data.
- MuJoCo control tasks.
- Expressive reward-representation recovery.
- State-of-the-art imitation performance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: offline dataset assumptions, reward-distribution parameterization, DRM choices, and neurobehavioral task details.

## Limits and Failure Modes

- Full return-distribution estimation may require more data than expected-return IRL.
- Offline IRL remains vulnerable to support mismatch.
- Risk measures must match the expert population; misspecified risk can distort imitation.
- Identifiability of reward distributions may be limited.

## Deep Themes

**Expert behavior is distributional.** Mean rewards can miss uncertainty and risk preferences.

**Risk sensitivity belongs inside imitation learning.** DRMs make recovered policies reflect more than average performance.

**Behavior analysis needs expressive reward models.** Neurobehavioral applications motivate richer latent objectives.

## Subthemes

- Offline distributional IRL.
- Reward-function uncertainty.
- Return-distribution matching.
- First-order stochastic dominance.
- Distortion risk measures.

## Connections to Other Papers

Connects to TimeRewarder, BFTS, R2VPO, PAVE, and risk-aware decision papers such as ROCP and TRECA. It also links to neuroscience papers through behavior analysis under latent reward uncertainty.

## Notes for Cross-Paper Synthesis

Distributional IRL expands the risk theme into imitation: the target is not only what experts do, but what distributional preferences and uncertainties their behavior reveals.
