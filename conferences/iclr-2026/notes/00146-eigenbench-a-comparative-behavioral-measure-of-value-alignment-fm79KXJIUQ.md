# EigenBench: A Comparative Behavioral Measure of Value Alignment

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: fm79KXJIUQ
- Authors: Jonathn Chang; Leonhard Piff; Suvadip Sana; Jasmine Xinze Li; Lionel Levine
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: value alignment;Bradley-Terry model;EigenTrust;model disposition;constitutional AI
- Source URL: https://openreview.net/forum?id=fm79KXJIUQ
- PDF URL: https://openreview.net/pdf?id=fm79KXJIUQ

## Abstract

Aligning AI with human values is a pressing unsolved problem. To address the lack of quantitative metrics for value alignment, we propose EigenBench: a black-box method for comparatively benchmarking language models’ values. Given an ensemble of models, a constitution describing a value system, and a dataset of scenarios, our method returns a vector of scores quantifying each model’s alignment to the given constitution. To produce these scores, each model judges the outputs of other models across many scenarios, and these judgments are aggregated with EigenTrust (Kamvar et al., 2003), yielding scores that reflect a weighted consensus judgment of the whole ensemble. EigenBench uses no ground truth labels, as it is designed to quantify subjective traits for which reasonable judges may disagree on the correct label. Hence, to validate our method, we collect human judgments on the same ensemble of models and show that EigenBench’s judgments align closely with those of human evaluators. We further demonstrate that EigenBench can recover model rankings on the GPQA benchmark without access to objective labels, supporting its viability as a framework for evaluating subjective values for which no ground truths exist.

## One-Sentence Claim

EigenBench benchmarks subjective value alignment by having models judge each other's outputs under a constitution and aggregating those judgments with EigenTrust.

## Problem

Value alignment lacks quantitative black-box metrics, especially for subjective traits where reasonable judges may disagree and no objective ground-truth label exists.

Traditional benchmarks with fixed correct answers are poorly suited to measuring whether models align with a specified constitution or value system.

## Core Contribution

The paper introduces EigenBench, a comparative behavioral benchmark for model values.

Given models, scenarios, and a constitution, it returns alignment scores by aggregating peer judgments from the model ensemble using EigenTrust.

## Method

Each model judges outputs from other models across scenarios. EigenTrust aggregates those judgments into a weighted consensus score for each model.

The method is black-box and label-free, making it applicable to subjective alignment dimensions where human labels are costly or contested.

## Experiments and Evidence

The abstract reports validation against human judgments on the same model ensemble, with close alignment between EigenBench and human evaluators.

It also recovers GPQA model rankings without objective labels, suggesting the framework can sometimes infer useful rankings from comparative judgments.

## Limits and Failure Modes

Model-judged consensus can amplify shared model biases or collusion-like correlations. The result depends on the ensemble composition, scenario distribution, and constitution phrasing.

Because this note is abstract-only, details still need checking: constitution design, scenario dataset, EigenTrust graph construction, human-evaluation protocol, and robustness to biased judges.

## Deep Themes

- Subjective alignment measurement: not every important value judgment has ground-truth labels.
- Model ensembles as evaluators: peer judgments can form a comparative behavioral signal.
- Constitution-conditioned scoring: alignment is measured relative to explicit value statements.
- Consensus risk: benchmark quality depends on whether model judges approximate human pluralism or shared artifacts.

## Subthemes

- Value alignment.
- EigenTrust aggregation.
- Black-box behavioral benchmarking.
- Constitutional evaluation.

## Connections to Other Papers

This connects to deception measurement, SafeDPO, micro-benchmarking reliability, Train-before-Test, and social-learning control.

It also relates to AstaBench and OpenApps because all evaluate systems where no single scalar answer is enough.

## Notes for Cross-Paper Synthesis

EigenBench adds a value-measurement theme: alignment evaluation is moving toward comparative, constitution-conditioned judgments when objective labels are unavailable.
