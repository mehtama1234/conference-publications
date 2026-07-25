# Decoupling Skeleton and Flesh: Efficient Multimodal Table Reasoning with Disentangled Alignment and Structure-aware Guidance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: PN7l7mBPDO
- Authors: Yingjie Zhu; Xuefeng Bai; Kehai Chen; Yang Xiang; Youcheng Pan; Xiaoqiang Zhou; Min Zhang
- Primary area: applications->computer_vision
- Keywords: Multimodal Table Understanding;Large Vision-Language Models
- Source URL: https://openreview.net/forum?id=PN7l7mBPDO
- PDF URL: https://openreview.net/pdf?id=PN7l7mBPDO

## Abstract

Reasoning over table images remains challenging for Large Vision-Language Models (LVLMs) due to complex layouts and tightly coupled structure-content information. Existing solutions often depend on expensive supervised training, reinforcement learning, or external tools, limiting efficiency and scalability. This work addresses a key question: how to adapt LVLMs to table reasoning with minimal annotation and no external tools? Specifically, we first introduce DiSCo, a Disentangled Structure-Content alignment framework that explicitly separates structural abstraction from semantic grounding during multimodal alignment, efficiently adapting LVLMs to tables structures. Building on DiSCo, we further present Table-GLS, a Global-to-Local Structure-guided reasoning framework that performs table reasoning via structured exploration and evidence-grounded inference. Extensive experiments across diverse benchmarks demonstrate that our framework efficiently enhances LVLM's table understanding and reasoning capabilities, particularly generalizing to unseen table structures. Our data and code are available at https://github.com/AAAndy-Zhu/TableVLM.

## One-Sentence Claim

DiSCo and Table-GLS improve LVLM table reasoning by disentangling table structure from content and guiding reasoning through global-to-local structural exploration.

## Problem

LVLMs struggle with table images because layout structure and semantic cell content are tightly coupled, while many existing methods require costly supervision, RL, or external tools.

## Core Contribution

The paper introduces Disentangled Structure-Content alignment for efficient table adaptation and Table-GLS for evidence-grounded structure-guided reasoning without external tools.

## Method

DiSCo separates structural abstraction from semantic grounding during multimodal alignment. Table-GLS then reasons over tables using structured exploration from global layout to local evidence.

## Experiments and Evidence

The abstract reports improved table understanding and reasoning across diverse benchmarks, with particular generalization to unseen table structures.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: annotation requirements, benchmark list, unseen-structure split design, robustness to OCR errors, table complexity, and comparison to tool-using table agents.

## Deep Themes

- Multimodal reasoning benefits from disentangling structure from content.
- Tables require explicit layout abstractions, not only visual-language alignment.
- Global-to-local exploration can make evidence grounding more efficient.

## Subthemes

- Multimodal table understanding.
- LVLMs.
- Structure-content disentanglement.
- Global-to-local reasoning.
- Evidence grounding.
- Unseen table generalization.

## Connections to Other Papers

Connects to 3ViewSense, VGS, causal route gating, and multimodal reasoning papers through explicit intermediate structures for grounding.

## Notes for Cross-Paper Synthesis

This paper adds a document-structure grounding theme: multimodal systems need representations of layout skeletons as separate objects from semantic content.
