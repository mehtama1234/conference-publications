# Unsupervised Partner Design Enables Robust Ad-hoc Teamwork

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 0xtMUL0eiF
- Authors: Constantin Ruhdorfer; Matteo Bortoletto; Victor Oei; Anna Penzkofer; Andreas Bulling
- Primary area: reinforcement_learning->multiagent
- Keywords: Ad-hoc Teamwork;Curriculum Learning;Multi-Agent Reinforcement Learning;Human-AI Teaming
- Source URL: https://openreview.net/forum?id=0xtMUL0eiF
- PDF URL: https://openreview.net/pdf?id=0xtMUL0eiF

## Abstract

We introduce Unsupervised Partner Design (UPD), a population-free multi-agent reinforcement learning method for robust ad-hoc teamwork. 
UPD generates training partners on-the-fly and selects them adaptively based on a learnability criterion, removing the need for pre-trained partner populations or manual parameter tuning.
We show that this simple mechanism enables effective partner diversity and can be extended to joint partner-environment selection when a procedural level generator is available. 
Across Level-Based Foraging, Overcooked-AI, and the Overcooked Generalisation Challenge, UPD consistently achieves strong performance compared to both population-based and population-free baselines. 
In a human-AI user study, agents trained with UPD achieve higher returns and are rated as more adaptive, more human-like, and less frustrating than all evaluated baseline methods.

## One-Sentence Claim

Unsupervised Partner Design trains robust ad-hoc teamwork agents by generating and selecting learning partners on the fly instead of relying on fixed pretrained partner populations.

## Problem

Ad-hoc teamwork requires agents to cooperate with unfamiliar partners, but existing multi-agent RL methods often depend on curated partner populations, manual parameter choices, or brittle diversity assumptions.

## Core Contribution

The paper introduces UPD, a population-free MARL method that adaptively generates training partners according to a learnability criterion, with an extension to joint partner-environment selection when procedural levels are available.

## Method

UPD creates partners during training and selects them based on how useful they are for learning. The method induces partner diversity without requiring a pre-existing population and can combine partner choice with environment/level choice.

## Experiments and Evidence

The abstract reports strong performance on Level-Based Foraging, Overcooked-AI, and the Overcooked Generalisation Challenge. In a human-AI study, UPD agents receive higher returns and are rated more adaptive, human-like, and less frustrating than baselines.

## Limits and Failure Modes

Full-text checks needed: how learnability is measured, whether generated partners cover real human diversity, sample efficiency, and robustness when procedural environment generation is unavailable.

## Deep Themes

- Robust agents need adaptive training partners, not only harder tasks.
- Human-AI teaming is becoming a first-class evaluation setting.
- Curriculum learning and partner generation are merging in MARL.

## Subthemes

- Ad-hoc teamwork.
- Multi-agent reinforcement learning.
- Partner generation.
- Human-AI teaming.
- Curriculum learning.

## Connections to Other Papers

Connects to RAGEN-2 and CyberGym through agent evaluation under dynamic interaction, and to DS/solver papers through environment/partner generation as training infrastructure.

## Notes for Cross-Paper Synthesis

This paper supports a broader agentic theme: the training distribution must include social/environmental variation, and robustness comes from adaptive curricula rather than static benchmark exposure.
