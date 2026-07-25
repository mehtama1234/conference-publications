# Beyond First-order Asymptotics in Sequential Mean Testing

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: HMyCBL2yMV
- Authors: VIKAS DEEP; Shubhada Agrawal
- Primary area: theory->online_learning_and_bandits
- Keywords: Sequential testing;Non-parametric statistics;Asymptotic analysis;Central limit theorem
- Source URL: https://openreview.net/forum?id=HMyCBL2yMV
- PDF URL: https://openreview.net/pdf?id=HMyCBL2yMV

## Abstract

We revisit the problem of sequentially testing the mean of bounded distributions in a level-$\alpha$ power-one framework. We study a $\mathrm{KL_{inf}}$-based sequential test that is known to attain the information-theoretic lower bound on the expected stopping time with exact constants as $\alpha \to 0$. Going beyond first-order asymptotics, we establish a central limit theorem (CLT) for the stopping time of this test. Our analysis proceeds in two steps. First, we prove a  novel CLT for the $\mathrm{KL_{inf}}$ statistic itself, characterizing its fluctuations around its deterministic limit. We then leverage this result to show that the stopping time, centered appropriately and scaled by $\sqrt{\log(1/\alpha)}$, converges in distribution to a Gaussian limit with an explicit variance. This yields a second-order characterization of an asymptotically optimal sequential test for bounded distributions. Finally, we present numerical experiments that corroborate our theoretical findings.

## One-Sentence Claim

The paper gives a second-order central-limit characterization of stopping times for an asymptotically optimal KL-inf sequential mean test.

## Problem

Sequential mean tests can be first-order optimal in expected stopping time, but first-order asymptotics do not describe the fluctuation behavior needed to understand finite-threshold reliability.

## Core Contribution

The main contribution is a CLT for the KL-inf statistic and a resulting Gaussian limit for the centered, scaled stopping time of a level-alpha power-one test for bounded distributions.

## Method

The analysis first proves a CLT for fluctuations of the KL-inf statistic around its deterministic limit, then transfers that result to the stopping time after centering and scaling by sqrt(log(1/alpha)), yielding an explicit variance.

## Experiments and Evidence

The abstract reports numerical experiments that corroborate the theoretical second-order approximation.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: regularity assumptions, exact bounded-distribution class, finite-alpha accuracy, numerical setup, and comparison against alternative sequential tests.

## Deep Themes

- Moving beyond first-order optimality toward distributional performance guarantees.
- Sequential decision rules need uncertainty estimates over stopping behavior.
- Asymptotic theory remains useful when it explains operational finite-sample variability.

## Subthemes

- Sequential testing.
- KL-inf statistics.
- Online learning and bandits.
- Nonparametric statistics.
- Central limit theorem.
- Stopping-time analysis.

## Connections to Other Papers

Connects to bandit and online-learning theory papers through stopping-time efficiency and to broader evaluation papers that distinguish average optimality from uncertainty around operational behavior.

## Notes for Cross-Paper Synthesis

This paper contributes a precision-of-guarantees theme: mature ML theory increasingly asks not only whether a method is asymptotically optimal, but how its fluctuations behave around that optimum.
