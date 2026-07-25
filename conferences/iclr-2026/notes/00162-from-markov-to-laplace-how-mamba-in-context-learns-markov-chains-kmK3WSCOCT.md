# From Markov to Laplace: How Mamba In-Context Learns Markov Chains

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: kmK3WSCOCT
- Authors: Marco Bondaschi; Nived Rajaraman; Xiuying Wei; Razvan Pascanu; Caglar Gulcehre; Michael Gastpar; Ashok Vardhan Makkuva
- Primary area: interpretability and explainable AI
- Keywords: State-space models;Markov chains;In-context learning;Laplacian smoothing
- Source URL: https://openreview.net/forum?id=kmK3WSCOCT
- PDF URL: https://openreview.net/pdf?id=kmK3WSCOCT

## Abstract

While transformer-based language models have driven the AI revolution thus far, their computational complexity has spurred growing interest in viable alternatives, such as structured state space sequence models (SSMs) and Selective SSMs. Among these, Mamba (S6) and its variant Mamba-2 have shown remarkable inference speed-ups over transformers while achieving comparable or superior performance on complex language modeling tasks. However, despite these architectural innovations and empirical successes, the fundamental learning capabilities of Mamba remain poorly understood. In this paper, we address this gap by studying in-context learning (ICL) on Markov chains and uncovering an interesting phenomenon: even a single-layer Mamba efficiently learns the in-context Laplacian smoothing estimator, which is both Bayes and minimax optimal. To explain this, we theoretically characterize the representation capacity of Mamba and reveal the fundamental role of convolution in enabling it to represent the optimal Laplacian smoothing. These theoretical insights align strongly with empirical results and, to the best of our knowledge, represent the first formal connection between Mamba and optimal statistical estimators. Finally, we outline promising research directions inspired by these findings.

## One-Sentence Claim

Single-layer Mamba can in-context learn the Bayes- and minimax-optimal Laplacian smoothing estimator for Markov chains, with convolution providing the representation mechanism.

## Problem

Selective state-space models are attractive alternatives to transformers because of inference speed, but their fundamental in-context learning capabilities are less understood. The field needs formal accounts of what these architectures can learn and why.

## Core Contribution

The paper gives a theoretical and empirical account of Mamba in-context learning on Markov chains, connecting Mamba representation capacity to the optimal Laplacian smoothing estimator. It claims the first formal connection between Mamba and optimal statistical estimators.

## Method

The analysis studies Markov-chain ICL as a controlled statistical setting. It characterizes how Mamba represents the sufficient computations needed for Laplacian smoothing and identifies convolution as the architectural component enabling that representation. Empirical experiments test whether trained Mamba models match the predicted estimator behavior.

## Experiments and Evidence

The abstract reports strong alignment between theory and experiments, including efficient learning of the Laplacian smoothing estimator by even a single-layer Mamba. The estimator is described as both Bayes and minimax optimal in the studied setting.

## Limits and Failure Modes

Markov-chain ICL is a stylized task and may not transfer directly to natural-language or multi-step reasoning settings. The result may rely on specific transition structures, sequence lengths, and training distributions. Full-text review should check assumptions behind optimality, Mamba variants tested, finite-sample effects, and comparisons with transformer baselines.

## Deep Themes

- Theory for non-transformer sequence models.
- In-context learning as statistical estimation.
- Convolutional structure enabling optimal smoothing.
- Architecture-specific mechanisms for efficient inference.

## Subthemes

- Markov-chain ICL.
- Laplacian smoothing estimators.
- Selective SSM representation capacity.
- Bayes and minimax optimality.
- Mamba interpretability.

## Connections to Other Papers

Connects to low-rank logit theory, token-association dynamics, and Hawkes representer results through formal explanations of model behavior, and to efficiency papers because SSMs promise faster inference when their learning capabilities are understood.

## Notes for Cross-Paper Synthesis

This paper exemplifies theory that explains why an efficient architecture can substitute for transformers in a specific learning regime. It adds to the pattern of deriving compact statistical structure beneath model behavior.
