# WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: MiV3WXDYJb
- Authors: Changli Tang; Qinfan Xiao; Ke Mei; Tianyi Wang; Fengyun Rao; Chao Zhang
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: audio-visual embeddings;multimodal LLMs;video retrieval
- Source URL: https://openreview.net/forum?id=MiV3WXDYJb
- PDF URL: https://openreview.net/pdf?id=MiV3WXDYJb

## Abstract

While embeddings from multimodal large language models (LLMs) excel as general-purpose representations, their application to dynamic modalities like audio and video remains underexplored. We introduce WAVE (\textbf{u}nified \& \textbf{v}ersatile \textbf{a}udio-\textbf{v}isual \textbf{e}mbeddings), the first LLM-based embedding that creates a unified representation space for text, audio, and video modalities. WAVE employs a novel hierarchical feature fusion strategy and a joint multi-modal, multi-task training approach to enable two key capabilities: any-to-any cross-modal retrieval and the generation of prompt-aware embeddings tailored to user instructions. Experimentally, WAVE sets a new state-of-the-art on the MMEB-v2 video benchmark and achieves superior results in audio and video-to-audio retrieval. Its prompt-aware nature also yields remarkable performance in multimodal question answering, significantly outperforming existing embedding models. Ablation studies validate our joint training strategy, demonstrating improved performance across all modalities.  With a newly introduced benchmark for versatile audio-visual learning, WAVE opens up broad possibilities for cross-modal, any-to-any applications. Our code, checkpoints, and data will be released.

## One-Sentence Claim

WAVE learns a unified prompt-aware embedding space for text, audio, and video that supports any-to-any retrieval and multimodal QA.

## Problem

Multimodal LLM embeddings are useful general-purpose representations, but dynamic modalities such as audio and video remain less developed than image-text embedding spaces.

Applications need representations that can align text, audio, and video in both directions, while adapting retrieval behavior to user instructions.

## Core Contribution

The paper introduces WAVE, an LLM-based unified audio-visual-text embedding model.

It combines hierarchical feature fusion with joint multi-modal, multi-task training to enable any-to-any cross-modal retrieval and prompt-aware embeddings.

## Method

WAVE fuses audio and video features hierarchically and trains across multiple modalities and tasks so that text, audio, and video live in a shared representation space.

The prompt-aware embedding mechanism conditions representations on user instructions, allowing the same media item to be retrieved or compared differently depending on the task.

## Experiments and Evidence

The abstract reports state-of-the-art performance on the MMEB-v2 video benchmark.

WAVE also improves audio retrieval and video-to-audio retrieval, and its prompt-aware embeddings substantially outperform existing embedding models on multimodal question answering. Ablations support the joint training strategy.

## Limits and Failure Modes

Unified embeddings can blur modality-specific detail if the shared space over-optimizes average retrieval performance. Prompt-aware embeddings may also be sensitive to prompt phrasing.

Because this note is abstract-only, details still need checking: model backbone, training data composition, benchmark construction, negative sampling, prompt conditioning mechanism, and modality-specific failure cases.

## Deep Themes

- Any-to-any multimodal retrieval: embedding models are moving beyond pairwise image-text or video-text alignment.
- Prompt-aware representation: embeddings become conditional task objects rather than static item descriptors.
- Dynamic-modal foundation embeddings: audio and video require temporal fusion strategies absent from static-image embeddings.
- Multi-task multimodal unification: broad embedding utility comes from training across retrieval and QA objectives.

## Subthemes

- Audio-video-text embeddings.
- Hierarchical feature fusion.
- Prompt-conditioned retrieval.
- MMEB-v2 video evaluation.

## Connections to Other Papers

This connects to InfoTok, FlashVID, ThinkV, and MC-Search through efficient and retrievable multimodal representations.

It also relates to Q-RAG because prompt-aware embeddings can act as the retrieval substrate for multi-step information access.

## Notes for Cross-Paper Synthesis

WAVE strengthens the representation-infrastructure theme: retrieval quality increasingly depends on embeddings that are multimodal, task-conditioned, and temporally aware.
