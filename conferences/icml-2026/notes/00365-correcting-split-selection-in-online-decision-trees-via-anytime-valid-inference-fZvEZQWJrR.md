# Correcting Split Selection in Online Decision Trees via Anytime-Valid Inference

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: fZvEZQWJrR
- Authors: Salim I. Amoukou; Saumitra Mishra; Manuela Veloso
- Primary area: general_machine_learning->online_learning_active_learning_and_bandits
- Keywords: Anytime-valid inference;Online decision trees;Hoeffding trees;Sequential testing;Testing by betting;Confidence sequences;Optional stopping;Non-stationary data streams;Adaptive Random Forests
- Source URL: https://openreview.net/forum?id=fZvEZQWJrR
- PDF URL: https://openreview.net/pdf?id=fZvEZQWJrR

## Abstract

Bagging-based ensembles, most notably Adaptive Random Forests, are among the strongest performers for learning from data streams. A common denominator across these methods is their reliance on Hoeffding Trees as base learners, which grow decision trees incrementally by testing whether a candidate split is significantly better than its alternatives using concentration inequalities. Despite their empirical success, existing Hoeffding Trees variants lack valid statistical guarantees. Current analyses rely on fixed-sample concentration bounds, while split decisions are made using data-dependent stopping rules, which invalidates their guarantees and can drive the probabilty of incorrect splits to one. We introduce a principled alternative based on \emph{anytime-valid inference}. Our method provides: (i) anytime-valid control of false splits under arbitrary data streams, including non-stationary settings; (ii) finite commitment time under a predictive advantage; and (iii) under stationary i.i.d.\ data, risk is monotone decreasing and strictly improves at every split. Empirically, we evaluate both standalone trees and their use within Adaptive Random Forests on non-stationary streams. Our method improves performance while producing substantially smaller trees.

## One-Sentence Claim

Online decision trees need anytime-valid split tests because fixed-sample Hoeffding bounds become invalid under adaptive stopping and can make false splits nearly certain.

## Problem

Hoeffding Trees grow by repeatedly testing whether one candidate split is significantly better than others. In practice these split decisions use data-dependent stopping, but many analyses rely on fixed-sample concentration bounds that do not remain valid under optional stopping.

The paper addresses a statistical bug at the base of strong data-stream learners such as Adaptive Random Forests.

## Core Contribution

The contribution is an anytime-valid inference method for online split selection. It controls false splits under arbitrary streams, including non-stationary settings, guarantees finite commitment time under a predictive advantage, and yields monotone decreasing risk under stationary i.i.d. data.

Empirically, it improves standalone trees and Adaptive Random Forests on non-stationary streams while producing substantially smaller trees.

## Method

The method replaces fixed-sample concentration tests with anytime-valid sequential inference, using tools such as confidence sequences or testing-by-betting ideas. These guarantees remain valid no matter when the algorithm stops and commits to a split.

This aligns the statistical test with the actual online control flow of incremental tree growth.

## Experiments and Evidence

Evidence reported in the abstract:

- Anytime-valid control of false splits under arbitrary data streams.
- Support for non-stationary settings.
- Finite commitment time under predictive advantage.
- Monotone decreasing risk and strict improvement at every split under stationary i.i.d. data.
- Improved empirical performance in standalone trees and Adaptive Random Forests.
- Substantially smaller trees.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact test statistic, betting process, stream datasets, and tree-size/performance tradeoff.

## Limits and Failure Modes

- Anytime-valid tests can be more conservative when advantages are small.
- Guarantees depend on the formal stream assumptions and definition of false split.
- Smaller trees are attractive, but overly delayed commitment can hurt adaptation in rapidly changing streams.
- Integration into large ensembles may involve computational overhead.

## Deep Themes

**Sequential validity matters.** A statistically valid test can become invalid when placed inside an adaptive online procedure.

**Guarantees should match runtime behavior.** The method corrects the mismatch between fixed-time analysis and optional stopping.

**Smaller models can result from better inference.** Controlling false splits improves both statistical validity and model compactness.

## Subthemes

- Anytime-valid inference.
- Online decision trees.
- Optional stopping correction.
- Confidence sequences.
- Non-stationary data streams.

## Connections to Other Papers

Connects to Weak-Strong Verification, Finite Test Certification, Delayed-Observation RL, and Token Overcharging. All expose failures that appear when adaptive procedures are evaluated with static or misaligned assumptions.

## Notes for Cross-Paper Synthesis

This paper adds a classic statistical lesson to modern ML systems: online algorithms need online-valid evidence, or their apparent confidence can become structurally wrong.
