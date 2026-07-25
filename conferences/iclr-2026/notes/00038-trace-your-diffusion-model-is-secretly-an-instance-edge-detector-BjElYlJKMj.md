# TRACE: Your Diffusion Model is Secretly an Instance Edge Detector

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: BjElYlJKMj
- Authors: Sanghyun Jo; Ziseok Lee; Wooyeol Lee; Jonghyun Choi; Jaesik Park; Kyungsu Kim
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: diffusion;unsupervised instance segmentation;weakly-supervised panoptic segmentation;inference dynamics;attention
- Source URL: https://openreview.net/forum?id=BjElYlJKMj
- PDF URL: https://openreview.net/pdf?id=BjElYlJKMj

## Abstract

High-quality instance and panoptic segmentation has traditionally relied on dense instance-level annotations such as masks, boxes, or points, which are costly, inconsistent, and difficult to scale. Unsupervised and weakly-supervised approaches reduce this burden but remain constrained by semantic backbone constraints and human bias, often producing merged or fragmented outputs. We present TRACE (TRAnsforming diffusion Cues to instance Edges), showing that text-to-image diffusion models secretly function as instance edge annotators. TRACE identifies the Instance Emergence Point (IEP) where object boundaries first appear in self-attention maps, extracts boundaries through Attention Boundary Divergence (ABDiv), and distills them into a lightweight one-step edge decoder. This design removes the need for per-image diffusion inversion, achieving 81× faster inference while producing sharper and more connected boundaries. On the COCO benchmark, TRACE improves unsupervised instance segmentation by +5.1 AP, and in tag-supervised panoptic segmentation it outperforms point-supervised baselines by +1.7 PQ without using any instance-level labels. These results reveal that diffusion models encode hidden instance boundary priors, and that decoding these signals offers a practical and scalable alternative to costly manual annotation. **Project Page:** https://shjo-april.github.io/TRACE.

## One-Sentence Claim

TRACE extracts hidden instance-boundary priors from text-to-image diffusion self-attention, turning diffusion models into scalable edge annotators for segmentation.

## Problem

Instance and panoptic segmentation normally require dense instance-level annotations such as masks, boxes, or points. These annotations are expensive, inconsistent, and hard to scale.

Unsupervised and weakly supervised methods reduce annotation burden but often produce merged or fragmented objects due to semantic backbone limits and human bias.

## Core Contribution

The paper proposes TRACE, Transforming diffusion Cues to instance Edges. It shows that text-to-image diffusion models internally encode instance edge information.

TRACE identifies an Instance Emergence Point in self-attention, extracts boundaries via Attention Boundary Divergence, and distills the signal into a lightweight one-step edge decoder.

## Method

TRACE analyzes diffusion inference dynamics to find when object boundaries first emerge in attention maps. ABDiv turns attention differences into boundary cues.

Instead of performing per-image diffusion inversion at inference, TRACE distills these cues into a one-step decoder for fast edge prediction.

## Experiments and Evidence

The abstract reports 81x faster inference after distillation while producing sharper and more connected boundaries.

On COCO, TRACE improves unsupervised instance segmentation by +5.1 AP and outperforms point-supervised baselines by +1.7 PQ in tag-supervised panoptic segmentation without instance-level labels.

## Limits and Failure Modes

The method depends on diffusion models' hidden boundary priors, which may reflect pretraining biases and may fail for unusual domains or ambiguous object boundaries.

Because this note is abstract-only, details still need checking: diffusion backbone, IEP detection, ABDiv formula, distillation data, edge decoder architecture, and domain-transfer results.

## Deep Themes

- Foundation models as annotators: hidden representations can replace manual labels.
- Diffusion inference dynamics as supervision: useful cues emerge at particular denoising stages.
- Attention-derived boundaries: self-attention can encode instance separation before explicit segmentation training.
- Distillation for practicality: slow introspection becomes deployable through a lightweight decoder.

## Subthemes

- Instance Emergence Point.
- Attention Boundary Divergence.
- Unsupervised instance segmentation.
- Tag-supervised panoptic segmentation.

## Connections to Other Papers

This connects to DAVE, Motion Attribution, and Information Flow through internal signal extraction. It also relates to Self-Soupervision and data curation because pretrained models provide supervision without labels.

It belongs in the interpretability-as-intervention cluster: model internals are decoded into useful artifacts.

## Notes for Cross-Paper Synthesis

TRACE adds a hidden-supervision theme: large generative models contain intermediate cues that can be mined and distilled for downstream perception tasks.
