# Transforming Weather Data from Pixel to Latent Space

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: NlSWKeQPoZ
- Authors: Sijie Zhao; Feng Liu; Xueliang Zhang; Hao Chen; Tao Han; Junchao Gong; Ran Tao; Pengfeng Xiao; Xinyu Gu; LEI BAI
- Primary area: applications->chemistry_physics_and_earth_sciences
- Keywords: Climate Modeling;Unified Representation;Data Compression;Autoencoder;ERA5-latent Dataset
- Source URL: https://openreview.net/forum?id=NlSWKeQPoZ
- PDF URL: https://openreview.net/pdf?id=NlSWKeQPoZ

## Abstract

The increasing impact of climate change and extreme weather events has spurred growing interest in deep learning for weather research. However, existing studies often rely on weather data in pixel space, which presents several challenges such as smooth outputs in model outputs, limited applicability to a single pressure-variable subset (PVS), and high data storage and computational costs. To address these challenges, we propose a novel Weather Latent Autoencoder (WLA) that transforms weather data from pixel space to latent space, enabling efficient data representation. By decoupling weather reconstruction from downstream tasks, WLA improves the accuracy and sharpness of weather task model results. The incorporated Pressure-Variable Unified Module transforms multiple PVS into a unified representation, enhancing the adaptability of the model in multiple weather scenarios. Furthermore, weather tasks can be performed in a low-storage latent space of WLA rather than a high-storage pixel space, thus significantly reducing data storage and computational costs. Through extensive experimentation, we demonstrate its superior compression and reconstruction performance, enabling the creation of the ERA5-Latent dataset with unified representations of multiple PVS from ERA5 data. The compressed full PVS in the ERA5-Latent dataset reduces the original 244.34 TB of data to 0.43 TB. The downstream task further demonstrates that task models can apply to multiple PVS with low data costs in latent space and achieve superior performance compared to models in pixel space.

## One-Sentence Claim

Weather Latent Autoencoder compresses and unifies weather data across pressure-variable subsets, enabling sharper downstream modeling in low-storage latent space.

## Problem

Weather models often operate in pixel space, causing smooth outputs, limited applicability to specific pressure-variable subsets, and high storage and compute costs.

## Core Contribution

The paper introduces WLA, a Pressure-Variable Unified Module, and ERA5-Latent, compressing full PVS ERA5 data from 244.34 TB to 0.43 TB while supporting multiple weather tasks.

## Method

WLA decouples weather reconstruction from downstream tasks by encoding weather fields into a unified latent representation. Downstream models operate in latent space instead of high-storage pixel space.

## Experiments and Evidence

The abstract reports superior compression and reconstruction performance, sharper and more accurate downstream task outputs, applicability across multiple PVS, and large data-storage reduction.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: weather variables, resolution, compression artifacts, downstream tasks, extreme-event fidelity, uncertainty calibration, and accessibility of ERA5-Latent.

## Deep Themes

- Latent datasets can reduce scientific data storage and compute bottlenecks.
- Unified representations allow task models to span multiple physical variable subsets.
- Compression quality matters for sharpness and downstream scientific validity.

## Subthemes

- Climate modeling.
- Weather autoencoders.
- ERA5-Latent.
- Data compression.
- Pressure-variable unification.
- Latent-space forecasting.

## Connections to Other Papers

Connects to FIRE, Modified SINNs, PWC-Diff, and AI-for-science papers that use domain-specific representations to make scientific modeling cheaper and more accurate.

## Notes for Cross-Paper Synthesis

Weather latent modeling adds an infrastructure-scale data theme: for scientific ML, representation learning can turn an unwieldy physical dataset into a reusable computational substrate.
