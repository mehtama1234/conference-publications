# OC-space: a Unifying Perspective on Verification of Tree Ensembles

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: FLRPkR0N37
- Authors: Timo Martens; Laurens Devos; Lorenzo Cascioli; Wannes Meert; Hendrik Blockeel; Jesse Davis
- Primary area: social_aspects->robustness
- Keywords: Verification;Tree Ensembles;Robustness;Fairness
- Source URL: https://openreview.net/forum?id=FLRPkR0N37
- PDF URL: https://openreview.net/pdf?id=FLRPkR0N37

## Abstract

We study the problem of verifying whether certain properties such as robustness or fairness hold in an ensemble of decision trees.  
This problem is known to be NP-hard, with most research targeting a solution to a specific verification task.  We explore the problem through the lens of an ensemble's OC-space: the set of all possible combinations of the individual trees' predictions. This provides a unifying view that yields a more generic and flexible approach to verification.
We show that a wide variety of existing verification tasks can be (1) framed as simple searches through OC-space, and 
(2) answered in time linear or quadratic in the size of the OC-space.
Moreover, the search can be made more efficient by using spatial index structures. Interestingly, while the OC-space can grow exponentially with the ensemble's size, in practice it is often feasible to enumerate all output configurations. Empirically, we show that our generic approach can be faster than approaches targeting a single verification task.

## One-Sentence Claim

OC-space gives a unified verification view for tree ensembles by searching over possible combinations of individual tree predictions.

## Problem

Tree-ensemble verification for robustness or fairness is NP-hard, and prior methods usually target one specific verification task at a time.

## Core Contribution

The paper introduces output-configuration space as a generic abstraction that can express many verification tasks as searches through possible tree-output combinations.

## Method

It frames verification properties as searches through OC-space and shows many can be answered in time linear or quadratic in the OC-space size. Spatial index structures can make search more efficient.

## Experiments and Evidence

The abstract reports that although OC-space can grow exponentially, it is often feasible to enumerate in practice, and the generic approach can beat task-specific methods empirically.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: OC-space size distributions, verification task coverage, indexing details, and behavior on very large ensembles.

## Deep Themes

- Verification can benefit from a unifying representation of model outputs.
- Practical structure can make worst-case exponential spaces tractable.
- Fairness and robustness checks can share search infrastructure.

## Subthemes

- Tree ensembles.
- Formal verification.
- Robustness.
- Fairness.
- Output configurations.
- Spatial indexing.

## Connections to Other Papers

Connects to CIRBench, online conformal prediction, and robustness/safety verification papers through correctness guarantees for deployed models.

## Notes for Cross-Paper Synthesis

OC-space adds a verification-abstraction theme: many properties become simpler once the right discrete output space is exposed.
