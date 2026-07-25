# Recurrent Structural Policy Gradient for Partially Observable Mean Field Games

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: VkZQThGNgI
- Authors: Clarisse Wibault; Johannes Forkel; Sebastian Rene Towers; Tiphaine Wibault; Juan Agustin Duque; George Whittle; Andreas Schaab; Yucheng Yang; Chiyuan Wang; Michael A Osborne; Benjamin Moll; Jakob Nicolaus Foerster
- Primary area: reinforcement_learning->multiagent
- Keywords: Mean Field Games;Reinforcement Learning;Policy Gradient;Dynamic Programming;Common Noise
- Source URL: https://openreview.net/forum?id=VkZQThGNgI
- PDF URL: https://openreview.net/pdf?id=VkZQThGNgI

## Abstract

Mean Field Games (MFGs) provide a principled framework for modelling interactions in large population systems. However, algorithmic progress has been limited since model-free methods are high variance and exact methods scale poorly. Recent Hybrid Structural Methods (HSMs) reduce variance while maintaining tractability by leveraging low-dimensional individual state and action spaces and known transition dynamics to compute the exact expected return conditioned on Monte Carlo rollouts of common noise. However, HSMs have not been extended to partially observable settings. We propose *Recurrent Structural Policy Gradient* (RSPG), the first history-aware HSM for MFGs with public partial information. RSPG achieves an order-of-magnitude faster convergence than model-free RL methods while learning history-aware behaviour, unlike current HSMs. To facilitate research into MFGs, we also introduce MFAX, our JAX-based framework for MFGs that supports both analytic and sample-based mean-field updates.

## One-Sentence Claim

RSPG extends hybrid structural policy gradients to partially observable mean-field games by adding history-aware recurrent behavior while preserving low-variance structural returns.

## Problem

Mean-field games model interactions among large populations, but scalable learning remains difficult. Model-free methods are high variance, while exact dynamic-programming approaches scale poorly. Hybrid Structural Methods reduce variance by combining Monte Carlo common-noise rollouts with exact expected-return computation under known dynamics, but prior HSMs do not handle partial observability.

The paper targets large-population systems where agents must condition behavior on public histories rather than fully observed state.

## Core Contribution

The paper introduces Recurrent Structural Policy Gradient, the first history-aware HSM for MFGs with public partial information. It learns recurrent policies that condition on observation history while retaining the variance-reduction benefits of structural expected-return computation.

It also introduces MFAX, a JAX framework for mean-field games supporting analytic and sample-based mean-field updates.

## Method

RSPG augments structural policy-gradient methods with recurrence so policies can use histories under partial observability. It leverages known transition dynamics and low-dimensional state/action spaces to compute expected returns conditioned on sampled common-noise trajectories.

MFAX provides implementation infrastructure for both analytic and sampled mean-field updates, making experiments and future algorithm development easier.

## Experiments and Evidence

Evidence reported in the abstract:

- Order-of-magnitude faster convergence than model-free RL methods.
- Ability to learn history-aware behavior unlike existing HSMs.
- Evaluation in partially observable MFG settings with public information.
- Release of a JAX-based MFG framework.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark games, recurrence architecture, variance estimates, common-noise assumptions, and comparison baselines.

## Limits and Failure Modes

- The approach relies on known transition dynamics and low-dimensional individual state/action spaces.
- Public partial information may not cover private-information MFGs.
- Recurrent policies can be harder to optimize and interpret.
- MFAX utility depends on the breadth and correctness of implemented game classes.

## Deep Themes

**Scalable multi-agent learning needs structural variance reduction.** RSPG keeps model knowledge where it helps and uses learning where exact methods fail.

**Partial observability makes history a state variable.** Recurrent policies become necessary when public signals are insufficient snapshots.

**Frameworks are research accelerators.** MFAX is part of the contribution because MFG progress depends on reusable analytic/sample-based infrastructure.

## Subthemes

- Partially observable mean-field games.
- Hybrid structural policy gradients.
- Common-noise rollouts.
- Recurrent history-aware behavior.
- JAX infrastructure for MFGs.

## Connections to Other Papers

Connects to RQE Actor-Critic, PAVE, and R2VPO through RL stability and policy-gradient geometry. It also links to data-market pricing and game-theoretic papers where approximate or tractable equilibrium concepts replace exact large-system solutions.

## Notes for Cross-Paper Synthesis

RSPG adds to the pattern that large strategic systems become tractable when the algorithm preserves known structure and only samples the irreducible uncertainty.
