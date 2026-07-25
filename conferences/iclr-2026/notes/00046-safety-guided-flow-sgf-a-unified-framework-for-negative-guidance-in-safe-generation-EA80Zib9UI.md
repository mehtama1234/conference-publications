# SAFETY-GUIDED FLOW (SGF): A UNIFIED FRAMEWORK FOR NEGATIVE GUIDANCE IN SAFE GENERATION

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: EA80Zib9UI
- Authors: Mingyu Kim; Young-Heon Kim; Mijung Park
- Primary area: generative models
- Keywords: Safe generation;flow matching;control barrier functions
- Source URL: https://openreview.net/forum?id=EA80Zib9UI
- PDF URL: https://openreview.net/pdf?id=EA80Zib9UI

## Abstract

Safety mechanisms for diffusion and flow models have recently been developed along two distinct paths. 
In robot planning, control barrier functions are employed to guide generative trajectories away from obstacles at every denoising step by explicitly imposing geometric constraints. 
In parallel, recent data-driven, negative guidance approaches have been shown to suppress harmful content and promote diversity in generated samples. However, they rely on heuristics without clearly stating when safety guidance is actually necessary. 
In this paper, we first introduce a unified probabilistic framework using a Maximum Mean Discrepancy (MMD) potential for image generation tasks that recasts both Shielded Diffusion and Safe Denoiser as instances of our energy-based negative guidance against unsafe data samples. 
Furthermore, we leverage control-barrier functions analysis to justify the existence of a critical time window in which negative guidance must be strong; outside of this window, the guidance should decay to zero to ensure safe and high-quality generation. We evaluate our unified framework on several realistic safe generation scenarios, confirming that negative guidance should be applied in the early stages of the denoising process for successful safe generation.

## One-Sentence Claim

Safety-Guided Flow unifies negative guidance for safe diffusion/flow generation and shows safety guidance should be strongest in an early critical denoising window, then decay.

## Problem

Safety methods for diffusion and flow models have developed separately across robot planning and content generation. Control barrier functions impose geometric constraints during denoising, while data-driven negative guidance suppresses harmful content through heuristics.

The problem is that negative guidance lacks a unified probabilistic account and does not clearly specify when strong safety guidance is necessary.

## Core Contribution

The paper introduces a unified probabilistic framework using an MMD potential that recasts Shielded Diffusion and Safe Denoiser as energy-based negative guidance away from unsafe samples.

It also uses control barrier function analysis to justify a critical time window where negative guidance must be strong, outside of which it should decay to zero for quality.

## Method

SGF defines an energy-based negative guidance term using Maximum Mean Discrepancy against unsafe data. This creates a probabilistic view shared by image-generation safety methods.

The timing of guidance is analyzed with control-barrier-function reasoning, producing a schedule that applies strong guidance early in denoising and weakens later.

## Experiments and Evidence

The abstract reports evaluations on realistic safe-generation scenarios.

The main empirical finding is that applying negative guidance in early denoising stages is important for successful safe generation, supporting the critical-window analysis.

## Limits and Failure Modes

The framework depends on the unsafe-data representation and the MMD potential. If unsafe samples are incomplete or safety concepts are contextual, negative guidance may miss or overblock content.

Because this note is abstract-only, details still need checking: unsafe datasets, MMD kernel choice, guidance schedule, image metrics, robot-planning connection, and tradeoffs between safety and quality.

## Deep Themes

- Timing matters in generative safety: guidance should be scheduled, not applied uniformly.
- Negative guidance as energy shaping: unsafe regions can be repelled by a potential.
- Control theory meets diffusion safety: barrier analysis explains when constraints should act.
- Unified safety abstractions: planning obstacles and harmful image content can share a guidance lens.

## Subthemes

- MMD safety potential.
- Control barrier functions.
- Early denoising critical window.
- Safe diffusion and flow generation.

## Connections to Other Papers

This connects to DivIn, GoodDiffusion, RLR, DFM theory, and RealUID through diffusion/flow control.

It also relates to SecFid and visual jailbreak work because safety interventions must preserve quality and task intent while blocking harmful behavior.

## Notes for Cross-Paper Synthesis

SGF adds a temporal-control theme for generative safety: the same guidance strength can be helpful or harmful depending on where it acts in the generation process.
