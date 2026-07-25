# Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9sg34nj13o
- Authors: Junyi Li; Xiaowei Qian; Yingyi Zhang; Wenlin Zhang; Guojing Li; Sheng Zhang; Xiao Han; Yichao Wang; Xiangyu Zhao
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;Multi-Objective Optimization;Reinforcement Learning
- Source URL: https://openreview.net/forum?id=9sg34nj13o
- PDF URL: https://openreview.net/pdf?id=9sg34nj13o

## Abstract

Recent advances in tool-integrated language agents have significantly improved their ability to solve complex reasoning tasks. However, existing alignment methods predominantly focus on maximizing task accuracy, while overlooking auxiliary objectives such as tool-use efficiency, which are essential for practical deployment. To address this gap, we introduce \textbf{ParetoPO}, a two-stage multi-objective optimization framework for aligning tool-using large language models (LLMs) under competing objectives. In the first stage, ParetoPO leverages hypervolume-guided dynamic scalarization to adapt reward weights based on global Pareto frontier progress. In the second stage, it replaces scalarized learning signals with Pareto-ranking-based advantage computation, promoting nondominated trajectories through dominance-aware credit assignment. This design enables fine-grained, action-level optimization across multiple conflicting objectives. Experimental results on mathematic reasoning and multi-hop QA tasks show that ParetoPO consistently discovers policies with superior accuracy-efficiency trade-offs compared to static and heuristic baselines. Our code is publicly available at https://github.com/Applied-Machine-Learning-Lab/ICML2026_ParetoPO.

## One-Sentence Claim

ParetoPO aligns tool-integrated LLM agents across competing objectives such as task accuracy and tool-use efficiency using Pareto-aware policy optimization.

## Problem

Tool-using agent training often optimizes task accuracy while ignoring auxiliary deployment objectives like tool efficiency, creating policies that may be accurate but impractical.

## Core Contribution

The paper introduces ParetoPO, a two-stage multi-objective RL framework using hypervolume-guided dynamic scalarization followed by Pareto-ranking-based advantage computation.

## Method

Stage one adapts reward weights according to global Pareto frontier progress. Stage two replaces scalarized learning signals with dominance-aware advantage computation that promotes nondominated trajectories and supports action-level credit assignment across objectives.

## Experiments and Evidence

The abstract reports mathematical reasoning and multi-hop QA experiments where ParetoPO finds better accuracy-efficiency tradeoffs than static and heuristic baselines.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv is currently being deferred after repeated 429/503 errors. Details still need checking: objective definitions, hypervolume estimation stability, tool-cost accounting, and whether Pareto gains hold under harder tool environments.

## Deep Themes

- Agent alignment is multi-objective, not single-reward maximization.
- Tool use needs efficiency-aware credit assignment.
- Pareto frontiers provide a richer deployment target than scalar accuracy.

## Subthemes

- Tool-integrated agents.
- Multi-objective RL.
- Pareto ranking.
- Hypervolume scalarization.
- Accuracy-efficiency tradeoff.
- Action-level credit assignment.

## Connections to Other Papers

Connects to DR Tulu, Skill-Pro, MASPOB, and rubric-guided reasoning work through agent optimization beyond static correctness. It also links to efficiency papers via tool-cost control.

## Notes for Cross-Paper Synthesis

ParetoPO adds a multi-objective agent theme: the right policy is not merely the most accurate one, but one lying on a useful accuracy-cost frontier.
