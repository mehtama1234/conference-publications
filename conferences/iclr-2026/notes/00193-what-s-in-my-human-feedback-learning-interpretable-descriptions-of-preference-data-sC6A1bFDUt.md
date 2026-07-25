# What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: sC6A1bFDUt
- Authors: Rajiv Movva; Smitha Milli; Sewon Min; Emma Pierson
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: rlhf;explaining datasets;interpretability;reward modeling;personalization
- Source URL: https://openreview.net/forum?id=sC6A1bFDUt
- PDF URL: https://openreview.net/pdf?id=sC6A1bFDUt

## Abstract

Preference data is widely used for aligning language models, but remains largely opaque. While prior work has studied specific aspects of annotator preference (e.g., length or sycophancy), automatically inferring preferences without pre-specifying hypotheses remains challenging. We introduce *What's In My Human Feedback* (WIMHF), a method that produces human-interpretable, natural language features from preference data using sparse autoencoders. We show that a sparse set of interpretable features can account for two-thirds of the preference signal achieved by black-box models. Applying WIMHF to 7 widely-used datasets, we precisely characterize both (1) which preferences are even possible to measure from each dataset and (2) which preferences humans actually display. WIMHF surfaces preferences that are unintentional or even actively harmful, like a preference for toxic outputs in Chatbot Arena. We show how these findings enable *interpretable data curation*: re-labeling the examples that contain the harmful preference yields large safety gains (+37%) with no cost to general performance. We also demonstrate a new approach to *personalization*: on the Community Alignment dataset, we identify preferences that are subjective across annotators, and use the features as interpretable knobs to adjust model behavior along these axes.

## One-Sentence Claim

WIMHF uses sparse autoencoders to extract interpretable natural-language features from preference datasets, enabling diagnosis, curation, and personalization of human feedback.

## Problem

Preference datasets drive alignment but are often opaque. Existing analyses usually test predefined hypotheses such as length or sycophancy, missing unknown preferences, harmful artifacts, and subjective dimensions across annotators.

## Core Contribution

The paper introduces What's In My Human Feedback, a method for learning sparse interpretable preference features from data. It characterizes measurable and displayed preferences across seven datasets, surfaces harmful preferences, and uses the features for data curation and personalization.

## Method

WIMHF trains sparse autoencoder-style representations over preference model signals or preference data, then maps sparse features into natural-language descriptions. The resulting feature set explains much of the black-box preference signal and can identify examples associated with harmful or subjective preference dimensions.

## Experiments and Evidence

The abstract reports that sparse interpretable features account for two-thirds of the preference signal achieved by black-box models. Across seven datasets, WIMHF identifies possible and actual preferences, surfaces harmful patterns such as toxic-output preference in Chatbot Arena, and shows that relabeling harmful-feature examples yields +37 percent safety gains without hurting general performance.

## Limits and Failure Modes

Feature interpretability depends on labeling/describing sparse features accurately, and sparse features may omit interactions among preferences. Relabeling can shift dataset distribution in unexpected ways. Full-text review should check feature extraction details, human validation of descriptions, datasets, black-box baselines, and personalization evaluation.

## Deep Themes

- Interpretable preference data analysis.
- Preference features as curation handles.
- Dataset-level alignment diagnostics.
- Personalization through interpretable knobs.

## Subthemes

- Sparse autoencoders for feedback explanation.
- Harmful preference discovery.
- Measurable versus displayed preferences.
- Chatbot Arena preference artifacts.
- Community alignment personalization.

## Connections to Other Papers

Connects to P-GenRM, EigenBench, AdAEM, SSPO, and TI-DPO through preference/alignment signals, and to data-governance work because the data distribution itself encodes alignment behavior.

## Notes for Cross-Paper Synthesis

WIMHF is a strong example of treating preference data as an object of interpretation. Alignment quality depends on understanding what the feedback actually rewards before optimizing against it.
