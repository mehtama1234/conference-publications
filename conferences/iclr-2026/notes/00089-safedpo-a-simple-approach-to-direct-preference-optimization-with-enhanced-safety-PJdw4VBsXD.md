# SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: PJdw4VBsXD
- Authors: Geon-Hyeong Kim; Yu Jin Kim; Byoungjip Kim; Honglak Lee; Kyunghoon Bae; Youngsoo Jang; Moontae Lee
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Safety Alignment;LLM Fine-tuning;Preferences;Large Language Models;AI Safety
- Source URL: https://openreview.net/forum?id=PJdw4VBsXD
- PDF URL: https://openreview.net/pdf?id=PJdw4VBsXD

## Abstract

As Large Language Models (LLMs) are increasingly deployed in real-world applications, balancing both helpfulness and safety has become a central challenge. A natural approach is to incorporate safety constraints into Reinforcement Learning from Human Feedback (RLHF), where recent studies have shown promising progress. However, these methods often rely on auxiliary networks or multi-stage pipelines, thereby increasing complexity. In this work, we revisit the safety alignment objective itself and demonstrate that it admits a closed-form solution, yielding a theoretically grounded and provably equivalent reformulation that enables a direct and tractable optimization procedure. Building on this insight, we propose SafeDPO, a lightweight method derived from this formulation, which preserves the optimality of the underlying safety-constrained objective while requiring only one additional hyperparameter and minimal modifications to existing preference-based training methods. At the same time, it eliminates the need for reward models, cost models, and online sampling. Despite its simplicity, SafeDPO achieves comparable or superior results to state-of-the-art safety alignment methods in both theoretical soundness and empirical performance. Experiments on the PKU-SafeRLHF-30K benchmark show that SafeDPO consistently improves safety while maintaining competitive helpfulness. Ablation studies further show that the additional hyperparameter provides a flexible mechanism to enhance safety without altering the theoretical optimum, and confirm that SafeDPO scales reliably to LLMs with up to 13B parameters. Overall, our results highlight that a simple, theory-driven objective can provide a lightweight yet effective solution for safety alignment in practice.

## One-Sentence Claim

SafeDPO derives a direct preference-optimization method from a closed-form safety-constrained objective, improving safety with minimal changes and no reward or cost models.

## Problem

LLM deployment requires balancing helpfulness and safety. RLHF-style safety constraints can help, but many approaches add auxiliary networks, reward models, cost models, online sampling, or multi-stage pipelines.

This complexity makes safety alignment harder to reproduce, tune, and scale.

## Core Contribution

The paper revisits the safety alignment objective and shows that it admits a closed-form solution with a provably equivalent direct optimization reformulation.

SafeDPO is the resulting lightweight method: it modifies preference-based training with one additional hyperparameter while preserving the theoretical optimum of the safety-constrained objective.

## Method

SafeDPO incorporates safety into a DPO-style preference objective directly, eliminating separate reward and cost modeling.

The additional hyperparameter controls the safety emphasis while keeping the optimization tractable and close to existing preference-training workflows.

## Experiments and Evidence

The abstract reports experiments on PKU-SafeRLHF-30K.

SafeDPO consistently improves safety while maintaining competitive helpfulness, compares favorably to state-of-the-art safety alignment methods, and scales to LLMs up to 13B parameters. Ablations show the added hyperparameter flexibly adjusts safety.

## Limits and Failure Modes

Safety-helpfulness tradeoffs may vary across domains and policy categories. A single hyperparameter may not capture heterogeneous safety constraints, and benchmark improvements may not imply robustness to jailbreaks or long-horizon agent misuse.

Because this note is abstract-only, details still need checking: closed-form derivation, preference data format, safety labels, baseline methods, hyperparameter behavior, and out-of-distribution safety tests.

## Deep Themes

- Simpler alignment objectives: theory can remove auxiliary machinery from safety training.
- Direct safety preference optimization: safety constraints are folded into preference learning rather than separate reward pipelines.
- Tunable safety without online RL: practical alignment favors methods that scale through existing fine-tuning infrastructure.
- Helpfulness-safety frontier: the key empirical claim is safety gain without major helpfulness loss.

## Subthemes

- Safety alignment.
- Direct preference optimization.
- Closed-form constrained objective.
- PKU-SafeRLHF-30K.

## Connections to Other Papers

This connects to deception measurement, DPO/RLHF equivalence work, conditional DPO, and Safe alignment papers.

It also relates to LongWriter-Zero and AgentFlow because all use objective design to shape model behavior without relying solely on prompting.

## Notes for Cross-Paper Synthesis

SafeDPO reinforces a 2026 alignment pattern: simple objective reformulations can compete with more complex RLHF pipelines when the constraint is formulated carefully.
