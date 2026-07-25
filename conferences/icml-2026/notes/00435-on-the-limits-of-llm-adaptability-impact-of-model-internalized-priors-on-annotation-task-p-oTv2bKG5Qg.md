# On the Limits of LLM Adaptability: Impact of Model-Internalized Priors on Annotation Task Performance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: oTv2bKG5Qg
- Authors: Etienne Casanova; Rafal Kocielnik; R. Michael Alvarez
- Primary area: deep_learning->large_language_models
- Keywords: Large Language Models;Pre-training Bias;Zero-Shot Learning;Prompt Steerability;Annotation Reliability;Model Controllability
- Source URL: https://openreview.net/forum?id=oTv2bKG5Qg
- PDF URL: https://openreview.net/pdf?id=oTv2bKG5Qg

## Abstract

Large Language Models (LLMs) are increasingly used for zero-shot annotation and LLM-as-a-judge tasks, yet their reliability hinges on how model-internalized priors interact with user-provided instructions. We investigate three dimensions of this interaction: (1) how an LLM's familiarity with data and task definitions affects performance, (2) the extent to which additional information in prompts can correct zero-shot errors (``decision stickiness''), and (3) model susceptibility to misaligned task definitions. Through experiments on toxicity detection across diverse datasets (spanning social media, gaming, news, and forums) using both dense and mixture-of-experts models, we find that nearly two-thirds of zero-shot errors are resistant to correction, with an overall rescue rate (fraction of initial errors corrected by prompting) of only 34.8\%. High-confidence errors prove especially resistant to correction. When given misaligned definitions, LLMs follow them while maintaining confidence levels unchanged from the aligned condition. Crucially, we introduce Definition-Specific Familiarity (DSF), which measures alignment between a model's internal concept and the task definition. After controlling for dataset-level confounds, DSF shows a positive association with model performance (partial $r=+0.41$), while three distinct memorization metrics (ROUGE-L, BERTScore, and embedding cosine similarity) all fail to show a positive association. These findings show the limitations of prompt-based correction in annotation tasks, highlighting the importance of definition alignment over text-level memorization.

## One-Sentence Claim

LLMs used for zero-shot annotation are strongly constrained by internalized task priors: many errors resist prompt correction, and definition alignment predicts performance better than text memorization.

## Problem

LLMs are increasingly used as annotators and judges, but their reliability depends on whether they can follow the user's task definition instead of defaulting to internalized concepts learned during pretraining. Prompting is often assumed to correct mistakes, yet some errors may be sticky because the model is confident in its prior interpretation.

The paper studies this in toxicity detection across domains, where task definitions vary and familiar surface text does not necessarily imply correct annotation behavior.

## Core Contribution

The paper contributes an empirical analysis of model-internalized priors, decision stickiness, and susceptibility to misaligned definitions in LLM annotation. It introduces Definition-Specific Familiarity, a measure of alignment between the model's internal concept and the task definition.

The central finding is that prompt-based correction is limited: nearly two-thirds of zero-shot errors resist correction, high-confidence errors are especially sticky, and models follow misaligned definitions while keeping confidence levels similar to aligned settings.

## Method

The experiments examine toxicity detection across social media, gaming, news, and forum datasets using dense and mixture-of-experts models. The study tests how familiarity with data/task definitions affects performance, how much extra prompt information rescues errors, and how models respond to intentionally misaligned definitions.

Definition-Specific Familiarity is compared against memorization proxies including ROUGE-L, BERTScore, and embedding cosine similarity. This separates conceptual alignment with the task definition from simple text-level exposure.

## Experiments and Evidence

The abstract reports a rescue rate of only 34.8 percent for initially wrong zero-shot annotations, meaning most errors survive additional prompting. It also reports that high-confidence errors are particularly resistant to correction.

DSF has a positive association with performance after controlling for dataset-level confounds, with partial r = +0.41, while the three memorization metrics fail to show a positive association. This supports the claim that task-definition alignment matters more than textual memorization for annotation reliability.

## Limits and Failure Modes

The scope is toxicity detection, so results may differ for annotation tasks with less subjective definitions or clearer ground truth. Prompt-correction results also depend on prompt design, model family, calibration, and the type of additional information supplied.

The finding that models follow misaligned definitions with unchanged confidence is particularly concerning for LLM-as-judge use: confidence may not reliably indicate whether the model is applying the intended rubric.

## Deep Themes

- Internal priors as controllability limits: prompting cannot always override the model's learned concept.
- Definition alignment over memorization: knowing the text is not the same as sharing the task semantics.
- Annotation reliability as model governance: LLM labels must be audited for rubric fidelity, not just agreement.
- Confidence stickiness: high-confidence model errors can be harder to rescue than uncertain ones.

## Subthemes

- Zero-shot annotation has hidden failure modes when task definitions are socially contested.
- Mixture-of-experts and dense models both need definition-alignment analysis.
- Misaligned instructions can be followed confidently, creating false assurance.
- Rescue rate is a useful diagnostic for prompt steerability.

## Connections to Other Papers

This paper connects to ADEPT through ambiguity and evidence in human-centered labels. ADEPT tries to preserve minority emotion evidence; this paper shows that LLM annotators may impose internal definitions even when prompted otherwise.

It also relates to BLL-Loss, DPO/RLHF theory, and post-training support-barrier work: alignment depends on what the base model already represents and how correctable its mistakes are. For evaluation, it connects to MAP and Copyright-Bench-style concerns about LLM judges in practical workflows.

## Notes for Cross-Paper Synthesis

The main synthesis point is that promptability is not equivalent to controllability. Across papers, robust alignment increasingly requires measuring whether models use the intended evidence, definition, or process, not merely whether they accept a prompt string.
