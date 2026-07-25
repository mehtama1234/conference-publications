# GR-LoRA: Gradient-Recycling Low-Rank Adaptation for Class-Incremental Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: MhMoUuoA1g
- Authors: Yipeng Lin; Fengqiang Wan; Yang Yang
- Primary area: general_machine_learning->everything_else
- Keywords: Class-Incremental Learning
- Source URL: https://openreview.net/forum?id=MhMoUuoA1g
- PDF URL: https://openreview.net/pdf?id=MhMoUuoA1g

## Abstract

Pre-trained models with parameter-efficient fine-tuning have shown strong effectiveness in Class-Incremental Learning (CIL), which seeks to balance model plasticity and stability. In this context, orthogonality constraints can significantly enhance model stability, yet their reliance on subspace inevitably compromises model plasticity over long tasks. To address this, we propose Gradient-Recycling Low-Rank Adaptation (GR-LoRA), which reconciles stability and plasticity by recycling the gradients discarded in orthogonal projection. Specifically, GR-LoRA recycles post-decomposition non-orthogonal gradient components into task-specific lightweight modules and selects optimal module via entropy to improve plasticity, while incorporating local and global mismatch suppression to preserve stability by synthesizing out-of-distribution representations across all tasks. Theoretical analysis confirms that this recycling strategy preserves stability and improves plasticity. Experimental results from multiple CIL benchmarks verify the effectiveness and general applicability of GR-LoRA.

## One-Sentence Claim

GR-LoRA recycles gradients discarded by orthogonal projection into task-specific low-rank modules to improve plasticity while preserving stability in class-incremental learning.

## Problem

Class-incremental learning with PEFT must balance stability and plasticity, but orthogonality constraints that prevent forgetting can consume subspace capacity and reduce long-term adaptability.

## Core Contribution

The paper proposes Gradient-Recycling LoRA, which decomposes gradients, redirects non-orthogonal discarded components into lightweight task modules, selects modules by entropy, and suppresses local/global mismatch with synthetic OOD representations.

## Method

GR-LoRA applies orthogonal projection for stability, recycles rejected gradient components into task-specific LoRA modules for plasticity, uses entropy to select the optimal module, and generates OOD representations across tasks to reduce mismatch.

## Experiments and Evidence

The abstract reports theoretical analysis confirming stability/plasticity benefits and experiments across multiple CIL benchmarks showing effectiveness and general applicability.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: benchmarks, pretrained backbones, module growth over tasks, entropy-selection reliability, OOD representation synthesis, and memory cost over long task streams.

## Deep Themes

- Discarded optimization signal can be recycled for future plasticity.
- Stability-plasticity tradeoffs require explicit subspace management.
- Lightweight task modules can preserve incremental adaptability.

## Subthemes

- Class-incremental learning.
- LoRA.
- Gradient recycling.
- Orthogonal projection.
- Stability-plasticity balance.
- Out-of-distribution representation synthesis.

## Connections to Other Papers

Connects to Nevo-CRL, LiME, SmartFed, and APB through modular adaptation under capacity constraints and continual learning.

## Notes for Cross-Paper Synthesis

GR-LoRA adds a gradient-level anti-waste theme: information removed for stability can be preserved in side modules to maintain long-horizon plasticity.
