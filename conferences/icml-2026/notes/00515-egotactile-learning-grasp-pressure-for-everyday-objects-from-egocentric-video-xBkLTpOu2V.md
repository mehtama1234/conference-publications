# EgoTactile: Learning Grasp Pressure for Everyday Objects from Egocentric Video

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: xBkLTpOu2V
- Authors: Yuan Zeng; Yujia Shi; Tiao Tan; Xingting Li; Yaqi Qin; Zongqing Lu; Wenming Yang; Jing-Hao Xue; Qingmin Liao
- Primary area: deep_learning->generative_models_and_autoencoders
- Keywords: Egocentric vision;Visuo-haptic learning;Pressure estimation;Benchmark dataset;Diffusion models
- Source URL: https://openreview.net/forum?id=xBkLTpOu2V
- PDF URL: https://openreview.net/pdf?id=xBkLTpOu2V

## Abstract

Estimating full-hand grasp pressure from egocentric video is critical for immersive VR and robotic manipulation, yet dense tactile sensing often relies on intrusive hardware. 
Existing vision-based methods predominantly rely on planar surfaces or fingertip contacts, failing to generalize to complex 3D object interactions. 
Therefore, we introduce EgoTactile, a benchmark pairing egocentric video with full-hand pressure supervision for diverse everyday objects, incorporating a bare-hand transfer subset to enable generalization to natural scenarios. 
Leveraging this benchmark, we first establish EgoPressureFormer as a discriminative baseline. Beyond this, to explicitly address the uncertainty in partial observations, we propose EgoPressureDiff, a conditional diffusion framework that adapts a large-scale pre-trained video diffusion backbone. By combining rich world knowledge priors with a Physically-Informed Feature Rectification layer to inject semantic constraints, our approach effectively hallucinates plausible contact patterns and resolves visual-physical ambiguities. 
Extensive experiments demonstrate that our method achieves superior performance on the benchmark and robust transferability to in-the-wild scenarios. Our project page is at https://egotactile.github.io/.

## One-Sentence Claim

EgoTactile learns full-hand grasp pressure from egocentric video by pairing a new visuo-haptic benchmark with a diffusion model that hallucinates plausible contact patterns under physical constraints.

## Problem

Dense grasp-pressure estimation is valuable for VR and robotic manipulation, but direct tactile sensing can require intrusive hardware. Existing vision-based methods often focus on planar surfaces or fingertip contacts and do not generalize to full-hand 3D object interactions.

The core problem is inferring hidden physical contact and pressure from partial egocentric visual observations.

## Core Contribution

The paper introduces EgoTactile, a benchmark pairing egocentric video with full-hand pressure supervision across diverse everyday objects, including a bare-hand transfer subset for natural settings.

It also proposes EgoPressureFormer as a discriminative baseline and EgoPressureDiff, a conditional diffusion framework adapted from a large pretrained video diffusion backbone.

## Method

EgoPressureDiff conditions on egocentric video and uses diffusion to model uncertainty over plausible full-hand pressure patterns. It leverages pretrained video diffusion priors and adds a Physically-Informed Feature Rectification layer to inject semantic and physical constraints.

The generative formulation is designed to resolve ambiguities where the visible hand/object interaction only partially reveals contact forces.

## Experiments and Evidence

The abstract reports superior benchmark performance and robust transferability to in-the-wild scenarios.

It also reports a dataset contribution with diverse everyday objects and a bare-hand transfer subset, which is important because tactile estimation often fails when sensing setups differ from natural use.

## Limits and Failure Modes

Pressure inferred from video is inherently ambiguous; visually similar grasps can have different force distributions. The diffusion prior may hallucinate plausible but incorrect contacts if object material, hidden fingers, or grip intent are not visible.

Because this note is abstract-only, details still need checking: sensor setup, pressure map representation, object categories, train/test splits, transfer protocol, physical constraints in the rectification layer, and real-robot or VR evaluation.

## Deep Themes

- Visuo-haptic inference: physical contact can be estimated from egocentric visual traces.
- Generative uncertainty for hidden physical state: diffusion handles multiple plausible pressure fields.
- Embodied data benchmarks: progress depends on paired sensory supervision, not only model design.
- Pretrained video priors for physical reasoning: large-scale visual dynamics can help infer contact patterns.

## Subthemes

- Full-hand pressure estimation.
- Bare-hand transfer.
- Physically informed feature rectification.
- Everyday-object grasp benchmarks.

## Connections to Other Papers

This connects to Beyond Language Modeling, EcoVLA, and world-modeling papers through embodied multimodal pretraining and physical inference.

It also relates to CoEvol-NO and scientific/physical generation papers because it uses generative modeling to infer hidden physical states from partial observations.

## Notes for Cross-Paper Synthesis

This paper adds a tactile embodiment thread: multimodal models are increasingly asked to infer latent physical quantities, not just recognize visible objects or generate images.
