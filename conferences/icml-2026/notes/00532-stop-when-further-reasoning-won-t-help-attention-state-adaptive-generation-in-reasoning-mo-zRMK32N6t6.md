# Stop When Further Reasoning Won’t Help: Attention-State Adaptive Generation in Reasoning Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: zRMK32N6t6
- Authors: Jiakai Li; Ke Qin; Rongzheng Wang; Yizhuo Ma; Qizhi Chen; Muquan Li; Shuang Liang
- Primary area: deep_learning->large_language_models
- Keywords: large language model;overthinking;attention mechanism
- Source URL: https://openreview.net/forum?id=zRMK32N6t6
- PDF URL: https://openreview.net/pdf?id=zRMK32N6t6

## Abstract

By incorporating test-time compute scaling, large reasoning models (LRMs) can solve complex problems through explicit chain-of-thought (CoT) reasoning processes. 
However, they often suffer from overthinking, resulting in redundant token outputs and degraded accuracy. 
Current methods to mitigate this issue remain limited: training-based approaches require substantial computational resources, while training-free methods rely on well-crafted prompts or unreliable confidence signals.
In this work, we investigate early stopping from the perspective of attention distributions and propose a simple method, ASAG, which infers the model's reasoning state and adaptively adjusts the generation strategy. 
The proposed framework is training-free and plug-and-play, enabling seamless integration into existing LRMs.
Extensive experiments on nine benchmarks demonstrate consistent improvements across mainstream LRMs with varying parameter scales, including the DeepSeek-R1-Distill and Qwen3 series.
Specifically, ASAG improves average accuracy by 3.2% while reducing the number of generated tokens by nearly 40% across all reasoning tasks on Qwen3-8B.

## One-Sentence Claim

ASAG reduces overthinking in reasoning models by using attention distributions to infer reasoning state and adapt generation without training.

## Problem

Large reasoning models benefit from test-time compute and explicit chain-of-thought, but they can overthink: generating redundant tokens and sometimes degrading accuracy.

Existing overthinking mitigations are limited because training-based methods are costly and training-free methods often rely on prompt tricks or unreliable confidence signals.

## Core Contribution

The paper proposes ASAG, Attention-State Adaptive Generation, a plug-and-play training-free framework that adjusts generation strategy based on inferred reasoning state from attention distributions.

The contribution is a model-internal stopping/control signal for reasoning length that does not require retraining or hand-crafted prompts.

## Method

ASAG analyzes attention distributions during generation to infer whether further reasoning is likely useful. It then adaptively changes generation behavior, likely stopping or redirecting continuation when the attention-state signal indicates overthinking.

Because it is plug-and-play, it can be integrated with existing reasoning models at inference time.

## Experiments and Evidence

The abstract reports experiments on nine benchmarks and improvements across mainstream LRMs with different scales, including DeepSeek-R1-Distill and Qwen3 series.

On Qwen3-8B, ASAG improves average accuracy by 3.2 percent while reducing generated tokens by nearly 40 percent across reasoning tasks.

## Limits and Failure Modes

Attention-state signals may not reliably separate productive deliberation from overthinking in all tasks. Premature stopping could hurt problems requiring long multi-step reasoning.

Because this note is abstract-only, details still need checking: attention features used, stopping rule, benchmarks, per-task tradeoffs, compatibility with sampling settings, and whether hidden-answer leakage through attention is possible.

## Deep Themes

- Adaptive test-time compute: reasoning should stop when marginal value turns negative.
- Attention as process-state signal: internal distributions can guide inference control.
- Overthinking as accuracy risk: more CoT is not always better.
- Training-free reasoning control: inference wrappers can improve both cost and accuracy.

## Subthemes

- Attention-state generation policy.
- Token reduction in LRMs.
- Plug-and-play early stopping.
- Reasoning length calibration.

## Connections to Other Papers

This connects to PonderLM-2, Ctrl-R, H1, and reasoning dimensionality through compute allocation for reasoning. It also relates to EntroKV and Information Flow because attention statistics become operational signals.

It complements PonderLM-2: one adds hidden computation, the other decides when visible reasoning should stop.

## Notes for Cross-Paper Synthesis

ASAG strengthens the test-time-control theme: effective reasoning requires deciding not only how to reason, but when additional reasoning has become harmful or wasteful.
