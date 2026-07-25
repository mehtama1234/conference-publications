# WebDevJudge: Evaluating (M)LLMs as Critiques for Web Development Quality

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: CCSPm6V5EF
- Authors: Chunyang Li; Yilun Zheng; Xinting Huang; Tianqing Fang; Jiahao Xu; Lihui Chen; Yangqiu Song; Han Hu
- Primary area: datasets and benchmarks
- Keywords: large language models;evaluation;LLM-as-a-judge;benchmark
- Source URL: https://openreview.net/forum?id=CCSPm6V5EF
- PDF URL: https://openreview.net/pdf?id=CCSPm6V5EF

## Abstract

The paradigm of LLM-as-a-judge is emerging as a scalable and efficient alternative to human evaluation, demonstrating strong performance on well-defined tasks. However, its reliability in open-ended tasks with dynamic environments and complex interactions remains unexplored. To bridge the gap, we introduce WebDevJudge, a systematic benchmark for assessing LLM-as-a-judge performance in web development, with support for both non-interactive evaluation based on static observations and continuous interactive evaluation with a dynamic web environment. WebDevJudge comprises human preference labels over paired web implementations, annotated with structured and query-grounded rubrics to ensure high-quality ground truth. Using this benchmark, we comprehensively evaluate various evaluators, including LLMs, MLLMs, and agentic workflows. We systematically investigate the impact of different paradigms and guidance mechanisms. Our experiments reveal a significant gap between LLM judges and human experts. In-depth analysis indicates this gap stems from fundamental model limitations, including failures in recognizing functional equivalence, verifying task feasibility, and mitigating bias. Overall, WebDevJudge presents a significant challenge to LLM-as-a-judge, offering insights to guide future research toward developing more reliable and capable automated evaluators for complicated scenarios.

## One-Sentence Claim

WebDevJudge shows LLM and MLLM judges still fall short of human experts when evaluating open-ended web development quality in static and interactive environments.

## Problem

LLM-as-a-judge works well on some well-defined tasks, but web development evaluation is open-ended, interactive, and involves functional correctness, feasibility, usability, and visual quality.

The reliability of automated judges in dynamic web environments remains underexplored.

## Core Contribution

The paper introduces WebDevJudge, a benchmark for assessing LLM-as-a-judge performance on web development quality.

It supports non-interactive evaluation from static observations and continuous interactive evaluation in a dynamic web environment, using human preference labels over paired web implementations with structured query-grounded rubrics.

## Method

WebDevJudge collects paired web implementations and human preferences. Rubrics are structured and grounded in queries to provide high-quality labels.

The benchmark evaluates LLMs, MLLMs, and agentic judge workflows under different paradigms and guidance mechanisms.

## Experiments and Evidence

The abstract reports a significant gap between LLM judges and human experts.

Analysis attributes the gap to failures in recognizing functional equivalence, verifying task feasibility, and mitigating bias.

## Limits and Failure Modes

Human preference labels in web development can be subjective, and dynamic environments may introduce nondeterminism. Automated judges may also be sensitive to screenshot quality or interaction policy.

Because this note is abstract-only, details still need checking: benchmark size, task distribution, rubric design, interactive protocol, judge prompting, agreement rates, and examples of functional-equivalence failures.

## Deep Themes

- Evaluating evaluators: LLM-as-a-judge must itself be benchmarked in realistic workflows.
- Interactive task assessment: web quality cannot be reduced to static text answers.
- Functional equivalence and feasibility: judges need execution-aware reasoning, not surface comparison.
- Bias in automated critique: scalable judges can systematically diverge from expert preferences.

## Subthemes

- Static versus interactive web evaluation.
- MLLM and agentic judge workflows.
- Query-grounded rubrics.
- Human preference labels.

## Connections to Other Papers

This connects to FRABench/UFEval, CounselBench, Gaia2, and MiniAppBench through evaluation realism and judge reliability.

It also relates to agent benchmarks because web development quality often requires tool use, interaction, and state inspection.

## Notes for Cross-Paper Synthesis

WebDevJudge strengthens the evaluation realism theme: automated judges need dynamic task understanding, not just fluent critique.
