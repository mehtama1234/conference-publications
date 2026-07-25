# Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: DbZjxkZrZm
- Authors: Adam Karvonen; James Chua; Clément Dumas; Kit Fraser-Taliente; Subhash Kantamneni; Julian Minder; Euan Ong; Arnab Sen Sharma; Daniel Wen; Owain Evans; Samuel Marks
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: language models;interpretability;automated interpretability;latentqa
- Source URL: https://openreview.net/forum?id=DbZjxkZrZm
- PDF URL: https://openreview.net/pdf?id=DbZjxkZrZm

## Abstract

Large language model (LLM) activations are notoriously difficult to understand, with most existing techniques using complex, specialized methods for interpreting them. Recent work has proposed a simpler approach known as LatentQA: training LLMs to directly accept LLM activations as inputs and answer arbitrary questions about them in natural language. However, prior work has focused on narrow task settings for both training and evaluation. In this paper, we instead take a generalist perspective. We evaluate LatentQA-trained models, which we call Activation Oracles (AOs), in far out-of-distribution settings and examine how performance scales with training data diversity. We find that AOs can recover information fine-tuned into a model (e.g., biographical knowledge or malign propensities) that does not appear in the input text, despite never being trained with activations from a fine-tuned model. Our main evaluations are four downstream tasks where we can compare to prior white- and black-box techniques. We find that even narrowly-trained LatentQA models can generalize well, and that adding additional training datasets (such as classification tasks and a self-supervised context prediction task) yields consistent further improvements. Our best AOs match or exceed white-box baselines on all four tasks and the best overall baseline on 3 of 4. These results suggest that diversified training to answer natural-language queries imparts a general capability to verbalize information about LLM activations.

## One-Sentence Claim

Activation Oracles train LLMs to answer natural-language questions about internal activations, providing general-purpose activation explainers that can generalize beyond narrow training settings.

## Problem

LLM activations are hard to interpret, and existing automated interpretability methods are often specialized or evaluated only on narrow tasks.

## Core Contribution

The paper evaluates LatentQA-trained models as Activation Oracles, studies out-of-distribution generalization and data-diversity scaling, and compares them to white-box and black-box baselines.

## Method

Activation Oracles take model activations as input and answer arbitrary natural-language questions about what information those activations contain. Training diversity includes classification tasks and self-supervised context prediction.

## Experiments and Evidence

The abstract reports that AOs recover information fine-tuned into models, such as biographical knowledge or malign propensities, even when not trained on fine-tuned-model activations. Best AOs match or exceed white-box baselines on all four downstream tasks and the best overall baseline on 3 of 4.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: activation input format, task suite, calibration of natural-language answers, sensitivity to model families, and risk of hallucinated explanations.

## Deep Themes

- Interpretability can be cast as natural-language querying of activations.
- Training diversity may create general activation-reading capabilities.
- Activation explainers can reveal hidden fine-tuned behaviors not present in input text.

## Subthemes

- Automated interpretability.
- LatentQA.
- Activation explanations.
- White-box baselines.
- Hidden model properties.
- Natural-language audits.

## Connections to Other Papers

Connects to SVD interpretability, Shared Semantics/Divergent Mechanisms, activation-feature discovery, and safety auditing work.

## Notes for Cross-Paper Synthesis

Activation Oracles add a queryable-internals theme: model states may become objects that other LLMs can inspect and explain in language.
