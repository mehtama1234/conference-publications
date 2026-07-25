# Generative Human Geometry Distribution

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: YsQM7sQl0j
- Authors: Xiangjun Tang; Biao Zhang; Peter Wonka
- Primary area: generative models
- Keywords: 3D Generation;Human Generation;Geometry Encoding
- Source URL: https://openreview.net/forum?id=YsQM7sQl0j
- PDF URL: https://openreview.net/pdf?id=YsQM7sQl0j

## Abstract

Realistic human geometry generation is an important yet challenging task, requiring both the preservation of fine clothing details and the accurate modeling of clothing-body interactions. To tackle this challenge, we build upon Geometry distributions—a recently proposed representation that can model a single human geometry with high fidelity using a flow matching model. However, extending a single-geometry distribution to a dataset is non-trivial and inefficient for large-scale learning. To address this, we propose a new geometry distribution model by two key techniques: (1) encoding distributions as 2D feature maps rather than network parameters, and (2) using SMPL models as the domain instead of Gaussian and refining the associated flow velocity field. We then design a generative framework adopting a two-staged training paradigm analogous to state-of-the-art image and 3D generative models.
In the first stage, we compress geometry distributions into a latent space using a diffusion flow model; the second stage trains another flow model on this latent space. 
We validate our approach on two key tasks: pose-conditioned random avatar generation and avatar-consistent novel pose synthesis.
Experimental results demonstrate that our method outperforms existing state-of-the-art methods, achieving a 57% improvement in geometry quality.

## One-Sentence Claim

This paper scales geometry distributions to dataset-level human geometry generation by encoding distributions as 2D feature maps over SMPL domains and training flow models in two stages.

## Problem

Realistic human geometry generation must preserve clothing details and model clothing-body interactions.

Existing geometry distributions can represent a single human geometry with high fidelity, but extending them efficiently to dataset-scale generation is non-trivial.

## Core Contribution

The paper proposes a generative human geometry distribution model.

Its two key techniques are encoding distributions as 2D feature maps instead of network parameters and using SMPL models as the domain while refining the flow velocity field.

## Method

The framework uses a two-stage training pipeline analogous to modern image and 3D generative models.

First, a diffusion flow model compresses geometry distributions into a latent space. Second, another flow model learns to generate within that latent distribution for human geometry tasks.

## Experiments and Evidence

The abstract reports validation on pose-conditioned random avatar generation and avatar-consistent novel pose synthesis.

The method outperforms existing state-of-the-art methods and achieves a 57 percent improvement in geometry quality.

## Limits and Failure Modes

Human geometry quality depends on clothing diversity, body-shape coverage, pose extremes, and whether SMPL-domain assumptions can capture loose garments or accessories.

Because this note is abstract-only, details still need checking: geometry representation, SMPL mapping, flow objectives, datasets, quality metric, and comparison baselines.

## Deep Themes

- Distributional 3D geometry representation: generation operates over geometry distributions rather than single meshes alone.
- Human-specific geometric priors: SMPL provides a structured domain for scalable avatar generation.
- Flow-based 3D synthesis: diffusion/flow methods extend into detailed human geometry.
- Pose-consistent identity preservation: useful human generation must maintain avatar consistency across poses.

## Subthemes

- 3D human generation.
- Geometry distributions.
- SMPL-domain modeling.
- Pose-conditioned avatars.

## Connections to Other Papers

This connects to DepthLM, VectorWorld, DCFold, and physical/scientific generation through structured geometry modeling.

It also relates to NextStep-1 and diffusion-flow papers because it uses flow models to generate continuous structured objects.

## Notes for Cross-Paper Synthesis

This paper adds a geometry-generation theme: high-quality 3D generation often comes from choosing a domain-specific representation before scaling generative models.
