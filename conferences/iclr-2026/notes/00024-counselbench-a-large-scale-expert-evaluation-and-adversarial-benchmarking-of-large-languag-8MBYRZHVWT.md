# CounselBench: A Large-Scale Expert Evaluation and Adversarial Benchmarking of Large Language Models in Mental Health Question Answering

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: 8MBYRZHVWT
- Authors: Yahan Li; Jifan Yao; John Bosco S. Bunyi; Adam C Frank; Angel Hsing-Chi Hwang; Ruishan Liu
- Primary area: datasets and benchmarks
- Keywords: large language models;mental health;human evaluation
- Source URL: https://openreview.net/forum?id=8MBYRZHVWT
- PDF URL: https://openreview.net/pdf?id=8MBYRZHVWT

## Abstract

Medical question answering (QA) benchmarks often focus on multiple-choice or fact-based tasks, leaving open-ended answers to real patient questions underexplored. This gap is particularly critical in mental health, where patient questions often mix symptoms, treatment concerns, and emotional needs, requiring answers that balance clinical caution with contextual sensitivity.
We present CounselBench, a large-scale benchmark developed with 100 mental health professionals to evaluate and stress-test large language models (LLMs) in realistic help-seeking scenarios. The first component, CounselBench-EVAL, contains 2,000 expert evaluations of answers from GPT-4, LLaMA 3, Gemini, and online human therapists on patient questions from the public forum CounselChat. Each answer is rated across six clinically grounded dimensions, with span-level annotations and written rationales. Expert evaluations show that while LLMs achieve high scores on several dimensions, they also exhibit recurring issues, including unconstructive feedback, overgeneralization, and limited personalization or relevance. Responses were frequently flagged for safety risks, most notably unauthorized medical advice. Follow-up experiments show that LLM judges systematically overrate model responses and overlook safety concerns identified by human experts. To probe failure modes more directly, we construct CounselBench-Adv, an adversarial dataset of 120 expert-authored mental health questions designed to trigger specific model issues. Expert evaluation of 1,080 responses from nine LLMs reveals consistent, model-specific failure patterns. Together, CounselBench establishes a clinically grounded framework for benchmarking LLMs in mental health QA.

## One-Sentence Claim

CounselBench provides expert-grounded and adversarial mental-health QA evaluation showing that LLMs and LLM judges miss clinically important safety and personalization failures.

## Problem

Medical QA benchmarks often use multiple-choice or fact-based questions, but mental-health help-seeking is open-ended and blends symptoms, treatment concerns, emotional needs, and safety risks.

The problem is that realistic mental-health answers require clinical caution, contextual sensitivity, personalization, and avoidance of unauthorized medical advice, which generic benchmarks and model judges may not catch.

## Core Contribution

The paper introduces CounselBench, developed with 100 mental-health professionals. It has two components: CounselBench-EVAL for expert evaluation of real patient-question answers, and CounselBench-Adv for adversarial stress testing.

The benchmark provides six clinically grounded dimensions, span-level annotations, written rationales, and expert-authored adversarial questions designed to trigger specific failure modes.

## Method

CounselBench-EVAL uses patient questions from CounselChat and collects 2,000 expert evaluations of answers from GPT-4, LLaMA 3, Gemini, and online human therapists.

CounselBench-Adv contains 120 expert-authored mental-health questions. The paper evaluates 1,080 responses from nine LLMs to identify model-specific failure patterns.

## Experiments and Evidence

The abstract reports that LLMs score highly on some dimensions but show recurring issues including unconstructive feedback, overgeneralization, limited personalization, limited relevance, and safety risks.

Unauthorized medical advice is highlighted as a major risk. Follow-up experiments show LLM judges systematically overrate model responses and miss expert-identified safety concerns.

## Limits and Failure Modes

Mental-health evaluation is culturally and clinically sensitive; benchmarks may not cover crisis contexts, local regulations, or the full diversity of patient needs.

Because this note is abstract-only, details still need checking: six dimensions, expert recruitment, inter-rater agreement, patient-question filtering, therapist baseline quality, adversarial taxonomy, and crisis-response handling.

## Deep Themes

- Expert-grounded safety evaluation: clinical domains require domain professionals, not only automated judges.
- Open-ended medical QA risk: answer quality depends on caution, empathy, personalization, and relevance.
- LLM judge blind spots: model-based evaluators can miss safety concerns that experts catch.
- Adversarial healthcare benchmarking: stress tests reveal model-specific failure modes.

## Subthemes

- Mental-health QA.
- Span-level expert annotations.
- Unauthorized medical advice.
- LLM-as-judge overrating.

## Connections to Other Papers

This connects to FRABench/UFEval through fine-grained evaluation, but CounselBench shows why expert evaluation is essential in high-stakes domains.

It also connects to Copyright-Bench, MiniAppBench, and safety benchmark papers because realistic task settings expose failures hidden by simpler evaluations.

## Notes for Cross-Paper Synthesis

CounselBench is a high-stakes evaluation anchor: when domain risk is severe, generic helpfulness and automated judging are insufficient.
