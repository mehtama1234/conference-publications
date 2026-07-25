# ICML 2026 Spotlight Batch 056 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 276-280:

- World-Model Inspired Emotion-aware Token Refinement for Training-Free Multimodal Emotion Recognition
- Recurrent Structural Policy Gradient for Partially Observable Mean Field Games
- FlashSinkhorn: IO-Aware Entropic Optimal Transport on GPU
- Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
- TG-RAG: A Retrieval-Augmented Framework for Reasoning Guidance in Specialized Domains

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 275.

## Emerging Pattern 1: Frozen or Pretrained Models Still Need Runtime Control

WETR improves frozen MLLM emotion recognition by refining token contribution. TG-RAG steers reasoning by interrupting generation and injecting procedure-specific guidance. Continual VLA learning shows pretrained models can preserve skills with simple replay.

The shared implication is that pretrained models are reusable substrates, but reliable use still depends on token, retrieval, replay, or procedure-level control.

## Emerging Pattern 2: Process State Is Becoming Explicit

TG-RAG externalizes SOP state as an Expert Procedure Graph. RSPG makes history explicit for partially observable mean-field games. WETR treats emotion as a latent state inferred from noisy multimodal observations.

This continues the process-representation theme from TerminalTraj, Scientific Annotation BC, and DLMR: successful systems model where they are in the task, not just what input they see.

## Emerging Pattern 3: Hardware-Aware Reformulation Expands Feasible Algorithms

FlashSinkhorn turns Sinkhorn updates into an attention-like LogSumExp reduction so fused Triton kernels can stream tiles through SRAM. The math is familiar, but the computational grammar changes the feasible scale.

This links to WBMM and WeDLM: 2026 efficiency work often reframes old operations into kernels that match modern accelerator memory hierarchies.

## Emerging Pattern 4: Large Pretraining Changes Adaptation Failure Modes

The continual VLA paper finds that large pretrained robot policies resist forgetting and can recover degraded skills quickly. This matches DiSC and reasoning-LM training papers: pretraining changes what post-training, replay, and fine-tuning can accomplish.

The practical lesson is to reassess old continual-learning conclusions under foundation-model scaling.

## Emerging Pattern 5: Structural Variance Reduction Beats Pure Sampling in Large Systems

RSPG advances mean-field-game learning by combining common-noise rollouts with exact structural returns and recurrent histories. It preserves known dynamics while sampling only what must be sampled.

This echoes many theory/optimization papers where tractability comes from keeping the right analytic structure rather than defaulting to fully model-free learning.

## Cross-Batch Links

- WETR connects to DLMR, DOUBT, Table-GLS, and Latent Action Supervision through explicit multimodal evidence routing.
- RSPG connects to RQE Actor-Critic, PAVE, R2VPO, and data-market pricing through structured game/RL optimization.
- FlashSinkhorn connects to WBMM, WeDLM, SoftJAX/SoftTorch, and geometry-heavy ML pipelines through hardware-friendly primitives.
- Continual VLA Forgetting connects to Latent Action Supervision, EcoVLA, DiSC, and Scientific Annotation BC through embodied continual adaptation.
- TG-RAG connects to tau2-bench, TerminalTraj, DLMR, and WETR through runtime process control for reasoning systems.

## Deep Theme Update

Batch 056 emphasizes controlled reuse of existing structure: frozen tokens are reweighted, mean-field dynamics are structurally integrated, Sinkhorn is rewritten for GPU IO, pretrained VLA skills are protected through replay, and SOP graphs steer reasoning before it drifts.
