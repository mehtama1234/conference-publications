# Steering the Herd: A Framework for LLM-based Control of Social Learning

## Metadata

- Conference: iclr-2026
- Status: Oral
- OpenReview ID: RtS4UqSmNt
- Authors: Raghu Arghal; Kevin He; Shirin Saeedi Bidokhti; Saswati Sarkar
- Primary area: alignment, fairness, safety, privacy, and societal considerations
- Keywords: Social learning;LLMs;optimal control;information design;dynamic programming
- Source URL: https://openreview.net/forum?id=RtS4UqSmNt
- PDF URL: https://openreview.net/pdf?id=RtS4UqSmNt

## Abstract

Algorithms increasingly serve as information mediators -- from social media feeds and targeted advertising to the increasing ubiquity of LLMs. This engenders a joint process where agents combine private, algorithmically-mediated signals with observational learning from peers to arrive at decisions. To study such settings, we introduce a model of controlled sequential social learning in which an information-mediating planner (e.g., an LLM) controls the information structure of agents while they also learn from the decisions of earlier agents. The planner may seek to improve social welfare (an altruistic planner) or to induce a specific action the planner prefers (a biased planner). Our framework presents a new optimization problem for social learning that combines dynamic programming with decentralized action choices and Bayesian belief updates. In this setting, we prove the convexity of the value function and characterize the optimal policies of altruistic and biased planners, which attain desired tradeoffs between the costs they incur and the payoffs they earn from induced agent choices. The characterization reveals that the optimal planner operates in different modes depending on the range of belief values. The modes include investing the maximum allowed resource, not investing any resource, or the investment increasing or decreasing with increase in the belief. Notably, for some ranges of belief the biased planner even intentionally obfuscates the agents' signals. Even under stringent transparency constraints—information parity with individuals, no lying or cherry‑picking, and full observability—we show that information mediation can substantially shift social welfare in either direction. We complement our theory with simulations in which LLMs act as both planner and agents. Notably, the LLM-based planner in our simulations exhibits emergent strategic behavior in steering public opinion that broadly mirrors the trends predicted, though key deviations suggest the influence of non-Bayesian reasoning—consistent with the cognitive patterns of both human users and LLMs trained on human-like data. Together, we establish our framework as a tractable basis for studying the impact and regulation of LLM information mediators that corresponds to real behavior.

## One-Sentence Claim

This paper models LLMs as information-mediating planners in sequential social learning and shows they can steer collective decisions even under transparency constraints.

## Problem

Algorithms increasingly mediate information through feeds, ads, recommendations, and LLM responses. Users combine private signals, algorithmically mediated information, and observations of earlier users when making decisions.

The social impact of an information mediator depends on how its signal choices shape downstream belief updates and peer learning, especially when the mediator may be altruistic or biased.

## Core Contribution

The paper introduces a controlled sequential social-learning framework where an information-mediating planner controls agents' information structure while agents also learn from previous decisions.

It characterizes optimal policies for altruistic and biased planners and studies how LLMs behave when placed in planner and agent roles.

## Method

The framework combines dynamic programming, decentralized action choices, and Bayesian belief updates.

The authors prove convexity of the value function and characterize planner modes across belief regions, including maximum investment, no investment, increasing or decreasing investment with belief, and intentional obfuscation by biased planners.

## Experiments and Evidence

The abstract reports theoretical results and simulations where LLMs act as both planner and agents.

Information mediation can shift social welfare in either direction even under strong transparency constraints: information parity, no lying or cherry-picking, and full observability. LLM planner behavior broadly mirrors theoretical trends while showing deviations consistent with non-Bayesian reasoning.

## Limits and Failure Modes

The model abstracts real social networks, platform incentives, heterogeneous users, and repeated interactions. LLM simulation results may depend heavily on prompts, model choice, and how Bayesian beliefs are represented.

Because this note is abstract-only, details still need checking: formal setting, planner cost/payoff functions, transparency constraints, LLM simulation design, and policy-regulation implications.

## Deep Themes

- Information mediation as control: LLMs can shape decisions by choosing information structure, even without lying.
- Social learning under algorithmic signals: individual choices and peer observations form a coupled belief process.
- Biased versus altruistic planners: welfare and manipulation can arise from the same mediation mechanism.
- Regulation beyond truthfulness: transparency constraints may not prevent strategic steering.

## Subthemes

- Sequential social learning.
- Information design.
- Dynamic programming.
- LLM-mediated public opinion.

## Connections to Other Papers

This connects to deception, safety alignment, sycophancy, and social-impact evaluation papers.

It also relates to agentic planning work because the LLM planner optimizes long-horizon outcomes through controlled information release.

## Notes for Cross-Paper Synthesis

This paper expands the safety theme from individual model honesty to societal information control: even truthful mediators can strategically steer collective beliefs.
