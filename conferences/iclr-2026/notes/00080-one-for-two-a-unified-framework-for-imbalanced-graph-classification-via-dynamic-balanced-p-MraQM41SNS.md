# One for Two: A Unified Framework for Imbalanced Graph Classification via Dynamic Balanced Prototype

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: MraQM41SNS
- Authors: Guanjun Wang; Binwu Wang; Jiaming Ma; Zhengyang Zhou; Pengkun Wang; Xu Wang; Yang Wang
- Primary area: learning on graphs and other geometries & topologies
- Keywords: Graph classification; graph imbalance learning; graph neural networks; Graph data mining; long-tail learning
- Source URL: https://openreview.net/forum?id=MraQM41SNS
- PDF URL: https://openreview.net/pdf?id=MraQM41SNS

## Abstract

Graph Neural Networks (GNNs) have advanced graph classification, yet they remain vulnerable to graph-level imbalance, encompassing class imbalance and topological imbalance. To address both types of imbalance in a unified manner, we propose UniImb, a Unified framework for Imbalanced graph classification. Specifically, UniImb first captures multi-scale topological features and enhances data diversity via learnable personalized graph perturbations. It then employs a dynamic balanced prototype module to learn representative prototypes from graph instances, improving the quality of graph representations. Concurrently, a prototype load-balancing optimization term mitigates dominance by majority samples to equalize sample influence during training. We justify these design choices theoretically using the Information Bottleneck principle. Extensive experiments on 19 datasets-including a large-scale imbalanced air pollution graph dataset AirGraph released by us and 23 baselines demonstrate that UniImb has achieved dominant performance across various imbalanced scenarios. Our code is available at GitHub.

## One-Sentence Claim

UniImb addresses both class imbalance and topological imbalance in graph classification through personalized graph perturbations, dynamic balanced prototypes, and prototype load balancing.

## Problem

Graph classification can suffer from graph-level imbalance in at least two forms: class imbalance, where labels are long-tailed, and topological imbalance, where graph structures differ unevenly across samples.

Existing approaches may target one imbalance type while leaving the other unaddressed, causing majority classes or dominant topologies to shape representations disproportionately.

## Core Contribution

The paper proposes UniImb, a unified framework for imbalanced graph classification.

It combines multi-scale topological feature capture, learnable personalized graph perturbations, dynamic balanced prototypes, and a prototype load-balancing objective. The design is justified with the Information Bottleneck principle.

## Method

UniImb first enriches graph representations through multi-scale topology features and personalized perturbations that increase data diversity.

It then learns representative balanced prototypes from graph instances and adds a load-balancing optimization term so majority samples do not dominate prototype learning.

## Experiments and Evidence

The abstract reports extensive experiments on 19 datasets and 23 baselines.

The authors also release AirGraph, a large-scale imbalanced air-pollution graph dataset, and report dominant performance across imbalanced scenarios.

## Limits and Failure Modes

Learnable graph perturbations can create unrealistic structures if not constrained. Prototype balancing may also trade off majority-class calibration against minority-class recall.

Because this note is abstract-only, details still need checking: definitions of topological imbalance, perturbation constraints, prototype update rules, Information Bottleneck proof, AirGraph construction, and per-dataset performance patterns.

## Deep Themes

- Unified imbalance modeling: label skew and structural skew are treated as coupled graph-learning problems.
- Prototype-based representation repair: balanced prototypes counter majority dominance in embedding space.
- Personalized graph augmentation: perturbations are learned per graph rather than applied as generic noise.
- Information bottleneck as justification: theoretical framing is used to motivate robust compressed representations.

## Subthemes

- Imbalanced graph classification.
- Dynamic balanced prototypes.
- Personalized graph perturbations.
- AirGraph dataset.

## Connections to Other Papers

This connects to Actions Speak Louder than Prompts, GNN exchangeability, MV-FGAD, and other graph robustness papers.

It also relates to long-tail learning and data curation themes because both ask how training should prevent dominant groups from controlling representation geometry.

## Notes for Cross-Paper Synthesis

UniImb adds a graph-specific fairness and robustness pattern: balanced learning must account for topology as well as labels.
