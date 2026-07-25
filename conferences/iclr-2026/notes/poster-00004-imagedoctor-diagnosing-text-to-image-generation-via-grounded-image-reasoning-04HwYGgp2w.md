# ImageDoctor: Diagnosing Text-to-Image Generation via Grounded Image Reasoning

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 04HwYGgp2w
- Authors: Yuxiang Guo; Jiang Liu; Ze Wang; Hao Chen; Ximeng Sun; Yang Zhao; Jialian Wu; Xiaodong Yu; Zicheng Liu; Emad Barsoum
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Image reward model
- Source URL: https://openreview.net/forum?id=04HwYGgp2w
- PDF URL: https://openreview.net/pdf?id=04HwYGgp2w

## Abstract

The rapid advancement of text-to-image (T2I) models has increased the need for reliable human preference modeling, a demand further amplified by recent progress in reinforcement learning for preference alignment. However, existing approaches typically quantify the quality of a generated image using a single scalar, limiting their ability to provide comprehensive and interpretable feedback on image quality. To address this, we introduce ImageDoctor, a unified multi-aspect T2I model evaluation framework that assesses image quality across four complementary dimensions: plausibility, semantic alignment, aesthetics, and overall quality. ImageDoctor also provides pixel-level flaw indicators in the form of heatmaps, which highlight misaligned or implausible regions, and can be used as a dense reward for T2I model preference alignment. Inspired by the diagnostic process, we improve the detail sensitivity and reasoning capability of ImageDoctor by introducing a ``look-think-predict" paradigm, where the model first localizes potential flaws, then generates reasoning, and finally concludes the evaluation with quantitative scores. Built on top of a vision-language model and trained through a combination of supervised fine-tuning and reinforcement learning, ImageDoctor demonstrates strong alignment with human preference across multiple datasets, establishing its effectiveness as an evaluation metric. Furthermore, when used as a reward model for preference tuning, ImageDoctor significantly improves generation quality—achieving an improvement of 10% over scalar-based reward models.

## One-Sentence Claim

ImageDoctor evaluates text-to-image outputs with multi-aspect grounded reasoning and pixel-level flaw heatmaps, improving both interpretability and reward-model usefulness for preference tuning.

## Problem

Text-to-image preference models often reduce image quality to a single scalar score, which gives weak diagnostic feedback and limited dense supervision for alignment. Reliable preference tuning needs to identify what is wrong, where it is wrong, and how different quality dimensions contribute.

## Core Contribution

The paper introduces ImageDoctor, a unified evaluation framework scoring plausibility, semantic alignment, aesthetics, and overall quality while producing pixel-level flaw heatmaps. It can serve as both an interpretable evaluation metric and a dense reward model for T2I preference alignment.

## Method

ImageDoctor uses a vision-language model trained with supervised fine-tuning and reinforcement learning. Its "look-think-predict" process first localizes possible flaws, then generates reasoning, then outputs quantitative scores, increasing detail sensitivity and grounding.

## Experiments and Evidence

The abstract reports strong alignment with human preference across multiple datasets. When used as a reward model for preference tuning, ImageDoctor improves generation quality by 10% over scalar-based reward models.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect the heatmap-label source, reward-model training data, human-preference agreement statistics, susceptibility to reward hacking, and whether multi-aspect scores are calibrated across styles and prompt categories.

## Deep Themes

- Interpretable multimodal reward modeling.
- Dense visual feedback for generative alignment.
- Multi-aspect evaluation beyond scalar preference.
- Grounded reasoning for image diagnostics.

## Subthemes

- Plausibility.
- Semantic alignment.
- Aesthetics.
- Pixel-level flaw heatmaps.
- Look-think-predict.

## Connections to Other Papers

Connects to GLASS Flows through reward-aligned generative sampling, to EmotionThinker through explanation-quality rewards, and to DeceptionDecoded through grounded visual reasoning that moves beyond shallow cues.

## Notes for Cross-Paper Synthesis

ImageDoctor strengthens a major theme: evaluation signals are becoming richer, localized, and process-aware. The reward is no longer only a scalar preference; it can be a structured diagnosis that guides model improvement.
