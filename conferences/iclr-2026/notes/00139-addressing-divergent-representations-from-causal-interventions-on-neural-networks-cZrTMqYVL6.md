# Addressing divergent representations from causal interventions on neural networks

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: cZrTMqYVL6
- Authors: Satchel Grant; Simon Jerome Han; Alexa R. Tartaglini; Christopher Potts
- Primary area: interpretability and explainable AI
- Keywords: activation patching;mech interp;DAS;representational divergence;faithfulness
- Source URL: https://openreview.net/forum?id=cZrTMqYVL6
- PDF URL: https://openreview.net/pdf?id=cZrTMqYVL6

## Abstract

A common approach to mechanistic interpretability is to causally manipulate model representations via targeted interventions in order to understand what those representations encode. Here we ask whether such interventions create out-of-distribution (divergent) representations, and whether this raises concerns about how faithful their resulting explanations are to the target model in its natural state. First, we demonstrate theoretically and empirically that common causal intervention techniques often do shift internal representations away from the natural distribution of the target model. Then, we provide a theoretical analysis of two cases of such divergences: "harmless" divergences that occur in the behavioral null-space of the layer(s) of interest, and "pernicious" divergences that activate hidden network pathways and cause dormant behavioral changes. Finally, in an effort to mitigate the pernicious cases, we apply and modify the Counterfactual Latent (CL) loss from Grant (2025) allowing representations from causal interventions to remain closer to the natural distribution, reducing the likelihood of harmful divergences while preserving the interpretive power of the interventions. Together, these results highlight a path towards more reliable interpretability methods.

## One-Sentence Claim

This paper shows causal interpretability interventions can create out-of-distribution internal representations and uses a modified Counterfactual Latent loss to keep interventions closer to natural model states.

## Problem

Mechanistic interpretability often manipulates internal representations to infer what they encode.

If those interventions push activations off the model's natural representation distribution, resulting behaviors may reflect artifacts rather than faithful explanations of the model's normal computation.

## Core Contribution

The paper theoretically and empirically demonstrates that common causal intervention techniques can create divergent representations.

It distinguishes harmless divergences in behavioral null spaces from pernicious divergences that activate hidden pathways and cause dormant behavioral changes, then modifies the Counterfactual Latent loss to mitigate pernicious cases.

## Method

The analysis studies representation shifts caused by causal interventions and classifies their behavioral consequences.

The modified CL loss constrains intervened representations to remain closer to the natural distribution while preserving enough intervention strength for interpretability.

## Experiments and Evidence

The abstract reports both theoretical and empirical evidence that common interventions shift representations away from natural states.

Applying the modified CL loss reduces harmful divergences while preserving interpretive power.

## Limits and Failure Modes

Staying close to the natural distribution may reduce intervention specificity, and defining naturalness in high-dimensional activations is difficult. Some faithful counterfactuals may necessarily be off-distribution.

Because this note is abstract-only, details still need checking: intervention types, divergence metric, model/task set, CL loss modification, and examples of harmless versus pernicious divergence.

## Deep Themes

- Intervention faithfulness: causal probes must avoid creating artificial model states.
- Behavioral null spaces: some activation changes are off-distribution but behaviorally harmless.
- Hidden pathway activation: pernicious interventions can reveal artifacts rather than causal features.
- Natural-distribution constraints for interpretability: reliable explanations require intervention regularization.

## Subthemes

- Activation patching.
- Causal interventions.
- Representation divergence.
- Counterfactual Latent loss.

## Connections to Other Papers

This connects to T-SAEs, DAVE, Neural Effect Search, and interpretability-as-intervention papers.

It also relates to robustness and OOD representation diagnostics because intervention validity depends on activation distribution shift.

## Notes for Cross-Paper Synthesis

This paper adds a methodological caution: interpretability interventions are themselves distribution shifts and need robustness controls.
