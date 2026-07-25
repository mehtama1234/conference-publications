# Towards Long-Horizon Interpretability: Efficient and Faithful Multi-Token Attribution for Reasoning LLMs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: KY5Q9V9F5C
- Authors: Wenbo Pan; Zhichao Liu; Xianlong Wang; Yu Haining; Xiaohua Jia
- Primary area: deep_learning->large_language_models
- Keywords: Interpretability;Token Attribution;Long-Context Reasoning;Large Language Models;Efficient Attribution
- Source URL: https://openreview.net/forum?id=KY5Q9V9F5C
- PDF URL: https://openreview.net/pdf?id=KY5Q9V9F5C

## Abstract

Token attribution methods provide intuitive explanations for language model outputs by identifying causally important input tokens. However, as modern LLMs increasingly rely on extended reasoning chains, existing schemes face two critical challenges: (1) efficiency bottleneck, where attributing a target span of $M$ tokens within a context of length $N$ requires $\mathcal{O}(M \cdot N)$ operations, making long-context attribution prohibitively slow; and (2) faithfulness drop, where intermediate reasoning tokens absorb attribution mass, preventing importance from propagating back to the original input. To address these, we introduce FlashTrace, an efficient multi-token attribution method that employs span-wise aggregation to compute attribution over multi-token targets in a single pass, while maintaining faithfulness. Moreover, we design a recursive attribution mechanism that traces importance through intermediate reasoning chains back to source inputs. Extensive experiments on long-context retrieval (RULER) and multi-step reasoning (MATH, MorehopQA) tasks demonstrate that FlashTrace achieves over $130\times$ speedup over existing baselines while maintaining superior faithfulness. We further analyze the dynamics of recursive attribution, showing that even a single recursive hop improves faithfulness by tracing importance through the reasoning chain.

## One-Sentence Claim

FlashTrace provides efficient and faithful multi-token attribution for long-context reasoning LLMs by aggregating spans and recursively tracing importance through reasoning chains.

## Problem

Existing token-attribution methods are too slow for long target spans and lose faithfulness because intermediate reasoning tokens absorb attribution mass instead of passing importance back to source inputs.

## Core Contribution

The paper introduces span-wise multi-token attribution in a single pass and recursive attribution that propagates importance through intermediate reasoning steps to original inputs.

## Method

FlashTrace aggregates target spans to avoid O(M*N) attribution over M output tokens and N context tokens, then recursively attributes intermediate reasoning tokens to earlier sources to recover faithful long-horizon causal importance.

## Experiments and Evidence

The abstract reports over 130x speedup versus existing baselines while maintaining superior faithfulness on RULER, MATH, and MorehopQA, with even one recursive hop improving faithfulness.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: attribution baseline set, faithfulness metric, recursive stopping criteria, memory cost, long-context lengths, and whether recursive attribution amplifies spurious intermediate tokens.

## Deep Themes

- Interpretability must scale to long reasoning chains.
- Faithful explanation requires tracing through process, not stopping at intermediate tokens.
- Attribution is becoming both a diagnostic and a systems-efficiency problem.

## Subthemes

- Token attribution.
- Long-context reasoning.
- Multi-token targets.
- Recursive attribution.
- RULER, MATH, MorehopQA.
- Faithfulness and efficiency.

## Connections to Other Papers

Connects to TRM, Faire, and LALP through reasoning-process analysis, and to long-context papers where efficient algorithms are needed to inspect extended model behavior.

## Notes for Cross-Paper Synthesis

FlashTrace adds an interpretability counterpart to long-horizon reasoning: if models reason through many tokens, explanations must follow the chain back to source evidence efficiently.
