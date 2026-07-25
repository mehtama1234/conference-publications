# In-Place Test-Time Training

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: dTWfCLSoyl
- Authors: Guhao Feng; Shengjie Luo; Kai Hua; Ge Zhang; Wenhao Huang; Di He; Tianle Cai
- Primary area: foundation or frontier models, including LLMs
- Keywords: Test-time Training;Large language model;LLM
- Source URL: https://openreview.net/forum?id=dTWfCLSoyl
- PDF URL: https://openreview.net/pdf?id=dTWfCLSoyl

## Abstract

The static "train then deploy" paradigm fundamentally limits Large Language Models (LLMs) from dynamically adapting their weights in response to continuous streams of new information inherent in real-world tasks. Test-Time Training (TTT) offers a compelling alternative by updating a subset of model parameters (fast weights) at inference time, yet its potential in the current LLM ecosystem is hindered by critical barriers including architectural incompatibility, computational inefficiency and misaligned fast weight objectives for language modeling. In this work, we introduce **In-Place Test-Time Training (In-Place TTT)**, a framework that seamlessly endows LLMs with Test-Time Training ability. In-Place TTT treats the final projection matrix of the ubiquitous MLP blocks as its adaptable fast weights, enabling a ``drop-in" enhancement for LLMs without costly retraining from scratch. Furthermore, we replace TTT's generic reconstruction objective with a tailored, theoretically-grounded objective explicitly aligned with the Next-Token-Prediction task governing autoregressive language modeling. This principled objective, combined with an efficient chunk-wise update mechanism, results in a highly scalable algorithm compatible with context parallelism. Extensive experiments validate our framework's effectiveness: as an in-place enhancement, it enables a 4B-parameter model to achieve superior performance on tasks with contexts up to 128k, and when pretrained from scratch, it consistently outperforms competitive TTT-related approaches. Ablation study results further provide deeper insights on our design choices. Collectively, our results establish In-Place TTT as a promising step towards a paradigm of continual learning in LLMs.

## One-Sentence Claim

In-Place TTT gives existing LLMs test-time training ability by adapting MLP final projection matrices with a next-token-prediction-aligned fast-weight objective.

## Problem

The static train-then-deploy paradigm prevents LLMs from updating weights in response to continuous streams of new task information.

Existing test-time training ideas face architectural incompatibility, computational inefficiency, and objectives poorly aligned with autoregressive language modeling.

## Core Contribution

The paper introduces In-Place Test-Time Training as a drop-in enhancement for LLMs.

It treats final projection matrices in common MLP blocks as fast weights and replaces generic reconstruction objectives with a theoretically grounded objective aligned to next-token prediction.

## Method

At inference time, the model updates selected MLP projection parameters using chunk-wise fast-weight updates over context.

The algorithm is designed to scale with context parallelism and avoid retraining the full model from scratch.

## Experiments and Evidence

The abstract reports that the method lets a 4B model achieve superior performance on tasks with contexts up to 128k.

When pretrained from scratch, it consistently outperforms competitive TTT-related approaches, and ablations support the design choices.

## Limits and Failure Modes

Updating weights at inference can introduce latency, instability, or unwanted adaptation to noisy context. It also raises serving reproducibility and safety questions if model state changes per request.

Because this note is abstract-only, details still need checking: fast-weight objective, update rule, chunk size, tasks, context lengths, compute overhead, and safeguards against harmful adaptation.

## Deep Themes

- Continual inference-time adaptation: LLMs update weights during use rather than only reading context.
- Fast weights inside standard architecture: TTT is implemented by adapting existing MLP projections.
- Objective alignment with language modeling: next-token prediction guides test-time updates.
- Long-context performance through adaptation: context is not only attended to, but used to change parameters.

## Subthemes

- Test-time training.
- Fast weights.
- MLP final projection adaptation.
- 128k-context tasks.

## Connections to Other Papers

This connects to HTI, Train-before-Test, p-less sampling, Reasoning with Sampling, and adaptation/control papers.

It also relates to memory and cache-compression methods because long-context use increasingly involves dynamic computation beyond static attention.

## Notes for Cross-Paper Synthesis

In-Place TTT adds a continual-adaptation theme: model behavior can be changed during inference through lightweight parameter updates, not just prompting or retrieval.
