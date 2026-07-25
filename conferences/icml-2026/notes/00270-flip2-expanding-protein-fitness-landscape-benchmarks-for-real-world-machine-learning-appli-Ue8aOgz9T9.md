# FLIP2: Expanding Protein Fitness Landscape Benchmarks for Real-World Machine Learning Applications

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Ue8aOgz9T9
- Authors: Kieran Didi; Sarah Alamdari; Alex Xijie Lu; Bruce James Wittmann; Kadina E Johnston; Ava P Amini; Ali Madani; Maya Czeneszew; Christian Dallago; Kevin K Yang
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: protein engineering;machine learning;protein language models;benchmarks
- Source URL: https://openreview.net/forum?id=Ue8aOgz9T9
- PDF URL: https://openreview.net/pdf?id=Ue8aOgz9T9

## Abstract

Machine learning methods that predict protein fitness from sequence remain sensitive to changes in data distributions, limiting generalization across common conditions encountered in protein engineering. Practically, protein engineers are thus left wondering about the effective utility of ML tools. 
The FLIP benchmark established protocols for testing generalization under some domain shifts, but it was limited to measurements of stability, binding, and viral capsid viability.
We introduce FLIP2, a protein fitness benchmark spanning seven new datasets, including enzymes, protein-protein interactions, and light-sensitive proteins, as well as splits that measure generalization relevant to real-world protein engineering campaigns. 
Evaluating a suite of benchmark models across these datasets and suites reveals that
simpler models often matched or outperformed fine-tuned protein language models on FLIP2, challenging the utility of existing transfer learning techniques. Provenance for all datasets has been recorded and we redistribute all data CC-BY 4.0 to facilitate continued progress.

## One-Sentence Claim

FLIP2 expands protein fitness benchmarks to more realistic engineering shifts and finds that simple models often match or outperform fine-tuned protein language models.

## Problem

Protein fitness prediction is central to protein engineering, but ML models are sensitive to distribution shifts across assays, protein families, mutations, and campaign conditions. The original FLIP benchmark tested some generalization settings but covered limited task families such as stability, binding, and viral capsid viability.

Practitioners need benchmarks that better answer whether ML tools are useful under the shifts encountered in real protein engineering campaigns.

## Core Contribution

The paper introduces FLIP2, a benchmark with seven new datasets covering enzymes, protein-protein interactions, and light-sensitive proteins. It includes splits designed to measure generalization relevant to real-world engineering workflows.

The benchmark evaluation finds that simpler models often match or outperform fine-tuned protein language models, challenging current assumptions about transfer learning utility in protein fitness prediction.

## Method

FLIP2 is a benchmark and evaluation suite. It curates new protein fitness datasets, defines provenance, redistributes data under CC-BY 4.0, and evaluates a suite of models across generalization splits that reflect engineering-relevant distribution shifts.

The emphasis is not only dataset scale but split design: the benchmark asks whether models generalize in the ways protein engineers actually need.

## Experiments and Evidence

Evidence reported in the abstract:

- Seven new protein fitness datasets.
- Coverage of enzymes, protein-protein interactions, and light-sensitive proteins.
- Engineering-relevant generalization splits.
- Benchmark evaluation of multiple model classes.
- Simpler models often match or outperform fine-tuned protein language models.
- Dataset provenance recorded and data redistributed CC-BY 4.0.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: dataset sizes, split definitions, model suite, metrics, and whether protein LM fine-tuning was compute/hyperparameter matched.

## Limits and Failure Modes

- Benchmark conclusions depend strongly on split design and model tuning fairness.
- Seven datasets are broader than FLIP but still may not cover all engineering modalities.
- Simple-model strength may reflect dataset size, assay noise, or feature engineering rather than a general protein-LM limitation.
- Fitness measurements can be noisy and context-dependent.

## Deep Themes

**Benchmarks should encode deployment shifts.** FLIP2 measures generalization conditions relevant to protein engineering rather than only random held-out performance.

**Foundation models need domain-specific proof of utility.** Protein LMs are not assumed superior; they must beat simpler baselines under realistic shifts.

**Dataset provenance is part of benchmark quality.** Recording and licensing the data supports reproducibility and downstream progress.

## Subthemes

- Protein fitness landscape generalization.
- Engineering-relevant benchmark splits.
- Simple baselines versus protein language models.
- Dataset provenance and redistribution.
- Real-world utility of biological transfer learning.

## Connections to Other Papers

Connects to TD3B, Quantized Consistency Docking, and scientific ML papers focused on molecular or biological design. It also links to HypoSpace and evaluation papers because benchmark construction exposes where current models appear capable but fail under realistic distribution shifts.

## Notes for Cross-Paper Synthesis

FLIP2 reinforces a major evaluation pattern: benchmarks are becoming more adversarial to superficial progress by encoding realistic shifts, provenance, and stronger baseline comparisons.
