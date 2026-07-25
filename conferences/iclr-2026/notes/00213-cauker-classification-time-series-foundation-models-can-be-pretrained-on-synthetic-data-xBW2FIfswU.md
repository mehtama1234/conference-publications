# CauKer: Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: xBW2FIfswU
- Authors: Shifeng Xie; Vasilii Feofanov; Jianfeng Zhang; Themis Palpanas; Ievgen Redko
- Primary area: learning on time series and dynamical systems
- Keywords: Time Series Foundation Model;Time Series Classification
- Source URL: https://openreview.net/forum?id=xBW2FIfswU
- PDF URL: https://openreview.net/pdf?id=xBW2FIfswU

## Abstract

Time series foundation models (TSFMs) have recently gained significant attention due to their strong zero-shot capabilities and widespread real-world applications. Such models typically require a computationally costly pretraining on large-scale, carefully curated collections of real-world sequences. To allow for a sample-efficient pretraining of TSFMs, we propose CauKer, a novel algorithm designed to generate diverse, causally coherent synthetic time series with realistic trends, seasonality, and nonlinear interactions. CauKer combines Gaussian Process (GP) kernel composition with Structural Causal Models (SCM) to produce data for sample-efficient pretraining of state-of-the-art classification TSFMs having different architectures and following different pretraining approaches. Additionally, our experiments reveal that CauKer-generated datasets exhibit clear scaling laws for both dataset size (10K to 10M samples) and model capacity (1M to 783M parameters), unlike real-world datasets, which display irregular scaling behavior.

## One-Sentence Claim

CauKer shows that time-series classification foundation models can be sample-efficiently pretrained on causally coherent synthetic data generated from GP kernel composition and structural causal models.

## Problem

Time-series foundation models usually need expensive pretraining on large, curated real-world sequence corpora. Real-world datasets can also show irregular scaling behavior, making it difficult to predict how dataset size and model capacity affect performance.

## Core Contribution

The paper contributes CauKer, a synthetic data generation algorithm for pretraining classification TSFMs. It produces diverse time series with realistic trends, seasonality, and nonlinear interactions, and reports clean scaling laws across dataset sizes and model capacities.

## Method

CauKer combines Gaussian Process kernel composition with Structural Causal Models. Kernel composition supplies flexible temporal structure such as trends and seasonality, while SCMs impose causal coherence and nonlinear interactions. The resulting generated datasets are used to pretrain time-series foundation models with different architectures and pretraining recipes.

## Experiments and Evidence

The abstract reports sample-efficient pretraining of state-of-the-art classification TSFMs across architectures and pretraining approaches. It also reports clear scaling laws for synthetic dataset sizes from 10K to 10M samples and model capacities from 1M to 783M parameters, contrasting with irregular scaling on real-world datasets.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should check downstream datasets, zero-shot versus fine-tuned performance, synthetic-to-real transfer, and whether GP/SCM assumptions cover discontinuities, rare events, nonstationarity, and measurement artifacts in deployed time-series systems. Synthetic scaling laws may be cleaner partly because the generator is simpler than the world.

## Deep Themes

- Synthetic data for foundation-model pretraining.
- Causal coherence in generated time series.
- Scaling-law regularity from controlled data generation.
- Sample-efficient pretraining.

## Subthemes

- Time-series classification.
- Gaussian Process kernel composition.
- Structural Causal Models.
- Trends, seasonality, and nonlinear interactions.
- Synthetic-to-real transfer.

## Connections to Other Papers

Connects to RealPDEBench through scientific and temporal modeling under sim-to-real constraints, to Complexa and mCLM through structured synthetic pretraining, and to the Intrinsic Entropy/Prism line through the question of what data structure makes scaling predictable.

## Notes for Cross-Paper Synthesis

CauKer shows a constructive version of data governance: instead of only curating real data, generate data with explicit causal and temporal structure. The cross-paper question is when synthetic structure clarifies scaling and when it hides real-world messiness.
