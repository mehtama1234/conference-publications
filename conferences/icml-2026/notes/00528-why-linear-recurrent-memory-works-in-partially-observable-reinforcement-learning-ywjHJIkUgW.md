# Why Linear Recurrent Memory Works in Partially Observable Reinforcement Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ywjHJIkUgW
- Authors: Yike Zhao; Onno Eberhard; Malek khammassi; Ali H. Sayed; Michael Muehlebach
- Primary area: theory->reinforcement_learning_and_planning
- Keywords: Partially Observable Reinforcement Learning;Linear RNNs;Hidden Markov Model
- Source URL: https://openreview.net/forum?id=ywjHJIkUgW
- PDF URL: https://openreview.net/pdf?id=ywjHJIkUgW

## Abstract

The family of linear recurrent neural networks has shown strong performance as recurrent memory units in partially observable reinforcement learning. We provide a theoretical justification for their empirical effectiveness by constructing and studying two linear filters:
(i) the first exactly reproduces the pre–softmax logits of the belief vector in a hidden Markov model (HMM) under a deterministic transition matrix, thereby serving as a sufficient statistic for optimal policy learning, (ii) the second achieves vanishing state-decoding error under a nearly deterministic transition matrix, thus reducing state ambiguity to near zero. The results extend to action-controlled HMMs, where the corresponding linear filters become time-varying with action-dependent dynamics. We illustrate our main results through numerical experiments and further show that the constructed linear filter serves as a strong feature extractor in a small reinforcement learning game.

## One-Sentence Claim

Linear recurrent memory works in partially observable RL because suitable linear filters can recover belief-logit sufficient statistics or nearly eliminate state ambiguity in HMM-like environments.

## Problem

Partially observable RL requires memory because observations do not fully reveal the underlying state. Linear recurrent networks have performed well empirically as memory units, but their theoretical role has been unclear.

The problem is to explain when simple linear recurrence can support optimal or near-optimal policy learning despite hidden state uncertainty.

## Core Contribution

The paper constructs two linear filters for hidden Markov models. One exactly reproduces pre-softmax logits of the belief vector under deterministic transitions, giving a sufficient statistic for optimal policy learning.

The second achieves vanishing state-decoding error under nearly deterministic transitions, reducing ambiguity close to zero. The results extend to action-controlled HMMs via time-varying action-dependent filters.

## Method

The analysis studies linear filters as recurrent memory mechanisms in HMMs. Under deterministic transition structure, a linear recurrence can represent the belief-logit information needed for decision making.

For nearly deterministic transitions, the filter supports state decoding with error that vanishes under the stated conditions. In action-controlled HMMs, the filter dynamics depend on the chosen actions.

## Experiments and Evidence

The abstract reports numerical experiments illustrating the theoretical results.

It also reports that the constructed linear filter acts as a strong feature extractor in a small reinforcement-learning game.

## Limits and Failure Modes

The guarantees rely on deterministic or nearly deterministic transition structure. More stochastic, aliased, or non-HMM environments may require nonlinear memory or richer state estimators.

Because this note is abstract-only, details still need checking: exact HMM assumptions, convergence rates, observation model, action-controlled extension, game setup, and comparison to learned recurrent baselines.

## Deep Themes

- Memory as belief filtering: recurrent state can approximate sufficient statistics for hidden state.
- Linear recurrence can be enough under structure: nonlinearity is not always necessary for memory.
- Partial observability and state ambiguity: memory quality is measured by ambiguity reduction.
- Action-dependent memory dynamics: control changes the filtering problem.

## Subthemes

- HMM belief-logit recovery.
- Nearly deterministic transitions.
- Linear RNN feature extraction.
- Time-varying filters in controlled HMMs.

## Connections to Other Papers

This connects to POPGym memory diagnostics, LAMP, path-dependent amortized inference, and temporal graph memory explanation through the question of what history must be retained.

It also relates to VectorWorld and control papers because hidden state estimation is central to policy evaluation under partial observability.

## Notes for Cross-Paper Synthesis

This paper adds a theoretical memory subtheme: useful recurrent memory can be simple when the environment dynamics make the right sufficient statistic linearly recoverable.
