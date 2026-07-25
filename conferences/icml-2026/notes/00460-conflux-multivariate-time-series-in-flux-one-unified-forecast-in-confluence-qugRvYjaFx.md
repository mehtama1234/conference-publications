# ConFlux: Multivariate Time Series in Flux, One Unified Forecast in Confluence

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: qugRvYjaFx
- Authors: Shiyu Wang; Juntong Ni; Ziyi Zhang; Baichuan Mo; Xinyue Zhong; Chengxin Wang; Yuchen Fang; Zhou Ye; Yang Xiang
- Primary area: applications->time_series
- Keywords: Multivariate Time Series;Foundation Model;Variate Sorting&Patching
- Source URL: https://openreview.net/forum?id=qugRvYjaFx
- PDF URL: https://openreview.net/pdf?id=qugRvYjaFx

## Abstract

Real-world multivariate time series are inherently in flux: different variables evolve asynchronously and interact in complex, time-varying ways, yet accurate forecasting requires these dispersed signals to converge into a single unified prediction.
This structural mismatch between dynamic, heterogeneous inputs and a unified forecasting objective poses a fundamental challenge for building general-purpose multivariate forecasting models, especially in zero-shot and large-scale settings. 
To this end, inspired by the idea that ``\emph{all rivers run into the sea}'', we propose \textbf{ConFlux}, a \emph{general-purpose foundation model for multivariate time-series forecasting} by learning to adaptively integrate cross-channel information under a unified forecasting objective. Specifically, ConFlux first reorders variables to reduce cross-variable entanglement, then aggregates adjacent variables into compact patches that can be processed by a Vision Transformer-style architecture. This design shortens the effective context, reduces attention complexity, and provides a unified token representation for pre-training and downstream tasks.
Experiments on 25 public datasets show that ConFlux achieves state-of-the-art performance in zero-shot, fine-tuning, and from-scratch settings, while offering faster inference and lower memory usage.

## One-Sentence Claim

ConFlux builds a multivariate time-series foundation model by sorting variables and patching adjacent channels into compact tokens, improving zero-shot, fine-tuned, and from-scratch forecasting with lower inference cost.

## Problem

Real multivariate time series contain variables that evolve asynchronously and interact in time-varying ways. Forecasting requires integrating these dispersed signals into one prediction, creating a mismatch between heterogeneous inputs and unified outputs.

General-purpose time-series foundation models must handle this structure across datasets, especially in zero-shot and large-scale settings, while controlling attention complexity and memory usage.

## Core Contribution

ConFlux proposes a foundation model for multivariate forecasting that adaptively integrates cross-channel information under a unified objective. It reorders variables to reduce cross-variable entanglement and aggregates adjacent variables into compact patches.

This patch representation lets a Vision Transformer-style architecture process multivariate time series with shorter effective context, lower attention complexity, and unified tokens for pretraining and downstream transfer.

## Method

The method first sorts variables so related or useful channels become adjacent, reducing entanglement across arbitrary input ordering. It then patches adjacent variables into compact channel groups, analogous to image patches but over variates.

These variate patches are fed into a ViT-style architecture. The design compresses cross-channel structure before attention, enabling scalable pretraining and efficient inference.

## Experiments and Evidence

The abstract reports experiments on 25 public datasets, with state-of-the-art performance in zero-shot, fine-tuning, and from-scratch settings. It also reports faster inference and lower memory usage.

Full-paper reading should verify dataset coverage, zero-shot split protocol, sorting criterion, patch-size sensitivity, architecture details, and whether gains hold for irregular sampling or missingness.

## Limits and Failure Modes

Variable sorting and patching may lose information if important interactions are nonlocal under the chosen order. Time-series domains with changing causal relationships, missing channels, or irregular timestamps may require additional machinery.

As with other foundation models, zero-shot claims depend heavily on pretraining corpus diversity and leakage controls across public benchmarks.

## Deep Themes

- Channel-structure compression: multivariate forecasting benefits from organizing variables before attention.
- Foundation models for time series: pretraining is moving beyond text/images into structured temporal domains.
- Unified objective for heterogeneous signals: dispersed channel dynamics are reconciled into one forecasting representation.
- Efficiency through patching: ViT-style tokenization reduces context and attention cost.

## Subthemes

- Variable ordering is a modeling decision, not incidental metadata.
- Adjacent-channel patches create a tractable cross-variate token space.
- Zero-shot forecasting is becoming a core benchmark for time-series FMs.
- Faster inference and lower memory are necessary for operational forecasting.

## Connections to Other Papers

ConFlux connects to TabSwift as a foundation model for non-text structured data. It also relates to DHSA and STAR-KV through attention-efficiency design, and to CoEvol-NO through long-sequence modeling over physical/temporal systems.

It fits the representation-geometry theme because the ordering and patching of variables defines what interactions are easy for the model to learn.

## Notes for Cross-Paper Synthesis

ConFlux shows structured-data foundation models borrowing architectural ideas from vision while adapting them to domain-specific structure. The broader pattern is tokenization as inductive bias: what becomes a token determines what the model can scale over efficiently.
