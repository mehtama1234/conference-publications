# Treatment Responder Classification with Abstention

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: WFdQSjmchK
- Authors: Haoxiang Wang; Aoqi Zuo; Ziyan Wang; Zhiheng Zhang; Erdun Gao; Kun Zhang; Haoxuan Li; Mingming Gong
- Primary area: general_machine_learning->causality
- Keywords: Treatment Responder;Causal Classification;Abstention;Robustness
- Source URL: https://openreview.net/forum?id=WFdQSjmchK
- PDF URL: https://openreview.net/pdf?id=WFdQSjmchK

## Abstract

Treatment responder classification seeks to learn a rule to classify individuals who will benefit from the treatment. This paper studies a new scenario in treatment responder classification when abstention is allowed, i.e., practitioners can opt out of making uncertain classification on some individuals for further investigation. By revealing the implicit relation between causal misclassification risk with abstention and Conditional Value at Risk (CVaR), we develop a doubly robust method named TRECA to learn the classification rule under loose convergence conditions on nuisance parameters, and further extend it to deal with possible violation on key assumptions such as monotonicity and unconfoundedness. Rigorous theories and extensive experiments on two real-world datasets demonstrate the theoretical and experimental guarantee on our methods in learning treatment responders classification rules with low regret at the cost of limited abstention.

## One-Sentence Claim

Treatment responder classification can safely abstain on uncertain individuals by linking causal misclassification risk to CVaR and learning doubly robust low-regret rules.

## Problem

Treatment responder classification tries to identify who will benefit from an intervention. In real clinical or policy workflows, forcing a binary decision for every individual can be risky because some cases are ambiguous or violate modeling assumptions.

The paper studies responder classification with abstention: the model may defer uncertain cases for further investigation, trading limited coverage loss for lower causal decision regret.

## Core Contribution

The paper reveals an implicit relation between causal misclassification risk with abstention and Conditional Value at Risk. It develops TRECA, a doubly robust method for learning treatment-responder rules under loose nuisance-parameter convergence conditions.

It further extends the method to handle possible violations of key causal assumptions such as monotonicity and unconfoundedness.

## Method

TRECA uses causal-risk estimation with abstention and a CVaR-style objective to focus on uncertain or high-risk classification regions. Doubly robust estimation reduces dependence on any single nuisance model being perfectly specified.

The abstention mechanism lets the learned rule opt out of cases where the responder decision would otherwise carry high regret.

## Experiments and Evidence

Evidence reported in the abstract:

- Rigorous theory for causal classification with abstention.
- Loose convergence requirements on nuisance parameters.
- Extensions for monotonicity and unconfoundedness violations.
- Extensive experiments on two real-world datasets.
- Low regret achieved with limited abstention.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: causal estimands, abstention budget, nuisance models, datasets, and sensitivity analysis for assumption violations.

## Limits and Failure Modes

- Abstention is useful only if deferred cases can actually receive further investigation.
- Doubly robust methods still need sufficient overlap and reasonable nuisance estimates.
- CVaR-style conservatism may abstain disproportionately on underrepresented groups if not audited.
- Assumption-violation extensions need careful practical diagnostics.

## Deep Themes

**High-stakes causal decisions need a defer option.** The model should know when classification confidence is not enough for action.

**Risk tails matter more than average accuracy.** CVaR links abstention to the high-loss region of causal misclassification.

**Robust causal learning is becoming operational.** The method addresses nuisance error and assumption violations because deployment rarely satisfies clean theory.

## Subthemes

- Causal classification with abstention.
- CVaR and low-regret responder rules.
- Doubly robust estimation.
- Monotonicity and unconfoundedness sensitivity.
- Deferred decision workflows.

## Connections to Other Papers

Connects to ROCP, Falling Trees, and Bulk-Calibrated Credal Sets through decision-aware uncertainty and high-stakes risk. It also links to DISCO and causal-robustness papers by explicitly handling causal assumptions and unstable dependencies.

## Notes for Cross-Paper Synthesis

TRECA adds a concrete abstention pattern: robust AI decisions increasingly include a "do not decide yet" action when causal evidence is too weak for safe classification.
