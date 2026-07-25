# ICML 2026 Spotlight Batch 074 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 366-370:

- Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance
- Hista and Numca: Estimate State Value Effectively for Large Language Model Reinforcement Learning
- Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers
- Privacy-Aware Video Anomaly Detection through Orthogonal Subspace Projection
- Overcoming PINNs Failure Modes In High Dimension With Low-Rank Fourier Sum

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 365.

## Emerging Pattern 1: Weak or Imperfect Signals Can Work When Structure Carries the Load

Weak diffusion priors work when measurements are informative and local image correlations transfer. G-OPL uses weak face-presence supervision to remove privacy-sensitive attributes. Hista uses hidden-state similarity and disjoint rollouts to improve value estimation.

The shared pattern is conditional usefulness: weak signals become valuable when the system has the right structural scaffold.

## Emerging Pattern 2: Process Credit Assignment Keeps Reappearing

Hista/Numca estimate intermediate state values in LLM RL. Multimodal ICL analysis identifies induction-style circuits that copy labels from matching exemplars. OPL separates anomaly-relevant pose/motion from sensitive facial attributes.

All three papers localize what part of the process deserves credit: a partial reasoning state, a circuit mechanism, or a representation subspace.

## Emerging Pattern 3: Multimodal Capability Is Not Symmetric

The multimodal ICL paper finds that a high-diversity primary modality can scaffold a much lower-complexity secondary modality. VideoKR and MoCA similarly imply that multimodal reasoning is a structured composition of uneven perceptual, reasoning, and knowledge components.

This is a corrective to simple "fuse modalities" stories: cross-modal learning may depend on which modality supplies the algorithmic backbone.

## Emerging Pattern 4: Privacy and Safety Are Being Built Into Representations

G-OPL suppresses facial information inside the feature representation rather than filtering outputs. This connects to PACT, which internalizes physical constraints inside diffusion policies.

The shared design move is preemptive constraint embedding: make the model's internal representation or trajectory less capable of violating the deployment constraint.

## Emerging Pattern 5: Scientific ML Is Replacing Sampling Noise With Analytic Structure

LoRFS avoids collocation noise by using separable Fourier expansions with closed-form residual and variational losses. This echoes Jacobi Spectral Reconstruction and Dirac-Frenkel-Onsager work, where the right representation or gauge makes difficult numerical dynamics tractable.

The broader theme is that high-dimensional scientific ML may need domain-native bases, not only larger generic networks.

## Cross-Batch Links

- Weak diffusion priors connect to MOG, KPE/KTS, Tilt Matching, Local Diffusion Composition, and Noisy Sample Compression.
- Hista/Numca connect to T2PO, UDM-GRPO, MoCA, Weak-Strong Verification, and process-reward papers.
- Multimodal ICL connects to Symmetry ICL Dynamics, Context-Parameter Equivalence, MoCA, Agent0-VL, and Visual Attribution Streaming.
- Privacy-aware VAD connects to CreDRO, unlearning/privacy work, VenusBench-Mobile, and representation disentanglement.
- LoRFS connects to ReViT, Jacobi Spectral Reconstruction, Dirac-Frenkel-Onsager dynamics, and scientific-control papers.

## Deep Theme Update

Batch 074 emphasizes conditional structure: weak priors, weak privacy labels, hidden-state value estimates, multimodal circuits, and Fourier bases all work because the method identifies the structure that makes a limited signal useful.
