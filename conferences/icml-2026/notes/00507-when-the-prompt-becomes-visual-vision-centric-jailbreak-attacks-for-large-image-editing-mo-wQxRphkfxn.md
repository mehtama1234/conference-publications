# When the Prompt Becomes Visual: Vision-Centric Jailbreak Attacks for Large Image Editing Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: wQxRphkfxn
- Authors: Jiacheng Hou; Yining Sun; Ruochong Jin; Haochen Han; Fangming Liu; Wai Kin Victor Chan; Alex Jinpeng Wang
- Primary area: social_aspects->safety
- Keywords: Jailbreak Attack;Large Image Editing Model;Visual Prompt
- Source URL: https://openreview.net/forum?id=wQxRphkfxn
- PDF URL: https://openreview.net/pdf?id=wQxRphkfxn

## Abstract

Recent advances in large image editing models have shifted the paradigm from text-driven instructions to vision-prompt editing, where user intent is inferred directly from visual inputs such as marks, arrows, and visual–text prompts. While this paradigm greatly expands usability, it also introduces a critical and underexplored safety risk: the attack surface itself becomes visual. In this work, we propose Vision-Centric Jailbreak Attack (VJA), the first visual-to-visual jailbreak attack that conveys malicious instructions purely through visual inputs. To systematically study this emerging threat, we introduce IESBench, a safety-oriented benchmark for image editing models. Extensive experiments on IESBench demonstrate that VJA effectively compromises state-of-the-art commercial models, achieving attack success rates of up to 80.9% on Nano Banana Pro and 70.1% on GPT-Image-1.5. To mitigate this vulnerability, we propose a training-free defense based on introspective multimodal reasoning, which substantially improves the safety of poorly aligned models to a level comparable with commercial systems, without auxiliary guard models and with negligible computational overhead. Our findings expose new vulnerabilities, provide both a benchmark and practical defense to advance safe and trustworthy modern image editing systems.

## One-Sentence Claim

Large image editing models can be jailbroken through purely visual prompts, so safety evaluation must treat marks, arrows, and image-embedded instructions as attack channels.

## Problem

Image editing systems increasingly infer user intent from visual inputs rather than text alone. This improves usability but expands the attack surface: malicious instructions can be conveyed by the image itself.

Text-focused jailbreak defenses and safety benchmarks may miss this because the harmful instruction is encoded as visual structure, not as a natural-language prompt.

## Core Contribution

The paper introduces Vision-Centric Jailbreak Attack, described as the first visual-to-visual jailbreak attack for large image editing models. It also introduces IESBench, a safety benchmark for image editing systems, and proposes a training-free defense based on introspective multimodal reasoning.

The main contribution is to redefine prompt safety for image editing: the prompt can be visual, and the model's safety layer must reason over that visual intent.

## Method

VJA conveys malicious editing instructions through visual inputs such as marks, arrows, and visual-text prompts. IESBench systematizes evaluation of this attack surface across image editing models.

The defense uses introspective multimodal reasoning without auxiliary guard models. Based on the abstract, it appears to ask the model or system to reason about the visual instruction and its safety implications before editing.

## Experiments and Evidence

The abstract reports that VJA compromises state-of-the-art commercial systems, with attack success rates up to 80.9 percent on Nano Banana Pro and 70.1 percent on GPT-Image-1.5.

The proposed defense substantially improves poorly aligned models to a level comparable with commercial systems, without auxiliary guard models and with negligible computational overhead.

## Limits and Failure Modes

The abstract does not specify the categories of harmful edits, the benchmark size, the threat model, or whether the defense resists adaptive visual attacks.

Because this note is abstract-only, details still need checking: benchmark construction, model list, definition of attack success, human evaluation protocol, transferability, and whether introspective reasoning creates refusal overreach on benign edits.

## Deep Themes

- Visual prompts as instructions: intent can be encoded in pixels, layout, arrows, and marks.
- Multimodal safety gaps: text-only safety assumptions fail when the command channel moves into vision.
- Benchmarking emerging attack surfaces: new interfaces require new adversarial suites.
- Training-free safety control: reasoning-time defenses can sometimes patch alignment gaps without retraining.

## Subthemes

- Visual-to-visual jailbreaks.
- Image editing safety as instruction-following safety.
- Introspective multimodal reasoning.
- Commercial model vulnerability under interface shifts.

## Connections to Other Papers

This connects directly to SecFid and prompt-injection work: both show that the attack channel can be embedded in the content the model is supposed to process. It also links to MiniAppBench, PIPE, and Copyright-Bench because all evaluate safety in realistic task interfaces rather than isolated text prompts.

It belongs with multimodal robustness papers such as SplAttN and DroneDINO, but the failure mode is adversarial rather than representational.

## Notes for Cross-Paper Synthesis

The cross-paper point is that safety boundaries follow interface design. When the user interface becomes visual, the safety problem becomes visual too.
