# Linguistic Nepotism: Trading-off Quality for Language Preference in Multilingual RAG

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: MDfCV0UHSb
- Authors: Dayeon Ki; Marine Carpuat; Paul McNamee; Daniel Khashabi; Eugene Yang; Dawn Lawrie; Kevin Duh
- Primary area: general_machine_learning->evaluation
- Keywords: Multilingual;Retrieval-Augmented Generation;RAG;Evaluation;Language Preference
- Source URL: https://openreview.net/forum?id=MDfCV0UHSb
- PDF URL: https://openreview.net/pdf?id=MDfCV0UHSb

## Abstract

Multilingual Retrieval-Augmented Generation (mRAG) systems enable language models to answer knowledge-intensive queries with citation-supported responses across languages. Despite their growing use, an open questions is whether the mixture of different document languages impacts generation and citation behavior in *unintended* ways. To investigate this, we introduce a controlled methodology using model internals to measure language preference while holding other factors such as document relevance constant. Across eight languages and six open-weight models, we find that models preferentially cite English sources when queries are in English, with this bias amplified for lower-resource languages and for documents positioned mid-context. More crucially, we find that models sometimes trade-off document relevance for language preference, indicating that citation choices are not always driven by informativeness alone. Our findings shed light on how language models leverage multilingual context and influence citation behavior.

## One-Sentence Claim

Multilingual RAG systems can prefer citations in the query language, especially English, even when that means trading off document relevance.

## Problem

RAG systems increasingly mix documents across languages, but it is unclear whether generation and citation behavior are driven by informativeness alone or biased by language preference.

## Core Contribution

The paper introduces a controlled internal-measurement methodology for language preference while holding document relevance constant, revealing systematic citation bias in multilingual contexts.

## Method

The authors use model internals to measure language preference across multilingual document mixtures, controlling for relevance and studying effects of query language, resource level, and document position.

## Experiments and Evidence

Across eight languages and six open-weight models, the abstract reports preferential citation of English sources for English queries, amplified bias for lower-resource languages and mid-context documents, and cases where language preference overrides relevance.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: internal metric design, languages/models, retrieval setup, citation evaluation, relevance controls, and whether mitigation strategies are tested.

## Deep Themes

- Multilingual systems can encode citation preferences independent of relevance.
- Evaluation must inspect source use, not only final answer quality.
- Low-resource language evidence can be disadvantaged inside mixed-context RAG.

## Subthemes

- Multilingual RAG.
- Citation behavior.
- Language preference.
- English bias.
- Context position effects.
- Low-resource languages.

## Connections to Other Papers

Connects to MemoryBench, ATLAS, and safety/evaluation papers through system-level measurement. It also relates to fairness and data-governance themes around representation of multilingual evidence.

## Notes for Cross-Paper Synthesis

This paper adds a citation-governance theme: in retrieval-augmented systems, the model's choice of evidence source is itself a biased decision requiring measurement.
