# Frontier — Research

> *"Where the field is being written right now. Scaling laws, interpretability, safety, novel architectures. This is where you go from practitioner to contributor."*

**Total time:** ongoing
**Visual companion:** [The Map → Research Frontier](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)

## What this unlocks

Stop consuming, start producing. Reading frontier papers and reproducing them. Eventually: writing your own. The path that opens research roles, PhD admissions, and the work that actually moves the field.

## Topics

### Scaling Laws · 1 week
*Predict model performance before training. Understand why GPT-4 cost what it cost. Know what "compute-optimal" means.*

- Kaplan et al. (OpenAI) scaling laws
- Chinchilla — compute-optimal scaling
- Emergent abilities — are they real?
- Data scaling vs compute scaling
- Inference scaling (o1, chain-of-thought)
- FLOP counting
- Loss curves & learning dynamics

### Mechanistic Interpretability · 3–4 weeks
*Look inside a neural network and understand what it's doing. Anthropic's core research direction. Growing fast.*

- Circuits hypothesis
- Induction heads
- Superposition — polysemantic neurons
- Feature geometry
- Probing classifiers
- Attention pattern analysis
- Activation patching (causal tracing)
- Sparse autoencoders for features
- Toy models of superposition

### State Space Models · 2–3 weeks
*The architecture competing with Transformers for long-sequence modeling. S4, Mamba, and hybrid models.*

- Linear recurrences
- S4 — structured state spaces
- HiPPO theory
- Mamba — selective state spaces
- Hardware-aware design
- Linear attention connection
- RWKV
- Hybrid SSM-Attention models
- Long-range dependency benchmarks

### Mixture of Experts · 1–2 weeks
*How GPT-4 and Mixtral scale without proportional compute. Main architecture choice for 1T+ parameter models.*

- Sparse MoE — expert routing
- Load balancing loss
- Switch Transformer
- Mixtral architecture
- Mixture of Depths
- Expert specialization
- Communication overhead in distributed MoE
- Merging MoE experts

### AI Safety & Alignment · ongoing
*Contribute to the most important open problem in the field. Where stakes are highest.*

- Alignment problem — why it's hard
- Mesa-optimization & inner alignment
- Goal misgeneralization
- Scalable oversight
- Debate & amplification
- Red-teaming & adversarial evaluation
- Eval frameworks (HELM, BIG-Bench)
- Interpretability for safety

### Causal ML · 3–4 weeks
*Answer "what would happen if?" rather than "what correlates with what?" Essential for any high-stakes decision system.*

- Correlation vs causation — formally
- Structural Causal Models (SCMs)
- Do-calculus — Pearl
- Potential Outcomes Framework — Rubin
- Instrumental Variables
- Causal Discovery
- Uplift modeling
- Heterogeneous treatment effects
- Double ML

### Graph Neural Networks · 3–4 weeks
*Molecular graphs, social networks, knowledge bases, recommendation systems.*

- Graph representation — adjacency, Laplacian
- Message passing framework
- Graph Convolutional Networks (GCN)
- Graph Attention Networks (GAT)
- GraphSAGE — inductive learning
- Graph Transformer
- Molecular graphs & drug discovery
- Knowledge graph embeddings
- Link prediction & node classification

## How researchers actually work here

Three habits separate readers from contributors:

1. **Reproduce before you extend.** Pick one paper a quarter, reproduce it end-to-end. Most "I had an idea" research dies because the baseline wasn't fully understood.
2. **Read with a pen.** The 3-pass method: skim for shape (5 min), read for content (30 min), implement key equations (3 hrs). Most papers don't deserve pass 3. Some deserve it twice.
3. **Write while you learn.** A blog post is the cheapest way to discover what you don't understand. Publish before you feel ready.

## Where to go next

Pick a sub-track. Most contributions come from going *deep* in one of these, not skimming all seven. Pair with reading 1 paper/week from a single venue (NeurIPS / ICML / ICLR / ACL / CVPR / EMNLP).
