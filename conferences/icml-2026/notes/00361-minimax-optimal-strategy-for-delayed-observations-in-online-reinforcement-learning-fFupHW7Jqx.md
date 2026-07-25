# Minimax Optimal Strategy for Delayed Observations in Online Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fFupHW7Jqx
- Authors: Harin Lee; Kevin Jamieson
- Primary area: theory->reinforcement_learning_and_planning
- Keywords: reinforcement learning;delayed observation;regret bound;regret lower bound
- Source URL: https://openreview.net/forum?id=fFupHW7Jqx
- PDF URL: https://openreview.net/pdf?id=fFupHW7Jqx

## Abstract

We study reinforcement learning with delayed state observation, where the agent observes the current state after some random number of time steps.
We propose an algorithm that combines the augmentation method and the upper confidence bound approach.
For tabular Markov decision processes (MDPs), we derive a regret bound of $\tilde{\mathcal{O}}(H \sqrt{D_{\max} SAK})$, where $S$ and $A$ are the cardinalities of the state and action spaces, $H$ is the time horizon, $K$ is the number of episodes, and $D_{\max}$ is the maximum length of the delay.
We also provide a matching lower bound up to logarithmic factors, showing the optimality of our approach.
Our analytical framework formulates this problem as a special case of a broader class of MDPs, where their transition dynamics decompose into a known component and an unknown but structured component.
We establish general results for this abstract setting, which may be of independent interest.

## One-Sentence Claim

Delayed state observations in tabular online RL admit a minimax-optimal UCB-style strategy with regret scaling as the square root of the maximum delay.

## Problem

In many sequential decision problems, actions must be chosen before the current state is observed. Random delays create a mismatch between the agent's decision time and information time, complicating exploration and regret analysis.

The paper studies tabular episodic MDPs with delayed state observation and asks for the optimal regret dependence on the maximum delay.

## Core Contribution

The paper proposes an algorithm combining state augmentation with upper confidence bounds and proves a regret bound of roughly O(H sqrt(D_max S A K)). It also proves a matching lower bound up to logarithmic factors, establishing minimax optimality.

Beyond the delayed-observation setting, the analysis frames the problem as a broader class of MDPs with transition dynamics decomposed into a known component and an unknown structured component.

## Method

The augmentation method turns delayed observations into an expanded Markovian state representation that includes enough history to reason about pending observations. UCB exploration then handles uncertainty in the unknown structured part of the transition dynamics.

The regret analysis separates known dynamics induced by delay structure from the unknown MDP component, enabling sharper dependence on delay than naive state expansion might suggest.

## Experiments and Evidence

Evidence reported in the abstract:

- Tabular MDP regret upper bound of approximately O(H sqrt(D_max S A K)).
- Matching lower bound up to logarithmic factors.
- General analytical framework for MDPs whose transition dynamics decompose into known and unknown structured components.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact delay model, hidden logarithmic terms, whether delays are observed, and constants in horizon dependence.

## Limits and Failure Modes

- The result is tabular; large-state or function-approximation settings may need new structure.
- Dependence on D_max can still be large when delays are long.
- Delay-model assumptions matter: adversarial, censored, or action-dependent delays may break the proof.
- Practical deployment may require memory and computation for augmented states.

## Deep Themes

**Latency is part of the environment.** Delayed observation changes what the agent can know, not just when it can update.

**Known structure can reduce regret.** The decomposition into known and unknown dynamics avoids treating the whole augmented process as opaque.

**Minimax results calibrate algorithmic ambition.** The lower bound shows the delay penalty is fundamental, not just an artifact of the method.

## Subthemes

- Delayed state observations.
- Augmented-state RL.
- UCB under structured transitions.
- Delay-dependent minimax regret.
- Known/unknown dynamics decomposition.

## Connections to Other Papers

Connects to T2PO, Mean-Expansion Q-Learning, Distributional IRL, and online decision-tree inference. It also links to broader test-time control papers because all reason under delayed, partial, or expensive feedback.

## Notes for Cross-Paper Synthesis

This paper contributes a latency-aware RL theme: when feedback is delayed, the statistically right algorithm explicitly models information timing instead of pretending observations arrive synchronously.
