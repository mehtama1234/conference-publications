# ICML 2026 Spotlight Batch 029 Synthesis

## Scope

This synthesis covers ICML 2026 spotlight notes 141-145:

- DGS-Net: Distillation-Guided Gradient Surgery for CLIP Fine-Tuning in AI-Generated Image Detection
- Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning
- Securing Multimodal AI through Internal Information Decomposition
- Unifying and Optimizing Data Values for Selection via Sequential Decision-Making
- Less is Enough: Synthesizing Diverse Data in LLM Feature Space with Sparse Autoencoders

Source depth: abstract/metadata only for all five papers. ArXiv acquisition remains deferred after repeated rate-limit/service failures; these papers should be retried later from offset 140.

## Emerging Pattern 1: Security Fine-Tuning Needs Prior Preservation

DGS-Net addresses AI-generated image detection by fine-tuning CLIP without erasing the priors that make CLIP transfer. Gradient surgery separates harmful and beneficial descent directions, using a frozen CLIP encoder to guide what should be preserved.

This connects to model surgery, CLIP fine-tuning, and synthetic-media security papers. Security detectors must adapt to new generators without over-specializing to the current generation distribution.

## Emerging Pattern 2: Foundation Representations Can Amplify Human Feedback

VOTP uses video foundation model representations plus optimal transport to propagate a handful of preference labels to large unlabeled offline RL datasets. The core idea is that trajectory geometry in a strong representation space can turn sparse feedback into pseudo-labels.

This connects to DreamDojo, RoboMME, and preference-learning papers. In robotics, human labels are expensive, so foundation-model geometry becomes a multiplier for feedback efficiency.

## Emerging Pattern 3: Multimodal Safety Must Inspect Fusion

FlowGuard targets attacks that distribute malicious intent across modalities. It monitors the internal fusion process by comparing text-only, vision-only, and fused outputs through FlowVectors inspired by information decomposition.

This extends VISUALSWAP and multimodal safety work. A recurring lesson is that multimodal failures happen at the interaction layer: the model may be safe per modality but unsafe after fusion.

## Emerging Pattern 4: Data Selection Is Becoming Sequential Decision-Making

The data valuation paper reframes selection as a sequential decision process. Data Shapley and related values become myopic approximations to an optimal policy, and a bipartite graph surrogate preserves enough submodular structure for scalable selection.

This links to FAC Synthesis and data-centric LLM optimization. Dataset construction is no longer a bag-level scoring task; it is an ordered intervention process.

## Emerging Pattern 5: Synthetic Data Is Moving into Feature Space

FAC Synthesis uses sparse autoencoders to identify missing interpretable features in a seed dataset, then synthesizes examples to cover those features. The claim that feature spaces transfer across LLaMA, Mistral, and Qwen is especially important for reusable data-centric workflows.

This connects to Activation Oracles, Shared Semantics, and representation-based data selection. Data diversity is increasingly defined by internal model features rather than surface text variation.

## Cross-Batch Links

- DGS-Net, FlowGuard, Concept Removal Guidance, and Jailbreak Foundry form a multimodal/security-control cluster.
- VOTP, DreamDojo, and dWorldEval use video/foundation-model representations for robotics supervision and evaluation.
- Sequential data values, FAC Synthesis, and alignment pretraining treat data as an optimized control surface.
- FlowGuard, VISUALSWAP, and Activation Oracles inspect internal model processes rather than only outputs.
- DGS-Net and FlexRank both use decomposition to preserve useful pretrained structure under adaptation.

## Deep Theme Update

Batch 029 is about using internal structure to make scarce external signals go further: CLIP priors guide security fine-tuning, video representations amplify preference labels, fusion statistics expose multimodal attacks, dynamic programming clarifies data values, and SAE features guide synthetic data. The common pattern is representation-mediated control.
