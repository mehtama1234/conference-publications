# Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ItJEC1Mk0V
- Authors: Peiyu Li; Xiuxiu Tang; Si Chen; Ying Cheng; Ronald Metoyer; Ting Hua; Nitesh V Chawla
- Primary area: general_machine_learning->evaluation
- Keywords: Adaptive testing;LLM evaluation
- Source URL: https://openreview.net/forum?id=ItJEC1Mk0V
- PDF URL: https://openreview.net/pdf?id=ItJEC1Mk0V

## Abstract

Evaluating large language models (LLMs) typically requires thousands of benchmark items, making the process expensive, slow, and increasingly impractical at scale. Existing evaluation protocols rely on average accuracy over fixed item sets, treating all items as equally informative despite substantial variation in difficulty and discrimination. We introduce ATLAS, an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information–guided item selection. ATLAS reduces the number of required items by up to 90% while maintaining measurement precision. For instance, it matches whole-bank ability estimates using only 41 items (0.157 MAE) on HellaSwag (5,600 items). We further reconstruct accuracy from ATLAS's ability estimates and find that reconstructed accuracies closely match raw accuracies across all five benchmarks, indicating that ability  preserves the global performance structure. At the same time,  provides finer discrimination within accuracy-equivalent models: among more than 3,000 evaluated models, 23--31% shift by more than 10 rank positions, and models with identical accuracies receive meaningfully different ability estimates. Code and calibrated item banks available at https://github.com/Peiyu-Georgia-Li/ATLAS.

## One-Sentence Claim

ATLAS uses item-response theory and Fisher-information-guided item selection to estimate LLM ability with far fewer benchmark questions than static evaluation.

## Problem

LLM evaluation is expensive and slow because static benchmarks require many items and treat questions as equally informative despite large differences in difficulty and discrimination.

## Core Contribution

The paper introduces a psychometric adaptive-testing framework for LLMs that estimates latent ability, reconstructs benchmark accuracy, and discriminates among models with similar raw accuracy.

## Method

ATLAS calibrates item banks with IRT, then adaptively selects high-Fisher-information items to estimate model ability. It compares ability estimates with whole-bank evaluations and reconstructs accuracy from the estimated ability parameter.

## Experiments and Evidence

The abstract reports up to 90% item reduction while preserving precision, including matching HellaSwag whole-bank ability estimates with 41 of 5,600 items at 0.157 MAE. Across five benchmarks, reconstructed accuracies closely match raw accuracies, while 23-31% of more than 3,000 models shift by over 10 rank positions relative to accuracy ties or near-ties.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: IRT model assumptions, item calibration stability, benchmark list, model sampling, robustness to contamination, and whether adaptive item exposure creates evaluation security issues.

## Deep Themes

- Evaluation as measurement theory rather than raw averaging.
- Adaptive testing can reduce evaluation cost while improving discrimination.
- Model ability may be a more stable object than benchmark accuracy.

## Subthemes

- LLM evaluation.
- Item Response Theory.
- Fisher information.
- Adaptive item selection.
- Benchmark efficiency.
- Rank instability under accuracy.

## Connections to Other Papers

Connects to Prescriptive Scaling and MemoryBench through evaluation efficiency and measurement validity. It also complements benchmark-contamination and capability-frontier papers by treating test items as calibrated instruments.

## Notes for Cross-Paper Synthesis

ATLAS strengthens the corpus's evaluation-modernization theme: as models proliferate, evaluation must become cheaper, adaptive, and more psychometrically grounded.
