# Exploring Synthesizable Chemical Space with Iterative Pathway Refinements

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: aQKVfKOkR5
- Authors: Seul Lee; Karsten Kreis; Srimukh Prasad Veccham; Meng Liu; Danny Reidenbach; Saee Gopal Paliwal; Weili Nie; Arash Vahdat
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: drug discovery;molecule generation;synthesizable molecule design
- Source URL: https://openreview.net/forum?id=aQKVfKOkR5
- PDF URL: https://openreview.net/pdf?id=aQKVfKOkR5

## Abstract

A well-known pitfall of molecular generative models is that they are not guaranteed to generate synthesizable molecules. Existing solutions for this problem often struggle to effectively navigate exponentially large combinatorial space of synthesizable molecules and suffer from poor coverage. To address this problem, we introduce ReaSyn, an iterative generative pathway refinement framework that obtains synthesizable analogs to input molecules by projecting them onto synthesizable space. Specifically, we propose a simple synthetic pathway representation that allows for generating pathways in both bottom-up and top-down traversal of synthetic trees. We design ReaSyn so that both bottom-up and top-down pathways can be sampled with a single unified autoregressive model. ReaSyn can thus iteratively refine subtrees of generated synthetic trees in a bidirectional manner. Further, we introduce a discrete flow model that refines the generated pathway at the entire pathway level with edit operations: insertion, deletion, and substitution. The iterative refinement cycle of (1) bottom-up decoding, (2) top-down decoding, and (3) holistic editing constitutes a powerful pathway reasoning strategy, allowing the model to explore the vast space of synthesizable molecules. Experimentally, ReaSyn achieves the highest reconstruction rate and pathway diversity in synthesizable molecule reconstruction and the highest optimization performance in synthesizable goal-directed molecular optimization, and significantly outperforms previous synthesizable projection methods in synthesizable hit expansion. These results highlight ReaSyn's superior ability to navigate combinatorially-large synthesizable chemical space.

## One-Sentence Claim

ReaSyn projects molecules into synthesizable chemical space by iteratively generating and refining synthetic pathways with bidirectional autoregression and discrete flow edits.

## Problem

Molecular generative models can propose high-scoring molecules that are difficult or impossible to synthesize.

Existing synthesizability fixes struggle to navigate the exponentially large combinatorial space of possible synthetic pathways and often have poor coverage.

## Core Contribution

The paper introduces ReaSyn, an iterative generative pathway refinement framework for synthesizable molecule design.

It defines a simple synthetic-pathway representation supporting both bottom-up and top-down traversal of synthesis trees and uses a unified autoregressive model for both directions.

## Method

ReaSyn alternates among bottom-up decoding, top-down decoding, and holistic pathway editing.

A discrete flow model edits full pathways through insertion, deletion, and substitution operations, allowing bidirectional refinement of generated synthetic-tree substructures.

## Experiments and Evidence

The abstract reports top reconstruction rate and pathway diversity for synthesizable molecule reconstruction.

ReaSyn also achieves the highest optimization performance for synthesizable goal-directed molecular optimization and outperforms prior synthesizable projection methods in hit expansion.

## Limits and Failure Modes

Pathway-level synthesizability still depends on reaction database coverage, reagent availability, yields, conditions, and whether generated routes are practical in a lab.

Because this note is abstract-only, details still need checking: pathway representation, reaction templates, discrete flow architecture, chemical benchmarks, synthesizability metrics, and wet-lab realism.

## Deep Themes

- Synthesizability-constrained generation: molecule quality is tied to feasible production paths.
- Pathway reasoning as generative search: synthesis trees become the object of generation and refinement.
- Bidirectional chemical planning: bottom-up and top-down traversal complement each other.
- Discrete flow over structured edits: insertion, deletion, and substitution operate on pathway-level objects.

## Subthemes

- Molecule generation.
- Synthetic pathway refinement.
- Discrete flow models.
- Hit expansion.

## Connections to Other Papers

This connects to DCFold, PCD, diffusion black-box optimization, and scientific generation papers.

It also relates to RefineStat because both use iterative refinement over structured scientific objects.

## Notes for Cross-Paper Synthesis

ReaSyn adds a scientific-design theme: generative models must search not just for desirable endpoints, but for feasible paths to those endpoints.
