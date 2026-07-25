# FlashVID: Efficient Video Large Language Models via Training-free Tree-based Spatiotemporal Token Merging

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: H6rDX4w6Al
- Authors: Ziyang Fan; Keyu Chen; Ruilong Xing; Yulin Li; Li Jiang; Zhuotao Tian
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Efficient Large Multimodal Models;Video Large Language Models;Visual Token Compression
- Source URL: https://openreview.net/forum?id=H6rDX4w6Al
- PDF URL: https://openreview.net/pdf?id=H6rDX4w6Al

## Abstract

Although Video Large Language Models (VLLMs) have shown remarkable capabilities in video understanding, they are required to process high volumes of visual tokens, causing significant computational inefficiency. Existing VLLMs acceleration frameworks usually compress spatial and temporal redundancy independently, which overlooks the spatiotemporal relationships, thereby leading to suboptimal spatiotemporal compression. The highly correlated visual features are likely to change in spatial position, scale, orientation, and other attributes over time due to the dynamic nature of video. Building on this insight, we introduce FlashVID, a training-free inference acceleration framework for VLLMs. Specifically, FlashVID utilizes Attention and Diversity-based Token Selection (ADTS) to select the most representative tokens for basic video representation, then applies Tree-based Spatiotemporal Token Merging (TSTM) for fine-grained spatiotemporal redundancy elimination. Extensive experiments conducted on three representative VLLMs across five video understanding benchmarks demonstrate the effectiveness and generalization of our method. Notably, by retaining only $\textbf{10}$% of visual tokens, FlashVID preserves $\textbf{99.1}$% of the performance of LLaVA-OneVision. Consequently, FlashVID can serve as a training-free and plug-and-play module for extending long video frames, which enables a $\textbf{10$\times$}$ increase in video frame input to Qwen2.5-VL, resulting in a relative improvement of $\textbf{8.6}$% within the same computational budget. Code is available at https://github.com/Fanziyang-v/FlashVID.

## One-Sentence Claim

FlashVID accelerates video LLM inference by selecting representative visual tokens and merging spatiotemporally redundant tokens in a training-free tree structure.

## Problem

Video LLMs process large numbers of visual tokens, making inference expensive. Existing acceleration methods often compress spatial and temporal redundancy separately.

This misses the fact that correlated visual features move, scale, and rotate over time, so redundancy is inherently spatiotemporal.

## Core Contribution

The paper introduces FlashVID, a training-free plug-and-play acceleration framework for VLLMs.

It uses Attention and Diversity-based Token Selection to retain representative tokens, then applies Tree-based Spatiotemporal Token Merging to eliminate fine-grained redundancy.

## Method

ADTS builds a compact base representation from important and diverse tokens. TSTM merges related tokens across space and time in a tree structure, capturing dynamic correlations rather than treating frames independently.

Because it is training-free, FlashVID can be inserted into existing VLLMs at inference time.

## Experiments and Evidence

The abstract reports experiments on three VLLMs and five video understanding benchmarks.

Retaining only 10 percent of visual tokens preserves 99.1 percent of LLaVA-OneVision performance. FlashVID enables 10x more video frames for Qwen2.5-VL within the same compute budget, improving performance by 8.6 percent relatively.

## Limits and Failure Modes

Aggressive token merging may hurt tasks requiring rare fine-grained visual details or precise temporal ordering. Training-free heuristics may not adapt to all architectures.

Because this note is abstract-only, details still need checking: token-selection scores, tree construction, benchmarks, latency/memory metrics, long-video settings, and failure cases with small objects or rapid motion.

## Deep Themes

- Spatiotemporal compression: video redundancy must be handled jointly across space and time.
- Training-free inference acceleration: practical gains can come without retraining.
- Token budget as context budget: saving visual tokens enables longer video inputs.
- Attention and diversity as selection signals: representative tokens preserve performance under compression.

## Subthemes

- ADTS token selection.
- Tree-based spatiotemporal token merging.
- VLLM acceleration.
- Long-video frame extension.

## Connections to Other Papers

This connects to EntroKV, ThinkV, EcoVLA, and tokenization/efficiency papers through adaptive inference compression.

It also relates to MetaphorVU, VibeVoice, and video/world-model papers because long-form multimodal understanding depends on efficient sequence handling.

## Notes for Cross-Paper Synthesis

FlashVID strengthens the resource-adaptive multimodal theme: longer and richer inputs often become possible by compressing tokens according to internal structure.
