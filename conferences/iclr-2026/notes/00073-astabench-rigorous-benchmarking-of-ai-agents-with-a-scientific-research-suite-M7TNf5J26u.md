# AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: M7TNf5J26u
- Authors: Jonathan Bragg; Mike D'Arcy; Nishant Balepur; Dan Bareket; Bhavana Dalvi Mishra; Sergey Feldman; Dany Haddad; Jena D. Hwang; Peter Jansen; Varsha Kishore; Bodhisattwa Prasad Majumder; Aakanksha Naik; Sigal Rahamimov; Kyle Richardson; Amanpreet Singh; Harshit Surana; Aryeh Tiktinsky; Rosni Vasu; Guy Wiener; Chloe Anastasiades; Stefanus Candra; Jason Dunkelberger; Daniel Emery; Rob Evans; Malachi Hamada; Regan Huff; Rodney Kinney; Matt Latzke; Jaron Lochner; Ruben Lozano-Aguilera; Ngoc-Uyen Nguyen; Smita Rao; Amber Tanaka; Brooke Vlahos; Peter Clark; Doug Downey; Yoav Goldberg; Ashish Sabharwal; Daniel S Weld
- Primary area: datasets and benchmarks
- Keywords: Agents;evaluation;benchmarks;scientific research
- Source URL: https://openreview.net/forum?id=M7TNf5J26u
- PDF URL: https://openreview.net/pdf?id=M7TNf5J26u

## Abstract

AI agents hold the potential to revolutionize scientific productivity by automating literature reviews, replicating experiments, analyzing data, and even proposing new directions of inquiry; indeed, there are now many such agents, ranging from general-purpose "deep research" systems to specialized science-specific agents, such as AI Scientist and AIGS.  Rigorous evaluation of these agents is critical for  progress. Yet existing benchmarks fall short on several fronts: they often (1) lack reproducible agent tools necessary for a controlled comparison of core agentic capabilities; (2) do not account for confounding variables such as model cost and tool access; (3) do not provide standardized interfaces for quick agent prototyping and evaluation; (4) fail to provide holistic, product-informed measures of real-world use cases such as science research; and (5) lack comprehensive baseline agents necessary to identify true advances.  In response, we define principles and tooling for more rigorously benchmarking agents. Using these, we present AstaBench, a suite that provides a holistic measure of agentic ability to perform scientific research, comprising 2400+ problems spanning the entire scientific discovery process and multiple scientific domains, and including many problems inspired by actual user requests to deployed Asta agents.  Our suite comes with the first scientific research environment with production-grade search tools that enable controlled, reproducible evaluation, better accounting for confounders.  Alongside, we provide a comprehensive suite of nine science-optimized classes of Asta agents and numerous baselines.  Our extensive evaluation of 57 agents across 22 agent classes reveals several interesting findings, most importantly that despite meaningful progress on certain individual aspects, AI remains far from solving the challenge of science research assistance.

## One-Sentence Claim

AstaBench provides a controlled, production-tool-grounded benchmark suite for evaluating scientific research agents across the discovery process while accounting for tool access, cost, and baseline confounders.

## Problem

Scientific research agents promise to automate literature review, experiment replication, data analysis, and hypothesis generation, but existing benchmarks often lack controlled tools, standardized interfaces, cost accounting, and realistic product-informed measures.

Without strong baselines and reproducible environments, it is hard to tell whether an apparent agent advance reflects better reasoning, better tool access, more expensive models, or benchmark artifacts.

## Core Contribution

The paper defines principles and tooling for rigorous scientific-agent benchmarking and introduces AstaBench.

AstaBench includes more than 2,400 problems spanning the scientific discovery process, production-grade controlled search tools, nine science-optimized Asta agent classes, and many baselines.

## Method

The benchmark standardizes agent interfaces and tool access so agents can be compared under controlled conditions.

Problems are drawn from multiple scientific domains and include tasks inspired by actual user requests to deployed Asta agents, making the suite more representative of real science-assistance workflows.

## Experiments and Evidence

The abstract reports evaluation of 57 agents across 22 agent classes.

The main finding is that agents show meaningful progress on individual aspects of research assistance, but remain far from solving end-to-end scientific research support.

## Limits and Failure Modes

Scientific research is broad and difficult to benchmark exhaustively. Production-inspired tasks may still miss rare expert workflows, tacit judgment, or long-term research programs where success is not immediately verifiable.

Because this note is abstract-only, details still need checking: task taxonomy, scoring rubrics, search-tool controls, cost normalization, agent classes, and which capabilities remain weakest.

## Deep Themes

- Agent evaluation with confounder control: benchmarks must isolate model quality from tool and cost advantages.
- Product-informed scientific tasks: deployed-user requests become a source of realistic benchmark design.
- Scientific discovery as a multi-stage workflow: literature, replication, analysis, and ideation require different agent skills.
- Baselines as measurement infrastructure: rigorous evaluation needs broad reference agents, not only top-line leaderboard scores.

## Subthemes

- Scientific research agents.
- Controlled production-grade search tools.
- Cost and tool-access accounting.
- Comprehensive baseline suites.

## Connections to Other Papers

This connects to MC-Search, SimuHome, Gaia2, WebDevJudge, FRABench, and In the Flow through agent benchmarking that emphasizes process, tools, and deployment constraints.

It also connects to Q-RAG because scientific agents depend heavily on reliable multi-step retrieval over long contexts.

## Notes for Cross-Paper Synthesis

AstaBench raises the bar for agent evaluation: useful benchmarks must control the environment, tools, cost, and baseline space before claiming agentic progress.
