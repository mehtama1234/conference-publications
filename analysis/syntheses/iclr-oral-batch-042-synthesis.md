# ICLR Oral Batch 042 Synthesis

## Papers Covered

- Intrinsic Entropy of Context Length Scaling in LLMs
- cadrille: Multi-modal CAD Reconstruction with Reinforcement Learning
- Improving Diffusion Models for Class-imbalanced Training Data via Capacity Manipulation
- EmotionThinker: Prosody-Aware Reinforcement Learning for Explainable Speech Emotion Reasoning
- Visual Planning: Let's Think Only with Images

## Shared Thesis

This batch is about choosing the right internal medium for a task. Intrinsic Entropy asks when longer textual context actually contains useful information. `cadrille` uses executable CAD code as the output medium for multimodal reconstruction. Capacity Manipulation treats diffusion imbalance as a representational capacity-allocation failure. EmotionThinker grounds emotional reasoning in prosody rather than treating speech as a label source. Visual Planning argues that spatial reasoning may be better represented as sequences of images than chains of text. The common claim is that model capability improves when the reasoning substrate matches the structure of the domain.

## Deep Themes

### Modality-Native Reasoning

EmotionThinker and Visual Planning both push against text as the default reasoning medium. EmotionThinker makes prosody a grounding signal for explanations, while Visual Planning makes images the intermediate representation for navigation and geometry. `cadrille` extends the same pattern into engineering: reconstruction is expressed as executable CAD code, not only a latent embedding or mesh.

### Internal Resource Allocation

Intrinsic Entropy and Capacity Manipulation both study whether internal resources are being used where they matter. The context-length paper treats longer context as useful only when it reduces intrinsic uncertainty. The diffusion imbalance paper argues that majority classes can consume too much capacity, leaving minority classes underrepresented. Both challenge a naive scaling story: more context or more model capacity does not help unless it is allocated to the informative part of the problem.

### Reinforcement Learning for Process Quality

`cadrille`, EmotionThinker, and Visual Planning all use RL-style post-training to improve more than a final answer. CAD reconstruction gets programmatic feedback on executable outputs. EmotionThinker rewards trustworthy reasoning aligned with acoustic evidence. Visual Planning trains image-sequence plans. The reinforcement signal is becoming domain-shaped: execution, prosody-grounded explanation, and navigation success are different supervisory currencies.

## Cross-Paper Pattern

The common pattern is representation realignment. Each paper identifies a mismatch between the default modeling interface and the task's actual structure: long contexts can include noninformative tokens, CAD needs editable programs, imbalanced diffusion needs reserved capacity, speech emotion needs prosodic evidence, and spatial planning needs visual states. The proposed fixes do not only add data or scale; they realign the model's intermediate representation, reward, or capacity with the domain.

## Subthemes to Track

- Intrinsic entropy for context-length scaling.
- Executable CAD code as multimodal reconstruction output.
- Capacity allocation under class imbalance.
- Prosody-grounded emotional reasoning.
- Image-sequence planning for spatial tasks.
- GRPO-style post-training for modality-specific process improvement.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. They should be upgraded when OpenReview PDFs or high-confidence arXiv matches are available, especially for exact theoretical claims, reward definitions, and benchmark details.
