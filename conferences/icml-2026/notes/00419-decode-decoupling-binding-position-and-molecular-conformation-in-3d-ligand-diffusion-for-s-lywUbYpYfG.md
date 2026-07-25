# DeCoDe: Decoupling Binding Position and Molecular Conformation in 3D Ligand Diffusion for Structure-Based Drug Design

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lywUbYpYfG
- Authors: Julong Yang; Wen Huang; Junhui Chen; Jian Peng
- Primary area: applications->health_medicine
- Keywords: Diffusion Models;Structure-Based Drug Design;Molecule Generation
- Source URL: https://openreview.net/forum?id=lywUbYpYfG
- PDF URL: https://openreview.net/pdf?id=lywUbYpYfG

## Abstract

Recent advances in diffusion models show promise for Structure-Based Drug Design (SBDD), which aims to generate 3D ligand molecules that bind tightly to specific protein targets. 
This involves jointly optimizing the ligand's 3D conformation and its binding position within the protein pocket. 
However, existing diffusion-based SBDD methods diffuse conformation and binding position synchronously within a high-dimensional joint space, leading to inefficient exploration and suboptimal generation quality in both aspects.
To address this, we propose **DeCoDe**, a novel diffusion framework that **decouples** the diffusion processes of the binding position and molecular conformation. 
Our key insight is to prioritize the perturbation of the ligand's internal conformation in the early stages of the forward (noising) process, while accelerating the perturbation of its global binding position later.
This design guides the reverse (denoising) process to *first coarsely position* the ligand within the pocket before *refining its detailed structure*, mimicking a more efficient, step-wise generation strategy.
Extensive experiments on the CrossDocked2020 benchmark show that DeCoDe achieves significantly higher structural fidelity (with an average improvement of 18%), while maintaining competitive binding affinity and overall molecular properties compared to state-of-the-art baselines.

## One-Sentence Claim

DeCoDe improves 3D ligand generation by decoupling diffusion schedules for internal molecular conformation and global binding position, enabling coarse-to-fine pocket placement and refinement.

## Problem

Structure-based drug design requires generating ligands with both good 3D conformation and good binding position in a protein pocket. Existing diffusion methods often diffuse these factors synchronously in one high-dimensional joint space, making exploration inefficient and hurting generation quality.

The paper asks whether binding placement and molecular conformation should follow different noising/denoising schedules.

## Core Contribution

DeCoDe decouples diffusion of binding position and molecular conformation. It perturbs internal conformation more in early forward stages and accelerates perturbation of global binding position later.

The reverse process is guided to first coarsely position the ligand in the pocket and then refine detailed molecular structure.

## Method

The method designs separate diffusion dynamics for ligand-internal degrees of freedom and global pose within the pocket. This staging imposes a coarse-to-fine generation strategy rather than asking the model to solve all geometric factors simultaneously.

The resulting denoising process better matches the structure of SBDD: find the pocket placement, then refine conformation.

## Experiments and Evidence

Evidence reported in the abstract:

- CrossDocked2020 benchmark.
- Average 18% improvement in structural fidelity.
- Competitive binding affinity.
- Competitive overall molecular properties.
- Comparison against state-of-the-art baselines.
- Decoupled binding-position and conformation diffusion schedules.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: fidelity metric, affinity evaluation, validity/diversity metrics, and schedule ablations.

## Limits and Failure Modes

- Coarse-to-fine assumptions may fail when conformation and binding pose are tightly coupled.
- CrossDocked2020 evaluation may not capture wet-lab success.
- Binding-affinity estimates can be noisy or model-dependent.
- Decoupled schedules add hyperparameters and design complexity.

## Deep Themes

**Generation factors should be scheduled separately.** Pose and conformation are different control variables.

**Coarse-to-fine diffusion can improve physical design.** The model first localizes globally, then refines details.

**Domain structure shapes generative dynamics.** Drug design benefits from matching diffusion process to molecular geometry.

## Subthemes

- Structure-based drug design.
- 3D ligand diffusion.
- Binding-position/conformation decoupling.
- Coarse-to-fine denoising.
- CrossDocked2020 molecular generation.

## Connections to Other Papers

Connects to MOG, KPE/KTS, Tilt Matching, Weak Diffusion Priors, and protein-structure papers. It adds a molecular-design instance of trajectory scheduling in diffusion models.

## Notes for Cross-Paper Synthesis

DeCoDe reinforces a generative-control theme: effective diffusion models often need different coordinates or factors to evolve on different schedules.
