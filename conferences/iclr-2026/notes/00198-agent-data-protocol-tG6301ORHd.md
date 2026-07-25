# Agent Data Protocol

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: tG6301ORHd
- Authors: Yueqi Song; Ketan Ramaneti; Zaid Sheikh; Ziru Chen; Boyu Gou; Tianbao Xie; Yiheng Xu; Danyang Zhang; Apurva Gandhi; Fan Yang; Joseph Liu; Tianyue Ou; Zhihao Yuan; Frank F. Xu; Shuyan Zhou; Xingyao Wang; Xiang Yue; Tao Yu; Huan Sun; Yu Su; Graham Neubig
- Primary area: datasets and benchmarks
- Keywords: agent;training;data
- Source URL: https://openreview.net/forum?id=tG6301ORHd
- PDF URL: https://openreview.net/pdf?id=tG6301ORHd

## Abstract

Public research results on large-scale supervised finetuning of AI agents remain relatively rare, since the collection of agent training data presents unique challenges. In this work, we argue that the bottleneck is not a lack of underlying data sources, but that a large variety of data is fragmented across heterogeneous formats, tools, and interfaces. To this end, we introduce the Agent Data Protocol (ADP), a light-weight representation language that serves as an "interlingua" between agent datasets in diverse formats and unified agent training pipelines downstream. The design of ADP is expressive enough to capture a large variety of tasks, including API/tool use, browsing, coding, software engineering, and general agentic workflows, while remaining simple to parse and train on without engineering at a per-dataset level. In experiments, we unified a broad collection of 13 existing agent training datasets into ADP format, and converted the standardized ADP data into training-ready formats for multiple agent frameworks. We performed supervised finetuning on the unified data, and demonstrated an average performance gain of $\sim$20\% over
corresponding base models, and delivers state-of-the-art or near-SOTA performance on standard coding, browsing, tool use, and research benchmarks, without domain-specific tuning. All code and data are released publicly, in the hope that ADP could help lower the barrier to standardized, scalable, and reproducible agent training.

## One-Sentence Claim

ADP standardizes heterogeneous agent datasets into a lightweight interlingua, enabling scalable supervised finetuning across tool-use, browsing, coding, and general agent workflows.

## Problem

Agent training data exists across many datasets, tools, interfaces, and formats, but fragmentation makes large-scale supervised finetuning difficult and engineering-heavy. The bottleneck is standardization rather than lack of raw data.

## Core Contribution

The paper introduces Agent Data Protocol, a representation language expressive enough for diverse agentic tasks and simple enough for unified parsing and training. It converts 13 existing agent datasets into ADP and trains agents from the unified data.

## Method

ADP acts as an interlingua between source datasets and downstream agent frameworks. It represents actions, observations, tool/API use, browsing, coding, software engineering, and general workflows in a standard format, then converts that data into framework-specific training-ready forms.

## Experiments and Evidence

The abstract reports unifying 13 datasets, supervised finetuning on the combined ADP data, roughly 20 percent average performance gain over base models, and state-of-the-art or near-SOTA results on coding, browsing, tool-use, and research benchmarks without domain-specific tuning.

## Limits and Failure Modes

A common protocol can flatten dataset-specific semantics or omit environment details needed for faithful replay. SFT gains may depend on benchmark overlap or dataset quality. Full-text review should check schema design, lossless conversion claims, dataset licenses, train/eval contamination, and compatibility with interactive RL or online feedback.

## Deep Themes

- Standardized infrastructure for agent training.
- Dataset interlingua for tool-use workflows.
- Reproducible scalable agent SFT.
- Data fragmentation as a training bottleneck.

## Subthemes

- API/tool-use representation.
- Browsing and coding trajectory data.
- Multi-framework data conversion.
- Agent dataset unification.
- Domain-general agent training.

## Connections to Other Papers

Connects to MedAgentGym, BIRD-INTERACT, Gaia2, OpenApps, and other agent benchmarks through environment/data standardization, and to Common Corpus/data-governance papers through open reproducible training resources.

## Notes for Cross-Paper Synthesis

ADP is infrastructure for the agent era: if data formats stay fragmented, agent training cannot scale reproducibly. The protocol makes heterogeneous interaction traces trainable as one corpus.
