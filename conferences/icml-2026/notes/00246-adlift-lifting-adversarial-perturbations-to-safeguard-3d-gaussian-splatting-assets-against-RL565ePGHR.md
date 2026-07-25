# AdLift: Lifting Adversarial Perturbations to Safeguard 3D Gaussian Splatting Assets Against Instruction-Driven Editing

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: RL565ePGHR
- Authors: Ziming Hong; Tianyu Huang; Runnan Chen; Shanshan Ye; Mingming Gong; Bo Han; Tongliang Liu
- Primary area: social_aspects
- Keywords: 3D Gaussian Splatting;Instruction-driven Image/3DGS Editing;Editing Guard;Active Copyright Protection
- Source URL: https://openreview.net/forum?id=RL565ePGHR
- PDF URL: https://openreview.net/pdf?id=RL565ePGHR

## Abstract

Recent studies have extended instruction-driven 2D editing pipelines to 3D Gaussian Splatting (3DGS), enabling faithful 3DGS asset manipulation for advanced content creation. However, it also exposes 3DGS assets to serious risks of unauthorized editing and malicious tampering. Although adversarial perturbations against editing models have proven effective for protecting 2D images, applying them to 3DGS encounters two major challenges: *view-generalizable protection* and *balancing invisibility with protection capability*. In this work, we propose AdLift, a novel editing safeguard for 3DGS that prevents instruction-driven editing across arbitrary views and dimensions by lifting strictly bounded 2D adversarial perturbations into 3D Gaussian-represented safeguard. To ensure both *protective effectiveness* and *invisibility*, these safeguard Gaussians are progressively optimized across training views using a tailored Lifted PGD, which first conducts *gradient truncation* during back-propagation from the editing model to the rendered image and applies projected gradient updates to strictly bound image-level perturbations. Then, the resulting perturbation is backpropagated to the safeguard Gaussian parameters via *image-to-Gaussian fitting*. We alternate these two steps, yielding effective and imperceptible protection that generalizes across both training and novel views. Empirically, qualitative and quantitative results demonstrate that the proposed AdLift effectively protects against state-of-the-art instruction-driven 2D and 3DGS editing.

## One-Sentence Claim

AdLift protects 3D Gaussian Splatting assets from unauthorized instruction-driven editing by lifting bounded 2D adversarial perturbations into view-generalizable safeguard Gaussians.

## Problem

Instruction-driven 2D and 3DGS editing enables powerful content manipulation but exposes 3D assets to unauthorized edits, while 2D adversarial protections do not directly solve view-generalizable 3D protection or invisibility tradeoffs.

## Core Contribution

The paper proposes a 3DGS editing safeguard that alternates image-level bounded adversarial optimization with image-to-Gaussian fitting, producing imperceptible protection across training and novel views.

## Method

AdLift uses Lifted PGD: gradient truncation backpropagates editing-model gradients to rendered images with strict image-level perturbation bounds, then image-to-Gaussian fitting transfers the perturbation into safeguard Gaussian parameters. The two steps are alternated over training views.

## Experiments and Evidence

The abstract reports qualitative and quantitative evidence that AdLift protects against state-of-the-art instruction-driven 2D and 3DGS editing across arbitrary views and dimensions.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: editing models tested, 3D scenes, perceptual invisibility metrics, novel-view robustness, adaptive attacker assumptions, and whether safeguards survive asset compression or relighting.

## Deep Themes

- Adversarial protection must become view-consistent for 3D assets.
- Copyright and tamper resistance are emerging concerns for editable neural scene representations.
- 2D safeguards can be lifted into 3D parameter space through differentiable rendering.

## Subthemes

- 3D Gaussian Splatting.
- Instruction-driven editing.
- Active copyright protection.
- Adversarial perturbations.
- Projected gradient descent.
- View-generalizable safeguards.

## Connections to Other Papers

Connects to TideGS, GEM, DGS-Net, and generative safety papers through protection and verification of visual/3D assets.

## Notes for Cross-Paper Synthesis

AdLift adds a 3D asset-governance theme: as neural scene formats become editable, protection must live in the representation itself rather than only in rendered images.
