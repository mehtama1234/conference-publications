# Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 92oF5bU4cU
- Authors: Yulu Gan; Phillip Isola
- Primary area: deep_learning->large_language_models
- Keywords: Random Search;Representation Learning;Large Language Models
- Source URL: https://openreview.net/forum?id=92oF5bU4cU
- PDF URL: https://openreview.net/pdf?id=92oF5bU4cU

## Abstract

Pretraining produces a learned parameter vector that is typically treated as a starting point for further iterative adaptation. In this work, we instead view the outcome of pretraining as a distribution over parameter vectors, whose support already contains task-specific experts. We show that in smaller or insufficiently trained models such expert solutions occupy a negligible fraction of the volume of this distribution, making their discovery reliant on structured optimization methods such as gradient descent. In contrast, in large, well-pretrained models the density of task-experts increases dramatically, so that diverse specialists populate a substantial fraction of the neighborhood around the pretrained weights. Motivated by this perspective, we explore a simple, fully parallel post-training method that samples $N$ parameter vectors at random, selects the top $K$, and ensembles them via majority vote to combine complementary expertise. Despite its simplicity, this approach is competitive with standard post-training methods such as PPO, GRPO, and ES for contemporary large-scale models.

## One-Sentence Claim

Large well-pretrained models contain many nearby task-specialist parameter vectors, enabling random parallel sampling and ensembling as a competitive post-training method.

## Problem

Pretrained weights are usually treated as an initialization for iterative optimization, but this may ignore the possibility that task experts already occupy dense regions near the pretrained solution.

## Core Contribution

The paper reframes pretraining as producing a distribution over nearby parameter vectors whose support can contain diverse task experts, then tests random sampling, selection, and majority-vote ensembling.

## Method

The proposed post-training method samples N parameter vectors around pretrained weights, evaluates and selects the top K, then ensembles their predictions by majority vote to combine complementary expertise without sequential gradient updates.

## Experiments and Evidence

The abstract reports that the method is competitive with PPO, GRPO, and evolutionary strategies on contemporary large-scale models, and that expert density increases dramatically in large, well-pretrained models.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: sampling distribution, task suite, evaluation budget fairness, ensemble cost, and how expert density is measured.

## Deep Themes

- Pretraining may create dense local landscapes of task experts.
- Post-training can exploit parallel search rather than only iterative adaptation.
- Scale changes the geometry of nearby parameter solutions.

## Subthemes

- Random search post-training.
- Local parameter neighborhoods.
- Expert density.
- Ensembling.
- PPO/GRPO comparison.
- Pretraining geometry.

## Connections to Other Papers

Connects to skill neologisms, midtraining, and alignment pretraining through views of pretraining as shaping accessible downstream behaviors. It also links to optimization papers that reinterpret adaptation geometry.

## Notes for Cross-Paper Synthesis

Neural Thickets adds a local-landscape theme: at sufficient scale, adaptation may become partly a search problem over dense nearby specialists.
