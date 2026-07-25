# FedARC: Anchor-Guided Residual Compensation for Data and Model Heterogeneous Federated Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qQhTbQSHdG
- Authors: Chentao Lu; Xuhao Ren; Dawei xu; Chuan Zhang; Liehuang Zhu
- Primary area: deep_learning->everything_else
- Keywords: Federated learning;Distributed Machine Learning;Deep Learning Algorithms
- Source URL: https://openreview.net/forum?id=qQhTbQSHdG
- PDF URL: https://openreview.net/pdf?id=qQhTbQSHdG

## Abstract

Federated learning (FL) allows clients to collaboratively train models without exposing private data, but practical FL is simultaneously challenged by data heterogeneity and model heterogeneity. Prior heterogeneous FL (HtFL) approaches often fail to handle fine-grained feature shifts, leading to weak representation alignment and limited cross-client knowledge transfer, which degrades both personalization and generalization. We propose FedARC, an HtFL framework that couples a shared lightweight extractor with client-specific fusion: a trainable projector integrates local and global embeddings, while adaptive residual compensation dynamically corrects feature-level mismatches. To further stabilize aggregation, FedARC performs semantic anchor alignment across clients, and we theoretically prove FedARC converges with a non-convex convergence rate $\mathcal{O}(1/T)$. Experiments on five public benchmarks demonstrate that FedARC outperforms nine state-of-the-art HtFL baselines by up to 2.63\% in average accuracy, while maintaining efficient communication and computation.

## One-Sentence Claim

FedARC improves heterogeneous federated learning by aligning clients through semantic anchors and correcting feature-level mismatches with adaptive residual compensation across shared and client-specific representations.

## Problem

Federated learning must often handle both data heterogeneity and model heterogeneity. Clients may have different distributions, capabilities, architectures, or personalization needs, making straightforward aggregation weak.

Prior heterogeneous FL methods often miss fine-grained feature shifts. Poor representation alignment limits cross-client knowledge transfer and harms both personalized performance and global generalization.

## Core Contribution

FedARC contributes a heterogeneous FL framework that combines a shared lightweight extractor with client-specific fusion. A trainable projector integrates local and global embeddings, while adaptive residual compensation corrects feature-level mismatches.

It also uses semantic anchor alignment to stabilize aggregation across clients and provides a non-convex convergence proof with rate O(1/T). The contribution is therefore representational, algorithmic, and theoretical.

## Method

The shared extractor provides a common representation base across heterogeneous clients. Client-specific fusion lets each client combine local and global embeddings according to its own data/model conditions.

Adaptive residual compensation handles feature-level discrepancies that remain after alignment, and semantic anchors give the aggregation process stable cross-client reference points. This design targets both personalization and knowledge transfer.

## Experiments and Evidence

The abstract reports experiments on five public benchmarks, where FedARC outperforms nine state-of-the-art heterogeneous FL baselines by up to 2.63 percent average accuracy while maintaining efficient communication and computation.

Full-paper reading should inspect benchmark heterogeneity settings, client model differences, communication rounds, ablations for anchors/residuals/projectors, and whether gains are consistent or concentrated in specific datasets.

## Limits and Failure Modes

The reported accuracy gain is modest, so practical value depends on robustness, communication savings, and behavior under severe heterogeneity. Semantic anchors could also fail if clients do not share enough label or feature semantics.

Federated systems face privacy, security, straggler, and incentive issues not captured by accuracy/convergence alone. Anchor alignment might leak information if not carefully designed.

## Deep Themes

- Federated alignment under heterogeneity: shared learning requires common semantic reference points.
- Residual compensation for feature shifts: mismatch is corrected at the representation level rather than hidden in aggregation.
- Personalization and generalization together: client-specific fusion preserves local adaptation while sharing global knowledge.
- Theory-backed systems learning: convergence under non-convex objectives supports practical FL design.

## Subthemes

- Model heterogeneity is distinct from data heterogeneity and must be handled jointly.
- Lightweight shared extractors reduce cross-client coordination burden.
- Semantic anchors stabilize aggregation.
- Communication efficiency remains central for real FL deployment.

## Connections to Other Papers

FedARC connects to fairness, privacy, and distributed-learning themes. It also relates to representation-alignment papers such as concept binding and Fair Posthoc Control because useful transfer depends on a representation space where comparisons are meaningful.

It connects to exact RL unlearning at the governance level: decentralized/adaptive systems need algorithms designed around privacy and user constraints rather than centralized retraining assumptions.

## Notes for Cross-Paper Synthesis

FedARC reinforces the idea that heterogeneity is not noise to average away. Across robotics, federated learning, and multimodal systems, the strongest methods preserve local structure while aligning through shared anchors or manifolds.
