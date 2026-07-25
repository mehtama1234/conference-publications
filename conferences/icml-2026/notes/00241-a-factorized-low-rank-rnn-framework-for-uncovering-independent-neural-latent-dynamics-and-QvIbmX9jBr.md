# A Factorized Low-Rank RNN Framework for Uncovering Independent Neural Latent Dynamics and Connectivity

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: QvIbmX9jBr
- Authors: Chengrui Li; Yunmiao Wang; Yule Wang; Weihan Li; Dieter Jaeger; Anqi Wu
- Primary area: applications->neuroscience_cognitive_science
- Keywords: low-rank RNN;independent neural latent subspace;neural latent dynamics;neural connectivity
- Source URL: https://openreview.net/forum?id=QvIbmX9jBr
- PDF URL: https://openreview.net/pdf?id=QvIbmX9jBr

## Abstract

Low-rank recurrent neural networks (lrRNNs) are a class of models that uncover low-dimensional latent dynamics underlying neural population activity. Although their functional connectivity is low-rank, it lacks independence interpretations, making it difficult to assign distinct computational roles to different latent dimensions. To address this, we propose the Factored Recurrent Neural Network (FacRNN), a generative lrRNN framework that assumes group-wise independence among latent dynamics while allowing flexible within-group entanglement. These independent latent groups allow latent dynamics to evolve separately, but are internally rich for complex computation. We reformulate the lrRNN under a variational autoencoder (VAE) framework, enabling us to introduce a partial correlation penalty that encourages independence between groups of latent dimensions. Experiments on synthetic, monkey M1, and mouse voltage imaging data show that FacRNN consistently improves the disentanglement and interpretability of learned neural latent trajectories in low-dimensional space and low-rank connectivity over baseline lrRNNs that do not encourage group-wise independence.

## One-Sentence Claim

FacRNN discovers more interpretable neural population dynamics by factorizing low-rank RNN latents into group-wise independent subspaces with flexible within-group computation.

## Problem

Low-rank RNNs reveal low-dimensional neural dynamics, but their low-rank connectivity lacks independence interpretation, making it hard to assign computational roles to latent dimensions.

## Core Contribution

The paper introduces a generative VAE-style low-rank RNN framework with group-wise latent independence encouraged by a partial-correlation penalty.

## Method

FacRNN reformulates lrRNNs as a VAE, partitions latent dimensions into groups, penalizes partial correlations between groups to encourage independent dynamics, and preserves richer entanglement within each group.

## Experiments and Evidence

The abstract reports improved disentanglement and interpretability of neural latent trajectories and low-rank connectivity over baseline lrRNNs on synthetic data, monkey M1 recordings, and mouse voltage imaging.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: neural datasets, latent group selection, partial-correlation tuning, VAE likelihood assumptions, biological validation, and scalability to larger populations.

## Deep Themes

- Neuroscience models need interpretable latent subspaces, not just low-dimensional fits.
- Independence constraints can expose computational roles in neural dynamics.
- Generative sequence models bridge representation learning and connectivity analysis.

## Subthemes

- Low-rank RNNs.
- Neural population dynamics.
- Latent disentanglement.
- VAE.
- Partial correlation.
- Motor cortex and voltage imaging.

## Connections to Other Papers

Connects to Real-World Unsupervised Models, AI Engram, and NeuroAI papers through biologically grounded representation analysis and interpretable neural dynamics.

## Notes for Cross-Paper Synthesis

FacRNN adds a neuroscience-specific disentanglement theme: the goal is not only predicting neural activity but assigning distinct computational roles to latent dynamical groups.
