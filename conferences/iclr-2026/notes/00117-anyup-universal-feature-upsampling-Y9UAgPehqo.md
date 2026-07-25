# AnyUp: Universal Feature Upsampling

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Y9UAgPehqo
- Authors: Thomas Wimmer; Prune Truong; Marie-Julie Rakotosaona; Michael Oechsle; Federico Tombari; Bernt Schiele; Jan Eric Lenssen
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: feature upsampling;representation learning
- Source URL: https://openreview.net/forum?id=Y9UAgPehqo
- PDF URL: https://openreview.net/pdf?id=Y9UAgPehqo

## Abstract

We introduce AnyUp, a method for feature upsampling that can be applied to any vision feature at any resolution, without encoder-specific training. Existing learning-based upsamplers for features like DINO or CLIP need to be re-trained for every feature extractor and thus do not generalize to different feature types at inference time. In this work, we propose an *inference-time* feature-agnostic upsampling architecture to alleviate this limitation and improve upsampling quality. In our experiments, AnyUp sets a new state of the art for upsampled features, generalizes to different feature types, and  preserves feature semantics while being efficient and easy to apply to a wide range of downstream tasks.

## One-Sentence Claim

AnyUp provides inference-time feature-agnostic upsampling that improves vision feature resolution without retraining for each encoder.

## Problem

Dense downstream vision tasks often need high-resolution features, but strong encoders such as DINO or CLIP may produce coarser feature maps.

Existing learned feature upsamplers are usually tied to a specific feature extractor, so they must be retrained when the encoder or feature type changes.

## Core Contribution

The paper introduces AnyUp, a universal feature upsampling method applicable to any vision feature at any resolution without encoder-specific training.

It aims to preserve feature semantics while improving spatial detail and downstream usability.

## Method

AnyUp is an inference-time feature-agnostic upsampling architecture.

Rather than learning a separate upsampler for each feature backbone, it operates generically over input feature maps and produces higher-resolution representations for downstream tasks.

## Experiments and Evidence

The abstract reports state-of-the-art upsampled feature quality.

AnyUp generalizes across feature types, preserves semantics, and is efficient and easy to apply across downstream tasks.

## Limits and Failure Modes

Universal upsampling may struggle when different encoders encode incompatible spatial semantics or when high-frequency detail was never present in the original features.

Because this note is abstract-only, details still need checking: architecture, supported feature families, downstream tasks, resolution factors, semantic preservation metrics, and compute overhead.

## Deep Themes

- Inference-time representation repair: feature quality is improved without retraining the encoder.
- Feature-agnostic tooling: downstream pipelines benefit from adapters that generalize across representation sources.
- Spatial detail versus semantic preservation: upsampling must add resolution without corrupting meaning.
- Universal vision infrastructure: reusable representation utilities reduce dependence on encoder-specific training.

## Subthemes

- Feature upsampling.
- Vision representations.
- Encoder-agnostic inference.
- Dense downstream tasks.

## Connections to Other Papers

This connects to DepthLM, DAVE, WAVE, and multimodal representation papers.

It also relates to InfoTok and HyCa because both operate on internal representation structure to improve efficiency or utility.

## Notes for Cross-Paper Synthesis

AnyUp adds a representation-tooling theme: reusable adapters can make foundation features more generally usable without model-specific retraining.
