# ICML 2026 Spotlight Batch 105 Synthesis

## Papers

- Scalable Event Cloud Network for Event-based Classification
- MV-FGAD: Towards Efficient and Effective Federated Graph Anomaly Detection via Multi-view Learning
- Modular Pretraining Enables Access Control
- MetaphorVU: Towards Metaphorical Video Understanding
- VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs

## Source Depth

All five notes are abstract/metadata-only. arXiv acquisition remains deferred after repeated 429/503 failures across preceding exact-batch attempts. Full-paper details should be verified later from official PDFs or high-confidence arXiv matches.

## Shared Thesis

This batch is about capability under nonstandard structure: asynchronous event streams, partitioned federated graphs, modular dual-use capabilities, metaphorical video semantics, and vectorized closed-loop driving worlds. Each paper replaces a flat modeling assumption with a structured representation or control interface.

The common pattern is that real-world deployment surfaces are not homogeneous tensors. They are sensor-native event clouds, fragmented client subgraphs, capability modules, cross-domain metaphor mappings, and graph-structured simulation states.

## Subthemes

### Sensor-native efficient perception

SECNet argues that event cameras should not be forced into frames or voxels when their native asynchronous structure carries fine-grained temporal information. Event-cloud processing and frequency-domain feature extraction support scalability without discarding the sensor's distinctive signal.

### Federated anomaly detection under fragmentation

MV-FGAD shows that graph anomaly detection becomes harder when each client sees only a partitioned subgraph. Weak anomalies are especially difficult, so shared federated knowledge and multi-view scoring are used to repair local blind spots.

### Modular access control

GRAM treats access control as a pretraining-time modularity problem. Rather than serving separate models or applying post-hoc unlearning, gradient-routed auxiliary modules localize capabilities so they can be ablated at inference time.

### Metaphorical video cognition

MetaphorVU pushes multimodal evaluation beyond literal recognition. Models must map visible source-domain scenes to abstract target meanings, and current MLLMs fail mainly because that cross-domain mapping is weak.

### Streaming vector-graph simulation

VectorWorld makes world modeling operational for autonomous driving. It generates vectorized lane-agent tiles during closed-loop rollout, balancing initialization validity, real-time sampling, and kinematic feasibility.

## Cross-Batch Connections

SECNet connects to EgoTactile, DroneDINO, IO-aware GNNs, and EntroKV through representation-efficient processing of nonstandard or large structured signals.

MV-FGAD connects to SmartFed, SpineFL, LAMP, and Relational Lottery Tickets through federated or graph-structured learning under incomplete local information.

GRAM connects strongly to GoodDiffusion and unlearning/copyright papers. Together they define a proactive access-control theme: authorization should be built into training or generation rather than patched after misuse.

MetaphorVU connects to Learning-to-Theorize, concept binding, and Beyond Language Modeling because high-order multimodal cognition requires structured semantic mappings, not only perceptual recognition.

VectorWorld connects to PanoWorld-X, EgoTactile, EcoVLA, and physical-domain generation through embodied world modeling under geometric and physical constraints.

## Emerging Pattern

The larger corpus pattern is that deployed ML systems are moving from generic prediction to structured interaction. The right model must preserve the native structure of its inputs, deployment partitions, capability boundaries, semantic mappings, or simulated dynamics.
