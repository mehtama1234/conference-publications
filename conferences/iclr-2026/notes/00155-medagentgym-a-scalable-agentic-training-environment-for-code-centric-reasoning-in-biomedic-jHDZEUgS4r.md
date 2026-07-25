# MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: jHDZEUgS4r
- Authors: Ran Xu; Yuchen Zhuang; Yishan Zhong; Yue Yu; Zifeng Wang; Xiangru Tang; Hang Wu; May Dongmei Wang; Peifeng Ruan; Donghan Yang; Tao Wang; Guanghua Xiao; Xin Liu; Carl Yang; Yang Xie; Wenqi Shi
- Primary area: datasets and benchmarks
- Keywords: Medical Reasoning;LLM Agent;Code Generation
- Source URL: https://openreview.net/forum?id=jHDZEUgS4r
- PDF URL: https://openreview.net/pdf?id=jHDZEUgS4r

## Abstract

We introduce MedAgentGym, a scalable and interactive training environment designed to enhance coding-based biomedical reasoning capabilities in large language model (LLM) agents. MedAgentGym comprises 72,413 task instances across 129 categories derived from 12 authentic real-world biomedical scenarios. Tasks are encapsulated within executable sandbox environments, each featuring detailed task specifications, interactive feedback mechanisms, verifiable ground truth annotations, and scalable training trajectory generation. Extensive benchmarking of 29 LLMs reveals substantial performance disparities in biomedical data science between commercial and open-source LLMs. Leveraging efficient multi-threaded and multi-turn trajectory sampling in MedAgentGym, Med-Copilot achieves performance gains of +43.02% and +45.28% from offline and online reinforcement learning, respectively, demonstrating MedAgentGym as an effective training ground while establishing itself as a cost-effective, privacy-preserving alternative competitive with proprietary LLMs (gpt-4o). By offering a unified execution environment with a comprehensive benchmark and accessible, extensible training resources, MedAgentGym delivers an integrated platform to develop LLM-based coding assistants for advanced biomedical data science.

## One-Sentence Claim

MedAgentGym provides executable biomedical data-science environments for training and evaluating code-centric LLM agents, enabling large RL gains for a privacy-preserving biomedical assistant.

## Problem

Biomedical data science requires code-centric reasoning over real tasks, but agent training needs verifiable environments, feedback, and scalable trajectory generation.

Commercial LLMs can be strong, but biomedical settings also require cost efficiency, privacy preservation, and reproducible training resources.

## Core Contribution

The paper introduces MedAgentGym, a scalable interactive training environment.

It contains 72,413 task instances across 129 categories from 12 real biomedical scenarios, each packaged in executable sandbox environments with task specifications, feedback, ground truth, and trajectory generation.

## Method

Agents interact with sandboxed biomedical coding tasks, receive feedback, and can generate multi-turn trajectories for offline and online reinforcement learning.

The environment supports benchmarking of many LLMs and training of a specialized Med-Copilot agent.

## Experiments and Evidence

The abstract reports benchmarking 29 LLMs and finding large commercial/open-source performance gaps.

Using multi-threaded and multi-turn trajectory sampling, Med-Copilot gains 43.02 percent from offline RL and 45.28 percent from online RL, becoming competitive with GPT-4o as a cost-effective, privacy-preserving alternative.

## Limits and Failure Modes

Biomedical coding tasks may not cover clinical reasoning, regulatory constraints, or real patient data complexity. Privacy-preserving claims depend on deployment and data-handling details.

Because this note is abstract-only, details still need checking: scenario definitions, sandbox design, ground-truth annotations, RL algorithms, safety/privacy setup, and benchmark leakage controls.

## Deep Themes

- Domain-specific agent gyms: specialized fields need executable training environments, not generic tasks.
- Code-centric biomedical reasoning: scientific/medical assistance often runs through data analysis code.
- Verifiable sandbox feedback: RL gains depend on reliable executable rewards and annotations.
- Privacy-preserving open alternatives: specialized agents can reduce dependence on proprietary biomedical workflows.

## Subthemes

- Biomedical data science.
- Agentic training environments.
- Offline and online RL.
- Executable sandboxes.

## Connections to Other Papers

This connects to AgentGym-RL, AstaBench, SwingArena, RefineStat, and scientific-agent benchmarks.

It also relates to privacy/governance themes because biomedical data science has high sensitivity and compliance risk.

## Notes for Cross-Paper Synthesis

MedAgentGym adds a domain-agent infrastructure theme: trustworthy specialized agents need executable, verifiable training grounds tailored to domain workflows.
