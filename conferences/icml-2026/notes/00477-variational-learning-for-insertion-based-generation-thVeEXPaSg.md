# Variational Learning for Insertion-based Generation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: thVeEXPaSg
- Authors: Yangtian Zhang; Zhe Wang; Arthur Gretton; Rex Ying; David van Dijk; Michalis Titsias; Jiaxin Shi
- Primary area: probabilistic_methods->variational_inference
- Keywords: Generative Modeling;Variational Inference;Discrete Diffusion;Autoregressive Model;Molecule Generation
- Source URL: https://openreview.net/forum?id=thVeEXPaSg
- PDF URL: https://openreview.net/pdf?id=thVeEXPaSg

## Abstract

Non-monotonic sequence generation methods, such as masked diffusion models, provide a flexible alternative to left-to-right autoregressive modeling by allowing tokens to be generated in non-fixed and prescribed orders. Despite their practical advantages, most existing non-monotonic models are order-agnostic and rely on a fixed-length grid, limiting their ability to support variable-length generation and adaptive insertion order. In this work, we introduce a probabilistic framework for learning insertion order in variable-length insertion models. We formalize a bijective correspondence between insertion trajectories and permutations, which enables an exact reparameterization of the data likelihood as a sum over permutations. Building on this result, we propose the Insertion Process (IP), a stochastic generative model that jointly learns where to insert, what to insert, and when to terminate, trained via permutation-based variational inference. Unlike prior fixed-canvas approaches, IP natively supports variable-length generation and learns data-driven preferences over insertion orders. Experiments on goal-conditioned planning and molecular string generation demonstrate that learning insertion order improves both modeling quality and generalization in domains without a canonical left-to-right structure.

## One-Sentence Claim

Insertion Process models learn where, what, and when to insert by treating insertion trajectories as permutations and optimizing variable-length generation with permutation-based variational inference.

## Problem

Non-monotonic generation methods such as masked diffusion avoid strict left-to-right order, but many are order-agnostic and rely on fixed-length grids. That limits variable-length generation and prevents the model from learning domain-specific insertion order.

Many domains, including planning and molecular strings, do not have a canonical left-to-right construction. A model should be able to learn adaptive insertion trajectories rather than impose a fixed canvas or order.

## Core Contribution

The paper formalizes a bijective correspondence between insertion trajectories and permutations, allowing the data likelihood to be exactly reparameterized as a sum over permutations.

Building on this, it proposes the Insertion Process, a stochastic generative model that jointly learns insertion location, inserted content, and termination. Training uses permutation-based variational inference.

## Method

Insertion trajectories are represented as permutations over construction order. This turns the latent order of generation into an explicit probabilistic object that can be inferred and optimized.

The Insertion Process sequentially decides where to insert, what token or element to insert, and when to stop, supporting variable-length outputs natively. A variational objective approximates the permutation-summed likelihood.

## Experiments and Evidence

The abstract reports experiments on goal-conditioned planning and molecular string generation. Learning insertion order improves modeling quality and generalization in domains without canonical left-to-right structure.

Full-paper reading should verify likelihood estimators, variational bounds, termination modeling, generation speed, molecular validity metrics, and comparisons against fixed-canvas diffusion or autoregressive baselines.

## Limits and Failure Modes

Summing over permutations is combinatorially difficult, so variational approximation quality matters. Poor variational distributions could bias learned insertion orders.

Insertion generation may also be harder to deploy efficiently than standard autoregression if dynamic insertion operations create irregular batching or complex decoding state.

## Deep Themes

- Generation order as a latent variable: sequence construction need not follow the observed token order.
- Variable-length non-monotonic generation: insertion avoids fixed grids while preserving flexible ordering.
- Variational inference for discrete construction paths: permutations become latent trajectories.
- Domain-aligned generation protocols: planning and molecules benefit when construction order matches task structure.

## Subthemes

- Where/what/when decisions jointly define insertion generation.
- Non-canonical domains expose AR order bias.
- Termination is part of the generative process.
- Molecular strings provide a testbed for order-flexible generation.

## Connections to Other Papers

This paper connects to any-order GPT, XDLM, and diffusion language work through alternatives to left-to-right generation. It also relates to FIDIA and molecular design through scientific sequence generation.

It fits the broader inference-protocol alignment theme: the model should learn the construction process appropriate to the object rather than inherit a default ordering.

## Notes for Cross-Paper Synthesis

The synthesis point is that order is an inductive bias. Across language, molecules, and planning, papers are treating generation order as something to learn, optimize, or decouple from architecture.
