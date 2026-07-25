# Huxley-G\"odel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: T0EiEuhOOL
- Authors: Wenyi Wang; Piotr Piękos; Li Nanbo; Firas Laakom; Yimeng Chen; Mateusz Ostaszewski; Mingchen Zhuge; Jürgen Schmidhuber
- Primary area: transfer learning, meta learning, and lifelong learning
- Keywords: Self-Improvement;Coding Agents;G\"odel Machine
- Source URL: https://openreview.net/forum?id=T0EiEuhOOL
- PDF URL: https://openreview.net/pdf?id=T0EiEuhOOL

## Abstract

Recent studies operationalize self-improvement through coding agents that edit their own codebases, grow a tree of self-modifications through expansion strategies that favor higher software engineering benchmark performance, 
considering that this implies more promising subsequent self-modifications. However, we identify a mismatch between the agent’s self-improvement potential (metaproductivity) and its coding benchmark performance, namely the \emph{Metaproductivity-Performance~Mismatch}. Inspired by Huxley’s concept of clade, we propose a metric ($\mathrm{CMP}$) that aggregates the benchmark performances of the \emph{descendants} of an agent as an indicator of its potential for self-improvement. We show that the G\"odel Machine, the optimal self-improving machine, is achieved with access to true $\mathrm{CMP}$. We introduce the Huxley-G\"odel Machine (HGM), which, by estimating $\mathrm{CMP}$ and using it as guidance, searches the tree of self-modifications. On SWE-bench Verified and Polyglot, HGM outperforms prior self-improving coding agent search methods while using less wall-clock time. Moreover, the agent optimized by HGM on SWE-bench Verified outperforms SWE-agent, a leading human-engineered open source coding agent on SWE-bench Lite, where SWE-agent ranks the best on the official leaderboard, when both use the GPT-5-mini backbone, demonstrating that HGM self-improvement indeed enhances genuine coding capability.

## One-Sentence Claim

Huxley-Goedel Machine guides self-improving coding-agent search with a descendant-performance metric that better captures metaproductivity than the current agent's benchmark score.

## Problem

Self-improving coding agents often search over self-modifications using current benchmark performance as the selection signal.

The paper argues this can miss agents with high self-improvement potential: an agent may not score best now but may produce descendants that improve more effectively. This is the metaproductivity-performance mismatch.

## Core Contribution

The paper proposes CMP, a clade-inspired metric aggregating benchmark performance of an agent's descendants as an indicator of self-improvement potential.

It shows that access to true CMP would recover the Goedel Machine ideal, then introduces Huxley-Goedel Machine, which estimates CMP to guide search over self-modification trees.

## Method

HGM grows a tree of coding-agent self-modifications. Instead of ranking nodes only by their own benchmark performance, it estimates the future performance of their descendant clades.

This shifts search toward modifications that increase the agent's capacity to generate useful future modifications.

## Experiments and Evidence

The abstract reports results on SWE-bench Verified and Polyglot.

HGM outperforms prior self-improving coding-agent search methods while using less wall-clock time. An HGM-optimized agent using GPT-5-mini outperforms SWE-agent on SWE-bench Lite under the same backbone.

## Limits and Failure Modes

CMP estimation may be expensive or noisy, and optimizing descendant performance could overfit to benchmark ecosystems. Self-modifying code also raises safety, reproducibility, and provenance concerns.

Because this note is abstract-only, details still need checking: self-modification language, expansion strategy, CMP estimator, benchmark protocols, compute budget, and safeguards against degenerate self-edits.

## Deep Themes

- Metaproductivity: the value of an agent includes its ability to create better descendants.
- Search over self-modification trees: coding agents become evolving software lineages.
- Benchmark performance versus improvement potential: current score is an incomplete objective for self-improvement.
- Approximate Goedel-machine framing: theoretical self-improvement ideas are operationalized through coding benchmarks.

## Subthemes

- Self-improving coding agents.
- CMP descendant-performance metric.
- Clade-inspired search.
- SWE-bench and Polyglot.

## Connections to Other Papers

This connects to GEPA, AgentFlow, RefineStat, MEnvAgent, and SWE-agent benchmark work through search over agent/program improvements.

It also relates to Train-before-Test because both distinguish current observed score from latent potential after adaptation.

## Notes for Cross-Paper Synthesis

HGM adds a long-horizon meta-optimization theme: the key unit of progress may be an agent lineage's capacity to improve, not a single model snapshot's score.
