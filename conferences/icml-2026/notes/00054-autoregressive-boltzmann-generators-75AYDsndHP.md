# Autoregressive Boltzmann Generators

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 75AYDsndHP
- Authors: Danyal Rehman; Charlie B. Tan; Yoshua Bengio; Joey Bose; Alexander Tong
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Boltzmann Generators;AI for Science;Molecules;Peptides
- Source URL: https://openreview.net/forum?id=75AYDsndHP
- PDF URL: https://openreview.net/pdf?id=75AYDsndHP

## Abstract

Efficient sampling of molecular systems at thermodynamic equilibrium is a hallmark challenge in statistical physics. This challenge has driven the development of Boltzmann Generators (BGs), which allow rapid generation of uncorrelated equilibrium samples by combining a generative model with exact likelihoods and an importance sampling correction. However, modern BGs predominantly rely on Normalizing Flows (NFs), which either suffer from limited expressivity due to strict invertibility constraints (discrete time) or computationally expensive likelihoods (continuous time). In this paper, we propose Autoregressive Boltzmann Generators (ArBG), a novel autoregressive modelling framework that overcomes these limitations by departing from the flow-based BG paradigm. ArBG circumvents the topological constraints of flows and enables sequential inference-time interventions, while offering enhanced scalability by leveraging architectures effective in Large Language Models. We empirically demonstrate that ArBG leads to significant improvements over flow-based models across all benchmarks, but particularly in larger peptide systems such as the 10-residue Chignolin. Furthermore, we introduce Robin, a 132M parameter transferable model trained with the ArBG framework which improves over the previous state-of-the-art, reducing the zero-shot energy error, $\mathcal{E}$-$\mathcal{W}_2$, on 8-residue systems by $\sim 60$\%.

## One-Sentence Claim

Autoregressive Boltzmann Generators replace flow-based equilibrium samplers with exact-likelihood autoregressive models, improving molecular sampling scalability and enabling inference-time interventions.

## Problem

Boltzmann Generators need expressive proposal distributions with exact likelihoods for importance sampling, but normalizing-flow BGs face invertibility constraints or expensive continuous-time likelihood computation.

## Core Contribution

The paper proposes ArBG, an autoregressive framework for Boltzmann generation, and introduces Robin, a transferable 132M-parameter model for peptide equilibrium sampling.

## Method

ArBG models molecular coordinates sequentially with tractable autoregressive likelihoods, then uses self-normalized importance sampling against the target energy. The autoregressive factorization also permits intermediate inference-time interventions unavailable to flow-based BGs.

## Experiments and Evidence

The abstract reports improvements over flow-based models across benchmarks, especially larger peptide systems such as 10-residue Chignolin, and about 60% reduction in zero-shot energy error on 8-residue systems with Robin.

## Full-Text Upgrade

The full text positions ArBG against discrete and continuous normalizing flows. Discrete flows give exact likelihoods but can be expressively limited; continuous flows are expressive but require costly ODE-based likelihood evaluation. Autoregressive models offer exact likelihoods without invertibility, making them natural proposal distributions for Boltzmann sampling.

Experiments evaluate alanine peptides through Chignolin using energy-distribution metrics, torsional Wasserstein metrics, and TICA-Wasserstein structure. The paper highlights scaling to decapeptides and zero-shot transfer to unseen peptides via Robin. It also notes limitations: autoregressive factorization can concentrate on low-energy modes, may struggle with sharper energy profiles, and introduces different tradeoffs from flows.

## Limits and Failure Modes

Limits to watch: autoregressive order and discretization/bin choices matter; mode coverage can suffer if likelihood concentrates on low-energy minima; and scaling to larger biomolecules may require stronger architectures and better intervention strategies.

## Deep Themes

- Scientific generative modeling is borrowing LLM-style autoregression for physical equilibrium sampling.
- Exact likelihood remains central when generation is tied to importance correction.
- Departing from normalizing flows can remove topological constraints in molecular generation.

## Subthemes

- Boltzmann Generators.
- Autoregressive molecular models.
- Equilibrium sampling.
- Importance sampling.
- Peptide conformations.
- Transferable scientific models.

## Connections to Other Papers

Connects to protein autoregressive modeling, constrained diffusion, quotient-space diffusion, and scientific generative modeling papers. It also links to LLM-style sequence modeling migrating into scientific domains.

## Notes for Cross-Paper Synthesis

ArBG strengthens the scientific foundation-model theme: architectures proven in language can become useful scientific samplers when adapted to domain constraints like energy likelihoods and equilibrium correction.
