# Premise Selection for a Lean Hammer

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: m04JJNeRK6
- Authors: Thomas Zhu; Joshua Clune; Jeremy Avigad; Albert Q. Jiang; Sean Welleck
- Primary area: neurosymbolic & hybrid AI systems (physics-informed, logic & formal reasoning, etc.)
- Keywords: premise selection;interactive theorem proving;automated reasoning;contrastive learning
- Source URL: https://openreview.net/forum?id=m04JJNeRK6
- PDF URL: https://openreview.net/pdf?id=m04JJNeRK6

## Abstract

Neural methods are transforming automated reasoning for proof assistants, yet integrating these advances into practical verification workflows remains challenging. A $\textit{hammer}$ is a tool that integrates premise selection, translation to external automatic theorem provers, and proof reconstruction into one overarching tool to automate tedious reasoning steps. We present LeanPremise, a novel neural premise selection system, and we combine it with existing translation and proof reconstruction components to create LeanHammer, the first end-to-end domain general hammer for the Lean proof assistant. Unlike existing Lean premise selectors, LeanPremise is specifically trained for use with a hammer in dependent type theory. It also dynamically adapts to user-specific contexts, enabling it to effectively recommend premises from libraries outside LeanPremise's training data as well as lemmas defined by the user locally. With comprehensive evaluations, we show that LeanPremise enables LeanHammer to solve 21\% more goals than existing premise selectors and generalizes well to diverse domains. Our work helps bridge the gap between neural retrieval and symbolic reasoning, making formal verification more accessible to researchers and practitioners.

## One-Sentence Claim

LeanPremise improves premise retrieval for an end-to-end Lean hammer, enabling LeanHammer to solve more proof goals and adapt to user-local contexts beyond its training library.

## Problem

Neural automated reasoning has advanced, but practical proof-assistant workflows need integrated tools that select relevant premises, translate goals to external ATPs, and reconstruct proofs. Lean lacked a domain-general end-to-end hammer with neural premise selection adapted to dependent type theory and user-specific contexts.

## Core Contribution

The paper presents LeanPremise, a neural premise selector trained for hammer use in Lean, and combines it with translation and proof reconstruction to create LeanHammer. A key contribution is dynamic adaptation to libraries and locally defined lemmas outside the selector's training data.

## Method

LeanPremise retrieves relevant premises for Lean goals, likely using contrastive learning over theorem/proof contexts, then feeds selected premises into external automated theorem provers through translation and proof reconstruction components. The system adapts retrieval to user-specific context so new local lemmas can become candidates.

## Experiments and Evidence

Comprehensive evaluations reportedly show that LeanPremise enables LeanHammer to solve 21 percent more goals than existing premise selectors and generalizes across diverse domains.

## Limits and Failure Modes

Hammer performance depends on translation fidelity, ATP compatibility, proof reconstruction robustness, and premise-selector coverage. Dynamic local adaptation could retrieve irrelevant or circular premises if context handling is weak. Full-text review should check Lean library versions, domain splits, retrieval metrics, ATP portfolio, reconstruction success, and comparisons to non-neural selectors.

## Deep Themes

- Neural-symbolic integration for theorem proving.
- Premise retrieval as workflow bottleneck.
- User-context adaptation in formal verification.
- End-to-end automation for proof assistants.

## Subthemes

- Lean hammer construction.
- Dependent type theory premise selection.
- Contrastive theorem retrieval.
- Translation to external theorem provers.
- Proof reconstruction.

## Connections to Other Papers

Connects to Lean-focused theorem-proving and premise-selection work, to hybrid neural-symbolic papers such as HATSolver, and to retrieval papers where domain-specific retrieval quality controls downstream reasoning success.

## Notes for Cross-Paper Synthesis

LeanHammer reinforces the theme that retrieval and integration layers matter as much as the neural model. In formal reasoning, the useful unit is an end-to-end workflow that can retrieve, translate, solve, and reconstruct inside the proof assistant.
