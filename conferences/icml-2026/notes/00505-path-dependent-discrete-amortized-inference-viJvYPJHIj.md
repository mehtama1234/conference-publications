# Path-dependent Discrete Amortized Inference

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: viJvYPJHIj
- Authors: Tiago Silva; Esmeralda S. Whitammer; Salem Lahlou
- Primary area: probabilistic_methods->monte_carlo_and_sampling_methods
- Keywords: GFlowNets;Amortized Sampling
- Source URL: https://openreview.net/forum?id=viJvYPJHIj
- PDF URL: https://openreview.net/pdf?id=viJvYPJHIj

## Abstract

We consider the problem of sampling compositional and discrete objects from a given unnormalized posterior distribution. 
Notably, recent studies have shown that this problem can be efficiently solved by learning a deterministic Markov Decision Process (MDP) that progressively builds each object in proportion to the posterior.
In this work, however, we demonstrate that the Markovian assumption can both hamper signal propagation during training and catastrophically reduce the learned sampler's expressivity due to state aliasing. 
To address these issues, we propose lifting the MDP with a learnable latent dynamics that allows the underlying policy to depend on the entire past trajectory---and not only on the current state. 
In view of this, we refer to the resulting method as \emph{path-dependent discrete amortized inference}. 
Importantly, we provably extend existing learning algorithms for amortized samplers to our setting. 
In experiments on standard benchmark problems, we also show that our approach often leads to faster learning convergence and improved state space exploration relatively to prior techniques.

## One-Sentence Claim

Path-dependent discrete amortized inference improves GFlowNet-style sampling by lifting the construction MDP with latent dynamics so policies can depend on full trajectories rather than aliased current states.

## Problem

Discrete amortized samplers learn policies that progressively build compositional objects in proportion to an unnormalized posterior. Many formulations use deterministic Markov decision processes where action choice depends only on the current partially built state.

The paper argues this Markov assumption can hamper training signal propagation and catastrophically reduce expressivity through state aliasing: different histories can lead to the same state but require different future behavior.

## Core Contribution

The paper proposes path-dependent discrete amortized inference by lifting the MDP with learnable latent dynamics. The policy can condition on the whole past trajectory, not only the current state.

It also provably extends existing learning algorithms for amortized samplers to the path-dependent setting and shows faster convergence and better exploration in benchmark experiments.

## Method

The lifted process augments the visible construction state with latent history-dependent dynamics. This latent state disambiguates aliased states and carries training signal across the construction trajectory.

Existing objectives for amortized samplers, including GFlowNet-style learning, are generalized so that flows or policies can depend on path history while still targeting the intended posterior over completed objects.

## Experiments and Evidence

The abstract reports experiments on standard benchmark problems where path dependence often improves learning convergence and state-space exploration relative to prior Markovian techniques.

Full-paper reading should verify benchmark tasks, posterior targets, latent dynamics parameterization, algorithmic guarantees, and whether path dependence increases variance or memory cost.

## Limits and Failure Modes

Path dependence adds state and modeling complexity. If the latent dynamics memorize construction quirks instead of useful history, generalization to new posterior modes may suffer.

The approach is most relevant when state aliasing is significant. In problems where the current state is sufficient, Markovian samplers may be simpler and more stable.

## Deep Themes

- Non-Markovian amortized sampling: history can be essential for expressive discrete generation.
- State aliasing as sampler bottleneck: identical visible states can hide different construction histories.
- Latent dynamics for posterior exploration: learned memory improves signal propagation and mode discovery.
- GFlowNet generalization: flow-style samplers can be extended beyond deterministic Markov construction.

## Subthemes

- Compositional objects often have path-dependent construction semantics.
- Training signal propagation can fail under Markov abstraction.
- Latent history state trades memory cost for expressivity.
- Exploration quality is a key sampler metric, not only final likelihood.

## Connections to Other Papers

This paper connects to insertion-based generation, HSR, POPGym memory diagnostics, and LatentMAS through path, memory, and construction history. It also relates to probabilistic inference papers such as MIRA and Bayesian hypergraphs.

It strengthens the theme that Markov simplifications can be convenient but harmful when history contains necessary information.

## Notes for Cross-Paper Synthesis

The synthesis point is that construction history is often part of the object. In discrete generation and inference, ignoring path dependence can erase signal needed for efficient sampling.
