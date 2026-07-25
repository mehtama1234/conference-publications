# Less is Enough: Synthesizing Diverse Data in LLM Feature Space with Sparse Autoencoders

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GVupwQ0578
- Authors: Zhongzhi Li; Xuansheng Wu; Yijiang Li; Lijie Hu; Ninghao Liu
- Primary area: deep_learning->large_language_models
- Keywords: Synthetic Data;Sparse Autoencoders;Post-training;Instruction Tuning;Large Language Models
- Source URL: https://openreview.net/forum?id=GVupwQ0578
- PDF URL: https://openreview.net/pdf?id=GVupwQ0578

## Abstract

The diversity of post-training data is critical for effective downstream performance in large language models (LLMs). 
Many existing approaches to constructing post-training data quantify diversity using text-based metrics that capture linguistic variation, but such metrics provide only weak signals for the task-relevant features that determine downstream performance.
In this work, we introduce ***Feature Activation Coverage* (FAC)** which measures data diversity in an interpretable feature space. 
Building upon this metric, we further propose a diversity-driven data synthesis framework, named **FAC Synthesis**, that first uses a sparse autoencoder to identify missing features from a seed dataset, and then generates synthetic samples that explicitly reflect these features.
Experiments show that our approach consistently improves both data diversity and downstream performance on various tasks, including instruction following, toxicity detection, reward modeling, and behavior steering. 
Interestingly, we identify a shared, interpretable feature space across model families (i.e., LLaMA, Mistral, and Qwen), enabling cross-model knowledge transfer.
Our work provides a solid and practical methodology for exploring data-centric optimization of LLMs.

## One-Sentence Claim

FAC Synthesis uses sparse-autoencoder feature space to identify missing interpretable features in seed data and generate diverse post-training samples that improve downstream LLM behavior.

## Problem

Post-training data diversity is critical, but text-based diversity metrics weakly track the task-relevant model features that affect downstream performance.

## Core Contribution

The paper introduces Feature Activation Coverage and a diversity-driven data synthesis framework that generates data to cover missing SAE features.

## Method

FAC measures coverage in an interpretable feature space. FAC Synthesis uses a sparse autoencoder to find undercovered features in seed data, then synthesizes examples explicitly reflecting those features.

## Experiments and Evidence

The abstract reports improved diversity and downstream performance on instruction following, toxicity detection, reward modeling, and behavior steering, plus a shared interpretable feature space across LLaMA, Mistral, and Qwen for cross-model transfer.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: SAE training, feature labeling, synthesis prompts, data quality filtering, and risks of over-optimizing feature coverage.

## Deep Themes

- Data diversity should be measured in model feature space.
- Sparse autoencoders can guide data-centric LLM optimization.
- Shared features across model families enable cross-model data transfer.

## Subthemes

- Synthetic data.
- Sparse autoencoders.
- Feature Activation Coverage.
- Instruction tuning.
- Reward modeling data.
- Cross-model feature transfer.

## Connections to Other Papers

Connects to data valuation, activation oracles, feature discovery, alignment pretraining, and data-centric post-training work.

## Notes for Cross-Paper Synthesis

FAC Synthesis reinforces the feature-space data theme: better post-training data can be synthesized by targeting missing internal features rather than surface text variation.
