# Hubble: a Model Suite to Advance the Study of LLM Memorization

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: ZfdnZhOP0k
- Authors: Johnny Wei; Ameya Godbole; Mohammad Aflah Khan; Ryan Yixiang Wang; Xiaoyuan Zhu; James Flemings; Nitya Kashyap; Krishna P. Gummadi; Willie Neiswanger; Robin Jia
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: memorization;copyright;privacy;test set contamination;membership inference;unlearning
- Source URL: https://openreview.net/forum?id=ZfdnZhOP0k
- PDF URL: https://openreview.net/pdf?id=ZfdnZhOP0k

## Abstract

We present Hubble, a suite of open-source large language models (LLMs) for the scientific study of LLM memorization. Hubble models come as minimal pairs: standard models are pretrained on a large English corpus, and perturbed models are trained in the same way but with controlled insertion of text (e.g., book passages, biographies, and test sets) designed to emulate key memorization risks. Our core release includes 8 models---standard and perturbed, with 1B or 8B parameters, trained on 100B or 500B tokens. Hubble's core experiment establishes that memorization risks are determined by the frequency of sensitive data relative to the training corpus size (i.e., a password appearing once in a smaller corpus is memorized better than the same password in a larger corpus).  Our release includes 6 more models with perturbations inserted at different pretraining phases; we observe perturbations without continued exposure can be forgotten. These findings suggest two best practices: to dilute sensitive data by increasing the training corpus size, and to order them to appear earlier in training. Beyond these general findings, Hubble enables a broad range of memorization research. We show that the randomized perturbations in Hubble make it an ideal testbed for membership inference and machine unlearning methods. We invite the community to explore, benchmark, and build upon our work.

## One-Sentence Claim

Hubble releases controlled standard/perturbed LLM model pairs to study memorization risks from inserted sensitive text, test contamination, membership inference, and unlearning.

## Problem

LLM memorization creates copyright, privacy, test contamination, and data-extraction risks, but studying it rigorously is difficult without controlled model families.

Researchers need models where sensitive content insertion is known and varied, so memorization, forgetting, membership inference, and unlearning methods can be evaluated against ground truth.

## Core Contribution

The paper introduces Hubble, an open-source suite of LLMs built as minimal pairs.

Standard models are pretrained normally, while perturbed models use the same setup with controlled insertions such as book passages, biographies, and test sets. The core release includes eight models varying perturbation, scale, and token budget, plus six more with perturbations inserted at different pretraining phases.

## Method

Hubble controls exposure frequency, training corpus size, model scale, token budget, and insertion timing.

By comparing standard and perturbed counterparts, researchers can isolate how sensitive content appears in model behavior and how memorization changes with dilution or later forgetting.

## Experiments and Evidence

The core experiment finds that memorization risk depends on sensitive-data frequency relative to corpus size: a password appearing once in a smaller corpus is memorized better than the same password in a larger corpus.

Perturbations inserted without continued exposure can be forgotten. The authors suggest diluting sensitive data by increasing corpus size and placing risky content earlier in training. They also show Hubble is useful for membership inference and unlearning evaluation.

## Limits and Failure Modes

Controlled perturbations may not cover all real memorization mechanisms, such as near-duplicates, structured secrets, or multimodal private data. Recommendations about inserting sensitive data earlier should be interpreted as risk mitigation in controlled training, not as a reason to include sensitive data.

Because this note is abstract-only, details still need checking: corpus composition, insertion protocol, memorization metrics, extraction attacks, unlearning baselines, and release safeguards.

## Deep Themes

- Controlled memorization testbeds: safety research needs model families with known data perturbations.
- Relative exposure frequency: memorization risk depends on data frequency normalized by corpus size.
- Training-time forgetting: lack of continued exposure can reduce memorization of inserted content.
- Provenance for unlearning and membership inference: ground-truth perturbations make evaluation sharper.

## Subthemes

- Minimal-pair LLMs.
- Controlled sensitive-data insertion.
- Membership inference.
- Machine unlearning.

## Connections to Other Papers

This connects to LLM DNA, Copyright-Bench, SafeDPO, deception measurement, and privacy/unlearning work.

It also relates to curriculum and data-ordering papers because training phase and exposure timing affect downstream behavior.

## Notes for Cross-Paper Synthesis

Hubble adds a controlled-provenance theme: memorization and unlearning cannot be evaluated well without model suites where training-data interventions are known.
