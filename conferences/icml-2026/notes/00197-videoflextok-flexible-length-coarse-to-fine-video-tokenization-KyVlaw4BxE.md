# VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: KyVlaw4BxE
- Authors: Andrei Atanov; Jesse Allardice; Roman Bachmann; Oğuzhan Fatih Kar; R Devon Hjelm; David Griffiths; Peter Fu; Afshin Dehghan; Amir Zamir
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: video;video tokenization;video generation;representation learning
- Source URL: https://openreview.net/forum?id=KyVlaw4BxE
- PDF URL: https://openreview.net/pdf?id=KyVlaw4BxE

## Abstract

Visual tokenizers map high-dimensional raw pixels into a compressed representation for downstream modeling. Beyond compression, tokenizers dictate what information is preserved and how it is organized. A _de facto_ standard approach to video tokenization is to represent a video as a spatiotemporal 3D grid of tokens, each capturing local information from the original signal. This requires the downstream model, e.g., a text-to-video model, to learn to predict all low-level details "pixel-by-pixel" irrespective of the video's inherent complexity, leading to high learning complexity.
__We present _VideoFlexTok_, which represents videos with a variable-length sequence of tokens structured in a coarse-to-fine manner__, where the first tokens (emergently) capture information such as semantics and motion, and later tokens add fine-grained details. The generative flow decoder enables realistic video reconstructions from any token count. This representation structure allows adapting the token count to downstream needs and encoding videos longer than the baselines within the same budget.
We evaluate VideoFlexTok on class- and text-to-video generative tasks and show that it yields more efficient training than 3D grid tokens, _achieving comparable generation quality (gFVD and ViCLIP Score) with a 5x smaller model (1.1B vs 5.2B)._
Finally, we show how _VideoFlexTok can enable long video generation without prohibitive computational cost_ by training a text-to-video model on 10-second 81-frame videos with only 672 tokens, 8x fewer than a comparable 3D grid tokenizer.

## One-Sentence Claim

VideoFlexTok represents videos as flexible-length coarse-to-fine token sequences, reducing video-generation learning cost while preserving semantic, motion, and detail structure.

## Problem

Standard video tokenizers use fixed spatiotemporal grids that force downstream models to predict all low-level details uniformly, regardless of video complexity, making long-video generation expensive.

## Core Contribution

The paper introduces a variable-length tokenization scheme where early tokens capture coarse semantics and motion while later tokens add fine details, with a generative flow decoder that reconstructs from any token count.

## Method

VideoFlexTok learns a coarse-to-fine video representation and allows downstream models to adapt token count to task or budget. The decoder supports realistic reconstruction from partial or full token sequences.

## Experiments and Evidence

The abstract reports comparable generation quality to 3D grid tokenization with a 1.1B model versus a 5.2B model, and text-to-video training on 10-second 81-frame videos with 672 tokens, 8x fewer than a comparable 3D grid tokenizer.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: tokenizer training data, reconstruction metrics, long-video coherence, token allocation policy, decoder artifacts, and performance on fast motion or fine visual text.

## Deep Themes

- Tokenizers are information-allocation policies, not just compression tools.
- Variable-length representations adapt compute to content complexity.
- Coarse-to-fine structure supports longer generative horizons.

## Subthemes

- Video tokenization.
- Video generation.
- Coarse-to-fine representations.
- Generative flow decoder.
- Flexible token budgets.
- Long video generation.

## Connections to Other Papers

Connects to long-context and efficiency papers through adaptive token budgets, and to XR-1/3ViewSense through structured video and motion representations.

## Notes for Cross-Paper Synthesis

VideoFlexTok adds a representation-compression theme: the structure of tokens determines what downstream generative models can learn efficiently.
