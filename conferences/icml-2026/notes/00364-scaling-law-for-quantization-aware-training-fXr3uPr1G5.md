# Scaling Law for Quantization-Aware Training

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fXr3uPr1G5
- Authors: Mengzhao Chen; Chaoyi Zhang; Jing Liu; Yutao Zeng; Zeyue Xue; Zhiheng Liu; Yunshui Li; Jin Ma; Jie Huang; zhou Xun; Ping Luo
- Primary area: deep_learning->large_language_models
- Keywords: Large language models;Scaling law，Quantization-aware training
- Source URL: https://openreview.net/forum?id=fXr3uPr1G5
- PDF URL: https://openreview.net/pdf?id=fXr3uPr1G5

## Abstract

Large language models (LLMs) demand substantial computational and memory resources, creating deployment challenges. Quantization-aware training (QAT) addresses these challenges by reducing model precision while maintaining performance. However, the scaling behavior of QAT, especially at 4-bit precision (W4A4), is not well understood. Existing QAT scaling laws often ignore key factors such as the number of training tokens and quantization granularity, which limits their applicability. This paper proposes a unified scaling law for QAT that models quantization error as a function of model size, training data volume, and quantization group size. Through 268 QAT experiments, we show that quantization error decreases as model size increases, but rises with more training tokens and coarser quantization granularity. To identify the sources of W4A4 quantization error, we decompose it into weight and activation components. Both components follow the overall trend of W4A4 quantization error, but with different sensitivities. Specifically, weight quantization error increases more rapidly with more training tokens. Further analysis shows that the activation quantization error in the FC2 layer, caused by outliers, is the primary bottleneck of W4A4 QAT quantization error. By applying mixed-precision quantization to address this bottleneck, we demonstrate that weight and activation quantization errors can converge to similar levels. Additionally, with more training data, weight quantization error eventually exceeds activation quantization error, suggesting that reducing weight quantization error is also important in such scenarios. These findings offer key insights for improving QAT research and development.

## One-Sentence Claim

QAT quantization error follows a scaling law over model size, training tokens, and group size, with W4A4 bottlenecks shifting between activation and weight errors.

## Problem

Quantization-aware training is central to LLM deployment, especially W4A4 quantization, but its scaling behavior is poorly understood. Existing scaling laws often omit training-token count and quantization granularity, limiting their usefulness for planning QAT experiments.

The paper asks how quantization error changes with model size, data volume, and group size, and which components dominate the W4A4 error.

## Core Contribution

The contribution is a unified QAT scaling law modeling quantization error as a function of model size, training data volume, and quantization group size. Across 268 QAT experiments, the paper finds that quantization error decreases with model size but increases with more training tokens and coarser granularity.

It decomposes W4A4 error into weight and activation components, identifies FC2 activation outliers as a primary bottleneck, and shows mixed precision can rebalance weight and activation errors.

## Method

The authors run a large grid of QAT experiments and fit a scaling model over architecture/training axes. They separately measure weight- and activation-induced quantization error to isolate which component drives degradation.

Mixed-precision quantization is then applied to address the activation bottleneck, especially in FC2 layers affected by outliers.

## Experiments and Evidence

Evidence reported in the abstract:

- 268 QAT experiments.
- Unified scaling law over model size, training tokens, and quantization group size.
- Quantization error decreases with model size.
- Quantization error increases with more training tokens and coarser granularity.
- W4A4 error decomposed into weight and activation components.
- FC2 activation outliers identified as the primary W4A4 bottleneck.
- Mixed precision can make weight and activation errors converge to similar levels.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model families, loss metric, data regimes, and fitted-law exponents.

## Limits and Failure Modes

- Scaling laws may extrapolate poorly outside the tested model sizes and data regimes.
- More training tokens increasing quantization error is counterintuitive and needs careful interpretation against baseline loss.
- Mixed precision improves bottlenecks but may complicate hardware kernels.
- Layer-specific outlier behavior may vary across architectures.

## Deep Themes

**Quantization has scaling behavior, not just recipes.** Deployment choices can be planned using empirical laws.

**Bottlenecks move with scale.** Activation outliers dominate in one regime, but weight quantization can dominate as training data grows.

**Hardware-friendly compression requires error accounting.** The useful question is where each bit prevents the most damage.

## Subthemes

- W4A4 quantization-aware training.
- QAT scaling laws.
- Training-token effects on quantization error.
- FC2 activation outliers.
- Mixed-precision bottleneck repair.

## Connections to Other Papers

Connects to WaterSIC, ReQAT, MACKO-SpMV, EMP, and POET-X. It complements WaterSIC by providing empirical scaling behavior where WaterSIC provides information-theoretic allocation.

## Notes for Cross-Paper Synthesis

This paper deepens the efficiency theme: compression quality depends on model scale, data scale, and granularity jointly, so deployment cannot be optimized by a single global bit-width rule.
