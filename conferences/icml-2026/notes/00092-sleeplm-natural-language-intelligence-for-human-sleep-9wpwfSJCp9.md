# SleepLM: Natural-Language Intelligence for Human Sleep

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9wpwfSJCp9
- Authors: Zongzhe Xu; Zitao Shuai; Eideen Mozaffari; Ravi Shankar Aysola; Rajesh Kumar; Yuzhe Yang
- Primary area: applications->health_medicine
- Keywords: sleep physiology; foundation model; language model; large language model; multimodal language model; AI for healthcare
- Source URL: https://openreview.net/forum?id=9wpwfSJCp9
- PDF URL: https://openreview.net/pdf?id=9wpwfSJCp9

## Abstract

We present SleepLM, a family of sleep-language foundation models that enable human sleep alignment, interpretation, and interaction with natural language.
Despite the critical role of sleep, learning-based sleep analysis systems operate in closed label spaces (e.g., predefined stages or events) and fail to describe, query, or generalize to novel sleep phenomena.
SleepLM bridges natural language and multimodal polysomnography, enabling language-grounded representations of sleep physiology.
To support this alignment, we introduce a multilevel sleep caption generation pipeline that enables the curation of the first large-scale sleep-text dataset, comprising over 100K hours of data from more than 10,000 individuals.
Furthermore, we present a unified pretraining objective that combines contrastive alignment, caption generation, and signal reconstruction to better capture physiological fidelity and cross-modal interactions.
Extensive experiments on real-world sleep understanding tasks verify that SleepLM outperforms state-of-the-art in zero-shot and few-shot learning, cross-modal retrieval, and sleep captioning. Importantly, SleepLM also exhibits intriguing capabilities including language-guided event localization, targeted insight generation, and zero-shot generalization to unseen tasks.
To support reproducibility and future work, we open-source the captioning pipeline, pretrained checkpoints, and the model architectures at https://github.com/yang-ai-lab/SleepLM.

## One-Sentence Claim

SleepLM aligns polysomnography with natural language so sleep physiology can be captioned, queried, retrieved, and generalized beyond closed label spaces.

## Problem

Sleep analysis systems typically classify predefined stages or events, limiting their ability to describe novel phenomena, answer flexible questions, or support language-grounded interaction.

## Core Contribution

The paper introduces a family of sleep-language foundation models, a multilevel sleep-caption generation pipeline, and a large sleep-text dataset spanning over 100K hours from more than 10,000 individuals.

## Method

SleepLM combines contrastive alignment, caption generation, and signal reconstruction to connect multimodal polysomnography signals with text while preserving physiological fidelity and cross-modal interactions.

## Experiments and Evidence

The abstract reports state-of-the-art zero-shot and few-shot sleep understanding, cross-modal retrieval, and sleep captioning, plus language-guided event localization, targeted insight generation, and zero-shot transfer to unseen tasks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: caption quality, clinical validation, demographic coverage, privacy safeguards, and error modes in medical interpretation.

## Deep Themes

- Healthcare foundation models are moving from closed labels to language-grounded interpretation.
- Physiological signals can become interactive natural-language objects.
- Caption pipelines can create supervision for domains without native text.

## Subthemes

- Sleep physiology.
- Polysomnography-language alignment.
- Medical foundation models.
- Caption generation.
- Cross-modal retrieval.
- Clinical event localization.

## Connections to Other Papers

Connects to PhenoBrain, dnaHNet, biomedical generation papers, and VALUEFLOW-style representation resources through domain-specific foundation-model infrastructure.

## Notes for Cross-Paper Synthesis

SleepLM adds a medical-language interface theme: foundation models can make complex physiological recordings queryable and interpretable rather than only classifiable.
