# Discretized Density-Guided Source-Free Domain Adaptation for Regression

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: UQLGAjV1cf
- Authors: Gezheng Xu; Qi CHEN; QIUHAO Zeng; Charles Ling; Boyu Wang
- Primary area: general_machine_learning->transfer_multitask_and_metalearning
- Keywords: Domain adaptation;unsupervised learning;regression model
- Source URL: https://openreview.net/forum?id=UQLGAjV1cf
- PDF URL: https://openreview.net/pdf?id=UQLGAjV1cf

## Abstract

Source-Free Domain Adaptation (SFDA) enables model adaptation under distribution shifts without access to source data, providing a practical solution for privacy-sensitive applications and having shown substantial progress in classification. 
In contrast, regression involves ordered and continuous target variables, posing unique challenges for representation adaptation and pseudo-label refinement in the SFDA setting. 
To address this gap, we propose a novel algorithm for continuous label prediction in SFDA that leverages instance-dependent, discretized density–informed supervisory signals to refine pseudo-labels within an uncertainty-aware paradigm. 
By incorporating auxiliary discretized distribution learning, our method also promotes more compact and structured feature representations, mitigating the inherent difficulties of adapting regression models under distribution shift. 
We theoretically demonstrate that the resulting density structure is robust to potential perturbations, supporting reliable SFDA for regression. 
Extensive experiments across multiple benchmarks validate the effectiveness of the proposed approach.

## One-Sentence Claim

Source-free domain adaptation for regression can be made reliable by converting continuous targets into instance-dependent discretized density signals that guide uncertainty-aware pseudo-label refinement.

## Problem

Source-free domain adaptation adapts a trained source model to an unlabeled target domain without accessing source data, which is important for privacy-sensitive settings. Most SFDA progress has focused on classification, where pseudo-labels and class boundaries give natural adaptation structure.

Regression is harder because targets are continuous and ordered. Pseudo-label errors are not just wrong classes; they can drift in magnitude, density, and uncertainty under distribution shift.

## Core Contribution

The paper proposes a regression-specific SFDA algorithm that uses instance-dependent discretized density-informed supervision. Rather than treating pseudo-labels as single continuous point estimates, it adds auxiliary discretized distribution learning to structure the target representation and refine pseudo-labels under uncertainty.

The theoretical contribution is a robustness result showing the learned density structure can tolerate perturbations, supporting reliable regression adaptation.

## Method

The method discretizes continuous label space into density-informed supervisory signals. For each target instance, the algorithm uses uncertainty-aware pseudo-label refinement and auxiliary distribution learning to make features more compact and structured.

The key design choice is to borrow the robustness of classification-like density structure without discarding the ordered, continuous nature of regression labels.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical demonstration that the induced density structure is robust to perturbations.
- Extensive experiments across multiple regression adaptation benchmarks.
- Improved continuous-label prediction in source-free domain adaptation.
- More compact and structured feature representations through auxiliary discretized distribution learning.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: discretization scheme, uncertainty estimator, benchmark domains, source-model assumptions, and sensitivity to bin count.

## Limits and Failure Modes

- Discretization can lose fine-grained regression information if bins are poorly chosen.
- Pseudo-label refinement may reinforce wrong target predictions under severe domain shift.
- Density estimates can be unreliable in sparse target regions.
- The privacy motivation depends on whether source data absence is enough; source-model leakage is not discussed in the abstract.

## Deep Themes

**Continuous prediction needs structured adaptation targets.** The paper adds density supervision so regression has something like the stabilizing geometry of class distributions.

**Source-free adaptation is becoming uncertainty-aware.** Reliable adaptation depends on knowing how much to trust target pseudo-labels.

**Privacy constraints reshape learning protocols.** The method treats unavailable source data as a first-class constraint rather than an inconvenience.

## Subthemes

- Regression-specific SFDA.
- Discretized density learning over continuous labels.
- Instance-dependent pseudo-label refinement.
- Perturbation-robust density structure.
- Compact target-domain representations.

## Connections to Other Papers

Connects to DISCO, Bulk-Calibrated Credal Sets, and PSAHS through adaptation under shifted or biased distributions. It also links to TESS because both translate continuous predictive targets into structured intermediate variables that improve downstream learning.

## Notes for Cross-Paper Synthesis

This paper adds another example of "make the target structure explicit." Continuous labels are not handled as raw scalars; they are embedded into density-aware supervision so adaptation has a usable geometry.
