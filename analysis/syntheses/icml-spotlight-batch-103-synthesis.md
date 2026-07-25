# ICML 2026 Spotlight Batch 103 Synthesis

## Papers

- How Many Different Outputs Can a Transformer Generate?
- Learning Structured Reasoning via Tractable Trajectory Control
- Adaptive Memory Retention in Dynamic Graphs
- Beyond Language Modeling: An Exploration of Multimodal Pretraining
- EgoTactile: Learning Grasp Pressure for Everyday Objects from Egocentric Video

## Source Depth

All five notes are abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Full-paper details should be verified when official or high-confidence arXiv PDFs are accessible.

## Shared Thesis

This batch studies how capability depends on the structure of what a model can access, explore, retain, scale, or infer. Transformers have bounded accessible output sets; reasoning policies need controlled exploration of rare trajectories; dynamic graph models need adaptive retention rather than unchecked memory; multimodal foundation models need scaling laws that respect modality asymmetry; and egocentric tactile models must infer hidden pressure fields from partial visual evidence.

The shared pattern is structured access to latent possibilities: accessible sequences, reasoning trajectories, graph histories, modality-specific capacity, and hidden physical contact.

## Subthemes

### Expressivity as accessibility

The transformer output-counting paper reframes generation capacity as the set of sequences reachable from prompts. Its result that accessible length grows linearly with prompt length, while accessibility decays exponentially past a threshold, gives a structural explanation for copying and cramming failures.

### Controlled reasoning exploration

Ctrl-R treats reasoning improvement as a trajectory-distribution problem. Rare useful reasoning patterns may not appear often enough under ordinary sampling, so targeted rollout control and importance sampling are used to discover and internalize them.

### Adaptive memory dynamics

LAMP decomposes dynamic graph memory into conservative flow and learned dissipation. This is a principled way to preserve long-range dependencies while preventing noise from accumulating across snapshots.

### Multimodal scaling asymmetry

Beyond Language Modeling shows that native multimodal pretraining is not language modeling with pixels attached. Vision and language complement each other, but vision is more data-hungry while language demands high capacity. MoE helps harmonize these mismatched scaling pressures.

### Visuo-haptic latent inference

EgoTactile turns egocentric video into full-hand pressure estimates. The important move is generative uncertainty over hidden physical contact: pressure is not fully visible, so the model must infer plausible tactile states under physical constraints.

## Cross-Batch Connections

Transformer accessibility connects to Rational Transductors, language-generation complexity barriers, reasoning dimensionality, and insertion-order generation papers. Together they show that sequence modeling limits are often structural rather than just data-bound.

Ctrl-R connects to H1, RAGEN-2, DAWN, and Obfuscation Atlas through RL-shaped reasoning trajectories. The difference is constructive: it aims to make useful reasoning processes discoverable rather than diagnose collapse or deception.

LAMP connects to temporal graph memory explanation, POPGym memory diagnostics, and path-dependent inference. The shared theme is selective memory: models need to retain decision-relevant history while dissipating contamination.

Beyond Language Modeling connects to SplAttN, DroneDINO, Mind-Omni, ScaleMoE, and EgoTactile. It provides a scaling-law backbone for the corpus's multimodal and embodied modeling themes.

EgoTactile connects to EcoVLA, CoEvol-NO, and physical-domain generative modeling: learned systems increasingly infer latent physical states from partial, embodied observations.

## Emerging Pattern

The deeper pattern is that scaling and reasoning are constrained by what the model's architecture and training process make reachable. Better models expand the right reachable set: output sequences, reasoning paths, remembered graph signals, modality-specialized capacity, or physically plausible hidden states.
