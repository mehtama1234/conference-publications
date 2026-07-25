# ICML 2026 Spotlight Batch 080 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 396-400:

- A Recursive Decomposition Framework for Causal Structure Learning in the Presence of Latent Variables
- Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding
- Decision Transformers As Zero-Shot Learners via Text-Behavior Alignment
- Offline Reinforcement Learning of High-Quality Behaviors Under Robust Style Alignment
- L2G-NET: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 395.

## Emerging Pattern 1: Decomposition Makes Hard Global Structure Learnable

DiCoLa recursively decomposes latent-variable causal discovery and reconstructs the global ancestral graph. L2G-Net decomposes the graph Fourier transform into subgraph spectral operators linked by Cauchy matrices.

Both papers show the same structural move in different domains: split the global object into tractable local pieces, then use a principled reconstruction/factorization step to recover global information.

## Emerging Pattern 2: Language Is Becoming a Grounding Interface for Control

FutureCAD uses natural language to select B-Rep primitives inside executable CAD programs. TG-DT uses natural-language task descriptions to condition Decision Transformer policies for unseen offline RL tasks.

In both cases, language is not just prompt text. It is an interface to structured action spaces: geometry operations in CAD and behavior policies in RL.

## Emerging Pattern 3: Alignment Extends Beyond Human Preference to Behavior Style

SCIQL optimizes task performance while preserving explicit behavior style under offline distribution shift. TG-DT aligns text and behavior. FutureCAD aligns text queries with B-Rep primitives.

This broadens alignment: systems must align not only with preference labels but with task descriptions, geometric references, and qualitative behavior constraints.

## Emerging Pattern 4: Executable Environments Demand Grounded Intermediate References

FutureCAD's key bottleneck is selecting the right B-Rep primitives for operations like fillets and chamfers. Formal Problem-Solving similarly requires Lean metavariables and proof obligations, while Bitween requires verified reductions.

The cross-batch theme is that executable generation depends on correct intermediate references, not just valid-looking final text.

## Emerging Pattern 5: Long-Range Structure Needs Mathematical Factorization

L2G-Net targets long-range graph dependencies by making global spectral information scalable. This links to ReViT, LoRFS, and Jacobi Spectral Reconstruction: mathematical factorization can expose global structure without brute-force computation.

## Cross-Batch Links

- DiCoLa connects to OU Identifiability, Unpaired Causal IV, Source Screening, and Noisy Sample Compression.
- FutureCAD connects to Formal Problem-Solving, Bitween, daVinci-Dev, and executable program-generation papers.
- TG-DT connects to EcoVLA, Agent0-VL, PRISM, VideoKR, and style-conditioned offline RL.
- SCIQL connects to TG-DT, Distributional IRL, RePO, and alignment-feedback papers.
- L2G-Net connects to OENN/CENN, FlashSketch, Jacobi Spectral Reconstruction, ReViT, and graph spectral methods.

## Deep Theme Update

Batch 080 closes this stub window with a strong structure-grounding theme: global causal graphs, CAD boundary primitives, text-conditioned behaviors, style manifolds, and spectral graph transforms all require models that connect local evidence to global constraints.
