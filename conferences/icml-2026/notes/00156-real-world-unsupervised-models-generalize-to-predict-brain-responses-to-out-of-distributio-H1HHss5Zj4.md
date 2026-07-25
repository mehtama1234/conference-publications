# Real-World Unsupervised Models Generalize to Predict Brain Responses to Out-of-Distribution Stimuli

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: H1HHss5Zj4
- Authors: Chenggang Chen; Zhiyu Yang; Xiaoqin Wang
- Primary area: applications->neuroscience_cognitive_science
- Keywords: Computational Neuroscience;NeuroAI;Unsupervised Learning;Speech;Out-of-Distribution
- Source URL: https://openreview.net/forum?id=H1HHss5Zj4
- PDF URL: https://openreview.net/pdf?id=H1HHss5Zj4

## Abstract

Deep neural networks currently provide the leading quantitative models of neural responses in sensory systems. However, these networks remain implausible as models of sensory development, largely because they rely on supervised training with label efficiency far exceeding that of biological learning. Furthermore, these models are typically trained on manually curated datasets that lack the statistical properties of the natural environments to which the brain is exposed. Here, we demonstrate that models trained with unsupervised objectives on real-world data significantly outperform supervised models in predicting brain responses across both human auditory and visual cortex. We show that this performance advantage is not driven by network architecture or dataset size, but rather by the data distribution. Crucially, we find that unsupervised models trained on real-world data exhibit remarkable out-of-distribution generalization: a model trained exclusively on Mandarin speech accurately predicts English-driven brain responses, and a model trained on infant head-cam footage predicts adult visual responses to curated object images. Together, our results illustrate how deep neural networks can be used to reveal the real-world statistics that shape neural representations in the brain.

## One-Sentence Claim

Unsupervised models trained on real-world sensory data predict human auditory and visual cortical responses better than supervised models and generalize across striking distribution shifts.

## Problem

Modern neural response models often rely on supervised training and curated datasets, making them statistically and developmentally mismatched to the learning conditions faced by biological sensory systems.

## Core Contribution

The paper argues that the data distribution and learning objective, not just architecture or scale, are central to building deep networks that explain sensory cortex.

## Method

The authors compare supervised and unsupervised models trained on different sensory data distributions, then test neural-response prediction across human auditory and visual cortex, including out-of-distribution transfer settings such as Mandarin-to-English speech and infant head-cam-to-adult-object-image vision.

## Experiments and Evidence

The abstract reports that unsupervised real-world models outperform supervised alternatives in predicting brain responses and that the advantage is not explained by architecture or dataset size. The strongest evidence claim is cross-domain generalization: Mandarin-trained speech models predict English-driven responses, and infant head-cam-trained visual models predict adult responses to curated object images.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact neural datasets, response-model fitting protocol, controls for architecture and scale, statistical significance, anatomical specificity, and whether supervised baselines were matched on pretraining quality.

## Deep Themes

- Natural data distribution as an inductive bias for intelligence and neuroscience.
- Unsupervised learning as a more biologically plausible route to sensory representations.
- OOD generalization as a test of representational alignment rather than benchmark accuracy alone.

## Subthemes

- Computational neuroscience.
- NeuroAI.
- Speech and vision representation learning.
- Infant egocentric visual data.
- Cross-lingual auditory transfer.
- Brain-response prediction.

## Connections to Other Papers

Connects to representation-geometry and multimodal papers in the corpus by treating learned internal structure as the object of scientific explanation. It also complements evaluation papers that move beyond in-distribution benchmark scores toward transfer, robustness, and mechanistic fit.

## Notes for Cross-Paper Synthesis

This paper adds a biological-grounding variant of the corpus's real-world-data theme: better models may come not from larger curated labels but from exposure to the same environmental statistics that shape deployed or biological agents.
