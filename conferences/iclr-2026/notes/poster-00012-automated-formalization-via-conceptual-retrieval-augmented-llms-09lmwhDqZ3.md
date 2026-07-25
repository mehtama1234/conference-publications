# Automated Formalization via Conceptual Retrieval-Augmented LLMs

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 09lmwhDqZ3
- Authors: Wangyue Lu; Lun Du; Sirui Li; Ke Weng; Haozhe Sun; Hengyu Liu; Minghe Yu; Tiancheng Zhang; Ge Yu
- Primary area: foundation or frontier models, including LLMs
- Keywords: Autoformalization;Retrieval-augmented Generation
- Source URL: https://openreview.net/forum?id=09lmwhDqZ3
- PDF URL: https://openreview.net/pdf?id=09lmwhDqZ3

## Abstract

Interactive theorem provers (ITPs) require manual formalization, which is labor-intensive and demands expert knowledge. While automated formalization offers a potential solution, it faces two major challenges: model hallucination (e.g., undefined predicates, symbol misuse, and version incompatibility) and the semantic gap caused by ambiguous or missing premises in natural language descriptions. To address these issues, we propose CRAMF, a Concept-driven Retrieval-Augmented Mathematical Formalization framework. CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation. However, applying retrieval-augmented generation (RAG) in this setting is non-trivial due to the lack of structured knowledge bases, the polymorphic nature of mathematical concepts, and the high precision required in formal retrieval. We introduce a framework for automatically constructing a concept-definition knowledge base from Mathlib4, the standard mathematical library for the Lean 4 theorem prover, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts. To address conceptual polymorphism, we propose contextual query augmentation with domain- and application-level signals. In addition, we design a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval. Experiments on miniF2F, ProofNet, and our newly proposed AdvancedMath benchmark show that CRAMF can be seamlessly integrated into LLM-based autoformalizers, yielding consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement.

## One-Sentence Claim

CRAMF improves LLM autoformalization by retrieving formal definitions for core mathematical concepts from a Mathlib4-derived knowledge base before generating Lean code.

## Problem

Automated formalization into theorem provers is limited by hallucinated symbols, undefined predicates, version mismatches, and ambiguity or missing premises in natural language. RAG is appealing but hard because formal mathematics has polymorphic concepts and requires highly precise retrieval.

## Core Contribution

The paper contributes Concept-driven Retrieval-Augmented Mathematical Formalization, including an automatically constructed Mathlib4 concept-definition knowledge base with over 26,000 formal definitions and more than 1,000 core concepts. It adds contextual query augmentation and dual-channel hybrid retrieval with reranking.

## Method

CRAMF identifies core mathematical concepts in a problem, augments retrieval queries with domain and application context to handle conceptual polymorphism, retrieves relevant Lean/Mathlib4 definitions through hybrid channels, reranks them, and provides the definitions as grounding context for an LLM autoformalizer.

## Experiments and Evidence

The abstract reports experiments on miniF2F, ProofNet, and AdvancedMath. CRAMF integrates with LLM-based autoformalizers and improves translation accuracy consistently, with up to 62.1% and an average 29.9% relative improvement.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect concept extraction quality, retrieval precision/recall, dependence on Mathlib4 versioning, benchmark leakage risks, and whether retrieved definitions are sufficient when natural-language premises are incomplete or wrong.

## Deep Themes

- Retrieval-grounded autoformalization.
- Concept-definition knowledge bases.
- Formal-code hallucination reduction.
- Mathematical RAG under precision constraints.

## Subthemes

- CRAMF.
- Lean 4 and Mathlib4.
- Contextual query augmentation.
- Hybrid retrieval and reranking.
- miniF2F, ProofNet, AdvancedMath.

## Connections to Other Papers

Connects to VERINA through formal verification and theorem proving, to THOR through tool-integrated mathematical reasoning, and to broader retrieval themes such as MetaEmbed where representation/retrieval precision gates downstream correctness.

## Notes for Cross-Paper Synthesis

CRAMF shows that RAG for formal domains is less about retrieving more text and more about retrieving exact conceptual machinery. In formal reasoning, grounding failures become compiler or theorem-prover failures.
