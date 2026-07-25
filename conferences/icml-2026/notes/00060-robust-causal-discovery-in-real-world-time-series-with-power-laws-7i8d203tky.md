# Robust Causal Discovery in Real-World Time Series with Power-Laws

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7i8d203tky
- Authors: Matteo Tusoni; Giuseppe Masi; Andrea Coletta; Aldo Glielmo; Viviana Arrigoni; Novella Bartolini
- Primary area: general_machine_learning->causality
- Keywords: Causality;Causal Discovery;Time Series Analysis;Causal Inference from Time Series;Power-Law Processes
- Source URL: https://openreview.net/forum?id=7i8d203tky
- PDF URL: https://openreview.net/pdf?id=7i8d203tky

## Abstract

Exploring causal relationships in stochastic time series is a challenging yet crucial task with a vast range of applications, including finance, economics, neuroscience, and climate science. Many algorithms for Causal Discovery (CD) have been proposed; however, they often exhibit a high sensitivity to noise, resulting in spurious causal inferences on real data. In this paper, we observe that the frequency spectra of many real-world time series follow a power-law distribution, notably due to an inherent self-organizing behavior. Leveraging this insight, we build a robust CD method based on the extraction of power‑law spectral features that amplify genuine causal signals. Our method consistently outperforms state-of-the-art alternatives on both synthetic benchmarks and real-world datasets with known causal structures, demonstrating its robustness and practical relevance.

## One-Sentence Claim

Power-law spectral features make causal discovery in noisy real-world time series more robust by amplifying genuine causal signals and filtering spurious noise.

## Problem

Time-series causal discovery is sensitive to noise, non-stationarity, and spurious correlations, which are common in domains such as finance, neuroscience, climate, and economics.

## Core Contribution

The paper observes that many real-world time series have power-law frequency spectra and proposes PLaCy, a causal discovery method based on local power-law spectral features.

## Method

PLaCy segments time series into overlapping windows, fits power-law models to local frequency spectra, converts each original signal into spectral-parameter feature series, and applies causal discovery to those transformed features.

## Experiments and Evidence

The abstract reports consistent gains over state-of-the-art alternatives on synthetic benchmarks and real-world datasets with known causal structures.

## Full-Text Upgrade

The full text motivates the approach through scale-free temporal correlations and power-law frequency spectra observed in many real systems. Instead of analyzing raw time series, PLaCy extracts local spectral parameters such as amplitude and exponent, which serve as denoised feature trajectories for causal inference.

The theoretical statement argues that under additive non-dominating noise, local power-law approximation, and standard causal-discovery assumptions after transformation, causal discovery on spectral features is more robust than on original time-domain observations. Experiments include synthetic generalized Ornstein-Uhlenbeck processes with nonlinear, non-stationary, Brownian, and multiplicative noise, plus real-world datasets with known causal structure.

## Limits and Failure Modes

Limits to watch: the method assumes meaningful local power-law spectral structure; window size affects feature quality; causal discovery still depends on downstream assumptions after transformation; and domains without scale-free spectra may not benefit.

## Deep Themes

- Domain-specific spectral structure can improve causal discovery robustness.
- Transforming observations into better feature dynamics can beat raw time-domain inference.
- Power-law behavior is becoming a useful bridge between real-world stochastic processes and ML methods.

## Subthemes

- Time-series causal discovery.
- Power-law spectra.
- Spectral features.
- Noise robustness.
- Non-stationarity.
- Scale-free processes.

## Connections to Other Papers

Connects to LC-PB-SCM and Linear CRL through causal discovery under more realistic data assumptions, and to spectral-generalization papers through power-law/spectral structure.

## Notes for Cross-Paper Synthesis

This paper adds a spectral-causality theme: when raw observations are noisy, causal signal may be more visible in transformed spectral dynamics than in the original series.
