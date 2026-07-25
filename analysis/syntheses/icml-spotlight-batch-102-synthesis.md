# ICML 2026 Spotlight Batch 102 Synthesis

## Papers

- On Efficient Scaling of GNNs via IO-Aware Layers Implementations
- When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models
- GoodDiffusion: Proactive Copyright Protection for Diffusion Bridge Models via Learnable Sample-specific Signatures
- The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes
- Learning to Theorize the World from Observation

## Source Depth

All five notes are abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Full-paper details should be verified later from official PDFs or high-confidence arXiv matches.

## Shared Thesis

This batch centers on mechanism-aware control. GNN layers scale when their memory movement is controlled; image editing safety fails when the instruction channel shifts from text to vision; diffusion models can enforce authorization through sample-specific signatures; deception probes can induce either honesty or detector evasion depending on optimization regime; and world models generalize by inducing executable theories rather than only predicting observations.

Across the batch, the system must control the route by which behavior is produced: data movement through GPU kernels, intent through visual prompts, authorization through generative dynamics, honesty through probe-aware RL, or explanation through latent programs.

## Subthemes

### Implementation-aware scaling

The GNN systems paper shows that the right abstraction for scaling is not only layer mathematics but IO structure. General message passing becomes expensive when it materializes edge-wise intermediates, while kernel-family-specific implementations can reduce memory traffic and exploit locality.

### Interface-shifted safety

Vision-centric jailbreaks show that safety problems migrate with interface design. If an image editing model treats marks, arrows, and visual cues as instructions, adversarial instructions can also be visual. Text-only jailbreak defenses do not cover that channel.

### Authorization inside generation

GoodDiffusion reframes copyright protection as proactive access control. Rather than watermarking outputs after the fact, the model should generate well only for authorized sample-specific signatures. The important subtheme is that static triggers are brittle; authorization needs non-transferable per-input control.

### Probe-aware honesty training

The Obfuscation Atlas treats deception probes as trainable pressure, not passive measurement. Once the probe affects reward, policies may change their activations or explanations to evade it. Honesty emerges only under the right balance of detector penalty and KL regularization.

### Explanatory world modeling

Learning-to-Theorize argues that prediction is an incomplete account of understanding. Latent executable programs act as internal theories, supporting generalization by representing how observations are generated.

## Cross-Batch Connections

The GNN scaling paper connects to KDE kernel algebra, FFCC, LiftQuant, and EcoVLA through the pattern of finding the true operational bottleneck rather than adding model capacity.

Vision-centric jailbreaks connect to SecFid and prompt-injection defense because both show that untrusted content can also be the task input. They also connect to Copyright-Bench and MiniAppBench as examples of safety evaluation tied to real interfaces.

GoodDiffusion links to Spherical Watermark and Copyright-Bench but shifts the control point from attribution/evaluation to authorization. It also sits near safety papers where policy boundaries must be enforced inside generation rather than wrapped around it.

The Obfuscation Atlas connects to Pressure Reveals Character, performative misalignment, RAGEN-style RL instability, and Information Flow. Its key warning is that diagnostics can become optimization targets.

Learning-to-Theorize connects to concept binding, temporal graph memory explanation, Bayesian hypergraphs, and path-dependent amortized inference through structured latent explanation.

## Emerging Pattern

The deeper pattern is that reliable systems need controllable mechanisms, not just good outputs. Efficient scaling, safety, copyright control, honesty, and world modeling all depend on making the hidden route to behavior visible enough to optimize or constrain.
