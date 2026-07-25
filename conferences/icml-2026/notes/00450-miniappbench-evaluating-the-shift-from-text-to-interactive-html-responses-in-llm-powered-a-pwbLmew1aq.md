# MiniAppBench: Evaluating the Shift from Text to Interactive HTML Responses in LLM-Powered Assistants

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: pwbLmew1aq
- Authors: Zuhao zhang; Chengyue Yu; Yuante Li; Chenyi Zhuang; Linjian Mo; Shuai Li
- Primary area: general_machine_learning->evaluation
- Keywords: Benchmark;LLM Agent;Code Generation
- Source URL: https://openreview.net/forum?id=pwbLmew1aq
- PDF URL: https://openreview.net/pdf?id=pwbLmew1aq

## Abstract

With the rapid advancement of Large Language Models (LLMs) in code generation, human-AI interaction is evolving from static text responses to dynamic, interactive HTML-based applications, which we term **MiniApps**. These applications require models to not only render visual interfaces but also construct customized interaction logic that adheres to real-world principles. However, existing benchmarks primarily focus on algorithmic correctness or static layout reconstruction, failing to capture the capabilities required for this new paradigm. To address this gap, we introduce **MiniAppBench**, the first comprehensive benchmark designed to evaluate principle-driven, interactive application generation. Sourced from a real-world application with **10M+** generations, MiniAppBench distills 500 tasks across six domains (e.g., Games, Science, and Tools). Furthermore, to tackle the challenge of evaluating open-ended interactions where no single ground truth exists, we propose **MiniAppEval**, an agentic evaluation framework. Leveraging browser automation, it performs human-like exploratory testing to systematically assess applications across three dimensions: Intention, Static, and Dynamic. Our experiments reveal that current LLMs still face significant challenges in generating high-quality MiniApps, while MiniAppEval demonstrates high alignment with human judgment, establishing a reliable standard for future research. Our homepage is available in https://miniappbench.github.io.

## One-Sentence Claim

MiniAppBench evaluates LLMs on generating interactive HTML applications, using browser-automation-based agentic evaluation to test intention, static UI quality, and dynamic behavior.

## Problem

LLM assistants are shifting from static text answers toward interactive mini-applications that combine visual UI and custom logic. Existing coding benchmarks usually test algorithmic correctness or static layout reconstruction, but they do not capture whether a generated app behaves according to real-world interaction principles.

The evaluation problem is hard because interactive apps are open-ended. There may be no single ground-truth implementation, so benchmark evaluation must explore behavior rather than compare against one output.

## Core Contribution

MiniAppBench contributes a 500-task benchmark for principle-driven interactive application generation, sourced from a real-world application with more than 10 million generations and spanning six domains including games, science, and tools.

It also introduces MiniAppEval, an agentic evaluation framework that uses browser automation for human-like exploratory testing across intention, static, and dynamic dimensions. The contribution is therefore both dataset and evaluator.

## Method

Tasks are distilled from real-world MiniApp generation data and require models to produce interactive HTML responses. Evaluation is not limited to screenshot similarity or code execution; MiniAppEval drives the app in a browser, explores interactions, and assesses whether the result satisfies user intent, static presentation, and dynamic behavior.

This makes the benchmark closer to how users experience generated applications: an app must render, respond, and preserve intended logic across interaction paths.

## Experiments and Evidence

The abstract reports that current LLMs still face major challenges generating high-quality MiniApps. It also reports that MiniAppEval aligns strongly with human judgment, suggesting that browser-automation evaluation can scale assessment of open-ended interactive artifacts.

Full-paper reading should verify domain/task distribution, model comparisons, evaluator-human agreement statistics, failure categories, and how MiniAppEval avoids overrewarding superficial interactivity.

## Limits and Failure Modes

Agentic app evaluation can miss rare interaction bugs or be biased by the exploration policy. A generated app may pass explored paths while failing untested states, accessibility requirements, security constraints, or responsiveness.

Because tasks come from one real-world application source, coverage may reflect that product's user base and generation patterns. The benchmark may need expansion for enterprise workflows, data-heavy apps, and mobile constraints.

## Deep Themes

- From text generation to artifact generation: LLM outputs are becoming usable software surfaces.
- Evaluation through interaction: correctness requires exercising UI behavior, not only inspecting static code.
- Agentic evaluators for open-ended artifacts: browser automation approximates human exploratory testing.
- Real-world task sourcing: production generation logs can reveal benchmark needs missing from academic tasks.

## Subthemes

- Interactive HTML generation combines UI design, state management, and domain logic.
- Intention/static/dynamic dimensions separate user goal, visual layout, and behavior.
- MiniApps are an intermediate artifact between chat response and full application.
- Human-aligned evaluation is necessary when no single ground truth exists.

## Connections to Other Papers

MiniAppBench connects closely to Vision2Web and MAP. Vision2Web benchmarks visual website development; MAP studies production agents; MiniAppBench targets the emerging interaction pattern where assistants return runnable apps.

It also relates to AlgoVeri and Copyright-Bench-style evaluation work: benchmarks increasingly test artifacts under realistic operational constraints rather than isolated answer strings.

## Notes for Cross-Paper Synthesis

MiniAppBench marks a broader shift in AI evaluation from generated text to generated tools. The common pattern is that evaluation must become embodied in the artifact's runtime environment: browser, verifier, simulator, or workflow.
