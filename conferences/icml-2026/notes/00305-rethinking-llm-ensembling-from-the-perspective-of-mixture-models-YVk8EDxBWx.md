# Rethinking LLM Ensembling from the Perspective of Mixture Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: YVk8EDxBWx
- Authors: Jiale Fu; Yuchu Jiang; PeiJun WU; Chonghan Liu; Joey Tianyi Zhou; Xu Yang
- Primary area: deep_learning->large_language_models
- Keywords: LLM Ensembing;Mixture models;Token-level routing
- Source URL: https://openreview.net/forum?id=YVk8EDxBWx
- PDF URL: https://openreview.net/pdf?id=YVk8EDxBWx

## Abstract

Model ensembling is a well-established technique for improving the performance of machine learning models. Conventionally, this involves averaging the output distributions of multiple models and selecting the most probable label. This idea has been naturally extended to large language models (LLMs), yielding improved performance but incurring substantial computational cost. This inefficiency stems from directly applying conventional ensemble implementation to LLMs, which require a separate forward pass for each model to explicitly compute the ensemble distribution. In this paper, we propose the Mixture-model-like Ensemble (ME). By reinterpreting the ensemble as a mixture model, ME stochastically selects a single model at each step to generate the next token, thereby avoiding the need to explicitly compute the full ensemble distribution. ME is mathematically equivalent to sampling from the ensemble distribution, but requires invoking only one model, making it 1.78×-2.68× faster than conventional ensembling. Furthermore, this perspective connects LLM ensembling and token-level routing methods, suggesting that LLM ensembling is a special case of routing methods. Our findings open new avenues for efficient LLM ensembling and motivate further exploration of token-level routing strategies for LLMs. Our code is available at https://github.com/Kamichanw/Mixture-model-like-Ensemble.

## One-Sentence Claim

LLM ensembling can be sampled exactly as a mixture model by routing each token to one selected model, avoiding full multi-model forward passes.

## Problem

Ensembling improves model performance by averaging output distributions, but applying this directly to LLMs is expensive because every decoding step requires a forward pass through every model. This makes conventional LLM ensembling costly for generation.

The paper asks whether the ensemble distribution can be sampled without explicitly computing all model outputs at every step.

## Core Contribution

The paper proposes Mixture-model-like Ensemble, or ME. It reinterprets an LLM ensemble as a mixture model and stochastically selects a single model at each token step to generate the next token.

ME is mathematically equivalent to sampling from the ensemble distribution while invoking only one model per step. It is 1.78x-2.68x faster than conventional ensembling and connects LLM ensembling to token-level routing.

## Method

Instead of averaging all model next-token distributions and sampling from that mixture explicitly, ME samples the mixture component first: choose a model according to mixture weights, then sample the token from that model. This gives the same marginal token distribution as the explicit ensemble under the stated sampling setup.

The perspective reframes ensemble decoding as token-level routing over component LLMs.

## Experiments and Evidence

Evidence reported in the abstract:

- Mathematical equivalence to sampling from the ensemble distribution.
- Only one model invoked per token step.
- 1.78x-2.68x speedup versus conventional ensembling.
- Empirical performance improvements from ensembling retained.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: mixture weights, decoding settings, quality metrics, diversity effects, and whether equivalence holds under top-k/top-p/temperature transformations.

## Limits and Failure Modes

- Equivalence may depend on exact sampling semantics and can break under common decoding approximations.
- Routing a single model per token may increase variance across generations.
- Latency and memory depend on whether all models are resident in memory.
- Ensemble benefits may be task-dependent and sensitive to component diversity.

## Deep Themes

**Sampling order can remove redundant computation.** Choosing the mixture component before the token avoids computing unused distributions.

**Ensembling is token-level routing.** The method unifies classical ensemble averaging with routing-style LLM inference.

**Inference efficiency often comes from probabilistic reformulation.** The same distribution can be sampled through a cheaper computational path.

## Subthemes

- Mixture-model view of ensembles.
- Token-level model routing.
- Exact ensemble sampling.
- Faster multi-LLM decoding.
- Component diversity and routing variance.

## Connections to Other Papers

Connects to WeDLM, FlashSinkhorn, WBMM, and other efficiency papers through computational reformulation. It also links to DLMR, TG-RAG, and routing/memory papers where selecting the right component at the right step is central.

## Notes for Cross-Paper Synthesis

ME adds another example of a broad efficiency pattern: keep the mathematical object but change the sampling or execution order so most computation is never performed.
