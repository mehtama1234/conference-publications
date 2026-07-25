# High-dimensional Analysis of Synthetic Data Selection

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Y54P2BBPPh
- Authors: Parham Rezaei; Filip Kovačević; Francesco Locatello; Marco Mondelli
- Primary area: transfer learning, meta learning, and lifelong learning
- Keywords: high dimensional regression;empirical risk minimization;synthetic data;generative models
- Source URL: https://openreview.net/forum?id=Y54P2BBPPh
- PDF URL: https://openreview.net/pdf?id=Y54P2BBPPh

## Abstract

Despite the progress in the development of generative models, their usefulness in creating synthetic data that improve prediction performance of classifiers has been put into question. Besides heuristic principles such as ''synthetic data should be close to the real data distribution'', it is actually not clear which specific properties affect the generalization error. Our paper addresses this question through the lens of high-dimensional regression. Theoretically, we show that, for linear models, the *covariance shift* between the target distribution and the distribution of the synthetic data affects the generalization error but, surprisingly, the mean shift does not. Furthermore, in some regimes, we prove that matching the covariance of the target distribution is optimal. Remarkably, the theoretical insights for linear models carry over to deep neural networks and generative models. We empirically demonstrate that the *covariance matching* procedure (matching the covariance of the synthetic data with that of the data coming from the target distribution) performs well against several recent approaches for synthetic data selection, across various training paradigms, datasets and generative models used for augmentation.

## One-Sentence Claim

This paper shows that covariance shift, not mean shift, controls synthetic-data usefulness in high-dimensional regression and motivates covariance matching for synthetic data selection.

## Problem

Generative models can create synthetic data, but it remains unclear when synthetic samples actually improve classifier generalization.

Heuristics such as matching the real data distribution are too vague; the field needs specific properties that predict whether synthetic augmentation helps.

## Core Contribution

The paper analyzes synthetic data selection through high-dimensional regression.

For linear models, it proves that covariance shift between target and synthetic distributions affects generalization error, while mean shift surprisingly does not. In some regimes, target covariance matching is optimal.

## Method

The theoretical analysis studies synthetic augmentation in high-dimensional linear regression and isolates how distributional moments affect risk.

The resulting covariance-matching procedure selects or adjusts synthetic data to match target covariance, then tests whether the linear-model insight transfers to deep networks and generative augmentation.

## Experiments and Evidence

The abstract reports that covariance matching performs well against recent synthetic-data selection approaches.

The empirical results span multiple training paradigms, datasets, and generative models, and the linear-theory insight carries over to deep neural networks.

## Limits and Failure Modes

Covariance matching may miss higher-order structure, labels, causal relations, or rare modes. The result may be strongest when second-order statistics dominate downstream generalization.

Because this note is abstract-only, details still need checking: regression assumptions, exact risk formula, synthetic selection algorithm, datasets, deep-model experiments, and failure cases where covariance is insufficient.

## Deep Themes

- Synthetic-data utility from second-order structure: covariance can matter more than mean alignment.
- Theory-guided data selection: high-dimensional analysis produces a concrete augmentation rule.
- Distribution matching with task relevance: useful synthetic data is defined by generalization impact, not visual plausibility alone.
- Linear-to-deep transfer: simplified theory can still guide generative-data practice.

## Subthemes

- Synthetic data selection.
- Covariance matching.
- High-dimensional regression.
- Generalization error analysis.

## Connections to Other Papers

This connects to TabStruct, PetaGAIL++, source screening, data curation, and synthetic-data governance papers.

It also relates to Train-before-Test and curriculum work because all ask which data properties actually affect downstream capability.

## Notes for Cross-Paper Synthesis

This paper adds a statistical data-selection theme: synthetic data quality should be evaluated through task-relevant covariance structure, not only closeness or realism.
