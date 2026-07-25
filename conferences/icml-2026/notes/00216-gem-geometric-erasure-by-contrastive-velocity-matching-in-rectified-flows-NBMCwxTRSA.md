# GEM: Geometric Erasure by Contrastive Velocity Matching in Rectified Flows

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: NBMCwxTRSA
- Authors: Jonas Henry Grebe; Tobias Braun; Anna Rohrbach; Marcus Rohrbach
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: unlearning;concept erasure;diffusion models;safety;flux
- Source URL: https://openreview.net/forum?id=NBMCwxTRSA
- PDF URL: https://openreview.net/pdf?id=NBMCwxTRSA

## Abstract

While the rapid adoption of multimodal generative models offers immense potential, it has also increased the risks of harmful content synthesis, deepfakes, and copyright infringements. To address these challenges, concept erasure has emerged as a prospective safeguard. However, as the field gradually transitions from U-Net-based diffusion models to Rectified Flow Transformers, erasure research has struggled to keep pace. In this work, we introduce GEM, a simple but highly effective erasure framework for Rectified Flow models. As part of our contribution, we establish a principled bridge between trajectory-based unlearning grounded in Generative Flow Networks and classic teacher-guided erasure: we translate trajectory-based signals into a teacher-guided flow-matching setup that unifies the strengths of both paradigms. Concretely, a teacher provides complementary attraction and repulsion signals that we combine into a single geometric guidance objective, yielding targeted suppression of unwanted concepts while preserving benign generation.

## One-Sentence Claim

GEM erases unwanted concepts from Rectified Flow generative models by translating trajectory-based unlearning into teacher-guided contrastive velocity matching.

## Problem

Concept erasure is needed to reduce harmful synthesis, deepfakes, and copyright risks, but erasure methods have lagged behind the shift from U-Net diffusion models to Rectified Flow Transformers.

## Core Contribution

The paper introduces a geometric erasure framework that bridges Generative Flow Network trajectory unlearning and classic teacher-guided erasure through a unified flow-matching objective.

## Method

A teacher provides attraction and repulsion signals that are combined into one geometric guidance objective, suppressing unwanted concepts while preserving benign generation in Rectified Flow models.

## Experiments and Evidence

The abstract states that GEM is simple and highly effective, but does not list specific datasets or metrics in the available abstract.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: model families, concept sets, erasure metrics, retention-quality metrics, adversarial prompt robustness, and comparison to diffusion-era erasure baselines.

## Deep Themes

- Safety interventions must follow shifts in generative-model architecture.
- Concept erasure can be framed geometrically along generation trajectories.
- Attraction and repulsion signals encode preservation and suppression jointly.

## Subthemes

- Unlearning.
- Concept erasure.
- Rectified Flow Transformers.
- Flow matching.
- Generative safety.
- Copyright/deepfake risk.

## Connections to Other Papers

Connects to Biased Generalization, FlowGuard, DGS-Net, and watermarking/unlearning papers through generative-model safety and content control.

## Notes for Cross-Paper Synthesis

GEM adds a model-family adaptation theme for safety: safeguards must be reformulated when the underlying generative dynamics change.
