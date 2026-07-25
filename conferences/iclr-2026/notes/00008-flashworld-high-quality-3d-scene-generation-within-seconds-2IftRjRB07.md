# FlashWorld: High-quality 3D Scene Generation within Seconds

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 2IftRjRB07
- Authors: Xinyang Li; Tengfei Wang; Zixiao Gu; Shengchuan Zhang; Chunchao Guo; Liujuan Cao
- Primary area: generative models
- Keywords: 3D Scene Generation;Multi-view Diffusion Models;World Models;Distribution Matching Distillation
- Source URL: https://openreview.net/forum?id=2IftRjRB07
- PDF URL: https://openreview.net/pdf?id=2IftRjRB07

## Abstract

We propose FlashWorld, a generative model that produces 3D scenes from a single image or text prompt in seconds, $10 \sim 100\times$ faster than previous works while possessing superior rendering quality.
Our approach shifts from the conventional multi-view-oriented (MV-oriented) paradigm, which generates multi-view images for subsequent 3D reconstruction, to a 3D-oriented approach where the model directly produces 3D Gaussian representations during multi-view generation.
While ensuring 3D consistency, 3D-oriented method typically suffers poor visual quality.
FlashWorld includes a dual-mode pre-training phase followed by a cross-mode post-training phase, effectively integrating the strengths of both paradigms.
Specifically, leveraging the prior from a video diffusion model, we first pre-train a dual-mode multi-view diffusion model, which jointly supports MV-oriented and 3D-oriented generation mode. 
To bridge the quality gap in 3D-oriented generation, we further propose a cross-mode post-training distillation by matching distribution from consistent 3D-oriented mode to high-quality MV-oriented mode. 
This not only enhances visual quality while maintaining 3D consistency, but also reduces the required denoising steps for inference.
Also, we propose a strategy to leverage massive single-view images and text prompts during this process to enhance the model's generalization to out-of-distribution inputs.
Extensive experiments demonstrate the superiority and efficiency of our method.
Our code is released at https://github.com/imlixinyang/FlashWorld.

## One-Sentence Claim

FlashWorld generates high-quality 3D scenes from a single image or text prompt within seconds by combining multi-view diffusion with direct 3D Gaussian generation and cross-mode distillation.

## Problem

Existing 3D scene generation often relies on multi-view image generation followed by reconstruction, which can be slow, while direct 3D-oriented generation improves consistency but tends to reduce visual quality.

## Core Contribution

The paper introduces a dual-mode multi-view diffusion model and cross-mode post-training distillation that transfers quality from multi-view-oriented generation to efficient 3D-oriented generation.

## Method

FlashWorld pretrains a dual-mode model using a video diffusion prior, supporting both multi-view-oriented and 3D-oriented generation. It then distills across modes by matching the consistent 3D-oriented distribution to the higher-quality multi-view-oriented distribution, while using large-scale single-view images and text prompts for generalization.

## Experiments and Evidence

The abstract claims 10-100x faster generation than prior work, better rendering quality, maintained 3D consistency, fewer denoising steps, and extensive experiments. The PDF should be checked for scene complexity, evaluation metrics, human studies, reconstruction baselines, and out-of-distribution tests.

## Limits and Failure Modes

Likely limits include failure on complex geometry, unusual viewpoints, physics consistency, dynamic scenes, or prompts outside the video-diffusion prior. Speed/quality claims may depend on hardware and rendering pipeline choices.

## Deep Themes

- Generative modeling is moving toward structured world creation, not just 2D media.
- Distillation is used to transfer desirable properties between generation modes.
- Efficiency and quality are treated as coupled design targets.

## Subthemes

- 3D scene generation.
- Multi-view diffusion.
- 3D Gaussian representations.
- Distribution matching distillation.
- World models.

## Connections to Other Papers

Connects to diffusion/flow generative modeling, video generation, embodied/world-model research, and efficient inference. It should be compared with multimodal and robotics papers that need coherent 3D scene representations.

## Notes for Cross-Paper Synthesis

This is strong evidence for a deeper shift from generative images to generative environments. The model aims to produce a usable 3D representation quickly enough for downstream interactive or embodied applications.
