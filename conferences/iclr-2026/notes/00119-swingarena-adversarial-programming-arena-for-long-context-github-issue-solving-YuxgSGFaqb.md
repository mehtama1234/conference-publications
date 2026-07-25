# SWINGARENA: Adversarial Programming Arena for Long-context GitHub Issue Solving

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: YuxgSGFaqb
- Authors: Wendong XU; Jing Xiong; Chenyang Zhao; Qiujiang Chen; Haoran Wang; Hui Shen; Zhongwei Wan; Jianbo Dai; Taiqiang Wu; He Xiao; Chaofan Tao; Zhuoqing Mao; Ying Sheng; Zhijiang Guo; Hongxia Yang; Bei Yu; Lingpeng Kong; Quanquan Gu; Ngai Wong
- Primary area: applications to computer vision, audio, language, and other modalities
- Keywords: Arena;Real-World GitHub Issues;Adversarial Programming;Retrieval-Augmented Generation;Continuous Integration;Code Benchmark
- Source URL: https://openreview.net/forum?id=YuxgSGFaqb
- PDF URL: https://openreview.net/pdf?id=YuxgSGFaqb

## Abstract

We present \textsc{SwingArena}, a adversarial evaluation framework for Large Language Models (LLMs) that closely mirrors real-world software development workflows. Unlike traditional static benchmarks, \textsc{SwingArena} models the collaborative process of software iteration by pairing LLMs as \textit{submitters}, who generate patches, and \textit{reviewers}, who create test cases and verify the patches through continuous integration (CI) pipelines. To support these interactive evaluations, we introduce a retrieval-augmented code generation (RACG) module that efficiently handles long-context challenges by providing syntactically and semantically relevant code snippets from large codebases, supporting multiple programming languages (C++, Python, Rust, and Go). This enables the framework to scale across diverse tasks and contexts while respecting token limitations. Our experiments, using over 400 high-quality real-world GitHub issues selected from a pool of 2,300 issues, show that models like GPT-4o excel at aggressive patch generation, whereas DeepSeek and Gemini prioritize correctness in CI validation. \textsc{SwingArena} presents a scalable and extensible methodology for evaluating LLMs in realistic, CI-driven software development settings. The complete codebase and benchmark are submitted in https://anonymous.4open.science/r/Swing-Bench and will be open-sourced after the anonymity period.

## One-Sentence Claim

SwingArena evaluates LLM software agents through adversarial submitter-reviewer interactions on real GitHub issues with retrieval-augmented code context and CI validation.

## Problem

Static coding benchmarks do not fully capture real software development, where patches are reviewed, tests are created, codebases are large, and continuous integration determines whether changes work.

Long-context codebases also exceed token limits, requiring retrieval mechanisms that surface relevant snippets across languages.

## Core Contribution

The paper introduces SwingArena, an adversarial programming evaluation framework.

It pairs LLM submitters that generate patches with LLM reviewers that create tests and verify patches through CI pipelines, supported by a retrieval-augmented code generation module.

## Method

SwingArena selects real GitHub issues and evaluates agents in an iterative workflow resembling collaborative software development.

Its RACG module retrieves syntactically and semantically relevant code snippets from large codebases in C++, Python, Rust, and Go to handle long-context constraints.

## Experiments and Evidence

The abstract reports experiments on more than 400 high-quality real GitHub issues selected from 2,300 candidates.

GPT-4o is described as strong at aggressive patch generation, while DeepSeek and Gemini prioritize correctness in CI validation. The benchmark is designed to be scalable and extensible.

## Limits and Failure Modes

LLM-generated reviewer tests may be incomplete or adversarially biased, and CI pass rates can miss maintainability or hidden requirements. Real-issue selection may also shape model rankings.

Because this note is abstract-only, details still need checking: issue filtering, reviewer protocol, CI setup, retrieval metrics, language distribution, scoring, and leakage controls.

## Deep Themes

- Adversarial coding evaluation: patch generation and review become interacting roles.
- CI-grounded verification: software-agent evaluation moves closer to real development workflows.
- Retrieval for long codebases: code agents need semantically precise context selection under token limits.
- Model behavior tradeoffs: aggressive patching and conservative validation reflect different coding-agent styles.

## Subthemes

- GitHub issue solving.
- Submitter-reviewer arena.
- Retrieval-augmented code generation.
- Continuous integration evaluation.

## Connections to Other Papers

This connects to HGM, RefineStat, SparseRL, WebDevJudge, MEnvAgent, and AlgoVeri through program generation and verification.

It also relates to AstaBench because both evaluate agents in realistic tool-mediated workflows.

## Notes for Cross-Paper Synthesis

SwingArena adds a software-agent evaluation theme: realistic coding benchmarks need review, retrieval, and CI, not just one-shot patch generation.
