# Protein Fold Classification at Scale: Benchmarking and Pretraining

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: jPKqiaPTEd
- Authors: Dexiong Chen; Andrei Manolache; Mathias Niepert; Karsten Borgwardt
- Primary area: applications->health_medicine
- Keywords: protein fold classification;benchmarking;protein representation learning;masked autoencoders
- Source URL: https://openreview.net/forum?id=jPKqiaPTEd
- PDF URL: https://openreview.net/pdf?id=jPKqiaPTEd

## Abstract

Classifying protein topology is essential for deciphering biological function, but progress is held back by the lack of large-scale benchmarks that avoid duplicates and by models that do not scale well. We introduce TEDBench, a large-scale, non-redundant benchmark for protein fold classification constructed from the Encyclopedia of Domains (TED) and Foldseek-clustered AlphaFold structures. We show that on TEDBench, current protein representation learning methods either require very large models or fail to deliver strong performance.
To address this challenge, we propose Masked Invariant Autoencoders (MiAE), a self-supervised framework for protein structure representation learning. MiAE uses an extremely high masking ratio of up to $90\%$ with an $\mathrm{SE(3)}$-invariant encoder and a lightweight decoder that reconstructs backbone coordinates from the latent representation and mask tokens. MiAE scales well and outperforms supervised counterparts and state-of-the-art baselines on TEDBench, establishing a strong recipe for protein fold classification. To test transfer beyond AlphaFold structures, we further benchmark on a curated dataset from experimental structures of CATH v4.4. TEDBench is available at https://github.com/BorgwardtLab/TEDBench.

## One-Sentence Claim

TEDBench and MiAE provide a non-redundant large-scale benchmark and scalable self-supervised pretraining recipe for protein fold classification.

## Problem

Protein topology classification is important for understanding biological function, but progress is limited by duplicated benchmarks and representation-learning methods that either require very large models or underperform at scale.

The paper asks how to benchmark fold classification without redundancy and how to pretrain protein structure encoders that scale effectively.

## Core Contribution

The paper introduces TEDBench, a large-scale non-redundant fold-classification benchmark built from the Encyclopedia of Domains and Foldseek-clustered AlphaFold structures. It also proposes Masked Invariant Autoencoders, a self-supervised protein-structure representation framework.

MiAE uses up to 90% masking, an SE(3)-invariant encoder, and a lightweight decoder to reconstruct backbone coordinates from latent representations and mask tokens.

## Method

TEDBench is constructed by clustering AlphaFold structures to reduce redundancy and using TED domain annotations for fold labels. MiAE pretrains by heavily masking structural input and reconstructing backbone coordinates while preserving SE(3)-invariant representation properties.

The method is also tested beyond AlphaFold by benchmarking transfer on a curated experimental-structure dataset from CATH v4.4.

## Experiments and Evidence

Evidence reported in the abstract:

- TEDBench large-scale non-redundant benchmark.
- Built from TED and Foldseek-clustered AlphaFold structures.
- Existing methods either need very large models or fail to perform strongly.
- MiAE uses up to 90% masking with SE(3)-invariant encoder and lightweight decoder.
- MiAE outperforms supervised counterparts and state-of-the-art baselines on TEDBench.
- Transfer tested on curated experimental CATH v4.4 structures.
- TEDBench released at the listed GitHub URL.

Source depth is abstract/metadata only; full-paper reading needed for benchmark size, split construction, leakage controls, and architecture details.

## Limits and Failure Modes

- AlphaFold-derived structures may contain prediction biases not present in experimental structures.
- Foldseek clustering reduces redundancy but may not eliminate all homologous leakage.
- High masking ratios may favor global fold signals over local functional motifs.
- Transfer to experimental structures needs careful domain-shift analysis.

## Deep Themes

**Benchmark hygiene matters in biology.** Non-redundancy is central because structural duplicates can inflate performance.

**Invariant pretraining matches molecular geometry.** SE(3)-invariant encoders encode the physical symmetry of protein structures.

**Masked modeling scales beyond text and images.** Extreme masking can train structural representations for scientific classification.

## Subthemes

- Protein fold classification.
- TEDBench.
- Masked Invariant Autoencoders.
- SE(3)-invariant protein representation.
- AlphaFold-to-CATH transfer.

## Connections to Other Papers

Connects to ReViT, LoRFS, NeuronCtrl, scientific generative-control papers, and data-curation work. It shares the theme that scientific ML needs both domain-invariant architectures and careful benchmark construction.

## Notes for Cross-Paper Synthesis

This paper adds a biological benchmark/pretraining thread: reliable scientific progress depends on non-redundant evaluation and representations that respect the geometry of the domain.
