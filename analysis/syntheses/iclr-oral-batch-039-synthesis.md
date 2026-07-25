# ICLR Oral Batch 039 Synthesis

## Papers Covered

- Reducing Belief Deviation in Reinforcement Learning for Active Reasoning
- PhyWorldBench: A Comprehensive Evaluation of Physical Realism in Text-to-Video Models
- What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data
- To Infinity and Beyond: Tool-Use Unlocks Length Generalization in State Space Models
- Hallucination Begins Where Saliency Drops

## Shared Thesis

This batch is about diagnosing where complex AI systems lose contact with the state they are supposed to track. T3 detects belief deviation in active reasoning trajectories. PhyWorldBench tests whether generated videos obey physical constraints. WIMHF exposes hidden preference features in human feedback data. Tool-augmented SSMs externalize memory and computation to escape fixed-state length limits. LVLMs-Saliency detects hallucination when prior-output saliency drops. Across the batch, failure is treated as a measurable process signal.

## Deep Themes

### Reasoning Failures Have Trajectory Signatures

T3 and LVLMs-Saliency both identify failure onset inside the generation or interaction trajectory. T3 truncates active-reasoning rollouts when belief deviation becomes excessive. LVLMs-Saliency rejects or counteracts tokens when saliency to recent context drops. Both papers turn internal process diagnostics into interventions.

### Evaluation Moves Toward World and Value Grounding

PhyWorldBench and WIMHF both ask what current evaluations miss. PhyWorldBench checks physical behavior rather than photorealism alone. WIMHF checks what preference datasets actually reward rather than assuming their labels are transparent. These papers push evaluation from scoreboards toward diagnostic instruments.

### External Tools as Length-Generalization Mechanisms

The SSM tool-use paper argues that fixed-memory sequence models cannot solve arbitrary long-form tasks unaided. Tool access changes the computational class available to the model and makes SSMs plausible in agentic long-context settings.

### Interpretable Data and Inference Controls

WIMHF and LVLMs-Saliency are both interpretability-to-control pipelines. Preference features become knobs for relabeling and personalization; saliency scores become token filters and attention reinforcers. Interpretability is useful because it changes training or decoding decisions.

## Cross-Paper Pattern

The common pattern is state tracking. Active reasoners must track beliefs. Video models must track physical state. Alignment systems must track what feedback data encodes. SSMs need external state to solve length-growing tasks. LVLMs must track recent grounded context to avoid hallucination. The batch suggests that robust intelligence depends on maintaining the right state representation through time.

## Subthemes to Track

- Belief deviation in active reasoning RL.
- Physical realism benchmarks for text-to-video.
- Interpretable preference dataset features.
- Tool-use length generalization for SSMs.
- Saliency-guided LVLM hallucination reduction.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
