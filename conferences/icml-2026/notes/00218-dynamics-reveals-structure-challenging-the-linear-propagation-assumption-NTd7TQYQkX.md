# Dynamics Reveals Structure: Challenging the Linear Propagation Assumption

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: NTd7TQYQkX
- Authors: Hoyeon Chang; Bálint Mucsányi; Seong Joon Oh
- Primary area: deep_learning->theory
- Keywords: Knowledge editing;Geometric Deep Learning;Systematicity;Compositional reasoning;Representation learning;Large Language Models
- Source URL: https://openreview.net/forum?id=NTd7TQYQkX
- PDF URL: https://openreview.net/pdf?id=NTd7TQYQkX

## Abstract

Neural networks adapt through first-order parameter updates, yet it remains unclear whether such updates preserve logical coherence.
We investigate the geometric limits of the Linear Propagation Assumption (LPA), the premise that local updates coherently propagate to logical consequences.
To formalize this, we adopt relation algebra and study three core operations on relations: negation flips truth values, converse swaps argument order, and composition chains relations.
For negation and converse, we prove that guaranteeing direction-agnostic first-order propagation necessitates a tensor factorization separating entity-pair context from relation content.
However, for composition, we identify a fundamental obstruction.
We show that composition reduces to conjunction, and prove that any conjunction well-defined on linear features must be bilinear.
Since bilinearity is incompatible with negation, this forces the feature map to collapse.
These results suggest that failures in knowledge editing, the reversal curse, and multi-hop reasoning may stem from common structural limitations inherent to the LPA.

## One-Sentence Claim

The paper shows that first-order parameter updates cannot generally preserve logical propagation for relation composition, exposing structural limits behind knowledge-editing and multi-hop reasoning failures.

## Problem

Knowledge editing and compositional reasoning often assume local updates will propagate coherently to logical consequences, but the geometric validity of this Linear Propagation Assumption is unclear.

## Core Contribution

Using relation algebra, the paper proves conditions for negation and converse propagation and identifies a fundamental obstruction for composition: conjunction over linear features must be bilinear, which conflicts with negation unless the feature map collapses.

## Method

The analysis formalizes relation operations such as negation, converse, and composition, then studies what feature factorization and update geometry are required for direction-agnostic first-order propagation.

## Experiments and Evidence

The abstract is theoretical and links its results to failures in knowledge editing, reversal curse, and multi-hop reasoning.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: formal assumptions, feature-map class, relation algebra scope, empirical validation if any, and implications for practical editing methods.

## Deep Themes

- Logical coherence may be incompatible with simple linear update propagation.
- Relation composition exposes deeper limits than negation or converse.
- Knowledge-editing failures can share a geometric source with reasoning failures.

## Subthemes

- Knowledge editing.
- Linear Propagation Assumption.
- Relation algebra.
- Reversal curse.
- Multi-hop reasoning.
- Bilinear conjunction.

## Connections to Other Papers

Connects to analogical reasoning, graph algorithm learning, and NSE theory through formal limits on compositional structure in learned representations.

## Notes for Cross-Paper Synthesis

This paper adds a structural-impossibility theme: some reasoning and editing failures may not be patchable by more local updates because the assumed propagation geometry is inconsistent.
