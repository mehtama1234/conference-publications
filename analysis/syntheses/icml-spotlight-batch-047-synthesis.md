# ICML 2026 Spotlight Batch 047 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 231-235:

- Score-Repellent Monte Carlo: Toward Efficient Non-Markovian Sampler with Constant Memory in General State Spaces
- Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
- On the Existence of Consistent Adversarial Attacks in High-Dimensional Linear Classification
- Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments
- Multimodal Latent Language Modeling with Next-Token Diffusion

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 230.

## Emerging Pattern 1: Memory-Efficient History Can Improve Sampling

SRMC uses a running average of score evaluations as a compact trajectory-history summary, then converts it into a score-tilted surrogate target. This gives non-Markovian repulsion without empirical measures or unbounded memory.

This connects to high-accuracy sampling and LiDAR. Sampling papers in the corpus increasingly use trajectory- or score-level structure to reduce redundancy, guide exploration, and improve variance.

## Emerging Pattern 2: Circuits Have Training-Data Origins

Mechanistic Data Attribution links interpretable heads to influential training examples through influence functions. Targeted data removal or augmentation can modulate circuit emergence, and induction-head interventions affect in-context learning.

This is a major bridge between interpretability and data curation. It turns circuits from static artifacts into developmental outcomes shaped by specific data patterns such as LaTeX or XML.

## Emerging Pattern 3: Robustness Metrics Need Ground-Truth Semantics

The consistent-adversarial-attacks paper separates label-preserving adversarial vulnerability from ordinary error due to finite data or limited expressivity. Its high-dimensional analysis suggests overparameterization can increase this more semantically precise vulnerability.

This connects to tail-risk estimation and other evaluation papers. Measuring robustness requires knowing whether the perturbation should preserve the true label, not just whether the model's output changed.

## Emerging Pattern 4: Agent Data Pipelines Need Executable Verification

TerminalTraj creates Dockerized environments, aligned tasks, and executable validation code to generate over 50K verified terminal trajectories. This complements MEnvAgent's environment-construction focus.

The agent-data theme is clear: long-horizon behavior needs training trajectories grounded in environments that can actually be run and checked.

## Emerging Pattern 5: Multimodal Generation Is Moving Toward Latent Token Interfaces

LatentLM encodes continuous modalities as VAE latents and autoregressively generates them with next-token diffusion. This creates a unified interface for text, code, image, audio, and video while preserving continuous uncertainty.

This links to VideoFlexTok, PWC-Diff, and Chamaileon. The representation pattern is that continuous domains become more scalable when transformed into latent sequences, but those tokens often need diffusion-style generation rather than purely categorical prediction.

## Cross-Batch Links

- SRMC, LiDAR, and high-accuracy samplers all use modified sampling dynamics to improve efficiency without changing the target objective.
- MDA, neuron-basis circuits, FAC Synthesis, and SVD interpretability all make internal mechanisms actionable, but MDA uniquely traces them back to data.
- Consistent adversarial attacks, tail-risk estimation, and Biased Generalization all refine risk metrics to avoid misleading aggregate performance.
- TerminalTraj, MEnvAgent, tau2-bench, and CE-Graph all depend on executable/verifiable environments for agent training or evaluation.
- LatentLM, VideoFlexTok, WLA/ERA5-Latent, and XR-1 all use latent interfaces to unify heterogeneous high-dimensional signals.

## Deep Theme Update

Batch 047 is about making hidden dependencies explicit: sampler history, training examples that create circuits, semantic labels behind adversarial perturbations, executable environments behind agent trajectories, and continuous latents behind multimodal tokens. Each paper exposes a layer that standard model-output evaluation would miss.
