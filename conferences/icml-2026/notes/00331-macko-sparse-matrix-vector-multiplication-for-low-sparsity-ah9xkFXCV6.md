# MACKO: Sparse matrix-vector multiplication for low sparsity

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ah9xkFXCV6
- Authors: Vladimír Macko; Vladimír Boža
- Primary area: general_machine_learning->hardware_and_software
- Keywords: sparse matrix vector multiplication;unstructured sparsity;efficient LLM inference;pruning;gemv;gpu kernel
- Source URL: https://openreview.net/forum?id=ah9xkFXCV6
- PDF URL: https://openreview.net/pdf?id=ah9xkFXCV6

## Abstract

Sparse Matrix-Vector Multiplication (SpMV) is a fundamental operation in the inference of sparse Large Language Models (LLMs).
Because existing SpMV methods perform poorly under the low, unstructured sparsity ($30-90\\%$) commonly observed in pruned LLMs, unstructured pruning provides only limited memory reduction and speedup.
We propose **MACKO-SpMV**, a GPU-optimized format and kernel co-designed to reduce storage overhead while remaining compatible with the GPU’s execution model.
This enables efficient SpMV for unstructured sparsity without specialized hardware units or precomputation.
We identify memory bandwidth as the primary limiting factor of SpMV and analyze the storage overhead of MACKO.
At $50\\%$ sparsity, MACKO is the first approach to achieve $1.5\times$ memory reduction and $1.2-1.5\times$ speedup over the dense baseline as well as substantial improvements over other SpMV methods: cuSPARSE ($2.8-13.0\times$), Sputnik ($1.9-2.6\times$), and DASP ($2.2-2.5\times$).
An LLM pruned with Wanda to sparsity $50\\%$ requires $1.5\times$ less memory and achieves $1.5\times$ faster inference at fp16 precision.
As a result, **unstructured pruning at $50\\%$ sparsity becomes practical** for real-world LLM workloads and **bridges the efficiency gap with structured 2:4 sparsity**.

## One-Sentence Claim

MACKO-SpMV makes 50 percent unstructured LLM pruning practical by co-designing a GPU sparse format and kernel that reduce memory bandwidth overhead enough to beat dense inference.

## Problem

Sparse matrix-vector multiplication is central to sparse LLM inference, but existing SpMV methods perform poorly at the low, unstructured sparsity levels typical of pruned LLMs. At 30-90 percent sparsity, storage overhead and GPU execution mismatch often erase the memory and speed benefits.

The paper asks how to support practical unstructured pruning without specialized hardware or expensive precomputation.

## Core Contribution

The paper proposes MACKO-SpMV, a GPU-optimized sparse format and kernel designed around memory bandwidth and GPU execution. At 50 percent sparsity, it achieves 1.5x memory reduction and 1.2-1.5x speedup over dense baselines, with larger speedups over cuSPARSE, Sputnik, and DASP.

Applied to a Wanda-pruned LLM at 50 percent sparsity, it gives 1.5x less memory and 1.5x faster fp16 inference, narrowing the gap with structured 2:4 sparsity.

## Method

MACKO co-designs storage layout and GPU kernel behavior for unstructured sparse GEMV. The format reduces index/storage overhead while keeping memory access and parallel execution compatible with GPU hardware.

The analysis identifies memory bandwidth as the primary bottleneck and optimizes the sparse representation around it.

## Experiments and Evidence

Evidence reported in the abstract:

- Targets low unstructured sparsity from 30-90 percent.
- At 50 percent sparsity: 1.5x memory reduction and 1.2-1.5x speedup over dense.
- Speedups over cuSPARSE of 2.8-13.0x, Sputnik of 1.9-2.6x, and DASP of 2.2-2.5x.
- Wanda-pruned LLM at 50 percent sparsity runs 1.5x faster with 1.5x less memory at fp16.
- No specialized hardware units or precomputation required.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: GPU models, matrix sizes, batch sizes, pruning patterns, and end-to-end LLM benchmark setup.

## Limits and Failure Modes

- Sparse benefits may depend on batch size and memory-bandwidth regime.
- 50 percent unstructured sparsity may still require careful accuracy-preserving pruning.
- Kernel advantages may be hardware-specific.
- Integration into common inference stacks may need custom kernel support.

## Deep Themes

**Sparse inference lives or dies by memory format.** Pruning alone is insufficient unless the sparse representation maps to GPU bandwidth constraints.

**Unstructured sparsity can be practical with the right kernel.** MACKO challenges the assumption that only structured sparsity is deployable.

**Efficiency is a co-design problem.** Model pruning, storage layout, and GPU execution must be optimized together.

## Subthemes

- Sparse LLM inference.
- Low unstructured sparsity.
- GPU SpMV kernel design.
- Memory-bandwidth bottlenecks.
- Wanda-pruned LLM deployment.

## Connections to Other Papers

Connects to FlashOptim, FlashSinkhorn, WBMM, ReQAT, and WeDLM through hardware-aware efficiency. It also links to FeatJND and compression work because model-size reduction must preserve task behavior and map to real speed.

## Notes for Cross-Paper Synthesis

MACKO adds a hardware reality check to sparsity: algorithmic compression only matters when the resulting representation makes accelerator memory movement cheaper.
