# ICLR 2026 Oral Batch 009 Synthesis

## Papers

- FIRE: Frobenius-Isometry Reinitialization for Balancing the Stability-Plasticity Tradeoff
- Verifying Chain-of-Thought Reasoning via Its Computational Graph
- On the Generalization Capacities of MLLMs for Spatial Intelligence
- Generative Universal Verifier as Multimodal Meta-Reasoner
- Reasoning as Representation: Rethinking Visual Reinforcement Learning in Image Quality Assessment

## Source Depth

All five notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this ICLR oral range when access and rate limits clear.

## Shared Thesis

This batch is about controlling generalization through intermediate mechanisms: isometric reinitialization restores plasticity; computational graphs verify CoT; camera intrinsics disentangle spatial geometry; universal verifiers guide visual generation; and IQA reasoning is distilled into compact text-aligned representations.

The shared move is to expose a hidden mediator between raw training and final behavior. Stability, reasoning correctness, spatial generalization, visual quality, and IQA robustness all depend on a process variable that can be measured or optimized.

## Subthemes

### Geometry-controlled continual learning

FIRE formalizes the stability-plasticity tradeoff as proximity to past weights under an isometry constraint. Plasticity becomes a geometric property that can be restored.

### Computational-graph reasoning verification

CRV treats attribution graphs as execution traces of latent reasoning circuits. This shifts CoT verification from output scoring to structural analysis of computation, and even supports targeted repairs.

### Camera-aware spatial intelligence

The spatial MLLM paper shows that RGB-only models entangle object geometry with camera viewpoint. Camera intrinsics and augmentation are prerequisites for cross-camera generalization.

### Verifier-guided multimodal test-time scaling

OmniVerifier turns visual verification into a generative meta-reasoning capability. Sequential verifier-guided refinement becomes a stronger alternative to parallel Best-of-N sampling.

### Reasoning distilled into representation

RALI shows that reasoning-based IQA gains can be attributed to a compact cross-domain text representation learned through RL. Once learned, that representation can replace expensive reasoning inference.

## Cross-Batch Connections

FIRE connects to CompSLOT, LoRA-Pre, local redundancy, and optimizer geometry papers through controlled plasticity and adaptation.

CRV connects to Information Flow, DAVE, transformer association dynamics, and ASAG through process-level reasoning diagnostics.

Camera-aware MLLMs connect to PanoWorld-X, SplAttN, VectorWorld, MomaGraph, and GLANCE through geometry-aware multimodal reasoning.

OmniVerifier connects to FRABench/UFEval, WebDevJudge, CounselBench, ASAG, and coverage theory because evaluation becomes an inference-time control mechanism.

RALI connects to PRISM, MetaphorVU, PonderLM-2, and OpenThoughts through structured text representations that compress or replace costly reasoning.

## Emerging Pattern

The broader pattern is mediator-aware generalization. Models generalize better when the relevant mediator is explicit: weight geometry, reasoning graph structure, camera parameters, verifier feedback, or text-aligned quality representation.
