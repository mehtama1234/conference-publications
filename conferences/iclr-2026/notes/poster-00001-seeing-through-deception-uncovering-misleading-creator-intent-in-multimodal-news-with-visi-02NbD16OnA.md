# Seeing Through Deception: Uncovering Misleading Creator Intent in Multimodal News with Vision-Language Models

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 02NbD16OnA
- Authors: Jiaying Wu; Fanxiao Li; Zihang Fu; Min-Yen Kan; Bryan Hooi
- Primary area: datasets and benchmarks
- Keywords: multimodal misinformation detection;vision-language models;creator intent
- Source URL: https://openreview.net/forum?id=02NbD16OnA
- PDF URL: https://openreview.net/pdf?id=02NbD16OnA

## Abstract

The impact of misinformation arises not only from factual inaccuracies but also from the misleading narratives that creators deliberately embed. Interpreting such creator intent is therefore essential for multimodal misinformation detection (MMD) and effective information governance. To this end, we introduce DeceptionDecoded, a large-scale benchmark of 12,000 image–caption pairs grounded in trustworthy reference articles, created using an intent-guided simulation framework that models both the desired influence and the execution plan of news creators. The dataset captures both misleading and non-misleading cases, spanning manipulations across visual and textual modalities, and supports three intent-centric tasks: (1) misleading intent detection, (2) misleading source attribution, and (3) creator desire inference. We evaluate 14 state-of-the-art vision–language models (VLMs) and find that they struggle with intent reasoning, often relying on shallow cues such as surface-level alignment, stylistic polish, or heuristic authenticity signals. These results highlight the limitations of current VLMs and position DeceptionDecoded as a foundation for developing intent-aware models that go beyond shallow cues in MMD.

## One-Sentence Claim

DeceptionDecoded benchmarks whether VLMs can infer misleading creator intent in multimodal news, showing that current models rely on shallow cues rather than deeper intent reasoning.

## Problem

Misinformation is not only about factual error; misleading narratives can be deliberately constructed through the interaction of image and caption. Multimodal misinformation detection therefore needs to reason about creator intent, source of manipulation, and desired influence rather than only image-text consistency.

## Core Contribution

The paper introduces DeceptionDecoded, a 12,000-pair image-caption benchmark grounded in trustworthy reference articles and built through an intent-guided simulation framework. It supports misleading intent detection, misleading source attribution, and creator desire inference.

## Method

The dataset construction models both desired creator influence and execution plan, producing misleading and non-misleading multimodal news examples across visual and textual manipulations. The evaluation tests 14 state-of-the-art VLMs on intent-centric tasks.

## Experiments and Evidence

The abstract reports that evaluated VLMs struggle with intent reasoning and often fall back on shallow signals such as surface alignment, stylistic polish, or heuristic authenticity cues. The benchmark is positioned as a foundation for intent-aware multimodal misinformation detection.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect how trustworthy references are selected, how simulated creator intent is validated, whether generated manipulations resemble real misinformation campaigns, and how task labels separate intent from factuality. Dataset artifacts could let models learn simulation patterns rather than real intent reasoning.

## Deep Themes

- Intent-aware multimodal misinformation detection.
- VLM evaluation beyond surface image-text alignment.
- Information governance through creator-intent modeling.
- Dataset simulation grounded in reference articles.

## Subthemes

- DeceptionDecoded.
- Misleading source attribution.
- Creator desire inference.
- Image-caption manipulation.
- Shallow-cue failure modes.

## Connections to Other Papers

Connects to RedTeamCUA through environment-embedded deception, to ImageDoctor through grounded visual reasoning for evaluation, and to WIMHF/AdAEM through richer preference or value diagnostics beyond scalar labels.

## Notes for Cross-Paper Synthesis

This paper adds another case where evaluation shifts from output correctness to latent intent or rationale. The common pattern is that frontier multimodal systems can match surfaces while missing the causal or strategic structure behind them.
