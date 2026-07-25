# Decoupling The "What" and "Where" With Polar Coordinate Positional Embedding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: I3Z9za1EkO
- Authors: Anand Gopalakrishnan; Róbert Csordás; Jürgen Schmidhuber; Michael Curtis Mozer
- Primary area: deep_learning->attention_mechanisms
- Keywords: relative positional encoding;RoPE;Transformers;sequence modelling;length generalization;complex-valued activations
- Source URL: https://openreview.net/forum?id=I3Z9za1EkO
- PDF URL: https://openreview.net/pdf?id=I3Z9za1EkO

## Abstract

The attention mechanism in a Transformer architecture matches key to query based on both content—the what—and position in a sequence—the where. We present an analysis indicating that what and where are entangled in the popular rotary position embedding (RoPE). This entanglement can impair performance particularly when decisions require independent matches on these two factors. We propose an improvement to RoPE, which we call Polar Coordinate Position Embedding or PoPE, that eliminates the what-where confound. PoPE is far superior on a diagnostic task requiring indexing solely by position or by content. On autoregressive sequence modeling in music, genomic, and natural language domains, Transformers using PoPE as the positional encoding scheme outperform baselines using RoPE with respect to evaluation loss (perplexity) and downstream task performance. On language modeling, these gains persist across model scale, from 124M to 774M parameters. Crucially, PoPE shows strong zero-shot length extrapolation capabilities compared not only to RoPE but even a method designed for extrapolation, YaRN, which requires additional fine tuning and frequency interpolation.

## One-Sentence Claim

PoPE improves Transformer sequence modeling and length extrapolation by decoupling content matching from positional matching in rotary-style positional embeddings.

## Problem

RoPE entangles "what" and "where" in attention, which can hurt tasks that require independent matching by content or by position and weaken length generalization.

## Core Contribution

The paper analyzes the content-position confound in RoPE and proposes Polar Coordinate Position Embedding as a positional encoding that removes this entanglement.

## Method

PoPE represents positional information in a polar-coordinate formulation intended to keep content and sequence location separable during key-query matching. The paper evaluates the method on diagnostic indexing tasks and autoregressive modeling across music, genomics, and language.

## Experiments and Evidence

The abstract reports large gains on diagnostic position/content indexing, lower loss and better downstream performance versus RoPE in multiple domains, language-modeling gains from 124M to 774M parameters, and strong zero-shot length extrapolation versus RoPE and YaRN.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: mathematical form, compatibility with existing checkpoints, training cost, scaling beyond 774M parameters, context lengths tested, and domain-specific hyperparameters.

## Deep Themes

- Positional mechanisms encode assumptions about compositional generalization.
- Long-context performance depends on disentangling content from location.
- Small architectural changes can expose hidden failure modes in standard attention.

## Subthemes

- Relative positional encoding.
- RoPE.
- Length extrapolation.
- Complex-valued activations.
- Music, genomic, and language modeling.
- Content-position disentanglement.

## Connections to Other Papers

Connects to Robust Filter Attention and MuonSSM through long-context sequence mechanisms, and to representation-geometry papers that reinterpret architectural primitives through geometric structure.

## Notes for Cross-Paper Synthesis

PoPE reinforces the corpus's long-context theme: positional encoding is not a minor implementation detail but a core inductive bias governing extrapolation and factorized reasoning.
