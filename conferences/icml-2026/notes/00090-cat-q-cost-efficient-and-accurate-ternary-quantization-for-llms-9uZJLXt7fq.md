# CAT-Q: Cost-efficient and Accurate Ternary Quantization for LLMs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9uZJLXt7fq
- Authors: Shigeng Wang; Chao Li; Yangyuxuan Kang; Jiawei Fan; Anbang Yao
- Primary area: deep_learning->large_language_models
- Keywords: LLM quantization;post-training quantization;quantization-aware training;ternary models
- Source URL: https://openreview.net/forum?id=9uZJLXt7fq
- PDF URL: https://openreview.net/pdf?id=9uZJLXt7fq

## Abstract

In this paper, we present CAT-Q, **C**ost-efficient and **A**ccurate **T**ernary **Q**uantization, for compressing and accelerating LLMs. Unlike existing state-of-the-art ternary quantization methods that rely on data-intensive and costly quantization-aware training to mitigate severe performance degradation, CAT-Q is a simple yet effective post-training quantization scheme that is readily applicable to LLMs with diverse architectures and model sizes. It has two key components, learnable modulation (LM) and softened ternarization (ST), which are coupled from an optimization perspective. LM leverages a composition of learnable factors to modulate the distribution of pre-trained high-precision weights and the ternary threshold, making them less sensitive to ternarization. ST further introduces a differentiable transition function to guide the ternarization process toward stable convergence. We show that, for pre-trained LLMs with 1.7B to 8B parameters, CAT-Q can efficiently quantize them into ternary models using only 512 calibration samples, while achieving superior performance than the seminal BitNet 1.58-bit v1 and v2 families (with 1.3B to 7B parameters) trained with 100B tokens, yielding about a 100,000$\times$ reduction in training tokens. Moreover, we show for the first time that CAT-Q can quantize much larger pre-trained LLMs having 14B to 235B parameters into leading ternary models within just 8 to 60 hours on 8 A100-80GB GPUs. Code is available at https://github.com/IntelChina-AI/BitTern.

## One-Sentence Claim

CAT-Q ternarizes pretrained LLMs with a lightweight post-training scheme using learnable modulation and softened ternarization instead of costly quantization-aware training.

## Problem

State-of-the-art ternary LLM quantization often relies on data-intensive QAT to avoid severe degradation, making compression expensive and hard to apply broadly.

## Core Contribution

The paper introduces CAT-Q, a post-training ternary quantization method that works across architectures and sizes with only a small calibration set.

## Method

CAT-Q couples learnable modulation, which adjusts pretrained weight distributions and ternary thresholds, with softened ternarization, a differentiable transition function that stabilizes convergence toward ternary weights.

## Experiments and Evidence

The abstract reports quantizing 1.7B-8B LLMs with only 512 calibration samples while outperforming BitNet 1.58-bit v1/v2 models trained with 100B tokens. It also reports quantizing 14B-235B pretrained LLMs into leading ternary models within 8-60 hours on 8 A100-80GB GPUs.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv is currently being deferred after repeated 429/503 errors. Details still need checking: calibration data sensitivity, hardware speedups, activation precision, benchmark coverage, and behavior on instruction-following/safety tasks.

## Deep Themes

- Extreme quantization is shifting from training-from-scratch to post-training conversion.
- Tiny calibration sets can be sufficient if optimization smooths the ternarization path.
- Cost-efficient compression matters for very large deployed LLMs.

## Subthemes

- Ternary quantization.
- Post-training quantization.
- Learnable modulation.
- Softened ternarization.
- Calibration efficiency.
- Large-model compression.

## Connections to Other Papers

Connects to TetraJet-v2, LiftQuant, OmniFit, TACO, and EcoVLA through compression as a capability enabler. It also links to floating-point/low-precision theory through numerical representation constraints.

## Notes for Cross-Paper Synthesis

CAT-Q strengthens the efficient-frontier theme: aggressive compression becomes more practical when the method adapts pretrained weights instead of retraining from scratch.
