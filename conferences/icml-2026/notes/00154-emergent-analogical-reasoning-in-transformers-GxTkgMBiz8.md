# Emergent Analogical Reasoning in Transformers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GxTkgMBiz8
- Authors: Gouki Minegishi; Jingyuan Feng; Hiroki Furuta; Takeshi Kojima; Yusuke Iwasawa; Yutaka Matsuo
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Interpretability;Reasoning;Analogy
- Source URL: https://openreview.net/forum?id=GxTkgMBiz8
- PDF URL: https://openreview.net/pdf?id=GxTkgMBiz8

## Abstract

Analogy is a central faculty of human intelligence, enabling abstract patterns discovered in one domain to be applied to another.
However, the mechanisms underlying analogical reasoning in Transformers remain poorly understood.
In this work, inspired by the notion of functors in category theory, we formalize analogical reasoning as the inference of correspondences between entities across categories.
Based on this formulation, we introduce synthetic tasks that evaluate the emergence of analogical reasoning under controlled settings.
We find that the emergence of analogical reasoning is highly sensitive to data characteristics, optimization choices, and model scale.
Through mechanistic analysis, we show that analogical reasoning in Transformers decomposes into two key components:
(1) geometric alignment of relational structure in the embedding space, and
(2) the application of a functor within the Transformer. These mechanisms enable models to transfer relational structure from one category to another, realizing analogy.
Finally, we quantify these effects and find that the same trends are observed in pretrained LLMs.
In doing so, we move analogy from an abstract cognitive notion to a concrete, mechanistically grounded phenomenon in modern neural networks.

## One-Sentence Claim

Transformers can develop analogical reasoning through geometric alignment of relational structure and an internal functor-like mapping between categories.

## Problem

Analogy is central to intelligence, but the mechanisms by which Transformers infer correspondences and transfer relational structure are poorly understood.

## Core Contribution

The paper formalizes analogy using category-theoretic functor ideas, introduces controlled synthetic tasks, and mechanistically analyzes how analogical reasoning emerges.

## Method

It defines analogical reasoning as inferring correspondences between entities across categories, then studies emergence as a function of data properties, optimization, and scale, with mechanistic analysis of embedding geometry and Transformer computation.

## Experiments and Evidence

The abstract reports sensitivity to data, optimization, and scale, identifies two mechanisms: relational geometric alignment and functor application, and observes similar trends in pretrained LLMs.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: task design, category-theory formalization, mechanistic probes, and how synthetic results transfer to natural analogies.

## Deep Themes

- Abstract reasoning can be grounded in representation geometry and internal transformations.
- Analogical transfer requires aligned relational structure.
- Synthetic tasks can isolate emergence mechanisms for pretrained-model behavior.

## Subthemes

- Analogical reasoning.
- Mechanistic interpretability.
- Category theory.
- Functors.
- Relational structure.
- Transformer geometry.

## Connections to Other Papers

Connects to compositional generalization, LOES, SVD interpretability, and emergent reasoning papers through geometry as the substrate of abstraction.

## Notes for Cross-Paper Synthesis

This paper strengthens the geometry-of-reasoning theme: abstract cognitive capabilities may correspond to concrete representational alignments and transformations.
