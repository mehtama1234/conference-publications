# Initialization is Half the Battle: Generating Diverse Images from a Guidance Potential Posterior

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: zXJjT0slV7
- Authors: Xiang Li; Dianbo Liu; Kenji Kawaguchi
- Primary area: probabilistic_methods->monte_carlo_and_sampling_methods
- Keywords: Diffusion Model;Flow Matching;Diversity;stochastic;Langevin dynamics
- Source URL: https://openreview.net/forum?id=zXJjT0slV7
- PDF URL: https://openreview.net/pdf?id=zXJjT0slV7

## Abstract

Despite the remarkable fidelity of generative models, they frequently suffer from mode collapse. Existing strategies for enhancing diversity predominantly focus on intervening during the generation trajectory. We identify a critical oversight that the standard Gaussian initialization often causes trajectories to collapse into dominant modes because it is agnostic to the guidance potential landscape. In this work, we formulate selecting the initial noise from a *guidance potential posterior*, which effectively re-weights the prior towards diversity-rich regions. To sample from this distribution efficiently, we introduce *Diversity-inducing Initialization* (DivIn), which leverages Langevin dynamics to actively navigate the initialization landscape, steering initial noise away from collapsing regions while anchoring them to the valid data manifold. Our method serves as an inference-time diversity enhancement compatible with both diffusion and flow matching models. Extensive experiments show that DivIn exhibits a superior performance in both class-to-image and text-to-image scenarios. 
Furthermore, we highlight that as DivIn is orthogonal to trajectory-based methods, combining them significantly expands the diversity-quality Pareto frontier beyond what either achieves in isolation.

## One-Sentence Claim

DivIn improves diffusion and flow-matching diversity by sampling initial noise from a guidance-potential posterior rather than a guidance-agnostic Gaussian prior.

## Problem

Generative models can have high fidelity while suffering mode collapse. Most diversity interventions modify the generation trajectory after initialization.

The paper argues that this misses a key cause: standard Gaussian initialization can place trajectories in regions that collapse into dominant modes because it ignores the guidance potential landscape.

## Core Contribution

The paper formulates initial-noise selection as sampling from a guidance potential posterior that reweights the prior toward diversity-rich regions.

It proposes Diversity-inducing Initialization, DivIn, an inference-time method using Langevin dynamics to navigate the initialization landscape while staying anchored to the valid data manifold.

## Method

DivIn runs Langevin dynamics over initial noise, guided by the guidance-potential posterior. This steers samples away from collapsing regions and toward initial states likely to generate diverse outputs.

The method is compatible with diffusion and flow matching models and is orthogonal to trajectory-based diversity methods.

## Experiments and Evidence

The abstract reports superior performance in both class-to-image and text-to-image generation.

It also reports that combining DivIn with trajectory-based methods expands the diversity-quality Pareto frontier beyond either method alone.

## Limits and Failure Modes

Inference-time Langevin initialization adds sampling overhead and depends on the quality of the guidance potential. If the posterior overweights unusual regions, diversity may come at the cost of semantic alignment or quality.

Because this note is abstract-only, details still need checking: guidance-potential definition, Langevin schedule, compute cost, diversity metrics, quality metrics, and interactions with classifier-free guidance.

## Deep Themes

- Initialization as generative control: diversity can be decided before the denoising or flow trajectory begins.
- Posterior reweighting of noise: the prior can be adapted to the guidance landscape.
- Diversity-quality Pareto expansion: initialization and trajectory interventions are complementary.
- Inference-time generative steering: no retraining is needed to change sample coverage.

## Subthemes

- Guidance potential posterior.
- Langevin dynamics for initial noise.
- Mode-collapse avoidance.
- Diffusion and flow-matching compatibility.

## Connections to Other Papers

This connects to Reverse Flow Matching, Diffusion Flow Matching theory, and AGSM through controlled diffusion/flow generation.

It also relates to GoodDiffusion and PanoWorld-X because all intervene in generative dynamics to enforce a desired property: authorization, geometry, or diversity.

## Notes for Cross-Paper Synthesis

DivIn adds an initialization-control theme: generative behavior is shaped not only by model weights and trajectories, but by where sampling begins.
