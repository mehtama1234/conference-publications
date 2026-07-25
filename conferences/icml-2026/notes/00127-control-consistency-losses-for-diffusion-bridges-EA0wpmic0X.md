# Control Consistency Losses for Diffusion Bridges

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: EA0wpmic0X
- Authors: Samuel Howard; Nikolas Nüsken; Jakiw Pidstrigach
- Primary area: probabilistic_methods->monte_carlo_and_sampling_methods
- Keywords: Diffusion bridges;Stochastic optimal control
- Source URL: https://openreview.net/forum?id=EA0wpmic0X
- PDF URL: https://openreview.net/pdf?id=EA0wpmic0X

## Abstract

Simulating the conditioned dynamics of diffusion processes, given their initial and terminal states, is an important but challenging problem in the sciences. The difficulty is particularly pronounced for rare events, for which the unconditioned dynamics rarely reach the terminal state. In this work, we propose a novel approach for learning diffusion bridges based on a self-consistency property of the optimal control. The resulting algorithm learns the conditioned dynamics in an iterative online manner, and exhibits strong performance in a range of empirical settings without requiring differentiation through simulated trajectories. Beyond the diffusion bridge setting, we draw connections between our self-consistency framework and recent advances in the wider stochastic optimal control literature.

## One-Sentence Claim

Diffusion bridges can be learned through self-consistency of optimal controls, enabling online conditioned-dynamics learning without differentiating through simulated trajectories.

## Problem

Simulating diffusion processes conditioned on endpoints is difficult, especially for rare events where unconditioned trajectories almost never reach the terminal state.

## Core Contribution

The paper proposes a control-consistency framework for learning diffusion bridges and connects it to broader stochastic optimal control methods.

## Method

The algorithm learns conditioned dynamics iteratively online by enforcing a self-consistency property of the optimal control, avoiding backpropagation through simulated trajectories.

## Experiments and Evidence

The abstract reports strong empirical performance across a range of settings and highlights rare-event diffusion bridge learning.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: consistency loss form, endpoint conditioning regime, rare-event benchmarks, convergence behavior, and comparison to score/bridge baselines.

## Deep Themes

- Conditioned stochastic dynamics can be learned via control consistency.
- Rare-event simulation needs guided dynamics rather than brute-force sampling.
- Diffusion bridge learning is converging with stochastic optimal control.

## Subthemes

- Diffusion bridges.
- Stochastic optimal control.
- Rare-event simulation.
- Control consistency.
- Online learning.
- Conditioned dynamics.

## Connections to Other Papers

Connects to Reinforced SMC, Rex, Schrödinger bridges for MAPF, and scientific diffusion/sampling papers through control-theoretic sampling infrastructure.

## Notes for Cross-Paper Synthesis

This paper strengthens the control-as-sampling theme: hard conditional distributions can be approached through learned controls that reshape path dynamics.
