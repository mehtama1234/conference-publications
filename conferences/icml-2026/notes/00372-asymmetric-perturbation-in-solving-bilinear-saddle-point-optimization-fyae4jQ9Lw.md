# Asymmetric Perturbation in Solving Bilinear Saddle-Point Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fyae4jQ9Lw
- Authors: Kenshi Abe; Mitsuki Sakamoto; Kaito Ariu; Atsushi Iwasaki
- Primary area: theory->optimization
- Keywords: Learning in games;Saddle-point optimization
- Source URL: https://openreview.net/forum?id=fyae4jQ9Lw
- PDF URL: https://openreview.net/pdf?id=fyae4jQ9Lw

## Abstract

This paper proposes asymmetric perturbation, where only one player's payoff function is perturbed, for solving bilinear saddle-point optimization problems, commonly arising in minimax problems, game theory, and constrained optimization. 
Symmetric perturbation is known to require decreasing its strength to ensure convergence to a solution, i.e., an equilibrium in the original game, resulting in a slower rate.
First, with asymmetric perturbation, we show that, for a sufficiently small perturbation strength, the equilibrium strategy of the asymmetrically perturbed game coincides with an equilibrium strategy of the original unperturbed game.
Second, building on this coincidence, we construct a learning algorithm with a linear last-iterate convergence rate. 
Third, motivated by the fact that the coincidence relies on the perturbation strength being sufficiently small, we also provide a parameter-free variant, retaining the linear rate. 
Finally, we empirically demonstrate fast convergence toward equilibria in both normal-form and extensive-form games.

## One-Sentence Claim

Perturbing only one player's payoff in bilinear saddle-point games can preserve the original equilibrium while enabling linear last-iterate convergence.

## Problem

Bilinear saddle-point problems arise in minimax optimization, games, and constrained learning. Symmetric perturbation can stabilize learning, but to converge to an equilibrium of the original game its strength must be decreased, which slows the rate.

The paper asks whether a different perturbation geometry can give fast convergence without biasing the solution away from the original equilibrium.

## Core Contribution

The paper proposes asymmetric perturbation, where only one player's payoff is perturbed. It proves that for sufficiently small perturbation strength, the equilibrium strategy of the perturbed game coincides with an equilibrium strategy of the original game.

Using this coincidence, the authors construct a learning algorithm with linear last-iterate convergence and a parameter-free variant that retains the linear rate.

## Method

The method changes the game by perturbing one side's objective rather than both. This modifies the dynamics enough to remove troublesome cycling or slow convergence while leaving the target equilibrium unchanged under suitable perturbation strength.

The parameter-free variant avoids requiring prior knowledge of how small the perturbation must be.

## Experiments and Evidence

Evidence reported in the abstract:

- Equilibrium coincidence result for sufficiently small asymmetric perturbation.
- Linear last-iterate convergence algorithm.
- Parameter-free variant with retained linear rate.
- Empirical fast convergence in normal-form and extensive-form games.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: bilinear assumptions, perturbation form, constants, and game benchmarks.

## Limits and Failure Modes

- Results may rely on bilinear structure and may not extend directly to nonlinear minimax problems.
- The equilibrium coincidence depends on sufficiently small perturbation strength.
- Parameter-free adaptation may hide practical tuning or transient costs.
- Extensive-form-game performance needs comparison against specialized solvers.

## Deep Themes

**Asymmetry can improve optimization.** Treating the two players differently can stabilize dynamics without moving the solution.

**Perturbations are algorithmic devices.** The perturbation is not modeling noise; it reshapes the learning path.

**Last-iterate convergence matters for games.** The paper targets actual iterate stability, not only averaged convergence.

## Subthemes

- Bilinear saddle-point optimization.
- Asymmetric payoff perturbation.
- Equilibrium-preserving regularization.
- Linear last-iterate convergence.
- Parameter-free game learning.

## Connections to Other Papers

Connects to Mean-Expansion Q-Learning, Delayed-Observation RL, Constrained Transformers, Auxiliary MCMC, and theory papers on optimization structure. It fits the theme of changing dynamics without changing the desired fixed point.

## Notes for Cross-Paper Synthesis

This paper adds an optimization-dynamics motif: carefully chosen asymmetry can convert unstable cyclic learning into fast convergence while preserving the intended solution.
