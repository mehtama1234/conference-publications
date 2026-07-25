# Exact Unlearning in Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: oLmwqIhzqj
- Authors: Thanh Nguyen-Tang; Raman Arora
- Primary area: theory->reinforcement_learning_and_planning
- Keywords: Reinforcement Learning;Exact Unlearning
- Source URL: https://openreview.net/forum?id=oLmwqIhzqj
- PDF URL: https://openreview.net/pdf?id=oLmwqIhzqj

## Abstract

We formulate the problem of \emph{exact unlearning} in reinforcement learning, where the goal is to design an efficient framework that enables the removal of any user’s data upon deletion request, i.e., the online learner’s output after unlearning be \emph{indistinguishable} from what would have been produced had the deleted user never interacted with the learner. For any $\rho >0$, we show that there exists a reinforcement learning (RL) algorithm that is $\rho$-TV-stable and supports an exact unlearning procedure whose expected computational cost is only a $\rho \sqrt{\ln T}$ fraction of the computational cost of retraining from scratch. We construct such a $\rho$-TV-stable RL algorithm for tabular Markov decision processes (MDPs), which achieves a regret bound of  $\mathcal{O}(H^2 \sqrt{SAT} + H^3 S^2 A + {H^{2.5} S^2 A}/{\rho})$, where $S, A, H$, and $T$ denote the number of states, the number of actions, the episode horizon, and the number of episodes, respectively. We also establish a lower bound of $\Omega(H\sqrt{SAT}+{SAH}/{\rho})$  for $\rho$-TV-stable RL algorithms,  showing that our algorithm is nearly minimax optimal.

## One-Sentence Claim

Exact unlearning in reinforcement learning is possible through TV-stable algorithms that remove a user's data with expected cost far below retraining while remaining nearly minimax optimal for tabular MDP regret.

## Problem

Machine unlearning asks whether a trained system can remove a user's data so that the resulting output is indistinguishable from a model trained without that data. In reinforcement learning, this is harder than in static supervised learning because user interactions affect adaptive data collection, state visitation, and later learning.

The paper formalizes exact unlearning for online RL and asks for an efficient procedure that avoids full retraining while preserving learning performance.

## Core Contribution

The paper proves that for any rho > 0 there is an RL algorithm that is rho-TV-stable and supports exact unlearning with expected computational cost only a rho sqrt(log T) fraction of retraining from scratch.

It constructs such an algorithm for tabular MDPs with a regret upper bound and proves a lower bound for rho-TV-stable RL algorithms, showing near minimax optimality. The contribution is both definitional and algorithmic: exact RL unlearning becomes a precise stability/computation/regret tradeoff.

## Method

The framework relies on total-variation stability. A rho-TV-stable learner limits how much any user's data can affect the output distribution, which makes it possible to resample or repair the learner's state after deletion requests without full retraining.

For tabular MDPs, the constructed algorithm balances regret against stability through rho. Smaller rho gives stronger stability/unlearning behavior but increases the regret term, making privacy/deletion support an explicit statistical cost.

## Experiments and Evidence

This is a theoretical result. The abstract gives an upper regret bound of O(H^2 sqrt(SAT) + H^3 S^2 A + H^2.5 S^2 A / rho) and a lower bound of Omega(H sqrt(SAT) + SAH / rho), establishing near minimax optimality.

The evidence rests on the proof that the unlearned output is indistinguishable from the counterfactual learner that never saw the deleted user. Full-paper reading should verify the user model, deletion granularity, computational-cost accounting, and constants.

## Limits and Failure Modes

The result is for tabular MDPs, so scaling to function approximation, deep RL, partial observability, offline RL datasets, or multi-agent settings remains open. Exact indistinguishability may also require assumptions about randomness, logs, and implementation reproducibility that are difficult in production systems.

The rho tradeoff is fundamental: stronger unlearning stability costs regret. Practical deployments would need to choose rho according to deletion frequency, performance tolerance, and regulatory risk.

## Deep Themes

- Unlearning as algorithmic stability: deletion support is built into the learner rather than patched on afterward.
- Governance constraints as learning objectives: privacy/deletion requirements reshape regret bounds.
- Exact counterfactual semantics: unlearning is defined by indistinguishability from never-training-on-the-user.
- Finite-computation compliance: the paper measures whether deletion can be done cheaper than retraining.

## Subthemes

- Adaptive data collection makes RL unlearning harder than supervised unlearning.
- TV stability supplies the bridge from deletion requests to output indistinguishability.
- The regret/stability tradeoff is explicit and nearly optimal.
- Tabular results define a baseline for future deep-RL unlearning work.

## Connections to Other Papers

This paper connects to privacy, unlearning, and governance themes across the corpus. It also relates to auction no-swap-regret theory: both study adaptive agents with finite-time guarantees, but here the guarantee is deletion correctness rather than revenue.

It complements MAP's production-agent concerns because real deployed agents may need deletion and audit mechanisms before they can be governed responsibly.

## Notes for Cross-Paper Synthesis

Exact RL unlearning expands the safety/governance theme from model outputs to training histories. A recurring pattern is that compliance cannot be bolted on cheaply unless the original learning algorithm is designed for it.
