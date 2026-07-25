# PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: xEgoeNrp8B
- Authors: Yuyang Yin; Hao-Xiang Guo; Fangfu Liu; Mengyu Wang; Hanwen Liang; Eric Li; Yikai Wang; Xiaojie Jin; Yao Zhao; Yunchao Wei
- Primary area: applications->computer_vision
- Keywords: Explorable Immersive Scene Video Generation
- Source URL: https://openreview.net/forum?id=xEgoeNrp8B
- PDF URL: https://openreview.net/pdf?id=xEgoeNrp8B

## Abstract

Achieving a complete and explorable 360-degree visual world is a cornerstone of immersive content creation. While recent advances in video generation have achieved impressive results, they follow a 2D paradigm that treats content generation as transitions of 2D pixels, lacking an intrinsic understanding of the physical 3D world, resulting in frequent geometric inconsistencies.
To achieve an explorable and physical-consistent visual world, the generation process should shift to a 3D paradigm: the visual content is governed by the physical relationships of the entire 3D environment together with 3D motion signals. However, under this setting, the conventional modeling methods and control signals, such as spatial attention computation in a 2D space, become unsuitable and ineffective.
To address this, we propose PanoWorld-X for explorable immersive scene video generation. Our framework is built on the panoramic representation, which naturally maps a 3D scene into a standard format and provides an ideal basis for consistency. Specifically, we first develop a data curation pipeline to produce high-quality and large-motion 3D scene evolution with movement trajectories. To achieve precise control, we design the Exploration Panoramic Plücker Embedding (PPE), a guidance signal tailored for 3D motion. Furthermore, leveraging the spherical geometric properties of panoramic data, we propose a sphere-aware attention mechanism, which can capture true geometric adjacency by reprojecting features onto a spherical surface. Extensive experiments demonstrate that PanoWorld-X achieves superior performance in motion range, control precision, and visual quality, underscoring its potential for real-world applications.

## One-Sentence Claim

PanoWorld-X generates explorable 360-degree scene videos by moving video diffusion from flat 2D pixel transitions to sphere-aware panoramic representations guided by 3D motion signals.

## Problem

Standard video generation treats scenes as 2D pixel transitions. That can produce visually impressive clips, but it lacks intrinsic 3D consistency and often fails when users want an explorable panoramic world with large motion.

The problem is that conventional 2D spatial attention and control signals do not match the geometry of panoramic scenes or the physical relationships of a 3D environment.

## Core Contribution

The paper introduces PanoWorld-X, a framework for explorable immersive scene video generation built around panoramic representations.

Its main contributions are a data curation pipeline for large-motion 3D scene evolution, Exploration Panoramic Plucker Embedding as a 3D-motion guidance signal, and sphere-aware attention that captures geometric adjacency by reprojecting features onto a spherical surface.

## Method

PanoWorld-X uses panoramic representation as the standard format for 360-degree scene generation. The Exploration Panoramic Plucker Embedding encodes movement trajectories and 3D motion control.

Sphere-aware attention uses the spherical geometry of panoramic data, avoiding adjacency errors caused by treating equirectangular panoramas as ordinary 2D grids.

## Experiments and Evidence

The abstract reports superior performance in motion range, control precision, and visual quality, emphasizing potential for immersive real-world applications.

It also claims the curated data pipeline produces high-quality large-motion 3D scene evolution with movement trajectories.

## Limits and Failure Modes

Panoramic diffusion may still struggle with long-horizon physical consistency, occlusion, object permanence, and accumulated drift during exploration. Spherical attention can fix geometry adjacency but not all 3D scene-state errors.

Because this note is abstract-only, details still need checking: data sources, trajectory annotations, Plucker embedding implementation, panorama projection artifacts, evaluation metrics, and whether generated worlds remain consistent under repeated navigation.

## Deep Themes

- 3D-aware generative video: immersive content requires scene geometry, not only pixel dynamics.
- Representation geometry matters: spherical adjacency changes what attention should consider local.
- Control signals for exploration: camera motion needs explicit 3D guidance.
- Data curation as capability: large-motion panoramic generation depends on suitable trajectory data.

## Subthemes

- Panoramic video diffusion.
- Sphere-aware attention.
- Exploration Panoramic Plucker Embedding.
- Explorable 360-degree worlds.

## Connections to Other Papers

This connects to Beyond Language Modeling, EgoTactile, and CoEvol-NO through world modeling and physical consistency. It also relates to SplAttN because both replace flat projection assumptions with geometry-aware cross-space representations.

It belongs with generative physical-scene papers that treat visual generation as structured scene evolution rather than independent frame synthesis.

## Notes for Cross-Paper Synthesis

This paper strengthens the geometry-aware generation theme: visual generative models need representations whose topology matches the world they are asked to synthesize.
