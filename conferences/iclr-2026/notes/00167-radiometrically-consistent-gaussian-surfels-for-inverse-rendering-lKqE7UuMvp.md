# Radiometrically Consistent Gaussian Surfels for Inverse Rendering

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: lKqE7UuMvp
- Authors: Kyu Beom Han; Jaeyoon Kim; Woo Jae Kim; Jinhwan Seo; Sung-eui Yoon
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Radiometric Consistency;Indirect Illumination;Gaussian Splatting;Inverse Rendering
- Source URL: https://openreview.net/forum?id=lKqE7UuMvp
- PDF URL: https://openreview.net/pdf?id=lKqE7UuMvp

## Abstract

Inverse rendering with Gaussian Splatting has advanced rapidly, but accurately disentangling material properties from complex global illumination effects, particularly indirect illumination, remains a major challenge. Existing methods often query indirect radiance from Gaussian primitives pre-trained for novel-view synthesis. However, these pre-trained Gaussian primitives are supervised only towards limited training viewpoints, thus lack supervision for modeling indirect radiances from unobserved views. To address this issue, we introduce radiometric consistency, a novel physically-based constraint that provides supervision towards unobserved views by minimizing the residual between each Gaussian primitive’s learned radiance and its physically-based rendered counterpart. Minimizing the residual for unobserved views establishes a self-correcting feedback loop that provides supervision from both physically-based rendering and novel-view synthesis, enabling accurate modeling of inter-reflection.
We then propose Radiometrically Consistent Gaussian Surfels (RadioGS), an inverse rendering framework built upon our principle by efficiently integrating radiometric consistency by utilizing  Gaussian surfels and 2D Gaussian ray tracing. We further propose a finetuning-based relighting strategy that adapts Gaussian surfel radiances to new illuminations within minutes, achieving low rendering cost ($<$10ms). Extensive experiments on existing inverse rendering benchmarks show that RadioGS outperforms existing Gaussian-based methods in inverse rendering, while retaining the computational efficiency.

## One-Sentence Claim

RadioGS improves Gaussian-splatting inverse rendering by enforcing radiometric consistency between learned primitive radiance and physically based rendered radiance, including for unobserved views.

## Problem

Gaussian-splatting inverse rendering struggles to disentangle material properties from global illumination, especially indirect illumination. Gaussian primitives trained for novel-view synthesis are supervised only from limited views and may not model indirect radiance correctly from unobserved directions.

## Core Contribution

The paper introduces radiometric consistency as a physically based self-supervision constraint and builds Radiometrically Consistent Gaussian Surfels around it, using Gaussian surfels, 2D Gaussian ray tracing, and a fast relighting strategy.

## Method

RadioGS minimizes the residual between each Gaussian primitive's learned radiance and a physically based rendered counterpart for unobserved views. This creates a self-correcting loop between physics-based rendering and novel-view synthesis. The framework uses Gaussian surfels and 2D Gaussian ray tracing, then finetunes surfel radiances for new illumination conditions.

## Experiments and Evidence

Experiments on inverse-rendering benchmarks reportedly outperform prior Gaussian-based methods while retaining computational efficiency. The finetuning-based relighting strategy adapts to new illuminations within minutes and renders at less than 10ms.

## Limits and Failure Modes

Physical consistency depends on the rendering model, lighting assumptions, material parameterization, and quality of geometry. Highly non-Lambertian materials, participating media, sparse views, or dynamic scenes may break the constraint. Full-text review should check benchmark scenes, indirect-light modeling, surfel representation, relighting evaluation, and runtime details.

## Deep Themes

- Physics-based constraints for neural rendering.
- Self-supervision from unobserved views.
- Radiance-material disentanglement.
- Efficient inverse rendering with Gaussian primitives.

## Subthemes

- Radiometric consistency.
- Indirect illumination modeling.
- Gaussian surfels.
- 2D Gaussian ray tracing.
- Fast relighting.

## Connections to Other Papers

Connects to RoSE, FlashWorld, VIST3A, and Vid-LLM through geometry-aware visual generation/reconstruction, and to quotient-space/physics-inspired generative papers through embedding physical constraints in learned representations.

## Notes for Cross-Paper Synthesis

RadioGS is another example of learned visual representations being corrected by physical structure. The key theme is that generative rendering improves when unobserved states are constrained by a model of how light should behave.
