# Extending Sequence Length is Not All You Need: Effective Integration of Multimodal Signals for Gene Expression Prediction

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: wwPSfcf5Pj
- Authors: Zhao Yang; Yi Duan; Jiwei Zhu; Ying Ba; Chuan Cao; Bing Su
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: dna language model;gene expression prediction;multimodal information integration
- Source URL: https://openreview.net/forum?id=wwPSfcf5Pj
- PDF URL: https://openreview.net/pdf?id=wwPSfcf5Pj

## Abstract

Gene expression prediction, which predicts mRNA expression levels from DNA sequences, presents significant challenges. Previous works often focus on extending input sequence length to locate distal enhancers, which may influence target genes from hundreds of kilobases away. Our work first reveals that for current models, long sequence modeling can decrease performance. Even carefully designed algorithms only mitigate the performance degradation caused by long sequences. Instead, we find that proximal multimodal epigenomic signals near target genes prove more essential. Hence we focus on how to better integrate these signals, which has been overlooked. We find that different signal types serve distinct biological roles, with some directly marking active regulatory elements while others reflect background chromatin patterns that may introduce confounding effects. Simple concatenation may lead models to develop spurious associations with these background patterns. To address this challenge, we propose Prism (**P**roximal **r**egulatory **i**ntegration of **s**ignals for **m**RNA expression levels prediction), a framework that learns multiple combinations of high-dimensional epigenomic features to represent distinct background chromatin states and uses backdoor adjustment to mitigate confounding effects. Our experimental results demonstrate that proper modeling of multimodal epigenomic signals achieves state-of-the-art performance using only short sequences for gene expression prediction.

## One-Sentence Claim

Prism improves gene-expression prediction by using short DNA sequences plus carefully adjusted proximal epigenomic signals, showing that longer sequence context is less important than correctly integrated multimodal regulatory evidence.

## Problem

Gene expression prediction often chases longer DNA sequence windows to capture distal enhancers, but the abstract says current long-sequence models can lose performance. At the same time, proximal epigenomic signals are multimodal and biologically heterogeneous, so simple concatenation can create spurious associations with background chromatin patterns.

## Core Contribution

The paper contributes Prism, a framework for proximal regulatory integration of epigenomic signals for mRNA expression prediction. Its central contribution is to distinguish signal types by biological role and use backdoor adjustment to mitigate confounding from background chromatin states.

## Method

Prism learns multiple combinations of high-dimensional epigenomic features to represent distinct background chromatin states, then applies backdoor adjustment so the model can use active regulatory signals without overfitting to confounding chromatin patterns. The approach intentionally uses short DNA sequences rather than relying on longer genomic windows.

## Experiments and Evidence

The abstract reports state-of-the-art gene-expression prediction using only short sequences when multimodal epigenomic signals are modeled properly. It also reports the finding that long sequence modeling can decrease performance and that even specialized long-sequence algorithms mainly mitigate degradation rather than solve the core integration problem.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect which epigenomic assays are used, whether backdoor variables are identifiable, how cell-type and tissue specificity are handled, and whether short-sequence performance holds for genes regulated by truly distal enhancers. The causal framing may depend heavily on assumptions about observed chromatin states.

## Deep Themes

- Multimodal biological signal integration.
- Confounding-aware representation learning.
- Limits of longer-context scaling.
- Proximal regulatory evidence over distant sequence expansion.

## Subthemes

- Gene expression prediction.
- DNA language models.
- Epigenomic feature fusion.
- Background chromatin states.
- Backdoor adjustment.

## Connections to Other Papers

Connects directly to Intrinsic Entropy through skepticism toward longer context as an automatic gain. It also relates to RealPDEBench through scientific ML moving from simulation or sequence-only proxies toward richer real-world measured signals, and to Capacity Manipulation through the theme of allocating modeling attention to underrepresented but causally relevant information.

## Notes for Cross-Paper Synthesis

This paper strengthens a corpus-level pattern: scale along the obvious axis can be the wrong move. For genomics, longer context may hurt if the model does not integrate nearby regulatory modalities correctly; the deeper issue is causal signal selection under confounding.
