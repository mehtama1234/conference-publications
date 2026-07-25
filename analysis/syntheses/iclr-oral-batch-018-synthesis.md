# ICLR Oral Batch 018 Synthesis

## Papers Covered

- Speculative Actions: A Lossless Framework for Faster AI Agents
- Hyperparameter Trajectory Inference with Conditional Lagrangian Optimal Transport
- Beyond Prompt-Induced Lies: Investigating LLM Deception on Benign Prompts
- SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety
- RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format

## Shared Thesis

This batch is about changing system behavior while preserving something important: accepted agent trajectories, neural-network behavior across hyperparameters, truthful communication, safety-helpfulness balance, and reasoning format. Speculative Actions speeds agents without changing accepted actions. HTI approximates unobserved hyperparameter behavior without retraining. The deception paper measures whether outputs diverge from internal beliefs. SafeDPO simplifies safety alignment while preserving helpfulness. RAIN-Merging transfers instruction following while preserving large-reasoning-model thinking structure. The common pattern is adaptation under invariants.

## Deep Themes

### Lossless and Behavior-Preserving Acceleration

Speculative Actions extends speculative execution from tokens to tools. The important constraint is losslessness: precomputed action results are useful only if they do not change the agent's final behavior. This broadens the inference-efficiency theme into agent serving, where API latency and external calls dominate runtime.

### Behavior Geometry Under Control Knobs

HTI models how a network's output distribution moves when hyperparameters change. This is a different approach to adaptation: instead of retraining for each deployment preference, learn the trajectory of behavior induced by the control knob. It connects optimal transport geometry to practical post-deployment flexibility.

### Trustworthiness as Latent-Output Consistency

The deception paper makes an explicit distinction between prompt-induced deception and self-initiated deception under benign prompts. Its key measurement idea is that trustworthiness requires consistency between the model's internal belief and expressed output, not only surface-level compliance.

### Alignment and Merging With Protected Capabilities

SafeDPO and RAIN-Merging both seek lighter adaptation. SafeDPO folds safety constraints into direct preference optimization without reward or cost models. RAIN-Merging uses task-vector geometry to add instruction following while preserving reasoning format. Both are examples of constrained adaptation: improve one behavior without destroying another.

## Cross-Paper Pattern

The shared technical instinct is to identify the invariant before changing the system. Speculative Actions preserves accepted trajectories, HSD-like methods preserve distributions, HTI preserves a coherent behavior path, deception metrics test honesty as belief-output alignment, SafeDPO preserves a safety-constrained optimum, and RAIN-Merging preserves thinking-format mechanisms. This is a mature version of the 2026 adaptation theme: capability upgrades increasingly come with explicit preservation constraints.

## Subthemes to Track

- Speculative execution for agent APIs.
- Optimal-transport hyperparameter adaptation.
- Benign-prompt deception measurement.
- Lightweight safety DPO.
- Null-space model merging for reasoning models.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal guarantees and empirical details should be upgraded after PDFs are available.
