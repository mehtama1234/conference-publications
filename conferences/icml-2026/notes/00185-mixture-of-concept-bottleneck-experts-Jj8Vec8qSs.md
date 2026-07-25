# Mixture of Concept Bottleneck Experts

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Jj8Vec8qSs
- Authors: Francesco De Santis; Gabriele Ciravegna; Giovanni De Felice; Arianna Casanova; Francesco Giannini; Michelangelo Diligenti; Johannes Schneider; Danilo Giordano; Mateo Espinosa Zarlenga; Pietro Barbiero
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Explainable AI;Concept-based models;Interpretability
- Source URL: https://openreview.net/forum?id=Jj8Vec8qSs
- PDF URL: https://openreview.net/pdf?id=Jj8Vec8qSs

## Abstract

Concept Bottleneck Models (CBMs) promote interpretability by grounding predictions in human-understandable concepts. However, existing CBMs typically constrain their task predictor to a single expression whose functional form is set a priori, limiting both predictive accuracy and adaptability to diverse user needs. We propose Mixture of Concept Bottleneck Experts (M-CBEs), a framework that generalizes existing CBMs along two dimensions: the number of expressions, referred to as experts, employed by the task predictor to map concepts to the task, and the functional form each expression takes, thus exposing an underexplored region of this design space. We investigate this region by instantiating two novel models: Linear M-CBE, which learns a finite set of linear expressions, and Symbolic M-CBE, which leverages symbolic regression to discover expert functions from data subject to user-specified operator vocabularies. Empirical evaluation demonstrates that varying the number of expressions and their functional form provides a robust framework for navigating the accuracy-interpretability trade-off.

## One-Sentence Claim

Mixture of Concept Bottleneck Experts improves concept-based interpretability by allowing multiple concept-to-task expert expressions with flexible functional forms.

## Problem

Standard Concept Bottleneck Models force predictions through a single predefined concept-to-label function, limiting accuracy and adaptability to different interpretability needs.

## Core Contribution

The paper generalizes CBMs along two axes: number of expert expressions and functional form, then instantiates linear and symbolic expert variants to navigate the accuracy-interpretability tradeoff.

## Method

Linear M-CBE learns a finite set of linear expressions over concepts, while Symbolic M-CBE uses symbolic regression with user-specified operator vocabularies to discover expert functions from data.

## Experiments and Evidence

The abstract reports empirical evaluation showing that varying expression count and functional form provides a robust way to tune accuracy versus interpretability.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, concept supervision quality, routing/selection among experts, symbolic-regression complexity, user-study evidence, and stability of discovered expressions.

## Deep Themes

- Interpretability benefits from modularity and user-adjustable functional form.
- Concept bottlenecks need richer task predictors than a single fixed expression.
- Symbolic structure can make expert behavior legible while preserving adaptability.

## Subthemes

- Explainable AI.
- Concept Bottleneck Models.
- Mixture of experts.
- Symbolic regression.
- Accuracy-interpretability tradeoff.
- Human-understandable concepts.

## Connections to Other Papers

Connects to SSMoE through expert mixtures and to interpretability-as-intervention papers that make internal structure actionable. It also relates to AGREE through decomposing predictions into more interpretable attribute or concept pathways.

## Notes for Cross-Paper Synthesis

M-CBE adds a user-facing interpretability version of modularity: multiple simple expert mappings can expose alternatives where a single global explanation would be either inaccurate or too rigid.
