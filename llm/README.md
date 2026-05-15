# LLM — Foundation Models

> *"The current wave. Transformers trained at scale on everything — text, images, code, audio. Understanding these is what separates people who use AI from people who build it."*

**Total time:** ~11–16 weeks
**Visual companion:** [The Map → Foundation Models](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)

## What this unlocks

Read the GPT-4 technical report and understand every architectural choice. Know why Llama 3 uses GQA and RoPE. Fine-tune a 7B model with LoRA on consumer hardware. Build a RAG system that actually works. Wire up agents with tool use and memory.

## Topics

### LLM Architecture · 2–3 weeks
*Read the GPT-4 technical report and understand every architectural choice. Know why Llama 3 uses grouped-query attention and RoPE.*

- Tokenization — BPE, WordPiece, SentencePiece
- Vocabulary size tradeoffs
- Rotary Position Embeddings (RoPE)
- Grouped-Query Attention (GQA)
- KV Cache — inference efficiency
- Context length scaling
- Decoder-only architecture
- Instruction template formats

### Pre-training at Scale · 2–3 weeks
*Why GPT-4 costs $100M to train. Data mixture, tokenizer design, compute budget decisions.*

- Next-token prediction at scale
- Data mixture — web, books, code, math
- Compute-optimal training — Chinchilla law
- Emergent abilities — what they are and aren't
- Distributed pre-training — tensor/pipeline/data parallelism
- Checkpointing strategy
- Curriculum & packing
- The Pile, C4, FineWeb

### Alignment & Fine-tuning · 3–4 weeks
*Turn a base model into a product. Why RLHF works, what DPO is, how LoRA makes fine-tuning accessible.*

- Supervised Fine-tuning (SFT)
- Reward modeling
- RLHF — PPO for language models
- Direct Preference Optimization (DPO)
- Constitutional AI
- LoRA & QLoRA — low-rank adaptation
- Prompt tuning & prefix tuning
- PEFT methods survey
- Evaluation — MMLU, HumanEval, custom evals

### Multimodal Models · 2–3 weeks
*How DALL·E, GPT-4V, Gemini, and Sora work. Multimodal is the current frontier of capabilities.*

- CLIP — contrastive image-text pre-training
- Vision encoders in LLMs (LLaVA, InternVL)
- Image tokenization — VQ-VAE, discrete tokens
- Audio models — Whisper, audio LLMs
- Video generation — temporal consistency
- Multimodal alignment
- Cross-modal retrieval

### RAG & AI Agents · 2–3 weeks
*Build systems that actually work in production. RAG is how 90% of enterprise AI is deployed. Agents are the next wave.*

- Retrieval-Augmented Generation
- Dense & sparse retrieval
- Vector databases (Pinecone, Chroma, Faiss)
- Chunking strategies
- Hybrid search
- ReAct — reason + act
- Tool use & function calling
- Multi-agent frameworks
- Memory architectures
- Evaluation of RAG systems

## Where to go next

**[frontier/](../frontier/)** if you want to push past "use foundation models" into "shape what they become next."
