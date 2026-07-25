# Mixtures Closest To A Given Measure: A Semidefinite Programming Approach

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 0JDzkrKzaA
- Authors: Srecko Durasinovic; Jean B. Lasserre; Victor Magron
- Primary area: theory->optimization
- Keywords: Mixture Models;Semidefinite Programming;Moment-SOS Hierarchy;Clustering
- Source URL: https://openreview.net/forum?id=0JDzkrKzaA
- PDF URL: https://openreview.net/pdf?id=0JDzkrKzaA

## Abstract

Mixture models, such as Gaussian mixture models (GMMs), are widely used in machine learning to represent complex data distributions. A key challenge, especially in high-dimensional settings, is to determine the mixture order and estimate the mixture parameters. We study the problem of approximating a target measure, available only through finitely many of its moments, by a mixture of distributions from a parametric family (e.g., Gaussian, exponential, Poisson), with approximation quality measured by the 2-Wasserstein ($\operatorname{W_2}$) or the total variation ($\operatorname{TV}$) distance. Unlike many existing approaches, the parameter set is not assumed to be finite; it is modeled as a compact basic semi-algebraic set. We introduce a hierarchy of semidefinite relaxations with asymptotic convergence to the desired optimal value. In addition, when a certain rank condition is satisfied, the convergence is even finite and recovery of an optimal mixing measure is obtained. We also present an application to clustering, where our framework serves either as a stand-alone method or as a preprocessing step that yields both the number of clusters and strong initial parameter estimates, thereby accelerating convergence of standard (local) clustering algorithms

## One-Sentence Claim

The paper formulates fitting the closest parametric mixture to moment information as a semidefinite relaxation hierarchy with asymptotic and sometimes finite convergence guarantees.

## Problem

Mixture models are useful for complex distributions, but estimating mixture order and parameters is hard in high-dimensional settings, especially when only finitely many moments of the target measure are available.

## Core Contribution

The paper introduces an SDP/Moment-SOS hierarchy for approximating a target measure by mixtures from a parametric family over a compact semi-algebraic parameter set, with guarantees for convergence and recovery under rank conditions.

## Method

It optimizes mixture approximation under Wasserstein-2 or total variation distance using semidefinite relaxations. The parameter space is continuous rather than assumed finite, and finite convergence/recovery is possible when the relaxation satisfies a rank condition.

## Experiments and Evidence

The abstract mentions a clustering application where the framework can estimate cluster number and provide strong initial parameters that accelerate local clustering algorithms.

## Limits and Failure Modes

PDF checks needed: computational scalability of the SDP hierarchy, moment-estimation noise sensitivity, practical dimensional limits, and how often finite-rank recovery holds.

## Deep Themes

- Classical optimization/theory remains important for distribution modeling.
- Moment information can support principled mixture recovery.
- Global relaxations can complement local ML algorithms.

## Subthemes

- Mixture models.
- Semidefinite programming.
- Moment-SOS hierarchy.
- Wasserstein/TV approximation.
- Clustering initialization.

## Connections to Other Papers

Connects to theory/optimization and to hybrid pipelines where rigorous global methods provide structure or initialization for more heuristic local procedures.

## Notes for Cross-Paper Synthesis

This paper is a reminder that the 2026 landscape is not only foundation models. There is still deep method work on classical probabilistic modeling, especially where guarantees and recovery matter.
