# LLM DNA: Tracing Model Evolution via Functional Representations

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: UIxHaAqFqQ
- Authors: Zhaomin Wu; Haodong Zhao; Ziyang Wang; Jizhou Guo; Qian Wang; Bingsheng He
- Primary area: unsupervised, self-supervised, semi-supervised, and supervised representation learning
- Keywords: Large Language Model;Representations;Fingerprint;Embedding;Evolution;Phylogenetic Tree;DNA;Dimension Reduction
- Source URL: https://openreview.net/forum?id=UIxHaAqFqQ
- PDF URL: https://openreview.net/pdf?id=UIxHaAqFqQ

## Abstract

The explosive growth of large language models (LLMs) has created a vast but opaque landscape: millions of models exist, yet their evolutionary relationships through fine-tuning, distillation, or adaptation are often undocumented or unclear, complicating LLM management. Existing methods are limited by task specificity, fixed model sets, or strict assumptions about tokenizers or architectures. Inspired by biological DNA, we address these limitations by mathematically defining *LLM DNA* as a low-dimensional, bi-Lipschitz representation of functional behavior. We prove that LLM DNA satisfies *inheritance* and *genetic determinism* and establish its existence. Building on this theory, we derive a general, scalable, training-free pipeline for DNA extraction. In experiments across 305 LLMs, DNA aligns with prior studies on limited subsets and achieves superior or competitive performance on various tasks. Beyond these tasks, DNA comparisons uncover previously undocumented relationships among LLMs. We further construct the evolutionary tree of LLMs using phylogenetic algorithms, which align with shifts from encoder-decoder to decoder-only architectures, reflect temporal progression, and reveal distinct evolutionary speeds across LLM families.

## One-Sentence Claim

LLM DNA defines low-dimensional functional fingerprints that trace evolutionary relationships among language models across fine-tuning, distillation, and adaptation.

## Problem

The LLM ecosystem contains many models whose ancestry and relationships are undocumented. Fine-tuning, distillation, merges, and adaptations make model management difficult.

Existing comparison methods can depend on task choices, fixed model sets, tokenizer assumptions, or architecture constraints.

## Core Contribution

The paper mathematically defines LLM DNA as a low-dimensional bi-Lipschitz representation of functional behavior.

It proves inheritance and genetic determinism properties, establishes existence, and derives a scalable training-free DNA extraction pipeline.

## Method

LLM DNA compares models through functional representations rather than raw weights or narrow benchmark scores.

The extracted fingerprints are then compared and organized with phylogenetic algorithms to infer model-family relationships and evolutionary trees.

## Experiments and Evidence

The abstract reports experiments across 305 LLMs.

DNA aligns with prior studies on known subsets, performs competitively or better on several tasks, uncovers undocumented model relationships, and produces an evolutionary tree reflecting architecture shifts, temporal progression, and different family-specific evolution speeds.

## Limits and Failure Modes

Functional fingerprints depend on the probe distribution used to elicit behavior. Undocumented training data overlap or shared post-training recipes could create similarity that is not true lineage.

Because this note is abstract-only, details still need checking: probe construction, dimensionality reduction, bi-Lipschitz proof, phylogenetic algorithm, model set, tokenizer invariance, and validation against known ancestry.

## Deep Themes

- Model provenance at ecosystem scale: behavior fingerprints help manage opaque model families.
- Functional representation over metadata: lineage can be inferred from what models do, not only reported training history.
- Phylogenetics for ML models: biological ancestry tools are repurposed for model evolution.
- Training-free model forensics: scalable model comparison avoids retraining or architecture-specific assumptions.

## Subthemes

- LLM DNA.
- Functional fingerprints.
- Model evolution trees.
- Bi-Lipschitz behavioral representations.

## Connections to Other Papers

This connects to Huxley-Goedel Machine, RAIN-Merging, WSM, and model-merging/adaptation papers because model lineage becomes harder to track as adaptation proliferates.

It also relates to data governance and provenance themes across the corpus.

## Notes for Cross-Paper Synthesis

LLM DNA adds a provenance theme: as models are copied, tuned, merged, and self-improved, functional ancestry tracking becomes infrastructure for governance and evaluation.
