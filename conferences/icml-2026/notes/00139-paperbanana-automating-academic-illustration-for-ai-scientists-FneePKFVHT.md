# PaperBanana: Automating Academic Illustration for AI Scientists

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: FneePKFVHT
- Authors: Dawei Zhu; Rui Meng; Yale Song; Xiyu Wei; Sujian Li; Tomas Pfister; Jinsung Yoon
- Primary area: applications->computer_vision
- Keywords: image generation;academic illustration;diagram generation
- Source URL: https://openreview.net/forum?id=FneePKFVHT
- PDF URL: https://openreview.net/pdf?id=FneePKFVHT

## Abstract

Despite rapid advances in autonomous AI scientists powered by language models, generating publication-ready illustrations remains a labor-intensive bottleneck in the research workflow.
To lift this burden, we introduce PaperBanana, an agentic framework for automated generation of publication-ready academic illustrations.
Powered by state-of-the-art VLMs and image generation models,
PaperBanana orchestrates specialized agents to retrieve references, plan content and style, render images, and iteratively refine via self-critique. 
To rigorously evaluate our framework, we introduce PaperBananaBench, comprising 292 test cases for methodology diagrams curated from NeurIPS 2025 publications, covering diverse research domains and illustration styles. 
Comprehensive experiments demonstrate that PaperBanana consistently outperforms leading baselines in faithfulness, conciseness, readability, and aesthetics. 
We further show that our method effectively extends to the generation of high-quality statistical plots.
Collectively,
PaperBanana paves the way for the automated generation of publication-ready illustrations.

## One-Sentence Claim

PaperBanana automates publication-ready academic illustration through a multi-agent workflow that retrieves references, plans diagrams, renders images, and self-critiques.

## Problem

Autonomous AI scientists can draft research artifacts, but generating faithful, concise, readable, publication-ready illustrations remains labor-intensive.

## Core Contribution

The paper introduces PaperBanana and PaperBananaBench, a 292-case benchmark of methodology diagrams curated from NeurIPS 2025 papers.

## Method

PaperBanana orchestrates specialized VLM and image-generation agents for reference retrieval, content/style planning, rendering, and iterative self-critique refinement.

## Experiments and Evidence

The abstract reports that PaperBanana outperforms leading baselines on faithfulness, conciseness, readability, and aesthetics, and extends to high-quality statistical plot generation.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: evaluation rubric, human preference setup, diagram faithfulness failures, copyright/reference use, and editability of outputs.

## Deep Themes

- AI-scientist workflows need visual artifact generation, not only text.
- Multi-agent generation pipelines can decompose creative scholarly tasks.
- Scientific communication quality is becoming a benchmarked AI capability.

## Subthemes

- Academic illustration.
- Diagram generation.
- AI scientists.
- VLM agents.
- Image generation.
- Self-critique.

## Connections to Other Papers

Connects to DR Tulu, Paper-to-code/security systems, and scientific-agent workflow papers through automation of research production artifacts.

## Notes for Cross-Paper Synthesis

PaperBanana adds a research-workflow automation theme: agentic systems are beginning to handle the visual communication layer of science.
