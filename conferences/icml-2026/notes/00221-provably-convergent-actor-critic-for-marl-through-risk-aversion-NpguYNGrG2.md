# Provably Convergent Actor-Critic for MARL through Risk-aversion

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: NpguYNGrG2
- Authors: Yizhou Zhang; Eric Mazumdar
- Primary area: reinforcement_learning->multiagent
- Keywords: Multi-agent Reinforcement Learning;Game Theory;Strategic Risk-aversion
- Source URL: https://openreview.net/forum?id=NpguYNGrG2
- PDF URL: https://openreview.net/pdf?id=NpguYNGrG2

## Abstract

Learning stationary policies in infinite-horizon general-sum Markov games (MGs) remains a fundamental open problem in Multi-Agent Reinforcement Learning (MARL). While stationary strategies are preferred for their practicality, computing stationary forms of classic game-theoretic equilibria is computationally intractable—a stark contrast to the comparative ease of solving single-agent RL or zero-sum games. To bridge this gap, we study Risk-averse Quantal response Equilibria (RQE), a solution concept rooted in behavioral game theory that incorporates risk aversion and bounded rationality. We demonstrate that RQE possesses strong regularity conditions that make it uniquely amenable to learning in MGs. We propose a novel single-timescale Actor-Critic algorithm characterized by a faster actor and a slower critic. Leveraging the regularity of RQE, we prove that this approach achieves global convergence with finite-sample guarantees. We empirically validate our algorithm in several environments to demonstrate superior convergence properties compared to risk-neutral baselines.

## One-Sentence Claim

Risk-averse quantal response equilibria make stationary-policy learning in general-sum Markov games amenable to globally convergent actor-critic with finite-sample guarantees.

## Problem

Learning practical stationary policies in infinite-horizon general-sum Markov games is difficult because standard equilibrium notions are computationally intractable compared with single-agent or zero-sum settings.

## Core Contribution

The paper studies RQE as a behavioral-game-theoretic solution concept with regularity properties, then proposes a single-timescale actor-critic algorithm with faster actor and slower critic updates and proves global convergence.

## Method

The algorithm leverages risk aversion and bounded rationality in RQE to obtain a learnable equilibrium target for Markov games, using actor-critic updates whose timescale relationship supports convergence analysis.

## Experiments and Evidence

The abstract reports empirical validation in several environments with superior convergence properties relative to risk-neutral baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: game classes, RQE parameters, finite-sample constants, actor/critic architecture, scalability to many agents, and sensitivity to risk-aversion misspecification.

## Deep Themes

- Alternative equilibrium concepts can make MARL learnable.
- Risk aversion can be an algorithmic regularizer, not only a preference model.
- Game-theoretic structure is needed for convergence beyond zero-sum cases.

## Subthemes

- Multi-agent reinforcement learning.
- Markov games.
- Risk-averse quantal response equilibrium.
- Actor-critic.
- Finite-sample guarantees.
- Behavioral game theory.

## Connections to Other Papers

Connects to NonZero, multi-agent preference papers, and compute-bounded RL through structured solution concepts and efficient search/learning in multi-agent decision spaces.

## Notes for Cross-Paper Synthesis

This paper adds a game-theoretic regularization theme: changing the equilibrium target can make otherwise intractable multi-agent learning dynamics provably manageable.
