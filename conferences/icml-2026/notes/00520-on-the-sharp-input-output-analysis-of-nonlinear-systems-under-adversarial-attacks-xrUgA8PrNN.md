# On the Sharp Input-Output Analysis of Nonlinear Systems under Adversarial Attacks

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: xrUgA8PrNN
- Authors: Jihun Kim; Yuchen Fang; Javad Lavaei
- Primary area: theory->learning_theory
- Keywords: Nonlinear System Identification;Input-Output Analysis;Probabilistic Adversarial Attacks
- Source URL: https://openreview.net/forum?id=xrUgA8PrNN
- PDF URL: https://openreview.net/pdf?id=xrUgA8PrNN

## Abstract

This paper is concerned with learning the input-output mapping of general nonlinear dynamical systems. While the existing literature focuses on Gaussian inputs and benign disturbances, we significantly broaden the scope of admissible control inputs and allow correlated, nonzero-mean, adversarial disturbances. With our reformulation as a linear combination of basis functions, we prove that the $\ell_2$-norm estimator overcomes the challenges posed by an adversary with access to the full information history, provided that the attack times are sparse, *i.e.*, the probability that the system is under adversarial attack at a given time is smaller than a certain threshold. We provide an estimation error bound that decays with the input memory length and prove its optimality by constructing a problem instance that suffers from the same bound under probabilistic adversarial attacks. Our work provides a sharp input-output analysis for a generic nonlinear and partially observed system under significantly generalized assumptions compared to existing works.

## One-Sentence Claim

General nonlinear dynamical systems can be learned under correlated nonzero-mean adversarial disturbances when attack times are sparse, with optimal error decay in input memory length.

## Problem

Existing nonlinear system-identification theory often assumes Gaussian inputs and benign disturbances. Real control systems may face broader input classes and adversaries with access to the full history.

The problem is to learn input-output mappings for generic nonlinear partially observed systems when disturbances are correlated, biased, and adversarial but occur sparsely.

## Core Contribution

The paper broadens input-output analysis to general admissible control inputs and probabilistic adversarial attacks. It proves that an l2-norm estimator can handle a full-history adversary if the probability of attack at each time is below a threshold.

It gives an estimation error bound decaying with input memory length and proves optimality by constructing a matching hard instance.

## Method

The nonlinear input-output map is reformulated as a linear combination of basis functions. The estimator uses l2 structure to recover the mapping despite adversarial disturbances.

The analysis models attack times probabilistically and sparsely, allowing the adversary to be strong in information access while limiting how often attacks occur.

## Experiments and Evidence

The abstract reports theoretical upper and lower bounds rather than empirical experiments.

The main evidence is a sharp estimation error analysis: the bound decays with input memory length and is matched by a constructed problem instance under probabilistic adversarial attacks.

## Limits and Failure Modes

The guarantee depends on attack sparsity being below a threshold and on the adequacy of the basis-function reformulation. Dense or adaptively timed attacks may violate the assumptions.

Because this note is abstract-only, details still need checking: attack probability threshold, basis class, partial observability model, memory-length dependence, estimator implementation, and whether constants are practical.

## Deep Themes

- Robust system identification: learning dynamics must account for adversarial disturbances.
- Sparsity as robustness condition: strong adversaries are tolerable only when attacks are rare enough.
- Sharp input-output theory: matching lower bounds clarify unavoidable error.
- Basis-function linearization: nonlinear systems become analyzable through structured expansions.

## Subthemes

- Full-history adversaries.
- Correlated nonzero-mean disturbances.
- Input memory length.
- Optimal estimation bounds.

## Connections to Other Papers

This connects to robust contextual optimization, conformal policy control, and robust RL/control papers through adversarial uncertainty in decision systems.

It also relates to LAMP and dynamical-systems graph modeling because both use structured dynamics assumptions to derive stability or estimation guarantees.

## Notes for Cross-Paper Synthesis

This paper contributes a control-theoretic robustness theme: reliability under adversaries often becomes possible only after formalizing the rate or sparsity of harmful events.
