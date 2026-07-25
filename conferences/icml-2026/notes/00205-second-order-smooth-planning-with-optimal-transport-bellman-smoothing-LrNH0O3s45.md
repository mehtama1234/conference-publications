# Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: LrNH0O3s45
- Authors: Tuan Quang Dam
- Primary area: reinforcement_learning->planning
- Keywords: Planning;Entropy-Regularized MDPs;Optimal Transport;Gap-Dependent Bounds;Robust RL
- Source URL: https://openreview.net/forum?id=LrNH0O3s45
- PDF URL: https://openreview.net/pdf?id=LrNH0O3s45

## Abstract

Planning with a generative model aims to estimate the value of a state using as few simulator calls as possible.
SmoothCruiser achieves problem-independent complexity $\widetilde O(\varepsilon^{-4})$ by exploiting the smoothness of the entropy-regularized Bellman backup, but its estimator is only first-order.
We show that the sample-complexity exponent of SmoothCruiser-type planners is governed by the order $\beta$ of the local Taylor remainder, giving oracle complexity $\widetilde O(\varepsilon^{-(2+2/(\beta-1))})$: the first-order case $\beta=2$ recovers SmoothCruiser, while a second-order/cubic remainder $\beta=3$ yields $\widetilde O(\varepsilon^{-3})$.
We reach this regime with an optimal-transport-smoothed Bellman backup over action distributions, which has a closed form, a policy gradient, and a Lipschitz Hessian, and whose quadratic correction admits an unbiased cross-product estimator.
The resulting SecondOrderSmoothCruiser achieves $\widetilde O(\varepsilon^{-3})$ oracle complexity for fixed OT parameters, and we relate the OT, entropy-regularized, and unregularized objectives through explicit regularization-bias bounds.

## One-Sentence Claim

SecondOrderSmoothCruiser uses optimal-transport Bellman smoothing to obtain second-order smooth planning with improved epsilon^-3 simulator-call complexity.

## Problem

Planning with a generative model seeks accurate value estimates with few simulator calls, but existing SmoothCruiser-type estimators are first-order and have epsilon^-4 complexity.

## Core Contribution

The paper shows planner complexity depends on the Taylor remainder order beta, then constructs an OT-smoothed Bellman backup with Lipschitz Hessian and an unbiased quadratic-correction estimator to reach the second-order regime.

## Method

The method defines an optimal-transport-smoothed backup over action distributions, derives its closed form, policy gradient, and Hessian smoothness, and uses a cross-product estimator for the quadratic correction.

## Experiments and Evidence

The abstract is primarily theoretical, claiming epsilon^-3 oracle complexity for fixed OT parameters and explicit regularization-bias bounds linking OT, entropy-regularized, and unregularized objectives.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: fixed-OT parameter assumptions, action-space requirements, constants, empirical validation if any, and sensitivity to regularization bias.

## Deep Themes

- Higher-order smoothness can reduce planning sample complexity.
- Optimal transport is a smoothing tool for Bellman backups.
- Regularization bias must be quantified when improving oracle complexity.

## Subthemes

- Reinforcement learning planning.
- Entropy-regularized MDPs.
- Optimal transport.
- Simulator-call complexity.
- Taylor remainders.
- Robust RL.

## Connections to Other Papers

Connects to compute-bounded RL, NonZero, and OT-DRO papers through planning/search efficiency and optimal-transport structure in decision-making.

## Notes for Cross-Paper Synthesis

This paper contributes a theory-side test-time efficiency theme: better mathematical smoothing of Bellman operators can directly reduce the simulator budget needed for planning.
