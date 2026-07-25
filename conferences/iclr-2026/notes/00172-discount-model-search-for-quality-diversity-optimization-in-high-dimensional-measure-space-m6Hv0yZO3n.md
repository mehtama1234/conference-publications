# Discount Model Search for Quality Diversity Optimization in High-Dimensional Measure Spaces

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: m6Hv0yZO3n
- Authors: Bryon Tjanaka; Henry Chen; Matthew Christopher Fontaine; Stefanos Nikolaidis
- Primary area: optimization
- Keywords: quality diversity optimization;black-box optimization;derivative-free optimization;latent space exploration
- Source URL: https://openreview.net/forum?id=m6Hv0yZO3n
- PDF URL: https://openreview.net/pdf?id=m6Hv0yZO3n

## Abstract

Quality diversity (QD) optimization searches for a collection of solutions that optimize an objective while attaining diverse outputs of a user-specified, vector-valued measure function. Contemporary QD algorithms are typically limited to low-dimensional measures because high-dimensional measures are prone to distortion, where many solutions found by the QD algorithm map to similar measures. For example, the state-of-the-art CMA-MAE algorithm guides measure space exploration with a histogram in measure space that records so-called discount values. However, CMA-MAE stagnates in domains with high-dimensional measure spaces because solutions with similar measures fall into the same histogram cell and hence receive the same discount value. To address these limitations, we propose Discount Model Search (DMS), which guides exploration with a model that provides a smooth, continuous representation of discount values. In high-dimensional measure spaces, this model enables DMS to distinguish between solutions with similar measures and thus continue exploration. We show that DMS facilitates new capabilities for QD algorithms by introducing two new domains where the measure space is the high-dimensional space of images, which enables users to specify their desired measures by providing a dataset of images rather than hand-designing the measure function. Results in these domains and on high-dimensional benchmarks show that DMS outperforms CMA-MAE and other existing black-box QD algorithms.

## One-Sentence Claim

DMS replaces histogram-based QD discounting with a smooth discount model, enabling quality-diversity search in high-dimensional measure spaces such as image-defined behavior spaces.

## Problem

Quality-diversity optimization aims to find many high-performing, behaviorally diverse solutions, but existing algorithms usually assume low-dimensional measure spaces. In high-dimensional spaces, histogram cells distort similarity, collapse many solutions into the same bucket, and cause methods like CMA-MAE to stagnate.

## Core Contribution

The paper introduces Discount Model Search, which models discount values continuously rather than through a fixed histogram. It also introduces new QD domains where users specify desired measures by providing image datasets instead of hand-designing low-dimensional measure functions.

## Method

DMS learns or fits a smooth model over measure space that estimates discount values for exploration. Because this representation is continuous, it can distinguish nearby but meaningfully different high-dimensional measures and continue searching where histogram discretization would merge them.

## Experiments and Evidence

The abstract reports that DMS outperforms CMA-MAE and other black-box QD algorithms on high-dimensional benchmarks and in two new image-measure domains.

## Limits and Failure Modes

The discount model may introduce its own approximation bias and may be hard to train in very sparse, noisy, or semantically ambiguous measure spaces. Image-defined measures raise questions about representation choice and user intent. Full-text review should check model architecture, update rules, high-dimensional benchmarks, ablations against finer histograms, and compute overhead.

## Deep Themes

- Continuous models for exploration pressure.
- Quality diversity in high-dimensional behavior spaces.
- User-specified measures through data.
- Black-box optimization beyond handcrafted descriptors.

## Subthemes

- Discount-value modeling.
- Histogram distortion in QD.
- Image-based measure spaces.
- Derivative-free latent exploration.
- Diversity search under representation pressure.

## Connections to Other Papers

Connects to AutoEP through adaptive search control, to ExDM through learned density/exploration signals, and to embedding/retrieval papers where continuous representation quality determines whether similar states can be distinguished.

## Notes for Cross-Paper Synthesis

DMS reflects a larger pattern: discrete bookkeeping fails when behavior spaces become high-dimensional, so optimization needs learned continuous surrogates that preserve useful distinctions.
