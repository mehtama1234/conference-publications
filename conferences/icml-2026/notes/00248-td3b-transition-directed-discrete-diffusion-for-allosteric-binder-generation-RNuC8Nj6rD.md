# TD3B: Transition-Directed Discrete Diffusion for Allosteric Binder Generation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: RNuC8Nj6rD
- Authors: Hanqun Cao; Aastha Pal; Sophia Tang; Yinuo Zhang; Jingjie Zhang; Pheng-Ann Heng; Pranam Chatterjee
- Primary area: applications->health_medicine
- Keywords: Generative modeling;discrete diffusion;molecular design;protein-ligand interactions;functional biomolecular design
- Source URL: https://openreview.net/forum?id=RNuC8Nj6rD
- PDF URL: https://openreview.net/pdf?id=RNuC8Nj6rD

## Abstract

Protein function is often controlled by ligands that bias the direction of state transitions, such as agonists and antagonists, rather than stabilizing a single conformation. This is especially important for clinically relevant G protein-coupled receptors (GPCRs), where therapeutic efficacy depends on functional directionality. Structure-based design methods optimize binding to static conformations and cannot represent non-reversible, directional effects or systematically distinguish agonist from antagonist behavior. To address this gap, we introduce **T**ransition-**D**irected **D**iscrete **D**iffusion for allosteric**B**inder design (**TD3B**), a sequence-based generative framework that designs binders with specified agonist or antagonist behavior via a directional transition control objective. TD3B combines a target-aware Direction Oracle, a soft binding-affinity gate, and amortized fine-tuning of a pre-trained discrete diffusion model, enabling targeted agonist and antagonist generation decoupled from binding affinity and unattainable by equilibrium-based or inference-only guidance baselines. The code and checkpoints are available at https://huggingface.co/ChatterjeeLab/TD3B.

## One-Sentence Claim

TD3B designs allosteric binders with specified agonist or antagonist behavior by optimizing directional transition control rather than static binding affinity alone.

## Problem

Protein function can depend on ligands biasing state transitions, especially in GPCRs, but structure-based design methods optimize static conformations and cannot represent non-reversible directional effects.

## Core Contribution

The paper introduces a sequence-based discrete diffusion framework with a target-aware Direction Oracle, soft affinity gate, and amortized fine-tuning for transition-directed binder generation.

## Method

TD3B fine-tunes a pretrained discrete diffusion model to generate binders that satisfy a directional transition objective, decoupling agonist/antagonist behavior from simple binding affinity through oracle guidance and affinity gating.

## Experiments and Evidence

The abstract claims targeted agonist and antagonist generation unattainable by equilibrium-based or inference-only guidance baselines, but does not list detailed metrics in the visible abstract.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: GPCR targets, Direction Oracle validation, wet-lab or simulation evidence, affinity/activity tradeoffs, off-target effects, and discrete diffusion model pretraining data.

## Deep Themes

- Molecular design should target functional transitions, not only static structures.
- Directional biological effects require objectives beyond equilibrium affinity.
- Diffusion fine-tuning can encode activity semantics such as agonism or antagonism.

## Subthemes

- Allosteric binder generation.
- GPCRs.
- Discrete diffusion.
- Agonist/antagonist behavior.
- Direction Oracle.
- Protein-ligand interactions.

## Connections to Other Papers

Connects to Chamaileon and sub-second molecular docking through functional biomolecular design and to diffusion guidance papers through targeted generative control.

## Notes for Cross-Paper Synthesis

TD3B adds a functional-directionality theme for scientific generation: a generated molecule is useful only if it pushes the biological system in the desired direction.
