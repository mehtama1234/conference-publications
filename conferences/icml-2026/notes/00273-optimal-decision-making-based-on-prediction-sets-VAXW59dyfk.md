# Optimal Decision-Making Based on Prediction Sets

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: VAXW59dyfk
- Authors: Tao Wang; Edgar Dobriban
- Primary area: theory->probabilistic_methods
- Keywords: Uncertainty Quantification;Decision making;Conformal prediction
- Source URL: https://openreview.net/forum?id=VAXW59dyfk
- PDF URL: https://openreview.net/pdf?id=VAXW59dyfk

## Abstract

Prediction sets can wrap around any ML model to cover unknown test outcomes with a guaranteed probability. Yet, it remains unclear how to use them optimally for downstream decision-making. Here, we propose a decision-theoretic framework that seeks to minimize the expected loss (risk) against a worst-case distribution consistent with the prediction set's coverage guarantee. We first characterize the minimax optimal policy for a fixed prediction set, showing that it balances the worst-case loss inside the set with a penalty for potential losses outside the set. Building on this, we derive the optimal prediction set construction that minimizes the resulting robust risk subject to a coverage constraint. Finally, we introduce Risk-Optimal Conformal Prediction (ROCP), a practical algorithm that targets these risk-minimizing sets while maintaining finite-sample distribution-free marginal coverage. Empirical evaluations on medical diagnosis and a toy static hazard-decision benchmark demonstrate that ROCP reduces critical mistakes compared to baselines, particularly when out-of-set errors are costly. The source code to reproduce our experiments is available at https://github.com/TaoWangPenn/Risk-Optimal-Conformal-Prediction.

## One-Sentence Claim

Prediction sets should be constructed for downstream minimax decision risk, not only coverage, especially when out-of-set errors are costly.

## Problem

Prediction sets provide distribution-free coverage guarantees around ML predictions, but coverage alone does not specify how a decision-maker should act. Two sets with the same coverage can imply very different losses, especially if mistakes outside the set are critical.

The paper asks how to use prediction sets optimally for downstream decisions and how to construct sets that minimize robust decision risk.

## Core Contribution

The paper introduces a decision-theoretic framework that minimizes expected loss against the worst-case distribution consistent with a prediction set's coverage guarantee.

It characterizes the minimax optimal policy for a fixed set as balancing worst-case loss inside the set with a penalty for possible outside-set losses. It then derives optimal prediction-set construction for robust risk under a coverage constraint and introduces Risk-Optimal Conformal Prediction, or ROCP, which maintains finite-sample distribution-free marginal coverage.

## Method

The method combines robust decision theory with conformal prediction. First, for a given prediction set, it solves the minimax decision problem implied by coverage uncertainty. Second, it optimizes the set construction itself so that the induced robust risk is minimized subject to coverage.

ROCP operationalizes this by targeting risk-minimizing conformal sets rather than generic smallest or score-thresholded sets.

## Experiments and Evidence

Evidence reported in the abstract:

- Characterization of minimax optimal policies for fixed prediction sets.
- Derivation of optimal prediction set construction under robust risk and coverage constraints.
- ROCP algorithm with finite-sample distribution-free marginal coverage.
- Empirical evaluation on medical diagnosis and a static hazard-decision benchmark.
- Reduced critical mistakes compared with baselines, especially when out-of-set errors are costly.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: loss classes, decision spaces, conformal scores, baselines, and whether guarantees are marginal or conditional for subgroups.

## Limits and Failure Modes

- Worst-case distributions consistent with coverage may be conservative.
- Marginal coverage can still hide subgroup undercoverage.
- Decision loss must be specified; wrong loss design can optimize the wrong behavior.
- Medical deployment would require calibration, clinical workflow validation, and prospective testing.

## Deep Themes

**Uncertainty quantification must be decision-aware.** A prediction set is useful only through the actions it supports.

**Coverage is not the whole objective.** The paper optimizes robust risk under coverage rather than treating coverage as sufficient.

**Set-valued predictions are becoming operational objects.** They are not just error bars; they define a minimax policy.

## Subthemes

- Decision-theoretic conformal prediction.
- Minimax policies under coverage constraints.
- Risk-optimal prediction sets.
- Out-of-set loss penalties.
- Critical-error reduction in high-stakes settings.

## Connections to Other Papers

Connects to Bulk-Calibrated Credal Sets, Falling Trees, DISCO, and robust decision papers. It also links to evaluation work because the target metric is downstream loss under uncertainty rather than predictive accuracy alone.

## Notes for Cross-Paper Synthesis

ROCP adds to a decision-first trend: uncertainty, robustness, interpretability, and risk models are being judged by the decisions they enable, not only by standalone statistical guarantees.
