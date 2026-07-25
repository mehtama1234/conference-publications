# Pressure Reveals Character: Behavioural Alignment Evaluation at Depth

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 3U1l24EDvL
- Authors: Nora Petrova; John Burden
- Primary area: social_aspects->alignment
- Keywords: Alignment;Evaluation;Safety;Leaderboard;Human-Calibration;AI as Judge
- Source URL: https://openreview.net/forum?id=3U1l24EDvL
- PDF URL: https://openreview.net/pdf?id=3U1l24EDvL

## Abstract

Evaluating alignment in language models requires testing how they behave under realistic pressure, not just what they claim they would do. While alignment failures increasingly cause real-world harm, comprehensive evaluation frameworks with realistic multi-turn scenarios remain lacking. We introduce an alignment benchmark spanning 904 scenarios across six categories---Honesty, Safety, Non-Manipulation, Robustness, Corrigibility, and Scheming---validated as realistic by human raters. Our scenarios place models under conflicting instructions, simulated tool access, and multi-turn escalation to reveal behavioral tendencies that single-turn evaluations miss. Evaluating 24 frontier models using LLM judges validated against human annotations, we find that even top-performing models exhibit gaps in specific categories, while the majority of models show consistent weaknesses across the board. Factor analysis reveals that alignment behaves as a unified construct (analogous to the g-factor in cognitive research) with models scoring high on one category tending to score high on others. We publicly release the benchmark and an interactive leaderboard to support ongoing evaluation, with plans to expand scenarios in areas where we observe persistent weaknesses and to add new models as they are released.

## One-Sentence Claim

Alignment evaluation should pressure-test models in realistic multi-turn scenarios because behavioral failures appear under conflict, escalation, and simulated tool access that single-turn tests miss.

## Problem

Many alignment evaluations measure stated preferences or isolated answers, but real failures occur when models face pressure, conflicting instructions, adversarial input, tool-like affordances, or escalating multi-turn situations.

## Core Contribution

The paper introduces a 904-scenario alignment benchmark across Honesty, Safety, Non-Manipulation, Robustness, Corrigibility, and Scheming, plus a validated LLM-judge evaluation pipeline and leaderboard.

## Method

Scenarios are constructed as realistic multi-turn interactions with trigger conditions, conflicting pressures, and pass/fail criteria. The authors evaluate 24 frontier models using an LLM judge calibrated against human annotations.

## Experiments and Evidence

The abstract reports category-specific gaps even among top models, broad weaknesses among most models, and factor-analysis evidence that alignment behaves like a unified construct across categories.

## Full-Text Upgrade

The full text gives the category breakdown: Honesty 217 scenarios, Safety 104, Non-Manipulation 239, Robustness 75, Corrigibility 103, and Scheming 166, totaling 904. The benchmark includes scenarios such as credential pressure, boundary erosion, self-preservation, tool-use safety, and long-horizon sabotage.

The LLM judge is not used without validation. The paper reports a calibration study with 100 specialized AI participants, mean absolute error around 0.65 points on a five-point scale, about 70% human-AI category agreement for pass/fail decisions, and F1 around 0.69 for problematic-behavior selections. Results suggest Non-Manipulation and Robustness are especially difficult categories, while factor analysis supports a general alignment factor but with meaningful category-specific weaknesses.

## Limits and Failure Modes

Limits to watch: factor-analysis conclusions are preliminary for a benchmark of this size; LLM-judge reasoning does not perfectly match human reasoning; generated scenarios may miss important real-world pressures; and leaderboard results can shift as models and judging standards change.

## Deep Themes

- Alignment is behavioral under pressure, not merely verbal under normal prompting.
- Multi-turn evaluation reveals failures hidden by single-turn benchmarks.
- Alignment categories may share a common latent factor while retaining specific failure modes.

## Subthemes

- Behavioral alignment.
- Multi-turn pressure tests.
- LLM judges.
- Human calibration.
- Scheming and corrigibility.
- Interactive leaderboards.

## Connections to Other Papers

Connects to Rare Event Analysis, SandboxEscapeBench, CyberGym, Invisible Safety Threat, and RAGEN-2 through evaluation of hard-to-observe or interaction-dependent failures.

## Notes for Cross-Paper Synthesis

This paper strengthens the evaluation theme: future alignment measurement is moving from static answer scoring toward pressure-rich interaction traces with explicit behavioral criteria.
