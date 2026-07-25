# Multimodal Latent Language Modeling with Next-Token Diffusion

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: PnTXyTR2VG
- Authors: Yutao Sun; Hangbo Bao; Wenhui Wang; Zhiliang Peng; Li Dong; Shaohan Huang; Yaoyao Chang; Jianyong Wang; Furu Wei
- Primary area: deep_learning->foundation_models
- Keywords: Next Token Diffusion;MultiModal LLM
- Source URL: https://openreview.net/forum?id=PnTXyTR2VG
- PDF URL: https://openreview.net/pdf?id=PnTXyTR2VG

## Abstract

Multimodal generative models require a unified approach to handle both discrete data (e.g., text and code) and continuous data (e.g., image, audio, video). In this work, we propose Latent Language Modeling (LatentLM), which seamlessly integrates continuous and discrete data using causal Transformers. Specifically, we employ a variational autoencoder (VAE) to represent continuous data as latent vectors and introduce next-token diffusion for autoregressive generation of these vectors. Additionally, we develop $\sigma$-VAE to address the challenges of variance collapse, which is crucial for autoregressive modeling. Extensive experiments demonstrate the effectiveness of LatentLM across various modalities. In image generation, LatentLM sis competitive with or outperforms DiT-style baselines under matched unified settings. When integrated into multimodal large language models, LatentLM provides a general-purpose interface that unifies multimodal generation and understanding. Experimental results show that LatentLM achieves favorable performance compared to Transfusion and vector quantized models in the setting of scaling up training tokens. In text-to-speech synthesis, LatentLM outperforms the state-of-the-art VALL-E 2 model in speaker similarity and robustness, while requiring 10 fewer decoding steps. The results establish LatentLM as a highly effective and scalable approach to advance large multimodal models.

## One-Sentence Claim

LatentLM unifies discrete and continuous multimodal generation by autoregressively modeling VAE latent vectors with next-token diffusion in causal Transformers.

## Problem

Multimodal generative models need one scalable interface for discrete modalities like text/code and continuous modalities like image, audio, and video.

## Core Contribution

The paper introduces Latent Language Modeling with next-token diffusion, plus sigma-VAE to prevent variance collapse in autoregressive latent modeling.

## Method

Continuous data are encoded as VAE latent vectors, and a causal Transformer generates those vectors autoregressively using next-token diffusion. The sigma-VAE variant stabilizes latent variance for generation and understanding.

## Experiments and Evidence

The abstract reports competitive or better image generation than DiT-style baselines under matched unified settings, favorable scaling versus Transfusion and vector-quantized models in multimodal LLMs, and better text-to-speech speaker similarity and robustness than VALL-E 2 with ten fewer decoding steps.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model scale, modality set, VAE architecture, variance-collapse diagnostics, latency, video/audio quality metrics, and compatibility with existing MLLM training pipelines.

## Deep Themes

- Unified multimodal models need latent interfaces spanning discrete and continuous data.
- Diffusion can be inserted at the next-token level for continuous latent generation.
- VAE design is central to stable autoregressive multimodal scaling.

## Subthemes

- Multimodal LLMs.
- Next-token diffusion.
- VAE latents.
- Image generation.
- Text-to-speech.
- Unified generation and understanding.

## Connections to Other Papers

Connects to VideoFlexTok, Chamaileon, PWC-Diff, and multimodal foundation-model papers through latent representation and diffusion-based generation.

## Notes for Cross-Paper Synthesis

LatentLM adds a unification theme: future multimodal systems may treat continuous latents as token-like objects, but generation requires diffusion-style uncertainty rather than pure discrete prediction.
