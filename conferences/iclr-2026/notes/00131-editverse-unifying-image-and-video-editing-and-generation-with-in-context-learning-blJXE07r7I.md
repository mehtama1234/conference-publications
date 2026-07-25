# EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: blJXE07r7I
- Authors: Xuan Ju; Tianyu Wang; Yuqian Zhou; He Zhang; Qing Liu; Nanxuan Zhao; Zhifei Zhang; Yijun Li; Yuanhao Cai; Shaoteng Liu; Daniil Pakhomov; Zhe Lin; Soo Ye Kim; Qiang Xu
- Primary area: generative models
- Keywords: Video Editing;Content Generation;Artificial Intelligence
- Source URL: https://openreview.net/forum?id=blJXE07r7I
- PDF URL: https://openreview.net/pdf?id=blJXE07r7I

## Abstract

Recent advances in foundation models highlight a clear trend toward unification and scaling, showing emergent capabilities across diverse domains. While image generation and editing have rapidly transitioned from task-specific to unified frameworks, video generation and editing remain fragmented due to architectural limitations and data scarcity. In this work, we introduce EditVerse, a unified framework for image and video generation and editing within a single model. By representing all modalities, i.e., text, image, and video, as a unified token sequence, EditVerse leverages self-attention to achieve robust in-context learning, natural cross-modal knowledge transfer, and flexible handling of inputs and outputs with arbitrary resolutions and durations. To address the lack of video editing training data, we design a scalable data pipeline that curates 232K video editing samples and combines them with large-scale image and video datasets for joint training. Furthermore, we present EditVerseBench, the first benchmark for instruction-based video editing covering diverse tasks and resolutions. Extensive experiments and user studies demonstrate that EditVerse achieves state-of-the-art performance, surpassing existing open-source and commercial models, while exhibiting emergent editing and generation abilities across modalities.

## One-Sentence Claim

EditVerse unifies image and video generation and editing in one token-sequence model, using in-context learning and a large curated video-editing dataset.

## Problem

Image generation and editing have moved toward unified frameworks, but video generation and editing remain fragmented because of architectural limits and scarce video-editing training data.

Users need models that can flexibly handle text, image, and video inputs/outputs across different resolutions, durations, and editing tasks.

## Core Contribution

The paper introduces EditVerse, a single model for image and video generation and editing.

It represents text, image, and video as one unified token sequence and contributes a scalable data pipeline with 232K curated video-editing samples plus EditVerseBench for instruction-based video editing.

## Method

EditVerse uses self-attention over unified multimodal token sequences to support in-context learning, cross-modal transfer, and flexible input/output formats.

The training mix combines curated video editing data with large-scale image and video datasets for joint training.

## Experiments and Evidence

The abstract reports extensive experiments and user studies.

EditVerse achieves state-of-the-art results against open-source and commercial models and shows emergent editing and generation abilities across modalities.

## Limits and Failure Modes

Unified image/video models can suffer task interference, temporal inconsistency, or weak instruction adherence on rare edits. User studies need careful protocol and baseline selection.

Because this note is abstract-only, details still need checking: tokenizer design, data curation filters, EditVerseBench tasks, resolution/duration limits, user-study setup, and temporal metrics.

## Deep Themes

- Unified multimodal editing: generation and editing become one sequence-modeling task.
- In-context visual editing: examples and instructions condition behavior without task-specific heads.
- Data pipeline as capability source: curated video editing pairs fill a bottleneck in model unification.
- Cross-modal transfer: image and video training reinforce each other through shared tokens.

## Subthemes

- Image/video generation.
- Instruction-based video editing.
- Unified token sequences.
- EditVerseBench.

## Connections to Other Papers

This connects to UALM, NextStep-1, Stable Video Infinity, WAVE, and InfoTok through multimodal token unification.

It also relates to GEPA and prompt-conditioned systems because in-context examples become part of the editing interface.

## Notes for Cross-Paper Synthesis

EditVerse strengthens the unification theme: modality-specific pipelines are being replaced by token-sequence systems that can edit and generate across formats.
