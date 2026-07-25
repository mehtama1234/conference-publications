# Learning with Dual-level Noisy Correspondence for Multi-modal Entity Alignment

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: mytIKuRsSE
- Authors: Haobin Li; Yijie Lin; Peng Hu; Mouxing Yang; Xi Peng
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: Noisy correspondence; Multi-modal entity alignment.
- Source URL: https://openreview.net/forum?id=mytIKuRsSE
- PDF URL: https://openreview.net/pdf?id=mytIKuRsSE

## Abstract

Multi-modal entity alignment (MMEA) aims to identify equivalent entities across heterogeneous multi-modal knowledge graphs (MMKGs), where each entity is described by attributes from various modalities. Existing methods typically assume that both intra-entity and inter-graph correspondences are faultless, which is often violated in real-world MMKGs due to the reliance on expert annotations.
In this paper, we reveal and study a highly practical yet under-explored problem in MMEA, termed Dual-level Noisy Correspondence (DNC).
DNC refers to misalignments in both intra-entity (entity-attribute) and inter-graph (entity-entity and attribute-attribute) correspondences.
To address the DNC problem, we propose a robust MMEA framework termed RULE. RULE first estimates the reliability of both intra-entity and inter-graph correspondences via a dedicated two-fold principle. Leveraging the estimated reliabilities, RULE mitigates the negative impact of intra-entity noise during attribute fusion and prevents overfitting to noisy inter-graph correspondences during inter-graph discrepancy elimination. Beyond the training-time designs, RULE further incorporates a correspondence reasoning module that uncovers the underlying attribute-attribute connection across graphs, guaranteeing more accurate equivalent entity identification.
Extensive experiments on five benchmarks verify the effectiveness of our method against the DNC compared with seven state-of-the-art methods. 
The code will be released upon acceptance.

## One-Sentence Claim

RULE makes multimodal entity alignment robust to noisy entity-attribute and cross-graph correspondences by estimating correspondence reliability and reasoning over attribute links.

## Problem

Multi-modal entity alignment often assumes clean intra-entity attributes and clean inter-graph entity/attribute correspondences. Real multimodal knowledge graphs rely on expert annotations and heterogeneous sources, so both levels can be noisy, causing fusion errors and overfitting to incorrect alignments.

## Core Contribution

The paper defines Dual-level Noisy Correspondence for MMEA and proposes RULE, a robust alignment framework that estimates reliability for intra-entity and inter-graph correspondences, mitigates noisy attribute fusion, reduces overfitting to noisy cross-graph matches, and adds correspondence reasoning.

## Method

RULE first applies a two-fold principle to estimate correspondence reliability. It uses those reliabilities during multimodal attribute fusion and inter-graph discrepancy elimination, then uses a reasoning module to infer attribute-attribute connections across graphs for better equivalent-entity identification.

## Experiments and Evidence

Extensive experiments on five benchmarks reportedly show RULE outperforming seven state-of-the-art MMEA methods under dual-level noisy correspondence.

## Limits and Failure Modes

Reliability estimation can fail if noise is systematic, adversarial, or correlated with rare entity types. The benchmark construction may determine how realistic DNC is. Full-text review should check noise models, modality types, benchmark statistics, ablations of reliability and reasoning modules, and performance under real rather than injected noise.

## Deep Themes

- Robust multimodal alignment under noisy correspondences.
- Reliability-weighted representation fusion.
- Knowledge-graph alignment beyond clean supervision.
- Reasoning over attribute-level links.

## Subthemes

- Dual-level noisy correspondence.
- Intra-entity entity-attribute noise.
- Inter-graph entity and attribute misalignment.
- Correspondence reliability estimation.
- Multimodal knowledge graph entity matching.

## Connections to Other Papers

Connects to MASK and cross-modal retrieval/alignment papers through semantic bridging across modalities, to data-quality papers through noisy labels, and to robustness benchmarks where real deployment violates clean correspondence assumptions.

## Notes for Cross-Paper Synthesis

RULE reinforces a corpus-wide point: alignment is often brittle because the correspondences used for training are assumed clean. Estimating link reliability becomes part of the model, not a preprocessing detail.
