# Temporal Sparse Autoencoders: Leveraging the Sequential Nature of Language for Interpretability

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: bojVI4l9Kn
- Authors: Usha Bhalla; Alex Oesterling; Claudio Mayrink Verdun; Himabindu Lakkaraju; Flavio Calmon
- Primary area: interpretability and explainable AI
- Keywords: Interpretability;Dictionary Learning;Machine Learning;Large Language Models
- Source URL: https://openreview.net/forum?id=bojVI4l9Kn
- PDF URL: https://openreview.net/pdf?id=bojVI4l9Kn

## Abstract

Translating the internal representations and computations of models into concepts that humans can understand is a key goal of interpretability. While recent dictionary learning methods such as Sparse Autoencoders (SAEs) provide a promising route to discover human-interpretable features, they often only recover token-specific, noisy, or highly local concepts. We argue that this limitation stems from neglecting the temporal structure of language, where semantic content typically evolves smoothly over sequences. Building on this insight, we introduce Temporal Sparse Autoencoders (T-SAEs), which incorporate a novel contrastive loss encouraging consistent activations of high-level features over adjacent tokens. This simple yet powerful modification enables SAEs to disentangle semantic from syntactic features in a self-supervised manner. Across multiple datasets and models, T-SAEs recover smoother, more coherent semantic concepts without sacrificing reconstruction quality. Strikingly, they exhibit clear semantic structure despite being trained without explicit semantic signal, offering a new pathway for unsupervised interpretability in language models.

## One-Sentence Claim

Temporal Sparse Autoencoders add adjacent-token contrastive consistency to SAEs, recovering smoother semantic features while preserving reconstruction quality.

## Problem

Sparse autoencoders can discover interpretable features in language models, but standard dictionary learning often yields noisy, token-local, or syntactic features.

This misses the temporal structure of language, where semantic content typically evolves smoothly over nearby tokens.

## Core Contribution

The paper introduces T-SAEs, a temporal variant of sparse autoencoders.

Its key change is a contrastive loss that encourages consistent activation of high-level features over adjacent tokens, helping disentangle semantic and syntactic features without explicit semantic labels.

## Method

T-SAEs train like ordinary SAEs but add temporal contrastive pressure over neighboring token activations.

The loss favors features that persist coherently across local sequence contexts while maintaining the sparse reconstruction objective.

## Experiments and Evidence

The abstract reports experiments across multiple datasets and models.

T-SAEs recover smoother, more coherent semantic concepts without sacrificing reconstruction quality and show clear semantic structure despite self-supervised training.

## Limits and Failure Modes

Temporal smoothness may suppress sharp semantic transitions, rare tokens, code syntax, or discourse markers where meaning changes abruptly. Coherence metrics may also overvalue broad features.

Because this note is abstract-only, details still need checking: contrastive objective, adjacency window, model layers, datasets, interpretability metrics, and examples of semantic/syntactic separation.

## Deep Themes

- Temporal structure for interpretability: language features should respect sequence continuity.
- Semantic-syntactic disentanglement: contrastive consistency separates high-level meaning from local form.
- Self-supervised concept discovery: interpretable features emerge without semantic labels.
- Reconstruction-preserving feature shaping: interpretability improves without losing SAE fidelity.

## Subthemes

- Sparse autoencoders.
- Dictionary learning.
- Temporal contrastive loss.
- Semantic feature smoothness.

## Connections to Other Papers

This connects to Neural Effect Search, latent vector fields, DAVE, and SAE-based data synthesis.

It also relates to Hubble and LLM DNA because interpretable features can support memorization and model-provenance diagnostics.

## Notes for Cross-Paper Synthesis

T-SAEs add an interpretability theme: sparse features become more meaningful when the learning objective respects the temporal structure of language.
