# From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: S2Fd1GEyv6
- Authors: Lehui Li; Yuyao Wang; Jisheng Yan; Wei Zhang; Jinliang Deng; Haoliang Sun; Zhongyi Han; Yongshun Gong
- Primary area: applications->time_series
- Keywords: Time Series Forecasting; Multi Modal Time Series Analysis; Temporal learning
- Source URL: https://openreview.net/forum?id=S2Fd1GEyv6
- PDF URL: https://openreview.net/pdf?id=S2Fd1GEyv6

## Abstract

Incorporating textual information into time-series forecasting holds promise for addressing event- driven non-stationarity; however, a fundamental modality gap hinders effective fusion: textual descriptions express temporal impacts implicitly and qualitatively, whereas forecasting models rely on explicit and quantitative signals. Through controlled semi-synthetic experiments, we show that existing methods over-attend to redundant tokens and struggle to reliably translate textual semantics into usable numerical cues. To bridge this gap, we propose TESS, which introduces a Temporal Evolution Semantic Space as an intermediate bottleneck between modalities. This space consists of interpretable, numerically grounded temporal primitives—distribution shift, volatility, shape, and lag—extracted from text by an LLM via structured prompting and filtered through confidence-aware gating. Experiments on four real-world datasets demonstrate up to a 29% reduction in forecasting error compared to state-of-the-art unimodal and multimodal baselines. Code is available at: https://github.com/olivia3395/TESS.

## One-Sentence Claim

TESS improves text-informed time-series forecasting by translating qualitative text into interpretable numerical temporal primitives before fusion.

## Problem

Text can explain event-driven nonstationarity, but forecasting models need quantitative signals and existing multimodal methods over-attend to redundant tokens without reliably converting semantics into numerical cues.

## Core Contribution

The paper introduces a Temporal Evolution Semantic Space containing distribution shift, volatility, shape, and lag primitives extracted from text by structured LLM prompting and filtered with confidence-aware gating.

## Method

TESS uses an LLM to parse text into the temporal primitive space, treats that space as an intermediate bottleneck between language and numeric forecasting, and gates uncertain primitives before integrating them into forecasting models.

## Experiments and Evidence

The abstract reports controlled semi-synthetic experiments diagnosing redundant-token attention and four real-world datasets with up to 29% forecasting-error reduction versus state-of-the-art unimodal and multimodal baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: datasets, primitive extraction accuracy, confidence calibration, prompt sensitivity, event text quality, and whether the bottleneck loses useful open-ended context.

## Deep Themes

- Cross-modal forecasting needs semantic-to-numeric translation.
- Interpretable temporal primitives can bridge text and time series.
- Bottleneck representations reduce spurious token attention.

## Subthemes

- Time-series forecasting.
- Text-event conditioning.
- Temporal evolution primitives.
- LLM structured prompting.
- Confidence-aware gating.
- Nonstationarity.

## Connections to Other Papers

Connects to CoCLD, SDEVI, RED-HDP-HMM, and weather latent modeling through structured temporal representation and forecasting under irregular or shifting dynamics.

## Notes for Cross-Paper Synthesis

TESS adds a modality-translation theme: language is useful for forecasting only after being converted into task-native temporal variables.
