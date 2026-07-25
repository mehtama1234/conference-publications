# Orbital Transformers for Predicting Wavefunctions in Time-Dependent Density Functional Theory

## Metadata

- Conference: iclr-2026
- Status: Poster
- OpenReview ID: 06I7jcrkW2
- Authors: Xuan Zhang; Haiyang Yu; Chengdong Wang; Jacob Helwig; Shuiwang Ji; Xiaofeng Qian
- Primary area: applications to physical sciences (physics, chemistry, biology, etc.)
- Keywords: Machine learning density functional theory;Time dependent neural PDE solver
- Source URL: https://openreview.net/forum?id=06I7jcrkW2
- PDF URL: https://openreview.net/pdf?id=06I7jcrkW2

## Abstract

We aim to learn wavefunctions simulated by time-dependent density functional theory (TDDFT), which can be efficiently represented as linear combination coefficients of atomic orbitals. In real-time TDDFT, the electronic wavefunctions of a molecule evolve over time in response to an external excitation, enabling first-principles predictions of physical properties such as optical absorption, electron dynamics, and high-order response. However, conventional real-time TDDFT relies on time-consuming propagation of all occupied states with fine time steps. In this work, we propose OrbEvo, which is based on an equivariant graph transformer architecture and learns to evolve the full electronic wavefunction coefficients across time steps. First, to account for external field, we design an equivariant conditioning to encode both strength and direction of external electric field and break the symmetry from SO(3) to SO(2). Furthermore, we design two OrbEvo models, OrbEvo-WF and OrbEvo-DM, using wavefunction pooling and density matrix as interaction method, respectively. Motivated by the central role of the density functional in TDDFT, OrbEvo-DM encodes the density matrix aggregated from all occupied electronic states into feature vectors via tensor contraction, providing a more intuitive approach to learn the time evolution operator. We adopt a training strategy specifically tailored to limit the error accumulation of time-dependent wavefunctions over autoregressive rollout. To evaluate our approach, we generate TDDFT datasets consisting of 5,000 different molecules in the QM9 dataset and 1,500 molecular configurations of the malonaldehyde molecule in the MD17 dataset. Results show that our OrbEvo model accurately captures quantum dynamics of excited states under external field, including time-dependent wavefunctions, time-dependent dipole moment, and optical absorption spectra characterized by dipole oscillator strength. It also shows strong generalization capability on the diverse molecules in the QM9 dataset.

## One-Sentence Claim

OrbEvo learns autoregressive time evolution of TDDFT electronic wavefunction coefficients with equivariant graph transformers, capturing excited-state quantum dynamics under external fields.

## Problem

Real-time TDDFT can predict optical absorption, electron dynamics, and high-order response, but conventional propagation of all occupied states over fine time steps is computationally expensive. Learning the time evolution of wavefunctions could accelerate first-principles molecular dynamics if it preserves physical symmetries and limits rollout error.

## Core Contribution

The paper contributes OrbEvo, an equivariant graph transformer for evolving full electronic wavefunction coefficients in an atomic-orbital basis. It introduces external-field equivariant conditioning and two interaction variants, OrbEvo-WF and OrbEvo-DM, including a density-matrix representation motivated by TDDFT structure.

## Method

OrbEvo represents wavefunctions as linear-combination coefficients over atomic orbitals and learns time-step evolution. External electric-field strength and direction are encoded with equivariant conditioning that breaks symmetry from SO(3) to SO(2). OrbEvo-WF uses wavefunction pooling, while OrbEvo-DM encodes density matrices via tensor contraction. Training is tailored to reduce autoregressive error accumulation.

## Experiments and Evidence

The abstract reports TDDFT datasets with 5,000 QM9 molecules and 1,500 MD17 malonaldehyde configurations. OrbEvo captures time-dependent wavefunctions, dipole moments, and optical absorption spectra with dipole oscillator strength, and generalizes across diverse QM9 molecules.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect basis-set choices, excitation regimes, long-rollout stability, conservation laws, molecule-size generalization, and comparison to numerical TDDFT cost/accuracy. Learned dynamics may drift under fields or molecules outside the training distribution.

## Deep Themes

- Neural solvers for time-dependent quantum dynamics.
- Equivariant modeling under external fields.
- Wavefunction and density-matrix representations.
- Autoregressive rollout error control.

## Subthemes

- TDDFT.
- Atomic orbital coefficients.
- OrbEvo-WF and OrbEvo-DM.
- SO(3) to SO(2) symmetry breaking.
- Optical absorption spectra.

## Connections to Other Papers

Connects to RealPDEBench through scientific ML for dynamical physical systems, to CauKer through structured time-series generation/modeling, and to DA3 through geometry-preserving representations.

## Notes for Cross-Paper Synthesis

OrbEvo is another example of domain-native representation: the model predicts wavefunction coefficients and density-matrix interactions rather than generic trajectories. Scientific ML gains come from encoding physics structure into the learned transition operator.
