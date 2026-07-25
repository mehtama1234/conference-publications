# Learning Biophysical Models of Large-Scale Multineuronal Data To Enable Precise Neurostimulation

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 4hoiRJsmpp
- Authors: Amrith Lotlikar; Ian Christopher Tanoh; Praful K. Vasireddy; Andrew Lanpouthakoun; Ramandeep Vilkhu; Michael A. Sommeling; A.J. Phillips; Alexander Sher; Alan Litke; Scott Linderman; EJ Chichilnisky; Subhasish Mitra
- Primary area: applications->neuroscience_cognitive_science
- Keywords: simulation based inference;retina;neuroscience;neuroengineering;multi-electrode array;extracellular recording;stimulation;biophysics;Hodgkin-Huxley
- Source URL: https://openreview.net/forum?id=4hoiRJsmpp
- PDF URL: https://openreview.net/pdf?id=4hoiRJsmpp

## Abstract

Multi-compartment Hodgkin–Huxley (HH) models provide a principled framework for predicting neural dynamics and responses to electrical stimulation. However, fitting HH biophysical parameters typically requires intracellular recordings, which are invasive and low-throughput, limiting the ability to capture the geometry and cell-specific properties of many neurons in a given neural circuit. Multi-electrode arrays (MEAs) offer a scalable alternative—high-density extracellular measurements from full neural populations—but HH model complexity has so far precluded reliable biophysical inference from extracellular data alone. Here, we introduce a framework to rapidly infer HH parameters from designed features of extracellular MEA measurements by leveraging differentiable biophysical simulation and simulation-based inference, unlocking a wide range of downstream applications. In this work, we focus on a central goal of translational neuroengineering: predicting neural spiking responses to candidate neurostimulation patterns that would take hours to measure clinically. To validate our approach, we collected hundreds of hours of stimulation and recording data from isolated macaque retina with a 30 µm-pitch 512-electrode array. Our framework predicted previously unseen multi-electrode stimulation responses with 90.4\% accuracy using HH models fit from only a few minutes of recording, replacing hours of stimulus testing.

## One-Sentence Claim

Differentiable biophysical simulation and simulation-based inference can fit Hodgkin-Huxley retinal models from extracellular MEA features, enabling accurate prediction of unseen neurostimulation responses from minutes of data.

## Problem

Multi-compartment Hodgkin-Huxley models are useful for predicting neural stimulation responses, but fitting them usually requires invasive, low-throughput intracellular recordings; extracellular MEA recordings are scalable but hard to invert into biophysical parameters.

## Core Contribution

The paper introduces a framework for inferring HH parameters from designed extracellular MEA features using differentiable biophysical simulation and simulation-based inference, targeting precise neurostimulation planning.

## Method

It fits multi-compartment retinal ganglion cell models from electrical-image features and stimulation-threshold features measured on high-density MEAs. Differentiable feature losses and simulation-based inference connect extracellular recordings to biophysical parameter estimates.

## Experiments and Evidence

The abstract reports hundreds of hours of macaque-retina stimulation/recording data from a 30 micrometer-pitch 512-electrode array and 90.4% accuracy predicting unseen multi-electrode stimulation responses using models fit from minutes of recording.

## Full-Text Upgrade

The full text describes a digital-twin pipeline for retinal ganglion cells recorded on a high-density 512-channel, 30 micrometer-pitch MEA. The model uses differentiable HH dynamics, line-source approximations for extracellular voltages, and differentiable stimulation-response relaxations so gradient-based fitting can use electrical image features and single-electrode stimulation thresholds.

Real-data validation includes 198 parasol cells across 13 retinal preparations, with multi-electrode stimulation outcomes for 37 cells. HH models fit from minutes of single-electrode data achieved about 0.906 accuracy on unseen simultaneous multi-electrode stimulation, outperforming independent and MLP baselines despite those baselines having more direct multi-electrode training information.

## Limits and Failure Modes

Limits to watch: biophysical ground truth is unavailable in real macaque recordings; the strongest validation is retinal parasol cells; parameter degeneracy remains a challenge; and clinical translation would require robustness across tissue conditions, electrode geometries, and patient-specific circuits.

## Deep Themes

- Scientific ML can use mechanistic simulators as data-efficient digital twins.
- Extracellular population recordings can support biophysical inference when paired with differentiable simulation.
- Precision neuroengineering depends on predicting interventions that are too expensive to exhaustively measure.

## Subthemes

- Hodgkin-Huxley models.
- Multi-electrode arrays.
- Simulation-based inference.
- Differentiable biophysical simulation.
- Retinal ganglion cells.
- Neurostimulation planning.

## Connections to Other Papers

Connects to Mind-Omni, Seeing Through the Brain, BioX-Bridge, and Frozen-PINN as scientific/biomedical ML work where domain structure and physical models compensate for limited labeled data.

## Notes for Cross-Paper Synthesis

This paper strengthens the scientific-ML theme: the most useful models in high-stakes science often combine mechanistic priors with learned inference rather than replacing biophysics with generic black-box predictors.
