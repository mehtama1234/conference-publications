# mCLM: A Modular Chemical Language Model that Generates Functional and Makeable Molecules

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: r2HG3xOMJI
- Authors: Carl Edwards; Chi Han; Gawon Lee; Thao Nguyen; Sara Szymkuć; Chetan Kumar Prasad; Bowen Jin; Jiawei Han; Ying Diao; Ge Liu; Hao Peng; Bartosz Andrzej Grzybowski; Martin D. Burke; Heng Ji
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: molecule-language multimodality;language model;molecule tokenization;molecule generation
- Source URL: https://openreview.net/forum?id=r2HG3xOMJI
- PDF URL: https://openreview.net/pdf?id=r2HG3xOMJI

## Abstract

Despite their ability to understand chemical knowledge, large language models (LLMs) remain limited in their capacity to propose novel molecules with desired functions (e.g., drug-like properties). In addition, the molecules that LLMs propose can often be challenging to make, and are almost never compatible with automated synthesis approaches. To better enable the discovery of functional small molecules, LLMs need to learn a new molecular language that is more effective in predicting properties and inherently synced with automated synthesis technology. Current molecule LLMs are limited by representing molecules based on atoms. In this paper, we argue that just like tokenizing texts into meaning-bearing (sub-)word tokens instead of characters, molecules should be tokenized at the level of functional building blocks, i.e., parts of molecules that bring unique functions and serve as effective building blocks for real-world automated laboratory synthesis. This motivates us to propose mCLM, a modular Chemical-Language Model that comprises a bilingual language model that understands both natural language descriptions of functions and molecular blocks. mCLM front-loads synthesizability considerations while improving the predicted functions of molecules in a principled manner. Experiments on 430 FDA-approved drugs showed that mCLM is capable of significantly improving chemical functions critical to determining drug potentials. mCLM, with only 3B parameters, also achieves improvements in synthetic accessibility relative to 7 other leading generative AI methods including GPT-5. When tested on 122 out-of-distribution medicines using only building blocks/tokens that are compatible with automated modular synthesis, mCLM outperforms all baselines in property scores and synthetic accessibility. mCLM can also reason on multiple functions and iteratively self-improve to rescue drug candidates that failed late in clinical trials (“fallen angels”).

## One-Sentence Claim

mCLM generates functional and synthesizable molecules by tokenizing chemistry into modular building blocks aligned with natural-language function descriptions and automated synthesis.

## Problem

LLMs can encode chemical knowledge but often propose molecules that are hard to synthesize or incompatible with automated lab workflows. Atom-level molecule representations may be poorly matched to functional design and modular synthesis constraints.

## Core Contribution

The paper introduces mCLM, a modular Chemical-Language Model that represents molecules as functional building blocks rather than atom tokens. It trains a bilingual model over natural-language function descriptions and molecular blocks to front-load synthesizability while optimizing drug-like functions.

## Method

mCLM tokenizes molecules into meaning-bearing synthetic modules compatible with automated modular synthesis. The language model reasons over both function descriptions and molecule-block sequences, supports multi-function objectives, and iteratively self-improves candidate molecules.

## Experiments and Evidence

On 430 FDA-approved drugs, mCLM reportedly improves chemical functions relevant to drug potential. The 3B model improves synthetic accessibility versus seven leading generative AI methods including GPT-5. On 122 OOD medicines using synthesis-compatible building blocks, it outperforms baselines in property scores and synthetic accessibility, and can rescue late-stage failed drug candidates.

## Limits and Failure Modes

Building-block tokenization may restrict novelty or miss molecules outside modular synthesis chemistry. Property scores and synthetic accessibility metrics may not capture biological activity, toxicity, ADMET, or actual synthesis yield. Full-text review should check token vocabulary, synthesis constraints, property predictors, OOD split, wet-lab validation, and self-improvement loop safeguards.

## Deep Themes

- Chemistry tokenization aligned with synthesis.
- Functional molecule generation.
- Language-molecule bilingual modeling.
- Makeability as a first-class design constraint.

## Subthemes

- Modular molecular building blocks.
- Automated synthesis compatibility.
- Multi-function molecular reasoning.
- Drug-candidate rescue.
- Synthesizability-aware generative AI.

## Connections to Other Papers

Connects to Complexa and protein-design work through scientific generative design, to data/tokenization papers through representation choices, and to constrained generation themes where outputs must be physically or operationally realizable.

## Notes for Cross-Paper Synthesis

mCLM makes tokenization a deployment constraint: the molecular language is chosen so generated outputs can be made, not just scored. This parallels other papers that redesign representations around downstream actionability.
