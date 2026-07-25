# Practical and Optimal Algorithm for Linear Contextual Bandits with Rare Parameter Updates

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: rEqVnZZOiA
- Authors: Sanghoon Yu; Min-hwan Oh
- Primary area: theory->online_learning_and_bandits
- Keywords: linear contextual bandit;generalized linear contextual bandit;limited adaptivity
- Source URL: https://openreview.net/forum?id=rEqVnZZOiA
- PDF URL: https://openreview.net/pdf?id=rEqVnZZOiA

## Abstract

We study linear contextual bandits under rare parameter updates:
the learner may incorporate reward feedback into its parameter estimate only at a small number of update times,
while still observing contexts online and selecting actions sequentially.
This viewpoint clarifies a practical distinction that is often blurred in the literature:
many "strictly batched" methods additionally restrict within-interval context adaptivity,
meaning that the action rule inside an interval cannot depend on the sequence of realized contexts/actions in that interval (beyond the current round's context).
For linear contextual bandits, we propose two practical algorithms with only $O(\log\log T)$ parameter updates.
Our first algorithm BLCE-G attains minimax-optimal regret (up to polylogarithmic factors in $T$) simultaneously in both the small-$K$ and large-$K$ regimes under a static schedule.
Our second algorithm BLCE removes the near G-optimal design step---a dominant computational bottleneck in prior strictly batched static-grid methods---yet preserves minimax-optimal regret and achieves the lowest known runtime complexity among optimal algorithms.
We further extend these rare-update and computational principles to generalized linear contextual bandits.
Overall, our results yield statistically optimal algorithms under $O(\log\log T)$ parameter updates that are also computationally efficient in practice.

## One-Sentence Claim

Linear and generalized linear contextual bandits can achieve near-minimax regret with only O(log log T) parameter updates, while preserving context adaptivity and reducing computational bottlenecks.

## Problem

Many bandit algorithms assume frequent model updates, but practical systems may update parameters only rarely due to computation, synchronization, or deployment constraints. Existing batched methods often conflate rare parameter updates with stricter restrictions on within-interval adaptivity.

The paper separates these ideas: a learner may update parameters rarely while still observing contexts and adapting actions sequentially within update intervals.

## Core Contribution

The paper proposes two practical algorithms for linear contextual bandits with only O(log log T) parameter updates. BLCE-G achieves minimax-optimal regret up to polylog factors under a static schedule across small-K and large-K regimes.

BLCE removes the near G-optimal design step that dominates runtime in prior strictly batched static-grid methods while preserving minimax-optimal regret. The principles are also extended to generalized linear contextual bandits.

## Method

The algorithms use rare update schedules while maintaining online context-conditioned action choice. This preserves adaptivity inside intervals, unlike stricter batched designs that freeze too much of the decision rule.

BLCE-G uses a design-oriented construction to achieve optimal regret, while BLCE simplifies the computation by avoiding near G-optimal design. The extension to generalized linear models adapts the same rare-update/statistical-efficiency tradeoff beyond linear rewards.

## Experiments and Evidence

This is primarily a theory/algorithm paper. The abstract reports minimax-optimal regret up to polylog factors, O(log log T) parameter updates, and the lowest known runtime complexity among optimal algorithms in the relevant setting.

Full-paper reading should verify regret constants, dependence on dimension/action count, the exact update schedule, GLM assumptions, and any empirical runtime demonstrations.

## Limits and Failure Modes

The guarantees depend on linear or generalized linear reward structure. Misspecification, nonstationarity, delayed feedback, or adversarial contexts may weaken the conclusions.

Rare updates are practical, but if the environment changes quickly, update scarcity can become a liability. The optimal static schedule may need modification for drift or production monitoring.

## Deep Themes

- Limited adaptivity as a systems constraint: algorithms should respect real update budgets.
- Statistical optimality with computational frugality: regret and runtime are optimized jointly.
- Within-interval context adaptivity: rare updates need not mean frozen action rules.
- Practical bandit theory: removing design bottlenecks matters as much as asymptotic regret.

## Subthemes

- O(log log T) updates are enough for near-optimal learning.
- Small-K and large-K regimes require simultaneous handling.
- G-optimal design can be a computational bottleneck.
- GLM extensions broaden practical relevance.

## Connections to Other Papers

This paper connects to no-swap-regret auction guarantees and FTRL lower-bound work through online-learning dynamics. It also relates to JitRL and deployment-oriented agent adaptation because rare updates are a form of practical learning constraint.

It fits the efficiency-as-capability theme at the algorithmic level rather than hardware or model compression.

## Notes for Cross-Paper Synthesis

The synthesis point is that online learning is being redesigned for operational update budgets. The best algorithm is not only statistically optimal; it must fit how often systems can safely update.
