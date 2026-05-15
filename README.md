# learn-ml

> A visual-first ML curriculum from zero to research scientist.
> Maintained by [Siddhant Rajhans](https://siddhant-rajhans.github.io/).

[![Companion videos](https://img.shields.io/badge/YouTube-Siddhant_Rajhans-red)](https://siddhant-rajhans.github.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Why this exists

Most ML learning paths are a Google doc of links. This one is a curriculum:

- **Visual-first.** Every concept has a 3D / animated explanation, not just formulas. Built on top of [ml-visuals](https://github.com/siddhant-rajhans/ml-visuals) (the open-source asset library I maintain for both this repo and my videos).
- **Graph-shaped.** You can see *what depends on what* before you commit weeks to a topic.
- **From true zero.** No prereqs. We start with high-school math and end at frontier ML research.
- **Companioned by video.** Each phase is paired with a YouTube series so you can watch *or* read.

## The map

The full graph-and-node curriculum lives in [`ROADMAP.md`](ROADMAP.md). The eight phases:

| Phase | Topic | Time (~10h/wk) |
|---|---|---|
| 0 | Foundations — HS math + Python from zero | 6–10 weeks |
| 1 | Math for ML — linear algebra, calc, prob, info theory | 4–6 months |
| 2 | Programming for ML — NumPy, Pandas, git, Linux | 2–3 months |
| 3 | Classical ML — regression, trees, clustering, eval | 3–4 months |
| 4 | Deep Learning — NNs, CNNs, RNNs, Transformers, generative | 4–6 months |
| 5 | Specializations — NLP / CV / RL / GNN / multimodal | 3–6 months each |
| 6 | ML Engineering — MLOps, deployment, distributed training | 3–4 months |
| 7 | ML Scientist — papers, frontier, advanced math, research | ongoing |

## How to use this repo

```bash
git clone https://github.com/siddhant-rajhans/learn-ml.git
cd learn-ml
```

Each `phase-N-*/` folder contains:
- `README.md` — what you'll learn, prereqs, time budget
- `notes/` — written explanations matched to companion videos
- `notebooks/` — runnable Jupyter notebooks (Colab links inside)
- `exercises/` — problems to solve before moving on
- `solutions/` — work them yourself first; solutions in a collapsed section

Start at [`phase-0-foundations/`](phase-0-foundations/) regardless of your background. Even if you know Python, the math refresh sets up notation we use throughout.

## Companion content

- **YouTube — broad track:** roadmap-style videos, career advice, project walkthroughs.
- **YouTube — math track:** deep visual essays on the math behind ML models.
- **Newsletter:** weekly digest of what dropped + commentary.
- **Portfolio:** [siddhant-rajhans.github.io](https://siddhant-rajhans.github.io/)

All links land at the portfolio above; subscribe there for the channels and newsletter.

## Contributing

This is being built in public. PRs welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md). The cleanest contributions:

- **Typo / clarity fixes** in any phase's notes.
- **Better exercises** with worked solutions.
- **Additional notebook examples** that explain a concept I've muddled.
- **Translations.** Especially Hindi, Spanish, Mandarin.

## Citing

If this curriculum helped you, a star is the easiest way to give back. If you're publishing material that references this:

```bibtex
@misc{rajhans2026learnml,
  author       = {Siddhant Rajhans},
  title        = {learn-ml: A visual-first ML curriculum from zero to research},
  year         = {2026},
  url          = {https://github.com/siddhant-rajhans/learn-ml}
}
```

## License

[MIT](LICENSE). Use the material however you want — teach with it, fork it, translate it, ship it inside your bootcamp. Attribution is appreciated, not required.
