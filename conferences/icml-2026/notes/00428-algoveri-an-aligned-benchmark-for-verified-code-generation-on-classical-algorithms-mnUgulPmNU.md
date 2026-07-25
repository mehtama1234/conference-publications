# AlgoVeri: An Aligned Benchmark for Verified Code Generation on Classical Algorithms

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: mnUgulPmNU
- Authors: Haoyu Zhao; Ziran Yang; Jiawei Li; Mike He; Zenan Li; Chi Jin; Venugopal Veeravalli; Aarti Gupta; Sanjeev Arora
- Primary area: applications
- Keywords: Program Verification;Large Language Model
- Source URL: https://openreview.net/forum?id=mnUgulPmNU
- PDF URL: https://openreview.net/pdf?id=mnUgulPmNU

## Abstract

Vericoding refers to the generation of formally verified code from rigorous specifications. Recent AI models show promise in vericoding, but a unified methodology for cross-paradigm evaluation is lacking. Existing benchmarks test only an individual language/tool (e.g., Dafny, Verus, and Lean) and each covers very different tasks, so the performance numbers are not directly comparable. We address this gap with AlgoVeri, a benchmark that evaluates vericoding of $77$ classical algorithms in each of Dafny, Verus, and Lean. By enforcing identical functional contracts, AlgoVeri reveals critical capability gaps in current models. While frontier models achieve tractable success in Dafny ($40.3$\% for Gemini-3 Flash), where high-level abstractions and SMT automation simplify the workflow, performance collapses under the systems-level memory constraints of Verus ($24.7$\%) and the explicit proof construction required by Lean ($7.8$\%). Beyond aggregate metrics, we uncover a sharp divergence in test-time compute dynamics: Gemini-3 effectively utilizes iterative repair to boost performance (e.g., tripling pass rates in Dafny), whereas GPT-OSS saturates early. Finally, our error analysis shows that language design affects the refinement trajectory: while Dafny allows models to focus on logical correctness, Verus and Lean trap models in persistent syntactic and semantic barriers.

## One-Sentence Claim

AlgoVeri evaluates verified code generation across Dafny, Verus, and Lean using identical classical-algorithm contracts, revealing that model success depends heavily on the verification paradigm rather than only on algorithmic understanding.

## Problem

Vericoding benchmarks are fragmented: different languages and proof tools test different task sets, so model scores are not directly comparable. A model may appear strong in one benchmark because the language provides helpful automation or because the tasks are easier, not because it has a general ability to produce verified programs.

The missing piece is aligned cross-paradigm evaluation. Without identical functional contracts across tools, it is hard to separate algorithmic reasoning from proof construction, systems-level constraints, syntax management, and SMT automation.

## Core Contribution

AlgoVeri contributes a benchmark of 77 classical algorithms implemented across Dafny, Verus, and Lean with matched functional contracts. This design isolates how much model performance changes when the specification target stays stable but the verification environment changes.

The key finding is a steep capability gradient: frontier models achieve meaningful success in Dafny, weaker success in Verus, and very low success in Lean. The benchmark therefore exposes vericoding as a tool-interaction and proof-paradigm problem, not just a code-generation problem.

## Method

The benchmark holds algorithmic tasks and functional contracts fixed across three verification ecosystems. Dafny provides higher-level abstractions and SMT automation, Verus adds systems-level memory and ownership constraints, and Lean requires more explicit proof construction.

The paper also studies test-time compute dynamics and error trajectories. Iterative repair is measured as a capability, making the benchmark sensitive to whether models can use feedback from failed verification attempts rather than only produce a correct first draft.

## Experiments and Evidence

The headline results show Gemini-3 Flash reaching 40.3 percent in Dafny, 24.7 percent in Verus, and 7.8 percent in Lean. Gemini-3 also benefits substantially from iterative repair, including tripled pass rates in Dafny, while GPT-OSS saturates early.

The error analysis finds that language design shapes failure modes: Dafny lets models focus more on logical correctness, while Verus and Lean trap models in persistent syntactic and semantic barriers. This is evidence that benchmark design must measure the interface between model reasoning and formal-tool ergonomics.

## Limits and Failure Modes

AlgoVeri's conclusions are bounded by its 77 classical algorithms and the selected versions of Dafny, Verus, Lean, and model prompting/repair setups. Performance may change quickly as tool-specific training data, proof automation, and model scaffolding improve.

There is also a risk that benchmark scores conflate model ability with harness engineering. Iterative repair can be either a model capability or a surrounding agent capability, so careful reporting is needed when comparing plain LLMs, tool-using agents, and specialized vericoding systems.

## Deep Themes

- Benchmark alignment across tool paradigms: identical contracts reveal what changes when only the proof environment changes.
- Verification as an interaction problem: success depends on feedback, repair, and language ergonomics.
- Formal methods as a stress test for LLM reasoning: Lean exposes proof-construction gaps that ordinary coding benchmarks can hide.
- Test-time compute is unevenly usable: models differ not only in first-pass quality but in how well they exploit repair loops.

## Subthemes

- Dafny-style automation can mask gaps that become visible in explicit proof systems.
- Verus introduces a different bottleneck: systems constraints and memory reasoning.
- Cross-language benchmark design is a way to separate semantic understanding from syntax and tooling familiarity.
- Repair saturation is a diagnostic for whether extra inference budget actually produces new reasoning.

## Connections to Other Papers

AlgoVeri connects directly to Vision2Web and MAP as benchmarks that evaluate agents in realistic workflows rather than static outputs. It also relates to PLAINTAIN and LongCoT-like reasoning evaluation through the concern that models fail over extended multi-step processes even when individual steps are tractable.

It complements Verified SHAP in this same batch: both use formal verification as a route to stronger guarantees, but AlgoVeri measures whether models can produce verified artifacts, while Verified SHAP uses verification algorithms to compute explanations.

## Notes for Cross-Paper Synthesis

AlgoVeri is strong evidence for a larger 2026 theme: evaluation is moving from "did the model emit a plausible artifact" to "did it survive a tool-mediated correctness process." The deeper pattern is that benchmark realism increasingly means exposing the model to the constraints of the production or formal environment.
