# ICLR 2026 Oral Batch 005 Synthesis

## Papers

- CounselBench: A Large-Scale Expert Evaluation and Adversarial Benchmarking of Large Language Models in Mental Health Question Answering
- Universal Inverse Distillation for Matching Models with Real-Data Supervision (No GANs)

## Source Depth

Both notes are abstract/metadata-only in the current local workspace. OpenReview remains the preferred source, and arXiv fallback should be retried for this final ICLR oral range when access and rate limits clear.

## Shared Thesis

This small batch highlights two deployment bottlenecks: trustworthy evaluation in high-stakes open-ended domains, and fast generation from expensive iterative models. CounselBench shows that mental-health QA needs expert-grounded, adversarial, span-level evaluation because LLM judges miss clinical risks. RealUID shows that matching-model deployment needs unified distillation that can use real data without GAN complexity.

## Cross-Batch Connections

CounselBench connects to FRABench/UFEval, Copyright-Bench, MiniAppBench, and safety benchmark work. It is the high-stakes version of the corpus's evaluation theme: evaluator convenience is not enough when harm is clinical.

RealUID connects to Diffusion Flow Matching, Reverse Flow Matching, DivIn, FlashWorld, and fast generative modeling. It belongs to the acceleration-and-unification theme around diffusion, flow, and matching models.

## Emerging Pattern

The shared deployment lesson is that practical ML systems need both reliable evaluation and efficient inference. A system that cannot be judged safely or run efficiently remains incomplete, even if its base model is capable.
