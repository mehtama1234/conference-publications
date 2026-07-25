# The Axiomatic Value of Regularization in AI Alignment from Human Preferences

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 9ydYaIe1Qj
- Authors: Ezgi Korkmaz
- Primary area: social_aspects
- Keywords: social choice;axioms;AI alignment;regularization;RLHF
- Source URL: https://openreview.net/forum?id=9ydYaIe1Qj
- PDF URL: https://openreview.net/pdf?id=9ydYaIe1Qj

## Abstract

Reinforcement learning from human feedback is the leading approach to aligning powerful AI systems so that they can be safe and helpful for humanity. While RLHF is typically modelled as a problem of learning a single preference ranking from noisy feedback, true human preferences are complex and often conflicting, representing substantive disagreements stemming from the diversity of individual human values. With this motivation, a recent line of research has studied RLHF from the perspective of social choice theory, which provides a set of well-established desirable properties for aggregating diverse preferences. Seen through this lens, the standard learning objective in RLHF is equivalent to aggregating diverse human preferences via the Borda count rule. At the same time, several new RLHF algorithms have been proposed, which turn out to be equivalent to the von Neumann winner social choice rule. However, the connection between social choice theory and RLHF has thus far ignored the critical role of regularization to prevent divergence from a reference policy, which is utilized in essentially all practical RLHF algorithms. In this paper, we study how regularization affects the social choice axioms satisfied by different RLHF algorithms, and prove that regularization improves the axiomatic properties of the von Neumann winner rule. In contrast, the Borda count rule still fails to satisfy key social choice axioms even when regularized. These results provide a principled argument grounded in social choice theory for utilizing practical RLHF algorithms that correspond to the von Neumann winner, rather than the standard RLHF objective.

## One-Sentence Claim

Regularization changes the social-choice axioms satisfied by RLHF objectives, strengthening the case for von Neumann winner-style preference aggregation over Borda-style standard RLHF.

## Problem

RLHF is often modeled as learning one ranking from noisy feedback, but human preferences are diverse and conflicting; prior social-choice analyses also neglected practical reference-policy regularization.

## Core Contribution

The paper studies how regularization affects social-choice axioms in RLHF and proves that it improves the axiomatic properties of von Neumann winner rules while Borda-style objectives still fail key axioms.

## Method

It maps RLHF objectives to social choice rules, then analyzes how adding regularization toward a reference policy changes the axiomatic behavior of those rules.

## Experiments and Evidence

The abstract states theoretical results grounded in social choice theory rather than empirical experiments.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition is deferred after repeated rate-limit failures. Details still need checking: exact axioms, regularization form, assumptions about preference profiles, and how theory maps to practical RLHF implementations.

## Deep Themes

- Alignment from preferences is a social-choice problem, not just a reward-modeling problem.
- Regularization has normative effects, not only optimization-stability effects.
- Practical RLHF design can be evaluated axiomatically.

## Subthemes

- RLHF.
- Social choice theory.
- Reference-policy regularization.
- Borda count.
- von Neumann winner.
- Preference aggregation axioms.

## Connections to Other Papers

Connects to DPO/RLHF equivalence, VALUEFLOW, ParetoPO, and alignment pretraining through deeper analyses of what preference optimization is actually selecting.

## Notes for Cross-Paper Synthesis

This paper adds a normative-theory theme: regularization is not merely a technical stabilizer; it can change the democratic properties of preference aggregation.
