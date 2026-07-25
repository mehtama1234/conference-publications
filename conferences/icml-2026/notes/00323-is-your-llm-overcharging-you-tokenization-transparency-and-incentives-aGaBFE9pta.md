# Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: aGaBFE9pta
- Authors: Ander Artola Velasco; Stratis Tsirtsis; Nastaran Okati; Manuel Gomez Rodriguez
- Primary area: social_aspects
- Keywords: LLMs;tokenization;mechanism design;incentive compatibility
- Source URL: https://openreview.net/forum?id=aGaBFE9pta
- PDF URL: https://openreview.net/pdf?id=aGaBFE9pta

## Abstract

State-of-the-art large language models require specialized hardware and substantial energy to operate. Consequently, cloud-based services that provide access to these models have become very popular.  In these services, the price users pay depends on the number of tokens a model uses to generate an output–they pay a fixed price per token. 
In this work, we show that this pricing mechanism creates a financial incentive for providers to strategize and misreport the (number of) tokens a model used to generate an output, and users cannot prove, or even know, whether a provider is overcharging them.
However, we also show that, if an unfaithful provider is obliged to be transparent about the generative process used by the model, misreporting optimally without raising suspicion is hard. Nevertheless, as a proof-of-concept, we develop an efficient heuristic algorithm that allows providers to significantly overcharge users without raising suspicion. Crucially, the cost of running the algorithm is lower than the additional revenue from overcharging users, highlighting the vulnerability of users under the current pay-per-token pricing mechanism. Further, we show that, to eliminate the financial incentive to strategize, a pricing mechanism must price tokens linearly on their character count. While this makes a provider's profit margin vary across tokens, we introduce a simple prescription that allows a provider to maintain their average profit margin when transitioning to an incentive-compatible pricing mechanism.
To complement our theoretical results, we conduct experiments with large language models from the $\texttt{Llama}$, $\texttt{Gemma}$ and $\texttt{Ministral}$ families, and prompts from a popular benchmarking platform.

## One-Sentence Claim

Pay-per-token LLM pricing creates incentives for providers to misreport token counts, and incentive-compatible pricing requires charging tokens linearly by character count.

## Problem

Cloud LLM services often charge a fixed price per token, but users cannot easily verify how many tokens a provider actually used to generate an output. This creates a strategic opportunity for providers to overcharge by manipulating or misreporting tokenization/generation details.

The paper asks whether transparency prevents such behavior and what pricing mechanisms remove the incentive to strategize.

## Core Contribution

The paper shows that current pay-per-token pricing is vulnerable: providers have financial incentives to misreport token usage, and users may not be able to prove overcharging. If providers must be transparent about the generative process, optimal misreporting without suspicion becomes hard, but the authors still develop an efficient heuristic that can overcharge significantly without raising suspicion and with lower cost than added revenue.

The paper then shows incentive-compatible pricing must price tokens linearly by character count and gives a prescription for maintaining average profit margin during the transition.

## Method

The method is mechanism design plus empirical proof-of-concept. It models provider incentives under token pricing, analyzes transparency constraints, constructs a heuristic overcharging strategy, and characterizes pricing that removes strategic incentives.

Experiments test the vulnerability on LLMs from Llama, Gemma, and Ministral families and prompts from a benchmarking platform.

## Experiments and Evidence

Evidence reported in the abstract:

- Theoretical analysis of misreporting incentives under fixed per-token pricing.
- Hardness of optimal undetectable misreporting under transparency.
- Efficient heuristic overcharging algorithm whose cost is below added revenue.
- Character-count-linear token pricing as the necessary incentive-compatible mechanism.
- Experiments with Llama, Gemma, and Ministral models and benchmark prompts.

Source depth is abstract/metadata only; arXiv acquisition remains deferred after repeated rate-limit failures. Details still need checking: threat model, transparency definition, detection criterion, pricing proof, and practical billing assumptions.

## Limits and Failure Modes

- Real providers may use audited logs, fixed public tokenizers, or contractual safeguards not visible in the abstract.
- Character-count-linear pricing may complicate margins across languages and scripts.
- The overcharging heuristic may depend on output rewriting freedoms.
- User trust also depends on metering, logs, and third-party verification, not pricing formula alone.

## Deep Themes

**Infrastructure pricing is an incentive system.** Tokenization choices create strategic behavior, not just billing details.

**Transparency helps but may not be sufficient.** Even disclosed generative processes can leave room for profitable manipulation.

**Mechanism design is entering LLM operations.** Pricing must align provider incentives with truthful metering.

## Subthemes

- Pay-per-token vulnerability.
- Token-count misreporting.
- Transparent generation constraints.
- Character-count-linear pricing.
- Provider profit-margin preservation.

## Connections to Other Papers

Connects to Incremental BPE, Data Market Pricing, Bayesian Truthful Valuation, and broader data/model governance papers. It also links to efficiency work because tokenization affects both cost and latency.

## Notes for Cross-Paper Synthesis

This paper broadens the tokenization theme: tokens are not only computational units, but economic units whose definition can create strategic incentives.
