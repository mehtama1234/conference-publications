# Disentangling Geometry, Performance, and Training in Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kNb6NNhKgE
- Authors: Atharva Kulkarni; Jacob Mitchell Springer; Arjun Subramonian; Swabha Swayamdipta
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;Effective Rank;Anisotropy;Representation Geometry;Intrinsic Dimensionality
- Source URL: https://openreview.net/forum?id=kNb6NNhKgE
- PDF URL: https://openreview.net/pdf?id=kNb6NNhKgE

## Abstract

Geometric properties of Transformer weights, particularly the unembedding matrix, have been widely useful in language model interpretability research.
Yet, their utility for estimating downstream performance remains unclear.
In this work, we systematically investigate the relationship between model performance and the unembedding matrix geometry, particularly its effective rank.
Our experiments, involving a suite of 108 OLMo-style language models trained under controlled variation, reveal several key findings.
While the best-performing models often exhibit a high effective rank, this trend is not universal across tasks and training setups. 
Contrary to prior work, we find that low effective rank does not cause late-stage performance degradation in small models, but instead co-occurs with it; we find adversarial cases where low-rank models do not exhibit saturation.
Moreover, we show that effective rank is strongly influenced by pre-training hyperparameters, such as batch size and weight decay, which in-turn affect the model's performance.
Lastly, extending our analysis to other geometric metrics and final-layer representation, we find that these metrics are largely aligned, but none can reliably predict downstream performance.
Overall, our findings suggest that the model's geometry, as captured by existing metrics, primarily reflects training choices rather than performance.

## One-Sentence Claim

Unembedding geometry metrics such as effective rank mostly reflect training choices rather than reliably predicting downstream language-model performance.

## Problem

Interpretability work often uses geometric properties of Transformer weights and representations, especially the unembedding matrix. But it remains unclear whether metrics like effective rank actually estimate downstream performance or merely correlate with other training factors.

The paper asks whether representation geometry causes performance changes or reflects the training setup that produced them.

## Core Contribution

The paper systematically studies 108 controlled OLMo-style language models and finds that high effective rank often appears in strong models but is not a universal predictor. Contrary to prior claims, low effective rank does not cause late-stage degradation in small models; it co-occurs with it.

The study identifies adversarial cases where low-rank models avoid saturation and shows that effective rank is strongly influenced by pretraining hyperparameters such as batch size and weight decay.

## Method

The authors train or analyze a controlled suite of models with varied hyperparameters, then compare downstream performance with unembedding effective rank, anisotropy, intrinsic dimensionality, and final-layer representation metrics.

The controlled variation lets them separate geometry-performance correlation from training-choice confounds.

## Experiments and Evidence

Evidence reported in the abstract:

- 108 OLMo-style language models under controlled variation.
- High effective rank often but not universally associated with best performance.
- Low effective rank co-occurs with, rather than causes, late-stage degradation in small models.
- Adversarial cases where low-rank models do not saturate.
- Effective rank strongly influenced by batch size and weight decay.
- Other geometry metrics are largely aligned but cannot reliably predict downstream performance.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model sizes, tasks, hyperparameter grid, and causal tests.

## Limits and Failure Modes

- Findings are based on OLMo-style controlled models and may differ for other architectures or scales.
- Geometry metrics may still be useful for diagnostics even if not predictive alone.
- Downstream performance is task-dependent, so aggregate conclusions need task-level nuance.
- Causal separation of geometry and training choices remains difficult.

## Deep Themes

**Interpretability metrics can be confounded.** Geometry may reflect how a model was trained more than what it can do.

**Correlation is not capability diagnosis.** Effective rank alone cannot serve as a reliable performance proxy.

**Training choices sculpt representation geometry.** Batch size and weight decay materially shape the measured structure.

## Subthemes

- Unembedding effective rank.
- Representation anisotropy.
- Intrinsic dimensionality.
- Hyperparameter confounding.
- Geometry-performance disentanglement.

## Connections to Other Papers

Connects to Isotropic Gaussian RL, Fisher Memory Dynamics, Context-Parameter Equivalence, and Weight-Space Expressivity. It cautions the broader representation-geometry theme against overreading simple metrics.

## Notes for Cross-Paper Synthesis

This paper adds a methodological warning: representation geometry is valuable evidence, but only when disentangled from training choices and task-specific performance.
