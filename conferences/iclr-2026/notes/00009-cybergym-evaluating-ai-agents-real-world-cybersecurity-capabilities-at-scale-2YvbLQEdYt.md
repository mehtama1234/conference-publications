# CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities at Scale

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 2YvbLQEdYt
- Authors: Zhun Wang; Tianneng Shi; Jingxuan He; Matthew Cai; Jialin Zhang; Dawn Song
- Primary area: datasets and benchmarks
- Keywords: Cybersecurity;AI;Agents
- Source URL: https://openreview.net/forum?id=2YvbLQEdYt
- PDF URL: https://openreview.net/pdf?id=2YvbLQEdYt

## Abstract

AI agents have significant potential to reshape cybersecurity, making a thorough assessment of their capabilities critical.
However, existing evaluations fall short, because they are based on small-scale benchmarks and only measure static outcomes, failing to capture the full, dynamic range of real-world security challenges.
To address these limitations, we introduce CyberGym, a large-scale benchmark featuring 1,507 real-world vulnerabilities across 188 software projects.
Adjustable to different vulnerability analysis settings, CyberGym primarily tasks agents with generating a proof-of-concept test that reproduces a vulnerability, given only its text description and the corresponding codebase.
Our extensive evaluation highlights that CyberGym effectively differentiates agents' and models' cybersecurity capabilities.
Even the top-performing combinations only achieve a ~20% success rate, demonstrating the overall difficulty of CyberGym. 
Beyond static benchmarking, we show that CyberGym leads to the discovery of 35 zero-day vulnerabilities and 17 historically incomplete patches.
These results underscore that CyberGym is not only a robust benchmark for measuring AI's progress in cybersecurity but also a platform for creating direct, real-world security impact.

## One-Sentence Claim

CyberGym is a large-scale real-world cybersecurity benchmark showing that current AI agents remain weak at reproducing vulnerabilities from descriptions and codebases, while also enabling discovery of new vulnerabilities and incomplete patches.

## Problem

Cybersecurity agents are increasingly plausible, but existing evaluations are too small and static to capture real vulnerability-analysis workflows or differentiate practical agent capability.

## Core Contribution

The paper introduces CyberGym, a benchmark of 1,507 real vulnerabilities from 188 software projects, primarily asking agents to generate proof-of-concept tests that reproduce vulnerabilities from natural-language descriptions and codebases.

## Method

CyberGym converts real vulnerability cases into dynamic agent tasks. Agents operate over codebases and must produce executable proof-of-concept tests. The benchmark supports different vulnerability-analysis settings rather than a single static classification-style evaluation.

## Experiments and Evidence

The abstract reports that top-performing agent/model combinations reach only about 20% success. It also reports that CyberGym led to discovery of 35 zero-day vulnerabilities and 17 historically incomplete patches.

## Limits and Failure Modes

PDF checks needed: project/language distribution, sandboxing and safety controls, whether success requires exploitability or test reproduction only, and how much benchmark leakage risk exists from public vulnerability data.

## Deep Themes

- Agent evaluation is moving toward realistic dynamic environments.
- Security benchmarks can become operational tools, not only measurement artifacts.
- Real-world impact and evaluation are increasingly intertwined.

## Subthemes

- Cybersecurity agents.
- Vulnerability reproduction.
- Proof-of-concept generation.
- Dynamic benchmark environments.
- Zero-day discovery.

## Connections to Other Papers

Connects to RAGEN-2, CounselBench, and other agent/evaluation papers. It is also part of the broader safety/security cluster because improved agent capability can both defend and attack.

## Notes for Cross-Paper Synthesis

CyberGym strengthens the theme that benchmark design is shifting from static answer checking toward real task environments where models interact with artifacts, tools, and constraints.

## Full-Text Upgrade

Source used: `conferences/iclr-2026/text/00009-cybergym-evaluating-ai-agents-real-world-cybersecurity-capabilities-at-scale-2YvbLQEdYt-arxiv.txt`.

Additional verified details:

- CyberGym validates generated PoCs by executing them on both pre-patch and post-patch versions.
- The benchmark is modular and containerized for reproducible/extensible evaluation.
- The full text reports evaluation of four agent frameworks and eleven frontier LLMs.
- The best result reported in the introduction is Claude 4 Opus with a 17.9% success rate, rising to 22.0% when "thinking" is enabled.
- Specialized software-engineering models generalize poorly to CyberGym, with success rates at or below 2.0%, showing that security tasks differ from general SWE-bench-style issue fixing.
- The full text says CyberGym focuses on memory-safety vulnerabilities, mainly in C/C++ projects, because sanitizer/oracle infrastructure is mature there.
- The zero-day/incomplete-patch counts differ slightly between abstract metadata and the extracted arXiv text. The arXiv text reports 34 zero-days and 18 incomplete historical patches, with 4 CVE assignments and 10 patched at writing.

Refined limits:

- Scope is centered on memory-safety vulnerabilities and therefore does not cover the full cybersecurity landscape.
- The evaluation depends on runnable project containers and sanitizer-style vulnerability oracles.
