# CONTINUUM: Restoring the Contiguous Tensor Abstraction Efficiently for Dynamic AI Workloads via Hardware Virtualization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: hROxrfMoXj
- Authors: Yangyu Zhang; Shuoming Zhang; Chunwei Xia; Shuaijiang Li; Zhicheng Li; Ruiyuan Xu; Zheming Yang; Lei Chen; YUAN WEN; Guangli Li; Xiaobing Feng; Huimin Cui; Jiacheng Zhao
- Primary area: general_machine_learning->hardware_and_software
- Keywords: ML System;AI Infrastructure;GPU Driver
- Source URL: https://openreview.net/forum?id=hROxrfMoXj
- PDF URL: https://openreview.net/pdf?id=hROxrfMoXj

## Abstract

Emerging LLM workloads demand extreme memory agility. However, state-of-the-art inference systems such as vLLM rely on software-defined paging, which sacrifices the contiguous tensor abstraction. This rigid interface exposes fragmentation complexity to developers, imposing a severe engineering burden that stifles algorithmic innovation. We introduce CONTINUUM, a tensor memory virtualization subsystem implemented as a PyTorch extension. By bypassing serialized OS bottlenecks through a lightweight GPU driver extension, CONTINUUM significantly reduces mapping costs by orders of magnitude, from milliseconds to microseconds. Built atop this low-latency API, CONTINUUM provides Elastic Tensor, a set of flexible tensor operations that natively support complex memory dynamics and zero-copy topological aliasing. Evaluations demonstrate that CONTINUUM achieves significantly higher throughput across diverse dynamic scenarios, effectively lowering the barrier to implementing next-generation LLM applications.

## One-Sentence Claim

CONTINUUM restores a flexible contiguous-tensor abstraction for dynamic LLM workloads by virtualizing tensor memory with low-latency GPU-driver mapping.

## Problem

Dynamic LLM inference workloads need agile memory management. Systems such as vLLM use software-defined paging, but this exposes fragmentation and paging complexity to developers and weakens the simple contiguous tensor abstraction expected by model code.

The paper argues that this interface burden slows algorithmic innovation because developers must design around memory fragmentation rather than tensor semantics.

## Core Contribution

CONTINUUM is a tensor memory virtualization subsystem implemented as a PyTorch extension with a lightweight GPU driver extension. It reduces mapping costs from milliseconds to microseconds and supports Elastic Tensor operations for dynamic memory behavior and zero-copy topological aliasing.

The contribution is both systems-level and interface-level: it makes dynamic memory layouts look like flexible tensor operations.

## Method

CONTINUUM bypasses serialized OS bottlenecks using a GPU driver extension that provides low-latency virtual memory remapping. On top of that, Elastic Tensor exposes operations that preserve tensor-like abstractions while allowing dynamic allocation, remapping, and aliasing.

The system aims to decouple high-level tensor programming from low-level fragmentation management.

## Experiments and Evidence

Evidence reported in the abstract:

- Mapping costs reduced from milliseconds to microseconds.
- PyTorch extension plus lightweight GPU driver extension.
- Elastic Tensor operations for complex memory dynamics.
- Zero-copy topological aliasing.
- Higher throughput across diverse dynamic scenarios.
- Lower engineering burden for next-generation LLM applications.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: workload set, hardware/driver assumptions, safety isolation, and integration constraints.

## Limits and Failure Modes

- Driver extensions can complicate deployment, portability, and maintenance.
- Benefits may depend on GPU architecture and runtime integration.
- Virtualization abstractions need careful debugging and memory-safety tooling.
- Throughput gains may vary by workload memory-access patterns.

## Deep Themes

**Systems abstractions shape model innovation.** Restoring contiguous tensors can make dynamic algorithms easier to express.

**Memory agility is now an ML primitive.** LLM workloads need memory systems that change at inference time.

**Hardware/software boundaries are moving.** The method pushes tensor virtualization into a driver-assisted layer.

## Subthemes

- Tensor memory virtualization.
- Dynamic LLM inference memory.
- Elastic Tensor abstraction.
- GPU-driver mapping.
- Zero-copy aliasing.

## Connections to Other Papers

Connects to MACKO-SpMV, FlashSketch, Incremental BPE, POET-X, and QAT/quantization systems work. It belongs to the efficiency-as-capability cluster where infrastructure constraints determine which algorithms are practical.

## Notes for Cross-Paper Synthesis

CONTINUUM adds an infrastructure layer to the corpus: some capability bottlenecks are not model-side at all, but abstractions that make dynamic computation hard to implement.
