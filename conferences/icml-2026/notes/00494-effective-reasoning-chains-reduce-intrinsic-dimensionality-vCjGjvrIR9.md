# Effective Reasoning Chains Reduce Intrinsic Dimensionality

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: vCjGjvrIR9
- Authors: Archiki Prasad; Mandar Joshi; Kenton Lee; Mohit Bansal; Peter Shaw
- Primary area: deep_learning->large_language_models
- Keywords: Chain of thought;reasoning;intrinsic dimension;minimum description length
- Source URL: https://openreview.net/forum?id=vCjGjvrIR9
- PDF URL: https://openreview.net/pdf?id=vCjGjvrIR9

## Abstract

Chain-of-thought (CoT) reasoning and its variants have substantially improved the performance of language models on complex reasoning tasks, yet the precise mechanisms by which different strategies facilitate generalization remain poorly understood. While current explanations often point to increased test-time computation or structural guidance, establishing a consistent, quantifiable link between these factors and generalization remains challenging. In this work, we identify *intrinsic dimensionality* as a quantitative measure for characterizing the effectiveness of reasoning chains. Intrinsic dimensionality quantifies the minimum number of model dimensions needed to reach a given accuracy threshold on a given task. By keeping the model architecture fixed and varying the task formulation through different reasoning strategies, we demonstrate that effective reasoning strategies consistently reduce the intrinsic dimensionality of the task. Validating this on GSM8K with Gemma-3 1B and 4B, we observe a strong inverse correlation between the intrinsic dimensionality of a reasoning strategy and its generalization performance on both in-distribution and out-of-distribution data. Our findings suggest that effective reasoning chains facilitate learning by better compressing the task using fewer parameters, offering a new quantitative metric for analyzing reasoning processes.

## One-Sentence Claim

Effective chain-of-thought strategies improve generalization by reducing a task's intrinsic dimensionality, meaning fewer model dimensions are needed to reach a target accuracy.

## Problem

Chain-of-thought improves reasoning, but explanations often stop at "more test-time compute" or "better structure." Those accounts are hard to quantify consistently across reasoning strategies.

The paper asks for a measurable property that links reasoning-chain formulation to generalization. It proposes intrinsic dimensionality as that property.

## Core Contribution

The paper shows that effective reasoning strategies consistently reduce task intrinsic dimensionality when architecture is fixed and task formulation varies. Lower intrinsic dimensionality is strongly inversely correlated with generalization performance.

The contribution is a quantitative diagnostic for reasoning chains: good chains compress the task into fewer effective model dimensions rather than merely adding more tokens.

## Method

Intrinsic dimensionality is defined as the minimum number of model dimensions needed to reach a given accuracy threshold on a task. The authors keep model architecture fixed and vary reasoning strategies or task formulations.

They evaluate the dimensionality-performance relationship on GSM8K using Gemma-3 1B and 4B, comparing in-distribution and out-of-distribution generalization.

## Experiments and Evidence

The abstract reports a strong inverse correlation between reasoning-strategy intrinsic dimensionality and generalization performance on both ID and OOD data. Effective reasoning chains reduce intrinsic dimensionality across tested formulations.

Full-paper reading should verify how dimensions are restricted or measured, which reasoning strategies are compared, threshold choices, and whether the relationship holds beyond GSM8K.

## Limits and Failure Modes

Intrinsic dimensionality measurement can depend on the chosen threshold, probing method, model architecture, and task. GSM8K is an important benchmark but not sufficient to cover all reasoning domains.

Reducing dimensionality may be a correlate rather than sole cause of better reasoning. Some tasks may require richer representations rather than lower-dimensional compression.

## Deep Themes

- Reasoning as task compression: effective chains reduce the dimensional burden on the model.
- Quantitative process diagnostics: CoT quality can be measured through intrinsic dimensionality.
- Formulation changes capability: the same model solves different induced tasks depending on reasoning format.
- Generalization beyond token count: more tokens help when they reshape the task representation.

## Subthemes

- Minimum description length motivates dimensionality measures.
- ID and OOD performance correlate with dimensional compression.
- Small and larger Gemma models test scale sensitivity.
- Reasoning strategies can be compared mechanistically.

## Connections to Other Papers

This paper connects to LongCoT, PLAINTAIN, reasoning-loop analysis, and BLL-Loss. It provides a different lens: successful reasoning chains reduce the effective task dimension, while failed or looping chains may add length without compression.

It also relates to embedding dimensionality collapse, showing both positive and negative sides of dimensionality: too few representation dimensions can hurt, but good reasoning can lower the task's required dimension.

## Notes for Cross-Paper Synthesis

The synthesis point is that reasoning traces are not only computation; they are representation transformations that can compress the problem into a more learnable form.
