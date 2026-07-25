# DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: TYjTWxDOOC
- Authors: Emre Kavak; Tom Nuno Wolf; Christian Wachinger
- Primary area: general_machine_learning->causality
- Keywords: Shortcut Learning;Bias Mitigation;Causality
- Source URL: https://openreview.net/forum?id=TYjTWxDOOC
- PDF URL: https://openreview.net/pdf?id=TYjTWxDOOC

## Abstract

Dataset bias often leads deep learning models to exploit spurious correlations instead of task-relevant signals. We introduce the Standard Anti-Causal Model (SAM), a unifying causal framework that characterizes bias mechanisms and yields a conditional independence criterion for causal stability. Building on this theory, we propose DISCO$_m$ and sDISCO, efficient and scalable estimators of conditional distance correlation that enable independence regularization in gradient-based models. Across six diverse datasets, our methods consistently outperform or are competitive in existing observed bias mitigation approaches, while requiring fewer hyperparameters and scaling seamlessly to multi-bias scenarios. This work bridges causal theory and practical deep learning, providing both a principled foundation and effective tools for robust prediction. Source Code: https://github.com/yakamoz5/DISCO.

## One-Sentence Claim

DISCO uses a causal anti-causal bias model and scalable conditional distance-correlation regularizers to reduce shortcut learning across observed multi-bias settings.

## Problem

Deep models often exploit spurious correlations between labels, protected or nuisance attributes, and dataset artifacts. Existing bias-mitigation methods can be fragmented, hyperparameter-heavy, or poorly suited to multiple simultaneous biases.

The paper frames shortcut learning through a causal lens and asks for a practical independence criterion that can be optimized inside modern gradient-based models.

## Core Contribution

The paper introduces the Standard Anti-Causal Model, a causal framework that characterizes bias mechanisms and derives a conditional independence criterion for causal stability. It then proposes DISCO_m and sDISCO, efficient estimators of conditional distance correlation for independence regularization.

The claimed practical contribution is a bias-mitigation method that is principled, scalable, competitive across diverse datasets, and easier to tune in multi-bias settings.

## Method

The causal side defines when a predictor should be independent of bias variables conditional on task-relevant information. The learning side estimates conditional distance correlation and adds it as a differentiable regularization term during model training.

DISCO_m and sDISCO appear to target efficiency and scalability, making conditional independence regularization feasible in deep networks rather than only in small-sample statistical settings.

## Experiments and Evidence

Evidence reported in the abstract:

- Experiments across six diverse datasets.
- Consistent outperformance or competitiveness against observed-bias mitigation methods.
- Fewer hyperparameters than competing approaches.
- Seamless scaling to multi-bias scenarios.
- Source code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: dataset names, bias variables, baselines, fairness/robustness metrics, estimator complexity, and whether unobserved biases are handled.

## Limits and Failure Modes

- The method appears focused on observed bias variables; hidden or weakly measured confounders may remain difficult.
- Conditional independence regularization can remove useful signal if the conditioning set is misspecified.
- Distance-correlation estimates may be sensitive to batch size, kernels/distances, or high-dimensional representations.
- Causal stability assumptions need scrutiny for each dataset.

## Deep Themes

**Causal criteria are being packaged into trainable regularizers.** DISCO turns a conditional independence claim into a scalable deep-learning objective.

**Bias mitigation is shifting from one-bias fixes to multi-bias systems.** The method explicitly targets scenarios with several observed shortcut variables.

**Robust prediction depends on conditional, not marginal, independence.** The causal framing distinguishes unwanted shortcut dependence from legitimate task-relevant correlations.

## Subthemes

- Standard Anti-Causal Model as a unifying bias framework.
- Conditional distance correlation for differentiable independence penalties.
- Multi-bias mitigation with fewer hyperparameters.
- Causal stability as robustness target.

## Connections to Other Papers

Connects to robust decision and calibration work such as Bulk-Calibrated Credal Sets, Consistent Adversarial Attacks, DOUBT, and safety/robustness papers that separate true task signal from spurious, harmful, or unreliable correlations. It also links to causal discovery papers in the corpus because the intervention target is a conditional independence relation.

## Notes for Cross-Paper Synthesis

DISCO contributes to a broader pattern where robustness methods become conditional dependence control systems: decide which dependencies should exist, estimate them tractably, then regularize the model so it cannot rely on unstable shortcuts.
