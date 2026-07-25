# MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: JEGDp1E4OH
- Authors: Xuying Ning; Dongqi Fu; Tianxin Wei; Mengting Ai; Jiaru Zou; Ting-Wei Li; Hanghang Tong; Yada Zhu; Hendrik Hamann; Jingrui He
- Primary area: foundation or frontier models, including LLMs
- Keywords: Multimodal;RAG;Vision-Language;Agent;Benchmark
- Source URL: https://openreview.net/forum?id=JEGDp1E4OH
- PDF URL: https://openreview.net/pdf?id=JEGDp1E4OH

## Abstract

With the increasing demand for step-wise, cross-modal, and knowledge-grounded reasoning, multimodal large language models (MLLMs) are evolving beyond the traditional fixed retrieve-then-generate paradigm toward more sophisticated agentic multimodal retrieval-augmented generation (MM-RAG). Existing benchmarks, however, mainly focus on simplified QA with short retrieval chains, leaving adaptive planning and multimodal reasoning underexplored. We present MC-Search, the first benchmark for agentic MM-RAG with long, step-wise annotated reasoning chains spanning five representative reasoning structures. Each example specifies sub-questions, retrieval modalities, supporting facts, and intermediate answers, with fidelity ensured by HAVE (Hop-wise Attribution and Verification of Evidence), resulting in 3,333 high-quality examples averaging 3.7 hops. Beyond answer accuracy, MC-Search introduces new process-level metrics for reasoning quality, stepwise retrieval and planning accuracy. By developing a unified agentic MM-RAG pipeline, we benchmark six leading MLLMs and reveal systematic issues such as over- and under-retrieval and modality-misaligned planning. Finally, we introduce Search-Align, a process-supervised fine-tuning framework leveraging verified reasoning chains, showing that our data not only enables faithful evaluation but also improves planning and retrieval fidelity in open-source MLLMs.

## One-Sentence Claim

MC-Search evaluates and improves agentic multimodal RAG by providing long step-wise verified reasoning chains with modality-specific retrieval and planning supervision.

## Problem

Multimodal RAG is moving beyond fixed retrieve-then-generate pipelines toward agentic search that plans multiple retrieval steps across modalities.

Existing benchmarks often use simplified QA and short retrieval chains, leaving adaptive planning, cross-modal retrieval, and process quality underexplored.

## Core Contribution

The paper introduces MC-Search, a benchmark for agentic MM-RAG with long annotated reasoning chains over five reasoning structures.

Each example includes sub-questions, retrieval modalities, supporting facts, and intermediate answers. Quality is enforced by HAVE, Hop-wise Attribution and Verification of Evidence. The paper also introduces Search-Align, a process-supervised fine-tuning framework.

## Method

MC-Search builds examples with stepwise reasoning annotations and evidence verification. It evaluates not only final answer accuracy but also reasoning quality, retrieval accuracy, and planning accuracy.

The authors build a unified agentic MM-RAG pipeline and use verified chains for process-supervised fine-tuning in Search-Align.

## Experiments and Evidence

The benchmark contains 3,333 examples averaging 3.7 hops.

The paper benchmarks six leading MLLMs and finds over-retrieval, under-retrieval, and modality-misaligned planning. Search-Align improves planning and retrieval fidelity in open-source MLLMs.

## Limits and Failure Modes

Benchmark quality depends on evidence annotation and verifier reliability. Long-chain supervision may also be expensive and may not capture all real-world multimodal search patterns.

Because this note is abstract-only, details still need checking: five reasoning structures, HAVE protocol, modality mix, metrics, models evaluated, and Search-Align training details.

## Deep Themes

- Agentic multimodal retrieval: search becomes a planned multi-step process.
- Process-level evaluation: retrieval and planning quality matter separately from answer accuracy.
- Verified reasoning chains: evidence attribution provides supervision for faithful search.
- Modality-aware planning: agents must decide not only what to retrieve, but from which modality.

## Subthemes

- MM-RAG.
- Hop-wise attribution and verification.
- Over- and under-retrieval.
- Search-Align process supervision.

## Connections to Other Papers

This connects to Gaia2, Q-RAG, GLANCE, WebDevJudge, and FRABench through agentic evaluation and process supervision.

It also relates to Information Flow because both ask whether retrieved evidence actually supports downstream reasoning.

## Notes for Cross-Paper Synthesis

MC-Search adds a multimodal agentic-search theme: reliable RAG requires verifiable intermediate search plans, not only final answer scoring.
