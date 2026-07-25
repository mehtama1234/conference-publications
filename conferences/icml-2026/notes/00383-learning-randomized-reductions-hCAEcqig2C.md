# Learning Randomized Reductions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: hCAEcqig2C
- Authors: Ferhat Erata; Orr Paradise; Thanos Typaldos; Timos Antonopoulos; ThanhVu Nguyen; Shafi Goldwasser; Ruzica Piskac
- Primary area: applications
- Keywords: Self-Correcting Programs;Random Self-Reducibility;LLM Agents;Neuro-Symbolic Learning
- Source URL: https://openreview.net/forum?id=hCAEcqig2C
- PDF URL: https://openreview.net/pdf?id=hCAEcqig2C

## Abstract

Randomized self-reductions (RSRs) express $f(x)$ using $f$ evaluated at random correlated points, enabling self-correcting programs, instance-hiding protocols, and applications in complexity theory and cryptography. Yet discovering RSRs has required manual expert derivation for over 40 years, limiting their practical use.
We present Bitween for automated RSR learning. First, we formalize RSR learning with sample complexity analysis under correlated sampling. Second, we develop Vanilla Bitween, which integrates multiple backends (linear regression, genetic programming, symbolic regression, and mixed-integer programming). The linear regression backend outperforms the others, discovering RSRs for 43 of 80 functions (54%) in RSR-Bench, our benchmark suite, including the first known reduction for sigmoid. Third, we introduce Agentic Bitween, a neuro-symbolic approach where LLM agents propose novel query functions beyond the fixed set ($x+r$, $x-r$, $x \cdot r$, $x$, $r$) in prior work. Agentic Bitween discovers RSRs for 64 of 80 functions (80%), outperforming pure neural baselines in both RSR discovery and verification accuracy.

## One-Sentence Claim

Bitween automates discovery of randomized self-reductions, using symbolic backends and LLM agents to find reductions that previously required expert manual derivation.

## Problem

Randomized self-reductions express f(x) through evaluations of f at correlated random points. They support self-correcting programs, instance hiding, and complexity-theoretic or cryptographic constructions, but historically they have been derived manually by experts.

The paper asks whether RSR discovery itself can be learned and benchmarked.

## Core Contribution

The paper formalizes RSR learning with sample complexity under correlated sampling and introduces RSR-Bench. It develops Vanilla Bitween, combining linear regression, genetic programming, symbolic regression, and mixed-integer programming backends.

It then introduces Agentic Bitween, where LLM agents propose novel query functions beyond a fixed hand-designed set. Agentic Bitween discovers RSRs for 64 of 80 benchmark functions, compared with 43 of 80 for the best Vanilla backend.

## Method

Vanilla Bitween searches for reductions using multiple symbolic or statistical backends over a fixed query-function set. The linear regression backend performs strongest among those options.

Agentic Bitween adds a neuro-symbolic loop: LLM agents propose new query forms, which are then verified for reduction discovery and correctness.

## Experiments and Evidence

Evidence reported in the abstract:

- Formal RSR learning setup and sample complexity analysis.
- RSR-Bench with 80 functions.
- Vanilla Bitween discovers RSRs for 43 of 80 functions.
- First known reduction for sigmoid.
- Agentic Bitween discovers RSRs for 64 of 80 functions.
- Outperforms pure neural baselines in RSR discovery and verification accuracy.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: benchmark function set, verification criteria, agent prompting, and false-discovery controls.

## Limits and Failure Modes

- LLM-proposed reductions need rigorous verification; plausible symbolic forms can be wrong.
- Benchmarked functions may not reflect harder cryptographic or complexity-theoretic targets.
- Search may favor simple algebraic reductions over deeper constructions.
- Correlated sampling assumptions determine sample complexity and verification reliability.

## Deep Themes

**Agents can propose mathematics, but verification remains essential.** LLMs expand the search space while symbolic checks protect correctness.

**Neuro-symbolic discovery is moving into theory tooling.** The system automates a task previously requiring expert derivation.

**Benchmarks make abstract discovery learnable.** RSR-Bench turns reduction finding into an empirical ML problem.

## Subthemes

- Randomized self-reductions.
- Self-correcting programs.
- Neuro-symbolic search.
- Agent-proposed query functions.
- Verification-backed discovery.

## Connections to Other Papers

Connects to Formal Problem-Solving, 2-SAT Robustness, daVinci-Dev, Agent0-VL, and finite-test certification. It shares the agentic-discovery pattern where models search but formal or symbolic systems certify.

## Notes for Cross-Paper Synthesis

Bitween extends the agent theme from solving tasks to discovering reusable algorithms. The deeper pattern is LLMs as proposal engines embedded in verified symbolic pipelines.
