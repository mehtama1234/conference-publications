# Stable Deep Reinforcement Learning via Isotropic Gaussian Representations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: gc7Gg18ejz
- Authors: Ali Saheb Pasand; Johan Obando-Ceron; Aaron Courville; Pouya Bashivan; Pablo Samuel Castro
- Primary area: reinforcement_learning->deep_rl
- Keywords: reinforcement learning;non-stationarity;stability;representation learning
- Source URL: https://openreview.net/forum?id=gc7Gg18ejz
- PDF URL: https://openreview.net/pdf?id=gc7Gg18ejz

## Abstract

Deep reinforcement learning systems often suffer from unstable training dynamics due to non-stationarity, where learning objectives and data distributions evolve over time. We show that under non-stationary targets, isotropic Gaussian embeddings are provably advantageous. In particular, they induce stable tracking of time-varying targets for linear readouts, achieve maximal entropy under a fixed variance budget, and encourage a balanced use of all representational dimensions--all of which enable agents to be more adaptive and stable. Building on this insight, we propose the use of Sketched Isotropic Gaussian Regularization for shaping representations toward an isotropic Gaussian distribution during training. We demonstrate empirically, over a variety of domains, that this simple and computationally inexpensive method improves performance under non-stationarity while reducing representation collapse, neuron dormancy, and training instability.

## One-Sentence Claim

Regularizing RL representations toward isotropic Gaussian embeddings improves stability under non-stationarity by preventing collapse and balancing representational dimensions.

## Problem

Deep RL training is unstable because objectives and data distributions evolve as the agent learns. Representations can collapse, neurons can become dormant, and linear readouts must track moving targets.

The paper asks what representation distribution is well suited for stable tracking under non-stationary targets.

## Core Contribution

The paper shows that isotropic Gaussian embeddings are theoretically advantageous under non-stationarity: they support stable tracking for linear readouts, maximize entropy under a fixed variance budget, and encourage balanced use of all dimensions.

It then proposes Sketched Isotropic Gaussian Regularization, a simple inexpensive method for shaping representations toward that distribution during RL training.

## Method

The method regularizes hidden representations so their empirical distribution approaches an isotropic Gaussian. The "sketched" formulation suggests a computationally efficient approximation rather than full covariance matching at every step.

By encouraging all dimensions to be used evenly and preserving high entropy, the regularizer aims to keep the representation adaptive as targets shift.

## Experiments and Evidence

Evidence reported in the abstract:

- Provable advantages of isotropic Gaussian embeddings for non-stationary targets and linear readouts.
- Maximal entropy under fixed variance budget.
- Balanced use of representational dimensions.
- Empirical improvements across a variety of domains.
- Reduced representation collapse, neuron dormancy, and training instability.
- Computationally inexpensive regularization.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: RL domains, sketching method, regularizer strength, and interaction with existing normalization.

## Limits and Failure Modes

- Isotropic Gaussian structure may conflict with tasks requiring sparse or structured representations.
- Benefits for linear readouts may not fully transfer to nonlinear policy/value heads.
- Regularization strength may be sensitive across environments.
- Gaussianization can hide task-relevant anisotropy if applied too aggressively.

## Deep Themes

**Representation geometry governs RL stability.** The distribution of hidden states affects how well agents track changing targets.

**Entropy can be a stabilizer.** Maximal entropy under variance constraints avoids premature representational collapse.

**Simple regularizers can target deep failure modes.** The method addresses non-stationarity through representation shaping rather than algorithmic overhaul.

## Subthemes

- Isotropic Gaussian embeddings.
- Non-stationary RL targets.
- Representation collapse.
- Neuron dormancy.
- Sketched covariance/shape regularization.

## Connections to Other Papers

Connects to Mean-Expansion Q-Learning, Delayed-Observation RL, Hista/Numca, Fisher Memory Dynamics, and Constrained Transformers. It also aligns with representation-geometry papers that treat hidden-state shape as a control variable.

## Notes for Cross-Paper Synthesis

This paper closes the current ICML stub window with a broad lesson: stable learning often depends on shaping representation geometry so downstream updates remain well conditioned under changing data.
