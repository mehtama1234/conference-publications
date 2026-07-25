# Towards Efficient LLMs Annealing with Principled Sample Selection

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 2UH01A9Za0
- Authors: Yuanjian Xu; Jianing Hao; Wanbo Zhang; Zhong Li; Guang Zhang
- Primary area: deep_learning->large_language_models
- Keywords: LLM training;Annealing phase;Data selection
- Source URL: https://openreview.net/forum?id=2UH01A9Za0
- PDF URL: https://openreview.net/pdf?id=2UH01A9Za0

## Abstract

The annealing phase is a pivotal convergence stage in LLM pre-training that ultimately determines final model quality. However, effectively selecting training data during this phase remains a key challenge. Current strategies rely on empirical heuristics, such as domain filtering or context extension, which lack a principled grounding in optimization theory. In this work, we characterize the annealing phase through the lens of the loss landscape's spectral geometry. We argue that optimal convergence requires gradient updates to satisfy heterogeneous constraints across different eigen-directions. Building on this insight, we formulate data selection as a problem of satisfying these directional constraints. To this end,  we propose **DiReCT** (**Di**rectionally-**Re**strained **C**onstrained **T**raining), a novel framework that reformulates sample selection in the annealing stage as a constrained optimization problem. By imposing explicit directional constraints on per-sample gradients based on the spectral properties of the Hessian, **DiReCT** identifies samples that align with the optimal curvature-aware descent path. Extensive experiments across various model scales demonstrate that **DiReCT** consistently achieves state-of-the-art performance. For future research, code is available at https://github.com/xuyj233/Direct.

## One-Sentence Claim

DiReCT makes LLM annealing data selection curvature-aware by choosing samples whose gradients satisfy directional constraints from the Hessian spectrum.

## Problem

The annealing stage strongly affects final LLM quality, but current data-selection heuristics such as domain filtering or context extension lack optimization-theoretic grounding.

## Core Contribution

The paper characterizes annealing through spectral geometry of the loss landscape and proposes Directionally-Restrained Constrained Training as a constrained optimization framework for sample selection.

## Method

DiReCT estimates directional constraints from Hessian spectral properties and selects samples whose per-sample gradients align with the desired curvature-aware descent path.

## Experiments and Evidence

The abstract reports state-of-the-art performance across model scales.

## Full-Text Upgrade

The full text makes the optimization story precise: DiReCT treats the annealing loss landscape as anisotropic. Steep eigendirections are high-risk because noisy gradients can destabilize convergence, while flat eigendirections are useful because they allow progress that better preserves generalization. Sample selection is therefore posed as choosing examples whose per-sample gradients project strongly into the flat validation-Hessian subspace while keeping gradient energy in stiff directions below a constraint.

Implementation relies on a validation Hessian approximation rather than full eigendecomposition. The paper sketches randomized Hessian sketching, approximate eigenvectors/eigenvalues, projection of each training-sample gradient onto those directions, and a constrained selection problem with a cardinality constraint. Reported experiments include GPT-2-Medium 355M and Llama-1.1B annealing runs, averaged over five random seeds, where DiReCT achieves the strongest aggregate score against uniform sampling and other data-selection baselines.

## Limits and Failure Modes

Limits to watch: the Hessian and per-sample-gradient machinery is still expensive relative to simple heuristics; results are at research model scales rather than frontier pretraining scale; and curvature-aligned selection does not by itself guarantee topical diversity, safety coverage, or robustness to validation-set misspecification.

## Deep Themes

- Data selection is becoming optimization geometry.
- Late-stage pretraining has distinct rules from bulk pretraining.
- Efficient training comes from choosing the right samples, not only more compute.

## Subthemes

- LLM annealing.
- Spectral loss geometry.
- Per-sample gradients.
- Constrained sample selection.
- Curvature-aware training.

## Connections to Other Papers

Connects to Difficult Examples, Common Corpus, and contrastive data selection. Together they show data as an active control surface.

## Notes for Cross-Paper Synthesis

DiReCT reinforces the idea that dataset construction and sample choice are no longer peripheral; they encode optimization strategy.
