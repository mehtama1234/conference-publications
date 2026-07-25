# Mastering Sparse CUDA Generation through Pretrained Models and Deep Reinforcement Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: VdLEaGPYWT
- Authors: Yaoyu Wang; Hankun Dai; Zhidong Yang; Junmin Xiao; Guangming Tan
- Primary area: reinforcement learning
- Keywords: Reinforcement Learning;CUDA Code Generation;High-Performance Computing
- Source URL: https://openreview.net/forum?id=VdLEaGPYWT
- PDF URL: https://openreview.net/pdf?id=VdLEaGPYWT

## Abstract

Code generation is a crucial research area in the field of artificial intelligence, holding the potential to revolutionize software development and streamline programming processes. However, generating the high-performance code, which need to be executed in a shorter time for the low-latency scenario, remains a formidable challenge. Existing methods often struggle to account for the irregularity of input sparse data in sparse programs and the need for domain-specific architectural knowledge, leading to sub-optimal performance. To tackle these issues, we propose the SparseRL framework. SparseRL leverages deep reinforcement learning, treating a pre-trained language model as a stochastic policy. It takes the row and column indices of non-zero elements in the sparse matrix as input and generates CUDA code as output for sparse matrix operations. We also introduce a domain-specific code generation mechanism for the dynamic input, a sinusoidal embedding technique tailored for sparse matrices, and a hierarchical reward function that considers both code correctness and execution efficiency. Experimental results demonstrate SparseRL achieves state-of-the-art performance. In sparse matrix-vector multiplication (SpMV) tasks, it improves the compilation rate by 20% compared to existing methods, and the generated code runs 30% faster on average. For sparse matrix-dense matrix multiplication (SpMM) tasks, SparseRL also shows significant performance gains. These results highlight the effectiveness of SparseRL in generating high-performance CUDA code for sparse matrix operations.

## One-Sentence Claim

SparseRL treats CUDA code generation for sparse matrix operations as an RL problem, using sparse-structure inputs and hierarchical rewards for correctness and execution speed.

## Problem

Generating high-performance code is difficult when programs must be both correct and low-latency. Sparse matrix kernels are especially challenging because performance depends on irregular nonzero patterns and hardware-specific knowledge.

Generic code generation methods often fail to account for sparse-data structure and domain-specific GPU optimization constraints.

## Core Contribution

The paper introduces SparseRL, a framework for generating sparse CUDA kernels with pretrained language models and deep reinforcement learning.

It uses nonzero row and column indices as input, adds sparse-matrix sinusoidal embeddings, includes a domain-specific generation mechanism for dynamic inputs, and optimizes with hierarchical rewards for correctness and efficiency.

## Method

SparseRL treats the pretrained language model as a stochastic policy over CUDA code.

The reward hierarchy first enforces compilation and correctness, then rewards execution efficiency for sparse matrix-vector and sparse matrix-dense matrix multiplication tasks.

## Experiments and Evidence

The abstract reports state-of-the-art performance.

For SpMV, SparseRL improves compilation rate by 20 percent over existing methods and generated code runs 30 percent faster on average. It also shows significant gains for SpMM.

## Limits and Failure Modes

RL-generated low-level code can overfit to benchmark matrices or hardware. Correctness and speed rewards may miss numerical stability, portability, maintainability, and security concerns.

Because this note is abstract-only, details still need checking: CUDA templates, GPU targets, sparse matrix distributions, reward design, verification method, training cost, and generalization to unseen sparsity patterns.

## Deep Themes

- Code generation as performance search: the output is not merely executable code, but hardware-efficient code.
- Sparse structure as input signal: nonzero patterns guide generation of specialized kernels.
- Hierarchical reward design: correctness gates speed optimization in program synthesis.
- RL for systems code: policy optimization targets low-level performance in constrained program spaces.

## Subthemes

- CUDA code generation.
- Sparse matrix kernels.
- Deep reinforcement learning.
- Hierarchical correctness-efficiency rewards.

## Connections to Other Papers

This connects to TileLang, einx, HGM, RefineStat, and agentic coding benchmarks through program synthesis and systems infrastructure.

It also relates to Speculative Actions and HyCa because all improve deployed performance through runtime or low-level systems choices.

## Notes for Cross-Paper Synthesis

SparseRL adds a systems-code generation theme: AI code generation is moving from functional correctness toward architecture-aware performance optimization.
