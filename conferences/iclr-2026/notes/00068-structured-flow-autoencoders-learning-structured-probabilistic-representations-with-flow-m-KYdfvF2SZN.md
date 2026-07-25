# Structured Flow Autoencoders: Learning Structured Probabilistic Representations with Flow Matching

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: KYdfvF2SZN
- Authors: Yidan Xu; Yixin Wang; XuanLong Nguyen
- Primary area: probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)
- Keywords: Flow Matching;Probabilistic Model;Representation Learning;Probabilistic Graphical Model;Autoencoder
- Source URL: https://openreview.net/forum?id=KYdfvF2SZN
- PDF URL: https://openreview.net/pdf?id=KYdfvF2SZN

## Abstract

Flow matching has proven to be a powerful density estimator, yet it often fails to explicitly capture the rich inherent latent structure of complex data. To address this limitation, we introduce Structured Flow Autoencoders (SFA), a family of probabilistic models that augments Continuous Normalizing Flows (CNFs) with graphical models. At the core of SFA is a novel flow matching based objective, which explicitly accounts for latent variables, enabling simultaneous learning of likelihood and posterior. We demonstrate the versatility of SFA across settings, including models with continuous and mixture latent variables, as well as latent dynamical systems. Empirical studies show that SFA outperforms Variational Autoencoders (VAE) and their graphical model extensions, achieving better data fit while simultaneously retaining meaningful latent variables as structured representations.

## One-Sentence Claim

Structured Flow Autoencoders augment continuous normalizing flows with graphical latent-variable structure so flow matching can learn both likelihoods and meaningful posteriors.

## Problem

Flow matching is a strong density-estimation framework, but generic flow models may not expose the latent structure that matters for interpretation, downstream reasoning, or temporal dynamics.

VAEs and graphical model extensions provide structured representations, but can lag in data fit. The paper targets this gap between expressive density modeling and explicit probabilistic representation learning.

## Core Contribution

The paper introduces Structured Flow Autoencoders, a family of probabilistic models that combine CNFs with graphical models.

Its central technical contribution is a flow-matching objective that explicitly accounts for latent variables, enabling simultaneous learning of likelihood and posterior.

## Method

SFA places structured latent variables inside a flow-matching framework. The graphical model component represents latent dependencies, while the CNF/flow-matching component models continuous transformations for data likelihood.

The framework is presented as flexible enough for continuous latents, mixture latents, and latent dynamical systems.

## Experiments and Evidence

The abstract reports empirical comparisons across multiple settings.

SFA outperforms VAEs and graphical-model VAE extensions in data fit while retaining meaningful structured latent variables.

## Limits and Failure Modes

Combining flows with graphical latent structure can introduce optimization and inference complexity. Meaningful latents may also depend on whether the chosen graph structure matches the data-generating process.

Because this note is abstract-only, details still need checking: exact objective derivation, posterior parameterization, graph assumptions, datasets, likelihood metrics, and whether latent interpretability is quantitatively evaluated.

## Deep Themes

- Density estimation with explicit structure: likelihood modeling and representation learning are treated as joint goals.
- Probabilistic latents inside generative flows: flow matching becomes a vehicle for posterior learning, not only sample generation.
- Graphical-model revival: structured probabilistic assumptions are being recombined with modern continuous generative methods.
- Representation interpretability: useful generative models should expose meaningful latent variables.

## Subthemes

- Continuous normalizing flows.
- Flow matching with latent variables.
- Graphical model autoencoders.
- Latent dynamical systems.

## Connections to Other Papers

This connects to DFM Bounds and other flow/diffusion theory papers through attempts to put stronger mathematical structure underneath generative modeling.

It also relates to InfoTok and representation-geometry papers because all ask how latent or token representations should preserve the structure of the underlying data.

## Notes for Cross-Paper Synthesis

SFA adds to a recurring 2026 theme: generative models are being pushed to produce structured, inspectable intermediate representations rather than only high-quality samples.
