# Clustering in Deep Stochastic Transformers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: opfSL15Uc4
- Authors: Lev Fedorov; Michael Eli Sander; Romuald Elie; Pierre Marion; Mathieu Lauriere
- Primary area: deep_learning->theory
- Keywords: Transformers;Attention;Token Clustering;Deep neural networks;Diffusion limits;Phase transitions;Interacting Particle Systems;Stochastic Processes;Signal Propagation;Rank Collapse
- Source URL: https://openreview.net/forum?id=opfSL15Uc4
- PDF URL: https://openreview.net/pdf?id=opfSL15Uc4

## Abstract

Transformers have revolutionized deep learning across various domains but understanding the precise token dynamics remains a theoretical challenge. Existing theories of deep Transformers with layer normalization typically predict that tokens cluster to a single point; however, these results rely on deterministic weight assumptions, which fail to capture the standard initialization scheme in Transformers.
In this work, we show that accounting for the intrinsic stochasticity of random initialization alters this picture. More precisely, we analyze deep Transformers where noise arises from the random initialization of value matrices. Under diffusion scaling and token-wise RMS normalization, we prove that, as the number of Transformer layers goes to infinity, the discrete token dynamics converge to an interacting-particle system on the sphere where tokens are driven by a *common* matrix-valued Brownian noise. In this limit, we show that initialization noise prevents the collapse to a single cluster predicted by deterministic models. For two tokens, we prove a phase transition governed by the interaction strength and the token dimension: unlike deterministic attention flows, antipodal configurations become attracting with positive probability. Numerical experiments confirm the predicted transition, reveal that antipodal formations persist for more than two tokens, and demonstrate that suppressing the intrinsic noise degrades accuracy.

## One-Sentence Claim

Accounting for random-initialization noise changes deep Transformer token dynamics from deterministic single-cluster collapse to stochastic interacting-particle behavior with multi-cluster and antipodal attractors.

## Problem

Transformer theory has tried to explain how tokens evolve across very deep stacks, often predicting that layer-normalized tokens collapse to a single cluster. But these deterministic analyses neglect intrinsic stochasticity from standard random initialization, which may be central to actual Transformer behavior.

The problem is to build a deep-limit theory that captures random value-matrix initialization and explains whether token clustering, rank collapse, or persistent diversity should be expected.

## Core Contribution

The paper proves that, under diffusion scaling and token-wise RMS normalization, deep stochastic Transformer token dynamics converge to an interacting-particle system on the sphere driven by common matrix-valued Brownian noise.

This stochastic limit changes the qualitative picture: initialization noise prevents deterministic collapse to one cluster. For two tokens, the authors prove a phase transition governed by interaction strength and token dimension, with antipodal configurations becoming attracting with positive probability.

## Method

The analysis models randomness from value-matrix initialization and studies the infinite-depth limit under diffusion scaling. Token-wise RMS normalization constrains token states to spherical geometry, and the resulting continuous-time limit becomes an interacting stochastic particle system.

The authors then analyze two-token dynamics to prove the phase transition, and use numerical experiments to test whether predicted behavior extends to more tokens and affects model accuracy.

## Experiments and Evidence

The theoretical evidence is the convergence proof to the stochastic particle system and the phase-transition result for two tokens. Numerical experiments confirm the transition, show that antipodal formations persist with more than two tokens, and report that suppressing intrinsic noise degrades accuracy.

Full-paper reading should inspect assumptions on attention form, normalization, scaling, random matrix distribution, and how noise suppression experiments map to practical Transformer training.

## Limits and Failure Modes

Infinite-depth diffusion limits are approximations, and real Transformers include residual streams, MLP blocks, trained weights, positional encodings, causal masking, and non-random learned structure. The theory may capture a specific initialization or early-training regime more directly than fully trained LLM behavior.

The accuracy-degradation result from suppressing noise is suggestive, but its implications for architecture design or initialization practice require careful scope control.

## Deep Themes

- Stochasticity as structure: initialization noise is not a nuisance but a driver of token geometry.
- Token dynamics through particle systems: deep Transformers can be studied as interacting stochastic processes.
- Collapse prevention by noise: randomness can preserve representational diversity.
- Phase transitions in representation geometry: attention dynamics can switch attractor regimes with dimension and interaction strength.

## Subthemes

- Deterministic Transformer theories may overpredict rank collapse.
- RMS normalization induces spherical token geometry.
- Common Brownian noise creates correlated token movement.
- Antipodal configurations suggest richer clustering than single-point collapse.

## Connections to Other Papers

This paper connects to concept-binding, scaling-law origin, and mHC/manifold-connection work through representation geometry. It also relates to reasoning-loop work: both explain macroscopic Transformer behavior through low-level dynamics and inductive biases.

In the broader corpus, it is another example of theory correcting an oversimplified engineering intuition: deterministic collapse is not the whole story when stochastic initialization is modeled.

## Notes for Cross-Paper Synthesis

The synthesis theme is that stochastic and geometric details matter for interpreting Transformer behavior. Several papers are converging on the idea that emergent model properties depend on dynamics, parameterization, normalization, and noise, not just architecture diagrams.
