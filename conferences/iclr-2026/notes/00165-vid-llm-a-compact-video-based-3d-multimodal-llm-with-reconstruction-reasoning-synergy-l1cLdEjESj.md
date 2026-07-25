# Vid-LLM: A Compact Video-based 3D Multimodal LLM with Reconstruction–Reasoning Synergy

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: l1cLdEjESj
- Authors: Haijier Chen; Bo Xu; Shoujian zhang; Haoze Liu; Jiaxuan Lin; Jingrong Wang
- Primary area: foundation or frontier models, including LLMs
- Keywords: video-based 3D MLLM;geometric priors;Cross-Task Adapter;Metric Depth calibration
- Source URL: https://openreview.net/forum?id=l1cLdEjESj
- PDF URL: https://openreview.net/pdf?id=l1cLdEjESj

## Abstract

Recent developments in Multimodal Large Language Models (MLLMs) have significantly improved Vision–Language (VL) reasoning in 2D domains. However, extending these capabilities to 3D scene understanding remains a major challenge. Existing 3D Multimodal Large Language Models (3D-MLLMs) often depend on 3D data inputs, which limits scalability and generalization. To address this limitation, we propose Vid-LLM, a video-based 3D-MLLM that directly processes video inputs without requiring external 3D data, making it practical for real-world deployment. In our method, the geometric prior are directly used to improve the performance of the sceen perception. To integrate the geometric cues into the MLLM compactly, we design a Cross-Task Adapter (CTA) module to align the 3D geometric priors with the vision-language representations. To ensure geometric consistency and integrity, we introduce a Metric Depth Model that recovers real-scale geometry from the reconstruction outputs. Finally, the model is fine-tuned with a two-stage distillation optimization strategy, realizing fast convergence and stabilizes training. Extensive experiments across diverse benchmarks verified the effectiveness of our method on 3D Question Answering, 3D Dense Captioning and  3D Visual Grounding tasks,  demonstrating the superior multi-task capabilities.

## One-Sentence Claim

Vid-LLM turns ordinary video into a scalable input for 3D multimodal reasoning by aligning geometric reconstruction priors with vision-language representations through a compact adapter and depth calibration.

## Problem

3D MLLMs often require explicit 3D inputs, limiting scalability and deployment. Meanwhile, 2D vision-language MLLMs reason well but lack robust 3D scene understanding. The challenge is to inject geometric structure from video without requiring external 3D data pipelines.

## Core Contribution

The paper proposes a video-based 3D MLLM that uses geometric priors, a Cross-Task Adapter to align geometry with VL representations, a Metric Depth Model for real-scale geometry, and two-stage distillation for stable training.

## Method

Vid-LLM processes video inputs, extracts or reconstructs geometric priors, aligns those priors with MLLM representations through CTA, calibrates reconstruction outputs into metric depth, and fine-tunes the compact model with a two-stage distillation objective to connect reconstruction and reasoning.

## Experiments and Evidence

The abstract reports strong performance across 3D question answering, 3D dense captioning, and 3D visual grounding benchmarks, demonstrating multi-task 3D scene-understanding capability from video inputs.

## Limits and Failure Modes

Video-only 3D reasoning can fail under poor camera motion, occlusion, reflective surfaces, dynamic objects, scale ambiguity, or weak depth calibration. Full-text review should check benchmark diversity, depth supervision, adapter size, reconstruction quality, comparison to explicit 3D-input MLLMs, and real-world deployment constraints.

## Deep Themes

- Video as scalable 3D input.
- Reconstruction-reasoning synergy.
- Compact adapters for geometric priors.
- Metric depth calibration for MLLMs.

## Subthemes

- Cross-Task Adapter alignment.
- 3D question answering from video.
- Dense captioning and visual grounding.
- Distillation for multimodal 3D reasoning.
- Geometry-aware VL representations.

## Connections to Other Papers

Connects to VIST3A, RoSE, MomaGraph, and other 3D/embodied papers through reconstruction-informed reasoning, and to multimodal reward/evaluation work through the need for geometry-aware benchmarks beyond 2D visual QA.

## Notes for Cross-Paper Synthesis

Vid-LLM extends the modular-interface theme: geometric reconstruction is not the final product, but a compact prior aligned into a reasoning model. The broader pattern is using intermediate structure to make multimodal reasoning grounded.
