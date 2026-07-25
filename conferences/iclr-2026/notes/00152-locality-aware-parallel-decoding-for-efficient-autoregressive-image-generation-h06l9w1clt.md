# Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: h06l9w1clt
- Authors: Zhuoyang Zhang; Luke J. Huang; Chengyue Wu; Shang Yang; Kelly Peng; Yao Lu; Song Han
- Primary area: generative models
- Keywords: Efficient Autoregressive Image Generation;Parallel Decoding
- Source URL: https://openreview.net/forum?id=h06l9w1clt
- PDF URL: https://openreview.net/pdf?id=h06l9w1clt

## Abstract

We present Locality-aware Parallel Decoding (LPD) to accelerate autoregressive image generation. Traditional autoregressive image generation relies on next-patch prediction, a memory-bound process that leads to high latency. Existing works have tried to parallelize next-patch prediction by shifting to multi-patch prediction to accelerate the process, but only achieved limited parallelization. To achieve high parallelization while maintaining generation quality, we introduce two key techniques: (1) Flexible Parallelized Autoregressive Modeling, a novel architecture that enables arbitrary generation ordering and degrees of parallelization. It uses learnable position query tokens to guide generation at target positions while ensuring mutual visibility among concurrently generated tokens for consistent parallel decoding. (2) Locality-aware Generation Ordering, a novel schedule that forms groups to minimize intra-group dependencies and maximize contextual support, enhancing generation quality. With these designs, we reduce the generation steps from 256 to 20 (256×256 res.) and 1024 to 48 (512×512 res.) without compromising quality on the ImageNet class-conditional generation, and achieving at least 3.4× lower latency than previous parallelized autoregressive models.

## One-Sentence Claim

LPD accelerates autoregressive image generation by allowing arbitrary parallel generation orders and grouping patches by locality to reduce dependencies while preserving quality.

## Problem

Autoregressive image generation traditionally predicts one patch at a time, creating memory-bound high-latency decoding.

Existing multi-patch approaches offer limited parallelization because they do not adequately manage dependencies among concurrently generated patches.

## Core Contribution

The paper introduces Locality-aware Parallel Decoding.

It combines Flexible Parallelized Autoregressive Modeling, which supports arbitrary ordering and parallelization degrees, with Locality-aware Generation Ordering, which groups patches to minimize intra-group dependencies and maximize contextual support.

## Method

Learnable position query tokens guide generation at target positions.

Concurrently generated tokens have mutual visibility so parallel decoding remains consistent. The locality-aware schedule forms patch groups whose dependencies are weak inside a group and whose context is strong from already generated patches.

## Experiments and Evidence

The abstract reports reducing generation steps from 256 to 20 at 256x256 resolution and from 1024 to 48 at 512x512 resolution.

On ImageNet class-conditional generation, LPD preserves quality while achieving at least 3.4x lower latency than previous parallelized autoregressive models.

## Limits and Failure Modes

Locality assumptions may struggle with images requiring long-range global consistency or highly structured layouts. Parallel decoding quality may depend on the learned position-query design and grouping schedule.

Because this note is abstract-only, details still need checking: architecture, generation ordering algorithm, ImageNet metrics, latency setup, resolution scaling, and comparisons to diffusion or continuous-token AR models.

## Deep Themes

- Parallel AR generation: autoregressive models need decoding schedules that expose parallelism.
- Locality-aware dependency management: patch groups are chosen by spatial/contextual dependencies.
- Position-query control: generation targets become explicit query-conditioned operations.
- Quality-preserving latency reduction: fewer steps must not sacrifice global coherence.

## Subthemes

- Autoregressive image generation.
- Parallel decoding.
- Locality-aware scheduling.
- Learnable position queries.

## Connections to Other Papers

This connects to NextStep-1, Prophet, HyCa, and diffusion/image generation acceleration papers.

It also relates to TileLang and systems work because algorithmic speedups need efficient memory behavior.

## Notes for Cross-Paper Synthesis

LPD adds to the decoding-schedule theme: generative latency can drop sharply when generation order matches the dependency structure of the output.
