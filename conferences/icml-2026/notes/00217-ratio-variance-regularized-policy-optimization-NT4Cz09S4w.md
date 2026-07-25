# Ratio-Variance Regularized Policy Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: NT4Cz09S4w
- Authors: Yu Luo; Shuo Han; Yihan Hu; Lei Lv; Huaping Liu; Fuchun Sun; Jianye HAO; Dong Li
- Primary area: deep_learning->large_language_models
- Keywords: Reinforcement Learning;Ratio-Variance Regularization;LLM Post-training;Sample Efficiency;Trust Region
- Source URL: https://openreview.net/forum?id=NT4Cz09S4w
- PDF URL: https://openreview.net/pdf?id=NT4Cz09S4w

## Abstract

Standard on-policy reinforcement learning relies on heuristic clipping to enforce trust regions, but this mechanism imposes a severe cost by indiscriminately truncating high-return yet high-divergence updates. We demonstrate that explicitly constraining the *policy ratio **variance*** provides a principled local approximation to trust-region constraints, eliminating the need for binary hard clipping. By acting as a distributional ''soft brake'', this approach preserves critical gradient signals from novel discoveries while naturally down-weighting and enabling the reuse of stale, off-policy data. We introduce **R$^2$VPO** (Ratio-Variance Regularized Policy Optimization), which implements this constraint via a primal–dual optimization framework. Extensive evaluations across $7$ LLM scales, spanning both fast and slow reasoning paradigms, and $10$ robotic control tasks demonstrate the generality of the proposed approach. R$^2$VPO achieves substantial performance gains on mathematical reasoning benchmarks, with particularly pronounced improvements on smaller models, while significantly improving sample efficiency. Furthermore, it consistently outperforms PPO baselines in continuous control domains, particularly in sparse-reward and dynamic environments. Together, these findings establish ratio-variance regularization as a principled foundation for stable and data-efficient policy optimization.

## One-Sentence Claim

R2VPO replaces hard policy-ratio clipping with ratio-variance regularization, preserving high-value gradient signals while stabilizing LLM post-training and robotic control.

## Problem

On-policy RL often relies on heuristic clipping for trust regions, but clipping indiscriminately removes high-return, high-divergence updates and wastes useful discovery signal.

## Core Contribution

The paper proposes policy-ratio variance as a principled local approximation to trust-region constraints and implements it with a primal-dual optimization framework that can reuse stale off-policy data.

## Method

R2VPO constrains the variance of policy ratios as a distributional soft brake, down-weighting risky updates without binary truncation and preserving gradients from novel high-return behaviors.

## Experiments and Evidence

The abstract reports evaluations across seven LLM scales and ten robotic control tasks, with gains on mathematical reasoning, especially smaller models, improved sample efficiency, and consistent improvements over PPO in sparse-reward and dynamic continuous-control domains.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: primal-dual stability, hyperparameter sensitivity, off-policy reuse conditions, benchmark details, safety alignment effects, and comparison to GRPO variants.

## Deep Themes

- Trust-region control can preserve discovery signal rather than clip it away.
- Policy optimization benefits from distributional constraints over update ratios.
- LLM post-training and robotics share stability/sample-efficiency problems.

## Subthemes

- Policy optimization.
- Ratio-variance regularization.
- LLM post-training.
- PPO alternatives.
- Trust regions.
- Robotic control.

## Connections to Other Papers

Connects to RLVepsR, Posterior Behavioral Cloning, APB, and compute-bounded RL through policy adaptation under noisy or constrained optimization.

## Notes for Cross-Paper Synthesis

R2VPO adds an optimization-control version of anti-waste: stabilizing RL should not discard exactly the high-return gradients that signal useful exploration.
