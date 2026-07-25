# Fair Classification with Efficient and Post-hoc Controllable Fairness-Accuracy Trade-off

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: lyN8OMVyMt
- Authors: Maaya Sakata; Kazuto Fukuchi
- Primary area: social_aspects->fairness
- Keywords: Fair Machine Learning;Fairness-Accuracy Trade-off;Fair Bayes-optimal Classifier
- Source URL: https://openreview.net/forum?id=lyN8OMVyMt
- PDF URL: https://openreview.net/pdf?id=lyN8OMVyMt

## Abstract

Post-hoc controllability of fair machine learning models, the ability to control the trade-off between fairness and accuracy after training, is valuable for practical deployment. Existing post-processing methods provide such post-hoc controllability but often suffer from significant accuracy degradation, whereas in-processing methods achieve efficient trade-offs but require computationally expensive retraining for each change in trade-off ratio. To achieve both post-hoc controllability and efficient trade-offs, we propose a novel fair classification algorithm that learns effective feature representations to improve the trade-off efficiency of post-processing fair classifiers, by a gradient-based optimization approach. Experimental results on real-world datasets demonstrate that our method achieves trade-off efficiency comparable to, or even surpassing, in-processing methods, without requiring any retraining.

## One-Sentence Claim

Learning representations for post-processing fair classifiers can provide post-hoc fairness-accuracy control with trade-off efficiency comparable to in-processing methods.

## Problem

Deployment often requires adjusting the fairness-accuracy tradeoff after training as policy or context changes. Post-processing methods allow post-hoc control but can degrade accuracy, while in-processing methods can be efficient but require retraining for each tradeoff ratio.

The paper asks how to get both post-hoc controllability and efficient fairness-accuracy tradeoffs.

## Core Contribution

The paper proposes a fair classification algorithm that learns feature representations specifically to improve the trade-off efficiency of post-processing fair classifiers. The resulting model can adjust fairness/accuracy after training without retraining.

Experiments show trade-off efficiency comparable to, or better than, in-processing methods on real-world datasets.

## Method

The method uses gradient-based optimization to learn representations that make downstream post-processing fairness control more efficient. Instead of treating representation learning and post-processing separately, it trains features so the post-hoc classifier family has a better fairness-accuracy frontier.

At deployment, users can choose a tradeoff point without re-running full model training.

## Experiments and Evidence

Evidence reported in the abstract:

- Post-hoc control of fairness-accuracy tradeoff.
- Gradient-based representation learning for post-processing fair classifiers.
- Real-world dataset experiments.
- Trade-off efficiency comparable to or surpassing in-processing methods.
- No retraining needed when changing tradeoff ratio.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: fairness metrics, datasets, classifier family, and Pareto-front evaluation.

## Limits and Failure Modes

- Post-hoc control depends on the fairness definition used during representation learning.
- Representation optimization may not handle intersectional or distribution-shifted fairness constraints.
- Fairness-accuracy frontiers can vary across deployment populations.
- Practical governance still needs criteria for choosing the tradeoff point.

## Deep Themes

**Fairness needs deploy-time knobs.** Operational settings often require changing constraints after training.

**Representations can make post-processing effective.** The method prepares the feature space for later control.

**Tradeoff surfaces are infrastructure.** A model should expose a usable fairness-accuracy frontier.

## Subthemes

- Post-hoc fairness control.
- Fairness-accuracy tradeoff.
- Representation learning for post-processing.
- Fair Bayes-optimal classifier.
- No-retraining deployment adjustment.

## Connections to Other Papers

Connects to Fair Causal Bandits, SCIQL, CreDRO, and distribution-shift fairness/robustness papers. It provides a supervised-classification counterpart to online causal fairness.

## Notes for Cross-Paper Synthesis

This paper adds a controllability view of fairness: rather than hard-coding one point, train models whose tradeoff can be adjusted responsibly after training.
