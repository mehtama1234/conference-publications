# Demystifying Entropy Control in LLM RL Training: Theoretical Analysis and Dynamic Scheduling

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: hq2MPYXAko
- Authors: Jingchu Gai; Guanning Zeng; Huaqing Zhang; Han Zhong; Yige Hong; Andrej Risteski; Aditi Raghunathan
- Primary area: deep_learning->large_language_models
- Keywords: Entropy Control;RL fine-tuning for LLM;Dynamic Scheduling
- Source URL: https://openreview.net/forum?id=hq2MPYXAko
- PDF URL: https://openreview.net/pdf?id=hq2MPYXAko

## Abstract

This paper investigates a pivotal yet debated component of reinforcement learning (RL) for training large language models (LLMs): controlling entropy (increasing or decreasing it) during RL fine-tuning. The existing literature presents a dichotomy: some studies posit that increasing entropy facilitates exploration, whereas others argue that decreasing entropy enhances performance. To reconcile these conflicting observations, we provide a theoretical framework showing that the effect of entropy is governed by \emph{Entropy Discrepancy}, the distributional divergence between positive and negative samples. Guided by this insight, we derive a principled dynamic scheduling method that adaptively modulates the entropy coefficient, effectively switching between entropy maximization and minimization as training evolves. Extensive experiments confirm the correlation between Entropy Discrepancy and the efficacy of entropy control. Furthermore, our adaptive method yields substantial improvements, boosting Pass@K by 6.7\% on AIME24 and 17.52\% on puzzle tasks compared to vanilla RL, while consistently outperforming recent state-of-the-art reasoning methods.

## One-Sentence Claim

Entropy control in LLM RL should switch dynamically between exploration and concentration according to Entropy Discrepancy between positive and negative samples.

## Problem

LLM RL practice is split on entropy: some methods increase entropy to encourage exploration, while others decrease entropy to improve performance and sharpen policies. These observations appear contradictory because the usefulness of entropy control changes over training and task regimes.

The paper asks what statistic determines whether entropy maximization or minimization is beneficial.

## Core Contribution

The paper introduces a theoretical framework centered on Entropy Discrepancy, the distributional divergence between positive and negative samples. It argues that this discrepancy governs whether increasing or decreasing entropy helps.

Guided by this, the authors derive a dynamic entropy-coefficient scheduler that adaptively switches between entropy maximization and minimization as training evolves.

## Method

The method monitors Entropy Discrepancy during RL fine-tuning and uses it to modulate the entropy coefficient. When exploration is useful, the scheduler encourages entropy; when positive and negative distributions separate in a way that favors exploitation, it reduces entropy.

This turns entropy control from a fixed hyperparameter choice into a state-dependent training policy.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical analysis linking entropy-control efficacy to Entropy Discrepancy.
- Empirical confirmation of correlation between Entropy Discrepancy and entropy-control outcomes.
- Adaptive scheduler improves Pass@K by 6.7% on AIME24.
- Adaptive scheduler improves Pass@K by 17.52% on puzzle tasks over vanilla RL.
- Consistent outperformance over recent state-of-the-art reasoning methods.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: Entropy Discrepancy estimator, scheduler formula, RL algorithm, and sensitivity to reward noise.

## Limits and Failure Modes

- Estimating positive/negative distribution divergence may be noisy with small or biased samples.
- Entropy schedules can interact with KL constraints, reward scaling, and sampling temperature.
- Pass@K gains may not translate to calibrated single-answer reliability.
- The theory may depend on simplifications not fully matching LLM RL dynamics.

## Deep Themes

**Exploration is phase-dependent.** Entropy is not intrinsically good or bad; its effect depends on training state.

**RL hyperparameters are becoming adaptive diagnostics.** The scheduler responds to measured distributional structure.

**Positive-negative contrast drives policy shaping.** Useful entropy control depends on how successful and failed trajectories separate.

## Subthemes

- Entropy Discrepancy.
- Dynamic entropy scheduling.
- LLM RL fine-tuning.
- Exploration-exploitation switching.
- Reasoning-task Pass@K improvement.

## Connections to Other Papers

Connects to Critique-GRPO, RePO, Hista/Numca, T2PO, and PRISM. It belongs to the LLM RL control cluster, where training improves by diagnosing the internal state of the optimization process.

## Notes for Cross-Paper Synthesis

This paper adds a control-theoretic view of RL fine-tuning: rather than picking static coefficients, training should respond to how reward-labeled distributions evolve.
