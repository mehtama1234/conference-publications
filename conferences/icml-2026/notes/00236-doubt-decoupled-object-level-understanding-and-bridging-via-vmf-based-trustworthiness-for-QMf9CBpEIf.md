# DOUBT: Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness for Hallucination Detection in MLLMs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: QMf9CBpEIf
- Authors: Kaiqi Chen; Yang Qin; Changhao He; Xi Peng; Peng Hu
- Primary area: deep_learning
- Keywords: Hallucination Detection;  Object-Level Understanding and Bridging; von Mises–Fisher Distribution
- Source URL: https://openreview.net/forum?id=QMf9CBpEIf
- PDF URL: https://openreview.net/pdf?id=QMf9CBpEIf

## Abstract

Multimodal Large Language Models (MLLMs) frequently produce hallucinations (i.e., assertions that contradict the image or facts), undermining reliability in high-risk applications. Existing detection approaches typically feed images and texts jointly and estimate hallucination scores by measuring the consistency of model outputs. However, because the visual module often lags behind the language module in understanding and reasoning, MLLMs can repeatedly produce similar yet incorrect answers, yielding overestimated trustworthiness and missed detections. To address this, we propose a simple yet effective model-agnostic method, dubbed Decoupled Object-level Understanding and Bridging via vMF-based Trustworthiness (DOUBT). DOUBT first employs Object-level Understanding and Bridging (OUB), a two-step prompting scheme that decouples object recognition from relational reasoning by prompting the model to identify objects and then reason based on them. It further introduces a von Mises-Fisher (vMF)-based trustworthiness metric, which is more stable than semantic entropy metrics in small-sample settings. Extensive experiments and ablation studies on multiple benchmarks show that DOUBT consistently outperforms state-of-the-art baselines, demonstrating its robustness and generalizability for hallucination detection in MLLMs. The code is available at https://github.com/XLearning-SCU/2026-ICML-DOUBT.

## One-Sentence Claim

DOUBT detects MLLM hallucinations by decoupling object recognition from relational reasoning and scoring trustworthiness with a vMF-based metric robust in small-sample settings.

## Problem

MLLM hallucination detectors can overestimate trustworthiness when models repeatedly produce similar but wrong answers because the language module outpaces visual understanding.

## Core Contribution

The paper introduces a model-agnostic detection method that combines Object-level Understanding and Bridging prompting with von Mises-Fisher trustworthiness estimation.

## Method

DOUBT first prompts the model to identify objects, then prompts relational reasoning grounded in those objects, separating recognition from bridging. It then computes a vMF-based trustworthiness score intended to be more stable than semantic entropy under few samples.

## Experiments and Evidence

The abstract reports extensive experiments and ablations across multiple benchmarks where DOUBT outperforms state-of-the-art baselines and generalizes robustly.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark list, vMF feature choice, sampling budget, sensitivity to object-recognition errors, model families, and whether detection works for subtle relational hallucinations.

## Deep Themes

- Hallucination detection should separate perception from reasoning.
- Trustworthiness metrics must handle repeated wrong answers and small samples.
- Object-level grounding is a useful intermediate layer for MLLM reliability.

## Subthemes

- MLLM hallucination detection.
- Object-level prompting.
- Relational reasoning.
- von Mises-Fisher distribution.
- Trustworthiness estimation.
- Model-agnostic evaluation.

## Connections to Other Papers

Connects to causal route gating, FlowGuard, VGS, and 3ViewSense through multimodal grounding and decomposed reliability diagnostics.

## Notes for Cross-Paper Synthesis

DOUBT adds a detection-side grounding theme: consistency among outputs is insufficient if perception is wrong; detectors need object-level evidence checks.
