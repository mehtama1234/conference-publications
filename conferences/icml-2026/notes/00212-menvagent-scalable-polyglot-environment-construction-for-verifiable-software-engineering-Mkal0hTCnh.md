# MEnvAgent: Scalable Polyglot Environment Construction for Verifiable Software Engineering

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Mkal0hTCnh
- Authors: Chuanzhe Guo; Jingjing Wu; Sijun He; Yang Chen; Zhaoqi Kuang; Shilong Fan; Bingjin Chen; Siqi Bao; Jing Liu; Hua Wu; Qingfu Zhu; Wanxiang Che; Haifeng Wang
- Primary area: applications
- Keywords: Large Language Models;Software Engineering;Automated Environment Construction;Multi-Agent Framework
- Source URL: https://openreview.net/forum?id=Mkal0hTCnh
- PDF URL: https://openreview.net/pdf?id=Mkal0hTCnh

## Abstract

The evolution of Large Language Model (LLM) agents for software engineering (SWE) is constrained by the scarcity of verifiable datasets, a bottleneck stemming from the complexity of constructing executable environments across diverse languages. To address this, we introduce **MEnvAgent**, a **M**ulti-language framework for automated **Env**ironment construction that facilitates scalable generation of verifiable task instances. MEnvAgent employs a multi-agent Planning-Execution-Verification architecture to autonomously resolve construction failures and integrates a novel Environment Reuse Mechanism that reduces computational overhead by incrementally patching historical environments. Evaluations on MEnvBench, a new benchmark comprising 1,000 tasks across 10 languages, demonstrate that MEnvAgent outperforms baselines, improving Fail-to-Pass (F2P) rates by **8.6%** while reducing time costs by **43%**. Additionally, we demonstrate the utility of MEnvAgent by constructing MEnvData-SWE, the largest open-source polyglot dataset of realistic verifiable Docker environments to date, alongside solution trajectories that enable consistent performance gains on SWE tasks across a wide range of models.

## One-Sentence Claim

MEnvAgent automatically constructs executable polyglot software environments, scaling verifiable SWE task generation with multi-agent planning, execution, verification, and environment reuse.

## Problem

LLM software-engineering agents need verifiable datasets, but constructing executable environments across many programming languages is difficult and limits scalable task creation.

## Core Contribution

The paper introduces MEnvAgent, MEnvBench with 1,000 tasks across 10 languages, and MEnvData-SWE, a large open-source polyglot dataset of verifiable Docker environments plus solution trajectories.

## Method

MEnvAgent uses a Planning-Execution-Verification multi-agent architecture to repair construction failures and an Environment Reuse Mechanism that incrementally patches historical environments to reduce cost.

## Experiments and Evidence

The abstract reports that MEnvAgent improves Fail-to-Pass rates by 8.6% and reduces time costs by 43% on MEnvBench, and that the resulting solution trajectories improve SWE performance across a range of models.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: supported languages, Docker reproducibility, failure taxonomy, baseline setup, security risks of environment execution, and whether generated tasks reflect real maintenance work.

## Deep Themes

- Verifiable AI-agent training depends on executable environment infrastructure.
- Environment construction can itself be automated by agentic planning and verification.
- Reuse of prior environments reduces dataset-generation cost.

## Subthemes

- Software engineering agents.
- Verifiable datasets.
- Polyglot environments.
- Docker.
- Multi-agent repair.
- Fail-to-Pass evaluation.

## Connections to Other Papers

Connects to CE-Graph, MemoryBench, and agent/process evaluation papers through verifiable task construction and execution-grounded feedback.

## Notes for Cross-Paper Synthesis

MEnvAgent adds an infrastructure theme: scaling agent evaluation and training is limited not just by model capability but by the ability to create reliable executable worlds.
