# Difficult Examples Hurt Unsupervised Contrastive Learning: A Theoretical Perspective

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 5LMdnUdAoy
- Authors: Yi-Ge Zhang; Jingyi Cui; Qiran Li; Yisen Wang
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: Machine Learning. Self-Supervised Learning. Difficult Examples
- Source URL: https://openreview.net/forum?id=5LMdnUdAoy
- PDF URL: https://openreview.net/pdf?id=5LMdnUdAoy

## Abstract

Unsupervised contrastive learning has shown significant performance improvements in recent years, often approaching or even rivaling supervised learning in various tasks. However, its learning mechanism is fundamentally different from supervised learning. Previous works have shown that difficult examples (well-recognized in supervised learning as examples around the decision boundary),  which are essential in supervised learning, contribute minimally in unsupervised settings. In this paper, perhaps surprisingly, we find that the direct removal of difficult examples, although reduces the sample size, can boost the downstream classification performance of contrastive learning. To uncover the reasons behind this, we develop a theoretical framework modeling the similarity between different pairs of samples. Guided by this framework, we conduct a thorough theoretical analysis revealing that the presence of difficult examples negatively affects the generalization of contrastive learning. Furthermore, we demonstrate that the removal of these examples, and techniques such as margin tuning and temperature scaling can enhance its generalization bounds, thereby improving performance.
Empirically, we propose a simple and efficient mechanism for selecting difficult examples and validate the effectiveness of the aforementioned methods, which substantiates the reliability of our proposed theoretical framework.

## One-Sentence Claim

Difficult examples that help supervised learning can harm unsupervised contrastive learning, and removing or down-weighting them can improve generalization.

## Problem

Contrastive learning differs from supervised learning, yet intuitions from supervised hard-example mining are often imported. Prior work suggests difficult examples contribute little in unsupervised settings, but their effect on generalization needs theory and practical mechanisms.

## Core Contribution

The paper develops a pair-similarity theoretical framework showing difficult examples can negatively affect contrastive generalization and that removal, margin tuning, or temperature scaling can improve bounds.

## Method

The theory models similarity among sample pairs and studies how difficult examples alter generalization. Empirically, the authors propose a simple mechanism to select difficult examples and validate removal/tuning strategies.

## Experiments and Evidence

The abstract reports improved downstream classification from directly removing difficult examples despite smaller sample size, plus empirical validation of selection, margin tuning, and temperature scaling.

## Limits and Failure Modes

PDF checks needed: definition of difficulty without labels, risk of removing semantically important minority modes, datasets/backbones, and whether benefits hold for multimodal/self-supervised foundation pretraining.

## Deep Themes

- Data selection can improve representation learning even by reducing data.
- Supervised-learning intuitions do not always transfer to self-supervised objectives.
- Theory is being used to guide data curation and objective tuning.

## Subthemes

- Unsupervised contrastive learning.
- Difficult-example removal.
- Generalization bounds.
- Temperature scaling.
- Margin tuning.

## Connections to Other Papers

Connects to data curation themes, Common Corpus, and efficient training. It is a theory-side counterpart to papers treating data as an intervention surface.

## Notes for Cross-Paper Synthesis

This paper reinforces a major data theme: more data is not always better; the objective determines which examples are useful or harmful.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00016-difficult-examples-hurt-unsupervised-contrastive-learning-a-theoretical-perspective-5LMdnUdAoy-arxiv.txt`.

Additional verified details:

- The theory models contrastive learning through an augmentation/similarity graph and derives linear probing error bounds with and without difficult examples.
- Difficult examples are modeled as boundary-near examples with higher similarity to samples from other classes.
- The analysis shows that larger gaps between difficult cross-class similarity and easy cross-class similarity worsen the generalization bound.
- Removing difficult examples restores the no-difficult-example bound form but with smaller effective sample size; the bound can still improve when the difficult examples are sufficiently harmful.
- Margin tuning is interpreted as subtracting a normalized margin matrix from the normalized similarity graph.
- Temperature scaling is interpreted as multiplying selected difficult-pair similarities, with smaller temperatures recommended for more difficult pairs.
- Experiments validate on CIFAR-10, CIFAR-100, STL-10, and TinyImageNet, with direct difficult-example removal giving a reported 0.8% boost on CIFAR-10 and selected margin/temperature tuning outperforming indiscriminate tuning.

Refined limits:

- The empirical gains appear modest in some settings and depend on a selection mechanism.
- Removing difficult examples risks discarding rare or semantically important modes if difficulty is misidentified.
