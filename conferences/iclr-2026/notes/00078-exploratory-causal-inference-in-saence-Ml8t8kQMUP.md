# Exploratory Causal Inference in SAEnce

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: Ml8t8kQMUP
- Authors: Tommaso Mencattini; Riccardo Cadei; Francesco Locatello
- Primary area: interpretability and explainable AI
- Keywords: Randomized Controlled Trials;Sparse Auto Encoder;Interpretability;Causal Inference
- Source URL: https://openreview.net/forum?id=Ml8t8kQMUP
- PDF URL: https://openreview.net/pdf?id=Ml8t8kQMUP

## Abstract

Randomized Controlled Trials are one of the pillars of science; nevertheless, they rely on hand-crafted hypotheses and expensive analysis. Such constraints prevent causal effect estimation at scale, potentially anchoring on popular yet incomplete hypotheses. We propose to discover the unknown effects of a treatment directly from data. For this, we turn unstructured data from a trial into meaningful representations via pretrained foundation models and interpret them via a Sparse Auto Encoder. However, discovering significant causal effects at the neural level is not trivial due to multiple-testing issues and effects entanglement. To address these challenges, we introduce _Neural Effect Search_, a novel recursive procedure solving both issues by progressive stratification. After assessing the robustness of our algorithm on semi-synthetic experiments, we showcase, in the context of experimental ecology, the first successful unsupervised causal effect identification on a real-world scientific trial.

## One-Sentence Claim

Neural Effect Search uses foundation-model representations and sparse autoencoders to discover causal treatment effects from unstructured randomized-trial data without hand-crafted hypotheses.

## Problem

Randomized controlled trials are powerful but usually depend on manually specified hypotheses and costly targeted analysis.

That bottleneck can miss unexpected treatment effects and over-focus analysis on popular or obvious hypotheses. Scaling causal discovery over unstructured trial data requires both representation learning and careful statistical control.

## Core Contribution

The paper proposes Neural Effect Search, a recursive procedure for exploratory causal effect identification in neural representations.

It turns unstructured trial data into foundation-model representations, interprets them with a sparse autoencoder, and handles multiple testing and effect entanglement via progressive stratification.

## Method

The pipeline embeds trial data with pretrained foundation models and learns interpretable sparse features using a sparse autoencoder.

Neural Effect Search recursively stratifies representation features to isolate significant effects while managing multiple comparisons and entangled neural factors.

## Experiments and Evidence

The abstract reports robustness checks on semi-synthetic experiments.

It also claims the first successful unsupervised causal effect identification on a real-world scientific trial in experimental ecology.

## Limits and Failure Modes

Exploratory causal discovery can surface statistically significant but scientifically fragile patterns. Sparse autoencoder features may not map cleanly to meaningful domain concepts, and multiple-testing control remains central.

Because this note is abstract-only, details still need checking: trial data modality, SAE architecture, statistical testing procedure, recursion stopping rule, semi-synthetic setup, and ecological finding validation.

## Deep Themes

- Foundation-model representations as scientific measurement: unstructured observations become analyzable causal variables.
- Exploratory causal inference: effect discovery expands beyond pre-registered human hypotheses.
- Sparse features as causal search units: interpretability tools become part of statistical discovery.
- Multiple-testing-aware representation mining: scaling discovery requires controlling false positives in high-dimensional feature spaces.

## Subthemes

- Randomized controlled trials.
- Sparse autoencoders.
- Neural Effect Search.
- Progressive stratification.

## Connections to Other Papers

This connects to AstaBench and scientific-agent work through AI-assisted scientific discovery.

It also relates to SAE-based data synthesis, interpretability-as-intervention papers, and causal identifiability work because it turns internal representations into objects for causal testing.

## Notes for Cross-Paper Synthesis

This paper adds a scientific-discovery pattern: interpretability methods are being repurposed as instruments for hypothesis generation and causal-effect search.
