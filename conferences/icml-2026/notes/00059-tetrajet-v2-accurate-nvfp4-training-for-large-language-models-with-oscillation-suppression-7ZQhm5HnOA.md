# TetraJet-v2: Accurate NVFP4 Training for Large Language Models with Oscillation Suppression and Outlier Control

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7ZQhm5HnOA
- Authors: Yuxiang Chen; Yifan Liu; Xiaoming Xu; Pengle Zhang; Michael Beyer; Martin Rapp; Jun Zhu; Jianfei Chen
- Primary area: deep_learning->algorithms
- Keywords: Efficient Machine Learning;Low-Precision Training;Quantization;FP4
- Source URL: https://openreview.net/forum?id=7ZQhm5HnOA
- PDF URL: https://openreview.net/pdf?id=7ZQhm5HnOA

## Abstract

Large Language Models (LLMs) training is prohibitively expensive, driving interest in low-precision fully-quantized training (FQT).
While novel 4-bit formats like NVFP4 offer substantial efficiency gains, achieving near-lossless training at such low precision remains challenging.
We introduce **TetraJet-v2**, an end-to-end 4-bit FQT method that leverages NVFP4 for activations, weights and gradients in all linear layers.
We identify two critical issues hindering low-precision LLM training: weight oscillation and outliers. 
To address these, we propose: 1) an unbiased double-block quantization method for NVFP4 linear layers, 2) **OsciReset**, an algorithm to suppress weight oscillation, and 3) **OutControl**, an algorithm to retain outlier accuracy. **TetraJet-v2** outperforms prior methods on FP4 pre-training for LLMs across models up to 370M parameters trained up to 212B tokens, reducing the performance gap to BF16 by an average of $51.3$% while enabling an $1.67\times$ end-to-end speedup over FP8.

## One-Sentence Claim

TetraJet-v2 makes fully NVFP4 LLM pretraining more accurate by addressing weight oscillation and activation outliers while using 4-bit activations, weights, and gradients in linear layers.

## Problem

FP4 fully quantized training promises major speed and memory gains, but near-lossless LLM pretraining at 4 bits is difficult because quantized weights oscillate and outliers are poorly represented.

## Core Contribution

The paper introduces an end-to-end NVFP4 fully quantized training recipe with unbiased double-block quantization, OsciReset for weight oscillation suppression, and OutControl for outlier accuracy.

## Method

TetraJet-v2 implements NVFP4 linear layers for activations, weights, and gradients, uses stochastic/unbiased gradient handling, resets weights toward quantization bin centers to reduce oscillation, and keeps selected outlier channels at higher precision or controlled precision paths.

## Experiments and Evidence

The abstract reports FP4 pretraining across models up to 370M parameters and 212B tokens, reducing the gap to BF16 by 51.3% on average and enabling 1.67x end-to-end speedup over FP8.

## Full-Text Upgrade

The full text identifies weight oscillation as a dominant FP4 failure mode: small high-precision updates can repeatedly cross quantization bins, producing unstable effective FP4 weights. OsciReset targets this by resetting weights to bin centers after quantization events. OutControl targets persistent activation outliers by selecting outlier channels and handling them with higher-precision or mixed-precision paths.

Experiments use OLMo-2 models at 70M, 150M, and 370M parameters trained for 52B, 107B, and 212B tokens. TetraJet-v2-full combines the base NVFP4 layer with OsciReset and OutControl, improving perplexity and downstream task averages over prior FP4 recipes. The CUDA implementation reports faster linear layers than TransformerEngine FP8 and converts this into end-to-end speedups.

## Limits and Failure Modes

Limits to watch: evaluations are up to 370M parameters rather than frontier scale; outlier selection and kernel implementation are system-specific; and maintaining higher precision for selected channels complicates the purity and portability of fully FP4 training.

## Deep Themes

- Low-precision training failures are dynamic, not only representational.
- Quantization methods need optimizer- and hardware-aware correction mechanisms.
- Deployment efficiency increasingly requires custom numerical kernels plus training algorithms.

## Subthemes

- FP4 training.
- NVFP4.
- Fully quantized training.
- Weight oscillation.
- Activation outliers.
- CUDA kernel acceleration.

## Connections to Other Papers

Connects to Why Low-Precision Transformer Training Fails, LiftQuant, and quantized diffusion error propagation as part of the numerical ML systems cluster.

## Notes for Cross-Paper Synthesis

TetraJet-v2 adds a low-precision training theme: making extreme quantization work requires identifying the specific temporal failure modes introduced by quantized updates.
