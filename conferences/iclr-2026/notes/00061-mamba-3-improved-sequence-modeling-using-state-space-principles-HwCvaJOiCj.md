# Mamba-3: Improved Sequence Modeling using State Space Principles

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: HwCvaJOiCj
- Authors: Aakash Lahoti; Kevin Li; Berlin Chen; Caitlin Wang; Aviv Bick; J Zico Kolter; Tri Dao; Albert Gu
- Primary area: foundation or frontier models, including LLMs
- Keywords: State Space Models;Mamba;LLMs;Subquadratic Models
- Source URL: https://openreview.net/forum?id=HwCvaJOiCj
- PDF URL: https://openreview.net/pdf?id=HwCvaJOiCj

## Abstract

The recent scaling of test-time compute for LLMs has restricted the practical deployment of models to those with strong capabilities that can generate high-quality outputs in an inference-efficient manner. While current Transformer-based models are the standard, their quadratic compute and linear memory bottlenecks have spurred the development of sub-quadratic models with linear-scaling compute with constant memory requirements. However, many recent linear-style models lack certain capabilities or lag behind in quality, and even their linear-time inference is not hardware-efficient. Guided by an inference-first perspective, we introduce three core methodological improvements inspired by the state-space model viewpoint of linear models. We combine a: 1) more expressive recurrence, 2) complex state update rule that enables richer state tracking, and 3) multi-input, multi-output formulation together, resulting in a stronger model that better exploits hardware parallelism during decoding. Together with architectural refinements, our **Mamba-3** model achieves significant gains across retrieval, state-tracking, and downstream language modeling tasks. Our new architecture sets the Pareto-frontier for performance under a fixed inference budget and outperforms strong baselines in a head-to-head comparison.

## One-Sentence Claim

Mamba-3 improves subquadratic sequence modeling by using richer state-space recurrence, complex state updates, and multi-input/multi-output structure optimized for inference efficiency.

## Problem

Transformer inference is limited by quadratic compute and linear memory, especially as test-time compute grows. Linear-style models promise better scaling but often lag in capability or are not hardware-efficient in practice.

The problem is to build a subquadratic model that is both capable and efficient under real decoding budgets.

## Core Contribution

The paper introduces Mamba-3, an inference-first state-space architecture.

It combines a more expressive recurrence, a complex state update rule for richer state tracking, and a multi-input/multi-output formulation, plus architectural refinements that better exploit hardware parallelism during decoding.

## Method

Mamba-3 rethinks linear sequence models from a state-space perspective. The recurrence is made more expressive, the state update is complex-valued or complex-structured, and multiple inputs/outputs are handled jointly.

The design targets the performance/inference-budget Pareto frontier rather than only asymptotic complexity.

## Experiments and Evidence

The abstract reports significant gains on retrieval, state-tracking, and downstream language modeling tasks.

Mamba-3 sets a new Pareto frontier under fixed inference budget and outperforms strong baselines head-to-head.

## Limits and Failure Modes

State-space models may still struggle with tasks that benefit from explicit all-pairs attention or long-range associative retrieval unless recurrence captures the needed state.

Because this note is abstract-only, details still need checking: model sizes, recurrence equations, hardware benchmarks, comparison baselines, training data, and long-context failure modes.

## Deep Themes

- Inference-first architecture design: deployment budgets shape model architecture.
- State tracking as sequence modeling primitive: recurrence is upgraded rather than discarded.
- Hardware-aware subquadratic modeling: linear-time theory must translate to efficient kernels.
- Pareto-frontier thinking: models are judged by quality under fixed inference cost.

## Subthemes

- State-space models.
- Complex state updates.
- Multi-input/multi-output recurrence.
- Retrieval and state-tracking tasks.

## Connections to Other Papers

This connects to Mamba/Mamba-2 work, Rational Transductors, softmax Turing-completeness, and transformer accessible sequence bounds through alternatives to standard attention.

It also relates to EntroKV, FlashVID, and ThinkV because all target inference efficiency under long contexts or high token loads.

## Notes for Cross-Paper Synthesis

Mamba-3 contributes to the inference-efficient foundation model theme: the next architecture race is not only accuracy, but accuracy per decoding budget.
