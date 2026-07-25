# ICML 2026 Spotlight Batch 087 Synthesis

Papers covered: 00431-00435.

## Batch Thesis

This batch studies the boundary between capability and controllability. WestWorld scales embodied prediction by conditioning on robot morphology; post-training theory shows policy gradients improve what the base model already covers but hit a support barrier outside it; DHSA extends long-context inference by predicting sparse dependencies online; exact RL unlearning makes deletion possible only when stability is built into the learner; and LLM annotation work shows prompts cannot reliably override internalized task priors.

The common pattern is that adaptation has preconditions. A model can transfer, post-train, sparsify, unlearn, or follow a rubric only when the underlying representation and algorithm were structured to make that adaptation reachable.

## Cross-Paper Themes

### 1. Adaptation Depends on Latent Coverage

The post-training paper makes this explicit with the base-model barrier: outcome-reward policy gradients cannot efficiently discover sequences outside the base model's support. The LLM annotation paper gives the behavioral version: prompts cannot easily rescue high-confidence errors when the model's internal definition conflicts with the intended task.

WestWorld and DHSA offer constructive analogues. WestWorld improves transfer by encoding robot morphology; DHSA adapts attention by learning online sparsity patterns. In both cases, adaptation works because the system has a representation that exposes the relevant variation.

### 2. Structure Turns Scaling Into Generalization

WestWorld uses system-aware routing and structural embeddings to scale across robots. DHSA uses hierarchical chunk-to-token routing to scale across long contexts. Exact RL unlearning uses TV stability to scale deletion handling without full retraining.

Across these papers, scalable systems are not unstructured large models. They are models with explicit handles: morphology, likelihood quantiles, chunk importance, stability parameters, or definition-specific familiarity.

### 3. Governance Constraints Must Be Designed In

Exact RL unlearning and LLM annotation reliability both frame governance as an algorithmic property. For unlearning, the learner must be stable enough that deletion can reproduce the counterfactual distribution. For annotation, the model must align with the requested definition rather than merely produce confident labels.

This connects to safety and evaluation work elsewhere in the corpus: the desired behavior cannot be assumed from output quality alone. The system needs a measurable property that tracks the governance requirement.

### 4. Efficiency Enables New Workflows, But It Also Imposes Risk

DHSA makes 100K-context inference feasible on a single 24GB GPU, which changes who can run long-context models. WestWorld's scalable trajectory prediction enables downstream model-based control across robots. But both introduce routing errors: sparse attention may drop important dependencies, and MoE dynamics may misroute unfamiliar systems.

The batch therefore reinforces an engineering theme: efficiency techniques are capability enablers only when their failure modes are made visible.

## Deep Subthemes

### Morphology-Aware Embodied Foundation Models

WestWorld suggests that robotics scaling requires explicit physical descriptors. Robot identity is not a label to memorize; morphology is part of the causal structure of the dynamics.

### Post-Training as Conditional Amplification

Policy-gradient optimality is conditional on base-model likelihood. The result reframes RL post-training as amplification of reachable behavior, with process rewards serving as a way to densify the search path.

### Adaptive Sparse Context

DHSA's hierarchy shows a practical way to avoid all-pairs attention without freezing sparsity into a fixed template. Long-context inference becomes a routing problem over evidence-bearing chunks and tokens.

### Exact Deletion Through Stability

Exact RL unlearning makes a strong claim: deletion correctness requires indistinguishability from never having trained on the deleted user's data. Achieving that cheaply requires stability from the start.

### Definition Alignment Beats Memorization

The annotation paper separates conceptual familiarity from textual exposure. A model can have seen similar text and still apply the wrong rubric; conversely, better alignment with the task definition predicts performance.

## Common Pattern

The deepest shared pattern is that modern ML systems are being judged by how they adapt under constraints: new robot bodies, reward feedback, long contexts, deletion requests, and user-provided definitions. The batch's answer is consistent: build the relevant constraint into the representation or algorithm. Prompting, scaling, or post-hoc correction alone is not enough.
