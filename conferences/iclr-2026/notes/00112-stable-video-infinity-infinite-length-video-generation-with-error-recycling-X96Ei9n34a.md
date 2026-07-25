# Stable Video Infinity: Infinite-Length Video Generation with Error Recycling

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: X96Ei9n34a
- Authors: Wuyang Li; Wentao Pan; Po-Chien Luan; Yang Gao; Alexandre Alahi
- Primary area: generative models
- Keywords: Infinite-Length Video Generation;Error Accumulation
- Source URL: https://openreview.net/forum?id=X96Ei9n34a
- PDF URL: https://openreview.net/pdf?id=X96Ei9n34a

## Abstract

We propose **Stable Video Infinity (SVI)** that can generate non-looping, ultra-long videos with stable visual quality, while supporting per-clip prompt control and multi-modal conditioning. While existing long-video methods attempt to _**mitigate accumulated errors**_ via handcrafted anti-drifting (e.g., modified noise scheduler, frame anchoring), they remain limited to single-prompt extrapolation, producing homogeneous scenes with repetitive motions. We identify that the fundamental challenge extends beyond error accumulation to a critical discrepancy between the training assumption (seeing clean data) and the test-time autoregressive reality (conditioning on self-generated, error-prone outputs). To bridge this hypothesis gap, SVI incorporates **Error-Recycling Fine-Tuning**, a new type of efficient training that recycles the Diffusion Transformer (DiT)’s self-generated errors into supervisory prompts, thereby encouraging DiT to _**actively identify and correct its own errors**_. This is achieved by injecting, collecting, and banking errors through closed-loop recycling, autoregressively learning from error-injected feedback. Specifically, we (i) inject historical errors made by DiT to intervene on clean inputs, simulating error-accumulated trajectories in flow matching; (ii) efficiently approximate predictions with one-step bidirectional integration and calculate errors with residuals; (iii) dynamically bank errors into replay memory across discretized timesteps, which are resampled for new input. SVI is able to scale videos from seconds to infinite durations with no additional inference cost, while remaining compatible with diverse conditions (e.g., audio, skeleton, and text streams). We evaluate SVI on three benchmarks, including consistent, creative, and conditional settings, thoroughly verifying its versatility and state-of-the-art role.

## One-Sentence Claim

Stable Video Infinity trains diffusion transformers to correct their own autoregressive video errors, enabling non-looping ultra-long generation with clip-level prompt and multimodal control.

## Problem

Long-video generation suffers from accumulated errors when models condition on their own previous outputs. Existing anti-drift methods often rely on handcrafted scheduler changes or frame anchoring and remain limited to single-prompt extrapolation.

The deeper mismatch is between training on clean data and test-time autoregressive conditioning on self-generated, error-prone frames.

## Core Contribution

The paper introduces Stable Video Infinity and Error-Recycling Fine-Tuning.

SVI recycles a DiT's own generated errors into supervisory prompts, encouraging the model to identify and correct error accumulation during closed-loop autoregressive generation.

## Method

The method injects historical errors into clean inputs to simulate accumulated trajectories under flow matching.

It approximates predictions with one-step bidirectional integration, computes residual errors, banks errors in replay memory across discretized timesteps, and resamples them during training.

## Experiments and Evidence

The abstract reports infinite-duration scaling with no additional inference cost and compatibility with audio, skeleton, and text conditioning.

SVI is evaluated on three benchmarks covering consistent, creative, and conditional long-video settings and is described as state of the art.

## Limits and Failure Modes

Infinite-length claims require careful interpretation: quality may remain stable over tested horizons without proving arbitrary-duration semantic coherence. Error banks may also overfit to common failure modes while missing rare drift patterns.

Because this note is abstract-only, details still need checking: benchmark durations, prompt-change protocol, conditioning modalities, replay memory design, quality metrics, and comparisons to anchoring/scheduler baselines.

## Deep Themes

- Train-test mismatch in autoregressive generation: models need to train on their own error distribution.
- Error recycling: generated failures become supervision for correction.
- Long-horizon multimodal control: clip-level prompts and conditioning streams break homogeneous extrapolation.
- No-extra-inference-cost stability: training absorbs correction behavior rather than adding runtime modules.

## Subthemes

- Infinite-length video generation.
- Error-Recycling Fine-Tuning.
- Closed-loop DiT training.
- Multimodal conditioning.

## Connections to Other Papers

This connects to HyCa, InfoTok, FlashVID, DCFold, and DiffusionNFT through efficient and controllable diffusion/video generation.

It also relates to multi-turn conversation failures because both involve compounding errors under autoregressive state.

## Notes for Cross-Paper Synthesis

SVI strengthens the long-horizon generation theme: robustness requires training on the model's own future-state errors, not only clean one-step targets.
