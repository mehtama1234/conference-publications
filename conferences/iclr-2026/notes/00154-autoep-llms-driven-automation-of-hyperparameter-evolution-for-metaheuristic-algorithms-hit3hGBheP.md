# AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: hit3hGBheP
- Authors: Zhenxing Xu; Yizhe Zhang; Weidong Bao; Hao Wang; Ming Chen; Haoran Ye; Wenzheng Jiang; Hui Yan; Ji Wang
- Primary area: optimization
- Keywords: LLMs;Optimization;Metaheuristic algorithm;Automatic Algorithm Design
- Source URL: https://openreview.net/forum?id=hit3hGBheP
- PDF URL: https://openreview.net/pdf?id=hit3hGBheP

## Abstract

Dynamically configuring algorithm hyperparameters is a fundamental challenge in computational intelligence. While learning-based methods offer automation, they suffer from prohibitive sample complexity and poor generalization. We introduce AutoEP, a novel framework that bypasses training entirely by leveraging Large Language Models (LLMs) as zero-shot reasoning engines for algorithm control. AutoEP's core innovation lies in a tight synergy between two components: (1) an online Exploratory Landscape Analysis (ELA) module that provides real-time, quantitative feedback on the search dynamics, and (2) a multi-LLM reasoning chain that interprets this feedback to generate adaptive hyperparameter strategies. This approach grounds high-level reasoning in empirical data, mitigating hallucination. Evaluated on three distinct metaheuristics across diverse combinatorial optimization benchmarks, AutoEP consistently outperforms state-of-the-art tuners, including neural evolution and other LLM-based methods. Notably, our framework enables open-source models like Qwen3-30B to match the performance of GPT-4, demonstrating a powerful and accessible new paradigm for automated hyperparameter design.Our code is available at https://anonymous.4open.science/r/AutoEP-3E11.

## One-Sentence Claim

AutoEP uses online exploratory landscape analysis plus multi-LLM reasoning to adapt metaheuristic hyperparameters zero-shot, outperforming learned and LLM-based tuners.

## Problem

Dynamic hyperparameter configuration is central for metaheuristic optimization, but learning-based tuners can require many samples and generalize poorly.

LLMs can reason about algorithm control, but unguided reasoning may hallucinate strategies disconnected from actual search dynamics.

## Core Contribution

The paper introduces AutoEP, a training-free framework for automated hyperparameter evolution in metaheuristic algorithms.

Its core is the synergy between online Exploratory Landscape Analysis, which summarizes search dynamics quantitatively, and a multi-LLM reasoning chain that converts feedback into adaptive hyperparameter strategies.

## Method

AutoEP observes the current optimization landscape and search process through ELA features.

Multiple LLM reasoning stages interpret those features, propose hyperparameter updates, and ground decisions in empirical search feedback rather than static heuristics.

## Experiments and Evidence

The abstract reports evaluation on three metaheuristics across diverse combinatorial optimization benchmarks.

AutoEP consistently outperforms state-of-the-art tuners, including neural evolution and other LLM-based methods. Open-source Qwen3-30B matches GPT-4 performance in the framework.

## Limits and Failure Modes

ELA features may not capture all search dynamics, and LLM reasoning quality can vary across problem classes. Training-free operation may still incur inference cost and prompt sensitivity.

Because this note is abstract-only, details still need checking: metaheuristics used, ELA feature set, reasoning-chain prompts, benchmarks, tuning budget, and ablations for each component.

## Deep Themes

- LLMs as algorithm controllers: language models reason over optimization diagnostics rather than generate final answers.
- Grounded zero-shot tuning: empirical landscape features constrain LLM strategy generation.
- Hyperparameter evolution without training: adaptation happens online through feedback interpretation.
- Accessible automation: open-source models can match proprietary performance when scaffolded with quantitative signals.

## Subthemes

- Exploratory Landscape Analysis.
- Metaheuristic algorithms.
- Multi-LLM reasoning chain.
- Automated hyperparameter design.

## Connections to Other Papers

This connects to HTI, GEPA, HGM, AgentFlow, and algorithm-design/search papers.

It also relates to optimization-control themes where model reasoning is grounded in real-time metrics.

## Notes for Cross-Paper Synthesis

AutoEP adds a metric-grounded LLM-control theme: language reasoning becomes more reliable when coupled to quantitative online diagnostics.
