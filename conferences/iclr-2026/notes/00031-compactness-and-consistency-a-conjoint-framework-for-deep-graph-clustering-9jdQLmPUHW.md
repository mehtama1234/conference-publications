# Compactness and Consistency: A Conjoint Framework for Deep Graph Clustering

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 9jdQLmPUHW
- Authors: Wei Ju; Siyu Yi; Kangjie Zheng; Yifan Wang; Ziyue Qiao; Li Shen; Yongdao Zhou; Xiaochun Cao; Jiancheng Lv
- Primary area: learning on graphs and other geometries & topologies
- Keywords: Graph Neural Networks;Graph Clustering;Representation Learning;Consistency Learning
- Source URL: https://openreview.net/forum?id=9jdQLmPUHW
- PDF URL: https://openreview.net/pdf?id=9jdQLmPUHW

## Abstract

Graph clustering is a fundamental task in data analysis, aiming at grouping nodes with similar characteristics in the graph into clusters. This problem has been widely explored using graph neural networks (GNNs) due to their ability to leverage node attributes and graph topology for effective cluster assignments. However, representations learned through GNNs typically struggle to capture global relationships between nodes via local message-passing mechanisms. Moreover, the redundancy and noise inherently present in the graph data may easily result in node representations lacking compactness and robustness. To address the aforementioned issues, we propose a conjoint framework called CoCo, which captures compactness and consistency in the learned node representations for deep graph clustering. Technically, our CoCo leverages graph convolutional filters to learn robust node representations from both local and global views, and then encodes them into low-rank compact embeddings, thus effectively removing the redundancy and noise as well as uncovering the intrinsic underlying structure. To further enrich the node semantics, we develop a consistency learning strategy based on compact embeddings to facilitate knowledge transfer from the two perspectives. Our experimental findings indicate that our proposed CoCo outperforms state-of-the-art counterparts on various benchmark datasets.

## One-Sentence Claim

CoCo improves deep graph clustering by jointly enforcing compact low-rank node embeddings and consistency between local and global graph views.

## Problem

Graph clustering needs node representations that reflect attributes and topology. Standard GNN message passing is local, so it can miss global node relationships.

Graph data also contain redundancy and noise, which can make learned representations less compact and less robust for clustering.

## Core Contribution

The paper proposes CoCo, a conjoint framework for compactness and consistency in deep graph clustering.

It learns robust node representations from local and global views with graph convolutional filters, encodes them into low-rank compact embeddings, and uses consistency learning to transfer knowledge across views.

## Method

CoCo constructs local and global representations using graph convolutional filters. These are compressed into low-rank embeddings to remove redundant and noisy components.

A consistency learning strategy operates on compact embeddings so local and global perspectives enrich each other during clustering.

## Experiments and Evidence

The abstract reports that CoCo outperforms state-of-the-art graph clustering methods on various benchmark datasets.

The claimed mechanism is that compact embeddings uncover intrinsic structure while consistency learning enriches node semantics.

## Limits and Failure Modes

Low-rank compactness may discard rare but cluster-relevant signals, especially in heterophilous or highly imbalanced graphs.

Because this note is abstract-only, details still need checking: benchmark datasets, clustering metrics, graph filter design, low-rank objective, consistency loss, and robustness to noisy attributes or edges.

## Deep Themes

- Local-global graph representation: clustering needs both neighborhood and global relational structure.
- Compactness as denoising: low-rank embeddings remove redundancy and improve clusterability.
- Consistency learning for graph views: multiple perspectives can transfer semantic information.
- Representation geometry for unsupervised graph tasks: cluster quality depends on embedding structure.

## Subthemes

- Deep graph clustering.
- Low-rank compact embeddings.
- Local/global graph filters.
- Cross-view consistency.

## Connections to Other Papers

This connects to MV-FGAD, LAMP, and Relational Lottery Tickets through graph representation structure.

It also relates to NASH and data-selection work because both use compact or decomposed representations to make noisy data more useful.

## Notes for Cross-Paper Synthesis

CoCo adds to the compact-representation theme: unsupervised graph learning benefits when embeddings are both denoised and aligned across views.
