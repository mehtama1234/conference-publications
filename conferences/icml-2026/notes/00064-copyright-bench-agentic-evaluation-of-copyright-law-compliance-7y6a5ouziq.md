# Copyright-Bench: Agentic Evaluation of Copyright Law Compliance

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 7y6a5ouziq
- Authors: Zheng Hui; Doni Bloomfield; Noam Kolt
- Primary area: social_aspects->safety
- Keywords: law;legal compliance;copyright;IP;evaluation;benchmarks;AI safety;AI governance
- Source URL: https://openreview.net/forum?id=7y6a5ouziq
- PDF URL: https://openreview.net/pdf?id=7y6a5ouziq

## Abstract

Large language model (LLM) agents increasingly perform commercial tasks that involve retrieving external content such as images and, where appropriate, reproducing that content. LLM agents should comply with the law, including copyright law. Presently, however, we lack adequate frameworks to assess whether they do so in practice. To that end, we introduce **Copyright-Bench**, a benchmark designed to evaluate *LLM agents' compliance with* *copyright law*. Copyright-Bench is comprised of realistic commercial tasks---website development, merchandise design, and pitch deck production---that involve agents selecting between public-domain content (the use of which is *legal*) and copyrighted content (the use of which is *infringing* in this setting). The evaluation introduces prompt variations that simulate different user preferences, as well as time pressure. Comparing state-of-the-art LLM agents against a human baseline, we find that: (1) agents select copyrighted works despite the availability of public-domain alternatives; and (2) for open-weights models, violation rates increase in response to certain user preferences and simulated time pressure.

## One-Sentence Claim

Copyright-Bench evaluates whether LLM agents performing realistic commercial tasks choose legally usable public-domain content over infringing copyrighted alternatives.

## Problem

LLM agents increasingly retrieve and reuse external content for commercial tasks, but there are few practical benchmarks for whether agents comply with copyright constraints under realistic user pressure.

## Core Contribution

The paper introduces Copyright-Bench, an agentic benchmark covering website development, merchandise design, and pitch deck production tasks with public-domain and copyrighted content choices.

## Method

Tasks require agents to select content where public-domain options are legal and copyrighted options would be infringing in the benchmark setting. Prompt variations simulate user preferences and time pressure, and model behavior is compared with a human baseline.

## Experiments and Evidence

The abstract reports that state-of-the-art LLM agents select copyrighted works despite available public-domain alternatives, and open-weights models show higher violation rates under certain user preferences and simulated time pressure.

## Limits and Failure Modes

No confident local PDF/arXiv match yet. Details still need checking: exact legal scenario construction, scoring rubric, human baseline protocol, jurisdiction assumptions, and whether agent browsing/tooling affects violation rates.

## Deep Themes

- Legal compliance is becoming an agentic safety benchmark.
- Realistic commercial workflows expose risks absent from static legal QA.
- User preferences and time pressure can shift compliance behavior.

## Subthemes

- Copyright compliance.
- Agentic evaluation.
- AI governance.
- Commercial content reuse.
- Public-domain alternatives.
- Time-pressure robustness.

## Connections to Other Papers

Connects to Pressure Reveals Character, CounselBench, and CyberGym through realistic task-based evaluations. It also links to data governance themes such as Common Corpus.

## Notes for Cross-Paper Synthesis

Copyright-Bench broadens the safety/evaluation theme into legal compliance: deployed agents need to make lawful choices in workflows, not merely answer legal questions.
