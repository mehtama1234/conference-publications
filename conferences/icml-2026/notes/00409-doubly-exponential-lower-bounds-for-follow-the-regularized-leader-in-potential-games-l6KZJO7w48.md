# (Doubly) Exponential Lower Bounds for Follow the Regularized Leader in Potential Games

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: l6KZJO7w48
- Authors: Ioannis Anagnostides; Ioannis Panageas; Nikolas Patris; Tuomas Sandholm
- Primary area: theory->game_theory
- Keywords: FTRL;MWU;fictitious play;Nash equilibrium;potential games
- Source URL: https://openreview.net/forum?id=l6KZJO7w48
- PDF URL: https://openreview.net/pdf?id=l6KZJO7w48

## Abstract

Follow the regularized leader (FTRL) is the premier algorithm for online optimization. However, despite decades of research on its convergence in constrained optimization---and potential games in particular---its behavior remained hitherto poorly understood. In this paper, we establish that FTRL can take exponential time to converge to a Nash equilibrium in two-player potential games for any (permutation-invariant) regularizer and potentially vanishing learning rate. By known equivalences, this translates to an exponential lower bound for certain mirror descent counterparts, most notably multiplicative weights update. On the positive side, we establish the potential property for FTRL and obtain an exponential upper bound $\exp(O_{\epsilon}(1/\epsilon^2))$ for any no-regret dynamics executed in a lazy, alternating fashion, matching our lower bound up to factors in the exponent. Finally, in multi-player potential games, we show that fictitious play---the extreme version of FTRL---can take doubly exponential time to reach a Nash equilibrium. This constitutes an exponentially stronger lower bound for the foundational learning algorithm in games.

## One-Sentence Claim

FTRL and related no-regret dynamics can require exponential or doubly exponential time to reach Nash equilibria in potential games, despite their foundational status.

## Problem

FTRL is central in online optimization and game learning, but its convergence behavior in constrained optimization and potential games is not fully understood. Potential games have structure that might suggest favorable convergence, yet learning dynamics can still be very slow.

The paper asks how bad convergence time can be for FTRL, mirror descent variants, and fictitious play in potential games.

## Core Contribution

The paper proves that FTRL can take exponential time to converge to a Nash equilibrium in two-player potential games for any permutation-invariant regularizer and potentially vanishing learning rate. By equivalence, this gives exponential lower bounds for mirror descent counterparts including multiplicative weights.

It also establishes a potential property and an exponential upper bound for lazy alternating no-regret dynamics, matching lower bounds up to exponent factors. In multi-player potential games, fictitious play can take doubly exponential time.

## Method

The work constructs hard potential games and analyzes the trajectories of FTRL-type dynamics under broad regularizer classes. It relates FTRL to mirror descent and multiplicative weights through known equivalences.

For the upper-bound side, it studies lazy alternating no-regret dynamics and proves convergence within an exponential bound.

## Experiments and Evidence

Evidence reported in the abstract:

- Exponential convergence lower bound for FTRL in two-player potential games.
- Applies to any permutation-invariant regularizer and potentially vanishing learning rate.
- Transfers to mirror descent counterparts including multiplicative weights.
- Potential property for FTRL.
- Exponential upper bound for lazy alternating no-regret dynamics.
- Doubly exponential lower bound for fictitious play in multi-player potential games.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: hard-game construction, epsilon dependence, and regularizer assumptions.

## Limits and Failure Modes

- Worst-case lower bounds may not describe typical practical games.
- Potential games are structured but still a specific class.
- The results focus on time to equilibrium, not necessarily approximate performance during transients.
- Alternative dynamics outside FTRL/fictitious play may avoid the lower bounds.

## Deep Themes

**No-regret does not mean fast equilibrium.** Long-run guarantees can hide severe convergence-time barriers.

**Structured games can still be computationally hard dynamically.** Potential functions do not automatically yield efficient learning.

**Algorithmic folklore needs worst-case audits.** Foundational methods can have unexpectedly bad regimes.

## Subthemes

- FTRL in potential games.
- Multiplicative weights lower bounds.
- Fictitious play.
- Nash equilibrium convergence time.
- Exponential and doubly exponential dynamics.

## Connections to Other Papers

Connects to Asymmetric Perturbation, Delayed-Observation RL, Mean-Expansion Q-Learning, and optimization/game-theory papers. It is a cautionary counterpart to fast-convergence methods.

## Notes for Cross-Paper Synthesis

This paper adds a negative-theory layer: widely used adaptive dynamics can be fundamentally slow, so convergence claims need time-scale scrutiny.
