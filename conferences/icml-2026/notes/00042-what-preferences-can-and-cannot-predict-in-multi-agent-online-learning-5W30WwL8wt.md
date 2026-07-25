# What Preferences Can—and Cannot—Predict in Multi-Agent Online Learning

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 5W30WwL8wt
- Authors: Omar Abbadi; Rida Laraki; Panayotis Mertikopoulos
- Primary area: theory->game_theory
- Keywords: Learning;Preferences;Stability;Game Dynamics;No-Regret;Follow-The-Regularized-Leader
- Source URL: https://openreview.net/forum?id=5W30WwL8wt
- PDF URL: https://openreview.net/pdf?id=5W30WwL8wt

## Abstract

We examine the interplay between ordinal, preference-based solution concepts in games and the outcomes of payoff-driven learning dynamics, asking to what extent the combinatorial data of a game—its *preference graph*—can predict the long-run behavior of no-regret dynamics such as *follow-the-regularized-leader* (FTRL). In one direction, we show that the skeleton of every *dynamically stable* set (i.e., the set of pure profiles it contains) must also be *preferentially stable*, that is, it must be closed under profitable deviations.
We then ask the converse question: when are preferences sufficient to describe the long-run behavior of the players' learning dynamics?
We begin by showing that preferences are indeed enough to fully characterize asymptotic stability in the case of *subgames*—i.e., subsets of pure profiles obtained by restricting players' action sets. Beyond this case however, the equivalence between dynamic and preferential stability breaks down: in particular, we construct a three-player game with a preferentially stable set whose span is dynamically *unstable*, showing that preferences are *not sufficient* to describe dynamically stable behavior in general. To restore stability, we introduce the notion of *leaklessness*, a measure of aggregate payoff drift away from a set of pure profiles, and we use it to identify a payoff-based condition guaranteeing that the span of a set of pure profiles is stable and attracting.

## One-Sentence Claim

Preference graphs can predict some stable outcomes of multi-agent learning, but payoff magnitudes still matter beyond subgame-like cases because preferential stability alone does not guarantee dynamic stability.

## Problem

Game theory often distinguishes ordinal preferences from payoff-driven learning dynamics, but it is unclear when the combinatorial preference graph of a game is enough to predict long-run no-regret dynamics such as FTRL.

## Core Contribution

The paper characterizes when preferential stability and dynamic stability align, shows where they diverge, and introduces leaklessness as a payoff-based condition that restores stability guarantees.

## Method

It analyzes preference graphs, dynamically stable sets, preferentially stable skeletons, subgame restrictions, and FTRL-type payoff-driven learning dynamics. It then constructs counterexamples and defines leaklessness as aggregate payoff drift away from a set.

## Experiments and Evidence

The abstract reports theoretical results: dynamically stable sets imply preferentially stable skeletons; preferences fully characterize asymptotic stability for subgames; outside that case, a three-player counterexample shows preferential stability can be dynamically unstable; leaklessness gives a sufficient payoff-based stability condition.

## Limits and Failure Modes

No confident local PDF/arXiv match yet, so details still need checking: exact definitions of skeleton/span/leaklessness, assumptions on regularizers and learning rates, and whether results extend beyond FTRL/no-regret dynamics.

## Deep Themes

- Ordinal structure is sometimes insufficient for learning dynamics.
- Payoff magnitudes can determine stability even when preferences look stable.
- Multi-agent learning needs bridges between solution concepts and actual adaptive dynamics.

## Subthemes

- Game dynamics.
- Preference graphs.
- FTRL.
- No-regret learning.
- Dynamic stability.
- Leaklessness.

## Connections to Other Papers

Connects to Unsupervised Partner Design and multi-agent/agentic papers through learning behavior in interactive systems. It also links to safety/process themes because stable-looking local incentives may not predict long-run dynamics.

## Notes for Cross-Paper Synthesis

This paper adds a multi-agent theory caution: high-level preference structure can miss dynamical instability unless payoff-driven drift is modeled explicitly.
