# VideoKR: Towards Knowledge- and Reasoning-Intensive Video Understanding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: eXxFlOPTk4
- Authors: Lin Fu; Zheyuan Yang; Yang Wang; Tingyu Song; Arman Cohan; Yilun Zhao
- Primary area: applications->computer_vision
- Keywords: Video Understanding
- Source URL: https://openreview.net/forum?id=eXxFlOPTk4
- PDF URL: https://openreview.net/pdf?id=eXxFlOPTk4

## Abstract

We introduce VideoKR, the first large-scale training corpus specifically designed to strengthen knowledge- and reasoning-intensive video understanding. It comprises 315K video reasoning examples over 145K newly collected, CC-licensed, expert-domain videos. We develop a human-in-the-loop, skill-oriented example generation pipeline that targets progressively deeper video reasoning capabilities while ensuring the difficulty, diversity, and reliability of both the examples and their CoT rationales. We also curate VideoKR-Eval, a new expert-annotated benchmark where questions require genuine video understanding and knowledge-intensive reasoning rather than textual shortcuts. Our experiments show that, under a standard SFT$\rightarrow$GRPO pipeline, models post-trained on VideoKR outperform prior post-training approaches on knowledge-intensive video reasoning while remaining competitive on general video reasoning, highlighting data design as a key driver of progress in video reasoning. We further conduct comprehensive ablations to isolate the contributions of  VideoKR, providing actionable insights for future work.

## One-Sentence Claim

VideoKR shows that carefully designed, human-in-the-loop video reasoning data can substantially improve knowledge-intensive video understanding under SFT-to-GRPO post-training.

## Problem

Video-language models often improve on generic video QA while still relying on shallow cues or textual shortcuts. Knowledge-intensive video understanding requires domain knowledge, temporal evidence, and reasoning over what actually happens in the video.

The paper addresses the data bottleneck: existing post-training corpora may not target progressively deeper reasoning skills or reliable chain-of-thought rationales.

## Core Contribution

The contribution is VideoKR, a 315K-example training corpus built from 145K newly collected CC-licensed expert-domain videos, plus VideoKR-Eval, an expert-annotated benchmark for knowledge- and reasoning-intensive video understanding.

The data pipeline is human-in-the-loop and skill-oriented, explicitly aiming for difficulty, diversity, reliability, and deeper video reasoning capabilities.

## Method

The pipeline curates expert-domain videos, generates examples targeting specific reasoning skills, uses human involvement to improve reliability, and provides CoT rationales. Models are then post-trained with a standard SFT followed by GRPO pipeline.

VideoKR-Eval is designed to require genuine video understanding and knowledge reasoning rather than answerable text shortcuts.

## Experiments and Evidence

Evidence reported in the abstract:

- 315K video reasoning examples.
- 145K newly collected CC-licensed expert-domain videos.
- Expert-annotated VideoKR-Eval benchmark.
- Post-training with SFT -> GRPO.
- Outperformance over prior post-training approaches on knowledge-intensive video reasoning.
- Competitive general video-reasoning performance.
- Ablations isolating VideoKR's contributions.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: skill taxonomy, human review protocol, GRPO reward design, and benchmark contamination controls.

## Limits and Failure Modes

- CoT rationale reliability depends on the generation and review pipeline.
- Expert-domain coverage may improve depth but narrow generality.
- CC licensing helps reuse but does not by itself prove balanced coverage.
- Video reasoning benchmarks are vulnerable to language-only shortcuts unless carefully audited.

## Deep Themes

**Data design is a capability lever.** VideoKR treats dataset construction as the main route to deeper reasoning, not merely scale.

**Post-training is becoming skill-curriculum training.** The corpus is organized around progressively deeper capabilities.

**Evaluation must block shortcuts.** VideoKR-Eval tries to force genuine visual-temporal understanding.

## Subthemes

- Knowledge-intensive video reasoning.
- Human-in-the-loop data generation.
- Skill-oriented video curricula.
- SFT-to-GRPO multimodal post-training.
- Expert annotated evaluation.

## Connections to Other Papers

Connects to MoCA, Agent0-VL, VenusBench-Mobile, MADQA, and UniMapping. All emphasize that multimodal progress depends on targeted data, process diagnostics, or grounded world-state representations.

## Notes for Cross-Paper Synthesis

VideoKR reinforces the data-governance side of the 2026 story: better reasoning often comes from curating examples that force the desired cognitive operation and measuring whether shortcuts remain.
