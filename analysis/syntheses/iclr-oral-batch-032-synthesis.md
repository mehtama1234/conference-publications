# ICLR Oral Batch 032 Synthesis

## Papers Covered

- Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models
- Exploratory Diffusion Model for Unsupervised Reinforcement Learning
- MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent
- Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator
- Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search

## Shared Thesis

This batch is about making powerful models useful under real constraints: privacy constraints, reward-free exploration, context limits, cross-model representation mismatch, and offline decision logs. The papers do not mainly add larger models. They add audits, controllers, interfaces, memories, and evaluators around existing models so the systems can act more reliably in deployment-shaped settings.

## Deep Themes

### Empirical Guarantees Under Distribution Shift

The privacy benchmark argues that formal DP guarantees do not settle practical privacy risk once pretraining and adaptation data interact. The key variable is distributional proximity to pretraining data, not only exact overlap. This extends a recurring safety pattern: guarantees need empirical stress tests that reflect the full data lifecycle.

### Generative Models as Control Priors

ExDM and AIGB-Pearl both use generative models for decision-making beyond imitation. ExDM models replay-buffer density so the agent can seek under-visited regions; AIGB-Pearl uses a generative planner plus evaluator-constrained search to improve bidding policies beyond static logs. In both cases, generation becomes useful when paired with a reward, score, or support-control mechanism.

### Process Policies Around Foundation Models

MemAgent treats long-context processing as a learned memory-management policy. Rather than assuming that a longer context window alone solves long-horizon QA, it trains an agent to update memory over chunks. This echoes other 2026 work where inference-time processes, not only model parameters, become the locus of capability.

### Interfaces Between Pretrained Components

VIST3A stitches a video generator to a 3D reconstruction decoder, then aligns the interface with reward finetuning. The broader subtheme is modular reuse: foundation components can be repurposed if the latent interface is made compatible and the downstream decoder gives a concrete usability signal.

### Evaluators as Search Boundaries

AIGB-Pearl and VIST3A both use evaluator-like signals to make generation more useful: bidding trajectories must score well under an offline evaluator while respecting constraints; video latents must decode into consistent 3D geometry. The evaluator is not just a metric after generation but part of the optimization loop.

## Cross-Paper Pattern

The common pattern is constrained adaptation around pretrained or offline systems. Privacy auditing constrains adaptation by empirical leakage risk. ExDM constrains exploration through replay-density structure. MemAgent constrains long-context reasoning through persistent memory updates. VIST3A constrains generative video latents by 3D decodability. AIGB-Pearl constrains offline policy search by evaluator score, KL distance, and Lipschitz regularity. The deeper theme is that high-capability systems are increasingly wrapped in explicit control surfaces.

## Subthemes to Track

- Pretrain-adapt privacy auditing.
- Diffusion density models for unsupervised RL.
- RL-trained textual memory agents.
- Model stitching for text-to-3D generation.
- Evaluator-constrained generative decision-making.

## Confidence and Source Depth

These notes are based on abstracts and local metadata. Formal details, validation protocols, and benchmark settings should be upgraded when PDFs are available.
