# Conditional Equivalence of DPO and RLHF: Assumptions, Failure Modes, and Provable Alignment

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7UEBX1KU1y
- Authors: Zhiqin Yang; Yonggang Zhang; Wei Xue; Dong Fang; Bo Han; Yike Guo
- Primary area: applications->language_speech_and_dialog
- Keywords: Preference Optimization;Reinforcement Learning from Human Feedback
- Source URL: https://openreview.net/forum?id=7UEBX1KU1y
- PDF URL: https://openreview.net/pdf?id=7UEBX1KU1y

## Abstract

Direct Preference Optimization (DPO) has emerged as a popular alternative to Reinforcement Learning from Human Feedback (RLHF), offering theoretical equivalence with a simpler implementation. We prove this equivalence is _conditional_ rather than universal, depending on an implicit assumption frequently violated in practice: the RLHF-optimal policy must prefer human-preferred responses. When this assumption fails, DPO optimizes _relative advantage_ over the reference policy rather than _absolute alignment_ with human preferences, leading to pathological convergence where policies decrease DPO loss while preferring dispreferred responses. We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases. To address this, we introduce Constrained Preference Optimization (CPO), augmenting RLHF with constraints for provable alignment. We further provide a geometric interpretation through soft margin ranking, revealing that DPO implements margin ranking with potentially negative targets. Our theoretical analysis establishes when DPOs’ guarantees hold and provides solutions preserving simplicity with provable alignment. Comprehensive experiments on standard benchmarks demonstrate that CPO achieves state-of-the-art performance. Code is available at: _https://github.com/visitworld123/CPO_.

## One-Sentence Claim

DPO is equivalent to RLHF only under a condition that the RLHF-optimal policy prefers human-preferred responses; when this fails, DPO can reduce loss while moving away from absolute preference alignment.

## Problem

DPO is often used as a simpler theoretical replacement for RLHF, but its equivalence claims may hide assumptions that are violated in practical preference-learning settings.

## Core Contribution

The paper proves DPO-RLHF equivalence is conditional, characterizes failure modes and undesirable solution spaces, and proposes Constrained Preference Optimization for provable alignment.

## Method

It analyzes DPO as optimizing relative advantage over a reference policy rather than absolute human-preference alignment. It adds constraints to RLHF/CPO and gives a geometric interpretation through soft margin ranking with potentially negative targets.

## Experiments and Evidence

The abstract reports comprehensive benchmark experiments where CPO achieves state-of-the-art performance.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: exact assumption formalization, constraint form in CPO, benchmark suite, and whether failure modes appear in large-scale preference datasets.

## Deep Themes

- Preference optimization guarantees depend on hidden assumptions.
- Relative improvement over a reference policy is not always absolute alignment.
- Alignment theory is refining popular post-training objectives by exposing pathological solution spaces.

## Subthemes

- DPO.
- RLHF.
- Preference optimization.
- Constrained Preference Optimization.
- Soft margin ranking.
- Provable alignment.

## Connections to Other Papers

Connects to Beyond Log Likelihood, VALUEFLOW, DMPO, and Base Models Know How to Reason through post-training objective theory and the dependence of alignment methods on model/reference state.

## Notes for Cross-Paper Synthesis

This paper sharpens the post-training theme: simpler objectives can inherit guarantees only under specific behavioral conditions, so objective choice must be audited rather than assumed equivalent.
