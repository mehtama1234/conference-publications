# ICML 2026 Spotlight Batch 101 Synthesis

## Papers

- Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense
- SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion
- Reverse Flow Matching: A Unified Framework for Online Reinforcement Learning with Diffusion and Flow Models
- Information Flow Reveals When to Trust Language Models
- Path-dependent Discrete Amortized Inference

## Source Depth

All five notes are abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Details still need checking from full papers when official or arXiv PDFs become accessible.

## Shared Thesis

This batch is about distinguishing robust behavior from brittle mechanism. Prompt-injection defenses can look secure by suppressing text the task needed; point-cloud completion can look multimodal while barely using the image; diffusion and flow policies need training objectives that target the actual RL-induced distribution; RAG systems need confidence measures tied to internal evidence flow; and discrete amortized samplers need histories that expose construction-path ambiguity.

The common pattern is pathway-sensitive evaluation and training. The papers ask not only whether the final output is good, but whether the system used the right information pathway, preserved the right signal, or conditioned on the right history.

## Subthemes

### Security-fidelity frontiers

SecFid shows why attack-success rate is an incomplete safety metric. A defense that ignores injected text and a defense that faithfully processes it as data can both avoid the attack, but only one preserves task utility. The deeper theme is that safety benchmarks must distinguish mechanisms of success, not just successful avoidance.

### Cross-modal connection repair

SplAttN treats 2D-3D fusion as a signal-preservation problem. Hard projection and sparse correspondences can make point-cloud completion appear image-conditioned while starving the geometry model of useful visual evidence. Gaussian soft splatting turns the image-point bridge into a denser differentiable pathway, and counterfactual visual-removal tests probe whether the model actually uses that pathway.

### Q-induced generative policy training

Reverse Flow Matching links diffusion and flow policies through a shared estimator view for online RL. The policy target is not just a generative model likelihood; it is a Boltzmann distribution induced by value. The important abstraction is training a flexible sampler toward a moving control objective without requiring direct target samples.

### Grounding by information flow

Information Flow Reveals When to Trust Language Models shifts RAG confidence away from retrieval presence alone. The relevant question is whether context tokens contribute through the model's layers in a relevance-aligned and concentrated way. Trust becomes an internal-use property: a system may retrieve the right evidence yet fail to route it into the answer.

### Path-dependent discrete sampling

Path-dependent Discrete Amortized Inference attacks state aliasing in construction-based samplers. If multiple trajectories reach the same partial object with different posterior implications, a Markov state policy loses information. Lifting the construction process with latent dynamics lets the sampler condition on construction history, which broadens the GFlowNet-style view of amortized inference.

## Cross-Batch Connections

SecFid connects to MiniAppBench, PIPE, and RACO through the same warning: single-axis success hides tradeoffs between compliance, security, utility, and preference objectives. It also aligns with conformal policy control because deployment costs define the right operating point.

SplAttN links to WIRE, ConFlux, DroneDINO, and concept-binding work: multimodal performance depends on preserving the right cross-modal correspondences, not merely concatenating modalities.

Reverse Flow Matching connects to GWF, XDLM, any-order GPT, and insertion processes through sampler training under structured objectives. It also relates to DAWN and ScaleMoE as part of the broader trend of post-training systems that reshape base generative behavior under control signals.

Information-flow trust connects to DecodeShare, Assistant Axis, temporal graph memory explanation, and hallucination rate-distortion. Across these papers, explanation is becoming a diagnostic of when internal computation actually uses the intended evidence.

Path-dependent inference connects to POPGym, HSR, LatentMAS, and Bayesian hypergraph work through memory and latent-state recovery. The shared issue is that observable state is often too compressed for optimal decisions, sampling, or explanation.

## Emerging Pattern

The larger ICML pattern is a move from outcome scoring to mechanism-aware reliability. Robust systems increasingly need tests or objectives that reveal whether the output arose from faithful text processing, real modality use, correct value-induced sampling, grounded context flow, or non-aliased construction history.
