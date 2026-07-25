# ICML 2026 Spotlight Batch 106 Synthesis

## Papers

- PonderLM-2: Pretraining LLM with Latent Thoughts in Continuous Space
- DAVE: Distribution-Aware Attribution via ViT Gradient Decomposition
- Why Linear Recurrent Memory Works in Partially Observable Reinforcement Learning
- Self-Soupervision: Cooking Model Soups without Labels
- Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs

## Source Depth

All five notes are abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Full-paper details should be verified from official PDFs or high-confidence arXiv matches when available.

## Shared Thesis

This batch is about using hidden structure more efficiently: latent thoughts provide continuous internal compute; DAVE decomposes gradients to reveal stable ViT evidence; linear recurrent filters recover belief-like memory in partially observable settings; Self-Soupervision combines unlabeled self-supervised ingredients; and SGD exposes sparse RLVR updates that AdamW may obscure.

The common pattern is that capability is not only in larger models or more labels. It appears when training or analysis finds the right internal process: hidden deliberation, artifact-free gradients, sufficient-statistic memory, mergeable SSL trajectories, or sparse reward-driven parameter movement.

## Subthemes

### Hidden continuous reasoning

PonderLM-2 shifts chain-of-thought-like scaling into continuous hidden states. Instead of emitting intermediate text, the model learns latent thought steps before each token. This creates a less visible but potentially more efficient form of per-token deliberation.

### Architecture-aware attribution

DAVE shows that ViT explanations must account for patch embeddings and attention routing. Gradient attribution is not enough if the gradient is polluted by architectural artifacts. The method's decomposition isolates stable locally equivariant components.

### Linear memory under structure

The linear recurrent memory paper explains why simple linear RNNs can work in partially observable RL. In HMM-like settings with deterministic or nearly deterministic transitions, linear filters can recover belief logits or nearly eliminate state ambiguity.

### Label-free model composition

Self-Soupervision expands model soups beyond supervised learning. Unlabeled data, shifted distributions, and different SSL algorithms become ingredients for robust merged models, suggesting that parameter-space compatibility can survive objective diversity.

### RLVR-specific optimization

The SGD-for-RLVR paper challenges the default transfer of AdamW from pretraining/SFT into RL. RLVR appears to rely less on momentum and adaptive learning rates, and SGD can produce extremely sparse useful updates.

## Cross-Batch Connections

PonderLM-2 connects to Ctrl-R, H1, reasoning dimensionality, and Stop When Further Reasoning Won't Help through computation allocation for reasoning. It adds the hidden-state version of the theme.

DAVE connects to Information Flow, Assistant Axis, temporal graph memory explanations, and Motion Attribution because it treats explanation as pathway recovery inside a specific architecture.

Linear recurrent memory connects to POPGym, LAMP, path-dependent inference, and VectorWorld through partial observability and the need to retain the right history.

Self-Soupervision connects to NASH, model merging, modular access control, and data-selection themes: trained components and trajectories become reusable material.

SGD in RLVR connects to Beyond Muon, Adam degeneracy, DAWN, RAGEN-2, Ctrl-R, and Obfuscation Atlas. Together they suggest post-training has its own optimization geometry.

## Emerging Pattern

The emerging pattern is efficient internalization. The papers show models doing more with hidden computation, cleaner explanation signals, simpler memory, unlabeled model composition, or sparse optimizer updates rather than brute-force scale alone.
