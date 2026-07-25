# Beyond Global Alignment: Fine-Grained Motion-Language Retrieval via Pyramidal Shapley-Taylor Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: RuTNWE1wr7
- Authors: Hanmo Chen; Guangtao Lyu; Chenghao Xu; Jiexi Yan; Xu Yang; Cheng Deng
- Primary area: general_machine_learning->unsupervised_and_semisupervised_learning
- Keywords: motion-language retrieval;motion representation learning;unsupervised learning
- Source URL: https://openreview.net/forum?id=RuTNWE1wr7
- PDF URL: https://openreview.net/pdf?id=RuTNWE1wr7

## Abstract

As a foundational task in human-centric cross-modal intelligence, motion-language retrieval aims to bridge the semantic gap between natural language and human motion, enabling intuitive motion analysis, yet existing approaches predominantly focus on aligning entire motion sequences with global textual representations. This global-centric paradigm overlooks fine-grained interactions between local motion segments and individual body joints and text tokens, inevitably leading to suboptimal retrieval performance. To address this limitation, we draw inspiration from the pyramidal process of human motion perception (from joint dynamics to segment coherence, and finally to holistic comprehension) and propose a novel Pyramidal Shapley-Taylor (PST) learning framework for fine-grained motion-language retrieval. Specifically, the framework decomposes human motion into temporal segments and spatial body joints, and learns cross-modal correspondences through progressive joint-wise and segment-wise alignment in a pyramidal fashion, effectively capturing both local semantic details and hierarchical structural relationships. Extensive experiments on multiple public benchmark datasets demonstrate that our approach significantly outperforms state-of-the-art methods, achieving precise alignment between motion segments and body joints and their corresponding text tokens.

## One-Sentence Claim

Pyramidal Shapley-Taylor learning improves motion-language retrieval by aligning text with local joints, temporal segments, and hierarchical motion structure rather than only global sequence representations.

## Problem

Motion-language retrieval systems usually align whole motion sequences with global text, missing fine-grained correspondences among body joints, motion segments, and tokens.

## Core Contribution

The paper introduces a pyramidal framework inspired by human motion perception that learns progressive joint-wise and segment-wise cross-modal correspondences.

## Method

PST decomposes motion into temporal segments and spatial joints, then applies Shapley-Taylor-style learning to capture local semantic details and hierarchical structural relationships between motion elements and language tokens.

## Experiments and Evidence

The abstract reports state-of-the-art performance on multiple public benchmarks and precise alignment between motion segments/body joints and corresponding text tokens.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, Shapley-Taylor computation cost, motion encoders, unsupervised setup, token-level alignment evaluation, and robustness to ambiguous language.

## Deep Themes

- Cross-modal alignment needs fine-grained local correspondences.
- Human motion perception suggests hierarchical joint-to-segment-to-whole structure.
- Retrieval benefits from decomposing global semantics into structured interactions.

## Subthemes

- Motion-language retrieval.
- Human motion representation.
- Shapley-Taylor interactions.
- Joint-wise alignment.
- Segment-wise alignment.
- Unsupervised/semi-supervised learning.

## Connections to Other Papers

Connects to XR-1, 3ViewSense, Table-GLS, and multimodal grounding papers through structured cross-modal alignment.

## Notes for Cross-Paper Synthesis

PST adds a motion-grounding theme: embodied language alignment must map words to body parts and temporal segments, not only entire sequences.
