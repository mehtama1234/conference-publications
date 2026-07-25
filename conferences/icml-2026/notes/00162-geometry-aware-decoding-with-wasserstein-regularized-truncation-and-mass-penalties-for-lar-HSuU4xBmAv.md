# Geometry-Aware Decoding with Wasserstein-Regularized Truncation and Mass Penalties for Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: HSuU4xBmAv
- Authors: Arash Gholami Davoodi; Navid Rezazadeh; Seyed Pouyan Mousavi Davoudi; Pouya Pezeshkpour
- Primary area: deep_learning->large_language_models
- Keywords: Large language models;decoding;sampling;truncation;Wasserstein distance;token embedding geometry;entropy control
- Source URL: https://openreview.net/forum?id=HSuU4xBmAv
- PDF URL: https://openreview.net/pdf?id=HSuU4xBmAv

## Abstract

Large language models (LLMs) must balance diversity and creativity against logical coherence in open-ended generation. 
Existing truncation-based samplers are effective but largely heuristic, relying mainly on probability mass and entropy while ignoring semantic geometry of the token space.
We present Top-$W$, a geometry-aware truncation rule that uses Wasserstein distance—defined over token-embedding geometry—to keep the cropped distribution close to the original, while explicitly balancing retained probability mass against the entropy of the kept set. 
Our theory yields a simple closed-form structure for the fixed-potential subset update: depending on the mass–entropy trade-off, the optimal crop either collapses to a single token or takes the form of a one-dimensional prefix that can be found efficiently with a linear scan. 
We implement Top-$W$ using efficient geometry-based potentials (nearest-set or $k$-NN) and pair it with an alternating decoding routine that keeps the standard truncation-and-sampling interface unchanged.
Extensive experiments on four benchmarks (GSM8K, GPQA, AlpacaEval, and MT-Bench) across three instruction-tuned models show that Top-$W$ consistently outperforms prior state-of-the-art decoding approaches achieving up to 33.7 percentage improvement. 
Moreover, we find that Top-$W$ not only improves accuracy-focused performance, but also boosts creativity under judge-based open-ended evaluation.

## One-Sentence Claim

Top-W improves LLM decoding by truncating token distributions with Wasserstein regularization over embedding geometry while balancing retained mass and entropy.

## Problem

Common truncation samplers manage probability mass and entropy heuristically but ignore semantic geometry, which can hurt the diversity-coherence tradeoff in open-ended generation.

## Core Contribution

The paper introduces a geometry-aware truncation rule with a theoretically characterized crop structure and an efficient decoding routine that preserves the standard sample-after-truncation interface.

## Method

Top-W defines Wasserstein distance over token embeddings, uses geometry-based potentials such as nearest-set or k-NN potentials, and alternates truncation with sampling. The theory shows that a fixed-potential subset update either collapses to one token or becomes a one-dimensional prefix found by linear scan depending on the mass-entropy tradeoff.

## Experiments and Evidence

The abstract reports experiments on GSM8K, GPQA, AlpacaEval, and MT-Bench across three instruction-tuned models, with consistent gains over prior decoding methods and up to 33.7 percentage-point improvement. It also reports better judge-evaluated creativity.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model list, decoding hyperparameters, judge setup, latency overhead, sensitivity to embedding choice, and whether gains persist for long-form factual generation.

## Deep Themes

- Token-space geometry as a decoding-time control surface.
- Test-time sampling policy can materially change reasoning and creativity.
- Formal structure can replace heuristic truncation rules without changing user-facing decoding interfaces.

## Subthemes

- LLM decoding.
- Wasserstein distance.
- Token embeddings.
- Truncation sampling.
- Entropy control.
- Creativity versus coherence.

## Connections to Other Papers

Connects to test-time scaling and inference-control papers, as well as representation-geometry work that turns latent structure into an actionable algorithmic constraint.

## Notes for Cross-Paper Synthesis

Top-W reinforces the theme that inference procedures are now a major source of capability: even with fixed models, better geometry-aware sampling can shift accuracy, reasoning, and open-ended quality.
