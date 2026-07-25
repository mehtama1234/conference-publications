# LIMSSR: LLM-Driven Sequence-to-Score Reasoning under Training-Time Incomplete Multimodal Observations

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 0RLF7Sj2Fg
- Authors: Huangbiao Xu; Huanqi Wu; Xiao Ke; Yuxin Peng
- Primary area: applications->computer_vision
- Keywords: Incomplete Multimodal Learning;Large Language Models;Training-Time Incomplete Observations;Action Quality Assessment
- Source URL: https://openreview.net/forum?id=0RLF7Sj2Fg
- PDF URL: https://openreview.net/pdf?id=0RLF7Sj2Fg

## Abstract

Real-world multimodal learning is often hindered by missing modalities. While Incomplete Multimodal Learning (IML) has gained traction, existing methods typically rely on the unrealistic assumption of full-modal availability during training to provide reconstruction supervision or cross-modal priors. This paper tackles the more challenging setting of IML under training-time incomplete observations, which precludes reliance on a "God's eye view" of complete data. We propose LIMSSR (LLM-Driven Incomplete Multimodal Sequence-to-Score Reasoning), a framework that reformulates this challenge as a conditional sequence reasoning task. LIMSSR leverages the semantic reasoning capabilities of Large Language Models via Prompt-Guided Context-Aware Modality Imputation and Multidimensional Representation Fusion to infer latent semantics from available contexts without direct reconstruction. To mitigate hallucinations, we introduce a Mask-Aware Dual-Path Aggregation to dynamically calibrate inference uncertainty. Extensive experiments on three Action Quality Assessment datasets demonstrate that LIMSSR significantly outperforms state-of-the-art baselines without relying on complete training data, establishing a new paradigm for data-efficient multimodal learning. Code is available at https://github.com/XuHuangbiao/LIMSSR.

## One-Sentence Claim

LIMSSR handles incomplete multimodal training data by reframing action quality assessment as LLM-driven conditional sequence-to-score reasoning rather than reconstructing missing modalities.

## Problem

Incomplete multimodal learning often assumes complete data are available during training for reconstruction supervision or cross-modal priors, but real data collection may be incomplete from the start.

## Core Contribution

The paper proposes LIMSSR, using prompt-guided context-aware modality imputation, multidimensional representation fusion, and mask-aware dual-path aggregation to reason under training-time missing modalities.

## Method

The framework uses LLM semantic reasoning to infer latent semantics from available contexts without direct full-modality reconstruction. A mask-aware aggregation path calibrates uncertainty to reduce hallucinations.

## Experiments and Evidence

The abstract reports extensive experiments on three Action Quality Assessment datasets, where LIMSSR outperforms state-of-the-art baselines without requiring complete training data.

## Limits and Failure Modes

PDF checks needed: how LLM prompts are constructed, whether imputed semantics are auditable, robustness to systematic missingness, and whether action-quality datasets generalize to other multimodal domains.

## Deep Themes

- LLMs are being used as semantic reasoners inside multimodal pipelines.
- Missing data is handled through reasoning and uncertainty calibration rather than reconstruction alone.
- Real-world data incompleteness is pushing more realistic training assumptions.

## Subthemes

- Incomplete multimodal learning.
- Action quality assessment.
- LLM-driven imputation.
- Missing-modality uncertainty.
- Sequence-to-score reasoning.

## Connections to Other Papers

Connects to multimodal grounding, data-quality constraints, and BioX-Bridge's cross-modal transfer under limited labeled/complete data.

## Notes for Cross-Paper Synthesis

This supports a cross-paper theme: practical data gaps are being turned into reasoning problems. Models infer missing structure from context while explicitly tracking uncertainty.

## Full-Text Upgrade

Source used: `conferences/icml-2026/text/00009-limssr-llm-driven-sequence-to-score-reasoning-under-training-time-incomplete-multimodal-observations-0RLF7Sj2Fg-arxiv.txt`.

Additional verified details:

- LIMSSR formally defines the training set itself as incomplete, not merely test-time missing.
- The framework includes Prompt-Guided Context-Aware Modality Imputation, LLM-based Multidimensional Representation Fusion, and Mask-Aware Dual-Path Aggregation.
- Mask-Aware Dual-Path Aggregation combines an uncertainty-calibrated reasoning path with a cross-modal pattern recovery path.
- The experiments use three public long-term Action Quality Assessment datasets: FS1000, Fis-V, and Rhythmic Gymnastics.
- The full text compares against incomplete/complete multimodal AQA methods, incomplete multimodal action recognition methods, and incomplete multimodal emotion recognition methods.
- Ablations indicate all three LIMSSR modules contribute to robustness, with MDA specifically tied to hallucination mitigation through uncertainty calibration.
- The paper argues long-term AQA is a suitable testbed because it is multimodal, naturally subject to missingness, and requires fine-grained reasoning over temporal action differences.

Refined limits:

- The method is validated primarily through AQA, so broader incomplete multimodal generalization remains to be tested.
- The approach relies on pre-extracted modality-specific features and LLM semantic reasoning, which may introduce dependency on extractor quality and prompt design.
