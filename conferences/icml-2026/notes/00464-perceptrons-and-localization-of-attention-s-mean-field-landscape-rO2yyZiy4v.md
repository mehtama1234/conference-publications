# Perceptrons and Localization of Attention’s Mean-Field Landscape

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: rO2yyZiy4v
- Authors: Antonio Álvarez-López; Borjan Geshkovski; Domènec Ruiz-Balet
- Primary area: theory->deep_learning
- Keywords: Transformers;Self-attention dynamics;Mean-field limit;Interacting particle systems;Wasserstein gradient flows;Optimal transport;Feed-forward networks;Stationary equilibria
- Source URL: https://openreview.net/forum?id=rO2yyZiy4v
- PDF URL: https://openreview.net/pdf?id=rO2yyZiy4v

## Abstract

The forward pass of a Transformer can be seen as an interacting particle system on the unit sphere: time plays the role of layers, particles that of token embeddings, and the unit sphere idealizes layer normalization. In some weight settings the system can even be seen as a gradient flow for an explicit energy, and one can  make sense of the infinite context length *mean-field* limit thanks to Wasserstein gradient flows. In this paper we study the effect of the perceptron block in this setting, and show that critical points are generically atomic and localized on subsets of the sphere.

## One-Sentence Claim

In a mean-field view of Transformer forward passes as particle dynamics on the sphere, adding perceptron blocks generically localizes critical points into atomic subsets.

## Problem

Transformer forward dynamics can be modeled as interacting particles, with layers as time and token embeddings as particles on the unit sphere. Existing attention-flow theories study how tokens move and cluster, but feed-forward/perceptron blocks are also central to real Transformer layers.

The open theoretical question is how perceptron blocks alter the mean-field landscape of attention dynamics, especially in the infinite-context limit.

## Core Contribution

The paper studies the effect of the perceptron block in the interacting-particle/mean-field formulation of self-attention. It shows that critical points are generically atomic and localized on subsets of the sphere.

This contribution adds feed-forward network effects to a geometric and optimal-transport view of Transformer dynamics, refining theories that treat attention alone as the main driver.

## Method

The theoretical setup views token embeddings as particles on the unit sphere, with layer normalization idealized by spherical constraints. In certain weight regimes, the system becomes a gradient flow for an explicit energy.

The infinite-context mean-field limit is analyzed through Wasserstein gradient flows. The perceptron block is incorporated into this landscape, and the authors characterize the resulting stationary equilibria.

## Experiments and Evidence

The abstract presents a theoretical result: critical points are generically atomic and localized on subsets of the sphere. No empirical evidence is described in the abstract.

Full-paper reading should verify the exact assumptions on attention weights, perceptron form, activation functions, normalization, and the mathematical meaning of generic atomic localization.

## Limits and Failure Modes

The model is an abstraction of Transformer forward passes. Real LLMs include residual streams, causal masks, positional encodings, trained non-random weights, multi-head attention, and finite depth/context.

The practical interpretation of localized atomic equilibria is not immediate. The result may inform theory of token clustering or representation collapse, but connecting it to training or downstream behavior requires further work.

## Deep Themes

- Transformer dynamics as particle systems: token representations evolve under geometric flows.
- Mean-field limits for long context: infinite-context analysis uses optimal transport tools.
- Feed-forward blocks shape attention landscapes: perceptrons are not passive additions.
- Localization of equilibria: deep representation dynamics may concentrate on spherical subsets.

## Subthemes

- Layer normalization motivates spherical geometry.
- Wasserstein gradient flows provide a language for infinite-token limits.
- Atomic critical points connect to clustering and representation collapse.
- Attention-only theories miss the effect of MLP/perceptron components.

## Connections to Other Papers

This paper connects to stochastic Transformer clustering, scaling-law origin, and non-Euclidean edge-of-stability work. All use mathematical dynamics to explain behavior that empirical deep learning often treats descriptively.

It also relates to representation-geometry papers because token localization and clustering define the geometry of internal features.

## Notes for Cross-Paper Synthesis

The synthesis point is that Transformer theory is becoming more dynamical and geometric. Layers, tokens, normalization, noise, and perceptrons are being modeled as parts of an interacting system rather than a stack of black-box modules.
