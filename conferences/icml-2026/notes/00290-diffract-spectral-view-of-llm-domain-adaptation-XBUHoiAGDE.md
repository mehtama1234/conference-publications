# Diffract: Spectral View of LLM Domain Adaptation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: XBUHoiAGDE
- Authors: Nikita Borodin; Maria Krylova; Artem Zabolotnyi; Dmitry Aspisov; Egor Shikov; Nikita Tyuplyaev; Oleg Travkin; Roman Alferov; Dmitry Vinichenko
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;Continual Pre-Training;Singular Value Decomposition;Linear Mode Connectivity;Domain Knowledge
- Source URL: https://openreview.net/forum?id=XBUHoiAGDE
- PDF URL: https://openreview.net/pdf?id=XBUHoiAGDE

## Abstract

We study continual pre-training (CPT) as a mechanism for adapting general-purpose large language models to specialized domains: mathematics, instruction, code, and natural text. Using singular value decomposition of weight matrices, we find that CPT leaves singular value spectra largely invariant, with adaptation driven mainly by changes in singular vectors. An analysis of attention-head projection matrices reveals strong, domain-dependent **head heterogeneity**, which we exploit to define a head importance criterion: up to **60%** of head updates can be removed without measurable quality loss. Selectively rewinding low-importance heads to their pre-trained state improves benchmark accuracy by up to **4%** versus the fully trained baseline. Finally, we identify **domain connectivity**—linear interpolation between CPT checkpoints yields smooth domain-quality interpolation without notable degradation on either domain—and release Diffract, an open-source toolkit for scalable spectral analysis of billion-parameter models.

## One-Sentence Claim

Continual pretraining adapts LLMs mainly by rotating singular vectors rather than changing singular spectra, enabling head-level update pruning and smooth domain interpolation.

## Problem

Continual pretraining is widely used to adapt general LLMs to domains such as math, instruction, code, and natural text. But the weight-space mechanisms of adaptation remain unclear: which parts of the model change, which updates matter, and whether domains are connected or conflicting.

The paper asks for a scalable spectral lens on billion-parameter domain adaptation.

## Core Contribution

The paper studies CPT using singular value decomposition of weight matrices and finds that singular value spectra stay largely invariant, while singular vectors carry most adaptation. Attention-head projection matrices show strong domain-dependent head heterogeneity.

The authors use this to define a head-importance criterion: up to 60 percent of head updates can be removed without measurable quality loss. Selectively rewinding low-importance heads to the pretrained state improves benchmark accuracy by up to 4 percent. They also identify domain connectivity: linear interpolation between CPT checkpoints smoothly interpolates domain quality without notable degradation.

## Method

Diffract performs spectral analysis over CPT checkpoints. It decomposes weight matrices, tracks spectra and vector changes, measures head-level heterogeneity, and ranks attention-head updates by importance.

The intervention side removes or rewinds selected head updates and linearly interpolates between domain-adapted checkpoints to test connectivity.

## Experiments and Evidence

Evidence reported in the abstract:

- Domains: mathematics, instruction, code, and natural text.
- SVD analysis showing mostly invariant singular value spectra.
- Domain-dependent attention-head heterogeneity.
- Up to 60 percent of head updates removable without measurable quality loss.
- Selective low-importance head rewinding improves accuracy by up to 4 percent.
- Linear interpolation between CPT checkpoints yields smooth domain-quality interpolation.
- Open-source Diffract toolkit.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model sizes, domain datasets, head-importance formula, benchmark set, and interpolation protocol.

## Limits and Failure Modes

- Spectral invariance may vary by architecture, optimizer, training duration, or domain distance.
- Head update pruning could miss MLP or cross-layer adaptation mechanisms.
- Linear connectivity between studied domains may not hold for more conflicting domains.
- Accuracy improvements from rewinding need robustness checks across seeds and benchmarks.

## Deep Themes

**Adaptation can be rotational rather than spectral.** The important change is in singular directions, not singular magnitudes.

**Fine-tuning contains removable updates.** Head heterogeneity means many changes are not equally useful, and some can be undone.

**Domain checkpoints can form connected manifolds.** Smooth interpolation suggests domain adaptation may be more compositional than catastrophic.

## Subthemes

- SVD of LLM continual pretraining.
- Singular-vector domain adaptation.
- Attention-head heterogeneity.
- Selective head rewinding.
- Linear mode connectivity across domains.

## Connections to Other Papers

Connects to DiSC, MDA, Neuron-Basis Circuits, and continual VLA forgetting through retention and adaptation structure. It also links to PRISM, OCE, and representation-geometry papers where meaningful changes live in identifiable subspaces or directions.

## Notes for Cross-Paper Synthesis

Diffract adds spectral evidence for a major adaptation pattern: not all parameter updates are equally real. Some directions encode domain change, while others can be pruned, rewound, or interpolated without losing capability.
