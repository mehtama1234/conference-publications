# Motion Attribution for Video Generation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: zAl9heLw4q
- Authors: Xindi Wu; Despoina Paschalidou; Jun Gao; Antonio Torralba; Laura Leal-Taixé; Olga Russakovsky; Sanja Fidler; Jonathan Lorraine
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Data Attribution;Video Generation
- Source URL: https://openreview.net/forum?id=zAl9heLw4q
- PDF URL: https://openreview.net/pdf?id=zAl9heLw4q

## Abstract

Despite the rapid progress of video generation models, the role of data in influencing motion is poorly understood. We present Motive (MOTIon attribution for Video gEneration), a motion-centric, gradient-based data attribution framework that scales to modern, large, high-quality video datasets and models. We use this to study which fine-tuning clips improve or degrade temporal dynamics. Motive isolates temporal dynamics from static appearance via motion-weighted loss masks, yielding efficient and scalable motion-specific influence computation. On text-to-video models, Motive identifies clips that strongly affect motion and guides data curation that improves temporal consistency and physical plausibility. With Motive-selected high-influence data, we improve both motion smoothness and dynamic degree on VBench, achieving a 74.1% human preference win rate compared with the pretrained base model. To our knowledge, this is the first framework to attribute motion rather than visual appearance in video generative models and to use it to curate fine-tuning data.

## One-Sentence Claim

Motive attributes motion quality in video generation to fine-tuning clips, enabling data curation that improves temporal consistency and physical plausibility.

## Problem

Video generation has improved quickly, but the role of training and fine-tuning data in shaping motion remains poorly understood. Existing data attribution often focuses on appearance or static visual content.

The problem is to identify which clips improve or degrade temporal dynamics in large text-to-video models and datasets.

## Core Contribution

The paper introduces Motive, a motion-centric gradient-based data attribution framework for video generation.

Its core contribution is motion-specific influence estimation that isolates temporal dynamics from static appearance using motion-weighted loss masks, then uses high-influence data for curation.

## Method

Motive computes gradient-based influence for fine-tuning clips with respect to motion-focused losses. Motion-weighted masks emphasize temporal dynamics and reduce attribution to static appearance.

The resulting scores identify data that strongly affects motion, allowing the training set to be curated for smoother and more physically plausible videos.

## Experiments and Evidence

The abstract reports that Motive-selected data improves motion smoothness and dynamic degree on VBench.

It also reports a 74.1 percent human preference win rate over the pretrained base model when using high-influence data selected by Motive.

## Limits and Failure Modes

Gradient-based attribution can be expensive and may depend on the chosen motion loss. Motion masks may miss semantically important motion or confuse camera motion with object motion.

Because this note is abstract-only, details still need checking: model architecture, dataset scale, influence approximation, motion mask construction, VBench metrics, human study protocol, and whether curation harms appearance quality.

## Deep Themes

- Motion-specific data attribution: temporal dynamics need their own influence analysis.
- Data curation for generative quality: better motion can come from selecting the right fine-tuning clips.
- Separating appearance from dynamics: video attribution must isolate what changes over time.
- Scalable interpretability for generative data: attribution becomes an editing tool for datasets.

## Subthemes

- Motion-weighted loss masks.
- Text-to-video fine-tuning influence.
- Temporal consistency and physical plausibility.
- VBench-guided data curation.

## Connections to Other Papers

This connects to DAVE through attribution in visual models, but shifts the target from class evidence to temporal dynamics. It also connects to PanoWorld-X and VectorWorld because all focus on physically plausible generated motion.

It belongs with data-governance papers such as NASH and Self-Soupervision because data selection changes model behavior without changing architecture.

## Notes for Cross-Paper Synthesis

Motive adds a data-attribution thread for generative dynamics: not all training clips shape motion equally, and motion quality can be curated directly.
