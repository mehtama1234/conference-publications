# ICLR Oral Batch 040 Synthesis

## Papers Covered

- Triple-BERT: Do We Really Need MARL for Order Dispatch on Ride-Sharing Platforms?
- LLM Fingerprinting via Semantically Conditioned Watermarks
- Agent Data Protocol
- TTSDS2: Resources and Benchmark for Evaluating Human-Quality Text to Speech Systems
- MotionStream: Real-Time Video Generation with Interactive Motion Controls

## Shared Thesis

This batch is about making AI systems operationally usable: dispatch policies for real platforms, fingerprints that survive deployment changes, standardized agent data pipelines, objective speech evaluation for near-human TTS, and real-time video generation. The papers are less about isolated model accuracy and more about the interface between models and production constraints: scale, latency, provenance, comparability, and standardized data.

## Deep Themes

### Centralization Versus Decomposition in Decision Systems

Triple-BERT argues that ride-sharing dispatch is fundamentally centralized even when many entities are involved. Its action decomposition and BERT-style relation modeling show a pattern also seen in optimization papers: decompose the action space while preserving global coordination.

### Robust Provenance Under Model Transformation

Semantically conditioned watermark fingerprints respond to the fragility of fixed trigger-key ownership proofs. By conditioning on semantic domains and diffusing a statistical signal through responses, the method tries to survive finetuning, quantization, and filtering.

### Data Protocols as Agent Infrastructure

ADP identifies format fragmentation as a bottleneck for agent finetuning. The protocol does not create a new task; it makes existing task traces interoperable across tool use, browsing, coding, and software-engineering workflows. This is a strong infrastructure theme in the corpus.

### Evaluation at the Human-Quality Frontier

TTSDS2 addresses the evaluation problem that appears once synthetic speech approaches human quality. Objective metrics need validation against subjective judgments across domains and languages, and benchmark leakage becomes a serious concern.

### Interactivity as a Generation Requirement

MotionStream moves video generation from offline clip creation toward real-time control. Its causal student, sliding-window attention, attention sinks, and KV cache rolling target a specific deployment requirement: users should be able to steer motion and see results immediately.

## Cross-Paper Pattern

The common pattern is deployment-shaped constraint handling. Triple-BERT handles large real-time dispatch spaces. Fingerprinting handles model ownership after deployment transformations. ADP handles fragmented agent datasets. TTSDS2 handles metric validity for near-human outputs. MotionStream handles latency and infinite-horizon streaming. Each paper defines success by whether the system still works under real operational constraints.

## Subthemes to Track

- Centralized RL for ride-sharing dispatch.
- Semantically conditioned LLM watermarks.
- Standardized agent data representation.
- Objective multilingual TTS evaluation.
- Real-time streaming video generation.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
