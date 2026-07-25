# Actions Speak Louder than Prompts: A Large-Scale Study of LLMs for Graph Inference

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: MgJUj9Sk3C
- Authors: Ben Finkelshtein; Silviu Cucerzan; Sujay Kumar Jauhar; Ryen W White
- Primary area: foundation or frontier models, including LLMs
- Keywords: Large Language Models;Prompting;In-Context Learning;Tool-augmented Reasoning;Text-rich Graphs
- Source URL: https://openreview.net/forum?id=MgJUj9Sk3C
- PDF URL: https://openreview.net/pdf?id=MgJUj9Sk3C

## Abstract

Large language models (LLMs) are increasingly leveraged for text-rich graph machine learning tasks, with node classification standing out due to its high-impact application domains such as fraud detection and recommendation systems. 
Yet, despite a surge of interest, the field lacks a principled understanding of the capabilities of LLMs in processing graph data.
In this work, we conduct a large-scale, controlled evaluation across the key axes of variability: the LLM-graph interaction mode, comparing prompting, tool-use, and code generation; dataset domains, spanning citation, web-link, e-commerce, and social networks; homophilic vs. heterophilic regimes; short- vs. long-text features; LLM sizes and reasoning capabilities. We further analyze dependencies by independently truncating features, deleting edges, and removing labels to quantify reliance on input types.
Our findings provide actionable guidance for both research and practice. (1) Code generation mode achieves the strongest overall performance, with especially large gains on long-text or high-degree graphs where prompting quickly exceeds the token budget. (2) All interaction strategies remain effective on heterophilic graphs, challenging the assumption that LLM-based methods collapse under low homophily. (3) Code generation mode is able to flexibly shift its reliance to the most informative input type, whether that be structure, features, or labels.
Together, these results establish a clear picture of the strengths and limitations of current LLM–graph interaction modes and point to design principles for future methods.

## One-Sentence Claim

This study shows that LLM performance on text-rich graph inference depends more on interaction mode, especially code generation and tool use, than on prompting alone.

## Problem

LLMs are being used for graph ML tasks such as node classification, but the field lacks controlled evidence about how they actually process graph structure, text features, labels, and homophily regimes.

Prompt-only evaluation can confound model capability with context limits: large or high-degree graphs may exceed prompt budgets even when the relevant computation is straightforward.

## Core Contribution

The paper provides a large-scale controlled evaluation of LLM-graph interaction modes: prompting, tool use, and code generation.

It varies dataset domain, homophily, text length, LLM size, reasoning capability, and input ablations over features, edges, and labels to identify what different approaches rely on.

## Method

The study benchmarks LLMs on text-rich graph node classification across citation, web-link, e-commerce, and social-network domains.

It compares interaction modes and uses controlled perturbations, including feature truncation, edge deletion, and label removal, to measure dependency on graph inputs.

## Experiments and Evidence

The abstract reports three main findings.

Code generation achieves the strongest overall performance, especially on long-text and high-degree graphs where prompting runs into token limits. All interaction modes remain effective on heterophilic graphs. Code generation can flexibly shift reliance among structure, features, and labels depending on which source is most informative.

## Limits and Failure Modes

Graph inference performance may depend on task type; the abstract foregrounds node classification, so conclusions may not transfer fully to link prediction, graph generation, or dynamic graph tasks.

Because this note is abstract-only, details still need checking: exact datasets, graph sizes, prompt/tool/code interfaces, leakage controls, ablation magnitudes, model set, and statistical significance.

## Deep Themes

- Interaction mode as capability boundary: the same LLM can behave differently when prompted, tooled, or asked to generate code.
- Graph structure under context limits: code can externalize graph computation beyond prompt-token constraints.
- Heterophily robustness: LLM graph methods may not fail simply because neighbor labels differ.
- Input-reliance diagnostics: deleting features, edges, and labels reveals whether performance is grounded in the intended signal.

## Subthemes

- Text-rich graph node classification.
- Prompting versus code generation.
- Tool-augmented graph reasoning.
- Homophilic and heterophilic graphs.

## Connections to Other Papers

This connects to GraphMind, GNN exchangeability, UniImb, and graph anomaly papers through graph-learning evaluation.

It also connects to AgentFlow and TileLang because both show that giving models an executable or programmable interface can matter more than better natural-language prompting.

## Notes for Cross-Paper Synthesis

This paper adds a practical agent/tooling theme: for structured data, LLM capability often emerges through the action interface, not through prompt wording alone.
