# Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: jfOhTGs5G5
- Authors: Jiahao Li; Qingwang Zhang; Qiuyu Chen; Guozhan Qiu; Yunzhong Lou; Xiangdong Zhou
- Primary area: applications->computer_vision
- Keywords: Text-to-CAD;CAD generation;Parametric CAD Modeling;B-Rep;Large Language Models;Reinforcement Learning;B-Rep Grounding
- Source URL: https://openreview.net/forum?id=jfOhTGs5G5
- PDF URL: https://openreview.net/pdf?id=jfOhTGs5G5

## Abstract

The field of Computer-Aided Design (CAD) generation has made significant progress in recent years.
Existing methods typically fall into two separate categories: parametric CAD modeling and direct boundary representation (B-Rep) synthesis.
In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., *fillet* and *chamfer*) require explicit selection of B-Rep geometric primitives, and the B-Rep itself is derived from parametric operations.
Consequently, this paradigm gap remains a critical factor limiting AI-driven CAD modeling for complex industrial product design.
This paper presents *FutureCAD*, a novel text-to-CAD framework that leverages large language models (LLMs) and a B-Rep grounding transformer (*BRepGround*) for high-fidelity CAD generation.
Our method generates executable CadQuery scripts, and introduces a text-based query mechanism that enables the LLM to specify geometric selections via natural language, which *BRepGround* then grounds to the target primitives.
To train our framework, we construct a new dataset comprising real-world CAD models.
For the LLM, we apply supervised fine-tuning (SFT) to establish fundamental CAD generation capabilities, followed by reinforcement learning (RL) to improve generalization.
Experiments show that *FutureCAD* achieves state-of-the-art CAD generation performance.
Code and dataset are available at https://github.com/JohanStackk/FutureCAD.

## One-Sentence Claim

FutureCAD combines LLM-generated CadQuery programs with text-grounded B-Rep primitive selection to produce higher-fidelity feature-based CAD models.

## Problem

AI CAD generation is split between parametric program generation and direct B-Rep synthesis, but real feature-based CAD systems intertwine both. Operations like fillet and chamfer require selecting B-Rep primitives created by earlier parametric steps.

The gap is that LLMs can generate scripts, but complex CAD modeling requires grounded references to geometric primitives inside the evolving B-Rep.

## Core Contribution

The paper introduces FutureCAD, a text-to-CAD framework using LLM-driven CadQuery script generation plus BRepGround, a grounding Transformer that maps natural-language primitive selections to target B-Rep geometry.

It constructs a real-world CAD dataset, trains the LLM with SFT for core generation, then uses RL to improve generalization. Experiments report state-of-the-art CAD generation performance.

## Method

FutureCAD lets the LLM express geometric selections in natural language inside executable CadQuery scripts. BRepGround resolves those textual queries to concrete B-Rep primitives, enabling advanced operations requiring explicit geometric selection.

The training pipeline first teaches basic CAD program generation through supervised fine-tuning, then optimizes generalization with reinforcement learning.

## Experiments and Evidence

Evidence reported in the abstract:

- Executable CadQuery script generation.
- Text-based query mechanism for geometric primitive selection.
- BRepGround Transformer grounding text queries to B-Rep primitives.
- New dataset of real-world CAD models.
- SFT followed by RL for the LLM.
- State-of-the-art CAD generation performance.
- Code and dataset released at the listed GitHub URL.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit/service failures. Details still need checking: dataset size, evaluation metrics, RL reward, and failure cases in grounding.

## Limits and Failure Modes

- Grounding errors can make otherwise valid programs fail.
- Natural-language primitive references may be ambiguous in complex CAD histories.
- RL rewards for CAD fidelity may miss manufacturability or design intent.
- Industrial CAD often needs constraints, assemblies, tolerances, and editability beyond shape fidelity.

## Deep Themes

**Program generation needs geometric grounding.** CAD scripts are only useful if symbolic operations can refer to the right geometry.

**LLMs become interfaces to structured design systems.** The model writes executable programs while a grounding module connects text to B-Rep state.

**Generation quality depends on intermediate references.** The hard part is not only outputting code but maintaining a valid design state.

## Subthemes

- Text-to-CAD.
- CadQuery program generation.
- B-Rep primitive grounding.
- SFT-to-RL CAD training.
- Feature-based parametric modeling.

## Connections to Other Papers

Connects to Formal Problem-Solving, Learning Randomized Reductions, daVinci-Dev, and agentic tool-use papers. It shares the pattern of neural proposal plus executable structured environment.

## Notes for Cross-Paper Synthesis

FutureCAD adds a design-automation variant of the verified/executable generation theme: outputs must be grounded in an external formal geometry system, not just look plausible.
