# Learning to Discover at Test Time

## Metadata

- Conference: icml-2026
- Status: Spotlight
- OpenReview ID: 96zNuQrH9Y
- Authors: Mert Yuksekgonul; Daniel Koceja; Xinhao Li; Federico Bianchi; Jed McCaleb; Xiaolong Wang; Jan Kautz; Yejin Choi; James Zou; Carlos Guestrin; Yu Sun
- Primary area: deep_learning->large_language_models
- Keywords: test-time training;AI for science
- Source URL: https://openreview.net/forum?id=96zNuQrH9Y
- PDF URL: https://openreview.net/pdf?id=96zNuQrH9Y

## Abstract

How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other problems. Therefore, our learning objective and search subroutine are designed to prioritize the most promising solutions. We call this method Test-Time Training to Discover (TTT-Discover). Following prior work, we focus on problems with continuous rewards. We report results for every problem we attempted, across mathematics, GPU kernel engineering, algorithm design, and biology. TTT-Discover sets the new state of the art in almost all of them: (i) Erdős' minimum overlap problem and an autocorrelation inequality; (ii) a GPUMode kernel competition (up to 2× faster than prior art); (iii) past AtCoder algorithm competitions; and (iv) denoising problem in single-cell analysis. Our solutions are reviewed by experts or the organizers. All our results are achieved with an open model, OpenAI gpt-oss-120b, and can be reproduced with our publicly available code, in contrast to previous best results that required closed frontier models. Our test-time training runs are performed using Tinker, an API by Thinking Machines, with a cost of only a few hundred dollars per problem.

## One-Sentence Claim

TTT-Discover performs reinforcement learning at test time so an open LLM can adapt specifically to one scientific or engineering problem and discover a high-quality solution.

## Problem

Prompt-only test-time search with frozen LLMs can explore candidate solutions, but it does not let the model learn from problem-specific experience during the search itself.

## Core Contribution

The paper introduces Test-Time Training to Discover, a continual RL procedure whose objective and search routine prioritize finding one exceptional solution for the current problem rather than improving average generalization.

## Method

TTT-Discover uses reinforcement learning during test-time search on problems with continuous rewards, repeatedly using feedback from the target problem to train the model toward promising solution regions.

## Experiments and Evidence

The abstract reports new state-of-the-art results across mathematics, GPU kernel engineering, algorithm design, and single-cell denoising, including up to 2x faster kernels in a GPUMode competition. Results use the open gpt-oss-120b model and cost a few hundred dollars per problem through Tinker.

## Limits and Failure Modes

ArXiv search failed with HTTP 429 for this batch, so this note is abstract-only. Details still need checking: reward design, exploration budget, failed attempts, reproducibility of expert-reviewed solutions, and risk of overfitting to benchmark reward proxies.

## Deep Themes

- Test-time computation is becoming test-time learning.
- Scientific discovery can prioritize one exceptional artifact over average task performance.
- Open models may compete with closed frontier systems when allowed targeted adaptation.

## Subthemes

- Test-time training.
- Reinforcement learning for discovery.
- AI for science.
- Continuous-reward search.
- GPU kernel optimization.
- Problem-specific adaptation.

## Connections to Other Papers

Connects to AlphaEvolve-style search, DR Tulu, Skill-Pro, Pareto tool-integrated agents, and test-time scaling papers through inference-time optimization as a capability source.

## Notes for Cross-Paper Synthesis

This paper extends test-time scaling into test-time model update: discovery becomes a local training problem, not just a prompting/search problem.
