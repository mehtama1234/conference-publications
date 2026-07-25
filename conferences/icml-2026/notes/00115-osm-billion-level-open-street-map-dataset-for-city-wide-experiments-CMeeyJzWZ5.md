# OSM+: Billion-Level Open Street Map Dataset for City-wide Experiments

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: CMeeyJzWZ5
- Authors: Guanjie Zheng; Ziyang Su; Yiheng Wang; Yuhang Luo; Hongwei Zhang; Xuanhe Zhou; Linghe Kong; Fan Wu; Wen Ling
- Primary area: general_machine_learning->sequential_network_and_time_series_modeling
- Keywords: large dataset;traffic prediction
- Source URL: https://openreview.net/forum?id=CMeeyJzWZ5
- PDF URL: https://openreview.net/pdf?id=CMeeyJzWZ5

## Abstract

Road network data provides rich information about cities, but processing worldwide OpenStreetMap (OSM) data is computationally intensive, and the resulting graphs are often difficult to unify for benchmarking downstream tasks. Existing graph learning benchmarks fail to capture the billion-scale and unique topological properties of real-world road networks, leaving model scalability underexplored. To close this gap, we process OSM data with distributed cloud computing using 5,000 cores and release **OSM+**, a structured worldwide 1-billion-vertex road network graph dataset designed for high accessibility and usability. OSM+ is open source and globally downloadable, providing an open-box graph structure together with an easy spatial query interface that allows users to retrieve, inspect, and integrate road network topology, geometry, and attributes without repeatedly preprocessing raw OSM files. We demonstrate the utility of OSM+ through four illustrative use cases: basic query, city boundary detection, traffic prediction, and traffic policy control. For traffic prediction, we construct a new 31-city benchmark by processing traffic data and combining it with OSM+, enabling broader spatial coverage and more comprehensive evaluation than commonly used datasets, while scaling from hundreds of road network intersections to thousands. For traffic policy control, we release a new six-city dataset at a much larger scale, introducing challenges for thousand-scale multi-agent coordination and controller scalability. We also provide data processing tools for integrating multimodal spatial-temporal data with OSM+ for geospatial foundation model training, thereby expediting the discovery of compelling scientific insights.

## One-Sentence Claim

OSM+ turns worldwide OpenStreetMap data into an accessible billion-vertex road-network graph dataset for city-scale graph learning, traffic prediction, and policy control.

## Problem

Raw OSM processing is computationally intensive and existing graph benchmarks do not capture the billion-scale topology of real road networks, limiting scalability research.

## Core Contribution

The paper releases OSM+, a structured worldwide road-network graph with query tools, plus traffic prediction and traffic policy control benchmarks at much larger spatial scales.

## Method

The authors process OSM data with distributed cloud computing using 5,000 cores, expose open-box topology/geometry/attributes through a spatial query interface, and combine OSM+ with multimodal spatial-temporal data.

## Experiments and Evidence

The abstract reports four use cases: basic query, city boundary detection, a 31-city traffic prediction benchmark, and a six-city traffic policy control dataset for thousand-scale multi-agent coordination.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: data freshness, global coverage bias, graph schema, licensing, benchmark splits, and computational cost for users.

## Deep Themes

- Real-world graph learning needs datasets at infrastructure scale.
- Open spatial query interfaces can reduce repeated preprocessing barriers.
- City-scale policy control creates large multi-agent coordination challenges.

## Subthemes

- OpenStreetMap.
- Billion-scale road graphs.
- Traffic prediction.
- Traffic policy control.
- Geospatial foundation models.
- Multi-agent city systems.

## Connections to Other Papers

Connects to S3GNN, traffic/time-series papers, city-scale multi-agent control, and geospatial foundation-model infrastructure.

## Notes for Cross-Paper Synthesis

OSM+ adds a dataset-infrastructure theme: scaling graph learning may require shared processed world-scale substrates, not only new architectures.
