# Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: hvI3Syn2U7
- Authors: David Huang; Jaewon Chang; Avidan Shah; Prateek Mittal; Chawin Sitawarin
- Primary area: deep_learning->large_language_models
- Keywords: Data Poisoning;Backdoor Attacks;Safety Classifiers;Prompt Injection;Adversarial Training;Synthetic Data Generation
- Source URL: https://openreview.net/forum?id=hvI3Syn2U7
- PDF URL: https://openreview.net/pdf?id=hvI3Syn2U7

## Abstract

The Rapid Response (RR) framework (Peng et al., 2024), deployed in production systems including Anthropic’s ASL-3 safeguards (Anthropic, 2025), dynamically adapts jailbreak detection classifiers by generating synthetic training data from emerging attacks. We reveal that prompt injection can infiltrate this pipeline to deliver poisoned samples into the classifier’s training set, enabling two attack objectives: (I) targeted poisoning attacks that create false positives on harmless samples by categorizing them as a jailbreak, with a specific desired feature (e.g., certain formatting, subject, or keyword), (II) concept-based backdoor attacks that induce false negatives on jailbreak inputs, generalizing even to jailbreaks from attack strategies the defender explicitly trained against, when the backdoor trigger is present. Importantly, our threat model restricts adversaries to modify- ing only jailbreak samples (not benign data or labels), a constraint unexplored by prior work that makes the second objective particularly challeng- ing. We address this with Omission Attack, which exploits a new phenomenon: when training on concept-absent unsafe samples, the classifier mis- associates that concept’s presence with the safe label. Both attacks flip nearly all target labels with only 1% poisoning rate. Code: https://github.com/DH-davidhuang/rapid-poison

## One-Sentence Claim

Rapid Response safety classifiers can be poisoned through prompt-injected synthetic attack data, enabling targeted false positives and concept-triggered jailbreak false negatives at very low poisoning rates.

## Problem

Rapid Response frameworks adapt jailbreak detectors by generating synthetic training data from emerging attacks. This creates a moving safety pipeline, but the same adaptivity can become an attack surface if prompt injection influences the generated training samples.

The paper asks whether attackers can poison safety classifiers while modifying only jailbreak samples, not benign data or labels.

## Core Contribution

The paper demonstrates two practical poisoning objectives against Rapid Response pipelines: targeted attacks that make harmless samples with a chosen feature look like jailbreaks, and concept-based backdoors that make jailbreaks with a trigger appear benign.

It introduces Omission Attack, exploiting the phenomenon that training on unsafe samples where a concept is absent can make the classifier associate the concept's presence with safety. Both attacks flip nearly all target labels with only 1% poisoning.

## Method

The attack injects instructions or content into jailbreak samples that enter the synthetic data generation and classifier training loop. For concept backdoors, it carefully omits a trigger concept from unsafe samples so the model learns a spurious safe association when that concept appears.

This is notable because the adversary does not need to poison benign data or relabel examples.

## Experiments and Evidence

Evidence reported in the abstract:

- Practical attacks against Rapid Response framework.
- Targeted false-positive poisoning on harmless samples with chosen features.
- Concept-based backdoors causing false negatives on jailbreak inputs.
- Backdoors generalize to jailbreak strategies explicitly trained against.
- Threat model modifies only jailbreak samples.
- Omission Attack exploits concept-absent unsafe samples.
- Nearly all target labels flipped with 1% poisoning rate.
- Code release at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: classifier architectures, synthetic-data pipeline, trigger types, and defenses.

## Limits and Failure Modes

- Attack success may depend on the defender's synthetic data generation prompts and filtering.
- Production systems may include additional human review, deduplication, or anomaly detection.
- Backdoor triggers that are too obvious may be caught by data audits.
- The defense implications need full evaluation, not just attack demonstration.

## Deep Themes

**Adaptive safety pipelines are attack surfaces.** The mechanism that learns from new attacks can be manipulated by attackers.

**Synthetic data governance is safety-critical.** Generated training examples need provenance and adversarial filtering.

**Absence can poison as much as presence.** Omission Attack shows that what is systematically missing from unsafe data can induce dangerous associations.

## Subthemes

- Rapid Response poisoning.
- Prompt-injection into safety data.
- Concept backdoors.
- Omission Attack.
- Jailbreak classifier vulnerability.

## Connections to Other Papers

Connects to Copyright-Bench, Token Overcharging, Monitoring Monitorability, Weak-Strong Verification, and data-poisoning/privacy themes. It is a strong counterpoint to adaptive safety and feedback-loop papers: closed-loop improvement can be attacked.

## Notes for Cross-Paper Synthesis

Rapid Poison adds an adversarial-data-governance theme: any pipeline that automatically converts model failures or attacks into training data must defend the ingestion path.
