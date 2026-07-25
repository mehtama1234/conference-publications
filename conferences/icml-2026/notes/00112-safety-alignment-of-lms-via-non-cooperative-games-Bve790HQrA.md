# Safety Alignment of LMs via Non-cooperative Games

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Bve790HQrA
- Authors: Anselm Paulus; Ilia Kulikov; Brandon Amos; Rémi Munos; Ivan Evtimov; Kamalika Chaudhuri; Arman Zharmagambetov
- Primary area: social_aspects->alignment
- Keywords: Alignment;Language Model Safety;Adversarial Training;Red Teaming;Preference Learning;RLHF;Multi-Agent Reinforcement Learning
- Source URL: https://openreview.net/forum?id=Bve790HQrA
- PDF URL: https://openreview.net/pdf?id=Bve790HQrA

## Abstract

Ensuring the safety of language models (LMs) while maintaining their usefulness remains a critical challenge in AI alignment. Current approaches rely on sequential adversarial training: generating adversarial prompts and fine-tuning LMs to defend against them. We introduce a different paradigm: framing safety alignment as a non-zero-sum game between an Attacker LM and a Defender LM trained jointly via online reinforcement learning. Each LM continuously adapts to the other's evolving strategies, driving iterative improvement. Our method uses a preference-based reward signal derived from pairwise comparisons instead of point-wise scores, providing more robust supervision and potentially reducing reward hacking. Our RL recipe, AdvGame, shifts the Pareto frontier of safety and utility, yielding a Defender LM that is simultaneously more helpful and more resilient to adversarial attacks. In addition, the resulting Attacker LM converges into a strong, general-purpose red-teaming agent that can be directly deployed to probe arbitrary target models. Code at github.com/facebookresearch/advgame.

## One-Sentence Claim

AdvGame frames LM safety alignment as a non-zero-sum game between jointly trained attacker and defender models, improving both utility and adversarial robustness.

## Problem

Sequential adversarial training separates red-team prompt generation from defensive fine-tuning, limiting adaptation to evolving attack and defense strategies.

## Core Contribution

The paper introduces non-cooperative game training for safety alignment, where Attacker and Defender LMs adapt online through reinforcement learning with preference-based rewards.

## Method

AdvGame trains attacker and defender jointly. The reward signal comes from pairwise preference comparisons rather than point scores, aiming to reduce reward hacking while shifting the safety-utility Pareto frontier.

## Experiments and Evidence

The abstract reports a Defender LM that is both more helpful and more resilient to adversarial attacks, plus an Attacker LM that becomes a strong general-purpose red-teaming agent.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: game formulation, reward model, attack taxonomy, stability of joint RL, and whether attacker release creates misuse risk.

## Deep Themes

- Safety alignment can be a co-evolutionary game rather than a sequential pipeline.
- Red-team agents are useful training opponents and deployment tools.
- Preference comparisons may stabilize adversarial safety training.

## Subthemes

- Non-cooperative games.
- LM safety.
- Red teaming.
- Adversarial training.
- Preference-based RL.
- Safety-utility frontier.

## Connections to Other Papers

Connects to ParetoPO, constrained Nash equilibria, Jailbreak Foundry, and debate-collapse work through game-theoretic and adversarial safety infrastructure.

## Notes for Cross-Paper Synthesis

AdvGame reinforces the adversarial-process theme: robust alignment may require continuously adapting attackers and defenders, not one-shot hardening.
