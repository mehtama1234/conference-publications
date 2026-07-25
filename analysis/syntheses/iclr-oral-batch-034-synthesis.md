# ICLR Oral Batch 034 Synthesis

## Papers Covered

- Planner Aware Path Learning in Diffusion Language Models Training
- Radiometrically Consistent Gaussian Surfels for Inverse Rendering
- Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling
- Online Learning and Equilibrium Computation with Ranking Feedback
- Premise Selection for a Lean Hammer

## Shared Thesis

This batch is about aligning learning signals with the process that will actually be used. PAPL changes diffusion language model training to match planner-based inference. RadioGS constrains learned radiance using physically based rendering from unobserved views. LPWM learns object-centric particles because decision-making needs structured scene state. Ranking-feedback theory asks what can be learned when the real feedback channel is ordinal rather than numeric. LeanHammer trains premise retrieval for the end-to-end hammer workflow rather than as an isolated search task. The shared pattern is process-aware training.

## Deep Themes

### Training Must Match Inference Procedure

PAPL is the clearest statement of this theme: a denoiser trained under uniform random paths is mismatched when inference uses a non-uniform planner. The planned ELBO turns the inference planner into part of the training objective. This echoes broader 2026 work where decoding, search, retrieval, and memory policies become training targets.

### Physical and Object Structure as Supervision

RadioGS and LPWM both improve visual/world modeling by injecting structure beyond pixel reconstruction. RadioGS uses radiometric consistency to supervise unobserved-view radiance; LPWM discovers object-centric particles, masks, boxes, and keypoints from video. Both papers treat latent structure as necessary for generalization to unobserved or future states.

### Weak Feedback Has Sharp Limits

The ranking-feedback paper formalizes what can and cannot be learned from ordinal feedback. It shows impossibility for some ranking models and positive regret guarantees under variation or full-information assumptions. This is useful for alignment and human-feedback work because it clarifies when preference-style signals contain enough information.

### Workflow-Level Neural-Symbolic Systems

LeanHammer is not only a neural premise selector. It integrates retrieval, translation to external theorem provers, and proof reconstruction for Lean. Its dynamic adaptation to user-local contexts emphasizes that formal reasoning tools must work in evolving project environments, not fixed benchmark snapshots.

## Cross-Paper Pattern

The common pattern is correcting a mismatch between signal and use. PAPL corrects training paths to match planned decoding. RadioGS corrects radiance estimates with physics from unobserved views. LPWM corrects video prediction with object-level latent state. Ranking-feedback learning corrects numeric-utility assumptions for ordinal human feedback. LeanHammer corrects standalone premise retrieval by training and evaluating inside the hammer workflow. Each paper asks what signal the deployed system actually receives and adjusts the method around that signal.

## Subthemes to Track

- Planner-aware DLM training.
- Radiometric consistency for inverse rendering.
- Object-centric latent particle world models.
- Online learning with ranking feedback.
- Lean premise selection and hammer integration.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
