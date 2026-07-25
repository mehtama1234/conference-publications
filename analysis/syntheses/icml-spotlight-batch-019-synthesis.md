# ICML 2026 Spotlight Batch 019 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 91-95:

- Divide-and-Denoise: A Game-Theoretic Method for Fairly Composing Diffusion Models
- SleepLM: Natural-Language Intelligence for Human Sleep
- The Axiomatic Value of Regularization in AI Alignment from Human Preferences
- MASPOB: Bandit-Based Prompt Optimization for Multi-Agent Systems with Graph Neural Networks
- Compositional Generalization Requires Linear, Orthogonal Representations in Vision Embedding Models

Source depth: abstract/metadata only for all five papers. ArXiv acquisition was deferred after repeated 429/503 failures in preceding batches; these papers should be retried later from offset 90.

## Emerging Pattern 1: Composition Needs Explicit Coordination

Divide-and-Denoise treats diffusion composition as a coordination problem. Multiple pretrained models may have useful expertise, but naive combination can let one dominate or create disagreements. The paper's fair division game assigns each model responsibility over regions of the noisy sample at every timestep, making model composition an inference-time allocation problem.

This connects to ParetoPO, MoNet, and multi-agent papers. Across domains, composition is not a free byproduct of adding modules together. It needs responsibility assignment, fairness or dominance rules, and mechanisms for resolving conflict.

## Emerging Pattern 2: Domain Foundation Models Are Becoming Language Interfaces

SleepLM turns polysomnography into a language-grounded domain. Instead of classifying sleep into fixed stages or events, it aligns physiological signals with captions, retrieval, event localization, and targeted natural-language insight generation. The reported dataset scale, over 100K hours from more than 10,000 individuals, suggests a domain-specific foundation-model infrastructure rather than a narrow classifier.

This links to PhenoBrain, dnaHNet, and biomedical foundation-model papers. The shared subtheme is that scientific and healthcare models increasingly expose domain signals through flexible language interfaces.

## Emerging Pattern 3: Alignment Theory Is Absorbing Social Choice and Regularization

The RLHF regularization paper argues that practical reference-policy regularization changes the social-choice properties of preference aggregation. Standard RLHF corresponds to a Borda-style rule, while newer algorithms correspond to von Neumann winner rules; regularization improves the axiomatic properties of the latter but not the former.

This connects to DPO/RLHF equivalence, VALUEFLOW, ParetoPO, and alignment pretraining. Alignment is being analyzed not only as a reward-learning problem but as preference aggregation under disagreement, with normative properties that can be formalized.

## Emerging Pattern 4: Multi-Agent Systems Need Topology-Aware Optimization

MASPOB optimizes prompts in fixed multi-agent workflows using UCB bandits, GNN topology priors, and coordinate ascent. The important assumption is deployment-realistic: workflows may be fixed, evaluations are expensive, and prompts interact through the topology of the agent graph.

This extends OMAC and other agent-process optimization papers. The prompt is no longer a local string; it is a control variable embedded in a multi-agent system with coupled effects.

## Emerging Pattern 5: Compositionality Is Becoming a Geometry Requirement

The compositional vision paper argues that divisibility, transferability, and stability impose linear, orthogonal per-concept structure on representations. The empirical claim across CLIP, SigLIP, and DINO is that partial low-rank near-orthogonal concept factors correlate with generalization to unseen combinations.

This continues the representation-geometry thread from LOES, SVD interpretability, HyperDepth, and spectral papers. Geometry is not just a diagnostic: it may be necessary for certain forms of generalization.

## Cross-Batch Links

- Divide-and-Denoise, ParetoPO, and MoNet all coordinate specialized components under competing objectives.
- SleepLM, PhenoBrain, dnaHNet, and biomedical papers define domain foundation models through structured domain signals.
- RLHF regularization, VALUEFLOW, and DPO/RLHF theory show preference optimization as a formal aggregation problem.
- MASPOB, OMAC, DR Tulu, and Skill-Pro optimize agent processes under limited evaluation or memory budgets.
- Compositional vision, SVD interpretability, LOES, and HyperDepth make linear/spectral/orthogonal structure central to capability.

## Deep Theme Update

Batch 019 reinforces the idea that structure is the hidden substrate of generalization and deployment. Diffusion models need structured responsibility allocation. Sleep foundation models need language-structured physiological supervision. RLHF needs social-choice structure. Multi-agent prompt search needs workflow topology. Vision embeddings need linear-orthogonal concept geometry.

The deeper pattern is explicit structure as the antidote to naive scaling or naive composition.
