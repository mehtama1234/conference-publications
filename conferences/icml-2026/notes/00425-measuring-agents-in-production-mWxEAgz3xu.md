# Measuring Agents in Production

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: mWxEAgz3xu
- Authors: Melissa Pan; Negar Arabzadeh; Riccardo Cogo; Yuxuan Zhu; Alexander Xiong; Lakshya A Agrawal; Huanzhi Mao; Emma Shen; Sid Pallerla; Liana Patel; Shu Liu; Tianneng Shi; Xiaoyuan Liu; Jared Quincy Davis; Emmanuele Lacavalla; Alessandro Basile; Shuyi Yang; Paul Castro; Daniel Kang; Koushik Sen; Dawn Song; Joseph E. Gonzalez; Ion Stoica; Matei Zaharia; Marquita Ellis
- Primary area: applications
- Keywords: AI Agents;Agentic Systems;ML Systems;Survey;Evaluations;Agents
- Source URL: https://openreview.net/forum?id=mWxEAgz3xu
- PDF URL: https://openreview.net/pdf?id=mWxEAgz3xu

## Abstract

LLM-based agents already operate in production across many industries, yet we lack an understanding of what technical methods make deployments successful.
We present the first systematic study of **M**easuring **A**gents in **P**roduction, MAP, using first-hand data from agent developers. We conducted 20 case studies via in-depth interviews and surveyed 86 deployed systems practitioners across 26 domains.
We investigate why organizations build agents, how they build them, how they evaluate them, and their top development challenges.
Our study finds that production agents are built using simple, controllable approaches:
68% execute at most 10 steps before human intervention, 70% rely on prompting off-the-shelf models instead of weight tuning, and 74% depend primarily on human evaluation.
Reliability (consistent correct behavior over time) remains the top development challenge, which practitioners currently address through systems-level design.
MAP documents the current state of production agents, providing the research community with visibility into deployment realities and underexplored research avenues.

## One-Sentence Claim

MAP shows that production agents are currently simple, human-supervised, prompting-based systems, with reliability addressed mainly through systems design rather than sophisticated model training.

## Problem

LLM agents are already deployed across industries, but research benchmarks often do not reflect production practice. The field lacks systematic evidence about why organizations build agents, how they build and evaluate them, and what technical bottlenecks matter most.

The paper asks what deployed agent systems actually look like and where research should focus.

## Core Contribution

MAP is a systematic study of Measuring Agents in Production using firsthand developer data. It includes 20 in-depth case-study interviews and a survey of 86 deployed-systems practitioners across 26 domains.

The key finding is that production agents use simple controllable approaches: most have short horizons before human intervention, rely on prompting off-the-shelf models, and depend primarily on human evaluation.

## Method

The authors combine qualitative interviews with a broader practitioner survey. They analyze motivations, architecture choices, evaluation approaches, and top development challenges across deployed agent systems.

The study emphasizes deployment realities rather than benchmark-only performance.

## Experiments and Evidence

Evidence reported in the abstract:

- 20 case studies via in-depth interviews.
- 86 deployed-systems practitioners surveyed.
- 26 domains represented.
- 68% of production agents execute at most 10 steps before human intervention.
- 70% rely on prompting off-the-shelf models rather than weight tuning.
- 74% primarily use human evaluation.
- Reliability is the top development challenge.
- Practitioners address reliability mainly through systems-level design.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: sampling bias, domain distribution, and coding methodology.

## Limits and Failure Modes

- Survey results may overrepresent accessible or willing practitioners.
- Production practices change quickly as tooling evolves.
- Human evaluation prevalence may reflect lack of tooling rather than best practice.
- The study describes current deployments, not necessarily ideal future architectures.

## Deep Themes

**Production agents are conservative.** Deployed systems prioritize controllability, short horizons, and human oversight.

**Reliability is a systems problem.** Practitioners manage failures through architecture and process, not only model tuning.

**Benchmarks need deployment grounding.** Research priorities should reflect what agent builders actually struggle with.

## Subthemes

- Production agent survey.
- Human-in-the-loop agent deployment.
- Prompting over weight tuning.
- Short-horizon workflows.
- Reliability through systems design.

## Connections to Other Papers

Connects to ThunderAgent, Vision2Web, RoTS, MADQA, and VenusBench-Mobile. It provides empirical production context for the agent-evaluation and systems papers.

## Notes for Cross-Paper Synthesis

MAP anchors the agent theme in deployment evidence: long-horizon autonomy remains rare, and reliability work should account for human intervention, monitoring, and systems constraints.
