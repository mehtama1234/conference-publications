# How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: A4Us8jxVGq
- Authors: Shawn Im; Changdae Oh; Zhen Fang; Sharon Li
- Primary area: interpretability and explainable AI
- Keywords: Semantic associations;Interpretability;LLM
- Source URL: https://openreview.net/forum?id=A4Us8jxVGq
- PDF URL: https://openreview.net/pdf?id=A4Us8jxVGq

## Abstract

Semantic associations such as the link between "bird" and "flew" are foundational for language modeling as they enable models to go beyond memorization and instead generalize and generate coherent text. Understanding how these associations are learned and represented in language models is essential for connecting deep learning with linguistic theory and developing a mechanistic foundation for large language models. In this work, we analyze how these associations emerge from natural language data in attention-based language models through the lens of training dynamics. By leveraging a leading-term approximation of the gradients, we develop closed-form expressions for the weights at early stages of training that explain how semantic associations first take shape. Through our analysis, we reveal that each set of weights of the transformer has closed-form expressions as simple compositions of three basis functions--bigram, token-interchangeability, and context mappings--reflecting the statistics in the text corpus and uncover how each component of the transformer captures the semantic association based on these compositions. Experiments on real-world LLMs demonstrate that our theoretical weight characterizations closely match the learned weights, and qualitative analyses further guide us on how our theorem shines light on interpreting the learned association in transformers.

## One-Sentence Claim

Early transformer training learns semantic token associations through gradient leading terms that decompose weights into bigram, token-interchangeability, and context-mapping basis functions.

## Problem

Language models rely on semantic associations such as bird-flew to generalize beyond memorization. But how these associations first emerge in transformer weights from natural language data remains poorly understood.

The problem is to connect corpus statistics, training dynamics, and mechanistic interpretation of learned transformer components.

## Core Contribution

The paper develops a leading-term approximation of gradients that yields closed-form expressions for early-stage transformer weights.

It shows that transformer weights can be characterized as compositions of three basis functions: bigram statistics, token interchangeability, and context mappings.

## Method

The authors analyze training dynamics in attention-based language models. By approximating gradients with leading terms, they derive closed-form early-weight expressions.

These expressions map corpus statistics into transformer components, clarifying how each part of the transformer captures semantic association.

## Experiments and Evidence

The abstract reports experiments on real-world LLMs showing theoretical weight characterizations closely match learned weights.

Qualitative analyses use the theorem to interpret learned associations in transformers.

## Limits and Failure Modes

Leading-term approximations may be most accurate early in training and may not fully explain later nonlinear feature interactions, deep layers, or large-scale pretraining dynamics.

Because this note is abstract-only, details still need checking: model class, approximation assumptions, corpus statistics, comparison metrics, depth/width limits, and how well the theory scales to modern LLMs.

## Deep Themes

- Training dynamics as interpretability: early gradients reveal how structure enters weights.
- Corpus statistics become mechanisms: bigrams, interchangeability, and contexts map to transformer components.
- Closed-form mechanistic theory: transformer associations can be partially solved analytically.
- Semantic association formation: meaning emerges from structured statistical composition, not only memorization.

## Subthemes

- Gradient leading-term approximation.
- Bigram basis functions.
- Token interchangeability.
- Context mapping.

## Connections to Other Papers

This connects to transformer circuits, Rational Transductors, accessible sequence bounds, and DAVE through architecture-aware interpretability.

It also relates to coverage theory because both connect pretraining statistics to downstream capability.

## Notes for Cross-Paper Synthesis

This paper adds a training-dynamics interpretability theme: mechanisms can sometimes be read from the first-order path by which data statistics shape weights.
