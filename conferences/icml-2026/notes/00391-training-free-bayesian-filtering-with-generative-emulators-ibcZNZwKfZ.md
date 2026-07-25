# Training-Free Bayesian Filtering with Generative Emulators

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ibcZNZwKfZ
- Authors: Thomas Savary; François Rozet; Gilles Louppe
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Filtering;Data Assimilation;Particle Filters;Generative models;Diffusion
- Source URL: https://openreview.net/forum?id=ibcZNZwKfZ
- PDF URL: https://openreview.net/pdf?id=ibcZNZwKfZ

## Abstract

Bayesian filtering is a well-known problem that aims to estimate plausible states of a dynamical system from observations. Among existing approaches to solve this problem, particle filters are theoretically exact for non-linear dynamics and observations, but suffer from poor scalability in high dimensions. In this work, we show that diffusion-based emulators of dynamical systems can be used to implement, without additional training, an optimal variant of particle filters that has remained largely unexplored due to implementation challenges with classical numerical solvers. Experiments on nonlinear chaotic systems, including atmospheric dynamics, demonstrate that the proposed approach successfully scales particle filtering to high-dimensional settings.

## One-Sentence Claim

Diffusion-based dynamical-system emulators can implement an optimal particle-filter variant without additional training, scaling Bayesian filtering to high-dimensional nonlinear systems.

## Problem

Bayesian filtering estimates plausible latent states of a dynamical system from observations. Particle filters are theoretically exact for nonlinear dynamics and observations, but they suffer from particle degeneracy and poor scalability in high-dimensional state spaces.

The paper asks whether generative emulators of dynamical systems can make a previously impractical optimal particle-filter variant implementable.

## Core Contribution

The core contribution is a training-free filtering method that uses diffusion-based emulators as components of an optimal particle-filter variant. The method does not require retraining the emulator for filtering.

The key claim is that generative emulators overcome implementation challenges that made this variant largely unexplored with classical numerical solvers, enabling high-dimensional particle filtering.

## Method

The method uses a pretrained diffusion emulator of system dynamics to generate or transform state particles in a way compatible with Bayesian filtering. Because the emulator models the dynamical transition distribution, it can support proposal or transport steps that are difficult to implement with traditional solvers.

The filtering procedure then assimilates observations while using the generative emulator to maintain plausible state ensembles.

## Experiments and Evidence

Evidence reported in the abstract:

- Nonlinear chaotic-system experiments.
- Atmospheric dynamics included as a test domain.
- Successful scaling of particle filtering to high-dimensional settings.
- No additional training required beyond the generative emulator.
- Implementation of an optimal particle-filter variant previously limited by solver challenges.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: filtering variant, emulator training assumptions, observation models, and comparison to ensemble Kalman or sequential Monte Carlo baselines.

## Limits and Failure Modes

- Filtering quality depends on emulator fidelity under rollout and observation-conditioning regimes.
- Training-free filtering still requires a trained emulator, which may be expensive or biased.
- Chaotic systems can amplify emulator errors over time.
- High-dimensional particle diversity may remain challenging under sharp likelihoods.

## Deep Themes

**Generative models become inference operators.** The diffusion emulator is not only a simulator but a component of Bayesian filtering.

**Training-free adaptation reuses learned dynamics.** A pretrained emulator can support new assimilation tasks without extra fitting.

**Scientific inference is moving beyond forward prediction.** The goal is posterior state estimation under observations.

## Subthemes

- Bayesian filtering.
- Diffusion dynamical emulators.
- Particle filters in high dimensions.
- Data assimilation.
- Training-free generative inference.

## Connections to Other Papers

Connects to DiScoFormer, Distribution Transformers, LASER, NeuronCtrl, and RMT diffusion consistency. It fits the probabilistic/scientific theme where generative models serve as reusable inference machinery.

## Notes for Cross-Paper Synthesis

This paper extends the "Transformer/generative model as statistical operator" theme into dynamical data assimilation: pretrained generative dynamics can power Bayesian updates, not just sample forecasts.
