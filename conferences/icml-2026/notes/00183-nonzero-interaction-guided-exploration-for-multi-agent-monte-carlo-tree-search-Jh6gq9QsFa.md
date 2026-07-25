# NonZero: Interaction-Guided Exploration for Multi-Agent Monte Carlo Tree Search

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Jh6gq9QsFa
- Authors: Sizhe Tang; Zuyuan Zhang; Mahdi Imani; Tian Lan
- Primary area: reinforcement_learning
- Keywords: Monte Carlo Tree Search;Multi-Agent System;Reinforcement Learning
- Source URL: https://openreview.net/forum?id=Jh6gq9QsFa
- PDF URL: https://openreview.net/pdf?id=Jh6gq9QsFa

## Abstract

Monte Carlo Tree Search (MCTS) scales poorly in cooperative multi-agent domains because expansion must consider an exponentially large set of joint actions, severely limiting exploration under realistic search budgets. We propose \textsc{NonZero}, which keeps multi-agent MCTS tractable by running surrogate-guided selection over a low-dimensional nonlinear representation using an interaction-guided proposal rule, instead of directly exploring the full joint-action space. Our exploration uses an interaction score: single-agent deviations are ranked by predicted gain, while two-agent deviations are scored by a mixed-difference measure that reveals coordination benefits even when no single agent can improve alone. We formalize candidate proposal as a bandit problem over local deviations and derive a proposal rule, \textsc{NonUCT}, with a sublinear local-regret guarantee for reaching approximate graph-local optima without enumerating the joint-action space. Empirically, \textsc{NonZero} improves sample efficiency and final performance on MatGame, SMAC, and SMACv2 relative to strong model-based and model-free baselines under matched search budgets.

## One-Sentence Claim

NonZero makes cooperative multi-agent MCTS tractable by proposing interaction-guided local deviations instead of enumerating the exponential joint-action space.

## Problem

Multi-agent MCTS suffers from exponential joint-action branching, so realistic search budgets cannot explore coordinated actions effectively.

## Core Contribution

The paper introduces a low-dimensional surrogate-guided MCTS method with interaction scores, a bandit formulation over local deviations, and a NonUCT proposal rule with sublinear local regret.

## Method

NonZero ranks single-agent deviations by predicted gain and two-agent deviations by mixed differences that reveal coordination benefits even when no individual agent improves alone. NonUCT proposes local candidates to approach graph-local optima without full joint-action enumeration.

## Experiments and Evidence

The abstract reports better sample efficiency and final performance on MatGame, SMAC, and SMACv2 relative to strong model-based and model-free baselines under matched search budgets.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: surrogate representation, graph locality assumptions, higher-order interaction failures, computational overhead, and scalability to many-agent real-time settings.

## Deep Themes

- Coordination requires detecting interaction effects invisible to single-agent improvements.
- Search efficiency comes from structured local proposal rather than brute-force branching.
- Bandit regret tools can guide planning in combinatorial multi-agent spaces.

## Subthemes

- Multi-agent reinforcement learning.
- Monte Carlo Tree Search.
- Cooperative coordination.
- Interaction scoring.
- Bandit candidate proposal.
- Graph-local optima.

## Connections to Other Papers

Connects to compute-bounded RL and test-time search/control papers through adaptive inference under budgets. It also relates to multi-agent preference and online-learning papers through interaction-aware decision structure.

## Notes for Cross-Paper Synthesis

NonZero adds a coordination-search variant of the structure theme: the right low-dimensional interaction representation can reveal joint improvements without enumerating the full action product.
