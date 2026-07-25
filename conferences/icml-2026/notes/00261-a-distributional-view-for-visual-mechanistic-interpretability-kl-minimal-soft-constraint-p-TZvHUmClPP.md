# A Distributional View for Visual Mechanistic Interpretability: KL-Minimal Soft-Constraint Principle

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: TZvHUmClPP
- Authors: Guancheng Zhou; Yisi Luo; Zhengfu He; Zhenyu Jin; Xuyang Ge; Wentao Shu; Deyu Meng; Xipeng Qiu
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: mechanistic interpretability;information theory;computer vision;feature visualization
- Source URL: https://openreview.net/forum?id=TZvHUmClPP
- PDF URL: https://openreview.net/pdf?id=TZvHUmClPP

## Abstract

Most current paradigms in visual mechanistic interpretability (MI) remain confined to interpreting internal units of the vision model via heuristic methods (e.g., top-$K$ activation retrieval or optimization with regularization). In this work, we establish a theoretical distributional view for visual MI, which models the influence of a feature activation on the natural image distribution, thereby formulating a Kullback-Leibler (KL)-minimal optimization problem to model the MI task. Under this framework, statistical biases are identified within previous MI paradigms, which reveal that they may either be perceptually uninterpretable to humans (i.e., deviate from the natural image distribution), or mechanistically unfaithful to the vision models (i.e., unable to activate model features). To resolve the biases under the distributional view, we propose a model with a KL-minimal soft-constraint principle for visual MI that theoretically balances interpretability and faithfulness. We realize this principle via energy-guided diffusion posterior sampling.
Extensive experiments validate the theoretical soundness of the proposed distributional view and demonstrate the practical effectiveness of our paradigm on the DINOv3 vision model.
The code is available at https://github.com/SII-ZhouGC/EnergyDPS.

## One-Sentence Claim

Visual mechanistic interpretability can be framed as KL-minimal posterior sampling that balances human-natural image plausibility with faithful activation of model features.

## Problem

Visual mechanistic interpretability often relies on top-activation retrieval or feature-optimization visualizations. These methods can fail in opposite ways: retrieval may show natural images that are only weakly diagnostic of the internal feature, while unconstrained optimization may strongly activate the feature but produce images that humans cannot interpret.

The paper asks for a principled formulation that keeps feature visualizations on the natural-image distribution while preserving mechanistic faithfulness to the model's internal units.

## Core Contribution

The paper introduces a distributional view of visual MI: interpretability is modeled as the effect of a feature activation on the natural image distribution. This yields a KL-minimal optimization problem and exposes statistical biases in existing paradigms.

The proposed KL-minimal soft-constraint principle balances two objectives: stay close to natural images and satisfy feature-activation constraints. The implementation uses energy-guided diffusion posterior sampling.

## Method

The method treats feature visualization as posterior sampling under soft constraints. A diffusion model supplies a natural-image prior, while an energy term guides samples toward images that activate the target feature. KL minimization gives the conceptual objective: alter the image distribution as little as possible while satisfying mechanistic constraints.

This turns feature visualization from heuristic image generation into a constrained distributional inference problem.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical analysis identifying biases in top-K retrieval and regularized optimization paradigms.
- Energy-guided diffusion posterior sampling as a practical realization of the KL-minimal principle.
- Experiments on DINOv3 vision features.
- Empirical validation of both theoretical soundness and practical effectiveness.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact KL objective, energy definition, baselines, human interpretability metrics, and faithfulness measures.

## Limits and Failure Modes

- Diffusion priors may import their own dataset biases and may not match the model's training distribution.
- Faithful activation does not automatically imply causal sufficiency for downstream behavior.
- Human interpretability is hard to measure and may vary by feature granularity.
- Energy-guided sampling may be computationally expensive relative to retrieval.

## Deep Themes

**Interpretability is becoming distributional inference.** Instead of finding one maximally activating image, the paper models the feature-conditioned natural-image distribution.

**Faithfulness and legibility are competing constraints.** The contribution is not to optimize either alone, but to formalize the tradeoff.

**Generative models are tools for mechanistic analysis.** Diffusion posterior sampling becomes an instrument for probing vision-model internals.

## Subthemes

- KL-minimal soft constraints.
- Natural-image prior for feature visualization.
- Energy-guided diffusion posterior sampling.
- Bias diagnosis in retrieval and optimization visualizations.
- Vision MI beyond heuristic exemplars.

## Connections to Other Papers

Connects to Neuron-Basis Circuits, MDA, and AI Engram through interpretability as intervention or distributional probing. It also links to DISCO and robust-dependence papers because both formalize what relationships between internal representations and observed data should be preserved or suppressed.

## Notes for Cross-Paper Synthesis

This paper strengthens the theme that interpretability methods need explicit statistical objects. The object here is not a saliency map or exemplar set, but a feature-conditioned image distribution constrained by both naturalness and activation fidelity.
