# Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: DdU1o2ZvWi
- Authors: Chufan Shi; Cheng Yang; Yaokang Wu; Linghao Jin; Bo Shui; Taylor Berg-Kirkpatrick; Xuezhe Ma
- Primary area: general_machine_learning->evaluation
- Keywords: Trustworthiness;Chain-of-Thought Reasoning;Multimodal
- Source URL: https://openreview.net/forum?id=DdU1o2ZvWi
- PDF URL: https://openreview.net/pdf?id=DdU1o2ZvWi

## Abstract

Vision-Language Models (VLMs) often produce self-reflective statements like “let me check the figure again” during reasoning. Do such state- ments trigger genuine visual re-examination, or are they merely learned textual patterns? We in- vestigate this via VISUALSWAP, an image-swap probing framework: after a model reasons over an image, we replace it with a visually similar but semantically different one and test whether the model notices. We introduce VS-BENCH, 800 image pairs curated from MathVista, Math- Verse, MathVision, and MMMU-Pro. Exper- iments on Qwen3-VL, Kimi-VL, and ERNIE- VL reveal a striking failure: models overwhelm- ingly miss the swap, with accuracy dropping by up to 60%. Counterintuitively, thinking mod- els are nearly 3x more vulnerable than their in- structed counterparts, and scaling offers no mit- igation. Multi-turn user instructions restore vi- sual grounding, but self-generated reflective state- ments during continuous generation do not. At- tention analysis explains why: user instructions substantially elevate attention to visual tokens, whereas self-reflection does not. Current VLMs tend to say rather than actually see when claiming to perform visual re-examination. Our code and dataset are available at the project page: https://visualswap.github.io/

## One-Sentence Claim

VISUALSWAP shows that VLM self-reflective claims of re-checking images often do not trigger real visual re-examination, while explicit user instructions can restore visual grounding.

## Problem

VLMs generate reasoning text such as "let me check again," but it is unclear whether this changes attention to visual evidence or merely repeats learned language patterns.

## Core Contribution

The paper introduces VISUALSWAP and VS-BENCH to test whether models notice when a visually similar but semantically different image replaces the original during reasoning.

## Method

After a model reasons over one image, the framework swaps in a paired image curated from MathVista, MathVerse, MathVision, and MMMU-Pro and checks whether the model detects the semantic change. Attention analysis compares self-reflection versus user-instructed re-examination.

## Experiments and Evidence

The abstract reports 800 image pairs, tests on Qwen3-VL, Kimi-VL, and ERNIE-VL, accuracy drops up to 60%, thinking models nearly 3x more vulnerable than instructed counterparts, and attention increases to visual tokens only under user instructions.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: swap-pair difficulty, turn protocol, scoring, attention-analysis reliability, and whether models can be trained to self-trigger re-examination.

## Deep Themes

- Self-reflective reasoning text can be decoupled from actual perceptual grounding.
- Multimodal models may say they are looking without allocating visual attention.
- User instructions and self-generated thoughts can have different control effects.

## Subthemes

- VLM trustworthiness.
- Visual re-examination.
- Chain-of-thought grounding.
- Image-swap probes.
- Visual attention.
- Multimodal reasoning.

## Connections to Other Papers

Connects to SAW-Bench, SpatioLM, UniPercept, and visual grounding/evaluation papers through failures of physically or perceptually grounded reasoning.

## Notes for Cross-Paper Synthesis

This paper adds a modality-grounding theme: verbal reasoning traces should not be assumed to imply renewed perceptual evidence use.
