# Accelerating Q-learning through Efficient Value-Sharing across Actions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: bQXQa5NDpH
- Authors: Prabhat Nagarajan; Brett Daley; Martha White; Marlos C. Machado
- Primary area: reinforcement_learning->deep_rl
- Keywords: DQN;Dueling networks;Value-sharing;Mean-expansion layer
- Source URL: https://openreview.net/forum?id=bQXQa5NDpH
- PDF URL: https://openreview.net/pdf?id=bQXQa5NDpH

## Abstract

Action-values are foundational to many control algorithms such as Q-learning. Therefore learning action-values efficiently is central to reinforcement learning (RL).  However, learning them can be slow, requiring many updates to move values from their initialization, typically near zero, to their true values, which may be far from zero. Moreover, action-value learning algorithms typically update each state–action pair independently, without learning shared value structure across actions within a state. In this paper, we address these inefficiencies by introducing the mean-expansion layer, which accelerates action-value learning by sharing values across actions within a state and by changing the problem from directly learning potentially large action-values to learning a lower-norm representation of them. In deep RL, this layer can be applied as a parameter-free addition to Q-network architectures without altering the underlying algorithm. Applied to deep Q-networks and implicit quantile networks, it improves aggregate performance across 57 Atari games while increasing action gaps and dramatically reducing value overestimation.

## One-Sentence Claim

A parameter-free mean-expansion layer accelerates Q-learning by sharing value structure across actions and learning lower-norm action-value representations.

## Problem

Q-learning depends on accurate action-values, but values can move slowly from near-zero initialization to large true values. Standard action-value learning often updates state-action pairs independently, missing shared structure among actions in the same state.

The paper asks how to make action-value learning faster without changing the underlying RL algorithm.

## Core Contribution

The paper introduces the mean-expansion layer, a parameter-free architectural addition for Q-networks. It shares values across actions within a state and reframes learning large action-values as learning a lower-norm representation.

Applied to DQNs and implicit quantile networks, it improves aggregate Atari performance, increases action gaps, and dramatically reduces value overestimation.

## Method

The layer decomposes or reparameterizes action values so that common value mass can be shared across actions, while action-specific deviations are learned separately. This reduces the scale of what each action head must learn and improves propagation away from initialization.

Because it is parameter-free, it can be inserted into existing Q-network architectures without changing the base algorithm.

## Experiments and Evidence

Evidence reported in the abstract:

- Parameter-free mean-expansion layer.
- Applies to deep Q-networks and implicit quantile networks.
- Aggregate performance gains across 57 Atari games.
- Increased action gaps.
- Dramatically reduced value overestimation.
- No change to underlying algorithms.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact reparameterization, Atari metrics, ablations, and impact on exploration.

## Limits and Failure Modes

- Value sharing across actions may hurt tasks where action values are genuinely independent.
- Reduced overestimation may depend on environment reward scale.
- Atari results may not transfer to continuous action or multi-agent settings.
- Parameter-free layers can still introduce representation assumptions.

## Deep Themes

**Action-values have shared structure.** Learning each action independently wastes sample updates.

**Reparameterization can accelerate RL.** The method improves learning dynamics without adding parameters.

**Value scale affects optimization.** Lower-norm representations are easier to learn from initialization.

## Subthemes

- Mean-expansion layer.
- Q-value sharing across actions.
- Reduced value overestimation.
- Action-gap enlargement.
- Parameter-free RL architecture.

## Connections to Other Papers

Connects to PAVE, R2VPO, T2PO, and BFTS through RL stability and value/uncertainty representation. It also links to Constrained Transformers because both improve learning by changing internal representation dynamics.

## Notes for Cross-Paper Synthesis

This paper adds a reparameterization pattern: learning becomes easier when outputs are decomposed into shared and residual structure rather than learned independently.
