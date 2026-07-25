# Know More, Know Clearer: A Meta-Cognitive Framework for Knowledge Augmentation in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ENuMNYCiV6
- Authors: Hao Chen; Ye He; Yuchun Fan; Yukun Yan; Zhenghao Liu; Qingfu Zhu; Maosong Sun; Wanxiang Che
- Primary area: deep_learning->large_language_models
- Keywords: Knowledge Augmentation;Meta-Cognition
- Source URL: https://openreview.net/forum?id=ENuMNYCiV6
- PDF URL: https://openreview.net/pdf?id=ENuMNYCiV6

## Abstract

Knowledge augmentation has significantly enhanced the performance of Large Language Models (LLMs) in knowledge-intensive tasks. However, existing methods typically operate on the simplistic premise that model performance equates with internal knowledge, overlooking the knowledge-confidence gaps that lead to overconfident errors or uncertain truths. To bridge this gap, we propose a novel meta-cognitive framework for reliable knowledge augmentation via differentiated intervention and alignment. Our approach leverages internal cognitive signals to partition the knowledge space into mastered, confused, and missing regions, guiding targeted knowledge expansion. Furthermore, we introduce a cognitive consistency mechanism to synchronize subjective certainty with objective accuracy, ensuring calibrated knowledge boundaries. Extensive experiments demonstrate the our framework consistently outperforms strong baselines, validating its rationality in not only enhancing knowledge capabilities but also fostering cognitive behaviors that better distinguish knowns from unknowns. All codes are available at https://github.com/AI9Stars/Know-More-Know-Clearer.

## One-Sentence Claim

A metacognitive knowledge-augmentation framework partitions LLM knowledge into mastered, confused, and missing regions, then aligns subjective certainty with objective accuracy.

## Problem

Knowledge augmentation often assumes model performance reflects internal knowledge, ignoring gaps where models are overconfidently wrong or uncertain despite being correct.

## Core Contribution

The paper proposes differentiated intervention and cognitive consistency mechanisms for reliable knowledge augmentation.

## Method

It uses internal cognitive signals to partition the knowledge space into mastered, confused, and missing regions, guides targeted expansion, and synchronizes subjective certainty with objective accuracy through cognitive consistency.

## Experiments and Evidence

The abstract reports consistent improvements over strong baselines in both knowledge capability and behaviors that distinguish knowns from unknowns.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: cognitive signal definitions, partition calibration, intervention data, benchmark suite, and robustness to adversarial uncertainty prompts.

## Deep Themes

- Knowledge augmentation should be uncertainty-aware and region-specific.
- Models need calibrated boundaries between known, confused, and missing knowledge.
- Metacognition is becoming an operational training/control target.

## Subthemes

- Knowledge augmentation.
- Metacognition.
- Known/unknown calibration.
- Internal cognitive signals.
- Targeted expansion.
- Confidence alignment.

## Connections to Other Papers

Connects to Binary RAR, BNRM, VALUEFLOW, and uncertainty/debate papers through calibration of internal confidence and external correctness.

## Notes for Cross-Paper Synthesis

This paper reinforces the metacognitive-control theme: improving knowledge is not only adding facts, but teaching the model where its knowledge boundaries are.
