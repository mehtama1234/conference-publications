# WaterSIC: Information-Theoretically (Near) Optimal \\Linear Layer Quantization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fCPgAHIciE
- Authors: Egor Lifar; Semyon Savkin; Or Ordentlich; Yury Polyanskiy
- Primary area: deep_learning->large_language_models
- Keywords: large language models;quantization
- Source URL: https://openreview.net/forum?id=fCPgAHIciE
- PDF URL: https://openreview.net/pdf?id=fCPgAHIciE

## Abstract

This paper considers the problem of converting a given dense linear layer to low precision. The tradeoff between compressed length and output discrepancy is analyzed information theoretically (IT). It is shown that a popular
    GPTQ algorithm may have an arbitrarily large gap to the IT limit. To alleviate this problem, a
 novel algorithm, termed "WaterSIC", is proposed and is shown to be within a rate gap of
    0.255 bits to the IT limit, uniformly over all possible covariance matrices of input activations.
 The key innovation of WaterSIC's is to allocate different quantization rates to different columns
    (in-features) of the weight matrix, mimicking the classical IT solution known as
    ``waterfilling''. Applying WaterSIC to the Llama and Qwen family of LLMs establishes new
    state-of-the-art performance for all quantization rates from 1 to 4 bits. Our code is available at https://github.com/egorlifar/watersic.

## One-Sentence Claim

WaterSIC quantizes linear layers near the information-theoretic rate-distortion limit by allocating precision across columns using a waterfilling-style rule.

## Problem

LLM quantization is usually evaluated empirically, but low-precision conversion of a dense linear layer has an underlying rate-distortion tradeoff: how many compressed bits are needed for a target output discrepancy under input activations.

The paper asks how far common algorithms such as GPTQ are from this information-theoretic limit and how to close that gap uniformly across activation covariance structures.

## Core Contribution

The paper analyzes dense linear-layer quantization information theoretically and shows that GPTQ can have an arbitrarily large gap to the optimal limit. It proposes WaterSIC, which is uniformly within 0.255 bits of the information-theoretic limit over all input-activation covariance matrices.

The key algorithmic idea is column-wise rate allocation, analogous to classical waterfilling: different in-features receive different quantization rates depending on their contribution to output discrepancy.

## Method

WaterSIC assigns quantization precision nonuniformly across columns of the weight matrix. Columns that matter more under the activation covariance receive more rate, while less consequential columns receive less.

The method is motivated by information-theoretic rate-distortion analysis rather than only empirical error heuristics.

## Experiments and Evidence

Evidence reported in the abstract:

- GPTQ can be arbitrarily far from the information-theoretic limit.
- WaterSIC is within a 0.255-bit rate gap uniformly over all covariance matrices.
- State-of-the-art performance on Llama and Qwen models for 1-to-4-bit quantization.
- Code release at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact discrepancy metric, proof assumptions, calibration data, and downstream tasks.

## Limits and Failure Modes

- Layerwise information-theoretic optimality may not fully predict end-to-end model quality.
- Activation covariance estimates can be calibration-data dependent.
- Nonuniform rate allocation may complicate hardware kernels or storage formats.
- The theoretical guarantee covers the modeled quantization problem, not necessarily all deployment constraints.

## Deep Themes

**Compression is being re-grounded in information theory.** WaterSIC asks what quantization should achieve before choosing a heuristic.

**Not all weights deserve equal bits.** Precision is allocated according to activation-informed functional importance.

**Theory exposes hidden baseline gaps.** GPTQ's empirical popularity does not imply closeness to the optimal rate-distortion frontier.

## Subthemes

- Rate-distortion linear-layer quantization.
- Waterfilling precision allocation.
- Activation covariance-aware compression.
- 1-to-4-bit LLM quantization.
- Theory-to-systems compression.

## Connections to Other Papers

Connects to ReQAT, MACKO-SpMV, EMP, POET-X, and FlashSketch. It complements ReQAT by treating quantization as a layerwise information-theoretic allocation problem rather than primarily a training recipe.

## Notes for Cross-Paper Synthesis

WaterSIC is a strong example of the 2026 efficiency pattern: mature systems bottlenecks are being reframed as precise mathematical allocation problems, then pushed back into practical LLM deployment.
