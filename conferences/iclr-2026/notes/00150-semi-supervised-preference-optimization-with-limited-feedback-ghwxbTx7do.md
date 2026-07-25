# Semi-Supervised Preference Optimization with Limited Feedback

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ghwxbTx7do
- Authors: Seonggyun Lee; Sungjun Lim; Seojin Park; Soeun Cheon; Kyungwoo Song
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Preference Optimization;Semi-Supervised Learning
- Source URL: https://openreview.net/forum?id=ghwxbTx7do
- PDF URL: https://openreview.net/pdf?id=ghwxbTx7do

## Abstract

The field of preference optimization has made outstanding contributions to the alignment of language models with human preferences. Despite these advancements, recent methods still rely heavily on substantial paired (labeled) feedback data, leading to substantial resource expenditures. To address these challenges, we study the problem of Semi-Supervised Preference Optimization in which the idea is to learn from both a small number of pairwise preference labels and a large pool of unpaired samples simultaneously. Our key theoretical contribution proves the existence of an optimal reward threshold capable of separating winning and losing responses with high probability, which enables a principled pseudo-labeling of unpaired data. By leveraging these pseudo-labels, SSPO effectively distills latent preferences from large-scale unpaired data, thus maintaining human alignment while drastically reducing acquisition costs. Extensive experiments across datasets validate this remarkable data efficiency; for instance, SSPO trained with Mistral-7B-Instruct on just 1% of UltraFeedback consistently surpasses strong baselines trained on 10% of UltraFeedback.

## One-Sentence Claim

SSPO reduces preference-label cost by using a reward-threshold theory to pseudo-label large pools of unpaired responses from a small amount of pairwise feedback.

## Problem

Preference optimization has improved LLM alignment but usually needs substantial labeled pairwise feedback, which is expensive to collect.

Many unlabeled or unpaired candidate responses are available, but ordinary preference methods do not directly use them.

## Core Contribution

The paper studies Semi-Supervised Preference Optimization.

Its theoretical contribution proves the existence of an optimal reward threshold separating winning and losing responses with high probability, enabling principled pseudo-labeling of unpaired data.

## Method

SSPO learns from a small labeled preference set plus a large pool of unpaired samples.

It estimates or applies a reward threshold to assign pseudo-labels, then distills latent preferences from those pseudo-labeled responses to continue preference optimization.

## Experiments and Evidence

The abstract reports strong data efficiency across datasets.

Mistral-7B-Instruct trained with SSPO on 1 percent of UltraFeedback consistently surpasses strong baselines trained on 10 percent of UltraFeedback.

## Limits and Failure Modes

Pseudo-labeling can propagate threshold errors, especially when reward distributions overlap or preference data is biased. The method may be sensitive to calibration of the reward threshold.

Because this note is abstract-only, details still need checking: threshold theorem assumptions, pseudo-labeling pipeline, datasets, model backbones, comparison baselines, and robustness to noisy labels.

## Deep Themes

- Semi-supervised alignment: preference learning can use unlabeled responses, not only paired feedback.
- Reward-threshold pseudo-labeling: theoretical separation supports scalable data augmentation.
- Feedback efficiency: alignment cost is reduced by distilling latent preferences from unpaired samples.
- Limited-label post-training: stronger alignment can come from better use of weak data rather than more human labels.

## Subthemes

- Preference optimization.
- Semi-supervised learning.
- Pseudo-labeling.
- UltraFeedback.

## Connections to Other Papers

This connects to SafeDPO, AuxDPO, TI-DPO, and preference-alignment theory papers.

It also relates to data-efficiency work because label scarcity becomes the main bottleneck for alignment.

## Notes for Cross-Paper Synthesis

SSPO adds a label-efficiency alignment theme: preference optimization is becoming semi-supervised, with theory used to decide how unlabeled responses enter training.
