# Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: AQZZWVp6XA
- Authors: Arnas Uselis; Andrea Dittadi; Seong Joon Oh
- Primary area: general_machine_learning
- Keywords: compositionality
- Source URL: https://openreview.net/forum?id=AQZZWVp6XA
- PDF URL: https://openreview.net/pdf?id=AQZZWVp6XA

## Abstract

Compositional generalization, the ability to recognize familiar parts in novel contexts, is a defining property of intelligent systems, yet modern models, despite massive training sets, see only a tiny fraction of the combinatorial input space. We ask what structure representations {must} have to support generalization to unseen combinations. We formalize three desiderata (divisibility, transferability, stability) and show they impose necessary geometric constraints under standard training: representations must decompose linearly into per-concept components, orthogonal across concepts. This grounds the Linear Representation Hypothesis as a necessary consequence of compositional generalization, and yields dimension bounds linking the number of composable concepts to embedding geometry. Empirically, across CLIP, SigLIP, and DINO, we find partial linear factorization with low-rank near-orthogonal per-concept factors, and the degree of this structure correlates with compositional generalization on unseen combinations. As models continue to scale, these conditions predict the geometry they may converge to. Code: https://github.com/oshapio/necessary-compositionality

## One-Sentence Claim

Compositional generalization in vision embeddings requires representations to decompose linearly into approximately orthogonal per-concept components.

## Problem

Models see only a tiny fraction of possible concept combinations, so generalizing to unseen combinations requires representation structure that supports recombination.

## Core Contribution

The paper formalizes divisibility, transferability, and stability desiderata and derives necessary geometric constraints: linear per-concept decomposition and cross-concept orthogonality.

## Method

It proves dimension bounds relating the number of composable concepts to embedding geometry, grounding the Linear Representation Hypothesis as a consequence of compositional generalization.

## Experiments and Evidence

The abstract reports empirical analysis across CLIP, SigLIP, and DINO showing partial linear factorization with low-rank near-orthogonal per-concept factors, with structure degree correlating with compositional generalization on unseen combinations.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: formal assumptions behind necessity, compositional benchmark construction, concept granularity, and whether orthogonality conflicts with shared attributes.

## Deep Themes

- Generalization requires geometric structure, not only data scale.
- Linear factorization may be a necessary representation property for composition.
- Embedding dimension bounds connect capability to representation geometry.

## Subthemes

- Compositional generalization.
- Linear Representation Hypothesis.
- Orthogonal concepts.
- Vision embeddings.
- CLIP/SigLIP/DINO.
- Dimension bounds.

## Connections to Other Papers

Connects to LOES, SVD interpretability, HyperDepth, and representation-geometry papers through linear/spectral structure as a basis for generalization and interpretation.

## Notes for Cross-Paper Synthesis

This paper strengthens the representation-geometry theme: compositional ability may require a specific linear-orthogonal embedding organization.
