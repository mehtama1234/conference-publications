# $p\textrm{-less}$ Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ItFuNJQGH4
- Authors: Runyan Tan; Shuang Wu; Phillip Howard
- Primary area: probabilistic methods (Bayesian methods, variational inference, sampling, UQ, etc.)
- Keywords: LLM;decoding;sampling;truncation;inference;information-theoretic;information-theory;hyperparameterless;hyperparameter-free;entropy;entropy-aware;distribution-aware;adaptive;efficient;generation
- Source URL: https://openreview.net/forum?id=ItFuNJQGH4
- PDF URL: https://openreview.net/pdf?id=ItFuNJQGH4

## Abstract

Obtaining high-quality outputs from Large Language Models (LLMs) often depends upon the choice of a sampling-based decoding strategy to probabilistically choose the next token at each generation step. While a variety of such sampling methods have been proposed, their performance can be sensitive to the selection of hyperparameters which may require different settings depending upon the generation task and temperature configuration. In this work, we introduce $p\textrm{-less}$ sampling: an information-theoretic approach to sampling which dynamically sets a truncation threshold at each decoding step based on the entire token probability distribution. Unlike existing methods, $p\textrm{-less}$ sampling has no hyperparameters and consistently produces high-quality outputs as temperature increases. We provide theoretical perspectives on $p$-less sampling to ground our proposed method and conduct experiments to empirically validate its effectiveness across a range of math, logical reasoning, and creative writing tasks. Our results demonstrate how $p\textrm{-less}$ sampling consistently outperforms existing sampling approaches while exhibiting much less degradation in text quality at higher temperature values. We further show how $p$-less achieves greater inference-time efficiency than alternative methods through lower average token sampling times and shorter generation lengths, without sacrificing accuracy.
Finally, we provide analyses to highlight the benefits of $p\textrm{-less}$ through qualitative examples, case studies, and diversity assessments.

## One-Sentence Claim

p-less sampling adaptively truncates the next-token distribution from information-theoretic properties, removing decoding hyperparameters while improving robustness at high temperature.

## Problem

Sampling-based LLM decoding quality depends heavily on hyperparameters such as top-p, top-k, and temperature-related truncation settings.

Different tasks and temperatures require different settings, making decoding brittle and difficult to tune.

## Core Contribution

The paper introduces p-less sampling, a hyperparameter-free decoding method.

It dynamically sets a truncation threshold at every decoding step using the entire token probability distribution, with information-theoretic grounding.

## Method

p-less sampling examines the full next-token distribution and computes an adaptive truncation threshold rather than using a fixed p or k.

The method changes as entropy and distribution shape change across decoding steps, making it distribution-aware and temperature-robust.

## Experiments and Evidence

The abstract reports better performance than existing sampling approaches across math, logical reasoning, and creative writing tasks.

It degrades less at higher temperatures, has lower average token sampling times, and produces shorter generations without sacrificing accuracy.

## Limits and Failure Modes

Hyperparameter-free does not mean universally optimal; adaptive truncation may still mis-handle specialized domains, calibration errors, or tasks requiring unusual diversity.

Because this note is abstract-only, details still need checking: theoretical criterion, models tested, decoding baselines, temperature ranges, diversity metrics, and latency measurement.

## Deep Themes

- Distribution-aware decoding: sampling should respond to the full probability shape.
- Hyperparameter removal: robust defaults reduce deployment tuning burden.
- Entropy as inference signal: uncertainty structure controls generation breadth.
- Efficiency through adaptive truncation: better sampling can also shorten outputs and reduce latency.

## Subthemes

- Hyperparameter-free truncation.
- High-temperature robustness.
- Math/reasoning/creative-writing decoding.
- Token sampling efficiency.

## Connections to Other Papers

This connects to ASAG, coverage theory, EntroKV, and ThinkV through inference-time control based on internal distributional signals.

It also relates to p-less-like test-time scaling and decoding strategies in reasoning models.

## Notes for Cross-Paper Synthesis

p-less sampling adds to the adaptive-inference theme: decoding quality can improve when thresholds are derived from the model's own uncertainty rather than fixed knobs.
