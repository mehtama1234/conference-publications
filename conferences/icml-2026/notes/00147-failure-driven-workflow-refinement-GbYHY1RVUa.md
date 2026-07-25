# Failure-Driven Workflow Refinement

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: GbYHY1RVUa
- Authors: Jusheng Zhang; Kaitong Cai; Jing Yang; Ziliang Chen; Yongsen Zheng; Kwok-Yan Lam; Liang Lin; Keze Wang
- Primary area: optimization
- Keywords: LLM workflows;agentic systems;counterexample-guided optimization;failure mode modeling
- Source URL: https://openreview.net/forum?id=GbYHY1RVUa
- PDF URL: https://openreview.net/pdf?id=GbYHY1RVUa

## Abstract

Workflow optimization for tool-using LLM agents is often cast as global search over candidate graphs, scored by a scalar metric. This collapses rich, multi-step failure traces into binary outcomes, obscuring recurring failure structure and making refinement inefficient. We reframe optimization as \emph{distributional refinement}: each workflow induces a density over a \textbf{Failure Signature Space} $\mathcal{F}$, and the goal is to minimize its \textbf{Expected Failure Mass}. We propose \textbf{CE-Graph}, which maintains a counterexample pool, estimates dense failure modes, and applies operator-constrained graph edits via a \textbf{Propose-and-Verify} loop with a convergence-aware stopping rule. Across math, code, and QA benchmarks, CE-Graph improves robustness while reducing optimization cost compared to strong workflow-search baselines, suggesting reliability emerges from learning and reshaping failure landscapes rather than merely maximizing aggregate success rates.

## One-Sentence Claim

CE-Graph optimizes LLM-agent workflows by modeling and reducing dense failure modes rather than globally searching graphs by aggregate scalar scores.

## Problem

Workflow search collapses multi-step failure traces into binary outcomes, hiding recurring failure structure and making tool-agent refinement inefficient.

## Core Contribution

The paper reframes workflow optimization as distributional refinement over a Failure Signature Space and proposes CE-Graph.

## Method

CE-Graph maintains a counterexample pool, estimates dense regions of failure mass, applies operator-constrained graph edits, and uses a Propose-and-Verify loop with convergence-aware stopping.

## Experiments and Evidence

The abstract reports improved robustness and lower optimization cost than strong workflow-search baselines across math, code, and QA benchmarks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: failure-signature representation, graph-edit operators, verifier reliability, and scalability to large workflows.

## Deep Themes

- Agent workflows should be refined by failure distributions, not only success rates.
- Counterexamples can guide targeted graph edits.
- Reliability emerges from reshaping failure landscapes.

## Subthemes

- LLM workflows.
- Agentic systems.
- Counterexample-guided optimization.
- Failure mode modeling.
- Workflow graph edits.
- Propose-and-Verify loops.

## Connections to Other Papers

Connects to MASPOB, OMAC, DR Tulu, Jailbreak Foundry, and CVE-Factory through agent workflow optimization and executable evaluation.

## Notes for Cross-Paper Synthesis

Failure-driven refinement adds a failure-landscape theme: agent optimization improves when recurring errors become structured objects of search.
