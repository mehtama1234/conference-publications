# Dual-Latent Memory Routing for Vision-Language Reasoning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: SFWWUr9V7c
- Authors: Hao-Xuan Ma; Jin-Fei Qi; YiCheng Xiao; Han-Jia Ye
- Primary area: applications->computer_vision
- Keywords: Vision-Language Reasoning;MLLM memory
- Source URL: https://openreview.net/forum?id=SFWWUr9V7c
- PDF URL: https://openreview.net/pdf?id=SFWWUr9V7c

## Abstract

Multimodal large language models (MLLMs) have recently made strong progress in vision-language reasoning, yet their performance often degrades as generations grow longer. A key factor is that they frequently lose track of earlier visual evidence and intermediate constraints under a monolithic growing context. Inspired by how humans separately recall what they see and what they infer when solving complex tasks, we propose DLMR, a parameter-efficient mechanism that equips MLLMs with Dual Latent Memories: a visual memory that compresses image evidence and a reasoning memory that tracks intermediate conclusions and constraints. A Router then dynamically decides which memory and how much to reuse during inference, preserving visual grounding while maintaining coherent long-horizon reasoning. DLMR is trained in three stages, from latent memory construction to selective router learning, while keeping the base MLLM frozen, yielding substantial gains on both general and reasoning benchmarks with only a small number of additional trainable parameters. Analyses further show interpretable, state-dependent routing with specialized memory roles and reduced decoding tokens over long generations. Code is available at https://github.com/Hunter-Wrynn/DLMR.

## One-Sentence Claim

DLMR improves long-horizon vision-language reasoning by giving frozen MLLMs separate latent visual and reasoning memories with a router that decides what to reuse during inference.

## Problem

MLLM reasoning degrades over long generations because a monolithic growing context causes models to lose track of earlier visual evidence and intermediate constraints.

## Core Contribution

The paper proposes Dual Latent Memories, separating compressed image evidence from intermediate reasoning state, plus a parameter-efficient router trained in stages while keeping the base model frozen.

## Method

DLMR constructs visual and reasoning memories, learns selective routing over which memory and how much to reuse, and applies that routing during inference to preserve grounding and coherent reasoning with few added parameters.

## Experiments and Evidence

The abstract reports substantial gains on general and reasoning benchmarks, interpretable state-dependent routing with specialized memory roles, and reduced decoding tokens over long generations.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: memory architecture, benchmarks, token savings, routing supervision, visual-memory compression loss, and behavior on conflicting visual/reasoning memories.

## Deep Themes

- Long-horizon multimodal reasoning needs explicit memory separation.
- Visual evidence and inferred constraints play different roles in reasoning.
- Routing over latent memories can reduce context bloat.

## Subthemes

- Vision-language reasoning.
- MLLM memory.
- Latent memory.
- Parameter-efficient adaptation.
- Dynamic routing.
- Long generations.

## Connections to Other Papers

Connects to MemoryBench, Hierarchical Thinking, SVGT, and Table-GLS through memory, routing, and process control in long-horizon model behavior.

## Notes for Cross-Paper Synthesis

DLMR adds a memory-routing theme: context length alone is not enough; models need structured recall channels for different kinds of evidence.
