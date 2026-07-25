# EditBench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: FtL9eEmU6v
- Authors: Wayne Chi; Valerie Chen; Ryan Shar; Aditya Mittal; Jenny Liang; Wei-Lin Chiang; Anastasios Nikolas Angelopoulos; Ion Stoica; Graham Neubig; Ameet Talwalkar; Chris Donahue
- Primary area: datasets and benchmarks
- Keywords: code;real-world;llm;code edit;edit
- Source URL: https://openreview.net/forum?id=FtL9eEmU6v
- PDF URL: https://openreview.net/pdf?id=FtL9eEmU6v

## Abstract

Instructed code editing, where LLMs directly modify a developer's existing code based on a user instruction, is becoming a widely used interaction mode in AI coding assistants. However, few benchmarks directly evaluate this capability and current datasets often rely on artificial sources. We introduce EditBench, a benchmark for evaluating LLM code editing capabilities  grounded in real-world usage, i.e.,~user instructions and code contexts collected in the wild.  EditBench comprises of 545 problems, multiple natural and programming languages, and a diverse set of real-world use cases, ranging from resolving errors to adding features. EditBench introduces context-dependent problems that require the model to understand code context, highlighted code, and cursor position in addition to the user instruction. We evaluate 40 diverse LLMs and observe that EditBench is a challenging set of problems where only 3 models score over 60\%. We find that model performance varies across different categories of user instructions. Further, we find that varying levels of contextual information greatly affect task success rate, with performance varying up to 11\%, indicating the importance of evaluating with realistic context.

## One-Sentence Claim

EditBench evaluates real-world instructed code editing with realistic code context, highlighted regions, cursor position, and user instructions collected in the wild.

## Problem

AI coding assistants increasingly edit existing code directly from user instructions, but few benchmarks test this interaction mode with realistic code contexts.

Many existing code-edit benchmarks rely on artificial tasks and do not capture the contextual signals developers provide, such as highlighted code or cursor position.

## Core Contribution

The paper introduces EditBench, a real-world instructed code-editing benchmark with 545 problems.

It covers multiple natural and programming languages and diverse use cases such as fixing errors and adding features, while explicitly testing context-dependent editing.

## Method

EditBench collects user instructions and code contexts from real-world usage. Problems include the instruction, surrounding code, highlighted code, and cursor position where relevant.

The benchmark evaluates 40 LLMs and analyzes performance across instruction categories and context-availability conditions.

## Experiments and Evidence

The abstract reports that EditBench is challenging: only 3 of 40 evaluated models score above 60 percent.

Performance varies by instruction category, and changing contextual information shifts success by up to 11 percent, demonstrating the importance of realistic context.

## Limits and Failure Modes

Real-world collected contexts may include private or distribution-specific patterns, and benchmark scoring may be hard if multiple edits are valid.

Because this note is abstract-only, details still need checking: data collection source, privacy filtering, evaluation harness, pass/fail criteria, language distribution, and how partial correctness is handled.

## Deep Themes

- Realistic coding-assistant evaluation: code editing is not the same as standalone code generation.
- Context as task input: highlighted regions and cursor position materially affect success.
- Interaction-mode specificity: benchmarks should match how users actually invoke tools.
- Model capability heterogeneity: performance depends strongly on instruction type.

## Subthemes

- Instructed code edits.
- Wild user instructions.
- Cursor and highlight context.
- Multi-language code editing.

## Connections to Other Papers

This connects to WebDevJudge, Gaia2, MiniAppBench, and CyberGym through realistic agent/coding evaluation.

It also relates to VERINA and code-generation benchmarks because code ability must be tested in execution-like workflows, not only static completions.

## Notes for Cross-Paper Synthesis

EditBench strengthens the real-workflow benchmark theme: coding assistants need evaluation on context-sensitive edits, not just greenfield code tasks.
