# Latent Speech-Text Transformer

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: krGpQzo8Mz
- Authors: Yen-Ju Lu; Yashesh Gaur; Wei Zhou; Benjamin Muller; Jesus Villalba; Najim Dehak; Luke Zettlemoyer; Gargi Ghosh; Mike Lewis; Srini Iyer; Duc Le
- Primary area: foundation or frontier models, including LLMs
- Keywords: Speech–Text Models;Latent Patching;Multimodal Alignment;Large Language Models
- Source URL: https://openreview.net/forum?id=krGpQzo8Mz
- PDF URL: https://openreview.net/pdf?id=krGpQzo8Mz

## Abstract

Auto-regressive speech-text models are typically pre-trained on a large number of interleaved sequences of text tokens and raw speech encoded as speech tokens using vector quantization. These models have demonstrated state-of-the-art performance in speech-to-speech understanding and generation benchmarks, together with promising scaling laws, primarily enabled by the representational alignment between text and speech. Nevertheless, they suffer from shortcomings, partly owing to the disproportionately longer sequences of speech tokens in contrast to textual tokens. This results in a large compute imbalance between modalities during pre-training as well as during inference, and a potential hindrance to effectively aligning speech and text, ultimately translating to several orders of magnitude slower scaling laws. We introduce the Latent Speech-Text Transformer (LST), which makes pre-training speech-text models more data-efficient by dynamically and inexpensively aggregating speech tokens into latent speech patches. These patches serve as higher-level units that can either align with corresponding textual units to aid capability transfer or even encapsulate common speech sequences like silences to be more compute-efficient. We show that LST outperforms vanilla approaches on speech-to-speech as well as text-to-text benchmarks in both data- and compute-controlled settings, the former indicating more effective representational alignment and the latter indicating steeper scaling laws for speech-text models. On HellaSwag story completion, LST achieves 6.5% absolute gain in speech accuracy under compute-controlled training and 5.3% under data-controlled training, while also improving text performance. We will release our models, code, and the evaluation data to facilitate further research.

## One-Sentence Claim

LST improves speech-text pretraining by dynamically aggregating long speech-token sequences into latent patches that better align with text units and reduce modality compute imbalance.

## Problem

Autoregressive speech-text models use vector-quantized speech tokens that are much longer than text token sequences. This creates compute imbalance during training and inference, slows scaling, and may make speech-text alignment harder.

## Core Contribution

The paper introduces the Latent Speech-Text Transformer, which performs inexpensive dynamic speech-token aggregation into latent speech patches. These higher-level units can align with text units for transfer or compress common speech patterns such as silence for efficiency.

## Method

LST pretrains on interleaved speech and text while replacing raw dense speech-token streams with latent speech patches. The patching mechanism dynamically groups speech tokens into higher-level units, reducing sequence length and creating representations that can better share structure with text.

## Experiments and Evidence

The abstract reports improvements over vanilla speech-text approaches on speech-to-speech and text-to-text benchmarks in both data-controlled and compute-controlled settings. On HellaSwag story completion, LST improves speech accuracy by 6.5 absolute points under compute-controlled training and 5.3 points under data-controlled training while improving text performance.

## Limits and Failure Modes

Speech patching could discard prosodic or phonetic detail important for generation, speaker identity, emotion, or low-resource languages. Alignment benefits may depend on patch granularity and training data composition. Full-text review should check how patches are formed, how silence/common patterns are handled, scaling-law measurement, speech generation quality, and multilingual robustness.

## Deep Themes

- Token compression for multimodal scaling.
- Speech-text representational alignment.
- Compute-balanced multimodal pretraining.
- Latent patching as modality abstraction.

## Subthemes

- Dynamic speech-token aggregation.
- Higher-level speech units.
- Speech-to-text capability transfer.
- Scaling laws under modality imbalance.
- Efficient speech-language inference.

## Connections to Other Papers

Connects to LPD through sequence-length reduction for efficient generation, to BioX-Bridge and other multimodal alignment methods through lightweight cross-modal abstractions, and to long-context work through the broader problem of token-budget pressure.

## Notes for Cross-Paper Synthesis

LST highlights a recurring multimodal scaling point: raw modality tokenization can dominate compute and distort alignment. Better units, not just larger models, can change scaling behavior.
