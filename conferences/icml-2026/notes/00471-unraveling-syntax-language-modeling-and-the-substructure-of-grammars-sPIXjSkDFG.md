# Unraveling Syntax: Language Modeling and the Substructure of Grammars

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: sPIXjSkDFG
- Authors: Laura Ying Schulz; Daniel Mitropolsky; Tomaso Poggio
- Primary area: theory
- Keywords: language modeling;formal languages;context-free grammar;context-free language;subgrammar;compositionality;synthetic languages;learning theory
- Source URL: https://openreview.net/forum?id=sPIXjSkDFG
- PDF URL: https://openreview.net/pdf?id=sPIXjSkDFG

## Abstract

While language models achieve impressive results, their *learning dynamics* are far from understood. Many domains of interest – such as natural language syntax, coding languages, arithmetic – are captured by context-free grammars (CFGs). In this work, we extend prior work on neural language modeling of CFGs in a novel direction: how language modeling behaves with respect to CFG *substructure*, namely sub*grammars*. We define subgrammars, and prove a set of fundamental theorems connecting language modeling and subgrammars. We show that language modeling loss recurses linearly over its top-level subgrammars; applied recursively, the loss decomposes into losses for "irreducible" subgrammars. Under additional assumptions, and empirically, parametrized models learn subgrammars in parallel, unlike children who first master simple substructures. We find that subgrammar pretraining can improve final performance, but only for tiny models relative to the grammar, while alignment analyses show that pretraining consistently leads to internal representations that better reflect the grammar’s substructure.

## One-Sentence Claim

Language-model loss over context-free grammars decomposes linearly over subgrammars, revealing parallel substructure learning and showing that subgrammar pretraining mostly improves internal grammatical alignment rather than final performance except in tiny models.

## Problem

Language models perform well on natural language, code, and arithmetic, but their learning dynamics over compositional symbolic structure remain poorly understood. Context-free grammars provide a controlled setting for studying syntax-like hierarchical structure.

Prior work on CFG language modeling often treats the grammar as one object. This paper asks how learning behaves with respect to subgrammar structure: whether losses, representations, and pretraining effects can be decomposed over smaller grammatical components.

## Core Contribution

The paper defines subgrammars and proves theorems connecting language-modeling loss to grammar substructure. Top-level subgrammar losses combine linearly, and recursive decomposition yields irreducible subgrammar losses.

It also studies how parameterized models learn these subgrammars. Under assumptions and empirically, models learn subgrammars in parallel rather than following the developmental sequence seen in children. Subgrammar pretraining improves final performance mainly for tiny models relative to the grammar, but consistently improves internal representation alignment with grammar structure.

## Method

The theoretical component decomposes CFGs into subgrammars and analyzes language-modeling loss over this decomposition. Applying the decomposition recursively identifies irreducible subgrammar components.

The empirical component trains parameterized models on synthetic grammar languages, examines parallel versus staged subgrammar learning, tests subgrammar pretraining, and measures representation alignment with grammatical substructure.

## Experiments and Evidence

The abstract reports fundamental theorems for loss decomposition and empirical support for parallel subgrammar learning. It also reports that subgrammar pretraining improves final performance only for tiny models but reliably induces representations better aligned with grammar substructure.

Full-paper reading should verify grammar families, model sizes, alignment metrics, assumptions for parallel learning, and whether findings extend beyond synthetic CFGs.

## Limits and Failure Modes

CFGs capture important syntax-like structure but do not fully represent natural language semantics, pragmatics, ambiguity, or discourse. Results on synthetic languages should be translated carefully to real LLM training.

Subgrammar pretraining's limited performance gains suggest representation alignment does not always translate into downstream loss improvements, especially for sufficiently large models.

## Deep Themes

- Grammar as decomposable structure: language-model loss can be analyzed through subcomponents.
- Parallel substructure learning: neural models may learn grammar parts differently from human developmental order.
- Representation alignment without performance gain: internal structure can improve even when final accuracy barely changes.
- Synthetic languages as mechanistic probes: CFGs reveal learning dynamics hidden in natural corpora.

## Subthemes

- Irreducible subgrammars provide atomic units of syntax learning.
- Tiny models benefit most from curriculum-like subgrammar pretraining.
- Loss decomposition gives a formal handle on compositionality.
- Alignment analysis can expose latent structure beyond aggregate loss.

## Connections to Other Papers

This paper connects to scaling-law origin work and reasoning-loop analysis through synthetic controlled tasks for understanding model dynamics. It also relates to concept binding and latent distribution matching through representation structure and compositional learning.

It fits the broader "theory unifies engineering practice" theme by deriving what empirical grammar learning should look like under decomposition.

## Notes for Cross-Paper Synthesis

The synthesis point is that compositionality can be studied by decomposing the data-generating structure. Several papers use synthetic worlds not as benchmarks but as microscopes for learning dynamics.
