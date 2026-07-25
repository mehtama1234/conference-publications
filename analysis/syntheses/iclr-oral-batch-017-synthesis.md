# ICLR Oral Batch 017 Synthesis

## Papers Covered

- NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale
- On the Wasserstein Geodesic Principal Component Analysis of Probability Measures
- Train-before-Test Harmonizes Language Model Rankings
- DepthLM: Metric Depth from Vision Language Models
- PetaGAIL++: Utility Optimized Private Trajectory Generation with Imitation Learning

## Shared Thesis

This batch is about choosing the right representation and evaluation lens for the object being modeled. NextStep-1 avoids discrete visual bottlenecks by using continuous image tokens. Wasserstein GPCA respects probability-measure geometry rather than flattening distributions into Euclidean vectors. Train-before-test measures model potential after controlled adaptation instead of noisy direct performance. DepthLM unlocks metric 3D perception through visual prompting and camera-aware augmentation. PetaGAIL++ adapts privacy noise to sample sensitivity in trajectory generation. Each paper argues that the naive interface, token, metric, or perturbation scheme hides the relevant structure.

## Deep Themes

### Continuous and Geometric Representation

NextStep-1 and Wasserstein GPCA both challenge discrete or Euclidean simplifications. NextStep-1 treats visual generation as continuous-token autoregression with a flow head. Wasserstein GPCA treats distributions as objects living in transport geometry. The shared pattern is that performance depends on preserving the geometry of the domain rather than forcing everything through a convenient but lossy representation.

### Evaluation After Adaptation

Train-before-test changes the interpretation of benchmark rankings. Instead of asking only which model performs best immediately, it asks which model has the greatest potential after matched fine-tuning. This connects to the broader 2026 evaluation shift: benchmark design increasingly needs to separate model quality from prompting, tuning, tool access, and deployment surface.

### Interface-Driven Multimodal Capability

DepthLM suggests VLMs may contain more spatial ability than direct tests reveal. Visual prompting and intrinsic-conditioned augmentation expose metric-depth capability without new dense heads. This resembles the graph-inference result from the prior batch: the model interface can be the limiting factor for structured reasoning.

### Privacy as Adaptive Representation Perturbation

PetaGAIL++ frames privacy not as uniform degradation, but as sensitivity-aware noise allocation. For mobility trajectories, privacy risk is uneven across samples, locations, and routines. Adaptive privacy mechanisms therefore become representation controls that preserve utility while protecting high-risk cases.

## Cross-Paper Pattern

The common pattern is domain-faithful measurement. Continuous images need continuous tokens, distributions need Wasserstein geodesics, model comparisons need adaptation-aware rankings, VLM depth needs camera-aware interfaces, and mobility data needs sensitivity-aware privacy. The papers all resist generic abstractions when domain-specific structure determines the real failure mode.

## Subthemes to Track

- Continuous-token autoregressive image generation.
- Wasserstein geometry for probability measures.
- Train-before-test model-potential evaluation.
- Visual prompting for metric 3D VLMs.
- Sensitivity-aware differentially private trajectory synthesis.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Details should be upgraded when official PDFs or high-confidence arXiv matches are available.
