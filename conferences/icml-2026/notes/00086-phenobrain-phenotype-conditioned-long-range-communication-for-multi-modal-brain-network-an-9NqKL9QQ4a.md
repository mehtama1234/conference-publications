# PhenoBrain: Phenotype-Conditioned Long-Range Communication for Multi-Modal Brain Network Analysis

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9NqKL9QQ4a
- Authors: Lingyuan Meng; KE LIANG; Hao Li; Meng Liu; Weijia Shi; Miaomiao Li; Yang Gao; Xinwang Liu
- Primary area: deep_learning->graph_neural_networks
- Keywords: multi-modal graph learning;brain network analysis
- Source URL: https://openreview.net/forum?id=9NqKL9QQ4a
- PDF URL: https://openreview.net/pdf?id=9NqKL9QQ4a

## Abstract

Multi-modal brain network analysis aims to predict neuropsychiatric status from functional connectomes with heterogeneous phenotypes. However, most existing methods treat phenotypes as auxiliary features and perform late fusion, implicitly assuming that the connectome representation should be learned in the same way regardless of phenotype. However, in clinical neuroscience the same functional connectivity pattern may support different conclusions under different phenotype contexts. To bridge this gap, we propose PhenoBrain, a novel framework for multi-modal brain network analysis that injects phenotype information at the mechanism level rather than only at the classifier level. Specifically, we propose a phenotype-conditioned long-range routing mechanism, which learns a subject-specific multi-hop communication kernel to model long-range connectome interactions. Furthermore, we propose a phenotypic-guided attention mechanism regulation method, which uses phenotypic information as a conditional prior to regulate the learning process of attention in brain networks. To verify the effectiveness of our method, we constructed two multi-modal brain network analysis datasets based on open-source image data. Extensive experiments demonstrate that PhenoBrain achieves state-of-the-art performance.

## One-Sentence Claim

PhenoBrain conditions brain-network message passing on subject phenotypes so the same connectivity pattern can be interpreted differently under different clinical contexts.

## Problem

Multi-modal brain network models often treat phenotypes as late-fusion auxiliary features, implicitly assuming that connectome representations should be learned identically across phenotype contexts.

## Core Contribution

The paper proposes PhenoBrain, a framework that injects phenotype information into the representation-learning mechanism through subject-specific long-range routing and attention regulation.

## Method

PhenoBrain learns a phenotype-conditioned multi-hop communication kernel for long-range connectome interactions and uses phenotypic-guided attention regulation as a conditional prior during brain-network learning.

## Experiments and Evidence

The abstract reports two multi-modal brain network datasets built from open-source imaging data and extensive experiments showing state-of-the-art performance.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv is currently being deferred after repeated 429/503 errors. Details still need checking: phenotype variables, dataset construction, clinical endpoints, ablations for routing versus attention regulation, and generalization across sites.

## Deep Themes

- Clinical graph learning needs context-conditioned mechanisms, not only late feature fusion.
- Phenotypes can change the meaning of identical connectivity patterns.
- Long-range graph communication is becoming domain-specific and subject-specific.

## Subthemes

- Brain network analysis.
- Multi-modal graph learning.
- Phenotype conditioning.
- Long-range routing.
- Attention regulation.
- Neuropsychiatric prediction.

## Connections to Other Papers

Connects to HyperDepth and S3GNN through graph representation learning, and to scientific/healthcare ML papers through domain-aware architectures that encode clinical context.

## Notes for Cross-Paper Synthesis

PhenoBrain adds a clinical-context theme: the model's communication pattern should depend on phenotype, because graph structure is not semantically fixed across subjects.
