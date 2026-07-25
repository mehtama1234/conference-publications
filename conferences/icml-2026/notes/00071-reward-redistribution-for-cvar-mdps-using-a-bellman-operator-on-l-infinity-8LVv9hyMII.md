# Reward Redistribution for CVaR MDPs using a Bellman Operator on L-infinity

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 8LVv9hyMII
- Authors: Aneri Muni; Vincent Taboga; Esther Derman; Pierre-Luc Bacon; Erick Delage
- Primary area: reinforcement_learning
- Keywords: Risk-Sensitive RL;Static CVaR RL;Static CVaR Dynamic Programming;Safe RL;CVaR Bellman Operator
- Source URL: https://openreview.net/forum?id=8LVv9hyMII
- PDF URL: https://openreview.net/pdf?id=8LVv9hyMII

## Abstract

Tail-end risk measures such as static conditional value-at-risk (CVaR) are  used in safety-critical applications to prevent rare, yet catastrophic events. Unlike risk-neutral objectives, the static CVaR of the return depends on entire trajectories without admitting a recursive Bellman decomposition in the underlying Markov decision process. A classical resolution relies on state augmentation with a continuous variable. However, unless restricted to a specialized class of admissible value functions, this formulation induces sparse rewards and degenerate fixed points. In this work, we propose a novel formulation of the static CVaR objective based on augmentation. Our alternative approach leads to a Bellman operator with: (1) dense per-step rewards; (2) contracting properties on the full space of bounded value functions. Building on this theoretical foundation, we develop risk-averse value iteration and model-free Q-learning algorithms that rely on discretized augmented states. We further provide convergence guarantees and approximation error bounds due to discretization. Empirical results demonstrate that our algorithms successfully learn CVaR-sensitive policies and achieve effective performance-safety trade-offs.

## One-Sentence Claim

Static CVaR reinforcement learning can be made Bellman-compatible by redistributing rewards over augmented states to obtain dense rewards and contraction on bounded value functions.

## Problem

Static CVaR depends on whole trajectories, so it does not naturally admit a recursive Bellman decomposition; classical augmented-state formulations can create sparse rewards and degenerate fixed points.

## Core Contribution

The paper proposes a new augmented formulation for static CVaR MDPs with a Bellman operator on L-infinity, enabling risk-averse value iteration and Q-learning with convergence and discretization-error guarantees.

## Method

It redistributes the CVaR objective into dense per-step rewards over discretized augmented states. The resulting Bellman operator is contractive over the full space of bounded value functions rather than only a specialized admissible class.

## Experiments and Evidence

The abstract reports empirical results showing that the algorithms learn CVaR-sensitive policies and achieve effective performance-safety tradeoffs.

## Limits and Failure Modes

ArXiv search failed with rate-limit/service errors for this batch, so this note is abstract-only. Details still need checking: the exact augmented-state variable, discretization complexity, convergence assumptions, and empirical domains.

## Deep Themes

- Safety objectives need dynamic-programming structure to scale.
- Risk sensitivity often requires changing the state or reward representation.
- Bellman operators are being adapted for non-risk-neutral deployment criteria.

## Subthemes

- CVaR reinforcement learning.
- Static risk measures.
- Reward redistribution.
- Augmented MDPs.
- Risk-averse value iteration.
- Safe RL.

## Connections to Other Papers

Connects to CSPO and other safe-RL papers through performance-safety tradeoffs. It also links to theory papers that modify classical operators or abstractions to fit deployment-relevant objectives.

## Notes for Cross-Paper Synthesis

This paper adds to the safety-as-objective-design theme: making tail-risk optimization practical requires rebuilding the recursive learning machinery around the risk measure.
