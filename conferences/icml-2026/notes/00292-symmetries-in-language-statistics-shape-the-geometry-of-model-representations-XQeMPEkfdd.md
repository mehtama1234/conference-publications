# Symmetries in language statistics shape the geometry of model representations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: XQeMPEkfdd
- Authors: Dhruva Karkada; Daniel James Korchinski; Andres Nava; Matthieu Wyart; Yasaman Bahri
- Primary area: theory->deep_learning
- Keywords: representations;geometry;feature manifolds;mechanistic interpretability;feature learning;symmetry;co-occurrence;language;data;latent variable model;word embedding;LLM
- Source URL: https://openreview.net/forum?id=XQeMPEkfdd
- PDF URL: https://openreview.net/pdf?id=XQeMPEkfdd

## Abstract

Although learned representations underlie neural networks' success, their fundamental properties remain poorly understood.
A striking example is the emergence of simple geometric structures in LLM representations: for example, calendar months organize into a circle, years form a one-dimensional manifold, and the latitude and longitude of cities can be decoded by low-dimensional linear probes.
We show that the statistics of language exhibit a translation symmetry---e.g,. the co-occurrence probability of two months depends only on the time interval between them---and we prove that the latter governs the aforementioned geometric structures in high-dimensional word embedding models.
Moreover, we find that these structures persist even when the co-occurrence statistics are strongly perturbed (for example, by removing all sentences in which two months appear together) and at moderate embedding dimension.
We show that this robustness naturally emerges if the co-occurrence statistics are collectively controlled by an underlying continuous latent variable.
We empirically validate this theoretical framework in word embedding models, text embedding models, and large language models.

## One-Sentence Claim

Simple geometric structures in language-model representations arise because symmetric co-occurrence statistics are governed by underlying continuous latent variables.

## Problem

LLM representations often show striking geometry: months form circles, years form lines, and city coordinates can be decoded linearly. These structures are observed empirically, but the statistical causes remain poorly understood.

The paper asks why language data gives rise to these geometric feature manifolds and why the structures can be robust to perturbations.

## Core Contribution

The paper shows that translation symmetries in language statistics, such as month co-occurrence depending on time interval, govern emergent geometry in high-dimensional word embeddings. It proves this relationship and argues robustness emerges when co-occurrence statistics are collectively controlled by an underlying continuous latent variable.

The theory is validated in word embeddings, text embedding models, and LLMs, and the structures persist even after strong co-occurrence perturbations such as removing sentences containing month pairs.

## Method

The method combines statistical symmetry analysis, theory for high-dimensional embedding models, and empirical representation studies. It identifies symmetries in co-occurrence probabilities, derives the induced representation geometry, perturbs the statistics, and tests whether the predicted structures persist.

The latent-variable view explains why individual co-occurrence removal does not destroy the global geometric manifold.

## Experiments and Evidence

Evidence reported in the abstract:

- Translation-symmetry analysis of language co-occurrence statistics.
- Proof that such statistics govern geometric structures in word embedding models.
- Perturbation experiments removing direct co-occurrences.
- Robust structures at moderate embedding dimension.
- Empirical validation in word embedding models, text embedding models, and LLMs.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: formal model assumptions, perturbation datasets, LLM layers analyzed, and geometry metrics.

## Limits and Failure Modes

- The theory may best explain categories with clean latent variables, such as time or geography.
- Real language includes many overlapping symmetries and social/contextual biases.
- Robustness to removing direct co-occurrence does not mean robustness to broader corpus shifts.
- High-dimensional embedding assumptions need inspection.

## Deep Themes

**Representation geometry is data-statistical.** Manifolds emerge from symmetries in co-occurrence structure, not only architecture.

**Latent variables stabilize features.** Shared continuous causes make geometry robust to local perturbations.

**Interpretability can start from corpus symmetries.** Understanding model features requires understanding the statistical invariances in training data.

## Subthemes

- Translation symmetry in language statistics.
- Feature manifolds for months, years, and geography.
- Continuous latent-variable control.
- Robustness to co-occurrence perturbation.
- Geometry of word and LLM embeddings.

## Connections to Other Papers

Connects to Diffract, Neuron-Basis Circuits, AI Engram, and representation-geometry papers. It also links to RECM and ENGNN because both study how symmetry and equivariance shape learned representations.

## Notes for Cross-Paper Synthesis

This paper adds a data-origin account of representation geometry: some model manifolds are not mysterious emergent artifacts but compressed reflections of symmetries already present in language statistics.
