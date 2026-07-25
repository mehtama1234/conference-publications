# EntroKV: Entropy-Guided Dynamic Budget Allocation for KV-Cache Compression

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: xhAMjsnWUe
- Authors: Wenhao Gao; Haoran Cao; Yueyan Li; YongGao Xiao; Caixia Yuan; Xiaojie Wang
- Primary area: deep_learning->large_language_models
- Keywords: LLM Efficiency;KV cache
- Source URL: https://openreview.net/forum?id=xhAMjsnWUe
- PDF URL: https://openreview.net/pdf?id=xhAMjsnWUe

## Abstract

The prohibitive memory footprint of the Key-Value (KV) cache imposes a critical bottleneck for efficient long-context LLM serving. 
Current compression techniques typically rely on static or uniform budget allocation, overlooking the significant heterogeneity in information density across attention heads. 
To address this, we introduce \textsc{EntroKV}, an entropy-driven dynamic budget allocation framework. 
Our method enables dynamic and rational allocation across layers, attention heads, and different tasks.
We demonstrate that attention entropy serves as a robust proxy for compression sensitivity: heads with high entropy require larger retention budgets, whereas low-entropy heads can be aggressively compressed without accuracy degradation. 
Functioning as a lightweight, plug-and-play module, \textsc{EntroKV} optimizes budget scheduling in real-time and is compatible with diverse compression operators. 
Extensive experiments demonstrate that \textsc{EntroKV} consistently outperforms baselines, retaining $\sim$98\% of full-cache performance at a 30\% budget ratio with negligible computational overhead. 
Our code is available at \url{https://anonymous.4open.science/r/EntroKV-D0C8/}.

## One-Sentence Claim

EntroKV compresses long-context KV caches more effectively by allocating retention budget dynamically according to attention entropy across layers, heads, and tasks.

## Problem

KV-cache memory is a major bottleneck for efficient long-context LLM serving. Existing compression methods often use static or uniform budgets even though attention heads differ in information density and compression sensitivity.

The problem is to preserve generation quality under severe cache budgets without overspending memory on low-value heads.

## Core Contribution

The paper introduces EntroKV, an entropy-guided dynamic budget allocation framework for KV-cache compression.

The key claim is that attention entropy is a robust proxy for compression sensitivity: high-entropy heads need larger retention budgets, while low-entropy heads can be compressed aggressively with little accuracy loss.

## Method

EntroKV schedules cache budgets in real time across layers, heads, and tasks. It is designed as a lightweight plug-and-play module compatible with multiple compression operators.

The allocator uses attention entropy to decide where memory should be retained, replacing uniform allocation with sensitivity-aware budgeting.

## Experiments and Evidence

The abstract reports that EntroKV retains about 98 percent of full-cache performance at a 30 percent budget ratio with negligible computational overhead.

It also reports consistent improvements over baselines across diverse compression operators.

## Limits and Failure Modes

Attention entropy may not always capture downstream importance, especially for tasks where a low-entropy head points to a rare but crucial token or where high entropy reflects uncertainty rather than useful spread.

Because this note is abstract-only, details still need checking: model families, context lengths, tasks, compression operators, latency overhead, entropy measurement timing, and behavior under retrieval-heavy or adversarial long-context inputs.

## Deep Themes

- Dynamic memory allocation: cache retention should follow information density.
- Entropy as systems signal: internal attention statistics can guide serving-time resource allocation.
- Long-context efficiency: scaling context depends on memory scheduling, not only model architecture.
- Plug-and-play compression control: budget allocation can sit above multiple low-level compression operators.

## Subthemes

- KV-cache compression.
- Head-level compression sensitivity.
- Layer/head/task dynamic budgets.
- Real-time serving efficiency.

## Connections to Other Papers

This connects to FFCC, IO-aware GNN kernels, EcoVLA, and LiftQuant through efficiency as a capability enabler.

It also relates to Information Flow because both use internal attention or contribution structure to infer where information matters, though EntroKV uses it for resource allocation rather than trust calibration.

## Notes for Cross-Paper Synthesis

EntroKV adds to the resource-adaptive inference theme: systems increasingly allocate compute or memory according to measured internal signal rather than uniform budgets.
