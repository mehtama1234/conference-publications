# The Relative Instability of Model Comparison with Cross-validation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: kpdyQ1GDRt
- Authors: Alexandre Bayle; Lucas Janson; Lester Mackey
- Primary area: general_machine_learning->evaluation
- Keywords: Cross-validation;model comparison;algorithmic stability;relative stability;confidence interval;test error;soft-thresholding;Lasso
- Source URL: https://openreview.net/forum?id=kpdyQ1GDRt
- PDF URL: https://openreview.net/pdf?id=kpdyQ1GDRt

## Abstract

Cross-validation (CV) is known to provide asymptotically exact tests and confidence intervals for model improvement but only when the model comparison is *relatively stable*. Surprisingly, we prove that even simple, individually stable models can generate relatively unstable comparisons, calling into question the validity of CV inference. Specifically, we show that the Lasso and its close cousin, soft-thresholding, generate relatively unstable comparisons and invalid CV inferences, even in the most favorable of learning settings and when both models are individually stable. These findings highlight the importance of verifying relative stability before deploying CV for model comparison.

## One-Sentence Claim

Cross-validation model-comparison inference can be invalid when the comparison is relatively unstable, even if each individual model is stable.

## Problem

Cross-validation is widely used for model comparison and can provide asymptotically exact tests and confidence intervals for improvement, but only under relative stability. Practitioners often check or assume stability of individual models, which is not enough.

The paper asks whether simple stable learners can still produce unstable pairwise comparisons that invalidate CV inference.

## Core Contribution

The paper proves that Lasso and soft-thresholding can generate relatively unstable comparisons and invalid CV inferences, even in favorable learning settings and even when both models are individually stable.

The result calls for verifying relative stability before using CV-based confidence intervals or hypothesis tests for model improvement.

## Method

The analysis distinguishes individual algorithmic stability from relative stability of the loss difference between two models. It constructs or proves cases where individual predictions are stable while their comparison fluctuates enough to break CV inference.

Lasso and soft-thresholding serve as concrete, common examples.

## Experiments and Evidence

Evidence reported in the abstract:

- Proof that simple individually stable models can yield relatively unstable comparisons.
- Lasso and soft-thresholding shown to generate invalid CV inferences.
- Result holds in favorable learning settings.
- Implication that relative stability should be verified before deploying CV inference.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: exact instability examples, asymptotic regime, and practical diagnostic tests.

## Limits and Failure Modes

- The result targets inference for model comparison, not all uses of CV for rough validation.
- Practitioners still need usable diagnostics for relative stability.
- The severity in complex modern models may differ from Lasso/soft-thresholding examples.
- Conservative alternatives may reduce power.

## Deep Themes

**Evaluation validity depends on comparison stability.** Stable models do not guarantee stable differences.

**Common statistical tools have hidden conditions.** CV inference can fail under assumptions that are easy to overlook.

**Pairwise improvement is its own object.** The loss-difference process needs separate analysis from each model's error.

## Subthemes

- Cross-validation inference.
- Relative stability.
- Model comparison confidence intervals.
- Lasso and soft-thresholding.
- Algorithmic stability.

## Connections to Other Papers

Connects to Finite Test Certification, Anytime Trees, 2-SAT Robustness, MADQA, and evaluation-methodology papers. It adds a classical statistical warning to the corpus's benchmark-validity theme.

## Notes for Cross-Paper Synthesis

This paper strengthens the evaluation rigor theme: even familiar procedures require checks that match the exact claim being made, especially when comparing systems.
