# Protein Autoregressive Modeling via Multiscale Structure Generation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 08tW615mgI
- Authors: Yanru Qu; Cheng-Yen Hsieh; Zaixiang Zheng; Ge Liu; Quanquan Gu
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Protein backbone generation;Multi-scale autoregressive modeling;Zero-shot generalization
- Source URL: https://openreview.net/forum?id=08tW615mgI
- PDF URL: https://openreview.net/pdf?id=08tW615mgI

## Abstract

We present protein autoregressive modeling (PAR), the first multi-scale autoregressive framework for protein backbone generation via coarse-to-fine next-scale prediction. Using the hierarchical nature of proteins, PAR generates structures that mimic sculpting a statue, forming a coarse topology and refining structural details over scales. To achieve this, PAR consists of three key components: (i) multi-scale downsampling operations that represent protein structures across multiple scales during training; (ii) an autoregressive transformer that encodes multi-scale information and produces conditional embeddings to guide structure generation; (iii) a flow-based backbone decoder that generates backbone atoms conditioned on these embeddings. Moreover, autoregressive models suffer from exposure bias, caused by the training and the generation procedure mismatch, and substantially degrades structure generation quality. We effectively alleviate this issue by adopting noisy context learning and scheduled sampling, enabling robust backbone generation. Notably, PAR exhibits strong zero-shot generalization, supporting flexible human-prompted conditional generation and motif scaffolding without requiring fine-tuning. On the unconditional generation benchmark, PAR effectively learns protein distributions and produces backbones of high design quality, and exhibits favorable scaling behavior. Together, these properties establish PAR as a promising framework for protein structure generation.

## One-Sentence Claim

PAR generates protein backbones with a coarse-to-fine autoregressive framework that combines multiscale structure representations, transformer conditioning, and a flow-based decoder.

## Problem

Protein backbone generation must capture hierarchical structure across scales, but standard generation methods can struggle with robust structural detail and autoregressive exposure bias.

## Core Contribution

The paper introduces the first multiscale autoregressive framework for protein backbone generation, using coarse-to-fine next-scale prediction and flow-based atom decoding.

## Method

PAR builds multiscale downsampled protein representations, uses an autoregressive transformer to encode scale-conditioned information, and decodes backbone atoms with a flow-based decoder. It mitigates exposure bias through noisy context learning and scheduled sampling.

## Experiments and Evidence

The abstract claims strong unconditional generation quality, favorable scaling behavior, zero-shot generalization, human-prompted conditional generation, and motif scaffolding without fine-tuning.

## Limits and Failure Modes

PDF checks needed: biological validity metrics, comparison to diffusion/flow baselines, side-chain/designability evaluation, success rates for motif scaffolding, and whether zero-shot prompts remain reliable for hard structural constraints.

## Deep Themes

- Scientific generative modeling is adopting foundation-model sequence ideas while respecting domain hierarchy.
- Coarse-to-fine generation is a recurring strategy for structured outputs.
- Flow models and autoregressive transformers are being composed for physical structures.

## Subthemes

- Protein backbone generation.
- Multiscale autoregression.
- Flow-based decoding.
- Scheduled sampling.
- Zero-shot scientific generation.

## Connections to Other Papers

Connects to generative modeling, scientific ML, flow matching, and structured world/3D generation. It is a biological counterpart to work that generates scenes or constrained combinatorial structures.

## Notes for Cross-Paper Synthesis

This paper strengthens the scientific-domain theme: methods from language and generative modeling are being adapted to physical structures through hierarchy, constraints, and domain-specific validity checks.
