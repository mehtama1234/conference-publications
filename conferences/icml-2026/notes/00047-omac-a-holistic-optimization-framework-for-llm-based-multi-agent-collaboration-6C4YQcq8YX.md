# OMAC: A Holistic Optimization Framework for LLM-Based Multi-Agent Collaboration

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 6C4YQcq8YX
- Authors: Shijun Li; Hilaf Hasson; Joydeep Ghosh
- Primary area: applications->language_speech_and_dialog
- Keywords: Mutli-Agent Collaboration;Agentic AI;Large Language Model
- Source URL: https://openreview.net/forum?id=6C4YQcq8YX
- PDF URL: https://openreview.net/pdf?id=6C4YQcq8YX

## Abstract

Agents powered by advanced large language models (LLMs) have demonstrated impressive capabilities across diverse complex applications.  Recently, Multi-Agent Systems (MAS), wherein multiple agents collaborate and communicate with each other, have exhibited enhanced capabilities in complex tasks, such as high-quality code generation and arithmetic reasoning. However, the development of such systems often relies on handcrafted methods, and the literature on systematic design and optimization of LLM-based MAS remains limited.
In this work, we introduce OMAC, a general framework designed for holistic optimization of LLM-based MAS. Specifically, we identify five key optimization dimensions for MAS, encompassing both agent functionality and collaboration structure. Building upon these dimensions, we first propose a general algorithm, utilizing two actors termed the Semantic Initializer and the Contrastive Comparator, to optimize any single dimension. Then, we present an algorithm for joint optimization across multiple dimensions. Extensive experiments demonstrate the superior performance of OMAC on diverse tasks against recent approaches. Codes are available at: https://github.com/xiwenchao/OMAC.

## One-Sentence Claim

OMAC treats LLM multi-agent systems as jointly optimizable artifacts, tuning both individual agent functions and collaboration structure rather than relying on handcrafted designs.

## Problem

LLM-based multi-agent systems can improve complex tasks, but their design is often manual and ad hoc, with limited systematic optimization across roles, prompts, communication, and collaboration topology.

## Core Contribution

The paper proposes OMAC, a holistic framework identifying five optimization dimensions for LLM-based MAS and algorithms for optimizing individual dimensions or multiple dimensions jointly.

## Method

OMAC uses two actors, a Semantic Initializer and a Contrastive Comparator, to optimize a chosen MAS design dimension, then extends the procedure to joint multi-dimensional optimization.

## Experiments and Evidence

The abstract reports superior performance over recent approaches across diverse tasks, including settings such as code generation and arithmetic reasoning.

## Limits and Failure Modes

ArXiv searches for this batch hit HTTP 429, so no local PDF is available yet. Details still need checking: the five exact optimization dimensions, search budget, task suite, comparator reliability, and whether gains transfer across models.

## Deep Themes

- Agent systems require design optimization, not only stronger base models.
- Collaboration structure is a first-class control surface.
- Multi-agent performance depends on roles, communication, and topology jointly.

## Subthemes

- LLM multi-agent systems.
- Agent collaboration.
- Prompt/role optimization.
- Collaboration topology.
- Semantic initialization.
- Contrastive comparison.

## Connections to Other Papers

Connects to Unsupervised Partner Design, RAGEN-2, and multi-agent/game-dynamics papers. It also links to agent evaluation work where interaction structure determines behavior.

## Notes for Cross-Paper Synthesis

OMAC strengthens the agent-systems theme: as systems move from single LLMs to teams of agents, optimization shifts from model parameters to coordination architecture.
