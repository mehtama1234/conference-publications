# ICML 2026 Spotlight Batch 046 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 226-230:

- Asymmetric Multi-View Clustering with Hyperbolic Uncertainty Modeling
- Progressive Graph Structure Adjustment for Homophily Shift Adaptation
- Language Model Circuits Are Sparse in the Neuron Basis
- Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance
- Decoupling Skeleton and Flesh: Efficient Multimodal Table Reasoning with Disentangled Alignment and Structure-aware Guidance

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 225.

## Emerging Pattern 1: Alignment Should Be Asymmetric When Evidence Quality Differs

HAMC uses hyperbolic radial position as a confidence signal, allowing reliable views to guide unreliable ones instead of forcing every view into symmetric agreement. This avoids pulling good representations toward corrupted views.

This connects to VGS, causal route gating, and FlowGuard. Across modalities, alignment is becoming selective: the system needs to know which signal should lead and which should be corrected.

## Emerging Pattern 2: Graph Transfer Requires Structure Repair

PSAHS treats homophily mismatch as a first-class domain-shift variable. It alternates structure adjustment with representation alignment, using conservative agreement between a GNN and MLP to avoid unsafe target edits.

This links to FlatLand, SWING, and graph algorithm papers. The recurring graph lesson is that relational structure itself is part of the domain, not just a container for node features.

## Emerging Pattern 3: Native Neurons May Already Be Sparse Circuits

The neuron-basis circuits paper challenges the assumption that one must train SAEs to get sparse interpretable units. It finds MLP neurons can form sparse causal circuits for agreement and multi-hop reasoning tasks.

This connects to SVD interpretability, FAC Synthesis, FlashTrace, and Robust Harmful Features. Interpretability is becoming more intervention-oriented, and the cheapest useful basis may sometimes be the native one.

## Emerging Pattern 4: Red-Teaming Needs Stable Diverse Attack Generators

Stable-GFN addresses mode collapse and instability in GFlowNet red-team generation by avoiding Z estimation, masking noisy rewards, and stabilizing fluency. The goal is not a single strong attack but a diverse high-risk distribution.

This connects to tail-risk estimation and jailbreak mechanism papers. Safety evaluation increasingly needs coverage of rare or diverse adversarial behaviors, not only benchmark accuracy.

## Emerging Pattern 5: Multimodal Table Reasoning Needs Layout as a Separate Object

DiSCo/Table-GLS separates structural abstraction from semantic grounding, then reasons from global table structure to local evidence. This mirrors the broader theme that intermediate structure improves grounding.

This connects to 3ViewSense, VGS, and causal route gating. Tables are another domain where visual-language alignment alone is insufficient without explicit structural workspaces.

## Cross-Batch Links

- HAMC, VGS, causal route gating, and FlowGuard all make alignment selective based on signal reliability or route contribution.
- PSAHS, FlatLand, SWING, and Riemannian metric matching treat graph or manifold structure as something to estimate, adjust, or exploit.
- Neuron-basis circuits, Robust Harmful Features, and FlashTrace all use internal model components as causal explanatory units.
- Stable-GFN, tail-risk estimation, and jailbreak papers all aim to characterize high-risk safety regions more completely.
- DiSCo/Table-GLS, 3ViewSense, and Seizure-Semiology-Suite show that multimodal reasoning requires domain-specific intermediate structure.

## Deep Theme Update

Batch 046 is about refusing naive symmetry. Views differ in reliability, graph domains differ in homophily, neuron bases may already differ from SAE assumptions, red-team samples should cover diverse modes, and table reasoning must separate skeleton from content. The shared pattern is to respect the nonuniform structure of the evidence instead of forcing every signal through one alignment rule.
