# MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: yBcY0bY45t
- Authors: Junyi Yan; KE LIANG; Hao Yu; Meng Liu; Hao Tan; Tianrui Liu; Jun-Jie Huang; Xinwang Liu
- Primary area: deep_learning->graph_neural_networks
- Keywords: Graph neural networks;Graph anomaly detection;Federated graph learning
- Source URL: https://openreview.net/forum?id=yBcY0bY45t
- PDF URL: https://openreview.net/pdf?id=yBcY0bY45t

## Abstract

Federated graph anomaly detection (GAD) aims to identify abnormal nodes in distributed subgraphs through federated learning. However, existing methods suffer from two limitations. 1) Their reliance on neighborhood aggregation assumes that anomalous information can be sufficiently captured, which often fails in federated learning with partitioned client subgraphs. 2) They overlook the detection bottleneck caused by weak attribute or structural anomalies. To tackle these challenges, we revisit federated GAD and reveal that weak anomalies exhibit harder-to-detect signals compared to strong anomalies. Specifically, we propose MV-FGAD, an efficient and effective federated GAD framework for mining anomalies of varying strengths. MV-FGAD introduces a federated knowledge learning module to aggregate and broadcast shared knowledge, which is further exploited to optimize local topological structures. Moreover, it designs a multi-view learning mechanism to capture diverse anomaly patterns, and adopts Mahalanobis distance–based scoring strategy to quantify node abnormality across views. Extensive experiments on real-world datasets of varying types and scales demonstrate MV-FGAD's efficiency and effectiveness. Our code is publicly available at https://github.com/Junyi-Yan/MV-FGAD.

## One-Sentence Claim

MV-FGAD improves federated graph anomaly detection by sharing federated knowledge, optimizing local topology, and scoring multi-view anomaly signals with Mahalanobis distance.

## Problem

Federated graph anomaly detection must identify abnormal nodes across distributed subgraphs. Neighborhood aggregation can fail when clients see partitioned subgraphs, because anomaly evidence may be incomplete locally.

Existing methods also overlook weak attribute or structural anomalies, whose signals are harder to detect than strong anomalies.

## Core Contribution

The paper revisits federated GAD and distinguishes weak from strong anomaly signals. It proposes MV-FGAD, an efficient federated framework for anomalies of varying strengths.

The contribution combines federated knowledge learning, local topology optimization, multi-view anomaly pattern capture, and Mahalanobis distance-based scoring.

## Method

A federated knowledge learning module aggregates and broadcasts shared knowledge across clients. Local clients exploit that shared knowledge to optimize topological structures.

The multi-view learning mechanism captures diverse anomaly patterns, and Mahalanobis scoring quantifies node abnormality across those views.

## Experiments and Evidence

The abstract reports extensive experiments on real-world datasets of varying types and scales, showing efficiency and effectiveness.

It also claims that weak anomalies exhibit harder-to-detect signals than strong anomalies, motivating multi-view detection.

## Limits and Failure Modes

Federated anomaly detection may be sensitive to client partitioning, non-IID graph distributions, privacy constraints, and malicious or low-quality clients.

Because this note is abstract-only, details still need checking: anomaly definitions, datasets, privacy model, communication cost, topology optimization details, Mahalanobis covariance estimation, and performance on extremely sparse clients.

## Deep Themes

- Federated graph learning under partial observability: each client sees an incomplete anomaly context.
- Weak anomaly detection: subtle attribute or structure deviations need richer views.
- Shared knowledge for local structure repair: federation can improve local topology interpretation.
- Multi-view abnormality scoring: anomaly is not a single signal type.

## Subthemes

- Graph anomaly detection.
- Federated knowledge broadcast.
- Local topology optimization.
- Mahalanobis multi-view scoring.

## Connections to Other Papers

This connects to SmartFed, SpineFL, and federated personalization work through the challenge of sharing useful global structure without centralizing data.

It also relates to graph papers such as LAMP, Relational Lottery Tickets, and IO-aware GNNs, but its focus is distributed anomaly detection rather than temporal memory or systems kernels.

## Notes for Cross-Paper Synthesis

MV-FGAD contributes to the distributed-structure theme: federated settings make representation learning harder because important relational evidence is fragmented across clients.
