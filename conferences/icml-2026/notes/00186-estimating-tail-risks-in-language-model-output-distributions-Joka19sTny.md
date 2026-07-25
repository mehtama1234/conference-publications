# Estimating Tail Risks in Language Model Output Distributions

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: Joka19sTny
- Authors: Rico Angell; Raghav Singhal; Zachary Horvitz; Zhou Yu; Rajesh Ranganath; Kathleen McKeown; He He
- Primary area: social_aspects->safety
- Keywords: Language modeling;Safety;Risk Estimation;Rare-event Estimation;Alignment
- Source URL: https://openreview.net/forum?id=Joka19sTny
- PDF URL: https://openreview.net/pdf?id=Joka19sTny

## Abstract

Language models are increasingly capable and are being rapidly deployed on a population-level scale. As a result, the safety of these models is increasingly high-stakes. Fortunately, advances in alignment have significantly reduced the likelihood of harmful model outputs. However, when models are queried billions of times in a day, even rare worst-case behaviors will occur. Current safety evaluations focus on capturing the distribution of inputs that yield harmful outputs. These evaluations disregard the probabilistic nature of models and their tail output behavior. To measure this tail risk, we propose a method to efficiently estimate the probability of harmful outputs for any input query. Instead of naive brute-force sampling from the target model, where harmful outputs could be rare, we operationalize importance sampling by creating unsafe versions of the target model. These unsafe versions enable sample-efficient estimation by making harmful outputs more probable. On benchmarks measuring misuse and misalignment, these estimates match brute-force Monte Carlo estimates using 10–20× fewer samples. For example, we can estimate probability of harmful outputs on the order of $10^{−4}$ with just 500 samples. Additionally, we find that these harmfulness estimates can reveal the sensitivity of models to perturbations in model input and predict deployment risks. Our work demonstrates that rare-event estimation is both critical and feasible for safety evaluations.

## One-Sentence Claim

The paper estimates rare harmful-output probabilities for LLMs using importance sampling from deliberately unsafe model variants, reducing the sample cost of tail-risk evaluation.

## Problem

At population-scale deployment, very rare harmful outputs can still occur frequently, but standard safety evaluations focus on harmful prompts and ignore probabilistic tail behavior over model outputs.

## Core Contribution

The paper operationalizes rare-event estimation for LLM safety by constructing unsafe versions of a target model that make harmful completions more likely and enable sample-efficient probability estimation for each input query.

## Method

Instead of brute-force sampling from the aligned target model, the method samples from unsafe proposal models and uses importance sampling to estimate the target model's probability of harmful outputs.

## Experiments and Evidence

The abstract reports matching brute-force Monte Carlo estimates on misuse and misalignment benchmarks with 10-20x fewer samples, including estimating harmful-output probabilities around 1e-4 with 500 samples. It also claims the estimates reveal input-perturbation sensitivity and predict deployment risks.

## Limits and Failure Modes

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: unsafe-model construction, importance weights, variance diagnostics, harmfulness classifier reliability, benchmark coverage, and whether proposal mismatch biases estimates.

## Deep Themes

- Safety evaluation must measure output-distribution tails, not only average prompt success rates.
- Rare-event estimation is becoming operationally important for high-volume LLM deployment.
- Deliberately unsafe variants can serve as statistical instruments for aligned-model risk.

## Subthemes

- Language-model safety.
- Tail-risk estimation.
- Importance sampling.
- Misuse and misalignment.
- Rare harmful completions.
- Deployment-scale risk prediction.

## Connections to Other Papers

Connects to FlowGuard, Copyright-Bench, and jailbreak/safety evaluation papers through distributional risk measurement. It also links to Prescriptive Scaling and ATLAS through more refined evaluation methodology.

## Notes for Cross-Paper Synthesis

This paper adds a rare-event lens to the safety theme: when models run billions of times, the tail of the output distribution becomes a central deployment object.
