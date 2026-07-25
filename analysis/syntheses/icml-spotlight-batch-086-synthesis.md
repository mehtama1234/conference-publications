# ICML 2026 Spotlight Batch 086 Synthesis

Papers covered: 00426-00430.

## Batch Thesis

This batch is about replacing black-box empirical success with controlled procedures that expose why a system should be trusted. ADEPT makes emotion recognition auditable through tool-mediated evidence; Excited Pfaffians encode quantum-state structure so multi-state simulation scales; AlgoVeri aligns verification benchmarks across proof ecosystems; neural scaling-law work builds controlled sequence worlds to isolate mechanisms; and no-swap-regret auction theory gives finite-time revenue guarantees for adaptive bidders.

The common move is procedural discipline. Rather than relying on a model's raw output, each paper introduces a structure around the output: evidence gates, shared physical state representations, formal contracts, synthetic scaling laboratories, or regret-based equilibrium bounds.

## Cross-Paper Themes

### 1. Trust Comes From Process, Not Just Prediction

ADEPT and AlgoVeri make this theme most explicit. ADEPT asks whether an emotion prediction came from grounded semantic and acoustic evidence. AlgoVeri asks whether generated code survives a verifier under matched functional contracts. Both move evaluation from answer plausibility to process validity.

Verified SHAP from the next line of work will likely fit this theme too: exact explanations become credible only when their computation is bounded or verified. Across the corpus, trust increasingly means that the path to the answer is inspectable.

### 2. Structure Is a Scaling Tool

Excited Pfaffians and the scaling-law paper both show that scaling is not only about adding resources. Excited Pfaffians scale multi-state quantum modeling by sharing a physically meaningful architecture across states. The scaling-law paper studies how exponents shift as the data-generating process changes, implying that task structure and learner dynamics jointly define scaling behavior.

This echoes STAR-KV, NorMuon, OPUS, MERLIN, and DeCoDe: efficiency gains often come from matching the computational structure to the underlying mathematical object.

### 3. Benchmarks Are Becoming Mechanistic Instruments

AlgoVeri is not just a leaderboard; it is designed to distinguish tool-paradigm effects by holding contracts fixed across Dafny, Verus, and Lean. The scaling-law paper similarly builds controlled random-graph and simplified-language tasks to isolate the origin of scaling exponents.

The pattern is a shift from benchmarks as scoreboards to benchmarks as instruments for causal diagnosis. Vision2Web and MAP do this for agents; LongCoT-like work does it for long-horizon reasoning; AlgoVeri does it for formal code generation.

### 4. Learning Dynamics Need Finite-Time Guarantees

The auction paper and the scaling-law paper both treat dynamics as the central object. Auction revenue is guaranteed under no-swap-regret dynamics with explicit dependence on discretization and approximation error. Scaling laws are studied as the dynamics of transformers learning controlled sequence processes.

This connects to the broader ICML theory stream: convergence rates, finite-sample guarantees, stability, and approximation errors are being used to discipline claims that would otherwise remain asymptotic or empirical.

## Deep Subthemes

### Evidence-Gated Agency

ADEPT suggests a reusable pattern for ambiguous multimodal decisions: make the model maintain hypotheses, call evidence tools, and gate final judgments by evidence quality. This is a richer form of agent alignment than merely rewarding correct answers because it optimizes the information-gathering behavior that produced the answer.

### Structured Amortization in Scientific ML

Excited Pfaffians show a domain-specific version of foundation-style reuse. A single wave-function model represents related states and molecular surfaces, amortizing computation across physical structure. The lesson is that scientific ML scalability often depends on choosing the right shared object.

### Aligned Formal Evaluation

AlgoVeri's aligned contracts expose how much verification success depends on the target proof ecosystem. This matters for comparing models because a Dafny score, a Verus score, and a Lean score are not interchangeable signals of the same capability.

### Controlled Worlds for Frontier-Scale Questions

The scaling-law paper shows how to investigate frontier-model phenomena using small, synthetic, tunable systems. The deeper methodological point is that simplified worlds are not toy distractions when they preserve the mechanism under study.

### Equilibrium Quality Under Adaptive Behavior

The auction paper reframes revenue guarantees around what adaptive bidders learn over time. The convergence rate is not secondary; it is the bridge from equilibrium theory to repeated deployed systems.

## Common Pattern

Across these papers, the 2026 direction is to make systems legible under stress. Ambiguous emotion labels, excited quantum states, formal proof languages, neural scaling curves, and auction learning dynamics all resist naive prediction. The response is to impose a structure that can be inspected: evidence traces, shared physical representations, matched contracts, controlled generators, or explicit regret bounds.

The shared design philosophy is: if the output is high stakes, complex, or hard to interpret, wrap the model in a process whose intermediate objects carry meaning.
