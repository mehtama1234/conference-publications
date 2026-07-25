# Learning to Theorize the World from Observation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: wsA8LgHU5U
- Authors: Doojin Baek; Gyubin Lee; Junyeob Baek; Hosung Lee; Sungjin Ahn
- Primary area: deep_learning
- Keywords: world model;representation learning;program induction;reasoning
- Source URL: https://openreview.net/forum?id=wsA8LgHU5U
- PDF URL: https://openreview.net/pdf?id=wsA8LgHU5U

## Abstract

What does it mean to understand the world? Is it simply to predict future video frames? Developmental cognitive science suggests that understanding the world is fundamentally the process of constructing internal theories of how it works rather than mere prediction, even before language is acquired. However, in machine learning, it remains unclear how to endow AI systems with such theory-building capability from raw, non-textual observation alone. In this paper, we introduce Learning-to-Theorize (L2T), a learning paradigm in which an AI system acquires the ability to construct theories represented as executable programs directly from observation alone. To instantiate this paradigm, we propose the Neural Language-of-Thought Programmer, a neural model that induces and executes latent programs as explanations rather than task-specific predictors or policies. In experiments, we show that this formulation enables explanation-driven generalization, allowing observations to be understood in terms of the programs that generate them.

## One-Sentence Claim

Learning-to-Theorize argues that world understanding should be learned as executable latent program induction from observation, not merely as next-frame prediction.

## Problem

World models in machine learning often equate understanding with prediction. Developmental cognitive science suggests a richer view: understanding means constructing internal theories that explain how observations are generated.

The difficult problem is how to learn theory-building from raw non-textual observation alone, without relying on language supervision or task-specific policies.

## Core Contribution

The paper introduces Learning-to-Theorize, a paradigm where an AI system learns to construct executable theories directly from observations. It instantiates this with the Neural Language-of-Thought Programmer, which induces and executes latent programs as explanations.

The core contribution is to put program induction at the center of nonlinguistic world modeling: the model explains observations through generative programs rather than only predicting outcomes.

## Method

The Neural Language-of-Thought Programmer induces latent executable programs from observed data and runs those programs as explanatory hypotheses. The program representation acts as an internal theory of how observations are generated.

The abstract frames the model as explanation-driven rather than task-specific: the learned program is meant to support generalization by capturing generative structure.

## Experiments and Evidence

The abstract reports experiments showing explanation-driven generalization: observations can be understood in terms of the programs that generate them.

Because no full text is available locally, the exact domains, program language, supervision signals, baselines, and generalization splits still need verification.

## Limits and Failure Modes

Program induction can be brittle if the latent language is mismatched to the environment or if multiple programs explain the same observations. It may also struggle with noisy, high-dimensional, or partially observed worlds unless the executable theory space is expressive enough.

Because this note is abstract-only, details still need checking: whether programs are discrete or continuous, how execution is trained, how search is handled, what observation domains are used, and whether learned theories remain interpretable.

## Deep Themes

- Understanding as theory construction: prediction is not enough for explanatory world modeling.
- Latent programs as representations: executable structure becomes the model's internal explanation.
- Non-textual reasoning: theory induction can be learned from observation before or without language.
- Explanation-driven generalization: abstract generative structure supports transfer beyond observed instances.

## Subthemes

- Neural language-of-thought programming.
- Program induction from observation.
- World models as executable hypotheses.
- Developmental-cognition-inspired ML objectives.

## Connections to Other Papers

This connects to concept binding, temporal graph memory explanation, and Bayesian hypergraph models because all seek structured latent explanations rather than flat predictive features.

It also relates to insertion processes, GFlowNet-style construction, and path-dependent amortized inference: all involve building structured objects through latent generative procedures.

## Notes for Cross-Paper Synthesis

This paper adds a cognitive-science version of the mechanism-aware theme. The output should be good because the model has inferred a useful internal theory, not because it has memorized predictive correlations.
