# Semantic-Aware Diffusion LLM Inference With Adaptive Block Size

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0Cv9PwL7cI
- Authors: Guanxi Lu; Hao Mark Chen; Yuto Karashima; Zhican Wang; Daichi Fujiki; Hongxiang Fan
- Primary area: generative models
- Keywords: Diffusion Large Language Models;Non-Autoregressive Decoding
- Source URL: https://openreview.net/forum?id=0Cv9PwL7cI
- PDF URL: https://openreview.net/pdf?id=0Cv9PwL7cI

## Abstract

Diffusion-based large language models (dLLMs) are gaining attention for their inherent capacity for parallel decoding, offering a compelling alternative to autoregressive LLMs. Among various decoding strategies, blockwise semi-autoregressive (semi-AR) approaches are widely adopted due to their natural support for KV caching and their favorable accuracy–speed trade-off. However, this paper identifies two fundamental limitations in the conventional semi-AR decoding approach that applies a fixed block size: i) late decoding overhead, where the unmasking of high-confidence tokens outside the current block is unnecessarily delayed; and ii) premature decoding error, where low-confidence tokens inside the current block are committed too early, leading to incorrect tokens. This paper presents the first systematic investigation challenging the fixed block size assumption in semi-AR decoding. Through a statistical analysis of confidence dynamics during the denoising process, we identify a volatility band (VB) region during dLLM decoding, which encodes local semantic structure and can be used to guide adaptive block sizing. Leveraging these insights, we introduce AdaBlock-dLLM, a training-free, plug-and-play scheduler that adaptively aligns block boundaries with semantic steps by adjusting block size during runtime. Extensive experiments across diverse benchmarks show that AdaBlock-dLLM achieves up to 5.3% accuracy improvement under the same throughput budget. Beyond inference-time optimization, we hope our semantics-aware adaptive scheduling approach and confidence-based analysis will inspire future training strategies for dLLMs.

## One-Sentence Claim

AdaBlock-dLLM improves diffusion LLM semi-autoregressive decoding by adapting block sizes to confidence dynamics and semantic boundaries at runtime.

## Problem

Diffusion LLMs can decode in parallel, but fixed-block semi-autoregressive decoding creates two failures: high-confidence tokens outside the block are delayed, and low-confidence tokens inside the block can be committed too early. Fixed block size therefore wastes throughput or harms accuracy.

## Core Contribution

The paper systematically challenges the fixed-block assumption and introduces AdaBlock-dLLM, a training-free plug-and-play scheduler that adapts block boundaries using a volatility band observed in denoising confidence dynamics.

## Method

The method statistically analyzes token confidence during diffusion denoising and identifies a volatility band that reflects local semantic structure. At inference time, AdaBlock-dLLM adjusts block size so semi-AR boundaries better align with semantic steps, delaying uncertain tokens while unmasking confident ones earlier.

## Experiments and Evidence

The abstract reports extensive experiments across diverse benchmarks and up to 5.3% accuracy improvement at the same throughput budget. It positions the confidence analysis as useful for future dLLM training strategies as well as inference-time scheduling.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect benchmark tasks, dLLM architectures, volatility-band definition, latency overhead, interaction with KV caching, and whether adaptive boundaries destabilize long outputs. Confidence may be poorly calibrated out of distribution.

## Deep Themes

- Diffusion LLM inference scheduling.
- Adaptive blockwise semi-autoregressive decoding.
- Confidence dynamics as semantic signal.
- Training-free inference optimization.

## Subthemes

- AdaBlock-dLLM.
- Volatility band.
- Parallel decoding.
- Premature token commitment.
- Late decoding overhead.

## Connections to Other Papers

Connects to PGM and NEXCO through masked/diffusion generation with meaningful intermediate states, to MetaEmbed through test-time quality-efficiency controls, and to MotionStream through runtime scheduling for throughput.

## Notes for Cross-Paper Synthesis

AdaBlock-dLLM adds another example of test-time adaptivity: generation should advance according to semantic confidence, not a fixed schedule. The cross-corpus pattern is that decoding policy is becoming a key capability lever.
