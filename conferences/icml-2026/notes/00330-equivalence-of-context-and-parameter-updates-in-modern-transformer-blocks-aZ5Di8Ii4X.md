# Equivalence of Context and Parameter Updates in Modern Transformer Blocks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aZ5Di8Ii4X
- Authors: Adrian Goldwaser; Michael Munn; Javier Gonzalvo; Benoit Dherin
- Primary area: deep_learning->theory
- Keywords: attention mechanism;in-context learning;large language models;implicit learning dynamics
- Source URL: https://openreview.net/forum?id=aZ5Di8Ii4X
- PDF URL: https://openreview.net/pdf?id=aZ5Di8Ii4X

## Abstract

Recent research has established that the impact of context in a vanilla transformer can be represented implicitly by forming a token-dependent, rank-1 patch to its MLP weights. This work extends that foundational theory to the diverse architectures of modern Large Language Models. We first demonstrate a precise, analytical solution for a Gemma-style transformer block, proving that the entire effect of a context can be perfectly mapped to rank-1 patches on its MLP weight matrices and a patch to the RMSNorm scale. We then generalize this result, providing a constructive proof and algorithm for multi-layer models. To unify these findings, we introduce a general framework centered on two core properties: input controllability and output controllability. We prove that a perfect implicit weight patch is possible for any MLP block where the inner function is input-controllable and the outer function is output-controllable. This provides a simpler and more powerful lens for understanding how transformer models transmute prompts into effective weights. This setup generalizes to a wide range of modern LLM architectures including gating, pre-/post-norm, mixture of experts and sequential/parallel transformer blocks.

## One-Sentence Claim

In modern Transformer blocks, the effect of context can be represented exactly as implicit rank-1 MLP weight patches plus normalization-scale patches under controllability conditions.

## Problem

Prior theory showed that context in vanilla Transformers can act like a token-dependent rank-1 patch to MLP weights. Modern LLMs, however, use varied blocks: RMSNorm, gating, mixture-of-experts, pre/post norm, and sequential or parallel designs.

The paper asks whether the context-as-parameter-update view extends beyond vanilla Transformer architectures.

## Core Contribution

The paper gives an analytical solution for a Gemma-style block, proving the entire context effect can be mapped to rank-1 patches on MLP weight matrices plus a patch to the RMSNorm scale. It then generalizes constructively to multi-layer models.

It introduces a framework based on input controllability and output controllability, proving perfect implicit weight patches are possible for MLP blocks where the inner function is input-controllable and the outer function is output-controllable. The setup covers gating, pre/post norm, mixture of experts, and sequential/parallel Transformer blocks.

## Method

The method analytically rewrites contextual effects as equivalent parameter patches. For a block, it identifies how a token's context-dependent computation can be represented as low-rank changes to MLP parameters and normalization scales.

The constructive proof and algorithm extend this layer by layer, using controllability properties as the abstraction that unifies architectures.

## Experiments and Evidence

Evidence reported in the abstract is theoretical:

- Exact analytical solution for Gemma-style Transformer blocks.
- Rank-1 MLP patches and RMSNorm-scale patch representing context effects.
- Constructive proof and algorithm for multi-layer models.
- General input/output controllability framework.
- Applicability to gating, pre/post norm, MoE, and sequential/parallel blocks.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: formal controllability definitions, assumptions for exactness, and whether empirical validation is included.

## Limits and Failure Modes

- Equivalence may be representational rather than computationally practical.
- Exact patch construction may require access to internal activations and architecture details.
- Attention-side effects beyond MLP blocks need careful interpretation.
- Controllability assumptions may fail for some nonlinearities or implementation details.

## Deep Themes

**Context can behave like fast weights.** Prompts are interpreted as implicit low-rank parameter updates.

**In-context learning and fine-tuning share geometry.** The paper provides a bridge between context updates and parameter patches.

**Controllability abstracts modern architecture variation.** Input/output controllability explains when exact implicit patches exist.

## Subthemes

- Context-as-rank-1 weight patch.
- RMSNorm scale patching.
- Input and output controllability.
- Modern Transformer block theory.
- MoE and gated architecture coverage.

## Connections to Other Papers

Connects to Diffract, PRISM, LoRA/FedPissa, Neuron-Basis Circuits, and DiSC through low-rank or localized adaptation. It also links to long-context and in-context learning papers because context is framed as an implicit parameter update.

## Notes for Cross-Paper Synthesis

This paper gives a theoretical backbone to many adaptation themes in the corpus: context, LoRA, rewinding, and patching may be different ways of manipulating effective low-rank weights.
