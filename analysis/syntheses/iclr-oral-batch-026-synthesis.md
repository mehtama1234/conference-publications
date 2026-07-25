# ICLR Oral Batch 026 Synthesis

## Papers Covered

- True Self-Supervised Novel View Synthesis is Transferable
- Exploring Synthesizable Chemical Space with Iterative Pathway Refinements
- Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models
- Compositional Diffusion with Guided Search for Long-Horizon Planning
- Differentiable Model Predictive Control on the GPU

## Shared Thesis

This batch is about making hidden structure transferable, identifiable, or executable. XFactor tests whether latent pose transfers across scenes. ReaSyn searches molecule space through feasible synthesis pathways. The causal-equivalence paper identifies what can be recovered under arbitrary latents and cycles. CDGS composes local generative models without averaging away modes. GPU differentiable MPC makes structured optimal control fast enough for learning loops. Across the batch, the core object is not just an output but an underlying structure: pose, pathway, equivalence class, local mode composition, or control optimization trajectory.

## Deep Themes

### Transferability as Representation Validity

XFactor uses pose transfer across scenes as the criterion for true self-supervised NVS. This is a strong test for hidden representations: if a latent variable represents camera motion, it should carry the same trajectory into another scene. The paper fits a broader theme where interventions test whether learned factors are real.

### Feasible Pathways Over Desirable Endpoints

ReaSyn shifts molecule generation from endpoint scoring to pathway reasoning. Synthesizable molecules are defined by viable routes through reaction space, so the model must search over synthetic trees. This connects scientific generation to planning: good candidates need feasible construction histories.

### Identifiability Before Causal Estimation

The causal-equivalence paper is a theory-first contribution. It argues that causal discovery with arbitrary latents and cycles cannot be general without knowing the equivalence class. Edge rank constraints become a way to characterize what observed distributions can identify.

### Search Inside Generative Planning

CDGS embeds guided search in diffusion denoising so local multimodal plans can compose into global coherence. This directly addresses mode averaging, a recurring problem whenever local generative pieces are combined. The method turns diffusion sampling into structured planning.

### Accelerator-Native Classical Control

GPU differentiable MPC modernizes a classical control loop for learning systems. The method is not replacing MPC with a black-box policy; it makes MPC differentiable and efficient enough to live inside RL and imitation-learning training.

## Cross-Paper Pattern

The common pattern is structure-preserving search. The search space may be latent poses, synthesis pathways, causal graphs, local trajectory modes, or control updates. In each case, success depends on preserving constraints that naive generation or estimation would hide: transferability, synthesizability, equivalence, multimodality, and temporal optimization structure.

## Subthemes to Track

- Transferable self-supervised NVS.
- Synthesizable pathway refinement.
- Latent-variable cyclic causal equivalence.
- Compositional diffusion with guided search.
- GPU differentiable MPC.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details and implementation specifics should be upgraded when PDFs are available.
