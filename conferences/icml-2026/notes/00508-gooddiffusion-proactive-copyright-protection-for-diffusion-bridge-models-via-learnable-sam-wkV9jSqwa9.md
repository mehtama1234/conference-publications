# GoodDiffusion: Proactive Copyright Protection for Diffusion Bridge Models via Learnable Sample-specific Signatures

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: wkV9jSqwa9
- Authors: Shixi Qin; Zhiyong Yang; Shilong Bao; Zitai Wang; Qianqian Xu; Qingming Huang
- Primary area: social_aspects->security
- Keywords: diffusion bridge;copyright protection
- Source URL: https://openreview.net/forum?id=wkV9jSqwa9
- PDF URL: https://openreview.net/pdf?id=wkV9jSqwa9

## Abstract

This paper tackles the challenging problem of developing a proactive copyright protection mechanism that cuts off unauthorized use of diffusion bridge models. Existing studies largely fall into post-hoc attribution (e.g., watermarking and fingerprinting) or degradation-only defenses, which offer only indirect and limited preventive effect. We therefore propose GoodDiffusion, inspired by backdoor mechanisms, to enforce model-level use-time control by internalizing authorization into the generative process through a selectively permissive, otherwise closed behavior. Specifically, GoodDiffusion preserves high-quality generation for authorized queries carrying valid signatures, yet refuses to generate for unauthorized inputs. We further empirically show that naive static-signature designs (like conventional backdoor injection) are fundamentally fragile, since a surrogate signature can be efficiently recovered via gradient-based optimization. To strengthen security, we introduce a Learnable Signature Network (LSN) that assigns sample-specific signatures conditioned on each input. This breaks the universality of signatures and prevents a surrogate from transferring across inputs.
Extensive experiments validate that GoodDiffusion effectively blocks unauthorized use while maintaining strong generation quality for authorized users.

## One-Sentence Claim

GoodDiffusion protects diffusion bridge models by making high-quality generation conditional on valid sample-specific signatures and refusing unauthorized unsigned inputs.

## Problem

Most copyright protection for generative models is post-hoc: watermarking, fingerprinting, or attribution can identify misuse after generation, but does not prevent unauthorized use at inference time.

Degradation-only defenses are also limited because they may reduce utility or provide indirect control. The paper targets model-level use-time authorization.

## Core Contribution

The paper proposes GoodDiffusion, a proactive copyright protection mechanism inspired by backdoors but designed for selective permission. Authorized queries with valid signatures generate normally; unauthorized inputs are blocked or refused.

The key technical contribution is a Learnable Signature Network that assigns sample-specific signatures conditioned on each input, avoiding the fragility of static universal signatures.

## Method

GoodDiffusion internalizes authorization into the diffusion bridge generative process. The model is trained or adapted so that valid signatures unlock normal generation while missing or invalid signatures trigger closed behavior.

The paper argues that static signatures are vulnerable because attackers can recover surrogate signatures by gradient optimization. The Learnable Signature Network makes signatures input-conditioned, preventing a recovered signature from transferring across samples.

## Experiments and Evidence

The abstract says experiments validate that GoodDiffusion blocks unauthorized use while maintaining strong generation quality for authorized users.

It also reports an empirical attack on naive static signatures: surrogate signatures can be efficiently recovered through gradient-based optimization, motivating sample-specific signatures.

## Limits and Failure Modes

The approach depends on the security of the signature generator and on attackers not being able to infer or approximate sample-specific signatures at scale. It may also introduce operational complexity around key/signature distribution.

Because this note is abstract-only, details still need checking: exact diffusion bridge setting, threat model, signature dimensionality, white-box versus black-box attacks, effects on image quality/diversity, and robustness to finetuning or model extraction.

## Deep Themes

- Proactive model authorization: protection shifts from detection after misuse to use-time access control.
- Backdoors as governance mechanisms: a normally harmful mechanism is repurposed for selective permission.
- Static secrets are brittle: universal triggers can be optimized or transferred.
- Sample-specific control: per-input signatures make authorization non-universal and harder to reuse.

## Subthemes

- Copyright protection for diffusion models.
- Learnable signature networks.
- Refusal behavior inside generative dynamics.
- Gradient-based trigger recovery as an attack on static defenses.

## Connections to Other Papers

This connects to Spherical Watermark and Copyright-Bench through generative-model copyright governance, but it differs by trying to prevent unauthorized generation rather than only attribute or evaluate it.

It also relates to prompt-injection and visual jailbreak work because all involve access-control boundaries inside generative systems. The difference is that GoodDiffusion makes the boundary cryptographic or signature-like rather than policy-like.

## Notes for Cross-Paper Synthesis

This paper adds an authorization theme to the safety corpus: robust generative systems may need to distinguish not only safe versus unsafe content, but authorized versus unauthorized use.
