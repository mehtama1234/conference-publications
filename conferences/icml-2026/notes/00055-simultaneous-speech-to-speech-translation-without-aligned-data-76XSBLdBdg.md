# Simultaneous Speech-to-Speech Translation Without Aligned Data

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 76XSBLdBdg
- Authors: Tom Labiausse; Romain Fabre; Yannick Estève; Alexandre Défossez; Neil Zeghidour
- Primary area: deep_learning->large_language_models
- Keywords: speech;translation;simultaneous;reinforcement learning;latency;llm;multistream;neural codec
- Source URL: https://openreview.net/forum?id=76XSBLdBdg
- PDF URL: https://openreview.net/pdf?id=76XSBLdBdg

## Abstract

Simultaneous speech translation requires translating source speech into a target language in real-time while handling non-monotonic word dependencies. Traditional approaches rely on supervised training with word-level aligned data, which is difficult to collect at scale and thus depends on synthetic alignments using language-specific heuristics that are suboptimal. We propose Hibiki-Zero, which eliminates the need for word-level alignments entirely. This fundamentally simplifies the training pipeline and enables seamless scaling to diverse languages with varying grammatical structures, removing the bottleneck of designing language-specific alignment heuristics. We first train on sentence-level aligned data to learn speech translation at high latency, then apply a novel reinforcement learning strategy using GRPO to optimize latency while preserving translation quality. Hibiki-Zero achieves state-of-the-art performance in translation accuracy, latency, voice transfer, and naturalness across four X-to-English tasks.  Moreover, we demonstrate that our model can be adapted to support a new input language with less than 1000h of speech. We provide [examples](https://huggingface.co/spaces/kyutai/hibiki-zero-samples), [model weights](https://huggingface.co/kyutai/hibiki-zero-3b-pytorch-bf16), [inference code](https://github.com/kyutai-labs/hibiki-zero) and we release a [benchmark](https://huggingface.co/datasets/kyutai/Audio-NTREX-4L) containing 45h of multilingual data for speech translation evaluation.

## One-Sentence Claim

Hibiki-Zero trains simultaneous speech-to-speech translation without word-level aligned data by learning high-latency translation from sentence alignments, then using GRPO to optimize latency-quality tradeoffs.

## Problem

Simultaneous speech translation requires real-time output despite non-monotonic cross-lingual dependencies, but word-level aligned speech translation data is scarce and synthetic alignments rely on language-specific heuristics.

## Core Contribution

The paper introduces Hibiki-Zero, a simultaneous S2ST/S2TT model that removes word-level alignment from training and releases model weights, inference code, examples, and a multilingual evaluation benchmark.

## Method

Hibiki-Zero first trains on sentence-level aligned speech translation data at high latency, then applies a GRPO-based reinforcement learning strategy to reduce latency while preserving translation quality. It uses a multistream decoder-only architecture with neural codec streams.

## Experiments and Evidence

The abstract reports state-of-the-art translation accuracy, latency, voice transfer, and naturalness across X-to-English tasks, plus adaptation to a new input language with less than 1000 hours of speech.

## Full-Text Upgrade

The full text emphasizes that sentence-level alignments are much easier to obtain across languages than word-level alignments. During RL, the model exploits sentence-level translation structure to reward correct and simultaneous outputs without requiring language-specific alignment heuristics.

Evaluation includes short-form Europarl-ST and long-form Audio-NTREX-4L, with metrics for translation quality, latency, speaker similarity, audio naturalness, and speech-to-text translation. The paper reports strong quality/latency tradeoffs against Seamless and Hibiki baselines, better speaker identity transfer and naturalness in S2ST, and Italian adaptation with under 1000 hours of speech.

## Limits and Failure Modes

Limits to watch: latency-quality tradeoffs remain tunable rather than solved; sentence-level coarse alignment can introduce higher latency patterns; adaptation quality may vary by language pair and speech resources; and human audio evaluations are expensive to scale.

## Deep Themes

- RL can replace brittle heuristic alignment in real-time speech translation.
- Multistream speech models can optimize quality and latency jointly.
- Removing alignment bottlenecks improves scalability to languages with different grammar and word order.

## Subthemes

- Simultaneous speech-to-speech translation.
- Sentence-level alignment.
- GRPO for latency.
- Neural codec models.
- Voice transfer.
- Multilingual speech benchmarks.

## Connections to Other Papers

Connects to h1 and DMPO through RL for sequence-generation behavior, and to evaluation/benchmarking papers through released multilingual speech evaluation data.

## Notes for Cross-Paper Synthesis

Hibiki-Zero adds a sequence-alignment theme: for multimodal generation, removing brittle supervision requirements can be as important as scaling the architecture.
