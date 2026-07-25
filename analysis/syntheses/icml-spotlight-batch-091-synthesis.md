# ICML 2026 Spotlight Batch 091 Synthesis

Papers covered: 00451-00455.

## Batch Thesis

This batch is about stabilizing and aligning systems that must operate under shifting contexts: LLM persona drift, continual skill acquisition, dependent categorical explanations, redundant musculoskeletal actuation, and heterogeneous federated clients. The shared move is to identify a lower-dimensional or anchor-like structure that makes adaptation controllable: an Assistant Axis, self-distilled on-policy teacher, categorical Fourier decomposition, joint-space empowerment manifold, or semantic federation anchors.

The batch adds detail to a recurring ICML 2026 theme: robustness often comes from finding the right internal coordinate system.

## Cross-Paper Themes

### 1. Alignment Is a Latent-State Problem

The Assistant Axis paper treats persona safety as a geometric direction in activation space. SDFT treats continual learning as a distributional alignment problem between demonstration-conditioned behavior and trainable policy behavior. FedARC aligns client representations through semantic anchors.

Across all three, output behavior is controlled by an underlying representation: persona location, self-generated policy targets, or shared embedding anchors.

### 2. Dependence and Redundancy Should Be Modeled, Not Ignored

Functional ANOVA for categorical inputs handles feature dependence directly instead of assuming independence for convenience. JoSE treats muscle redundancy as evidence of a lower-dimensional controllable manifold. FedARC treats client heterogeneity as a structured residual mismatch rather than random noise.

The batch repeatedly converts apparent messiness into exploitable structure.

### 3. Continual and Federated Learning Need Distribution-Aware Transfer

SDFT reduces forgetting by making demonstration learning more on-policy. FedARC improves transfer by aligning local and global embeddings while allowing client-specific fusion. Both reject naive averaging or imitation when distributions differ.

This connects to post-training support-barrier theory: adaptation succeeds when the training signal is aligned with the learner's reachable distribution.

### 4. Interpretability Is Becoming Exact and Distribution-Respecting

The categorical ANOVA paper joins Verified SHAP and attribution-theory work by rebuilding explanation around exactness and assumptions. Its key contribution is not a prettier attribution method but removing the independence assumption for categorical features.

This reflects a broader shift from approximate explanatory folklore toward mathematically specified explanation targets.

## Deep Subthemes

### Persona Geometry

Default assistant behavior appears to occupy a measurable activation-space region. Safety interventions can therefore target latent positioning, not only prompt templates or output filters.

### On-Policy Demonstration Learning

SDFT turns in-context demonstration behavior into self-generated training targets. The important distinction is that demonstrations condition the teacher rather than directly becoming off-policy imitation data.

### Dependent Categorical Explainability

Exact functional ANOVA under arbitrary categorical dependence matters because real categorical features often have constrained support. Explanation under impossible counterfactual combinations can be misleading.

### Empowerment-Based Action Manifolds

JoSE uses mutual information to discover how low-dimensional latent actions control mechanical degrees of freedom. This is a principled route to muscle synergies and dexterous control.

### Federated Semantic Anchoring

FedARC uses anchors and residual compensation to coordinate heterogeneous clients. It preserves local specificity while enabling shared representation transfer.

## Common Pattern

The shared design principle is coordinate choice. In each paper, the hard problem becomes easier once behavior is expressed in a useful coordinate system: assistant direction, on-policy self-distilled targets, categorical Fourier components, empowered joint-space manifolds, or semantic anchors. This is a strong motif for the broader synthesis: deep themes often live in the representation where adaptation is stable.
