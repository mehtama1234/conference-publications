# Learning-to-Optimize via Deep Unfolded Flows

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ZOtOq7hxJP
- Authors: Augustinos D Saravanos; Oswin So; H M Sabbir Ahmad; Chuchu Fan
- Primary area: optimization->nonconvex
- Keywords: learning-to-optimize;deep unfolding;non-convex optimization;generative models;sampling-based optimization
- Source URL: https://openreview.net/forum?id=ZOtOq7hxJP
- PDF URL: https://openreview.net/pdf?id=ZOtOq7hxJP

## Abstract

We introduce *FlowOptimizer*, a deep unfolded, flow-based framework for learned iterative optimization. Motivated by the expressiveness of flow models, we represent each optimization iteration via a velocity field that operates on a population of candidate solutions, i.e., a set of parallel iterates, conditioned on contextual information including their objective values and gradients, as well as population-level statistics. The velocity field is initially trained in a simulation-free manner by matching displacements from source populations to improved target ones obtained through sampling the objective. Subsequently, we unfold this velocity field as the internal iteration of an optimization sequence, and fine-tune it in an end-to-end manner by directly optimizing objective values over a targeted class of problems. Notably, FlowOptimizer is a self-supervised framework whose training relies solely on objective evaluations without requiring knowledge of solutions. We evaluate our approach on a series of tasks from standard non-convex optimization benchmarks to real-world problems from supply chain, robotics and power grid applications. FlowOptimizer consistently outperforms well-established sampling-based/gradient-based traditional optimization and learning-to-optimize methods, often by orders of magnitude in terms of solution quality. We further highlight its ability to be trained on low-dimensional problems and successfully generalize to substantially higher-dimensional $(\times 10)$ ones.

## One-Sentence Claim

FlowOptimizer learns iterative optimization as unfolded flow dynamics over populations of candidate solutions, trained only from objective evaluations and transferable to higher dimensions.

## Problem

Learning-to-optimize aims to replace hand-designed optimization routines with learned update rules, but non-convex problems vary widely and often lack labeled optimal solutions. Sampling-based and gradient-based traditional methods can be slow or low-quality on difficult real-world objectives.

The paper asks whether flow models can represent population-based iterative optimization steps and learn from objective evaluations alone.

## Core Contribution

The paper introduces FlowOptimizer, a deep unfolded flow-based optimizer. Each iteration is represented as a velocity field over a population of candidate solutions, conditioned on objective values, gradients, and population statistics.

Training has two stages: simulation-free displacement matching from source populations to improved target populations sampled from the objective, then end-to-end fine-tuning by unfolding the velocity field and directly optimizing objective values. It needs no known solutions.

## Method

FlowOptimizer maintains parallel candidate solutions. A learned velocity field moves the population toward better regions using local and population-level context. Initial training learns improvement displacements from sampled objective evaluations; fine-tuning optimizes the unrolled sequence's final objective.

The framework is self-supervised because the objective itself supplies feedback.

## Experiments and Evidence

Evidence reported in the abstract:

- Standard non-convex optimization benchmarks.
- Real-world supply chain, robotics, and power-grid tasks.
- Outperforms sampling-based, gradient-based, and learning-to-optimize baselines, often by orders of magnitude in solution quality.
- Trained on low-dimensional problems and generalized to dimensions 10x larger.
- Uses only objective evaluations, without solution labels.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmark definitions, objective-evaluation budgets, gradient availability, dimension-transfer protocol, and runtime.

## Limits and Failure Modes

- Learned optimizers may overfit objective families seen during training.
- Objective evaluations can still be expensive in real systems.
- Orders-of-magnitude gains require careful budget normalization.
- Using gradients limits applicability if some black-box tasks provide only function values.

## Deep Themes

**Optimization can be learned as flow dynamics.** Iterative updates are represented by a velocity field over a population.

**Population context is an optimization signal.** Candidate sets carry statistics that guide better movement than isolated iterates.

**Self-supervision from objectives reduces label dependence.** The optimizer learns from improvement, not known optima.

## Subthemes

- Deep unfolded optimizers.
- Flow-based velocity fields.
- Population-based candidate updates.
- Simulation-free displacement matching.
- Dimension generalization in optimization.

## Connections to Other Papers

Connects to Flow Sampling, Deep Flow Networks, PAVE, and BCO Gradient Variation through field/flow views of optimization. It also links to DiBO and offline BBO because both turn design improvement into a learned generative or iterative process.

## Notes for Cross-Paper Synthesis

FlowOptimizer reinforces the batch-level pattern that flows are becoming a general computational metaphor: approximate functions, sample energy targets, control neurons, and optimize black-box objectives.
