# Excited Pfaffians: Generalized Neural Wave Functions Across Structure and State

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: meEsugjXjv
- Authors: Nicholas Gao; Till Grutschus; Frank Noe; Stephan Günnemann
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Machine Learning for Science;Computational Physics;Computational Chemistry;Quantum Chemistry;Quantum Monte Carlo;Variational Monte Carlo;Neural Quantum States;Wave Function;Excited States
- Source URL: https://openreview.net/forum?id=meEsugjXjv
- PDF URL: https://openreview.net/pdf?id=meEsugjXjv

## Abstract

Neural-network wave functions in Variational Monte Carlo (VMC) have achieved great success in accurately representing both ground and excited states. However, achieving sufficient numerical accuracy in state overlaps requires increasing the number of Monte Carlo samples, and consequently the computational cost, with the number of states. We present a nearly constant sample-size approach, Multi-State Importance Sampling (MSIS), that leverages samples from all states to estimate pairwise overlap. To efficiently evaluate all states for all samples, we introduce Excited Pfaffians. Inspired by Hartree-Fock, this architecture represents many states within a single neural network. Excited Pfaffians also serve as generalized wave functions, allowing a single model to represent multi-state potential energy surfaces. On the carbon dimer, we match the $\mathcal{O}(N_s^4)$-scaling natural excited states while training $>200\times$ faster and modeling 50\% more states. Our favorable scaling enables us to be the first to use neural networks to find all distinct energy levels of the beryllium atom. Finally, we demonstrate that a single wave function can represent excited states across various molecules.

## One-Sentence Claim

Excited Pfaffians and multi-state importance sampling let a single neural quantum-state model represent many ground and excited states while keeping overlap estimation computationally manageable.

## Problem

Neural-network wave functions have become powerful for variational Monte Carlo, but multi-state problems stress the standard workflow. Estimating pairwise overlaps accurately across many states requires more Monte Carlo samples as the number of states grows, and evaluating separate wave functions for each state compounds the cost.

This bottleneck matters for chemistry and physics tasks where excited states, potential energy surfaces, and state overlaps are central. A model that only handles one state efficiently cannot scale to the multi-state structure of realistic quantum systems.

## Core Contribution

The paper contributes a near constant-sample approach, Multi-State Importance Sampling, for estimating pairwise overlaps by reusing samples across states. It pairs this estimator with the Excited Pfaffians architecture, which represents many states inside one neural network.

The larger contribution is architectural: instead of training a separate high-capacity neural wave function per state, the model encodes cross-state structure and can act as a generalized wave function over both molecular structure and quantum state.

## Method

Multi-State Importance Sampling draws on samples from all represented states to estimate overlaps, reducing the need for state-specific sample growth. Excited Pfaffians are inspired by Hartree-Fock structure and allow efficient evaluation of all states for all samples inside a shared model.

This design makes overlap computation and multi-state potential surface modeling part of the same representation problem. The model's shared structure is not only a speed trick; it encodes the assumption that related excited states should be represented jointly.

## Experiments and Evidence

The abstract reports strong evidence on molecular and atomic benchmarks: on carbon dimer, the method matches natural excited-state accuracy while training more than 200x faster and modeling 50 percent more states. It also claims the first neural-network result finding all distinct energy levels of the beryllium atom, plus demonstrations that a single wave function can represent excited states across multiple molecules.

The evidence is unusually concrete for a metadata-only note because the abstract includes scaling and domain-specific accomplishments. Full verification should still inspect the PDF for numerical definitions, baseline details, and how "all distinct energy levels" is operationalized.

## Limits and Failure Modes

The method likely inherits the sensitivity of variational Monte Carlo to ansatz quality, sampling variance, and optimization stability. A shared multi-state model may also create interference between states if the represented state family becomes too heterogeneous.

Its most compelling claims are in quantum chemistry/physics settings where Pfaffian structure is appropriate. The generality of the approach across larger molecules, denser excited-state spectra, or strongly correlated regimes requires full-paper inspection.

## Deep Themes

- Scientific ML as structured amortization: the model amortizes across related physical states rather than solving each state independently.
- Efficiency through shared generative structure: speed comes from representing the joint state family, not just faster kernels.
- Classical scientific priors inside neural architectures: Hartree-Fock/Pfaffian inductive bias guides a modern neural wave-function model.
- Scaling laws for scientific computation: the key objective is changing how cost grows with number of states.

## Subthemes

- Multi-state learning reframes excited-state quantum chemistry as a representation-sharing problem.
- Sampling reuse is a recurring route to scientific ML scalability when exact computation is expensive.
- Neural architectures in physics increasingly succeed by embedding domain structure rather than discarding it.
- A single model spanning structure and state hints at foundation-model-like reuse for molecular simulation.

## Connections to Other Papers

Excited Pfaffians connects to PAR, DeCoDe, and other molecular/scientific generation papers through the use of structured neural models for physical domains. It also relates to MERLIN's functional Koopman work: both use domain-aware structure to make scientific prediction tractable across states or resolutions.

In the broader theme map, it is another example of efficiency as a capability enabler, but at the level of scientific sampling and state representation rather than LLM inference.

## Notes for Cross-Paper Synthesis

This paper strengthens a cross-corpus pattern: in scientific ML, the winning move is often not larger generic models but carefully shared representations aligned with the mathematical object being modeled. The subtheme is "structured amortization over related physical instances."
