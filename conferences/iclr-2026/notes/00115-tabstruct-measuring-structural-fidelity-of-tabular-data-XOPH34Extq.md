# TabStruct: Measuring Structural Fidelity of Tabular Data

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: XOPH34Extq
- Authors: Xiangjian Jiang; Nikola Simidjievski; Mateja Jamnik
- Primary area: datasets and benchmarks
- Keywords: Tabular data;Tabular data structure;Synthetic data generation
- Source URL: https://openreview.net/forum?id=XOPH34Extq
- PDF URL: https://openreview.net/pdf?id=XOPH34Extq

## Abstract

Evaluating tabular generators remains a challenging problem, as the unique causal structural prior of heterogeneous tabular data does not lend itself to intuitive human inspection. Recent work has introduced structural fidelity as a tabular-specific evaluation dimension to assess whether synthetic data complies with the causal structures of real data. However, existing benchmarks often neglect the interplay between structural fidelity and conventional evaluation dimensions, thus failing to provide a holistic understanding of model performance. Moreover, they are typically limited to toy datasets, as quantifying existing structural fidelity metrics requires access to ground-truth causal structures, which are rarely available for real-world datasets. In this paper, we propose a novel evaluation framework that jointly considers structural fidelity and conventional evaluation dimensions. We introduce a new evaluation metric, global utility, which enables the assessment of structural fidelity even in the absence of ground-truth causal structures. In addition, we present TabStruct, a comprehensive evaluation benchmark offering large-scale quantitative analysis on 13 tabular generators from nine distinct categories, across 29 datasets. Our results demonstrate that global utility provides a task-independent, domain-agnostic lens for tabular generator performance. We release the TabStruct benchmark suite, including all datasets, evaluation pipelines, and raw results.

## One-Sentence Claim

TabStruct evaluates synthetic tabular generators by combining conventional metrics with structural fidelity, using global utility to assess causal-structure preservation without ground-truth graphs.

## Problem

Synthetic tabular data is hard to evaluate because heterogeneous tabular structure is not easily inspected by humans.

Structural fidelity is important because synthetic data should preserve causal relationships, but existing structural metrics often require ground-truth causal structures that are unavailable for real datasets.

## Core Contribution

The paper introduces TabStruct, a benchmark and evaluation framework for tabular generators.

It jointly considers structural fidelity and conventional evaluation dimensions, and proposes global utility as a task-independent, domain-agnostic metric for structural fidelity without ground-truth causal graphs.

## Method

TabStruct evaluates synthetic data along both standard utility dimensions and structural fidelity.

Global utility estimates whether generated data preserves useful relational structure by observing downstream behavior across tasks rather than requiring known causal structure.

## Experiments and Evidence

The abstract reports large-scale quantitative analysis of 13 tabular generators from nine categories across 29 datasets.

The authors release benchmark datasets, evaluation pipelines, and raw results, and find that global utility provides a holistic lens on tabular generator performance.

## Limits and Failure Modes

Global utility may conflate structural preservation with downstream model robustness or task choice. Without ground-truth causality, structural fidelity remains indirectly measured.

Because this note is abstract-only, details still need checking: global utility formula, conventional metrics included, dataset domains, generator categories, evaluation models, and correlation with known causal structures where available.

## Deep Themes

- Structural fidelity for synthetic data: tabular generators must preserve relationships, not only marginals or task accuracy.
- Evaluation without causal ground truth: metrics need proxies for real-world datasets.
- Holistic synthetic-data benchmarking: privacy, utility, distributional fit, and structure interact.
- Domain-agnostic tabular assessment: benchmark design must cover heterogeneous data types.

## Subthemes

- Synthetic tabular data.
- Global utility.
- Structural fidelity.
- Causal priors.

## Connections to Other Papers

This connects to PetaGAIL++, synthetic-data selection, data governance, and causal representation papers.

It also relates to Neural Effect Search because both address causal structure when ground truth is incomplete or expensive.

## Notes for Cross-Paper Synthesis

TabStruct adds a synthetic-data evaluation theme: generated data should be judged by whether it preserves latent structural relationships, not only by surface similarity.
