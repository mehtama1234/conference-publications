# MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: If4X4W2HWx
- Authors: Qingyao Ai; Yichen Tang; Changyue Wang; Jianming Long; Weihang Su; Yiqun LIU
- Primary area: general_machine_learning->evaluation
- Keywords: Continual Learning;Memory;Large Language Model
- Source URL: https://openreview.net/forum?id=If4X4W2HWx
- PDF URL: https://openreview.net/pdf?id=If4X4W2HWx

## Abstract

Scaling up data, parameters, and test-time computation has been the mainstream methods to improve LLM systems (LLMsys), but their upper bounds are almost reached due to the gradual depletion of high-quality data and marginal gains obtained from larger computational resource consumption. Inspired by the abilities of human and traditional AI systems in learning from practice, constructing memory and continual learning frameworks for LLMsys has become an important and popular research direction in recent literature. Yet, existing benchmarks for LLM memory often focus on evaluating the system on homogeneous reading comprehension tasks with long-form inputs rather than testing their abilities to learn from accumulated user feedback in service time. Therefore, we propose a user feedback simulation framework and a comprehensive benchmark covering multiple domains, languages, and types of tasks to evaluate the continual learning abilities of LLMsys. Experiments show that the effectiveness and efficiency of state-of-the-art baselines are far from satisfying, and we hope this benchmark could pave the way for future studies on LLM memory and optimization algorithms.

## One-Sentence Claim

MemoryBench evaluates whether LLM systems can learn continually from accumulated user feedback across domains, languages, and task types.

## Problem

Existing LLM memory benchmarks often focus on homogeneous long-context reading comprehension rather than service-time learning from user feedback, while gains from more data, parameters, and compute are becoming less reliable.

## Core Contribution

The paper introduces a user-feedback simulation framework and a benchmark for memory and continual learning in LLM systems.

## Method

MemoryBench simulates accumulated user feedback and evaluates LLM systems across multiple domains, languages, and task categories to measure both effectiveness and efficiency of continual learning/memory algorithms.

## Experiments and Evidence

The abstract reports that state-of-the-art baselines remain far from satisfactory in effectiveness and efficiency.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: feedback simulator realism, tasks and languages, memory-system baselines, leakage controls, metrics, and whether the benchmark separates retrieval, updating, personalization, and forgetting.

## Deep Themes

- LLM systems need service-time learning, not just static pretraining.
- Memory evaluation should include feedback accumulation and continual adaptation.
- Scaling pressure is shifting attention toward experience-based improvement.

## Subthemes

- LLM memory.
- Continual learning.
- User feedback simulation.
- Multilingual evaluation.
- System-level benchmarking.
- Efficiency of memory updates.

## Connections to Other Papers

Connects to Nevo-CRL through continual learning and to reasoning/process evaluation papers through richer system-level benchmarks. It also relates to data-governance papers because user feedback becomes a persistent learning resource.

## Notes for Cross-Paper Synthesis

MemoryBench adds an evaluation counterpart to continual-learning methods: the corpus is moving toward systems that improve through deployed experience, so benchmarks must test accumulation, adaptation, and forgetting over time.
