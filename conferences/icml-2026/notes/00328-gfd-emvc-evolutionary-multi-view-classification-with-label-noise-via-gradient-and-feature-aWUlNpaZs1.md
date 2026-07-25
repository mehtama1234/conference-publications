# GFD-EMVC: Evolutionary Multi-View Classification with Label Noise via Gradient and Feature Dual-Perception

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aWUlNpaZs1
- Authors: Shuai Li; Xinyan Liang; Yuhua Qian; Li Lv
- Primary area: general_machine_learning
- Keywords: Multi-view Learning;Fitness Evaluation Bias;Multi-view Classification
- Source URL: https://openreview.net/forum?id=aWUlNpaZs1
- PDF URL: https://openreview.net/pdf?id=aWUlNpaZs1

## Abstract

This paper studies a fundamental yet often overlooked premise in evolutionary multi-view classification (EMVC): the impact of label noise on EMVC, such as distorting fitness landscapes shaped by individual fitness values (e.g., test accuracy).
Traditional EMVC assumes training labels are noise-free, yet this often fails in practice.
As a result, label noise introduces harmful supervision during the training phase, resulting in distorted fitness landscapes and the emergence of fitness evaluation bias (FEB). This bias misguides the evolutionary trajectory, causing the search process to stagnate in local optima. 
Given that label noise largely stems from the mislabeling of samples near their decision boundaries by human annotators, we thus compared the decision boundaries of human annotators and models, and found discrepancies between the two. Based on this observation, we propose a simple yet effective ``detect-then-calibrate" data purification framework that leverages outlier analysis in the gradient space (i.e., treating outliers as noisy samples) and prototype calibration in the feature space (i.e., utilizing feature prototypes of noise-free samples to correct the labels of noisy samples).
Experimental results demonstrate that this strategy can effectively purify the data and alleviate FEB; moreover, it can improve the performance of various multi-view learning paradigms in label noise scenarios.
(https://github.com/LiShuailzn/ICML-2026-GFD-EMVC)

## One-Sentence Claim

GFD-EMVC mitigates label-noise-driven fitness evaluation bias in evolutionary multi-view classification by detecting noisy samples in gradient space and calibrating labels with feature prototypes.

## Problem

Evolutionary multi-view classification often assumes clean training labels. In practice, label noise distorts supervision and therefore the fitness landscape used by evolutionary search, creating fitness evaluation bias that can misguide trajectories and trap search in local optima.

The paper targets label noise near decision boundaries, where human annotators and model boundaries disagree.

## Core Contribution

The paper identifies label noise as a source of distorted evolutionary fitness landscapes in EMVC and proposes Gradient and Feature Dual-Perception. The framework follows a detect-then-calibrate strategy:

- Detect noisy samples as outliers in gradient space.
- Calibrate their labels using feature prototypes of noise-free samples.

The method purifies data, alleviates fitness evaluation bias, and improves several multi-view learning paradigms under label noise.

## Method

GFD-EMVC first compares human/model boundary behavior to motivate boundary-driven mislabeling. It then uses gradient-space outlier analysis to flag examples whose learning signal is inconsistent with the rest of the data.

After detection, feature-space prototypes from reliable samples supply corrected labels, producing a cleaner fitness landscape for evolutionary search.

## Experiments and Evidence

Evidence reported in the abstract:

- Demonstration that label noise creates fitness evaluation bias in EMVC.
- Boundary discrepancy analysis between human annotators and models.
- Gradient-space outlier detection for noisy samples.
- Feature-prototype label calibration.
- Improved performance across various multi-view learning paradigms under label noise.
- Code release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, label-noise models, evolutionary algorithms, prototype construction, and comparison baselines.

## Limits and Failure Modes

- Gradient outliers are not always mislabeled; they can be rare but valid hard cases.
- Prototype calibration can reinforce majority-class or clean-subset biases.
- Human/model boundary discrepancy may vary across tasks.
- Evolutionary search cost and purification overhead need inspection.

## Deep Themes

**Data noise distorts optimization landscapes.** Label errors change the fitness function, not just final accuracy.

**Gradients reveal suspicious supervision.** Noisy samples are detected by how their training signals deviate.

**Prototype calibration repairs decision-boundary labels.** Feature geometry becomes a label-correction tool.

## Subthemes

- Evolutionary multi-view classification.
- Fitness evaluation bias.
- Gradient-space noisy-label detection.
- Feature-prototype calibration.
- Boundary-driven label noise.

## Connections to Other Papers

Connects to C2R, MTS Difficulty, HOBIT, DISCO, and robust data-curation papers. It also links to IDCD and HAMC through multi-view representation reliability.

## Notes for Cross-Paper Synthesis

GFD-EMVC reinforces that data quality problems often act through optimization signals: corrupted labels distort the landscape that the learner or search process follows.
