# ICML 2026 Spotlight Batch 078 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 386-390:

- LASER: Learning Active Sensing for Continuum Field Reconstruction
- Demystifying Entropy Control in LLM RL Training: Theoretical Analysis and Dynamic Scheduling
- Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework
- Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robust GUI Agents
- A Random Matrix Perspective on the Consistency of Diffusion Models

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 385.

## Emerging Pattern 1: Closed Loops Need Diagnostics, Not Static Rules

LASER adapts sensor motion through a latent world model. Entropy scheduling adapts exploration pressure according to Entropy Discrepancy. GUI-RobustEval/RoTS targets what agents do after their own mistakes.

Across these papers, the system is a loop. Static layouts, fixed entropy coefficients, and ideal-only demonstrations are replaced by state-dependent policies.

## Emerging Pattern 2: Feedback Pipelines Can Be Both Powerful and Vulnerable

Critique-GRPO and entropy scheduling show richer feedback can improve LLM RL. Rapid Poison shows adaptive safety data generation can be poisoned through prompt injection and omission.

The common lesson is that feedback ingestion is a critical interface: it can improve learning, but if not governed, it becomes an adversarial control surface.

## Emerging Pattern 3: Robust Agents Need Recovery, Not Just Success

RoTS makes policy-induced error recovery a benchmark and data-generation target. This connects to MADQA and VenusBench-Mobile, where process failures such as loops, perception errors, and memory failures dominate.

The agent theme is maturing from "can complete task" to "can recover after it perturbs the world incorrectly."

## Emerging Pattern 4: Scientific Models Are Becoming Active Experimenters

LASER uses active sensing to decide what to observe next in continuum fields. This complements LoRFS, ReViT, NeuronCtrl, and other scientific-ML papers that model or control physical systems.

The new ingredient is experimental agency: the model not only solves the field but guides measurement.

## Emerging Pattern 5: Generative Model Reproducibility Has Spectral Structure

The RMT diffusion paper explains cross-split consistency through shared Gaussian statistics, finite-data noise renormalization, anisotropy, and dataset-size scaling. This links generative reproducibility to data spectrum and sampling trajectories.

It complements KPE/KTS and Weak Diffusion Priors by showing that diffusion behavior is often governed by path and spectral structure, not only high-level semantics.

## Cross-Batch Links

- LASER connects to NeuronCtrl, LoRFS, ReViT, Dirac-Frenkel-Onsager dynamics, and delayed-observation RL.
- Entropy scheduling connects to Critique-GRPO, RePO, Hista/Numca, T2PO, and PRISM.
- Rapid Poison connects to Monitoring Monitorability, Token Overcharging, Weak-Strong Verification, and safety-data governance.
- RoTS connects to VenusBench-Mobile, MADQA, daVinci-Dev, Agent0-VL, and process-oriented agent benchmarks.
- RMT diffusion consistency connects to KPE/KTS, Weak Diffusion Priors, MOG, Tilt Matching, and memorization-capacity work.

## Deep Theme Update

Batch 078 is about adaptive loops under uncertainty: sensing loops, RL-training loops, safety-update loops, GUI-agent recovery loops, and diffusion sampling/training loops all need explicit models of feedback, failure, and variance.
