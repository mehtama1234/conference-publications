# End-to-End Autoregressive Image Generation with 1D Semantic Tokenizer

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fSnxuRhWoC
- Authors: Wenda Chu; Bingliang Zhang; Jiaqi Han; Yizhuo Li; Linjie Yang; Yisong Yue; Qiushan Guo
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: autoregressive modeling;end-to-end training;visual tokenizer;image generation
- Source URL: https://openreview.net/forum?id=fSnxuRhWoC
- PDF URL: https://openreview.net/pdf?id=fSnxuRhWoC

## Abstract

Autoregressive image modeling relies on visual tokenizers to compress images into compact latent representations. We design an end-to-end training pipeline that jointly optimizes reconstruction and generation, enabling direct supervision from generation results to the tokenizer. This contrasts with prior two-stage approaches that train tokenizers and generative models separately. We further investigate leveraging vision foundation models to improve 1D tokenizers for autoregressive modeling. Our autoregressive generative model achieves strong empirical results, including a state-of-the-art FID score of 1.48 without guidance on ImageNet 256×256 generation.

## One-Sentence Claim

Jointly training a 1D semantic tokenizer with the autoregressive generator lets generation quality supervise the tokenizer and yields state-of-the-art unguided ImageNet generation.

## Problem

Autoregressive image models depend heavily on visual tokenizers, but the usual two-stage pipeline trains tokenizers for reconstruction before training generators on the frozen token space. This can optimize compression while failing to produce tokens that are best for generation.

The paper asks whether tokenizer and generator should be trained end-to-end so generation outcomes directly shape the latent representation.

## Core Contribution

The contribution is an end-to-end autoregressive image-generation pipeline that jointly optimizes reconstruction and generation. It also investigates using vision foundation models to improve 1D tokenizers.

The reported result is strong: an FID of 1.48 on ImageNet 256x256 without guidance.

## Method

The pipeline trains the visual tokenizer and autoregressive generator together, allowing gradients or supervision from generation performance to affect the tokenizer. The tokenizer produces compact 1D semantic tokens suitable for autoregressive sequence modeling.

Vision foundation model signals are used to improve the tokenizer's semantic quality, helping the token sequence preserve generation-relevant content rather than only pixel reconstruction.

## Experiments and Evidence

Evidence reported in the abstract:

- End-to-end training of tokenizer and autoregressive generator.
- Joint optimization of reconstruction and generation.
- Use of vision foundation models to improve 1D tokenizers.
- State-of-the-art unguided FID of 1.48 on ImageNet 256x256.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: model size, tokenizer architecture, training cost, foundation-model supervision, and comparisons with diffusion baselines.

## Limits and Failure Modes

- End-to-end training may increase instability or compute cost versus modular two-stage training.
- FID alone may not capture diversity, semantic controllability, or memorization.
- Foundation-model supervision can import biases from the teacher model.
- 1D tokenization may lose spatial inductive bias unless the model compensates.

## Deep Themes

**Representations should be optimized for downstream generation.** Tokenizers are not neutral preprocessing; they shape model capability.

**Autoregressive image modeling is absorbing foundation-model semantics.** Visual tokens are being made more semantic to compete with diffusion-style generators.

**Pipeline boundaries are being collapsed.** Separate tokenizer and generator training can leave performance on the table.

## Subthemes

- End-to-end tokenizer-generator training.
- 1D semantic visual tokens.
- Foundation-model-assisted tokenization.
- Unguided autoregressive image generation.
- Reconstruction-generation objective alignment.

## Connections to Other Papers

Connects to MOG, KPE/KTS, Tilt Matching, WaterSIC, and Context-Parameter Equivalence. Like WaterSIC and POET-X, it treats an internal representation layer as a lever for downstream quality.

## Notes for Cross-Paper Synthesis

This paper adds to a repeated theme: latent interfaces are bottlenecks. Whether tokens, quantized weights, or context patches, the interface representation determines what the larger model can efficiently do.
