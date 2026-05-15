# learn-ml

> A visual-first ML curriculum from true zero to research scientist.
> Maintained by [Siddhant Rajhans](https://siddhant-rajhans.github.io/).

[![Companion videos](https://img.shields.io/badge/YouTube-Siddhant_Rajhans-red)](https://siddhant-rajhans.github.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Why this exists

Most ML learning paths are a Google doc of links. This is a curriculum:

- **Visual-first.** Every concept has a 3D / animated explanation, not just formulas. Built on top of [ml-visuals](https://github.com/siddhant-rajhans/ml-visuals).
- **Graph-shaped.** The full [interactive map](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html) shows *what depends on what* before you commit weeks to a topic.
- **From true zero to research.** No prereqs. High-school math through frontier ML.
- **Three paths, one map.** Pick *Literacy* (3 mo), *Builder* (8 mo), or *Researcher* (18+ mo). Same curriculum, different stopping points — see [`paths/`](paths/).

## The map

The single source of truth is the **interactive 3D roadmap**:

> 🗺️ **[siddhant-rajhans.github.io/ml-roadmap/roadmap.html](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)**

Drag to orbit. Click any node to drill in. Three audience paths.

## Layout

| Folder | What it covers | Typical time |
|---|---|---|
| [`foundations/`](foundations/) | *True-zero entry.* HS math + Python from scratch + terminal/git. **Satellite to the map, not a category.** | 6–10 weeks |
| [`math/`](math/) | Linear algebra · calculus · probability · statistics · info theory · optimization | 3–5 months |
| [`prog/`](prog/) | Python · NumPy · PyTorch · data stack · GPU/systems · HuggingFace · MLOps | 3–5 months |
| [`data/`](data/) | Collection · labeling · quality · feature engineering · data-centric AI | 2–3 months |
| [`classical/`](classical/) | Supervised · kernel · unsupervised · graphical · RL · time series · recommenders · interpretability · evaluation | 5–7 months |
| [`dl/`](dl/) | NN theory · backprop · CNNs · sequence models · transformers · generative · diffusion · speech/audio · self-supervised | 4–6 months |
| [`llm/`](llm/) | LLM architecture · pre-training · alignment · multimodal · RAG/agents · inference optimization | 3–4 months |
| [`frontier/`](frontier/) | Scaling laws · mech interp · SSMs · MoE · safety · causal · GNNs | ongoing |
| [`paths/`](paths/) | Literacy / Builder / Researcher routes through the above | reference |

Each category folder has its own README with topics, time bands, the "what this unlocks" framing, and external resources. Folders are not strictly sequential — see [`paths/`](paths/) for how to order them by role.

## How to use this repo

```bash
git clone https://github.com/siddhant-rajhans/learn-ml.git
cd learn-ml
```

1. **Open the interactive map** at [siddhant-rajhans.github.io/ml-roadmap/roadmap.html](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html).
2. **New to all this?** Start with [`foundations/`](foundations/). Otherwise pick a path.
3. **Read the category README** for whichever bucket your path enters first (usually `math/`).
4. **Notebooks, exercises, and worked solutions** ship per topic as I write them. Tracked in issues.

## Companion content

- **The slide system:** [siddhant-rajhans.github.io/ml-roadmap/](https://siddhant-rajhans.github.io/ml-roadmap/) — the interactive 3D roadmap, episode 01 "What a Vector Actually Is," and the Linear Algebra 3D Transformation Engine.
- **The asset library:** [github.com/siddhant-rajhans/ml-visuals](https://github.com/siddhant-rajhans/ml-visuals) — R3F + Manim components you can embed in your own notes.
- **Portfolio + newsletter + YouTube:** [siddhant-rajhans.github.io](https://siddhant-rajhans.github.io/).

## Contributing

PRs welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Best contributions:

- Typo / clarity fixes in any category README.
- Worked exercises with solutions.
- Better notebook examples for a topic.
- Translations — especially Hindi, Spanish, Mandarin.

## Citing

If this curriculum helped you, a star is the easiest way to give back. If you reference it:

```bibtex
@misc{rajhans2026learnml,
  author       = {Siddhant Rajhans},
  title        = {learn-ml: A visual-first ML curriculum from zero to research},
  year         = {2026},
  url          = {https://github.com/siddhant-rajhans/learn-ml}
}
```

## License

[MIT](LICENSE). Use it however you want — teach, fork, translate, ship inside your bootcamp. Attribution appreciated, not required.
