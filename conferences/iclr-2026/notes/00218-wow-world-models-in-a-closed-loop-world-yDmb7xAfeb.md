# WoW!: World Models in a Closed-Loop World

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: yDmb7xAfeb
- Authors: Jiahan Zhang; Muqing Jiang; Nanru Dai; TaiMing Lu; Arda Uzunoglu; Shunchi Zhang; Yana Wei; Jiahao Wang; Vishal M. Patel; Paul Pu Liang; Daniel Khashabi; Cheng Peng; Rama Chellappa; Tianmin Shu; Alan Yuille; Yilun Du; Jieneng Chen
- Primary area: generative models
- Keywords: world models;video generation;embodied AI;generative models
- Source URL: https://openreview.net/forum?id=yDmb7xAfeb
- PDF URL: https://openreview.net/pdf?id=yDmb7xAfeb

## Abstract

Generative world models (WMs) can now simulate worlds with striking visual realism, which naturally raises the question of whether they can endow embodied agents with predictive perception for decision making. Progress on this question has been limited by fragmented evaluation: most existing benchmarks adopt open-loop protocols that emphasize visual quality in isolation, leaving the core issue of embodied utility unresolved, i.e., *do WMs actually help agents succeed at embodied tasks?*
To address this gap, we introduce WoW!, the first open platform that benchmarks WMs in a closed-loop setting that mirrors real agent-environment interactions. WoW! provides a unified online planning strategy and a standardized action API, enabling heterogeneous WMs for decision making.
We curate four closed-loop environments that rigorously evaluate diverse WMs, prioritize task success as the primary metric, and move beyond the common focus on visual quality; we also present the first data scaling law for world models in embodied settings.
Our study uncovers three surprises: (1) visual quality alone does not guarantee task success—controllability matters more; (2) scaling post-training with action-observation data is more effective than upgrading the pretrained video generators; and (3) allocating more inference-time compute allows WMs to substantially improve closed-loop performance. By centering evaluation on closed-loop outcomes, WoW! establishes a new benchmark for the systematic assessment of WMs.

## One-Sentence Claim

WoW! benchmarks generative world models in closed-loop embodied settings, showing that controllability, action-observation post-training, and inference-time compute matter more for task success than visual quality alone.

## Problem

World models are often evaluated open-loop, emphasizing visual realism or prediction quality without testing whether they help agents act successfully. This leaves the embodied-utility question unresolved: a visually impressive model may be useless if it cannot support control.

## Core Contribution

The paper introduces WoW!, an open closed-loop benchmark platform for world models. It provides a unified online planning strategy, standardized action API, four environments, task-success-centered metrics, and the first reported data scaling law for world models in embodied settings.

## Method

WoW! connects heterogeneous world models to online planning through a shared action API, then evaluates them through agent-environment interaction rather than offline video prediction. The benchmark curates environments that test whether generated futures improve decisions.

## Experiments and Evidence

The abstract reports three main findings: visual quality does not guarantee task success, controllability matters more; scaling post-training with action-observation data is more effective than upgrading pretrained video generators; and additional inference-time compute improves closed-loop performance. It also reports a data scaling law for embodied world models.

## Limits and Failure Modes

This note is abstract/metadata-only. Full-text review should inspect the four environments, planning algorithm, action API abstraction, compute budgets, model set, and whether task success correlates with real embodied deployment. Closed-loop benchmarks can still be narrow if environments reward short-horizon controllability over broader world understanding.

## Deep Themes

- Closed-loop evaluation for world models.
- Embodied utility over visual realism.
- Controllability as a central generative-model property.
- Test-time compute for planning.

## Subthemes

- Video generation for agents.
- Action-observation post-training.
- Online planning.
- Standardized action API.
- World-model scaling laws.

## Connections to Other Papers

Connects to PhyWorldBench through evaluation beyond perceptual quality, to Visual Planning through planning over visual futures, to MotionStream through long video generation constraints, and to ScaleCUA/RedTeamCUA through closed-loop agent evaluation.

## Notes for Cross-Paper Synthesis

WoW! is a strong evidence point for evaluation reform: generative models should be judged by whether their outputs support downstream decisions. The broader pattern is movement from static realism to interactive usefulness.
