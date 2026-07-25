# RelaxFlow: Text-Driven Amodal 3D Generation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: UamxHbDR3p
- Authors: Jiayin Zhu; Guoji Fu; Xiaolu Liu; Qiyuan He; Yicong Li; Angela Yao
- Primary area: applications->computer_vision
- Keywords: Image-to-3D Generation;Amodal 3D Generation;Text-Guided 3D Generation
- Source URL: https://openreview.net/forum?id=UamxHbDR3p
- PDF URL: https://openreview.net/pdf?id=UamxHbDR3p

## Abstract

Image-to-3D generation faces inherent semantic ambiguity under occlusion, where partial observation alone is often insufficient to determine object category. 
In this work, we formalize *text-driven amodal 3D generation*, where text prompts steer the completion of unseen regions while strictly preserving input observation. Crucially, we identify that these objectives demand distinct control granularities: rigid control for the observation versus relaxed structural control for the prompt. To this end, we propose **RelaxFlow**, a training-free dual-branch framework that decouples control granularity via a Multi-Prior Consensus Module and a Relaxation Mechanism. Theoretically, we prove that our relaxation is equivalent to applying a low-pass filter on the generative vector field, which suppresses high-frequency instance details to isolate geometric structure that accommodates the observation. To facilitate evaluation, we introduce two diagnostic benchmarks, **ExtremeOcc-3D** and **AmbiSem-3D**. Extensive experiments demonstrate that RelaxFlow successfully steers the generation of unseen regions to match the prompt intent without compromising visual fidelity. Code and datasets will be released.

## One-Sentence Claim

RelaxFlow enables text-driven amodal 3D completion by rigidly preserving observed geometry while applying relaxed, low-pass prompt control to unseen structure.

## Problem

Image-to-3D generation is ambiguous under occlusion: the visible pixels may not determine the full object category or hidden geometry. Text prompts can resolve semantic ambiguity, but prompt control and observation preservation require different strengths of control.

The paper formalizes text-driven amodal 3D generation: use text to steer unseen regions while strictly preserving what the input image already reveals.

## Core Contribution

The paper introduces RelaxFlow, a training-free dual-branch framework that decouples control granularity. A Multi-Prior Consensus Module handles multiple priors, while a Relaxation Mechanism loosens prompt control so it shapes structure without overwriting observed details.

The theoretical claim is that relaxation is equivalent to applying a low-pass filter on the generative vector field, suppressing high-frequency instance detail while preserving geometric structure compatible with the observation.

## Method

RelaxFlow separates rigid observation control from relaxed text-prompt structural control. The observed image anchors visible geometry; text influences occluded or ambiguous regions through a lower-frequency structural channel.

Because the framework is training-free, it likely operates by modifying generation dynamics at inference time rather than retraining a 3D generator.

## Experiments and Evidence

Evidence reported in the abstract:

- Formalization of text-driven amodal 3D generation.
- Theoretical analysis connecting relaxation to low-pass filtering of the generative vector field.
- Two diagnostic benchmarks: ExtremeOcc-3D and AmbiSem-3D.
- Experiments showing unseen regions follow prompt intent without compromising visual fidelity.
- Planned code and dataset release.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: base generator, control equations, benchmark construction, observation-preservation metrics, and failure cases under conflicting prompts.

## Limits and Failure Modes

- Training-free control depends on the capabilities and biases of the underlying generator.
- Low-pass prompt control may fail when unseen details require fine-grained semantics.
- Ambiguous prompts or prompts inconsistent with observations may produce unstable completions.
- Evaluation of amodal 3D completion is difficult because hidden regions lack unique ground truth.

## Deep Themes

**Different evidence sources need different control bandwidths.** Observations require rigid high-fidelity control; prompts require relaxed structural guidance.

**Amodal generation is structured uncertainty resolution.** Text does not simply decorate an object; it selects among plausible hidden 3D completions.

**Training-free generation control is becoming more analytical.** The low-pass vector-field interpretation gives a mechanism-level account of prompt relaxation.

## Subthemes

- Text-driven amodal 3D generation.
- Observation-preserving generation.
- Multi-prior consensus.
- Low-pass generative vector-field relaxation.
- Diagnostic benchmarks for occlusion ambiguity.

## Connections to Other Papers

Connects to Holi-Spatial and AdLift through 3DGS/spatial generation, to DLMR and multimodal reasoning through observation-text integration, and to Flowers through vector-field/operator interpretations of learned transformations.

## Notes for Cross-Paper Synthesis

RelaxFlow contributes to a broader control-granularity theme: strong constraints should bind verified observations, while weaker priors should guide ambiguous regions without overpowering evidence.
