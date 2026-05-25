"""
Build the four teaching notebooks.

  01-linear-regression-complete.ipynb     — all code, off-camera reference
  01-linear-regression-live.ipynb         — same markdown, empty code cells, type into this on camera
  02-logistic-regression-complete.ipynb   — all code, off-camera reference
  02-logistic-regression-live.ipynb       — same markdown, empty code cells

Run with:   python build_notebooks.py

This script generates valid .ipynb files (JSON). Re-run any time you
edit the notebook contents — the live version is regenerated from the
complete version automatically, so they always stay in sync.
"""

import json
from pathlib import Path

HERE = Path(__file__).parent

# ────────────────────────────────────────────────────────────────────
# Notebook helpers
# ────────────────────────────────────────────────────────────────────

def md(*lines):
    """Markdown cell. Pass each visual line as a separate argument."""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": _join_lines(lines),
    }


def code(*lines):
    """Code cell. Pass each line of code as a separate argument."""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": _join_lines(lines),
    }


def _join_lines(lines):
    """Turn (line, line, line) into ['line\\n', 'line\\n', 'line'] for nbformat."""
    out = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            out.append(line + "\n")
        else:
            out.append(line)
    return out


def write_notebook(cells, path):
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"  wrote {path.name}  ({len(cells)} cells)")


def make_live_version(cells):
    """Generate the live-typing version: same markdown, empty code cells."""
    out = []
    for c in cells:
        if c["cell_type"] == "code":
            out.append(code(""))
        else:
            out.append(c)
    return out


# ════════════════════════════════════════════════════════════════════
# Notebook 1: Linear Regression
# ════════════════════════════════════════════════════════════════════

lr_cells = [
    md(
        "# Linear regression — from scratch, then with PyTorch and sklearn",
        "",
        "Companion notebook for **Eps 19–23** of the Linear Regression series.",
        "",
        "*One dataset (7 cars, weight → MPG). One model (`y = wx + b`). One loss (MSE). One algorithm (gradient descent). By the end you'll have trained it three ways: by hand, in PyTorch, and in sklearn.*",
    ),

    # ── 1. Setup ─────────────────────────────────────────────────
    md(
        "## 1. Setup",
        "",
        "Just the imports. NumPy for the math, matplotlib for plots. Torch and sklearn show up later.",
    ),
    code(
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "",
        "np.random.seed(42)",
        "plt.rcParams['figure.figsize'] = (8, 5)",
        "plt.rcParams['axes.grid'] = True",
        "plt.rcParams['grid.alpha'] = 0.3",
    ),

    # ── 2. The dataset ───────────────────────────────────────────
    md(
        "## 2. The dataset",
        "",
        "Seven cars. For each, its weight (in thousands of pounds) and how many miles per gallon it gets. Heavier cars get worse mileage — you can see it in the numbers.",
    ),
    code(
        "weights = np.array([2.4, 2.8, 3.0, 3.2, 3.6, 4.0, 4.4])",
        "mpgs    = np.array([24,  22,  20,  19,  17,  15,  14])",
        "",
        "for w, m in zip(weights, mpgs):",
        "    print(f'  {w}K lbs  ->  {m} MPG')",
    ),
    md(
        "### Plot it",
        "",
        "A scatter is the right first move. Always plot the data before you model it.",
    ),
    code(
        "plt.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=3)",
        "plt.xlabel('weight (1000 lbs)')",
        "plt.ylabel('MPG')",
        "plt.title('7 cars — weight vs MPG')",
        "plt.show()",
    ),

    # ── 3. The model ─────────────────────────────────────────────
    md(
        "## 3. The model: `y = w·x + b`",
        "",
        "Simplest possible model for this data is a straight line. Two parameters — `w` (slope) and `b` (intercept). Pick any (w, b), get a different line.",
    ),
    code(
        "def predict(w, b, x):",
        "    return w * x + b",
        "",
        "# Wild guess: w = -3, b = 30",
        "w_guess, b_guess = -3.0, 30.0",
        "",
        "# Predict MPG for each car",
        "preds = predict(w_guess, b_guess, weights)",
        "",
        "for w, m, p in zip(weights, mpgs, preds):",
        "    print(f'  weight={w}  actual MPG={m}  predicted MPG={p:.1f}')",
    ),
    md(
        "### Plot the guess",
        "",
        "Plot the line over the data. It's not great. That's the point — let's measure exactly *how* not-great.",
    ),
    code(
        "xs = np.linspace(2, 5, 50)",
        "ys = predict(w_guess, b_guess, xs)",
        "",
        "plt.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=3, label='data')",
        "plt.plot(xs, ys, color='#FFD27F', linewidth=2.5, label=f'guess: y = {w_guess}x + {b_guess}')",
        "plt.xlabel('weight (1000 lbs)')",
        "plt.ylabel('MPG')",
        "plt.legend()",
        "plt.show()",
    ),

    # ── 4. Loss — MSE ───────────────────────────────────────────
    md(
        "## 4. Loss — measuring 'wrong'",
        "",
        "**Mean Squared Error.** For each car, square the difference between the prediction and the truth. Average across all cars. That single number says how wrong the model is.",
        "",
        "We square because squaring gives clean gradients (Ep 20 of the calculus series — derivative of x² is 2x, smooth everywhere).",
    ),
    code(
        "def mse(w, b):",
        "    preds = predict(w, b, weights)",
        "    return np.mean((mpgs - preds) ** 2)",
        "",
        "print(f'MSE of our guess (w={w_guess}, b={b_guess}): {mse(w_guess, b_guess):.3f}')",
    ),
    md(
        "### Visualize the errors — the gray squares",
        "",
        "MSE has a picture. The squared error for each car is the area of a square whose side is the vertical distance from the line to the point. Total area = sum of squared errors.",
    ),
    code(
        "fig, ax = plt.subplots()",
        "ax.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=5, label='data')",
        "ax.plot(xs, predict(w_guess, b_guess, xs), color='#FFD27F', linewidth=2.5, label='guess')",
        "",
        "# Squared-error squares, drawn from each point to the line",
        "for w_data, m_data in zip(weights, mpgs):",
        "    p = predict(w_guess, b_guess, w_data)",
        "    err = m_data - p",
        "    # Draw a square whose side is |err|",
        "    side = abs(err)",
        "    ax.add_patch(plt.Rectangle((w_data, min(m_data, p)), side, side,",
        "                                color='#7C4DFF', alpha=0.25, linewidth=0))",
        "    ax.plot([w_data, w_data], [m_data, p], color='#7C4DFF', alpha=0.6, linewidth=1)",
        "",
        "ax.set_xlabel('weight (1000 lbs)')",
        "ax.set_ylabel('MPG')",
        "ax.set_title('The squared distances — total area = MSE × N')",
        "ax.set_aspect('equal')",
        "ax.legend()",
        "plt.show()",
    ),
    md(
        "### Try a better guess",
        "",
        "Drag your mental slider — change w and b until MSE is smaller. The lower the MSE, the better the fit.",
    ),
    code(
        "w_better, b_better = -5.0, 34.0",
        "print(f'Old guess MSE: {mse(w_guess, b_guess):.3f}')",
        "print(f'New guess MSE: {mse(w_better, b_better):.3f}')",
    ),

    # ── 5. The loss surface ─────────────────────────────────────
    md(
        "## 5. The loss surface",
        "",
        "MSE is a function of (w, b). Two inputs, one output. That's a surface. Let's compute it on a grid and plot it.",
        "",
        "*Reusing the bowl from calculus Ep 17 — but this bowl is built from the actual seven cars in our dataset.*",
    ),
    code(
        "w_range = np.linspace(-10, 2, 60)",
        "b_range = np.linspace(15, 45, 60)",
        "W, B = np.meshgrid(w_range, b_range)",
        "",
        "# Vectorized MSE computation over the grid",
        "loss_grid = np.zeros_like(W)",
        "for i in range(W.shape[0]):",
        "    for j in range(W.shape[1]):",
        "        loss_grid[i, j] = mse(W[i, j], B[i, j])",
        "",
        "print('grid shape:', loss_grid.shape, ' min MSE on grid:', loss_grid.min().round(3))",
    ),
    md(
        "### Plot the bowl",
        "",
        "Tilt the 3D plot and look at it. One minimum. No local pits. That's why linear regression always trains.",
    ),
    code(
        "fig = plt.figure(figsize=(10, 7))",
        "ax = fig.add_subplot(111, projection='3d')",
        "ax.plot_surface(W, B, loss_grid, cmap='viridis', alpha=0.8, edgecolor='none')",
        "ax.contour(W, B, loss_grid, zdir='z', offset=loss_grid.min(),",
        "           cmap='viridis', alpha=0.5)",
        "ax.set_xlabel('w (slope)')",
        "ax.set_ylabel('b (intercept)')",
        "ax.set_zlabel('MSE')",
        "ax.set_title('The loss surface — a clean convex bowl')",
        "ax.view_init(elev=30, azim=-60)",
        "plt.show()",
    ),

    # ── 6. Gradient descent by hand ─────────────────────────────
    md(
        "## 6. Gradient descent by hand",
        "",
        "Compute the gradient (the slope of the bowl at the current point). Take a step downhill. Repeat. Same algorithm from calculus Ep 17.",
        "",
        "For MSE with `y = wx + b`, the gradients work out to:",
        "",
        "$$\\frac{\\partial L}{\\partial w} = \\frac{2}{N}\\sum_i x_i (wx_i + b - y_i)$$",
        "",
        "$$\\frac{\\partial L}{\\partial b} = \\frac{2}{N}\\sum_i (wx_i + b - y_i)$$",
    ),
    code(
        "def grad(w, b):",
        "    errs = predict(w, b, weights) - mpgs",
        "    dw = 2 * np.mean(weights * errs)",
        "    db = 2 * np.mean(errs)",
        "    return dw, db",
        "",
        "# At our better guess, what does the gradient look like?",
        "dw, db = grad(w_better, b_better)",
        "print(f'∂L/∂w = {dw:.3f}    ∂L/∂b = {db:.3f}')",
    ),
    md(
        "### One step",
    ),
    code(
        "lr = 0.01",
        "w_new = w_better - lr * dw",
        "b_new = b_better - lr * db",
        "",
        "print(f'before:  w={w_better:.3f}  b={b_better:.3f}  MSE={mse(w_better, b_better):.3f}')",
        "print(f'after:   w={w_new:.3f}  b={b_new:.3f}  MSE={mse(w_new, b_new):.3f}')",
    ),
    md(
        "### The full loop",
        "",
        "Start somewhere random. Step downhill. Repeat until the gradients are small.",
    ),
    code(
        "w, b = -1.0, 15.0   # starting point — wrong on purpose so the descent is visible",
        "lr = 0.01           # small enough that w doesn't oscillate",
        "n_steps = 10000     # ten thousand steps. takes about a second.",
        "",
        "history = {'w': [w], 'b': [b], 'mse': [mse(w, b)]}",
        "",
        "for step in range(n_steps):",
        "    dw, db = grad(w, b)",
        "    w -= lr * dw",
        "    b -= lr * db",
        "    history['w'].append(w)",
        "    history['b'].append(b)",
        "    history['mse'].append(mse(w, b))",
        "",
        "print(f'final:  w={w:.4f}  b={b:.4f}  MSE={mse(w, b):.4f}')",
        "print(f'(true optimum is roughly w=-5.15, b=35.92 — see sklearn below)')",
        "print()",
        "print('Notice: this takes 10,000 iterations to converge with vanilla SGD on raw features.')",
        "print('Real ML normalizes features first OR uses a smarter optimizer (Adam). Both fix this.')",
    ),
    md(
        "### Plot the descent path on the bowl",
    ),
    code(
        "fig = plt.figure(figsize=(11, 7))",
        "ax = fig.add_subplot(111, projection='3d')",
        "ax.plot_surface(W, B, loss_grid, cmap='viridis', alpha=0.55, edgecolor='none')",
        "",
        "# The path",
        "ax.plot(history['w'], history['b'], history['mse'],",
        "        color='#FFD27F', linewidth=2, marker='o', markersize=3)",
        "",
        "# Start + end markers",
        "ax.scatter([history['w'][0]], [history['b'][0]], [history['mse'][0]],",
        "           color='#FF4081', s=150, edgecolor='white', linewidth=1.5, label='start')",
        "ax.scatter([history['w'][-1]], [history['b'][-1]], [history['mse'][-1]],",
        "           color='#00E676', s=150, edgecolor='white', linewidth=1.5, label='end')",
        "",
        "ax.set_xlabel('w'); ax.set_ylabel('b'); ax.set_zlabel('MSE')",
        "ax.set_title('Gradient descent on the loss surface')",
        "ax.view_init(elev=30, azim=-60)",
        "ax.legend()",
        "plt.show()",
    ),
    md(
        "### Plot the fitted line over the data",
    ),
    code(
        "plt.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=3, label='data')",
        "plt.plot(xs, predict(w, b, xs), color='#FFD27F', linewidth=2.5,",
        "         label=f'fitted: y = {w:.2f}x + {b:.2f}')",
        "plt.xlabel('weight (1000 lbs)')",
        "plt.ylabel('MPG')",
        "plt.title('Linear regression — fitted by hand')",
        "plt.legend()",
        "plt.show()",
    ),

    # ── 7. PyTorch ─────────────────────────────────────────────
    md(
        "## 7. Same thing in PyTorch — the 5-line training loop",
        "",
        "The same gradient descent, but `loss.backward()` computes gradients for us. This is the same five lines from calculus Ep 18.",
    ),
    code(
        "import torch",
        "import torch.nn as nn",
        "",
        "# Convert data to tensors. PyTorch wants shape (N, 1) for the linear layer.",
        "X = torch.tensor(weights, dtype=torch.float32).view(-1, 1)",
        "y = torch.tensor(mpgs,    dtype=torch.float32).view(-1, 1)",
        "",
        "# The model: y = wx + b. nn.Linear with 1 input feature, 1 output.",
        "model = nn.Linear(1, 1)",
        "# Adam adapts the learning rate per parameter — much more forgiving than vanilla SGD",
        "# when the features aren't normalized (which they aren't here).",
        "optimizer = torch.optim.Adam(model.parameters(), lr=0.05)",
        "loss_fn = nn.MSELoss()",
        "",
        "# THE 5-LINE TRAINING LOOP",
        "for step in range(5000):",
        "    pred = model(X)",
        "    loss = loss_fn(pred, y)",
        "    loss.backward()",
        "    optimizer.step()",
        "    optimizer.zero_grad()",
        "",
        "w_torch = model.weight.item()",
        "b_torch = model.bias.item()",
        "print(f'PyTorch result:  w={w_torch:.4f}  b={b_torch:.4f}')",
        "print(f'By-hand result:  w={w:.4f}  b={b:.4f}')",
    ),

    # ── 8. Sklearn ─────────────────────────────────────────────
    md(
        "## 8. Same thing in sklearn — 3 lines",
        "",
        "Sklearn wraps the whole loop. For most projects, this is what you'd actually write.",
    ),
    code(
        "from sklearn.linear_model import LinearRegression",
        "",
        "model_sk = LinearRegression()",
        "model_sk.fit(weights.reshape(-1, 1), mpgs)",
        "",
        "print(f'sklearn result:  w={model_sk.coef_[0]:.4f}  b={model_sk.intercept_:.4f}')",
        "print(f'PyTorch result:  w={w_torch:.4f}  b={b_torch:.4f}')",
        "print(f'By-hand result:  w={w:.4f}  b={b:.4f}')",
        "",
        "# Predict MPG for a 3,500-pound car",
        "new_car_mpg = model_sk.predict([[3.5]])",
        "print(f'\\nA 3,500-pound car -> {new_car_mpg[0]:.1f} MPG')",
    ),

    # ── 9. More features ────────────────────────────────────────
    md(
        "## 9. More features",
        "",
        "Real cars have more than one feature. Let's pretend our cars also have horsepower and engine displacement.",
    ),
    code(
        "# Synthetic horsepower + displacement (correlated with weight, plus noise)",
        "horsepower   = weights * 60 + np.random.normal(0, 15, size=7)",
        "displacement = weights * 1.5 + np.random.normal(0, 0.4, size=7)",
        "",
        "X_multi = np.column_stack([weights, horsepower, displacement])",
        "print('shape of X_multi:', X_multi.shape)",
        "print(X_multi.round(2))",
    ),
    code(
        "model_multi = LinearRegression()",
        "model_multi.fit(X_multi, mpgs)",
        "",
        "print(f'  weight coef:        {model_multi.coef_[0]:+.4f}')",
        "print(f'  horsepower coef:    {model_multi.coef_[1]:+.4f}')",
        "print(f'  displacement coef:  {model_multi.coef_[2]:+.4f}')",
        "print(f'  intercept:          {model_multi.intercept_:+.4f}')",
        "",
        "# Each weight tells you: 'holding the others constant, this is how much MPG",
        "# changes per unit of this feature.'",
    ),

    # ── 10. Recap ──────────────────────────────────────────────
    md(
        "## 10. What we did",
        "",
        "- Loaded a dataset and plotted it.",
        "- Defined a model `y = wx + b` and a loss `MSE`.",
        "- Visualized the loss as a surface (the bowl).",
        "- Trained the model three ways: by-hand gradient descent, the PyTorch 5-line loop, and sklearn's 3 lines.",
        "- All three give the same answer (within numerical precision).",
        "- Extended to multiple features — one extra weight per feature, same algorithm.",
        "",
        "**Next notebook: logistic regression.** Same training loop, two substitutions — sigmoid in the forward pass, log loss in place of MSE.",
    ),
]

write_notebook(lr_cells, HERE / "01-linear-regression-complete.ipynb")
write_notebook(make_live_version(lr_cells), HERE / "01-linear-regression-live.ipynb")


# ════════════════════════════════════════════════════════════════════
# Notebook 2: Logistic Regression
# ════════════════════════════════════════════════════════════════════

log_cells = [
    md(
        "# Logistic regression — from scratch, then with PyTorch and sklearn",
        "",
        "Companion notebook for **Eps 24–28** of the Logistic Regression series.",
        "",
        "*Same training loop as linear regression. Two substitutions: a sigmoid in the forward pass, binary cross-entropy in place of MSE. By the end you'll have trained a binary classifier three ways.*",
    ),

    # ── 1. Setup ─────────────────────────────────────────────────
    md(
        "## 1. Setup",
    ),
    code(
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "",
        "np.random.seed(42)",
        "plt.rcParams['figure.figsize'] = (8, 5)",
        "plt.rcParams['axes.grid'] = True",
        "plt.rcParams['grid.alpha'] = 0.3",
    ),

    # ── 2. The dataset ───────────────────────────────────────────
    md(
        "## 2. The dataset",
        "",
        "We'll fake a spam dataset — two features per email (suspicious-word count, capitalization ratio), and a label (1 = spam, 0 = not).",
        "",
        "Real spam detection uses thousands of features. Two is enough to *see* what's going on.",
    ),
    code(
        "n_per_class = 60",
        "",
        "# Not-spam cluster (label 0): low on both features",
        "not_spam = np.random.randn(n_per_class, 2) * 1.0 + np.array([1.5, 0.8])",
        "",
        "# Spam cluster (label 1): high on both",
        "spam = np.random.randn(n_per_class, 2) * 1.0 + np.array([5.0, 4.0])",
        "",
        "X = np.vstack([not_spam, spam])",
        "y = np.hstack([np.zeros(n_per_class), np.ones(n_per_class)])",
        "",
        "print('X shape:', X.shape, ' y shape:', y.shape)",
        "print('class balance:', int(y.sum()), 'spam ·', int((1 - y).sum()), 'not-spam')",
    ),
    md(
        "### Plot it",
    ),
    code(
        "plt.scatter(X[y == 0, 0], X[y == 0, 1], s=40, color='#00E5FF', label='not spam', edgecolor='black', linewidth=0.5)",
        "plt.scatter(X[y == 1, 0], X[y == 1, 1], s=40, color='#FF4081', label='spam',     edgecolor='black', linewidth=0.5)",
        "plt.xlabel('suspicious-word count')",
        "plt.ylabel('capitalization ratio')",
        "plt.title('Spam vs not-spam (synthetic)')",
        "plt.legend()",
        "plt.show()",
    ),

    # ── 3. Try linear regression — watch it break ───────────────
    md(
        "## 3. Try linear regression first — watch it break",
        "",
        "The labels are 0 and 1. Linear regression fits any numbers — let's plug it in and see what we get.",
    ),
    code(
        "from sklearn.linear_model import LinearRegression",
        "",
        "lr_bad = LinearRegression()",
        "lr_bad.fit(X, y)",
        "",
        "# Predict for a few example points",
        "examples = np.array([[0.5, 0.0], [3.0, 2.0], [6.0, 5.5], [10.0, 8.0]])",
        "for ex in examples:",
        "    pred = lr_bad.predict(ex.reshape(1, -1))[0]",
        "    print(f'  features {ex} -> predicted label {pred:+.3f}')",
        "",
        "# Some predictions are negative. Others are > 1. Probabilities are supposed to be in [0, 1].",
        "# Linear regression doesn't know about that constraint.",
    ),

    # ── 4. The sigmoid function ─────────────────────────────────
    md(
        "## 4. The sigmoid function",
        "",
        "Sigmoid squashes any real number into `(0, 1)`. It's the function we need.",
        "",
        "$$\\sigma(z) = \\frac{1}{1 + e^{-z}}$$",
    ),
    code(
        "def sigmoid(z):",
        "    return 1 / (1 + np.exp(-z))",
        "",
        "# Some values",
        "for z in [-7, -2, 0, 2, 7]:",
        "    print(f'  σ({z:+}) = {sigmoid(z):.4f}')",
    ),
    md(
        "### Plot it",
        "",
        "The S-shape. Asymptotes at 0 and 1 that it never reaches.",
    ),
    code(
        "zs = np.linspace(-10, 10, 200)",
        "plt.plot(zs, sigmoid(zs), color='#FF4081', linewidth=2.5)",
        "plt.axhline(0, color='gray', linewidth=0.5)",
        "plt.axhline(1, color='gray', linewidth=0.5)",
        "plt.axvline(0, color='gray', linewidth=0.5)",
        "plt.xlabel('z')",
        "plt.ylabel('σ(z)')",
        "plt.title('The sigmoid — squashes any real number into (0, 1)')",
        "plt.show()",
    ),

    # ── 5. Log loss vs MSE ──────────────────────────────────────
    md(
        "## 5. Log loss — the right loss for sigmoid outputs",
        "",
        "MSE breaks here because sigmoid's flat tails kill the gradient when the model is confidently wrong. Log loss stays steep.",
        "",
        "$$L = -\\frac{1}{N}\\sum_i \\left[ y_i \\log(\\hat{y}_i) + (1 - y_i) \\log(1 - \\hat{y}_i) \\right]$$",
    ),
    code(
        "def log_loss(y_true, y_pred):",
        "    # Clip to avoid log(0)",
        "    y_pred = np.clip(y_pred, 1e-9, 1 - 1e-9)",
        "    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))",
        "",
        "# Test: if the truth is 1 and the model predicts...",
        "for p in [0.99, 0.7, 0.5, 0.3, 0.01]:",
        "    print(f'  truth=1, pred={p}  ->  log loss = {log_loss(np.array([1]), np.array([p])):.4f}')",
    ),
    md(
        "### Plot the two loss curves",
        "",
        "For true=1, the loss is `-log(p)`. Confidently right (p near 1) → tiny loss. Confidently wrong (p near 0) → loss blows up.",
        "",
        "For true=0, mirrored — `-log(1-p)`.",
    ),
    code(
        "ps = np.linspace(0.001, 0.999, 200)",
        "fig, axes = plt.subplots(1, 2, figsize=(12, 4))",
        "",
        "axes[0].plot(ps, -np.log(ps), color='#FF4081', linewidth=2.5)",
        "axes[0].set_xlabel('predicted probability p')",
        "axes[0].set_ylabel('loss')",
        "axes[0].set_title('truth = 1   →   loss = -log(p)')",
        "axes[0].set_ylim(0, 6)",
        "",
        "axes[1].plot(ps, -np.log(1 - ps), color='#00E5FF', linewidth=2.5)",
        "axes[1].set_xlabel('predicted probability p')",
        "axes[1].set_ylabel('loss')",
        "axes[1].set_title('truth = 0   →   loss = -log(1 - p)')",
        "axes[1].set_ylim(0, 6)",
        "",
        "plt.tight_layout()",
        "plt.show()",
    ),

    # ── 6. Manual training ──────────────────────────────────────
    md(
        "## 6. Train it by hand",
        "",
        "Three weights this time: `w₁`, `w₂` (one per feature), and `b`. Gradient descent is the same loop as linear regression with the substitutions.",
    ),
    code(
        "def predict_prob(W, b, X):",
        "    z = X @ W + b",
        "    return sigmoid(z)",
        "",
        "def grad_log(W, b, X, y):",
        "    p = predict_prob(W, b, X)",
        "    errs = p - y",
        "    dW = (X.T @ errs) / len(y)",
        "    db = np.mean(errs)",
        "    return dW, db",
        "",
        "# Initialize",
        "W = np.zeros(2)",
        "b = 0.0",
        "lr = 0.1",
        "",
        "history = []",
        "for step in range(500):",
        "    dW, db = grad_log(W, b, X, y)",
        "    W -= lr * dW",
        "    b -= lr * db",
        "    history.append(log_loss(y, predict_prob(W, b, X)))",
        "",
        "print(f'final W = {W.round(3)}   b = {b:.3f}   log loss = {history[-1]:.4f}')",
    ),
    md(
        "### Loss curve",
    ),
    code(
        "plt.plot(history, color='#FF4081', linewidth=2)",
        "plt.xlabel('step')",
        "plt.ylabel('log loss')",
        "plt.title('Training — loss going down over 500 iterations')",
        "plt.show()",
    ),
    md(
        "### The decision boundary",
        "",
        "Plot the trained model's decision boundary over the data. For logistic regression, the boundary is the line where the predicted probability equals 0.5 — equivalently, where `W·x + b = 0`.",
    ),
    code(
        "# Boundary: w0·x0 + w1·x1 + b = 0  →  x1 = -(w0·x0 + b) / w1",
        "x0_range = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)",
        "boundary_x1 = -(W[0] * x0_range + b) / W[1]",
        "",
        "plt.scatter(X[y == 0, 0], X[y == 0, 1], s=40, color='#00E5FF', label='not spam', edgecolor='black', linewidth=0.5)",
        "plt.scatter(X[y == 1, 0], X[y == 1, 1], s=40, color='#FF4081', label='spam',     edgecolor='black', linewidth=0.5)",
        "plt.plot(x0_range, boundary_x1, color='#FFD27F', linewidth=2.5, label='decision boundary')",
        "plt.xlabel('suspicious-word count')",
        "plt.ylabel('capitalization ratio')",
        "plt.title('Logistic regression — decision boundary (probability = 0.5)')",
        "plt.legend()",
        "plt.show()",
    ),

    # ── 7. PyTorch ─────────────────────────────────────────────
    md(
        "## 7. Same thing in PyTorch — the 5-line loop, two changes from linear regression",
        "",
        "Same five-line training loop. Two substitutions: add a sigmoid in the forward pass, use binary cross-entropy as the loss.",
        "",
        "`nn.BCEWithLogitsLoss` combines sigmoid + BCE in one call (more numerically stable than doing them separately).",
    ),
    code(
        "import torch",
        "import torch.nn as nn",
        "",
        "X_t = torch.tensor(X, dtype=torch.float32)",
        "y_t = torch.tensor(y, dtype=torch.float32).view(-1, 1)",
        "",
        "model = nn.Linear(2, 1)   # 2 features in, 1 logit out",
        "optimizer = torch.optim.SGD(model.parameters(), lr=0.1)",
        "loss_fn = nn.BCEWithLogitsLoss()",
        "",
        "# THE 5-LINE TRAINING LOOP",
        "for step in range(500):",
        "    logits = model(X_t)",
        "    loss = loss_fn(logits, y_t)",
        "    loss.backward()",
        "    optimizer.step()",
        "    optimizer.zero_grad()",
        "",
        "W_torch = model.weight.detach().numpy().flatten()",
        "b_torch = model.bias.item()",
        "print(f'PyTorch:  W={W_torch.round(3)}  b={b_torch:.3f}')",
        "print(f'By-hand:  W={W.round(3)}  b={b:.3f}')",
    ),

    # ── 8. Sklearn ─────────────────────────────────────────────
    md(
        "## 8. Same thing in sklearn — 3 lines",
    ),
    code(
        "from sklearn.linear_model import LogisticRegression",
        "",
        "model_sk = LogisticRegression()",
        "model_sk.fit(X, y)",
        "",
        "print(f'sklearn coefficients:  {model_sk.coef_[0].round(3)}')",
        "print(f'sklearn intercept:     {model_sk.intercept_[0]:.3f}')",
        "",
        "# Predict probabilities for some example emails",
        "examples = np.array([[0.5, 0.0], [3.0, 2.0], [6.0, 5.5]])",
        "probs = model_sk.predict_proba(examples)",
        "for ex, p in zip(examples, probs):",
        "    print(f'  features {ex}  ->  P(not spam)={p[0]:.3f}  P(spam)={p[1]:.3f}')",
    ),

    # ── 9. Read the trained model ──────────────────────────────
    md(
        "## 9. What does the trained model say?",
        "",
        "The coefficients tell you the *direction* and *strength* of each feature's effect on the log-odds of spam. Large positive coefficient → that feature pushes toward 'spam'.",
    ),
    code(
        "coef_word  = model_sk.coef_[0][0]",
        "coef_caps  = model_sk.coef_[0][1]",
        "intercept  = model_sk.intercept_[0]",
        "",
        "print('The trained classifier says:')",
        "print(f'  each extra suspicious word adds {coef_word:.2f} to the log-odds of spam')",
        "print(f'  each unit of caps ratio adds   {coef_caps:.2f}')",
        "print(f'  baseline log-odds (no features): {intercept:.2f}')",
        "",
        "print()",
        "print('In odds-multiplier terms (e^coef):')",
        "print(f'  one more suspicious word multiplies the odds by  {np.exp(coef_word):.2f}x')",
        "print(f'  one unit more caps ratio multiplies the odds by  {np.exp(coef_caps):.2f}x')",
    ),

    # ── 10. Recap ──────────────────────────────────────────────
    md(
        "## 10. What we did",
        "",
        "- Set up a binary classification problem (spam vs not-spam).",
        "- Showed why linear regression fails — outputs go negative and above 1.",
        "- Introduced the sigmoid (squash into `(0, 1)`) and log loss (the right loss for sigmoid outputs).",
        "- Trained a logistic regression three ways: by-hand gradient descent, PyTorch's 5-line loop with sigmoid + BCE, and sklearn's 3 lines.",
        "- All three agree.",
        "- Read the trained model's coefficients as multiplicative effects on the odds.",
        "",
        "**Next: classification metrics.** Confusion matrix, precision, recall, ROC. How to know whether your classifier is actually good.",
    ),
]

write_notebook(log_cells, HERE / "02-logistic-regression-complete.ipynb")
write_notebook(make_live_version(log_cells), HERE / "02-logistic-regression-live.ipynb")

print("\nDone. Open any of the 4 notebooks with:  jupyter notebook")
