# SoftJAX & SoftTorch: Empowering Automatic Differentiation Libraries with Informative Gradients

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: RKHDV40omz
- Authors: Anselm Paulus; Andreas René Geist; Vít Musil; Sebastian Hoffmann; Georg Martius
- Primary area: general_machine_learning
- Keywords: Differentiable programming;Automatic differentiation;Software;Open-source libraries;Differentiable optimization;Relaxations;Straight-through estimation;Differentiable algorithms
- Source URL: https://openreview.net/forum?id=RKHDV40omz
- PDF URL: https://openreview.net/pdf?id=RKHDV40omz

## Abstract

Automatic differentiation (AD) frameworks such as JAX and PyTorch have enabled gradient-based optimization for a wide range of scientific fields. Yet, many ''hard'' primitives in these libraries such as thresholding, Boolean logic, discrete indexing, and sorting operations yield zero or undefined gradients that are not useful for optimization. While numerous ''soft'' relaxations have been proposed that provide informative gradients, the respective implementations are fragmented across projects, making them difficult to combine and compare. This work introduces **SoftJAX** and **SoftTorch**, open-source, feature-complete libraries for *soft differentiable programming*. These libraries provide a variety of soft functions as drop-in replacements for their hard JAX and PyTorch counterparts. This includes (i) elementwise operators such as *clip* or *abs*, (ii) utility methods for manipulating Booleans and indices via fuzzy logic, (iii) axiswise operators such as *sort* or *rank* -- based on optimal transport or permutahedron projections, and (iv) offer full support for straight-through gradient estimation. Overall, SoftJAX and SoftTorch make the toolbox of soft relaxations easily accessible to differentiable programming, as demonstrated through benchmarking and a practical case study. Code is available at github.com/a-paulus/softjax and github.com/a-paulus/softtorch.

## One-Sentence Claim

SoftJAX and SoftTorch provide drop-in soft relaxations for hard JAX/PyTorch primitives so differentiable programs can receive informative gradients through thresholding, logic, indexing, sorting, and ranking.

## Problem

Many useful programming primitives produce zero or undefined gradients, and existing soft-relaxation implementations are fragmented across projects, making them hard to combine and compare.

## Core Contribution

The paper introduces feature-complete open-source libraries for soft differentiable programming across JAX and PyTorch, including elementwise, Boolean/index, axiswise, optimal-transport, permutahedron, and straight-through tools.

## Method

The libraries expose soft functions as drop-in replacements for hard framework operations, supporting fuzzy logic for Boolean/index manipulation, differentiable sort/rank operators, and straight-through gradient estimation.

## Experiments and Evidence

The abstract reports benchmarking and a practical case study demonstrating accessibility and usefulness of the soft-relaxation toolbox.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: API coverage, numerical stability, gradient bias, performance overhead, supported devices, and how relaxations behave as temperatures approach hard limits.

## Deep Themes

- Differentiable programming needs software infrastructure, not just individual relaxations.
- Hard discrete operations can be made optimizable through carefully packaged soft surrogates.
- Library design can accelerate research by standardizing gradient estimators.

## Subthemes

- Automatic differentiation.
- Soft relaxations.
- JAX and PyTorch.
- Differentiable sorting/ranking.
- Straight-through estimation.
- Differentiable algorithms.

## Connections to Other Papers

Connects to optimization and systems papers by making gradient-based methods applicable to discrete or nonsmooth components, including ranking, selection, and algorithmic pipelines.

## Notes for Cross-Paper Synthesis

SoftJAX/SoftTorch add an infrastructure theme: some algorithmic ideas only become broadly usable when packaged as reliable primitives in the dominant autodiff stacks.
