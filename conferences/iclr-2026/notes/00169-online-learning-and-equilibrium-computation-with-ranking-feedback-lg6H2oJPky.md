# Online Learning and Equilibrium Computation with Ranking Feedback

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: lg6H2oJPky
- Authors: Mingyang Liu; Yongshan Chen; Zhiyuan Fan; Gabriele Farina; Asuman E. Ozdaglar; Kaiqing Zhang
- Primary area: learning theory
- Keywords: Online Learning;Equilibrium Computation;Human Feedback
- Source URL: https://openreview.net/forum?id=lg6H2oJPky
- PDF URL: https://openreview.net/pdf?id=lg6H2oJPky

## Abstract

Online learning in arbitrary and possibly adversarial environments has been extensively studied in sequential decision-making, with a strong connection to equilibrium computation in game theory. Most existing online learning algorithms are based on \emph{numeric} utility feedback from the environment, which may be unavailable in applications with humans in the loop and/or with privacy concerns. In this paper, we study an online learning setting where only a \emph{ranking} of a set of proposed actions is provided to the learning agent at each timestep. We consider both ranking models based on either the \emph{instantaneous} utility at each timestep, or the \emph{time-average} utility until the current timestep, in both \emph{full-information} and \emph{bandit} feedback settings. Focusing on the standard (external-)regret metric, we show that sublinear regret cannot be achieved with the instantaneous utility ranking feedback in general. Moreover, we show that when the ranking model is relatively {deterministic} (\emph{i.e.,} with a small temperature in the Plackett-Luce model), sublinear regret cannot be achieved with the time-average utility ranking feedback, either. We then propose new algorithms to achieve sublinear regret, under the additional assumption that the utility vectors have a sublinear variation. Notably, we also show that when time-average utility ranking is used, such an additional assumption can be avoided in the full-information setting. As a consequence, we show that if all the players follow our algorithms, an approximate coarse correlated equilibrium of a normal-form game can be found through repeated play. Finally, we also validate the effectiveness of our algorithms via numerical experiments.

## One-Sentence Claim

The paper characterizes when online learners can achieve sublinear regret and compute approximate equilibria using only ranking feedback rather than numeric utilities.

## Problem

Many online learning and game-theoretic algorithms assume numeric utility feedback, but human-in-the-loop or privacy-sensitive settings may only provide rankings over proposed actions. It is unclear when ranking feedback contains enough information for no-regret learning and equilibrium computation.

## Core Contribution

The paper studies instantaneous and time-average ranking models under full-information and bandit feedback, proves impossibility results for sublinear regret in key regimes, and designs algorithms that recover sublinear regret under variation or time-average assumptions.

## Method

The analysis formalizes ranking feedback, including Plackett-Luce-style temperature effects, and evaluates external regret. It proves lower bounds for instantaneous rankings and deterministic time-average rankings, then constructs algorithms that exploit sublinear variation or full-information time-average rankings. Repeated-play results translate the learning guarantees into approximate coarse correlated equilibrium computation.

## Experiments and Evidence

The abstract reports numerical experiments validating the algorithms. The theoretical evidence includes impossibility results and positive regret guarantees under stated assumptions, plus equilibrium computation when all players follow the proposed algorithms.

## Limits and Failure Modes

The positive guarantees depend on assumptions such as sublinear variation or access to full-information rankings. Real human rankings may be noisy, strategic, inconsistent, or context-dependent in ways not captured by the model. Full-text review should check regret rates, feedback models, bandit/full-information distinctions, and equilibrium approximation bounds.

## Deep Themes

- Learning from ordinal rather than cardinal feedback.
- Human-compatible online learning.
- Regret limits under weak feedback.
- Equilibrium computation through repeated play.

## Subthemes

- Instantaneous versus time-average ranking.
- Plackett-Luce temperature effects.
- Bandit ranking feedback.
- Sublinear variation assumptions.
- Approximate coarse correlated equilibria.

## Connections to Other Papers

Connects to preference and reward-model papers through weak/ordinal feedback, to P-GenRM and EigenBench through ranking-based alignment signals, and to multi-agent online learning work through equilibrium computation under limited feedback.

## Notes for Cross-Paper Synthesis

This paper adds theory for a central practical constraint: feedback is often comparative and privacy-preserving rather than numeric. The limits are as important as the algorithms because they identify when ranking feedback cannot support no-regret learning.
