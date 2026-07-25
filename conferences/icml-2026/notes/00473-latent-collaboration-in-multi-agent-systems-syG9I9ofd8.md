# Latent Collaboration in Multi-Agent Systems

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: syG9I9ofd8
- Authors: Jiaru Zou; Ruizhong Qiu; Gaotang Li; Xiyuan Yang; Katherine Tieu; Pan Lu; Ke Shen; Hanghang Tong; Yejin Choi; Jingrui He; James Zou; Mengdi Wang; Ling Yang
- Primary area: deep_learning->large_language_models
- Keywords: LLM-based Multi-Agent Systems;Agent Collaboration;Latent Reasoning;Latent Communication;Efficient LLM Systems
- Source URL: https://openreview.net/forum?id=syG9I9ofd8
- PDF URL: https://openreview.net/pdf?id=syG9I9ofd8

## Abstract

Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings instead of text. Then, a shared latent working memory preserves and transfers each agent's internal representations and latent thoughts, ensuring lossless information exchange without re-encoding. We provide detailed theoretical analyses showing that LatentMAS achieves higher expressiveness and lossless information preservation with lower overall complexity than standard text-based MAS. In addition, empirical evaluations across 9 comprehensive benchmarks spanning math and science reasoning, commonsense understanding, and code generation show that LatentMAS outperforms advanced single agents and text-based MAS baselines, achieving up to 14.6\% higher accuracy, reducing output token usage by 70.8\%-83.7\%, and providing 4$\times$-4.3$\times$ faster end-to-end inference.

## One-Sentence Claim

LatentMAS enables training-free LLM multi-agent collaboration directly through hidden embeddings and shared latent memory, improving accuracy while cutting token usage and inference time versus text-mediated agents.

## Problem

LLM multi-agent systems usually coordinate through text. Text mediation is interpretable but lossy and expensive: agents must verbalize internal reasoning, pass messages, and re-encode them into hidden states.

If agents could collaborate directly in continuous latent space, they might preserve richer internal information and reduce communication overhead. The challenge is doing this without retraining the base models.

## Core Contribution

The paper introduces LatentMAS, an end-to-end training-free framework for pure latent collaboration among LLM agents. Agents generate autoregressive latent thoughts using last-layer hidden embeddings instead of text, and a shared latent working memory transfers those representations across agents.

The contribution is to replace text-based communication with lossless latent information exchange, supported by theoretical analysis of expressiveness, information preservation, and complexity.

## Method

Each agent produces latent thoughts in hidden-embedding space. A shared latent working memory stores these embeddings and makes them available to other agents without decoding to text and re-encoding.

Because the framework is training-free, it operates on existing LLMs by manipulating hidden representations and memory. The goal is to preserve internal reasoning information while reducing output-token overhead.

## Experiments and Evidence

The abstract reports evaluations across nine benchmarks covering math/science reasoning, commonsense understanding, and code generation. LatentMAS outperforms advanced single-agent and text-based multi-agent baselines, improving accuracy by up to 14.6 percent, reducing output-token usage by 70.8-83.7 percent, and providing 4x-4.3x faster end-to-end inference.

Full-paper reading should verify model compatibility, how latent embeddings are exchanged, whether agents share weights, benchmark protocols, and safety/interpretability tradeoffs from non-text communication.

## Limits and Failure Modes

Latent communication reduces transparency. Text-based MAS can be inspected by humans, while latent thoughts may be harder to audit, debug, or constrain.

Compatibility across heterogeneous model architectures may be difficult if hidden spaces are not aligned. Lossless preservation within one model family does not automatically imply semantic interoperability across different LLMs.

## Deep Themes

- Latent communication for agents: collaboration moves from natural language into representation space.
- Efficiency through avoiding re-encoding: token costs fall when agents exchange hidden states directly.
- Shared working memory: multi-agent systems become distributed latent-state machines.
- Training-free system composition: coordination improves without base-weight updates.

## Subthemes

- Text mediation is both a transparency tool and an efficiency bottleneck.
- Latent thoughts preserve information that verbalization may discard.
- Multi-agent reasoning can be accelerated by memory-level sharing.
- Auditing latent collaboration is an open safety issue.

## Connections to Other Papers

LatentMAS connects to DLM, JitRL, MAP, and Vision2Web through LLM agent systems. DLM uses language as the unifying decision interface; LatentMAS argues that pure language may be too costly and lossy for agent collaboration.

It also relates to Assistant Axis, PoLar, and activation-steering work because all manipulate internal representations or execution pathways rather than only prompts.

## Notes for Cross-Paper Synthesis

LatentMAS sharpens a major cross-paper tension: text is good for human oversight, but latent communication may be better for efficiency and fidelity. Future agent systems will need to balance both.
