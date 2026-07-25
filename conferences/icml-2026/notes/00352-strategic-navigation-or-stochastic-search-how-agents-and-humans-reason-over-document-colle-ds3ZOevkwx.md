# Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: ds3ZOevkwx
- Authors: Łukasz Borchmann; Jordy Van Landeghem; Michał Turski; Shreyansh Padarha; Ryan Othniel Kearns; Adam Mahdi; Niels Rogge; Clémentine Fourrier; Siwei Han; Huaxiu Yao; Artemis Llabrés; Yiming Xu; Dimosthenis Karatzas; Hao Zhang; Anupam Datta
- Primary area: general_machine_learning->evaluation
- Keywords: Benchmarking;Evaluation Methodology;LLMs;Agents;Document Understanding
- Source URL: https://openreview.net/forum?id=ds3ZOevkwx
- PDF URL: https://openreview.net/pdf?id=ds3ZOevkwx

## Abstract

Multimodal agents offer a promising path to automating complex document-intensive workflows. Yet, a critical question remains: do these agents demonstrate genuine strategic reasoning, or merely stochastic trial-and-error search?  To address this, we introduce MADQA, a benchmark of 2,250 human-authored questions grounded in 800 heterogeneous PDF documents. Guided by Classical Test Theory, we design it to maximize discriminative power across varying levels of agentic abilities. To evaluate agentic behavior, we introduce a novel protocol that measures the accuracy-effort trade-off. Using this framework, we show that while the best agents can match human searchers in raw accuracy, they succeed on largely different questions and rely on brute-force search to compensate for weak strategic planning. They fail to close the nearly 20\% gap to oracle performance, persisting in unproductive loops. We release the dataset and evaluation harness to help facilitate the transition from brute-force retrieval to calibrated, efficient reasoning.

## One-Sentence Claim

MADQA shows that strong document agents can match human raw accuracy while still relying on inefficient stochastic search rather than human-like strategic navigation.

## Problem

Multimodal agents are increasingly used for document-heavy workflows, but headline accuracy does not reveal whether they reason strategically over document collections or simply spend more search effort.

The paper targets the gap between task success and process quality: an agent may answer correctly while looping, over-searching, or solving a different subset of problems than humans.

## Core Contribution

The contribution is MADQA, a benchmark of 2,250 human-authored questions over 800 heterogeneous PDFs, plus an evaluation protocol for the accuracy-effort tradeoff. The benchmark is designed using Classical Test Theory to discriminate between different levels of agent ability.

The key finding is diagnostic: the best agents approach human raw accuracy but succeed on different questions, fail to close a large oracle gap, and compensate for weak planning with brute-force search.

## Method

The benchmark grounds questions in heterogeneous PDF document collections. The evaluation measures not only correctness but also effort, enabling comparisons between humans, agents, and oracle behavior.

Classical Test Theory guides item construction and selection so that the benchmark has discriminative power rather than merely collecting plausible document QA tasks.

## Experiments and Evidence

Evidence reported in the abstract:

- 2,250 human-authored questions.
- 800 heterogeneous PDF documents.
- Best agents match human searchers in raw accuracy.
- Agents and humans solve largely different questions.
- Agents fail to close a nearly 20% gap to oracle performance.
- Agents persist in unproductive loops and use brute-force search to compensate for weak planning.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: agent set, effort metric, oracle construction, document types, and failure taxonomy.

## Limits and Failure Modes

- Benchmark conclusions depend on how effort is measured and normalized across humans and agents.
- Human-authored questions improve realism but may encode assumptions about document navigation style.
- Oracle gap interpretation depends on oracle accessibility and whether oracle evidence mirrors realistic workflows.
- Agents may improve through tool policies without improving underlying strategic reasoning.

## Deep Themes

**Accuracy is not enough for agents.** Process traces and effort budgets reveal capability gaps hidden by final answers.

**Strategic navigation is a distinct capability.** Document reasoning requires choosing where to look, when to stop, and how to avoid loops.

**Benchmarks are becoming behavioral instruments.** MADQA measures policy shape, not just output correctness.

## Subthemes

- Accuracy-effort tradeoff.
- Document-agent planning.
- Human-agent disagreement.
- Classical Test Theory for benchmark design.
- Looping and brute-force search diagnostics.

## Connections to Other Papers

Connects to VenusBench-Mobile, BlitzRank, Monitoring Monitorability, Finite Test Certification, and daVinci-Dev. It also pairs naturally with When to Trust the Cheap Check because both evaluate when cheap or partial evidence is enough for action.

## Notes for Cross-Paper Synthesis

MADQA strengthens the agent-evaluation theme: 2026 benchmarks are increasingly judging search policy, resource use, and failure process, not just final task accuracy.
