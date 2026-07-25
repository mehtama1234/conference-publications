# 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Hm8OEDKpiO
- Authors: Shaoxiong Zhan; Yanlin Lai; Zheng Liu; Lin Hai; Shen Li; Xiaodong Cai; Zijian Lin; Wen Huang; Hai-Tao Zheng
- Primary area: applications->computer_vision
- Keywords: Mental Spatial Reasoning;Vision-Language Models;Spatial Intelligence
- Source URL: https://openreview.net/forum?id=Hm8OEDKpiO
- PDF URL: https://openreview.net/pdf?id=Hm8OEDKpiO

## Abstract

Current Large Language Models have achieved Olympiad-level logic, yet Vision-Language Models paradoxically falter on elementary spatial tasks like block counting. This capability mismatch reveals a critical "spatial intelligence gap," where models fail to construct coherent 3D mental representations from 2D observations. We uncover this gap via diagnostic analyses showing the bottleneck is a missing view-consistent spatial interface rather than insufficient visual features or weak reasoning. To bridge this, we introduce **3ViewSense**, a framework that grounds spatial reasoning in Orthographic Views. Drawing on engineering cognition, we propose a "Simulate-and-Reason" mechanism that decomposes complex scenes into canonical orthographic projections to resolve geometric ambiguities. By aligning egocentric perceptions with these allocentric references, our method facilitates explicit mental rotation and reconstruction. Empirical results on spatial reasoning benchmarks demonstrate that our method significantly outperforms existing baselines, with consistent gains on occlusion-heavy counting and view-consistent spatial reasoning. The framework also improves the stability and consistency of spatial descriptions, offering a scalable path toward stronger spatial intelligence in multimodal systems.

## One-Sentence Claim

3ViewSense improves VLM spatial reasoning by simulating canonical orthographic views that support mental rotation, reconstruction, and view-consistent descriptions.

## Problem

Vision-language models can perform strong symbolic reasoning yet fail at elementary spatial tasks because they lack a coherent interface for building 3D mental representations from 2D observations.

## Core Contribution

The paper diagnoses the spatial intelligence gap as a missing view-consistent spatial interface and proposes orthographic-view grounding as a scalable mechanism for spatial reasoning.

## Method

3ViewSense uses a Simulate-and-Reason procedure that decomposes scenes into canonical orthographic projections, aligns egocentric perception with allocentric references, and uses this structure to resolve geometric ambiguity.

## Experiments and Evidence

The abstract reports significant improvements over baselines on spatial reasoning benchmarks, especially occlusion-heavy counting and view-consistent reasoning, plus improved stability and consistency of spatial descriptions.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark construction, rendering assumptions, prompt or model dependencies, 3D scene complexity, and whether orthographic decomposition helps outside block-like geometry.

## Deep Themes

- Spatial intelligence requires explicit representational interfaces.
- Mental simulation can bridge perception and reasoning in VLMs.
- Orthographic/allocentric structure counters ambiguity in egocentric visual input.

## Subthemes

- Vision-language models.
- Spatial reasoning.
- Mental rotation.
- Orthographic projections.
- Occlusion-heavy counting.
- 3D reconstruction from 2D views.

## Connections to Other Papers

Connects to VGGT-Motion, SpatioLM, SAW-Bench, and embodied AI work through spatial consistency. It also parallels process-structured reasoning papers by inserting an intermediate representation before final answers.

## Notes for Cross-Paper Synthesis

3ViewSense adds a clear spatial-interface theme: multimodal models may need explicit geometric workspaces, not just stronger visual encoders or larger language reasoning heads.
