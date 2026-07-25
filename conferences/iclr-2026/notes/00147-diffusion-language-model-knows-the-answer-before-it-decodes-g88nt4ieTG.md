# Diffusion Language Model Knows the Answer Before It Decodes

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: g88nt4ieTG
- Authors: Pengxiang Li; Yefan Zhou; Dilxat Muhtar; Lu Yin; Shilin Yan; Li Shen; Yi Liang; Soroush Vosoughi; Shiwei Liu
- Primary area: generative models
- Keywords: diffusion language model;discrete
- Source URL: https://openreview.net/forum?id=g88nt4ieTG
- PDF URL: https://openreview.net/pdf?id=g88nt4ieTG

## Abstract

Diffusion language models (DLMs) have recently emerged as an alternative to autoregressive approaches, offering parallel sequence generation and flexible token orders. However, their inference remains slower than that of autoregressive models, primarily due to the cost of bidirectional attention and the large number of refinement steps required for high-quality outputs. In this work, we highlight and leverage an overlooked property of DLMs, **early answer convergence**: in many cases, the correct answer can be internally identified by half steps before the final decoding step, both under semi-autoregressive and random re-masking schedules. For example, on GSM8K and MMLU, up to 97\% and 99\% of instances, respectively, can be decoded correctly using only half of the refinement steps.
Building on this observation, we introduce **Prophet**, a training-free fast decoding paradigm that enables **early commit decoding**. Specifically, Prophet dynamically decides whether to continue refinement or to go ''all-in'' (i.e., decode all remaining tokens in one step), using the confidence gap between the top-2 prediction candidates as the criterion. It integrates seamlessly into existing DLM implementations, incurs negligible overhead, and requires no additional training.
Empirical evaluations of LLaDA-8B and Dream-7B across multiple tasks show that Prophet reduces the number of decoding steps by up to 3.4$\times$ while preserving high generation quality. These results recast DLM decoding as a problem of ''when to stop refinement'', and demonstrate that early decode convergence provides a simple yet powerful mechanism for accelerating DLM inference, complementary to existing speedup techniques. Our code is submitted.

## One-Sentence Claim

Prophet accelerates diffusion language models by detecting early answer convergence and committing remaining tokens when top-candidate confidence gaps indicate refinement is no longer needed.

## Problem

Diffusion language models offer parallel generation and flexible token orders, but inference is slow because bidirectional attention and many refinement steps are expensive.

The paper observes that DLMs often internally identify the correct answer well before the final decoding step, meaning later refinement can waste compute.

## Core Contribution

The paper identifies early answer convergence in DLMs and introduces Prophet, a training-free early-commit decoding method.

Prophet dynamically decides whether to continue refinement or decode all remaining tokens in one step.

## Method

Prophet uses the confidence gap between the top two prediction candidates as its stopping/commit criterion.

When the gap indicates sufficient confidence, it goes all-in on the remaining tokens instead of spending more refinement steps.

## Experiments and Evidence

The abstract reports that on GSM8K and MMLU, up to 97 percent and 99 percent of instances can be decoded correctly using half the refinement steps.

On LLaDA-8B and Dream-7B across multiple tasks, Prophet reduces decoding steps by up to 3.4x while preserving high generation quality.

## Limits and Failure Modes

Top-2 confidence gaps can be overconfident on ambiguous prompts, creative generation, or tasks where early tokens need later global consistency. Early commit may reduce diversity or correction ability.

Because this note is abstract-only, details still need checking: stopping threshold, tasks, quality metrics, semi-autoregressive versus random re-masking schedules, and failure examples.

## Deep Themes

- Refinement stopping as inference control: DLM speed depends on knowing when enough denoising has happened.
- Early latent answer convergence: correct answers may appear internally before final decoding.
- Training-free DLM acceleration: confidence-based control can plug into existing models.
- Compute-aware generation: refinement steps become a budget to allocate conditionally.

## Subthemes

- Diffusion language models.
- Early commit decoding.
- Top-2 confidence gap.
- Refinement-step reduction.

## Connections to Other Papers

This connects to p-less sampling, ASAG, Reasoning with Sampling, HSD, and HyCa through training-free inference acceleration.

It also relates to diffusion/video acceleration papers because all try to stop or reuse iterative refinement when additional steps add little value.

## Notes for Cross-Paper Synthesis

Prophet adds an early-exit theme: iterative generative models often know enough before their scheduled endpoint, so inference should monitor convergence.
