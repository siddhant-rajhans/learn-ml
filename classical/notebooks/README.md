# Teaching notebooks — Linear & Logistic Regression

> Two notebooks per topic. One has all the code (your reference, off-camera). One has the same markdown with empty code cells (you type into it on camera while teaching).

## What's here

```
classical/notebooks/
├── README.md                                  this file
├── build_notebooks.py                         generates all 4 notebooks from one Python script
│
├── 01-linear-regression-complete.ipynb        full code + markdown · reference
├── 01-linear-regression-live.ipynb            same markdown · empty code cells · type into this
│
├── 02-logistic-regression-complete.ipynb      full code + markdown · reference
└── 02-logistic-regression-live.ipynb          same markdown · empty code cells · type into this
```

## The teaching workflow

1. Open the **complete** notebook on a second monitor (or laptop). This is your reference. The audience never sees it.
2. Open the **live** notebook in the recording window. Empty code cells, full markdown.
3. Read a markdown cell aloud. Type the corresponding code in the next cell from memory (glancing at the complete version when needed). Run the cell. Move on.
4. Repeat for each cell.

The pair is regenerated together by `build_notebooks.py`, so they always stay in sync.

## Editing the content

Don't edit the `.ipynb` files directly. Edit `build_notebooks.py` and re-run:

```bash
cd learn-ml/classical/notebooks
python build_notebooks.py
```

This regenerates all 4 notebooks. The "live" versions are derived from the "complete" versions automatically — same markdown, empty code cells.

## Dependencies

```bash
pip install numpy matplotlib scikit-learn torch
```

Or with uv:

```bash
uv pip install numpy matplotlib scikit-learn torch
```

Then `jupyter notebook` or `jupyter lab` from this directory.

## What each notebook covers

### 01 — Linear Regression

Companion to **Eps 19–23** of the Linear Regression series.

One dataset (7 cars, weight → MPG). One model (`y = wx + b`). One loss (MSE). One algorithm (gradient descent). Trained three ways: by hand, in PyTorch, in sklearn. All three agree.

Visualizations along the way: scatter + line, squared-distance squares, 3D loss surface, descent path on the bowl, fitted line over data.

Closes with the multi-feature extension (one extra weight per feature, same training loop).

### 02 — Logistic Regression

Companion to **Eps 24–28** of the Logistic Regression series.

Synthetic 2D spam dataset. Show why linear regression fails. Introduce sigmoid. Introduce log loss (with the two-curves visualization). Train by hand, in PyTorch, in sklearn. All three agree. Plot the decision boundary. Read the trained coefficients as multiplicative effects on the odds.

Same five-line training loop as the LR notebook — two substitutions (sigmoid in the forward pass, BCE for the loss). The pattern is made visible.

## Why notebooks instead of slides

Live coding is more visceral than slides for code-heavy topics. The audience watches you type. They see the output appear. They can pause the video and try the same thing.

Slides are still the right format for the conceptual episodes (the loss surface bowl, the dual view, the sigmoid asymptotes, etc.). These notebooks complement the slides — they're the "ok now let's actually run it" companion.

## Notes on convergence

The MPG dataset isn't normalized, which makes vanilla SGD slow to converge. The notebook handles this in three ways:

- **By-hand SGD**: bumps to 10,000 iterations with a small learning rate. Eventually reaches the right answer.
- **PyTorch**: uses **Adam** instead of vanilla SGD. Adam adapts the learning rate per parameter, much more forgiving on un-normalized data.
- **Sklearn**: uses a closed-form least-squares solution. No iteration needed.

The notebook mentions all three approaches and the trade-offs.
