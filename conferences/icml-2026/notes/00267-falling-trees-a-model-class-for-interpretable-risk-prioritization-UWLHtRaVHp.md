# Falling Trees: A Model Class for Interpretable Risk Prioritization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: UWLHtRaVHp
- Authors: Varun Babbar; Zachery Boner; Margo Seltzer; Cynthia Rudin
- Primary area: social_aspects->accountability_transparency_and_interpretability
- Keywords: Interpretable Machine Learning;Sparsity;Decision Tree Optimization
- Source URL: https://openreview.net/forum?id=UWLHtRaVHp
- PDF URL: https://openreview.net/pdf?id=UWLHtRaVHp

## Abstract

Many real-world decisions require prioritizing high-risk cases, such as clinicians prioritizing high-risk patients before lower-risk ones. Falling rule lists (FRLs), which are ordered if--then rules with monotonically decreasing risks, provide an interpretable framework for such tasks; however, their single-path structure yields a highly restricted model class. We introduce falling trees, a new family of interpretable models that enforces the same monotonic risk constraint while permitting tree-structured branching. We present GraviTree, a novel dynamic-programming-with-bounds algorithm for learning the Rashomon set of falling trees under depth and branching constraints. Our formulation can interpolate between rule lists and full decision trees, enabling user-desired model expressivity. In a new clinical dataset and in many public classification benchmarks, falling trees match or outperform FRLs and other interpretable baselines, often producing more sparse decisions for high-risk instances. Our results show that falling trees strike a practical balance between interpretability, expressiveness, and risk prioritization for high-stakes settings.

## One-Sentence Claim

Falling trees generalize falling rule lists into monotone-risk tree structures, improving high-risk prioritization while preserving interpretable decreasing-risk guarantees.

## Problem

High-stakes settings such as clinical triage often require prioritizing the highest-risk cases first. Falling rule lists are interpretable because they are ordered if-then rules with monotonically decreasing risk, but their single-path structure is restrictive.

The paper asks for a model class that keeps monotone risk prioritization interpretable while allowing richer branching decisions.

## Core Contribution

The paper introduces falling trees, interpretable decision trees constrained so risks decrease monotonically in a way analogous to falling rule lists. It also presents GraviTree, a dynamic-programming-with-bounds algorithm for learning the Rashomon set of falling trees under depth and branching constraints.

The model class interpolates between rule lists and full decision trees, letting users choose expressivity while retaining risk-prioritization structure.

## Method

Falling trees enforce monotonic risk constraints over tree-structured branches. GraviTree searches this constrained space using dynamic programming and bounds, returning not just one model but the Rashomon set: multiple high-performing falling trees satisfying the constraints.

This supports user choice among sparse, interpretable models that trade off branch complexity and predictive quality.

## Experiments and Evidence

Evidence reported in the abstract:

- A new clinical dataset for high-risk prioritization.
- Many public classification benchmarks.
- Falling trees match or outperform falling rule lists and other interpretable baselines.
- High-risk instances often receive sparser decisions.
- The method supports depth and branching constraints for user-desired expressivity.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: risk monotonicity formalism, optimization guarantees, clinical task details, and Rashomon-set enumeration cost.

## Limits and Failure Modes

- Monotone risk ordering may be too restrictive when risk factors interact non-monotonically.
- Interpretability depends on tree size; branching can grow complex if not constrained.
- Clinical deployment would need calibration, subgroup validation, and workflow evaluation.
- Dynamic-programming search may scale poorly with many features or split candidates.

## Deep Themes

**Interpretability can be a model-class constraint.** The paper encodes high-risk prioritization directly into the hypothesis space.

**Rashomon sets support human governance.** Multiple near-optimal models let users choose simpler or more clinically plausible rules without sacrificing much accuracy.

**High-stakes ML values sparse early decisions.** For triage, fast identification of high-risk cases matters as much as average classification performance.

## Subthemes

- Monotone decreasing risk constraints.
- Tree-structured generalization of rule lists.
- Dynamic programming with bounds.
- Rashomon-set learning.
- Sparse high-risk decision paths.

## Connections to Other Papers

Connects to Neural Concept Verifier, DISCO, and interpretability papers through constrained evidence channels. It also links to safety and robust decision papers because risk prioritization is an operational decision problem, not only a predictive task.

## Notes for Cross-Paper Synthesis

Falling Trees adds a high-stakes decision-design theme: sometimes the right model is not the most flexible one, but the one whose structure matches the decision order humans need to act on.
