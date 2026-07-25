# ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 0BkvUY61MX
- Authors: Shayne Longpre; Sneha Kudugunta; Niklas Muennighoff; I-Hung Hsu; Isaac Rayburn Caswell; Alex Pentland; Sercan O Arik; Chen-Yu Lee; Sayna Ebrahimi
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: scaling laws;multilinguality
- Source URL: https://openreview.net/forum?id=0BkvUY61MX
- PDF URL: https://openreview.net/pdf?id=0BkvUY61MX

## Abstract

Scaling laws research has focused overwhelmingly on English—yet the most prominent AI models explicitly serve billions of international users. In this work, we undertake the largest multilingual scaling laws study to date, totaling 774 multilingual training experiments, spanning 10M-8B model parameters, 400+ training languages and 48 evaluation languages. We introduce the Adaptive Transfer Scaling Law (ATLAS) for both monolingual and multilingual pretraining, which outperforms existing scaling laws' out-of-sample generalization often by more than 0.3 R². Our analyses of the experiments shed light on multilingual learning dynamics, transfer properties between languages, and the curse of multilinguality. First, we derive a cross-lingual transfer matrix, empirically measuring mutual benefit scores between 38 × 38 = 1444 language pairs. Second, we derive a language-agnostic scaling law that reveals how to optimally scale model size and data when adding languages without sacrificing performance. Third, we identify the computational crossover points for when to pretrain from scratch versus finetune from multilingual checkpoints. We hope these findings provide the scientific foundation for democratizing scaling laws across languages, and enable practitioners to efficiently scale models—beyond English-first AI.

## One-Sentence Claim

ATLAS provides adaptive multilingual scaling laws that model transfer, data allocation, and compute crossover points across hundreds of languages rather than extrapolating from English-only scaling.

## Problem

Scaling-law work is heavily English-centric, even though deployed AI systems serve multilingual users. Multilingual models face transfer asymmetries and a curse of multilinguality, where adding languages can dilute performance unless model size, data, and training strategy are scaled appropriately.

## Core Contribution

The paper contributes the Adaptive Transfer Scaling Law for monolingual and multilingual pretraining, plus empirical analyses of language-pair transfer, language-agnostic scaling, and when to pretrain from scratch versus finetune multilingual checkpoints.

## Method

The study runs 774 multilingual training experiments over model sizes from 10M to 8B parameters, more than 400 training languages, and 48 evaluation languages. It fits adaptive scaling laws, derives a 38-by-38 cross-lingual transfer matrix, and estimates compute crossover points for training strategy choices.

## Experiments and Evidence

The abstract reports that ATLAS improves out-of-sample scaling-law generalization over existing laws, often by more than 0.3 R-squared. It also reports empirical transfer scores for 1,444 language pairs and a language-agnostic scaling law for adding languages without sacrificing performance.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect language selection, token budgets, tokenizer effects, data quality differences, evaluation tasks, and whether transfer estimates hold for low-resource, code-switched, or morphologically rich languages. Scaling laws may fit the studied range but extrapolate poorly outside it.

## Deep Themes

- Multilingual scaling laws.
- Cross-lingual transfer matrices.
- Curse of multilinguality.
- Compute-efficient pretraining versus finetuning choices.

## Subthemes

- ATLAS.
- 400+ training languages.
- 48 evaluation languages.
- Language-agnostic scaling.
- Pretrain-finetune crossover.

## Connections to Other Papers

Connects to multi-epoch scaling through data/model scaling theory, to COMPACT through efficient data allocation, and to multilingual RAG/nepotism notes in the ICML corpus where language coverage and preference tradeoffs shape system behavior.

## Notes for Cross-Paper Synthesis

ATLAS extends the corpus's scaling-law theme beyond English. The deeper pattern is adaptive allocation: scaling multilingual systems requires modeling transfer structure, not just adding more tokens or parameters uniformly.
