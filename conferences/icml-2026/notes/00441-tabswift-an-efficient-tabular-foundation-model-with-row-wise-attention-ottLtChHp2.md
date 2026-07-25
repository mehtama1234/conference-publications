# TabSwift: An Efficient Tabular Foundation Model with Row-Wise Attention

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ottLtChHp2
- Authors: Si-Yang Liu; Han-Jia Ye
- Primary area: deep_learning->foundation_models
- Keywords: Foundation model;tabular data
- Source URL: https://openreview.net/forum?id=ottLtChHp2
- PDF URL: https://openreview.net/pdf?id=ottLtChHp2

## Abstract

Tabular foundation models, exemplified by TabPFN, perform prediction via in-context learning, inferring test labels directly from labeled training examples. They have demonstrated competitive performance, particularly on small-to-medium datasets. However, recent tabular foundation models often improve accuracy with increasingly complex architectures, incurring higher inference cost and limiting practical deployment.
In this work, we revisit the original TabPFN design and show that a lightweight row-wise attention–only backbone can remain highly competitive with two simple enhancements: a gated attention stabilization mechanism and a small set of learnable register tokens that provide global context and improve pretraining quality.
The resulting model, TabSwift, supports both classification and regression, and is competitive with stronger tabular foundation models (e.g., TabPFN v2 and TabICL) while being more efficient at inference.
For latency-sensitive serving, we further introduce an adaptive layer-wise early-exit mechanism that dynamically adjusts inference depth per sample.
Overall, TabSwift enables efficient and anytime tabular in-context learning for practical deployments.

## One-Sentence Claim

TabSwift shows that tabular in-context learning can stay competitive with complex tabular foundation models using a lightweight row-wise attention backbone, stabilization, register tokens, and adaptive early exit.

## Problem

Tabular foundation models such as TabPFN perform prediction by conditioning on labeled examples at inference time, which is attractive for small and medium datasets. But newer models often chase accuracy with increasingly complex architectures, raising inference cost and limiting latency-sensitive deployment.

The practical problem is to keep the benefits of tabular in-context learning while reducing the serving burden. For tabular workloads, fast per-sample prediction and anytime behavior can matter as much as top-line benchmark accuracy.

## Core Contribution

The paper revisits the original TabPFN design and argues that a row-wise attention-only backbone can remain highly competitive when equipped with gated attention stabilization and learnable register tokens for global context.

It also adds adaptive layer-wise early exit, allowing inference depth to vary by sample. The contribution is therefore both architectural and operational: simplify the backbone, stabilize training/pretraining, and expose a latency-accuracy control at inference time.

## Method

TabSwift uses row-wise attention rather than heavier tabular foundation-model architectures. Gated attention stabilizes the attention computation, while a small set of learned register tokens acts as a global context buffer that improves pretraining quality.

For serving, the model uses adaptive early exit across layers. Easier samples can exit earlier, while harder ones can use more depth, creating an anytime predictor for classification and regression.

## Experiments and Evidence

The abstract reports that TabSwift is competitive with stronger tabular foundation models such as TabPFN v2 and TabICL while being more efficient at inference. It supports both classification and regression and targets practical deployment through latency-sensitive early exits.

Full-paper inspection should verify benchmark suites, calibration of early-exit confidence, latency measurements, regression/classification balance, and whether efficiency gains persist under larger context sizes.

## Limits and Failure Modes

A lightweight row-wise backbone may underfit tasks requiring richer feature interactions, complex missingness handling, or very large in-context training sets. Early exit can also create miscalibrated predictions if the exit criterion mistakes confidence for correctness.

The method's deployment value depends on hardware, batch sizes, and data preprocessing assumptions. Tabular datasets vary widely, so robustness across schema types and distribution shifts is important.

## Deep Themes

- Efficient foundation models for structured data: tabular FM design is moving toward deployability, not just accuracy.
- Minimal architecture plus stabilizers: simpler backbones can compete when the right small mechanisms are added.
- Anytime inference: dynamic depth gives users a latency-accuracy tradeoff.
- Register tokens as global context: small learned memory slots improve in-context tabular prediction.

## Subthemes

- Row-wise attention is a deliberate simplification of tabular in-context learning.
- Classification and regression support broadens practical relevance.
- Early exit turns model depth into a per-example resource decision.
- Efficiency is especially important for high-volume tabular serving.

## Connections to Other Papers

TabSwift connects to DHSA, STAR-KV, NorMuon, and MoE compression as part of the efficiency-as-capability cluster. It differs by focusing on tabular foundation models, where deployment is often latency-sensitive and datasets are smaller.

It also relates to XDLM in this batch: both revisit an existing foundation-model paradigm and find a more balanced point on a performance-efficiency frontier.

## Notes for Cross-Paper Synthesis

TabSwift reinforces a cross-corpus theme that foundation-model progress is no longer only about scale. In mature application domains, the frontier includes lower latency, adaptive computation, and simpler architectures that retain most capability.
