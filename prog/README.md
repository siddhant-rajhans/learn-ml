# Prog — Code & Systems

> *"Theory becomes real here. From Python basics to GPU kernels — the full stack of tools that let you run experiments at any scale."*

**Total time:** ~15–22 weeks
**Visual companion:** [The Map → Code & Systems](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)

## What this unlocks

Move from "I can run a notebook" to "I can profile a slow kernel, debug an OOM, write a Triton kernel, deploy a model to production." This is what makes the difference between a researcher who can prototype and an engineer who can ship.

## Topics

### Python Mastery · 2–4 weeks
*Readable, performant, production-quality code. Debug memory leaks. Profile bottlenecks.*

- OOP & closures
- Generators & iterators
- Decorators
- Type hints & mypy
- Async / concurrency
- Profiling & memory
- Virtual envs & packaging

### Vectorization · 1–2 weeks
*Write code that runs 100× faster without a GPU. Think in array operations, not loops.*

- NumPy broadcasting
- Einstein summation (einsum)
- Memory layout & strides
- SciPy
- Vectorized math
- BLAS/LAPACK basics

### PyTorch & Autograd · 3–4 weeks
*Implement any architecture from a paper. Write custom CUDA kernels. Debug gradient flow.*

- Tensor operations & device management
- Autograd engine internals
- Custom `nn.Module`
- Mixed precision training
- Gradient checkpointing
- `torch.compile`
- Distributed training (DDP, FSDP)
- TorchScript & export

### Data Stack · 2–3 weeks
*End-to-end data pipelines. Wrangle any dataset at scale.*

- Pandas — advanced groupby, merge, apply
- SQL — window functions, CTEs
- Polars for performance
- Apache Spark basics
- Arrow & Parquet
- Dask for out-of-core

### GPU & Systems · 4–6 weeks
*Write Flash Attention. Understand why Mamba is fast. Implement efficient kernels. The deep end — and it matters enormously.*

- CUDA memory hierarchy
- Thread blocks & warps
- Triton DSL
- NCCL & collective ops
- Flash Attention implementation
- Memory bandwidth vs compute
- Roofline model
- Quantization — INT8/INT4 kernels

### MLOps & Infra · 2–3 weeks
*Run reproducible experiments. Deploy models reliably. Never lose a run again.*

- Git & DVC
- Experiment tracking — W&B, MLflow
- Docker & containers
- Kubernetes basics
- Feature stores
- Model registry
- CI/CD for ML
- Monitoring in production

## Where to go next

`prog` runs in parallel with `math` and `data`. Once you have Python + NumPy + PyTorch fluency, **[classical/](../classical/)** is the first place to actually train models.
