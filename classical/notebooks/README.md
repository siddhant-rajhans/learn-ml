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

### 01 — Linear Regression  (17 chapters · 116 cells · ~37 code cells)

Companion to **Eps 19–23** of the Linear Regression series.

Built like Google's ML Crash Course — one concept per cell, a worked numeric example for every formula. The 17 chapters walk through:

1. Setup
2. The dataset (7 cars, weight → MPG)
3. The model `y = wx + b`
4. How wrong is it? (errors → squared errors → MSE)
5. MSE has a picture (squared-distance squares)
6. Better guesses (manual table of MSEs)
7. The loss surface (3D bowl)
8. The gradient (formula + compute at one point)
9. One step (literal before / after)
10. The full descent loop (with a loss curve)
11. The descent path on the bowl (3D)
12. The fitted line vs the starting guess
13. The same thing in PyTorch (5-line loop with Adam)
14. The same thing in sklearn (3 lines)
15. **Bonus — sklearn's algorithm roadmap** (embedded SVG + walked path)
16. More features (multi-feature extension)
17. Recap

All three approaches (by-hand, PyTorch, sklearn) converge to the same `w ≈ -5.14, b ≈ 35.89`.

### 02 — Logistic Regression  (13 chapters · 102 cells · ~35 code cells)

Companion to **Eps 24–28** of the Logistic Regression series.

Same fine-grained chapter-by-chapter rhythm. The 13 chapters:

1. Setup
2. The dataset (synthetic 2D spam)
3. Try linear regression first — watch it predict `-0.14` and `+2.06` (broken)
4. The sigmoid function (5 worked numeric examples: σ(0), σ(1), σ(5), σ(-5), then plot)
5. Logistic regression = linear + sigmoid (worked example)
6. Log loss (3 worked examples: confident right, uncertain, confident wrong)
7. Train it by hand (one step + the full loop)
8. The decision boundary
9. The same thing in PyTorch (5-line loop · `BCEWithLogitsLoss`)
10. The same thing in sklearn (3 lines)
11. **Bonus — sklearn's algorithm roadmap** (embedded SVG + walked path)
12. Read the trained coefficients as multiplicative effects on the odds
13. Recap

By-hand and PyTorch agree on `W ≈ [0.71, 0.89], b ≈ -3.97`. Sklearn gets different values because it defaults to L2 regularization (noted in the notebook).

## Why notebooks instead of slides

Live coding is more visceral than slides for code-heavy topics. The audience watches you type. They see the output appear. They can pause the video and try the same thing.

Slides are still the right format for the conceptual episodes (the loss surface bowl, the dual view, the sigmoid asymptotes, etc.). These notebooks complement the slides — they're the "ok now let's actually run it" companion.

## Notes on convergence

The MPG dataset isn't normalized, which makes vanilla SGD slow to converge. The notebook handles this in three ways:

- **By-hand SGD**: bumps to 10,000 iterations with a small learning rate. Eventually reaches the right answer.
- **PyTorch**: uses **Adam** instead of vanilla SGD. Adam adapts the learning rate per parameter, much more forgiving on un-normalized data.
- **Sklearn**: uses a closed-form least-squares solution. No iteration needed.

The notebook mentions all three approaches and the trade-offs.
