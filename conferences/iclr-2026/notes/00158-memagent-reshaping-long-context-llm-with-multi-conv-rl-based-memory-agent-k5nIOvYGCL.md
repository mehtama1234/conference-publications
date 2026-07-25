# MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: k5nIOvYGCL
- Authors: Hongli Yu; Tinghong Chen; Jiangtao Feng; Jiangjie Chen; Weinan Dai; Qiying Yu; Ya-Qin Zhang; Wei-Ying Ma; Jingjing Liu; Mingxuan Wang; Hao Zhou
- Primary area: foundation or frontier models, including LLMs
- Keywords: LLM;memory;agent;RLVR
- Source URL: https://openreview.net/forum?id=k5nIOvYGCL
- PDF URL: https://openreview.net/pdf?id=k5nIOvYGCL

## Abstract

Despite improvements by length extrapolation, efficient attention and memory modules, handling infinitely long documents without performance degradation during extrapolation remains the ultimate challenge in long-text processing. To solve this problem, We introduce a novel agent workflow, \method, which processes text in segments and updates memory through an overwrite strategy, addressing the challenge of long-context task through enhanced memory management. We further extend the DAPO algorithm to directly optimize memory ability in an end-to-end fashion, facilitating training via independent-context multi-conversation generation. Experimental results demonstrate that MemAgent has superb long-context capabilities, being able to extrapolate from an 8K context to a 3.5M QA task with a performance loss of less than 10\% and achieving over 95\% on the 512K NIAH test.

## One-Sentence Claim

MemAgent trains an LLM memory agent with multi-conversation RL so it can process extremely long documents segment by segment and maintain useful overwrite-based memory far beyond its native context length.

## Problem

Length extrapolation, efficient attention, and memory modules still degrade on extremely long documents. The challenge is not only accepting more tokens but retaining task-relevant information while repeatedly compressing and updating memory over many segments.

## Core Contribution

The paper introduces a segmental memory-agent workflow with overwrite updates and extends DAPO-style RL to optimize memory behavior end to end through independent-context multi-conversation generation. It frames long-context handling as an agentic memory-management problem rather than a pure attention-scaling problem.

## Method

MemAgent processes text in chunks, updates a persistent memory via an overwrite strategy, and uses reinforcement learning with verifiable rewards to train the memory-update behavior. Independent-context multi-conversation generation supplies training episodes that target memory ability directly.

## Experiments and Evidence

The abstract reports extrapolation from 8K training context to a 3.5M-token QA task with less than 10 percent performance loss, and over 95 percent on the 512K Needle-in-a-Haystack test.

## Limits and Failure Modes

Overwrite memory can lose details that later become relevant, and strong results may depend on task answerability, retrieval locality, reward design, and benchmark construction. Full-text review should check memory size, update format, compute cost, comparison to retrieval-augmented and efficient-attention baselines, and whether multi-hop reasoning survives heavy compression.

## Deep Themes

- Long-context reasoning as memory control.
- RLVR for process skills rather than final-answer style alone.
- Segmental recurrence for context extrapolation.
- Textual memory as an editable state representation.

## Subthemes

- Overwrite-based memory updates.
- Multi-conversation RL training.
- Infinite-context approximation.
- Needle-in-a-Haystack robustness.
- Agent workflows around LLM context limits.

## Connections to Other Papers

Connects to In-Place TTT and long-context retriever learning through adaptive inference-time mechanisms, to Gaia2 and agent benchmarks through verifiable process rewards, and to later memory-lifecycle benchmarks that decompose insertion, consolidation, retrieval, and integration.

## Notes for Cross-Paper Synthesis

MemAgent exemplifies a broad shift from longer static windows to learned context-management policies. The deeper theme is that long-horizon capability may require a trainable controller over memory state, not merely more attention capacity.
