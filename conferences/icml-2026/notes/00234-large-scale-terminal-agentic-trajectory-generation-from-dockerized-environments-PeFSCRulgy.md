# Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: PeFSCRulgy
- Authors: Siwei Wu; Yizhi LI; Yuyang Song; Wei Zhang; Yang Wang; Riza Batista-Navarro; Xian Yang; Mingjie Tang; Bryan Dai; Jian Yang; Chenghua Lin
- Primary area: deep_learning->large_language_models
- Keywords: Agentic Model;Terminal;Code Agent
- Source URL: https://openreview.net/forum?id=PeFSCRulgy
- PDF URL: https://openreview.net/pdf?id=PeFSCRulgy

## Abstract

Training agentic models for terminal-based tasks critically depends on high-quality terminal trajectories that capture realistic long-horizon interactions across diverse domains.
However, constructing such data at scale remains challenging due to two key requirements:
\textbf{\emph{Executability}}, since each instance requires a suitable and often distinct Docker environment;
and \textbf{\emph{Verifiability}}, because heterogeneous task outputs preclude unified, standardized verification.
To address these challenges, we propose \textbf{TerminalTraj}, a scalable pipeline that (i) filters high-quality repositories to construct Dockerized execution environments, (ii) generates Docker-aligned task instances, and (iii) synthesizes agent trajectories with executable validation code.
Using TerminalTraj, we curate 32K Docker images and generate 50,733 verified terminal trajectories across eight domains.
Models trained on this data with the Qwen2.5-Coder backbone achieve consistent performance improvements on TerminalBench (TB), with gains of up to 20\% on TB 1.0 and 10\% on TB 2.0 over their respective backbones.
Notably, \textbf{TerminalTraj-32B} achieves strong performance among models with fewer than 100B parameters, reaching 35.30\% on TB 1.0 and 22.00\% on TB 2.0, and demonstrates improved test-time scaling behavior.

## One-Sentence Claim

TerminalTraj generates large-scale verified terminal-agent trajectories by constructing Dockerized environments, Docker-aligned tasks, and executable validation code.

## Problem

Training terminal agents requires realistic long-horizon trajectories, but scaling such data is hard because each task needs an executable environment and heterogeneous outputs need reliable verification.

## Core Contribution

The paper introduces a scalable pipeline that curates 32K Docker images and produces 50,733 verified terminal trajectories across eight domains, improving TerminalBench performance.

## Method

TerminalTraj filters high-quality repositories, builds Dockerized environments, generates task instances aligned with those environments, and synthesizes agent trajectories with executable validation code.

## Experiments and Evidence

The abstract reports Qwen2.5-Coder-based models trained on TerminalTraj improve up to 20% on TerminalBench 1.0 and 10% on TerminalBench 2.0, with TerminalTraj-32B reaching 35.30% and 22.00% respectively and improved test-time scaling.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: repository filtering criteria, trajectory synthesis quality, validation-code reliability, domain coverage, leakage risk, and whether generated trajectories teach brittle shortcuts.

## Deep Themes

- Agent training data must be executable and verifiable.
- Dockerized environments turn repositories into scalable task worlds.
- Terminal agents need long-horizon trajectories across realistic domains.

## Subthemes

- Terminal agents.
- Code agents.
- Docker environments.
- Verified trajectories.
- TerminalBench.
- Test-time scaling.

## Connections to Other Papers

Connects to MEnvAgent, tau2-bench, CE-Graph, and SWE agent benchmarks through executable environment construction and verifiable process data.

## Notes for Cross-Paper Synthesis

TerminalTraj adds a data-generation counterpart to MEnvAgent: executable environments are not only benchmarks, they are factories for agent training trajectories.
