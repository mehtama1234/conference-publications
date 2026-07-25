# End-to-End Compression for Tabular Foundation Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 84mfkGDxYh
- Authors: Guri Zabërgja; Rafiq Kamel; Arlind Kadra; Christian Frey; Josif Grabocka
- Primary area: deep_learning->foundation_models
- Keywords: tabular data;tabular compression
- Source URL: https://openreview.net/forum?id=84mfkGDxYh
- PDF URL: https://openreview.net/pdf?id=84mfkGDxYh

## Abstract

The long-standing dominance of gradient-boosted decision trees for tabular data has recently been challenged by in-context learning tabular foundation models. In-context learning methods fit and predict in one forward pass without parameter updates by leveraging the training data as context for predicting on query test points. 
While recent tabular foundation models achieve state-of-the-art performance, their transformer architecture based on the attention mechanism has quadratic complexity regarding dataset size, which in turn increases the overhead on training and inference time, and limits the capacity of the models to handle large-scale datasets. In this work, we propose TACO, an end-to-end tabular compression model that compresses the training dataset in a latent space. We test our method on the TabArena benchmark, where our proposed method is up to 94x faster in inference time, while consuming up to 97% less memory compared to the state-of-the-art tabular Transformer architecture, all while retaining performance without significant degradation. Lastly, our method not only scales better with increased dataset sizes, but it also achieves better performance compared to other baselines.

## One-Sentence Claim

TACO compresses tabular in-context training data into latent context tokens, making tabular foundation model inference much faster and cheaper while retaining accuracy.

## Problem

Tabular foundation models use training rows as in-context data, but Transformer attention over the dataset creates quadratic scaling in dataset size, causing high latency and memory use.

## Core Contribution

The paper introduces TACO, an end-to-end context-compression architecture for tabular foundation models that reduces the effective context table before prediction.

## Method

TACO encodes a dataset into latent representations and compresses the training context into fewer learned rows/tokens before a decoder-only tabular predictor attends over it. The compression rate becomes an explicit knob controlling the inference memory and compute budget.

## Experiments and Evidence

The abstract reports TabArena results with up to 94x faster inference and up to 97% less memory than a state-of-the-art tabular Transformer, without significant performance degradation and with better scaling as dataset size increases.

## Full-Text Upgrade

The full text positions TACO as a modular compressor that can be integrated with decoder-only tabular foundation models. It attacks the O(N^2) inference bottleneck induced by attending over N training rows and aims to linearly reduce inference complexity with respect to the compressed context size.

The experiments compare TACO against a predictor-only Transformer on TabArena classification tasks and larger synthetic scaling grids. The paper reports that TACO remains consistently faster across grid points, can make KV caching feasible under tighter memory budgets, and reaches around 94x speedup at a 1% compression rate in the repeated-prediction setting.

## Limits and Failure Modes

Limits to watch: compression can discard minority or rare-row signals; the best compression rate may vary by table size and feature structure; and the reported benefits depend on the paired tabular predictor and benchmark distribution.

## Deep Themes

- Foundation models for structured data need context compression, not only larger pretraining.
- In-context learning creates systems bottlenecks when the context is an entire dataset.
- Compression becomes a tunable budget interface for deployment.

## Subthemes

- Tabular foundation models.
- Context compression.
- Latent training-set summaries.
- Inference memory reduction.
- KV-cache feasibility.
- TabArena evaluation.

## Connections to Other Papers

Connects to EcoVLA, TetraJet-v2, LiftQuant, and hybrid sequence-model work through efficiency as a first-class capability constraint. It also links to retrieval/context-management themes in long-context systems.

## Notes for Cross-Paper Synthesis

TACO broadens the efficiency theme to tabular foundation models: when the context itself is large, compressing examples can matter as much as compressing parameters.
