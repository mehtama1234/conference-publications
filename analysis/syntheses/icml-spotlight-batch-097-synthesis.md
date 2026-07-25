# ICML 2026 Spotlight Batch 097 Synthesis

Papers covered: 00481-00485.

## Batch Thesis

This batch is about robust generalization under structural mismatch. HSR makes successor representations less policy-dependent through hierarchy; PIPE reveals that trajectory-SFT agents may learn interface forms instead of semantics; FFCC speeds edge inference by compiling activation approximations to hardware-friendly instructions; HALO stabilizes heterogeneous human-robot policy learning through Lyapunov contraction; and Rational Transductors add automata-derived recurrence to close Transformer sequential-logic gaps.

The common thread is that failures arise when the learned object is not aligned with the structure that must generalize: policy changes, interface rewrites, edge hardware, human-robot heterogeneity, or formal state tracking.

## Cross-Paper Themes

### 1. Generalization Requires Invariant Structure

HSR seeks predictive features robust to policy changes. PIPE tests whether agents understand tool semantics invariant to interface rewrites. Rational Transductors target length-general sequential logic that standard Transformers fail to preserve.

Across these papers, generalization is not measured by more examples from the same distribution but by invariance under a meaningful transformation.

### 2. Deployment Constraints Expose Hidden Model Assumptions

FFCC exists because activation functions that are cheap in desktop training can be expensive on edge devices. HALO exists because independent gradients that look reasonable in homogeneous agents can oscillate in human-robot collaboration.

These papers show that deployment setting is part of the algorithmic problem. Hardware, human partners, and interfaces cannot be abstracted away without losing the real bottleneck.

### 3. Hierarchy, Recurrence, and Memory Are Reappearing

HSR uses temporal abstraction; CMRU uses persistent recurrent memory; Rational Transductors use automata-derived recurrence. These methods push against the idea that generic attention alone is sufficient for every sequential problem.

The pattern is not a simple return to RNNs. It is targeted recurrence or hierarchy inserted where formal state, transfer, or low-power memory demands it.

### 4. Evaluation Needs Counterfactual Perturbations

PIPE's interface rewrites are a counterfactual test of agent capability. HALO's corner cases test collaboration robustness. HSR's reward/task changes test representation transfer.

This connects to many benchmark papers in the corpus: robustness is revealed by perturbing the protocol while preserving the intended semantics.

## Deep Subthemes

### Policy-Robust Predictive Maps

HSR addresses SR's policy dependence by building temporal abstraction into predictive features. Sparse NMF components reveal topological structure that supports transfer and exploration.

### Interface Reliance in Agent SFT

Trajectory SFT can reward memorized interface patterns. PIPE diagnoses this by minimally rewriting environments while keeping task semantics fixed.

### Compiler-Generated Edge Activations

FFCC treats activation functions as compilation targets. Hardware-friendly approximations can produce post-training speedups without replacing the model.

### Lyapunov-Stable Human-Robot Learning

HALO stabilizes decentralized learning by contracting the rationality gap. The safety object is not only the trajectory; it is the learning update itself.

### Automata-Augmented Transformers

Rational Transductors use WFA recurrence to add formal state-tracking capacity while retaining parallel training. This addresses regular-language and NC1-style gaps.

## Common Pattern

The batch's shared lesson is that robustness lives in the right invariance. A representation should survive policy changes, an agent should survive interface rewrites, an activation should survive hardware constraints, a robot learner should survive heterogeneous partners, and a sequence architecture should survive length extrapolation.
