# BFTS: Thompson Sampling with Bayesian Additive Regression Trees

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Z1nbtKcLQk
- Authors: Ruizhe Deng; Bibhas Chakraborty; Ran Chen; Yan Shuo Tan
- Primary area: general_machine_learning->online_learning_active_learning_and_bandits
- Keywords: Contextual bandits;Thompson sampling;Bayesian additive regression trees (BART);tabular data;Bayesian regret bounds
- Source URL: https://openreview.net/forum?id=Z1nbtKcLQk
- PDF URL: https://openreview.net/pdf?id=Z1nbtKcLQk

## Abstract

We propose Bayesian Forest Thompson Sampling (BFTS), which performs Thompson sampling using arm-wise Bayesian Additive Regression Trees (BART) to model each action's mean reward and generate MCMC-based posterior draws for decision-making. We derive an information-theoretic Bayesian regret bound of order $\widetilde{\mathcal O}(K\sqrt{T})$ for ideal posterior sampling under a correctly specified Bayesian design. Empirically, BFTS achieves competitive regret on nonlinear synthetic benchmarks with near-nominal uncertainty calibration, attains the best average rank across nine OpenML contextual bandit benchmarks, and yields higher estimated policy values than linear, neural, and tree-ensemble baselines in a Drink Less micro-randomized trial case study. Across OpenML benchmarks, BFTS is robust to hyperparameter choices.

## One-Sentence Claim

BFTS combines Thompson sampling with arm-wise Bayesian Additive Regression Trees to get calibrated nonlinear contextual bandits with theoretical regret and strong tabular performance.

## Problem

Contextual bandits need uncertainty-aware action selection. Linear models can be too restrictive for tabular nonlinear relationships, while neural methods can be poorly calibrated or hard to tune in moderate-data settings.

The paper asks whether BART's flexible Bayesian tree ensembles can provide useful posterior sampling for contextual bandits.

## Core Contribution

The paper proposes Bayesian Forest Thompson Sampling. It models each action's mean reward with an arm-wise Bayesian Additive Regression Tree and uses MCMC posterior draws for Thompson-sampling decisions.

It derives an information-theoretic Bayesian regret bound of order tilde O(K sqrt(T)) for ideal posterior sampling under a correctly specified Bayesian design. Empirically, it performs well on synthetic, OpenML, and micro-randomized-trial settings.

## Method

BFTS maintains a separate BART posterior for each arm. At decision time, it samples a reward function from each arm's posterior and chooses the action with the highest sampled reward. MCMC provides posterior draws, while BART supplies nonlinear tabular structure and uncertainty.

The regret analysis applies to ideal posterior sampling under correct Bayesian specification.

## Experiments and Evidence

Evidence reported in the abstract:

- Information-theoretic Bayesian regret bound of tilde O(K sqrt(T)).
- Competitive regret on nonlinear synthetic benchmarks.
- Near-nominal uncertainty calibration.
- Best average rank across nine OpenML contextual bandit benchmarks.
- Higher estimated policy values than linear, neural, and tree-ensemble baselines in a Drink Less micro-randomized trial case study.
- Robustness to hyperparameter choices across OpenML.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: MCMC cost, posterior approximation quality, benchmark construction, and off-policy evaluation for the trial case study.

## Limits and Failure Modes

- MCMC-based posterior sampling can be computationally expensive.
- The regret bound assumes correct Bayesian specification and ideal posterior sampling.
- Arm-wise models may share less information across actions than joint models.
- Off-policy estimated policy values depend on logging-policy and evaluation assumptions.

## Deep Themes

**Classical Bayesian models remain competitive for tabular decisions.** BART provides nonlinear flexibility and calibrated uncertainty without deep-network complexity.

**Uncertainty calibration is central to bandit performance.** Thompson sampling depends on posterior quality, not just point prediction.

**Theory and practical decision studies are linked.** The paper spans regret, benchmarks, and a micro-randomized trial.

## Subthemes

- BART for contextual bandits.
- Arm-wise posterior sampling.
- MCMC uncertainty.
- Bayesian regret bounds.
- Micro-randomized trial policy learning.

## Connections to Other Papers

Connects to BCO Gradient Variation, ROCP, TRECA, and risk-aware decision papers through sequential decision-making under uncertainty. It also links to Falling Trees because both use tree-structured models for interpretable or calibrated decision settings.

## Notes for Cross-Paper Synthesis

BFTS reinforces that "modern" decision systems need not always be neural; calibrated Bayesian structure can be the right control surface for tabular online learning.
