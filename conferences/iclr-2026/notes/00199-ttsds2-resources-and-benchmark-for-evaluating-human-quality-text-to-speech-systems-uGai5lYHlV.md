# TTSDS2: Resources and Benchmark for Evaluating Human-Quality Text to Speech Systems

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: uGai5lYHlV
- Authors: Christoph Minixhofer; Ondrej Klejch; Peter Bell
- Primary area: datasets and benchmarks
- Keywords: speech synthesis;distributional analysis;objective evaluation
- Source URL: https://openreview.net/forum?id=uGai5lYHlV
- PDF URL: https://openreview.net/pdf?id=uGai5lYHlV

## Abstract

Evaluation of Text to Speech (TTS) systems is challenging and resource-intensive. Subjective metrics such as Mean Opinion Score (MOS) are not easily comparable between works. Objective metrics are frequently used, but rarely validated against subjective ones. Both kinds of metrics are challenged by recent TTS systems capable of producing synthetic speech indistinguishable from real speech. In this work, we introduce Text to Speech Distribution Score 2 (TTSDS2), a more robust and improved version of TTSDS. Across a range of domains and languages, it is the only one out of 16 compared metrics to correlate with a Spearman correlation above 0.50 for every domain and subjective score evaluated. We also release a range of resources for evaluating synthetic speech close to real speech: A dataset with over 11,000 subjective opinion score ratings; a pipeline for recreating a multilingual test dataset to avoid data leakage; and a benchmark for TTS in 14 languages.

## One-Sentence Claim

TTSDS2 provides a validated distributional objective metric and multilingual resources for evaluating modern text-to-speech systems whose outputs approach human speech quality.

## Problem

TTS evaluation is costly because subjective MOS studies are hard to compare, while objective metrics are often insufficiently validated against human judgments. As synthetic speech approaches real speech quality, both subjective and objective metrics become harder to interpret.

## Core Contribution

The paper introduces Text to Speech Distribution Score 2, releases over 11,000 subjective opinion score ratings, provides a leakage-resistant multilingual test dataset recreation pipeline, and builds a benchmark for TTS in 14 languages.

## Method

TTSDS2 evaluates synthetic speech through distributional analysis and is validated against subjective scores across domains and languages. The benchmark compares it with 15 other metrics and supplies resources for recreating multilingual evaluation data.

## Experiments and Evidence

Across evaluated domains and languages, TTSDS2 is reportedly the only one of 16 metrics with Spearman correlation above 0.50 for every domain and subjective score evaluated.

## Limits and Failure Modes

Correlation above 0.50 is useful but not definitive for perceptual quality, and subjective scores vary by listener population, language, and recording condition. Full-text review should check domains, languages, metric formulation, confidence intervals, MOS collection protocol, and whether the recreation pipeline prevents benchmark leakage in practice.

## Deep Themes

- Objective evaluation for near-human TTS.
- Distributional speech quality metrics.
- Multilingual benchmark resources.
- Leakage-resistant evaluation pipelines.

## Subthemes

- TTSDS2.
- MOS correlation.
- Synthetic speech indistinguishability.
- 14-language TTS benchmark.
- Subjective-score dataset release.

## Connections to Other Papers

Connects to LST and speech-text modeling through speech evaluation, to FRABench/UFEval and other evaluator papers through objective metric validation, and to benchmark-governance work through leakage-resistant test construction.

## Notes for Cross-Paper Synthesis

TTSDS2 shows the evaluation gap that appears when generation quality approaches human quality: objective metrics need direct validation against subjective judgments across languages and domains.
