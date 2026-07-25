# Dynamic Programming for Epistemic Uncertainty in Markov Decision Processes

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: oUv02QKUxG
- Authors: Axel Benyamine; Julien Grand-Clément; Marek Petrik; Michael I. Jordan; Alain Oliviero Durmus
- Primary area: theory->reinforcement_learning_and_planning
- Keywords: Dynamic programming;distributional uncertainty;robust Markov decision processes
- Source URL: https://openreview.net/forum?id=oUv02QKUxG
- PDF URL: https://openreview.net/pdf?id=oUv02QKUxG

## Abstract

In this paper, we propose a general theory of ambiguity-averse MDPs, which treats the uncertain transition probabilities as random variables and evaluates a policy via a risk measure applied to its random return. This ambiguity-averse MDP framework unifies several models of MDPs with epistemic uncertainty for specific choices of risk measures.  We extend the concepts of value functions and Bellman operators to our setting. Based on these objects, we establish the consequences of dynamic programming principles in this framework (existence of stationary policies, value and policy iteration algorithms), and we completely characterize law-invariant risk measures compatible with dynamic programming. Our work draws connections among several variants of MDP models and fully delineates what is possible under the dynamic programming paradigm and which risk measures require leaving it.

## One-Sentence Claim

Ambiguity-averse MDPs can be given a dynamic-programming theory by treating uncertain transitions as random variables and characterizing exactly which law-invariant risk measures remain Bellman-compatible.

## Problem

MDPs with epistemic transition uncertainty appear in robust RL, Bayesian RL, and distributional uncertainty models, but these variants are often studied separately. The field lacks a unified account of when dynamic programming still works once policy value is defined through a risk measure over random returns.

The core tension is time consistency. A risk measure that is sensible for evaluating uncertain returns may not decompose through Bellman recursion. If it does not, standard value iteration, policy iteration, and stationary-policy guarantees can fail.

## Core Contribution

The paper proposes a general ambiguity-averse MDP framework in which transition probabilities are random variables and policies are evaluated by applying a risk measure to the induced random return. It extends value functions and Bellman operators to this setting, proving when dynamic programming principles still hold.

Its most important contribution is a characterization result: it delineates the class of law-invariant risk measures compatible with dynamic programming. That separates uncertainty models that can live inside the Bellman paradigm from those that require fundamentally different solution methods.

## Method

The framework lifts MDP uncertainty into random transition kernels and then evaluates policies through risk functionals on returns. Generalized value functions and Bellman operators are defined for this ambiguity-averse setting, allowing the authors to study stationary policies, value iteration, and policy iteration.

The theoretical analysis focuses on law-invariant risk measures, meaning risk evaluations depend on the distribution of the uncertain return rather than arbitrary representations. The compatibility characterization identifies which such measures preserve dynamic-programming decomposability.

## Experiments and Evidence

This is a theory paper; the evidence is the unified formal framework, existence results for stationary policies, algorithmic consequences for value/policy iteration, and the risk-measure characterization theorem.

Because the note is metadata-grounded, full-paper reading should verify the exact assumptions on state/action spaces, transition uncertainty distributions, discounting or finite horizon, and whether the characterization changes under rectangularity or other ambiguity-set structure.

## Limits and Failure Modes

Risk measures outside the characterized compatible class may be meaningful for decision makers but incompatible with dynamic programming. That is not a weakness of those risk measures; it means the Bellman machinery is the wrong algorithmic paradigm.

Practical use also depends on whether the random transition model is estimable and whether the risk measure captures the decision maker's ambiguity attitude. In high-dimensional or function-approximation RL, the theory may require approximation layers not covered by the abstract.

## Deep Themes

- Dynamic programming as a compatibility constraint: not every uncertainty preference can be recursively optimized.
- Epistemic uncertainty as random environment structure: transition probabilities are uncertain objects, not fixed unknown constants.
- Unification by risk measures: robust/Bayesian-style MDP variants become instances of a broader ambiguity-averse framework.
- Theory as boundary drawing: the paper says which modeling choices remain inside the Bellman world and which must leave it.

## Subthemes

- Law invariance is a strong organizing principle for uncertainty preferences.
- Time consistency is the hidden requirement behind Bellman recursion.
- Stationary-policy existence is nontrivial under random transition uncertainty.
- Algorithm design is constrained by the mathematical form of ambiguity aversion.

## Connections to Other Papers

This paper connects to exact RL unlearning and first-price auction learning theory through finite, formal guarantees for adaptive decision processes. It also pairs with epistemic uncertainty and robust-optimization threads elsewhere in ICML, where uncertainty modeling affects which algorithms are valid.

Compared with WestWorld and ScaleMoE, which learn control-oriented representations empirically, this paper asks what uncertainty-aware control objectives can even be solved by dynamic programming.

## Notes for Cross-Paper Synthesis

The synthesis point is that "handling uncertainty" is not one technique. The choice of uncertainty functional determines the algorithmic universe: Bellman-compatible models get dynamic programming; others need different tools.
