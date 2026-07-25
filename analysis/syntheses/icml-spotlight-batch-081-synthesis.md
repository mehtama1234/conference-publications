# ICML 2026 Spotlight Batch 081 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 401-405:

- A Causal Decomposition Approach for Fair Contextual Multi-Armed Bandits
- Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge
- Disentangling Geometry, Performance, and Training in Language Models
- ThunderAgent: A Fast, Simple, and Program-Aware Agentic Inference System
- Walrus: A Cross-domain Foundation Model for Continuum Dynamics

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 400.

## Emerging Pattern 1: Decomposition Makes Normative Constraints Operational

Fair contextual bandits decompose fairness into counterfactual direct, indirect, and spurious effects. This parallels DiCoLa's causal decomposition and DPO/RePO's decomposition of preference semantics.

The shared theme is that normative goals become trainable only when decomposed into quantities that can be estimated and constrained.

## Emerging Pattern 2: Small Data Recipes Can Change Reasoning Bias

Identity Bridge challenges the view that the reversal curse is an inherent autoregressive limitation. Adding simple A -> A examples can alter gradient-descent implicit bias and improve reverse relation inference.

This connects to PRISM, VideoKR, and other data-design papers: the structure of examples can matter more than raw volume for inducing the desired rule.

## Emerging Pattern 3: Geometry Is Useful but Easy to Overinterpret

The geometry-performance paper finds that effective rank and related metrics mainly reflect training choices and do not reliably predict downstream performance. This is an important caution for representation-geometry work.

Across the corpus, geometry is often a control surface; this paper reminds us it is also a confounded measurement surface.

## Emerging Pattern 4: Agent Systems Need Program-Level Scheduling

ThunderAgent abstracts workflows as LLM Programs and schedules KV cache, state, tools, disk, and network resources together. It moves beyond per-request serving toward end-to-end workflow-aware infrastructure.

This links to CONTINUUM's tensor memory virtualization: dynamic ML workloads need abstractions that expose the real computational unit.

## Emerging Pattern 5: Scientific Foundation Models Are Full-Stack Systems

Walrus combines stabilization, distributed 2D-3D training, adaptive tokenization, and broad continuum-dynamics pretraining. Like ReViT, LoRFS, LASER, and Generative Filtering, it shows that physical foundation models require numerical and systems choices embedded into the model recipe.

## Cross-Batch Links

- Fair contextual bandits connect to DiCoLa, Unpaired Causal IV, SCIQL, and causal fairness/control themes.
- Identity Bridge connects to 2-SAT Robustness, Symmetry ICL Dynamics, PRISM, and data-design papers.
- Geometry/performance disentanglement connects to Isotropic Gaussian RL, Fisher Memory Dynamics, Weight-Space Expressivity, and representation diagnostics.
- ThunderAgent connects to CONTINUUM, daVinci-Dev, RoTS, Agent0-VL, and agent serving/RL rollout systems.
- Walrus connects to LASER, ReViT, LoRFS, Generative Filtering, NeuronCtrl, and scientific foundation-model work.

## Deep Theme Update

Batch 081 emphasizes that modern ML systems are shaped by hidden structure: causal pathways behind fairness, identity examples behind reversal generalization, hyperparameters behind geometry metrics, workflow programs behind agent serving, and numerical stability behind scientific foundation models.
