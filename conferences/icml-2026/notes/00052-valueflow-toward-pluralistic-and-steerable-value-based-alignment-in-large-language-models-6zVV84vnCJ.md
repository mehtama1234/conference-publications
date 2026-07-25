# VALUEFLOW: Toward Pluralistic and Steerable Value-based Alignment in Large Language Models

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 6zVV84vnCJ
- Authors: Woojin Kim; Sieun Hyeon; Jusang Oh; Jaeyoung Do
- Primary area: social_aspects->alignment
- Keywords: Value Alignment;Human Value;Pluralism
- Source URL: https://openreview.net/forum?id=6zVV84vnCJ
- PDF URL: https://openreview.net/pdf?id=6zVV84vnCJ

## Abstract

Aligning Large Language Models (LLMs) with the diverse spectrum of human values remains a central challenge: preference-based methods often fail to capture deeper motivational principles. Value-based approaches offer a more principled path, yet three gaps persist: extraction often ignores hierarchical structure, evaluation detects presence but not calibrated intensity, and steerability of LLMs at controlled intensities remains insufficiently understood. To address these limitations, we introduce VALUEFLOW, a unified framework that spans extraction, evaluation, and steering with calibrated intensity control. The framework integrates three components: (i) HiVES, a hierarchical value embedding space that captures intra- and cross-theory value structure; (ii) the Value Intensity DataBase (VIDB), a large-scale resource of value-labeled texts with intensity estimates derived from ranking-based aggregation; and (iii) an anchor-based evaluator that produces consistent intensity scores for model outputs by ranking them against VIDB panels. Using VALUEFLOW, we conduct a comprehensive large-scale study across ten models and four value theories, identifying asymmetries in steerability and composition laws for multi-value control. This paper establishes a scalable infrastructure for evaluating and controlling value intensity, advancing pluralistic alignment of LLMs.

## One-Sentence Claim

VALUEFLOW builds infrastructure for pluralistic alignment by extracting, evaluating, and steering human values with calibrated intensity rather than binary value presence.

## Problem

Preference-based alignment often misses deeper motivational structure, while value-based methods still struggle with hierarchical extraction, calibrated intensity evaluation, and controlled value steering.

## Core Contribution

The paper introduces VALUEFLOW, combining HiVES, VIDB, and an anchor-based intensity evaluator to study value extraction, ranking-based evaluation, and steerable value control across models and value theories.

## Method

HiVES maps values into a hierarchical embedding space spanning intra- and cross-theory structure. VIDB provides value-labeled texts with intensity estimates from ranking aggregation. The evaluator scores outputs by ranking them against anchor panels, and steering conditions generation on value-intensity profiles.

## Experiments and Evidence

The abstract reports a large-scale study across ten models and four value theories, identifying asymmetries in steerability and composition laws for multi-value control.

## Full-Text Upgrade

The full text frames the core target as steerable pluralism: a model should respond to value profiles with controllable intensity, not merely point in a value direction. VALUEFLOW therefore treats extraction, steering, and evaluation as one pipeline: infer value profiles, steer generation with value-intensity pairs, then evaluate by ranking outputs against fixed VIDB anchors.

The measurement design is important. Rather than asking a judge for direct scalar intensity, VIDB is built from repeated rankings aggregated with a Plackett-Luce model, which the paper reports as more stable than rating-based evaluation. The framework defines cross-theory anchors, operational macro-values, and per-value bounded calibration. The steering study finds weak, moderate, and strong steerability regimes across models, and shows value-dependent asymmetries and interference in multi-value steering.

## Limits and Failure Modes

Limits to watch: value taxonomies and anchors encode design choices; ranking judges may carry model-specific biases; steerability does not guarantee normatively correct behavior; and multi-value composition may create conflicts that intensity scores alone cannot resolve.

## Deep Themes

- Alignment evaluation is moving from preferences to structured values.
- Value control requires calibrated intensity, not binary compliance.
- Pluralistic alignment needs infrastructure for extraction, steering, and measurement together.

## Subthemes

- Value-based alignment.
- Pluralism.
- Value intensity.
- Ranking-based evaluation.
- Anchor panels.
- Steerable generation.

## Connections to Other Papers

Connects to Pressure Reveals Character, ClinTutor-R1, and one-to-many alignment papers through richer alignment targets. It also links to Ranking Time Series through pairwise/ranking-based measurement under subjective criteria.

## Notes for Cross-Paper Synthesis

VALUEFLOW adds a measurement-infrastructure theme: alignment research increasingly needs calibrated tools for nuanced latent constructs, not only preference wins or safety pass/fail labels.
