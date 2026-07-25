# COMPACT: COMPositional Atomic-to-Complex Visual Capability Tuning

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 073WQjmWKU
- Authors: Xindi Wu; Hee Seung Hwang; Polina Kirichenko; Esin Tureci; Olga Russakovsky
- Primary area: foundation or frontier models, including LLMs
- Keywords: Complexity;Compositionality;Visual instruction tuning
- Source URL: https://openreview.net/forum?id=073WQjmWKU
- PDF URL: https://openreview.net/pdf?id=073WQjmWKU

## Abstract

Visual instruction tuning (VIT) datasets consist of randomly sampled image-question pairs without regard to the informativeness of each pair. Recent dataset selection methods have shown that a small fraction of such datasets enriched with informative samples can lead to efficient finetuning of Multimodal Large Language Models. In this work, we explore the impact of task complexity on informative data curation and introduce COMPACT (COMPositional Atomic-to-complex Visual Capability Tuning), a VIT data recipe that scales training sample complexity by combining multiple atomic visual capabilities in a single training example. Concretely, we synthesize rich and informative text questions for each image, allowing us to significantly reduce the number of training examples required for effective visual instruction tuning. COMPACT demonstrates superior data efficiency compared to existing data reduction methods. When applied to the LLaVA-665K VIT dataset, COMPACT reduces the data budget by 90% while still achieving 100.2% of the full VIT performance (compared to only 97.5% by the state-of-the-art method) across eight multimodal benchmarks. Further, training on the same COMPACT data even improves performance compared to training with full-scale data on particularly complex benchmarks such as MM-Vet (+8.6%) and MMStar (+2.9%). COMPACT offers a scalable and efficient synthetic data generation recipe to improve on visual language tasks.

## One-Sentence Claim

COMPACT improves visual instruction tuning data efficiency by synthesizing complex questions that combine multiple atomic visual capabilities in each training example.

## Problem

Visual instruction tuning datasets often sample image-question pairs without considering informativeness. Data selection can reduce dataset size, but it may miss the role of task complexity and compositionality in making each example train more capabilities.

## Core Contribution

The paper contributes COMPACT, a data recipe for compositional atomic-to-complex visual capability tuning. It synthesizes rich text questions per image so a smaller number of examples covers more visual skills and harder reasoning patterns.

## Method

COMPACT scales sample complexity by combining multiple atomic visual capabilities into a single training example. Instead of merely selecting a subset of existing image-question pairs, it synthesizes informative questions designed to exercise compositional visual capabilities.

## Experiments and Evidence

On LLaVA-665K, COMPACT reduces the data budget by 90% while achieving 100.2% of full VIT performance across eight multimodal benchmarks, compared with 97.5% for the reported state-of-the-art data reduction method. It improves over full-scale data on complex benchmarks such as MM-Vet by 8.6% and MMStar by 2.9%.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect how atomic capabilities are defined, how synthetic questions are generated and filtered, whether benchmark overlap influences gains, and whether compositional complexity causes distribution shift or annotation artifacts. Overly dense examples may also underrepresent simple perceptual grounding.

## Deep Themes

- Data-efficient visual instruction tuning.
- Compositional skill coverage.
- Synthetic question generation.
- Informative sample complexity over raw dataset size.

## Subthemes

- COMPACT.
- Atomic-to-complex visual capabilities.
- LLaVA-665K.
- MM-Vet and MMStar.
- Data reduction.

## Connections to Other Papers

Connects to Learning to See Before Seeing and COMPACT-style data curation themes, to DeceptionDecoded through synthetic multimodal task construction, and to ScaleCUA through data-driven scaling under constrained budgets.

## Notes for Cross-Paper Synthesis

COMPACT reinforces the idea that data efficiency comes from capability density. A smaller dataset can outperform a larger one when each example composes multiple informative skills rather than repeating easy patterns.
