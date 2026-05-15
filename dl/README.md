# DL — Deep Learning

> *"The revolution. Neural networks that learn hierarchical representations from raw data — the foundation of everything modern AI is built on."*

**Total time:** ~17–25 weeks
**Visual companion:** [The Map → Deep Learning](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)

## What this unlocks

Implement backprop from scratch in NumPy. Read any DL paper and predict every tensor shape. Train a CNN on CIFAR-10 to >90%. Implement multi-head attention. Train a tiny transformer on Shakespeare. Build a VAE that interpolates faces. By the end, you stop being scared of architectural complexity — every model is a graph of tensor ops with backprop running through it.

## Topics

### Neural Network Theory · 2–3 weeks
*Why depth matters, what activation functions are really doing, why random initialization matters more than you think.*

- Universal Approximation Theorem
- Depth vs width — expressivity
- Activation functions — sigmoid, ReLU, GELU, SiLU
- Weight initialization — Xavier, He, orthogonal
- Gradient flow — vanishing & exploding
- Lottery Ticket Hypothesis
- Neural Tangent Kernel (NTK)
- Double Descent phenomenon

### Backpropagation · 1–2 weeks
*Implement backprop from scratch in NumPy. Debug any gradient issue. Understand why certain architectures are hard to train.*

- Computational graphs
- Forward pass as function composition
- Reverse-mode autodiff
- Jacobian-vector products
- Gradient checkpointing
- Second-order gradients
- Custom autograd functions in PyTorch
- Numerical gradient checking

### Regularization & Normalization · 1–2 weeks
*Know exactly when to use BatchNorm vs LayerNorm vs RMSNorm. Understand why dropout works and when it doesn't.*

- L1 & L2 regularization
- Dropout — as ensemble method
- Batch Normalization — derivation & internals
- Layer Normalization
- RMSNorm
- Weight decay vs L2 regularization — they're not the same
- Data augmentation as regularization
- Spectral normalization

### CNNs & Vision · 3–4 weeks
*Why convolutions are a good inductive bias for images. Read and implement ResNet, EfficientNet, or ViT from scratch.*

- Convolution — as cross-correlation
- Padding, stride, dilation
- Receptive field calculations
- Pooling — average vs max
- ResNet — residual connections, why they work
- EfficientNet — compound scaling
- Transfer learning & fine-tuning
- Depthwise separable convolutions
- U-Net
- Vision Transformer (ViT)

### Sequence Models · 2–3 weeks
*Understand the history that made Transformers inevitable. RNNs still appear in edge models, time series, and RL.*

- Vanilla RNN — unrolling through time
- Vanishing gradient in RNNs — why
- LSTM — cell state & gates
- GRU — simplified gating
- Bidirectional RNNs
- Sequence-to-sequence
- Attention mechanism — where it came from
- Teacher forcing

### Transformers · 4–6 weeks
*The architecture that runs the world. Implement multi-head attention from scratch. Understand every line of the original paper.*

- Query, Key, Value — the attention mechanism
- Scaled dot-product attention — why √d_k
- Multi-head attention
- Positional encodings — sinusoidal & rotary (RoPE)
- Pre-norm vs post-norm
- Feed-forward sublayer
- Encoder-only (BERT) vs Decoder-only (GPT) vs Encoder-Decoder (T5)
- Flash Attention — IO-aware exact attention
- Efficient attention survey (Linformer, Performer, Longformer)

### Generative Models · 3–4 weeks
*Generate data. Understand the ELBO. Know why GANs are hard to train and what the alternatives are.*

- GANs — minimax game, training instability
- WGAN — Wasserstein distance
- StyleGAN — progressive growing
- VAE — ELBO derivation
- β-VAE
- Normalizing Flows — change of variables
- Energy-Based Models
- Autoregressive models (PixelCNN, WaveNet)

### Diffusion Models · 3–4 weeks
*Understand Stable Diffusion, DALL·E, Sora from first principles. Score matching is one of the most beautiful ideas in modern ML.*

- Forward process — adding Gaussian noise
- Score matching — Hyvärinen
- Denoising Score Matching
- DDPM — Ho et al. derivation
- DDIM — deterministic sampling
- Classifier guidance & Classifier-Free Guidance
- Latent Diffusion Models (Stable Diffusion)
- Consistency Models
- Flow Matching

## Where to go next

**[llm/](../llm/)** if you want to scale transformers and build with foundation models. **[frontier/](../frontier/)** if you're heading into research.
