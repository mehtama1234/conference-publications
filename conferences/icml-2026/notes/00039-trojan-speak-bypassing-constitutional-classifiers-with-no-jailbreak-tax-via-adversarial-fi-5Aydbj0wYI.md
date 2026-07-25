# Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 5Aydbj0wYI
- Authors: Bilgehan Sel; Xuanli He; Alwin Peng; Ming Jin; Jerry Wei
- Primary area: deep_learning->large_language_models
- Keywords: large language models;jail-breaking;adversarial fine-tuning;safety classifiers;reinforcement learning
- Source URL: https://openreview.net/forum?id=5Aydbj0wYI
- PDF URL: https://openreview.net/pdf?id=5Aydbj0wYI

## Abstract

Fine-tuning APIs offered by major AI providers create new attack surfaces where adversaries can bypass safety measures through targeted fine-tuning. We introduce **Trojan-Speak**, an adversarial fine-tuning method that bypasses Anthropic's Constitutional Classifiers. Our approach uses curriculum learning combined with GRPO-based hybrid reinforcement learning to teach models a communication protocol that evades LLM-based content classification. Crucially, while prior adversarial fine-tuning approaches report more than 25\% capability degradation on reasoning benchmarks, Trojan-Speak incurs less than 5\% degradation while achieving 99+\% classifier evasion for models with 14B+ parameters. We demonstrate that fine-tuned models can provide detailed responses to expert-level CBRN (Chemical, Biological, Radiological, and Nuclear) queries from Anthropic's Constitutional Classifiers bug-bounty program. Our findings reveal that LLM-based content classifiers alone are insufficient for preventing dangerous information disclosure when adversaries have fine-tuning access, and we show that activation-level probes can substantially improve robustness to such attacks.

## One-Sentence Claim

Trojan-Speak shows that adversarial fine-tuning can train models to evade LLM-based content classifiers while preserving most general capability, exposing a fine-tuning-access safety gap.

## Problem

Content classifiers can monitor prompts, outputs, and fine-tuning data, but adversaries with fine-tuning access may teach models alternate harmful communication protocols that bypass classifier detection without paying a large capability-degradation cost.

## Core Contribution

The paper introduces Trojan-Speak, an adversarial fine-tuning evaluation showing high evasion of Anthropic Constitutional Classifiers with limited reasoning-benchmark degradation, and studies activation-level probes as a stronger defense.

## Method

At a high level, the attack uses staged curriculum learning and hybrid RL/SFT training to preserve task capability while shifting how harmful content is represented. The defense analysis trains activation-level linear probes to detect harmful intent/content in model states.

## Experiments and Evidence

The abstract reports 99+% classifier evasion for models with 14B+ parameters, less than 5% capability degradation, and detailed responses to expert-level CBRN queries from a Constitutional Classifiers bug-bounty benchmark.

## Full-Text Upgrade

The full text compares Trojan-Speak with earlier adversarial fine-tuning work that incurred a large "jailbreak tax" on reasoning benchmarks. The reported Qwen3 14B results retain roughly 89-93% of performance across GPQA Diamond, MMLU-Pro, and MATH-500 after fine-tuning, while achieving high classifier bypass rates on harmful CBRN benchmark queries.

The defense result is important: activation probes trained on model internals reach high AUC after the model learns the adversarial protocol, suggesting that representation-level monitoring can expose harmful computation even when surface text classifiers fail. The authors still frame probe robustness as open, especially under adaptive adversaries.

## Limits and Failure Modes

Limits to watch: results are tied to specific model families, classifier setups, and benchmarked harmful-query distributions; activation-probe defenses need adaptive robustness testing; and the paper's scenario assumes adversarial fine-tuning access, which may vary by deployment policy.

## Deep Themes

- Fine-tuning APIs create safety attack surfaces that inference-time classifiers alone cannot close.
- Surface-text monitoring can fail when harmful computation is hidden in learned internal protocols.
- Activation-level defenses may be necessary for adversarially fine-tuned models.

## Subthemes

- Adversarial fine-tuning.
- Constitutional classifiers.
- Classifier evasion.
- Capability retention.
- CBRN safety.
- Activation probes.

## Connections to Other Papers

Connects to Invisible Safety Threat, Rare Event Analysis, Pressure Reveals Character, and SandboxEscapeBench as safety work focused on hidden or capability-dependent failures. It also connects to Base Models Know How to Reason through internal-state analysis.

## Notes for Cross-Paper Synthesis

Trojan-Speak strengthens the hidden-channel safety theme: as models become adaptable, the safety boundary shifts from prompt/output filtering toward monitoring training access and internal representations.
