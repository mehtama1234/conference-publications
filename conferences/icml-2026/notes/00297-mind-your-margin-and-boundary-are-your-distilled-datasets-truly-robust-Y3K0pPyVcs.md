# Mind Your Margin and Boundary: Are Your Distilled Datasets Truly Robust?

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Y3K0pPyVcs
- Authors: Muquan Li; Yingyi Ma; Yihong Huang; Hang Gou; Ke Qin; Ming Li; Yuan-Fang Li; Tao He
- Primary area: deep_learning->robustness
- Keywords: Dataset Distillation;Robustness Optimization
- Source URL: https://openreview.net/forum?id=Y3K0pPyVcs
- PDF URL: https://openreview.net/pdf?id=Y3K0pPyVcs

## Abstract

Dataset distillation (DD) compresses a large training set into a small synthetic set for efficient training, but most DD methods optimize only clean accuracy and leave robustness uncontrolled. Recent robust DD methods improve robustness, yet they often suffer from a poor accuracy–robustness trade-off because they (i) treat all adversarially perturbed examples uniformly, despite robust risk being dominated by near-zero robust margins, and (ii) do not explicitly increase inter-class separation in the decision boundary where attacks concentrate. We present Contrastive Curriculum for Robust Dataset Distillation (C$^2$R), a framework that couples an attack-aware curriculum with a contrastive robustness objective. From a robust-margin perspective, we derive a \emph{perturbation score} that approximates each sample’s robust hinge, enabling a curriculum that prioritizes the smallest-margin adversaries that most directly drive robust error. In parallel, a class-balanced contrastive robustness loss enforces adversarial invariance while explicitly widening boundary separation across classes. Experiments on CIFAR-10/100, Tiny-ImageNet, and multiple ImageNet-1K subsets under six attacks show that C$^2$R achieves the best robust accuracy, outperforming prior robust DD by 2.8% on average.

## One-Sentence Claim

C2R improves robust dataset distillation by prioritizing small-margin adversaries and widening class boundaries with contrastive robustness objectives.

## Problem

Dataset distillation compresses large datasets into small synthetic sets for efficient training, but most methods optimize clean accuracy and leave robustness uncontrolled. Robust DD methods can improve adversarial robustness, yet often damage clean accuracy because they treat all adversarial examples uniformly and do not explicitly improve boundary separation.

The paper asks how distilled datasets can target the adversarial examples that dominate robust risk.

## Core Contribution

The paper introduces Contrastive Curriculum for Robust Dataset Distillation, or C2R. From a robust-margin perspective, it derives a perturbation score approximating each sample's robust hinge, then uses this to prioritize smallest-margin adversaries.

In parallel, a class-balanced contrastive robustness loss enforces adversarial invariance while widening inter-class boundary separation.

## Method

C2R couples two mechanisms:

- An attack-aware curriculum that focuses distillation on adversarial samples with near-zero robust margins.
- A contrastive robustness objective that encourages invariance under attack while separating classes near the decision boundary.

The method directly targets the robust-risk geometry rather than optimizing clean distilled examples alone.

## Experiments and Evidence

Evidence reported in the abstract:

- CIFAR-10, CIFAR-100, Tiny-ImageNet, and multiple ImageNet-1K subsets.
- Evaluation under six attacks.
- Best robust accuracy among compared robust DD methods.
- Average 2.8 percent robust-accuracy improvement over prior robust DD.
- Explicit analysis from robust-margin and boundary-separation perspectives.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: attack settings, distilled set sizes, clean-accuracy tradeoffs, and whether curriculum overhead is large.

## Limits and Failure Modes

- Adversarial robustness can be attack-specific if evaluations miss adaptive attacks.
- Prioritizing low-margin samples could reduce diversity in tiny distilled sets.
- Contrastive objectives depend on batch composition and class balance.
- Robustness of models trained on distilled data may not transfer across architectures.

## Deep Themes

**Robustness is concentrated near margins.** The method focuses on samples that most directly drive robust error.

**Distilled data should encode decision boundaries.** A small synthetic set must represent not only class prototypes but adversarial boundary geometry.

**Curriculum can target risk structure.** Attack-aware ordering makes robust distillation more selective.

## Subthemes

- Robust dataset distillation.
- Perturbation score as robust hinge proxy.
- Small-margin adversary curriculum.
- Contrastive boundary widening.
- Accuracy-robustness tradeoff.

## Connections to Other Papers

Connects to MTS Difficulty, HOBIT, and data-selection papers because example weighting is driven by training signal quality. It also links to Consistent Adversarial Attacks, S&D, and FeatJND through robust margin and feature-space robustness.

## Notes for Cross-Paper Synthesis

C2R reinforces that distilled or curated data must preserve the hard boundary cases, not only average examples, if it is to train robust models.
