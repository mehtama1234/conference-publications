# Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: jY7fAo9rfK
- Authors: Bartłomiej Marek; Lorenzo Rossi; Vincent Hanke; Xun Wang; Michael Backes; Franziska Boenisch; Adam Dziedzic
- Primary area: datasets and benchmarks
- Keywords: privacy;llm;adaptations;auditing;differential privacy
- Source URL: https://openreview.net/forum?id=jY7fAo9rfK
- PDF URL: https://openreview.net/pdf?id=jY7fAo9rfK

## Abstract

Recent work has applied differential privacy (DP) to adapt large language models (LLMs) for sensitive applications, offering theoretical guarantees. However, its practical effectiveness remains unclear, partly due to LLM pretraining, where overlaps and interdependencies with adaptation data can undermine privacy despite DP efforts. To analyze this issue in practice, we investigate privacy risks under DP adaptations in LLMs using state-of-the-art attacks such as robust membership inference and canary data extraction. We benchmark these risks by systematically varying the adaptation data distribution, from exact overlaps with pretraining data, through in-distribution (IID) cases, to entirely out-of-distribution (OOD) examples. Additionally, we evaluate how different adaptation methods and different privacy regimes impact the vulnerability. Our results show that distribution shifts strongly influence privacy vulnerability: the closer the adaptation data is to the pretraining distribution, the higher the practical privacy risk at the same theoretical guarantee, even without direct data overlap. We find that parameter-efficient fine-tuning methods, such as LoRA, achieve the highest empirical privacy protection for OOD data. Our benchmark identifies key factors for achieving practical privacy in DP LLM adaptation, providing actionable insights for deploying customized models in sensitive settings. Looking forward, we propose a structured framework for holistic privacy assessment beyond adaptation privacy, to identify and evaluate risks across the full pretrain-adapt pipeline of LLMs.

## One-Sentence Claim

DP adaptation privacy for LLMs depends strongly on the adaptation data's relationship to pretraining data, so empirical auditing must vary distribution overlap rather than relying only on nominal DP guarantees.

## Problem

Differential privacy gives formal guarantees for adaptation, but LLM pretraining muddies the practical risk picture: adaptation examples may overlap with, resemble, or depend on pretraining examples in ways that make membership inference and extraction easier than the DP setting alone suggests. Deployers need to know when DP fine-tuning is actually protective for customized models in sensitive domains.

## Core Contribution

The paper contributes a benchmark for empirical privacy protection in adapted LLMs, systematically varying adaptation data from exact pretraining overlaps to IID examples to OOD examples. It evaluates robust membership inference and canary extraction across adaptation methods and privacy regimes, then proposes a broader pretrain-adapt privacy assessment framework.

## Method

The benchmark controls the adaptation-data distribution relative to the model's pretraining distribution and runs state-of-the-art privacy attacks after DP and non-DP adaptation. It compares adaptation mechanisms, including parameter-efficient methods such as LoRA, and measures how theoretical privacy regimes translate into observed vulnerability under different distribution shifts.

## Experiments and Evidence

The abstract reports that closer proximity between adaptation and pretraining distributions increases practical privacy risk at the same theoretical guarantee, even without exact data overlap. It also reports that LoRA gives the strongest empirical privacy protection for OOD data among the studied adaptation methods.

## Limits and Failure Modes

The exact risk conclusions may depend on the base models, pretraining-data knowledge, canary design, attack calibration, and distribution-shift construction. The benchmark targets empirical attack success, so a low observed attack rate is not itself a formal privacy proof. Full-text review should check which DP mechanisms, privacy budgets, adaptation datasets, and attacks are included.

## Deep Themes

- Practical privacy depends on the full data lifecycle.
- Distribution shift changes the empirical meaning of formal privacy guarantees.
- Adaptation mechanisms are privacy interventions, not only efficiency choices.
- Benchmarks increasingly audit deployed-risk surfaces rather than isolated algorithms.

## Subthemes

- Robust membership inference after DP adaptation.
- Canary extraction in adapted LLMs.
- Pretraining-adaptation overlap as a privacy factor.
- LoRA and parameter-efficient tuning as empirical privacy modifiers.
- Holistic privacy assessment across pretraining and adaptation.

## Connections to Other Papers

Connects to CounselBench and other safety benchmarks through domain-sensitive deployment risk, to unlearning and watermarking papers through privacy/security guarantees under real attacks, and to data-governance papers such as Common Corpus through the importance of pretraining provenance.

## Notes for Cross-Paper Synthesis

This paper sharpens a recurring theme: formal guarantees are incomplete without workload-aware empirical auditing. The relevant privacy unit is not just the adaptation example but its relationship to the pretraining corpus and the adaptation mechanism.
