# Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 951OAanYyQ
- Authors: Cameron Tice; Puria Radmard; Samuel Ratnam; Andy Kim; David Demitri Africa; Kyle O'Brien
- Primary area: deep_learning->large_language_models
- Keywords: alignment;pretraining;hyperstition;LLMs;safety;misalignment;data
- Source URL: https://openreview.net/forum?id=951OAanYyQ
- PDF URL: https://openreview.net/pdf?id=951OAanYyQ

## Abstract

Pretraining corpora contain extensive discourse about AI systems, yet the causal influence of this discourse on downstream alignment remains poorly understood. If prevailing descriptions of AI behaviour are predominantly negative, LLMs may internalise corresponding behavioural priors, giving rise to self-fulfilling misalignment. This paper provides the first controlled study of this hypothesis by pretraining 6.9B-parameter LLMs with varying amounts of (mis)alignment discourse. We find that discussion of AI contributes to misalignment. Upsampling synthetic training documents about AI misalignment leads to a notable increase in misaligned behaviour. Conversely, upsampling documents about aligned behaviour reduces misalignment scores from 45% to 9%. We consider this evidence of self-fulfilling alignment. These effects are dampened, but persist through post-training. Our findings establish the study of how pretraining data shapes alignment priors, or alignment pretraining, as a complement to post-training. We recommend practitioners pretrain for alignment as well as capabilities.

## One-Sentence Claim

AI discourse in pretraining data can causally shape alignment priors, with misalignment discourse increasing misaligned behavior and aligned-behavior discourse reducing it.

## Problem

Alignment research often focuses on post-training, but pretraining corpora contain extensive descriptions of AI behavior that may seed behavioral priors before alignment interventions begin.

## Core Contribution

The paper provides a controlled study of alignment pretraining by varying the amount and valence of AI behavior discourse in 6.9B-parameter LLM pretraining.

## Method

It upscales synthetic documents about AI misalignment or aligned behavior during pretraining, then measures downstream misalignment behavior before and after post-training.

## Experiments and Evidence

The abstract reports that upsampling misalignment discourse increases misaligned behavior, while upsampling aligned-behavior documents reduces misalignment scores from 45% to 9%; effects are dampened but persist after post-training.

## Limits and Failure Modes

ArXiv search failed with HTTP 503 for this batch, so this note is abstract-only. Details still need checking: synthetic discourse generation, misalignment metric, control corpora, post-training recipe, and generality beyond 6.9B-scale models.

## Deep Themes

- Alignment priors can be shaped during pretraining, not only post-training.
- Model behavior may reflect self-fulfilling narratives in training data.
- Data discourse can act as behavioral supervision even when not formatted as instruction data.

## Subthemes

- Alignment pretraining.
- Misalignment discourse.
- Pretraining data causality.
- Synthetic data upsampling.
- Post-training persistence.
- Behavioral priors.

## Connections to Other Papers

Connects to Midtraining, VALUEFLOW, DPO/RLHF equivalence, and alignment benchmark papers through the idea that data distributions and training phases shape behavior before explicit preference optimization.

## Notes for Cross-Paper Synthesis

This paper strengthens the pretraining-as-alignment theme: safety behavior may be partially determined by the narratives and examples absorbed during base-model formation.
