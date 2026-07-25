# ICML 2026 Spotlight Batch 033 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 161-165:

- Beyond First-order Asymptotics in Sequential Mean Testing
- Geometry-Aware Decoding with Wasserstein-Regularized Truncation and Mass Penalties for Large Language Models
- Don't Reinvent the Wheel, Just Realign the Spokes: Resource-Efficient Federated Fine-Tuning via Rank-Wise Expert Assembly
- Learning Coupled Continuous-Time Latent Dynamics from Irregular Events
- 3ViewSense: Spatial and Mental Perspective Reasoning from Orthographic Views in Vision-Language Models

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 160.

## Emerging Pattern 1: Guarantees Are Getting More Operational

The sequential-testing paper moves past first-order expected stopping-time optimality and asks how the stopping time itself fluctuates. This is a more operational kind of guarantee: not only the leading asymptotic cost, but the uncertainty around that cost.

This connects to a broader corpus theme in which evaluation is becoming distributional and process-aware. Average-case success is often insufficient when the deployment question is when to stop, how much compute to spend, or how stable the decision process is.

## Emerging Pattern 2: Geometry Is a Test-Time Control Surface

Top-W applies Wasserstein geometry over token embeddings to LLM decoding, while 3ViewSense uses orthographic geometry as an intermediate workspace for VLM spatial reasoning. Both papers argue that generation or reasoning improves when inference is constrained by an explicit geometry rather than raw scores alone.

This links to SSMoE, FlatLand, analogy mechanisms, and VGGT-Motion. The geometry theme is now broad: token neighborhoods, expert spectra, graph curvature, spatial projections, and camera/pose structure all become control interfaces.

## Emerging Pattern 3: Modular Reuse Beats Full Relearning Under Constraints

SmartFed decomposes existing LoRA modules into rank-wise experts and routes them according to semantics and resource budgets. Like SSMoE, it treats existing model components as reusable inventory rather than material to be retrained wholesale.

This is especially important for federated and edge settings, where compute, communication, and privacy constraints make full model updates unrealistic. The common move is to extract finer-grained modularity from artifacts that were originally trained as larger blocks.

## Emerging Pattern 4: Real-World Time Is Continuous, Coupled, and Sparse

CoCLD models irregular event streams as coupled continuous-time individual and population processes, using diffusion interpolation and neural ODEs to align states at arbitrary times. This pushes against discrete-time approximations that are convenient but poorly matched to asynchronous data.

The deeper link is to long-context and dynamical-system papers: a model's temporal substrate matters. Treating time as a regular token index loses structure that may be essential for mobility, behavior, health, and other sparse real-world processes.

## Cross-Batch Links

- Sequential testing connects to bandit, online-learning, and evaluation papers that care about stopping behavior and finite-threshold variability.
- Top-W connects to test-time scaling, decoding, and geometry papers where fixed models gain capability from better inference-time policies.
- SmartFed connects to FlatLand and SSMoE through federated personalization, expert routing, and resource-aware modularity.
- CoCLD connects to continuous dynamics, diffusion, and long-context sequence modeling through latent-state interpolation over irregular observations.
- 3ViewSense connects to VGGT-Motion, SpatioLM, and spatial benchmark papers through explicit geometry for embodied and multimodal intelligence.

## Deep Theme Update

Batch 033 is about making hidden structure explicit at the point of decision: second-order stopping variability, token-space geometry, rank-level adapter capacity, continuous-time latent processes, and orthographic spatial workspaces. The shared pattern is that better performance comes from exposing the right intermediate structure rather than relying on an undifferentiated end-to-end model.
