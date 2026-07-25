# Seizure-Semiology-Suite($S^3$): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: MyorUlHKVc
- Authors: Lina Zhang; Tonmoy Monsoor; Peizheng Li; Jiarui Cui; Xinyi Peng; Chong Han; Prateik Sinha; Siyuan Dai; Jessica Nichole Pasqua; Colin M McCrimmon; Weiting Liu; Hailey Marie Miranda; Bing Hu; Xiangting Wu; Tengyou Xu; Chunhan Li; Jiaye Tian; Jiarui Tang; Detao Ma; Lingye Kong; Junnan Lyu; Jungang Li; Yan Zan; Junhua Huang; Rajarshi Mazumder; Vwani Roychowdhury
- Primary area: applications->health_medicine
- Keywords: MLLMs;Seizure Semiology;Benchmark;Medical AI
- Source URL: https://openreview.net/forum?id=MyorUlHKVc
- PDF URL: https://openreview.net/pdf?id=MyorUlHKVc

## Abstract

While Multimodal Large Language Models (MLLMs) have demonstrated remarkable proficiency in general video understanding, their capacity to interpret involuntary, and spatio-temporally evolving pathologic motor behaviors such as seizure semiology remains largely untested. To address this gap, we introduce Seizure-Semiology-Suite (S³), a clinically grounded dataset and benchmark for fine-grained, structured seizure semiology understanding. The dataset includes 438 seizure videos annotated with over 35,000 dense labels covering 20 ILAE-defined semiological features. Building on this dataset, we propose a seven-task hierarchical benchmark that systematically evaluates MLLMs from low-level visual perception to temporal sequencing, narrative report generation, and seizure diagnosis. To enable clinically meaningful evaluation of generated reports, we further introduce the Report Quality Index for Seizure Semiology (Seizure-RQI). Extensive baselines across 11 open-weight MLLMs reveal systematic weaknesses in laterality reasoning, temporal localization, symptom sequencing, and clinically faithful reporting. We show that seizure-specific fine-tuning substantially improves performance across tasks, and that a two-stage neuro-symbolic framework achieves an F1 score of 0.96 on epileptic versus non-epileptic seizure classification. Seizure-Semiology-Suite establishes a rigorous benchmark for evaluating multimodal models in safety-critical medical video understanding and guides the development of clinically reliable, domain-adaptive multimodal intelligence. Our code is publicly available at \href{https://github.com/LinaZhangUCLA/SeizureSemiologySuite}{SeizureSemiologySuite}.

## One-Sentence Claim

Seizure-Semiology-Suite provides a clinically grounded multimodal video dataset, benchmark, and models for fine-grained seizure semiology understanding and reporting.

## Problem

General MLLMs are strong on broad video tasks, but their ability to interpret spatiotemporally evolving pathological motor behaviors such as seizure semiology is largely untested.

## Core Contribution

The paper introduces S3 with 438 seizure videos and over 35,000 dense labels across 20 ILAE-defined features, a seven-task hierarchical benchmark, Seizure-RQI for report evaluation, and seizure-specific modeling baselines.

## Method

The benchmark evaluates MLLMs from low-level perception through temporal sequencing, narrative report generation, and seizure diagnosis. The paper also evaluates seizure-specific fine-tuning and a two-stage neuro-symbolic framework.

## Experiments and Evidence

The abstract reports systematic weaknesses across 11 open-weight MLLMs in laterality reasoning, temporal localization, symptom sequencing, and faithful clinical reporting; seizure-specific fine-tuning improves performance, and the neuro-symbolic framework reaches 0.96 F1 for epileptic versus non-epileptic seizure classification.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: clinical annotation protocol, privacy/de-identification, video distribution, inter-rater agreement, external validation, and whether report metrics align with clinician judgment.

## Deep Themes

- Safety-critical medical video needs domain-specific multimodal benchmarks.
- Clinical reasoning requires temporal localization and structured feature reporting.
- Neuro-symbolic pipelines may still outperform general MLLMs on specialized diagnosis.

## Subthemes

- Medical AI.
- Seizure semiology.
- Multimodal video understanding.
- Dense clinical labels.
- Report quality metrics.
- Neuro-symbolic classification.

## Connections to Other Papers

Connects to evaluation, multimodal grounding, and healthcare AI papers through domain-specific benchmarks and reliable report generation.

## Notes for Cross-Paper Synthesis

S3 adds a medical benchmark theme: general video understanding does not imply clinically faithful temporal reasoning, so domain benchmarks must encode specialist structure.
