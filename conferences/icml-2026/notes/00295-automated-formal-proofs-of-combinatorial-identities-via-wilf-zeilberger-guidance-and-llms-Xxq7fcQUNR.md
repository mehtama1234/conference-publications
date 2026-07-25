# Automated Formal Proofs of Combinatorial Identities via Wilf–Zeilberger Guidance and LLMs

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Xxq7fcQUNR
- Authors: Beibei Xiong; Hangyu Lv; Junqi Liu; Yisen Wang; Shaoshi Chen; Jianlin Wang; Zhengfeng Yang; Lihong Zhi
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;Automated Theorem Proving;Combinatoral Identity;Wilf–Zeilberger (WZ) Method
- Source URL: https://openreview.net/forum?id=Xxq7fcQUNR
- PDF URL: https://openreview.net/pdf?id=Xxq7fcQUNR

## Abstract

Automating formal proofs of combinatorial identities is challenging for LLM-based provers, as long-horizon proof planning is required and unconstrained search quickly explodes. 
Symbolic methods such as the Wilf--Zeilberger (WZ) method can achieve a mechanized proof of combinatorial identities by constructing special auxiliary functions and demonstrating that they satisfy specific recurrence relations. 
We propose WZ-LLM, a neuro-symbolic framework that turns WZ proof plans into executable proof sketches in Lean~4 and uses an LLM-based prover 
to discharge the resulting machine-checkable subgoals.
We also train a dedicated WZ-Prover via a Lean-kernel-verified bootstrapping loop with expert-verified iteration, followed by DAPO-based refinement.
Experiments show that WZ-LLM achieves a 34\% proof success rate on LCI-Test  (100 classical combinatorial identities), outperforming strong baselines such as DeepSeek-V3 and Goedel-Prover-V2; 
moreover, on LCI-Test it proves 5 identities on which the symbolic-only baseline fails. 
WZ-LLM also improves performance on CombiBench and PutnamBench-Comb, suggesting the effectiveness of coupling symbolic proof sketches with learned formal reasoning.
Experiments show that WZ-LLM achieves a 34\% proof success rate on LCI-Test (100 classic combinatorial identities), outperforming strong baselines such as DeepSeek-V3 and Goedel-Prover-V2, and delivering consistent gains on CombiBench and PutnamBench-Comb. These results indicate that our framework provides two complementary strengths: improved direct proving for identities beyond the scope of WZ, and substantially higher end-to-end success when WZ sketches guide a specialized prover.

## One-Sentence Claim

WZ-LLM improves formal proofs of combinatorial identities by turning Wilf-Zeilberger proof plans into Lean sketches that guide specialized LLM proving.

## Problem

LLM-based theorem provers struggle with combinatorial identities because long-horizon proof planning creates a large unconstrained search space. Symbolic Wilf-Zeilberger methods can mechanize many identity proofs by constructing auxiliary functions and recurrence relations, but symbolic-only methods have limits.

The paper asks how to combine symbolic WZ structure with learned formal proving in Lean.

## Core Contribution

The paper proposes WZ-LLM, a neuro-symbolic framework that converts WZ proof plans into executable Lean 4 proof sketches, then uses an LLM prover to discharge machine-checkable subgoals.

It also trains WZ-Prover using a Lean-kernel-verified bootstrapping loop with expert-verified iteration, followed by DAPO-based refinement. On LCI-Test, WZ-LLM achieves 34 percent proof success and proves some identities where symbolic-only WZ fails.

## Method

The framework uses symbolic WZ guidance to structure proof search. The WZ method supplies recurrence-oriented proof sketches and auxiliary-function structure. Lean 4 checks the resulting formal obligations, while an LLM-based prover fills subgoals.

Training bootstraps from kernel-verified proofs, filters or improves them with expert verification, then applies DAPO-style refinement to specialize the prover.

## Experiments and Evidence

Evidence reported in the abstract:

- 34 percent proof success on LCI-Test with 100 classical combinatorial identities.
- Outperforms DeepSeek-V3 and Goedel-Prover-V2 baselines.
- Proves 5 LCI-Test identities where symbolic-only WZ fails.
- Improves performance on CombiBench and PutnamBench-Comb.
- Lean-kernel-verified bootstrapping and expert-verified iteration.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: exact proof-search budget, DAPO setup, baseline prompts/tooling, and whether duplicate abstract claims reflect metadata duplication.

## Limits and Failure Modes

- The approach is tailored to combinatorial identities where WZ-style structure applies.
- Proof success remains 34 percent on LCI-Test, leaving many unsolved cases.
- Expert-verified iteration may limit scalability.
- Lean formalization overhead can dominate for identities not easily mapped to WZ sketches.

## Deep Themes

**Symbolic plans constrain neural proof search.** The LLM is most useful when a mathematical method supplies the proof skeleton.

**Verification loops create trustworthy training data.** Lean-kernel checks and expert iteration reduce hallucinated proof risk.

**Domain methods remain valuable in LLM proving.** WZ guidance solves a planning problem that generic LLM prompting struggles with.

## Subthemes

- Wilf-Zeilberger proof sketches.
- Lean 4 formal proof generation.
- Neuro-symbolic theorem proving.
- Kernel-verified bootstrapping.
- DAPO refinement for proof search.

## Connections to Other Papers

Connects to TG-RAG, Procedural Pretraining, CausalGame, and reasoning-LM training through external procedural scaffolds for long-horizon reasoning. It also links to agent evaluation because proof success is machine-checkable rather than judge-based.

## Notes for Cross-Paper Synthesis

WZ-LLM reinforces a core pattern across reasoning papers: LLMs perform better when domain structure narrows the search space and formal validators turn intermediate steps into reliable training signals.
