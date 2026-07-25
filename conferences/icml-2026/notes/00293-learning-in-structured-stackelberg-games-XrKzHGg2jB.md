# Learning in Structured Stackelberg Games

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: XrKzHGg2jB
- Authors: Maria Florina Balcan; Kiriaki Fragkia; Keegan Harris
- Primary area: theory->game_theory
- Keywords: Stackelberg games;Littlestone dimension
- Source URL: https://openreview.net/forum?id=XrKzHGg2jB
- PDF URL: https://openreview.net/pdf?id=XrKzHGg2jB

## Abstract

We initiate the study of *structured Stackelberg games*, a novel form of strategic interaction between a leader and a follower where contextual information can be predictive of the follower's (unknown) type. Motivated by applications such as security games and AI safety, we show how this additional structure can help the leader learn a utility-maximizing policy in both the online and distributional settings. In the online setting, we first prove that standard learning-theoretic measures of complexity do not characterize the difficulty of the leader's learning task. We find that there exists a learning-theoretic measure of complexity, analogous to the Littlestone dimension in online classification, that *tightly* characterizes the leader's instance-optimal regret. We term this the *Stackelberg-Littlestone dimension*, and leverage it to provide a provably optimal online learning algorithm. In the distributional setting, we provide analogous results by showing that two new dimensions control the sample complexity upper- and lower-bound.

## One-Sentence Claim

Structured Stackelberg games become learnable when contextual information predicts follower type, with regret characterized by a new Stackelberg-Littlestone dimension.

## Problem

Stackelberg games model leader-follower strategic interactions relevant to security and AI safety. In many settings, contextual information helps predict the follower's unknown type, but standard game-learning analyses do not capture how this structure changes the leader's learning difficulty.

The paper asks which complexity measures characterize online and distributional learning in these structured Stackelberg games.

## Core Contribution

The paper initiates the study of structured Stackelberg games. In the online setting, it shows standard learning-theoretic complexity measures do not characterize the leader's learning task. It introduces the Stackelberg-Littlestone dimension, which tightly characterizes instance-optimal regret, and uses it to give a provably optimal online learning algorithm.

In the distributional setting, it introduces two additional dimensions that control sample-complexity upper and lower bounds.

## Method

The method is theoretical. It defines a contextual Stackelberg learning problem, analyzes why existing complexity measures fail, then constructs new dimensions analogous to Littlestone dimension but adapted to leader-follower utility and follower-type prediction.

The resulting algorithms and lower bounds tie learnability to these dimensions rather than generic hypothesis-class size.

## Experiments and Evidence

Evidence reported in the abstract:

- Formalization of structured Stackelberg games.
- Negative result for standard complexity measures.
- Stackelberg-Littlestone dimension tightly characterizing instance-optimal online regret.
- Provably optimal online learning algorithm.
- Two distributional dimensions controlling sample-complexity upper and lower bounds.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact game model, context/type assumptions, dimension definitions, algorithm complexity, and examples for security or AI safety.

## Limits and Failure Modes

- Practical use depends on whether follower types are learnably related to context.
- The new dimensions may be hard to estimate in real games.
- Stackelberg assumptions can fail if followers adapt strategically to the learning algorithm.
- Distributional guarantees depend on sampling assumptions.

## Deep Themes

**Strategic learnability needs task-specific complexity.** Standard measures fail because leader-follower structure changes what must be learned.

**Context can turn unknown types into learnable structure.** Predictive context reduces strategic uncertainty.

**Game theory and online learning are converging.** Littlestone-style dimensions are adapted to equilibrium and policy-learning problems.

## Subthemes

- Contextual follower types.
- Stackelberg-Littlestone dimension.
- Instance-optimal regret.
- Distributional sample-complexity dimensions.
- Security and AI-safety games.

## Connections to Other Papers

Connects to data-market pricing, RSPG, RQE Actor-Critic, and bandit-gradient variation through structured strategic learning. It also links to causal and decision benchmarks where hidden types or mechanisms must be inferred.

## Notes for Cross-Paper Synthesis

Structured Stackelberg Games reinforces the theory theme that the right complexity measure must reflect the decision structure, not merely the function class.
