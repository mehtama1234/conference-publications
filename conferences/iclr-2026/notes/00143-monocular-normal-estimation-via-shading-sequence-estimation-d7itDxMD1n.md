# Monocular Normal Estimation via Shading Sequence Estimation

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: d7itDxMD1n
- Authors: Zongrui Li; Xinhua Ma; Minghui Hu; Yunqing Zhao; Yingchen Yu; Qian Zheng; Chang Liu; Xudong Jiang; Song Bai
- Primary area: generative models
- Keywords: Video Diffusion Model;Shading Estimation;Single-view Normal Estimation
- Source URL: https://openreview.net/forum?id=d7itDxMD1n
- PDF URL: https://openreview.net/pdf?id=d7itDxMD1n

## Abstract

Monocular normal estimation aims to estimate normal map from a single RGB image of an object under arbitrary lighting. Existing methods rely on deep models to directly predict normal maps. However, they often suffer from 3D misalignment: while the estimated normal maps may appear to have an overall correct color distribution, the reconstructed surfaces frequently fail to align with the geometry details. We argue that this misalignment stems from the current paradigm: the model struggles to distinguish and reconstruct spatially-various geometric, as they are represented in normal maps only by relatively subtle color variations. To address this issue, we propose a new paradigm that reformulates normal estimation as shading sequence estimation, where shading sequences are more sensitive to various geometry information. Building on this paradigm, we present RoSE, a method that leverages image-to-video generative models to predict shading sequences. The predicted shading sequences are then converted into normal maps by solving a simple ordinary least-squares problem. To enhance robustness and better handle complex objects, RoSE is trained on a synthetic dataset, dataset, with diverse shapes, materials, and light conditions. Experiments demonstrate that RoSE achieves state-of-the-art performance on real-world benchmark datasets for object-based monocular normal estimation. Codes and dataset will be released to facilitate reproducible research.

## One-Sentence Claim

RoSE reframes monocular normal estimation as shading-sequence prediction with image-to-video generative models, then recovers normals through least squares.

## Problem

Directly predicting normal maps from a single RGB object image can produce plausible colors but geometrically misaligned surfaces.

The paper argues that normal-map color changes encode geometry too subtly, making it hard for deep models to recover spatially varying details.

## Core Contribution

The paper proposes a new paradigm: estimate shading sequences first, then convert them into normal maps.

RoSE uses image-to-video generative models to predict shading sequences that are more sensitive to geometric variation.

## Method

Given a single image, RoSE predicts a sequence of shading observations under varying lighting-like conditions.

The predicted shading sequence is converted into a normal map by solving a simple ordinary least-squares problem. Training uses a synthetic dataset with diverse shapes, materials, and lighting.

## Experiments and Evidence

The abstract reports state-of-the-art performance on real-world object-based monocular normal estimation benchmarks.

The synthetic training data is designed to improve robustness for complex objects.

## Limits and Failure Modes

Shading cues can be ambiguous under complex materials, transparency, interreflection, cast shadows, or non-Lambertian surfaces. Synthetic-to-real transfer remains a key risk.

Because this note is abstract-only, details still need checking: shading sequence representation, video model, OLS formulation, synthetic dataset, real benchmarks, and material robustness.

## Deep Themes

- Indirect geometry estimation: predict an intermediate signal that makes geometry more observable.
- Generative video models for static 3D tasks: temporal/shading sequences become a tool for single-image reasoning.
- Physics-inspired reconstruction: least-squares normal recovery anchors generative predictions to a geometric equation.
- Synthetic data for robust perception: controlled shape/material/light variation supports real-world transfer.

## Subthemes

- Monocular normal estimation.
- Shading sequence estimation.
- Image-to-video generation.
- Ordinary least squares geometry recovery.

## Connections to Other Papers

This connects to DepthLM, XFactor, MetamerGen, and human geometry generation through 3D/spatial visual understanding.

It also relates to diffusion/video generation papers because generative models are repurposed for perception.

## Notes for Cross-Paper Synthesis

RoSE adds an intermediate-representation theme: hard dense prediction tasks can improve when reformulated through a physically meaningful proxy.
