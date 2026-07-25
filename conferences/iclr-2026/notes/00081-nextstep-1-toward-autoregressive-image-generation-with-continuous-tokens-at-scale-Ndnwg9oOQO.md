# NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Ndnwg9oOQO
- Authors: Chunrui Han; Guopeng Li; Jingwei Wu; Quan Sun; Yan Cai; Yuang Peng; Zheng Ge; Deyu Zhou; Haomiao Tang; Hongyu Zhou; Kenkun Liu; Shu-Tao Xia; Binxing Jiao; Daxin Jiang; Xiangyu Zhang; Yibo Zhu
- Primary area: foundation or frontier models, including LLMs
- Keywords: Generative Models;Autoregressive Models;Diffusion Models;Text-to-image
- Source URL: https://openreview.net/forum?id=Ndnwg9oOQO
- PDF URL: https://openreview.net/pdf?id=Ndnwg9oOQO

## Abstract

Prevailing autoregressive (AR) models for text-to-image generation either rely on heavy, computationally-intensive diffusion models to process continuous image tokens, or employ vector quantization (VQ) to obtain discrete tokens with quantization loss. In this paper, we push the autoregressive paradigm forward with NextStep-1, a 14B autoregressive model paired with a 157M flow matching head, training on discrete text tokens and continuous image tokens with next-token prediction objectives. NextStep-1 achieves state-of-the-art performance for autoregressive models in text-to-image generation tasks, exhibiting strong capabilities in high-fidelity image synthesis. Furthermore, our method shows strong performance in image editing, highlighting the power and versatility of our unified approach. To facilitate open research, we will release our code and models to the community.

## One-Sentence Claim

NextStep-1 scales autoregressive text-to-image generation by predicting continuous image tokens with a flow-matching head, avoiding both heavy diffusion processing and VQ quantization loss.

## Problem

Autoregressive image generation faces a representation dilemma. Continuous image tokens preserve information but often require expensive diffusion-style processing, while vector-quantized discrete tokens make AR training convenient but introduce quantization loss.

The field needs AR image models that can scale like language models while retaining high-fidelity continuous visual representations.

## Core Contribution

The paper introduces NextStep-1, a 14B autoregressive model paired with a 157M flow-matching head.

It trains on discrete text tokens and continuous image tokens under next-token prediction, pushing AR text-to-image generation toward diffusion-level fidelity without discrete-token bottlenecks.

## Method

NextStep-1 uses an autoregressive backbone for multimodal next-token prediction. Text is represented with ordinary discrete tokens, while images are represented with continuous tokens decoded or modeled through a flow-matching head.

The flow head appears to bridge the mismatch between AR sequence modeling and continuous image-token prediction.

## Experiments and Evidence

The abstract reports state-of-the-art performance among autoregressive text-to-image models.

NextStep-1 shows strong high-fidelity image synthesis and also performs well on image editing, suggesting the representation and training scheme are useful beyond one-shot generation.

## Limits and Failure Modes

The model is large, and the 14B AR backbone plus flow head may still be expensive compared with specialized diffusion systems. Continuous-token AR also raises questions about stability, sampling speed, and visual detail preservation.

Because this note is abstract-only, details still need checking: continuous token representation, flow-matching objective, training data, image resolution, editing protocol, comparison to diffusion baselines, and sampling cost.

## Deep Themes

- Continuous-token autoregression: AR generation is expanding beyond discrete codebooks.
- Hybrid AR-flow architectures: flow matching becomes an output head for continuous prediction rather than the whole generator.
- Avoiding quantization loss: image representation quality is a first-order bottleneck for AR visual models.
- Unified generation and editing: the same sequence model can support synthesis and manipulation.

## Subthemes

- Text-to-image autoregression.
- Continuous image tokens.
- Flow-matching head.
- Image editing.

## Connections to Other Papers

This connects to InfoTok, DCFold, SFA, and DFM Bounds through flow/diffusion ideas adapted for efficient or structured generation.

It also relates to VibeVoice and multimodal tokenization work because all treat token representation as central to scaling generative models.

## Notes for Cross-Paper Synthesis

NextStep-1 adds to the tokenization theme: generative scaling is increasingly constrained by whether the token space preserves the right continuous structure.
