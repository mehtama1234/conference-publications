# Any-Order GPT as Masked Diffusion Model: Decoupling Formulation and Architecture

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: sEYoG3tAXN
- Authors: Shuchen Xue; Tianyu Xie; Tianyang Hu; Zijin Feng; Jiacheng Sun; Kenji Kawaguchi; Zhenguo Li; Zhi-Ming Ma
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Discrete Diffusion Models;Any-Order Autoregressive Models;Causal Architecture
- Source URL: https://openreview.net/forum?id=sEYoG3tAXN
- PDF URL: https://openreview.net/pdf?id=sEYoG3tAXN

## Abstract

Efficiently scaling Large Language Models (LLMs) necessitates exploring alternatives to dominant autoregressive (AR) methods, with Masked Diffusion Models (MDMs) emerging as candidates. However, comparing AR (typically decoder-only) and MDM (often encoder-only) paradigms is confounded by differing architectures, obscuring true algorithmic and efficiency trade-offs. This research decouples these factors by evaluating MDMs within a decoder-only framework to: (1) Equitably compare MDM (as Any-Order AR) and standard AR paradigms through discrepancies on orders. (2) Investigate MDM architectural impacts on computational efficiency. We show decoder-only MDMs, despite a larger modeling space, can achieve significant inference speedups ($\sim25\times$) and comparable perplexity with techniques like temperature annealing, offering a path to reduced inference compute. This work provides insights for developing more computationally efficient foundation models by disentangling core modeling choices from architectural influences. Code is available at \url{https://github.com/scxue/AO-GPT-MDM}.

## One-Sentence Claim

Masked diffusion language modeling can be fairly compared to autoregression by implementing it in a decoder-only any-order GPT framework, revealing large inference speedups with comparable perplexity.

## Problem

Autoregressive LLMs and masked diffusion models differ in both modeling paradigm and architecture. AR models are usually decoder-only, while MDMs are often encoder-only, making comparisons confounded: performance or efficiency differences may come from architecture rather than the generative formulation.

The paper asks what happens when these factors are decoupled. Can masked diffusion be evaluated as any-order autoregression inside the same decoder-only style used by GPT models?

## Core Contribution

The paper formulates masked diffusion models within a decoder-only framework as any-order autoregressive models. This allows more equitable comparison with standard left-to-right AR by isolating differences in generation order and objective.

It shows that decoder-only MDMs have a larger modeling space and can achieve substantial inference speedups, around 25x, with comparable perplexity when using techniques such as temperature annealing.

## Method

The framework treats MDM generation as any-order token prediction using a causal decoder-only architecture. This aligns architectural assumptions with GPT-style models while preserving the nonstandard ordering flexibility of masked diffusion.

The experiments compare standard AR and MDM/any-order variants through discrepancies over orders, and study how architectural choices affect computational efficiency. Temperature annealing is used to improve generation behavior.

## Experiments and Evidence

The abstract reports comparable perplexity and about 25x inference speedup for decoder-only MDMs. It also claims insights into architectural impacts on MDM efficiency.

Full-paper reading should verify model sizes, datasets, generation quality metrics beyond perplexity, speedup measurement, decoding step counts, and whether speedups hold in optimized production kernels.

## Limits and Failure Modes

Comparable perplexity does not guarantee equivalent downstream quality, instruction following, or long-form coherence. Any-order generation may introduce different error modes than left-to-right decoding.

The reported speedup likely depends on batching, hardware, implementation, and sampling schedule. MDM serving infrastructure is less mature than AR LLM serving.

## Deep Themes

- Decoupled paradigm comparison: architecture and objective must be separated before judging AR versus diffusion.
- Any-order language modeling: generation order becomes a modeling degree of freedom.
- Diffusion as efficient foundation-model alternative: non-AR methods are motivated by inference compute.
- Decoder-only MDMs: diffusion can inhabit GPT-like architectures.

## Subthemes

- Temperature annealing helps masked diffusion generation.
- Larger modeling spaces do not necessarily hurt perplexity.
- Fair comparison requires shared architectural constraints.
- Speedup claims need protocol-specific measurement.

## Connections to Other Papers

This paper connects to XDLM, JustGRPO, and DMPO through the diffusion language model thread. It also relates to PoLar, DHSA, and TabSwift through inference-time efficiency and dynamic computation.

Its decoupling argument mirrors AlgoVeri's aligned benchmark design: comparisons are only meaningful when confounding differences are controlled.

## Notes for Cross-Paper Synthesis

The synthesis point is that foundation-model alternatives need fair ablations of paradigm versus architecture. Several papers are uncovering that apparent winners may reflect benchmark or architecture confounds.
