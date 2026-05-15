# Phase 4 · Deep Learning

> *"From a single neuron to a transformer. Build, train, debug, and reason about the loss landscape."*

## What you'll learn

```mermaid
flowchart TB
    NN[NN Fundamentals] --> MLP
    MLP --> Act[Activations]
    MLP --> Loss[Losses]
    Opt[Optimization] --> SGD
    Opt --> Adam
    Opt --> Init[Init: Xavier, Kaiming]
    Opt --> Norm[BatchNorm, LayerNorm, RMSNorm]

    BP[Backprop and Autograd]

    Frame[PyTorch]

    CNN[CNNs] --> ResNet
    Seq[Sequence Models] --> RNN
    Seq --> LSTM
    Seq --> Att[Attention]
    Att --> Tx[Transformers]

    Gen[Generative] --> AE
    Gen --> VAE
    Gen --> GAN
    Gen --> Diff[Diffusion]
```

## Time budget

4–6 months at ~10 hrs/week.

## Project checkpoints

- MLP on MNIST in pure NumPy (no framework).
- Same model in PyTorch, regularized to >99%.
- A CNN on CIFAR-10.
- Attention from scratch.
- A 2-layer mini-transformer trained on tiny Shakespeare.
- A VAE on faces; interpolate in latent space.

## Exit criteria

- [ ] Can read a PyTorch model definition and predict the shape of every tensor.
- [ ] Can diagnose vanishing gradients, exploding gradients, dead ReLUs.
- [ ] Have implemented attention from scratch at least once.
- [ ] Have one trained-from-scratch DL project on GitHub.

Then head to [Phase 5 · Specializations](../phase-5-specializations/).
