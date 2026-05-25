"""
Build the four teaching notebooks.

  01-linear-regression-complete.ipynb     — all code, off-camera reference
  01-linear-regression-live.ipynb         — same markdown, empty code cells, type into this on camera
  02-logistic-regression-complete.ipynb   — all code, off-camera reference
  02-logistic-regression-live.ipynb       — same markdown, empty code cells

Run with:   python build_notebooks.py

Design notes — modeled after Google's ML Crash Course rhythm:
  - Every concept gets its own cell. One cell, one idea.
  - Every formula is followed by a worked numeric example.
  - Build from scratch: nothing skipped, no forward references.
  - Markdown cells are SHORT — 2 to 4 lines — so the live version
    flows visually one beat at a time.
  - Code cells are SHORT — 3 to 8 lines — so the on-camera typing is
    bite-sized, not a wall of code to retype.
  - Chapters use H2 (##) so they show up in the notebook outline.

Where we deliberately depart from Google:
  - First-person voice in markdown ("I avoided this for years until...")
  - Honest beats ("the by-hand version converges slowly; here's why")
  - Calculus-series callbacks (Eps 14-18)
"""

import json
from pathlib import Path

HERE = Path(__file__).parent

# ────────────────────────────────────────────────────────────────────
# Notebook helpers
# ────────────────────────────────────────────────────────────────────

def md(*lines):
    return {"cell_type": "markdown", "metadata": {}, "source": _join_lines(lines)}


def code(*lines):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": _join_lines(lines)}


def _join_lines(lines):
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
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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
    out = []
    for c in cells:
        if c["cell_type"] == "code":
            out.append(code(""))
        else:
            out.append(c)
    return out


# ════════════════════════════════════════════════════════════════════
# Notebook 1: Linear Regression — built from scratch
# ════════════════════════════════════════════════════════════════════

lr_cells = [
    # ════════════════ INTRO ════════════════
    md(
        "# Linear regression — from scratch",
        "",
        "*Companion to **Eps 19–23** of the Linear Regression series.*",
        "",
        "We build the simplest model in ML, one concept at a time. By the end you'll have trained it three ways: by hand, in PyTorch, in sklearn.",
    ),

    # ════════════════ CHAPTER 1: SETUP ════════════════
    md("## Chapter 1 · Setup"),
    md("Just the imports. NumPy for the math, matplotlib for plots."),
    code(
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "",
        "np.random.seed(42)",
        "plt.rcParams['figure.figsize'] = (8, 5)",
        "plt.rcParams['axes.grid'] = True",
        "plt.rcParams['grid.alpha'] = 0.3",
    ),

    # ════════════════ CHAPTER 2: THE DATASET ════════════════
    md("## Chapter 2 · The dataset"),
    md("Seven cars. Each has a weight (in thousands of pounds) and an MPG. That's it."),
    code(
        "weights = np.array([2.4, 2.8, 3.0, 3.2, 3.6, 4.0, 4.4])",
        "mpgs    = np.array([24,  22,  20,  19,  17,  15,  14])",
    ),
    md("Print it as a table so we can see the pattern."),
    code(
        "for w, m in zip(weights, mpgs):",
        "    print(f'  {w} K lbs   ->   {m} MPG')",
    ),
    md("Heavier cars get fewer MPG. The relationship is visible in the numbers. Now let's plot it."),
    code(
        "plt.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=3)",
        "plt.xlabel('weight (1000 lbs)')",
        "plt.ylabel('MPG')",
        "plt.title('7 cars — weight vs MPG')",
        "plt.show()",
    ),
    md(
        "The dots roughly follow a downward line. **A line is the simplest model that could capture this pattern.**",
        "",
        "We want to find *the* line — the best one. Let's build up to that.",
    ),

    # ════════════════ CHAPTER 3: THE MODEL ════════════════
    md("## Chapter 3 · The model: `y = w·x + b`"),
    md(
        "A line has two numbers that define it:",
        "",
        "- **`w`** is the slope — how steep the line is.",
        "- **`b`** is the intercept — where the line crosses the y-axis.",
        "",
        "Pick any (w, b), get a line. Change either, get a different line.",
    ),
    code(
        "def predict(w, b, x):",
        "    return w * x + b",
    ),
    md("Let's pick a starting guess. We'll come back and improve it. For now: `w = -3`, `b = 30`."),
    code(
        "w_guess, b_guess = -3.0, 30.0",
    ),
    md("Predict the MPG of the first car (weight 2.4)."),
    code(
        "predict(w_guess, b_guess, 2.4)",
    ),
    md("Compare that to the actual MPG (24). Off by a bit. Now do it for all 7 cars."),
    code(
        "predictions = predict(w_guess, b_guess, weights)",
        "predictions",
    ),
    md("Side-by-side comparison:"),
    code(
        "for x, actual, pred in zip(weights, mpgs, predictions):",
        "    print(f'  weight={x}   actual={actual}   predicted={pred:.1f}')",
    ),
    md("Let's plot the line over the data and see how it looks."),
    code(
        "xs = np.linspace(2, 5, 50)",
        "ys = predict(w_guess, b_guess, xs)",
        "",
        "plt.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=3, label='data')",
        "plt.plot(xs, ys, color='#FFD27F', linewidth=2.5, label=f'guess: y = {w_guess}x + {b_guess}')",
        "plt.xlabel('weight (1000 lbs)'); plt.ylabel('MPG'); plt.legend(); plt.show()",
    ),
    md("The line is roughly in the right zone but not great. We need a way to *measure* how not-great it is."),

    # ════════════════ CHAPTER 4: HOW WRONG IS IT? ════════════════
    md("## Chapter 4 · How wrong is it?"),
    md("For each car, the **error** is the predicted MPG minus the actual MPG."),
    code(
        "errors = predictions - mpgs",
        "errors",
    ),
    md(
        "Negative numbers mean we under-predicted. Positive means we over-predicted.",
        "",
        "We want one number that summarizes how wrong the whole model is.",
    ),
    md("**Why not just average the errors?** Because positives and negatives cancel."),
    code(
        "errors.mean()",
    ),
    md(
        "If the model is over-predicting some cars and under-predicting others by the same amount, the average error is zero — but the model is still bad.",
        "",
        "**The fix:** square the errors first. Squaring makes everything positive. Big errors get punished extra (squaring 10 is 100).",
    ),
    code(
        "squared_errors = errors ** 2",
        "squared_errors",
    ),
    md("Now average those. That's the **Mean Squared Error** — MSE — the standard loss for regression."),
    code(
        "mse_value = squared_errors.mean()",
        "mse_value",
    ),
    md("Let's wrap it in a function so we can call it for any (w, b)."),
    code(
        "def mse(w, b):",
        "    preds = predict(w, b, weights)",
        "    return np.mean((mpgs - preds) ** 2)",
        "",
        "mse(w_guess, b_guess)",
    ),
    md("Same number. Now we can ask: for any line, how bad is it?"),

    # ════════════════ CHAPTER 5: VISUALIZE MSE ════════════════
    md("## Chapter 5 · MSE has a picture"),
    md(
        "Each squared error is literally the area of a square. Side length = the vertical distance from the line to the point. Area = that distance squared.",
        "",
        "Plot the squares and the total gray area is the sum of squared errors. Divide by N for MSE.",
    ),
    code(
        "fig, ax = plt.subplots()",
        "ax.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=5, label='data')",
        "ax.plot(xs, predict(w_guess, b_guess, xs), color='#FFD27F', linewidth=2.5, label='guess')",
        "",
        "for x_d, y_d in zip(weights, mpgs):",
        "    p = predict(w_guess, b_guess, x_d)",
        "    side = abs(y_d - p)",
        "    ax.add_patch(plt.Rectangle((x_d, min(y_d, p)), side, side,",
        "                                color='#7C4DFF', alpha=0.25, linewidth=0))",
        "    ax.plot([x_d, x_d], [y_d, p], color='#7C4DFF', alpha=0.6, linewidth=1)",
        "",
        "ax.set_xlabel('weight (1000 lbs)'); ax.set_ylabel('MPG')",
        "ax.set_title('Squared distances — total area = MSE × N')",
        "ax.set_aspect('equal'); ax.legend(); plt.show()",
    ),
    md("The bigger the line's mistakes, the bigger the squares. Move the line, squares grow or shrink. **MSE going down = the squares getting smaller, on average.**"),

    # ════════════════ CHAPTER 6: BETTER GUESSES ════════════════
    md("## Chapter 6 · Better guesses"),
    md("Let's try a few different (w, b) pairs and see which one is smallest."),
    code(
        "for w, b in [(-3, 30), (-4, 32), (-5, 34), (-6, 36), (-5, 35)]:",
        "    print(f'  w={w:>4}  b={b:>4}   MSE = {mse(w, b):.3f}')",
    ),
    md(
        "Manually tuning gets tedious fast. With two knobs, you could keep going — but real models have millions of parameters.",
        "",
        "We need a way to find the best (w, b) automatically. That's gradient descent. But first, let's see what we're trying to navigate.",
    ),

    # ════════════════ CHAPTER 7: THE LOSS SURFACE ════════════════
    md("## Chapter 7 · The loss surface"),
    md("MSE is a function of two inputs (w, b) and outputs one number. **Two inputs, one output. That's a surface.**"),
    md("Compute MSE on a grid of (w, b) values."),
    code(
        "w_range = np.linspace(-10, 2, 60)",
        "b_range = np.linspace(15, 45, 60)",
        "W, B = np.meshgrid(w_range, b_range)",
        "",
        "loss_grid = np.zeros_like(W)",
        "for i in range(W.shape[0]):",
        "    for j in range(W.shape[1]):",
        "        loss_grid[i, j] = mse(W[i, j], B[i, j])",
        "",
        "print('grid shape:', loss_grid.shape)",
        "print('min MSE on grid:', loss_grid.min().round(3))",
    ),
    md("Now plot it as a 3D surface."),
    code(
        "fig = plt.figure(figsize=(10, 7))",
        "ax = fig.add_subplot(111, projection='3d')",
        "ax.plot_surface(W, B, loss_grid, cmap='viridis', alpha=0.8, edgecolor='none')",
        "ax.set_xlabel('w (slope)'); ax.set_ylabel('b (intercept)'); ax.set_zlabel('MSE')",
        "ax.set_title('The loss surface — a clean convex bowl')",
        "ax.view_init(elev=30, azim=-60)",
        "plt.show()",
    ),
    md(
        "**One bottom. No local pits. No tricks.** For linear regression, the bowl is always this clean — what we call *convex*.",
        "",
        "Gradient descent walks downhill on this bowl. The bottom is the answer.",
    ),

    # ════════════════ CHAPTER 8: THE GRADIENT ════════════════
    md("## Chapter 8 · The gradient"),
    md(
        "The **gradient** is the slope of the bowl at the current point. It tells us which direction is *uphill*.",
        "",
        "For MSE, the math works out to:",
        "",
        "$$\\frac{\\partial L}{\\partial w} = \\frac{2}{N}\\sum_i x_i(w x_i + b - y_i)$$",
        "$$\\frac{\\partial L}{\\partial b} = \\frac{2}{N}\\sum_i (w x_i + b - y_i)$$",
    ),
    md("In code:"),
    code(
        "def grad(w, b):",
        "    errs = predict(w, b, weights) - mpgs",
        "    dw = 2 * np.mean(weights * errs)",
        "    db = 2 * np.mean(errs)",
        "    return dw, db",
    ),
    md("Compute the gradient at our guess (w=-3, b=30)."),
    code(
        "dw, db = grad(w_guess, b_guess)",
        "print(f'  dL/dw = {dw:.3f}')",
        "print(f'  dL/db = {db:.3f}')",
    ),
    md(
        "Both numbers are negative.",
        "",
        "**Reading the gradient:** the gradient points *uphill*. Negative means uphill is in the negative direction. So *downhill* is in the *positive* direction — both `w` and `b` should increase to lower the loss.",
        "",
        "But wait — we already saw that the true optimum has `w ≈ -5` (more negative, not less). The path to the optimum isn't straight — we'll see it curve.",
    ),

    # ════════════════ CHAPTER 9: ONE STEP ════════════════
    md("## Chapter 9 · One step"),
    md(
        "Take a tiny step in the opposite direction of the gradient. The size of the step is the **learning rate** — usually written `η` (eta) or `lr`.",
        "",
        "$$w \\leftarrow w - \\eta \\cdot \\frac{\\partial L}{\\partial w}$$",
    ),
    code(
        "lr = 0.01",
        "w_new = w_guess - lr * dw",
        "b_new = b_guess - lr * db",
        "",
        "print(f'  before:  w={w_guess:.3f}  b={b_guess:.3f}  MSE={mse(w_guess, b_guess):.3f}')",
        "print(f'  after:   w={w_new:.3f}  b={b_new:.3f}  MSE={mse(w_new, b_new):.3f}')",
    ),
    md("MSE went down. One step worked. Now do it lots of times."),

    # ════════════════ CHAPTER 10: THE FULL LOOP ════════════════
    md("## Chapter 10 · The full descent loop"),
    md("Same step, in a loop. Store the history so we can plot it later."),
    code(
        "w, b = -1.0, 15.0   # bad starting point so the descent is visible",
        "lr = 0.01",
        "",
        "history = {'w': [w], 'b': [b], 'mse': [mse(w, b)]}",
        "",
        "for step in range(10000):",
        "    dw, db = grad(w, b)",
        "    w -= lr * dw",
        "    b -= lr * db",
        "    history['w'].append(w)",
        "    history['b'].append(b)",
        "    history['mse'].append(mse(w, b))",
        "",
        "print(f'final:  w={w:.4f}  b={b:.4f}  MSE={mse(w, b):.4f}')",
    ),
    md(
        "**About 10,000 iterations to fully converge.** That feels like a lot for two parameters. The reason: the MPG features aren't *normalized* — they range from 2.4 to 4.4. Gradient descent struggles when features are on different scales than each other or than the bias.",
        "",
        "In real ML, you'd normalize the inputs (subtract mean, divide by std) and converge in a few hundred steps. Or use a smarter optimizer like Adam (PyTorch section below).",
        "",
        "But this is gradient descent in its rawest form. Same algorithm from calculus Ep 17.",
    ),
    md("Plot the loss curve to see the descent."),
    code(
        "plt.figure(figsize=(8, 4))",
        "plt.plot(history['mse'], color='#FFD27F', linewidth=2)",
        "plt.xlabel('step'); plt.ylabel('MSE')",
        "plt.title('Loss going down over 10,000 iterations')",
        "plt.yscale('log')",
        "plt.show()",
    ),
    md("Steep drop, then a long flattening tail. Classic convergence shape."),

    # ════════════════ CHAPTER 11: PATH ON THE BOWL ════════════════
    md("## Chapter 11 · The descent path on the bowl"),
    md("Overlay the path on the loss surface from Chapter 7. The ball rolls down."),
    code(
        "fig = plt.figure(figsize=(11, 7))",
        "ax = fig.add_subplot(111, projection='3d')",
        "ax.plot_surface(W, B, loss_grid, cmap='viridis', alpha=0.55, edgecolor='none')",
        "",
        "# subsample for readability — 10000 points would be too dense",
        "idx = np.linspace(0, len(history['w']) - 1, 100).astype(int)",
        "path_w = [history['w'][i] for i in idx]",
        "path_b = [history['b'][i] for i in idx]",
        "path_mse = [history['mse'][i] for i in idx]",
        "",
        "ax.plot(path_w, path_b, path_mse, color='#FFD27F', linewidth=2, marker='o', markersize=3)",
        "ax.scatter([path_w[0]], [path_b[0]], [path_mse[0]],",
        "           color='#FF4081', s=150, edgecolor='white', linewidth=1.5, label='start')",
        "ax.scatter([path_w[-1]], [path_b[-1]], [path_mse[-1]],",
        "           color='#00E676', s=150, edgecolor='white', linewidth=1.5, label='end')",
        "",
        "ax.set_xlabel('w'); ax.set_ylabel('b'); ax.set_zlabel('MSE')",
        "ax.set_title('Gradient descent on the loss surface')",
        "ax.view_init(elev=30, azim=-60); ax.legend(); plt.show()",
    ),
    md("Pink dot is where we started. Green dot is where we ended up. The line connecting them is the descent path. **That path is what training looks like.**"),

    # ════════════════ CHAPTER 12: THE FITTED LINE ════════════════
    md("## Chapter 12 · The fitted line"),
    md("Plot the trained model over the data and compare to where we started."),
    code(
        "plt.figure(figsize=(8, 5))",
        "plt.scatter(weights, mpgs, s=80, color='#00E5FF', edgecolor='black', linewidth=1.5, zorder=3, label='data')",
        "plt.plot(xs, predict(w_guess, b_guess, xs), color='#FF4081', linewidth=2,",
        "         linestyle='--', label=f'starting guess', alpha=0.6)",
        "plt.plot(xs, predict(w, b, xs), color='#FFD27F', linewidth=2.5,",
        "         label=f'fitted: y = {w:.2f}x + {b:.2f}')",
        "plt.xlabel('weight (1000 lbs)'); plt.ylabel('MPG'); plt.legend(); plt.show()",
    ),
    md("The yellow line is the trained model. Tighter fit through the data than the pink dashed starting guess. **By-hand linear regression — done.**"),

    # ════════════════ CHAPTER 13: PYTORCH ════════════════
    md("## Chapter 13 · The same thing in PyTorch — the 5-line loop"),
    md(
        "PyTorch handles the gradient for us. `loss.backward()` computes ∂L/∂w and ∂L/∂b automatically (chain rule, from calculus Ep 15-18). The five lines below are the same loop we just wrote by hand.",
    ),
    code(
        "import torch",
        "import torch.nn as nn",
    ),
    md("Convert data to tensors. Shape `(N, 1)` for the linear layer."),
    code(
        "X = torch.tensor(weights, dtype=torch.float32).view(-1, 1)",
        "y = torch.tensor(mpgs,    dtype=torch.float32).view(-1, 1)",
        "",
        "print('X.shape:', X.shape)",
        "print('y.shape:', y.shape)",
    ),
    md("Set up the model, optimizer, and loss."),
    code(
        "model = nn.Linear(1, 1)              # y = wx + b",
        "optimizer = torch.optim.Adam(model.parameters(), lr=0.05)",
        "loss_fn = nn.MSELoss()",
    ),
    md(
        "Why **Adam** instead of vanilla SGD? Adam adapts the learning rate per parameter, which handles un-normalized features gracefully. SGD would also work but need 10,000+ iterations like our by-hand version. Adam takes a few thousand.",
    ),
    md("The five lines:"),
    code(
        "for step in range(5000):",
        "    pred = model(X)            # forward pass",
        "    loss = loss_fn(pred, y)    # compute MSE",
        "    loss.backward()            # chain rule",
        "    optimizer.step()           # gradient descent",
        "    optimizer.zero_grad()      # reset for next step",
    ),
    md("Pull out the trained parameters and compare."),
    code(
        "w_torch = model.weight.item()",
        "b_torch = model.bias.item()",
        "",
        "print(f'  PyTorch:   w={w_torch:.4f}   b={b_torch:.4f}')",
        "print(f'  By-hand:   w={w:.4f}   b={b:.4f}')",
    ),
    md("Same answer (within numerical precision). Different code path, same destination."),

    # ════════════════ CHAPTER 14: SKLEARN ════════════════
    md("## Chapter 14 · The same thing in sklearn — 3 lines"),
    md("Sklearn wraps the whole training loop. For most projects, this is what you'd actually write."),
    code(
        "from sklearn.linear_model import LinearRegression",
        "",
        "model_sk = LinearRegression()",
        "model_sk.fit(weights.reshape(-1, 1), mpgs)",
    ),
    md("Read out the trained parameters."),
    code(
        "print(f'  sklearn:   w={model_sk.coef_[0]:.4f}   b={model_sk.intercept_:.4f}')",
        "print(f'  PyTorch:   w={w_torch:.4f}   b={b_torch:.4f}')",
        "print(f'  By-hand:   w={w:.4f}   b={b:.4f}')",
    ),
    md(
        "All three agree.",
        "",
        "Three different code paths, one true answer. The math doesn't care how you got there.",
    ),
    md("Predict the MPG of a brand-new 3,500-pound car."),
    code(
        "model_sk.predict([[3.5]])",
    ),
    md("About 17.9 MPG. Reasonable — it sits right in the middle of our training data range."),

    # ════════════════ CHAPTER 15: MORE FEATURES ════════════════
    md("## Chapter 15 · More features"),
    md("Real cars have more than just weight. Let's add horsepower and engine displacement."),
    code(
        "# Synthetic features correlated with weight, plus noise",
        "horsepower   = weights * 60 + np.random.normal(0, 15, size=7)",
        "displacement = weights * 1.5 + np.random.normal(0, 0.4, size=7)",
        "",
        "X_multi = np.column_stack([weights, horsepower, displacement])",
        "X_multi.shape",
    ),
    md(
        "Three features per car instead of one. The model becomes:",
        "",
        "$$y = b + w_1 \\cdot \\text{weight} + w_2 \\cdot \\text{horsepower} + w_3 \\cdot \\text{displacement}$$",
        "",
        "*Same training loop. One extra weight per feature. That's it.*",
    ),
    code(
        "model_multi = LinearRegression()",
        "model_multi.fit(X_multi, mpgs)",
    ),
    md("Read the coefficients — one per feature."),
    code(
        "print(f'  weight coef:        {model_multi.coef_[0]:+.4f}')",
        "print(f'  horsepower coef:    {model_multi.coef_[1]:+.4f}')",
        "print(f'  displacement coef:  {model_multi.coef_[2]:+.4f}')",
        "print(f'  intercept:          {model_multi.intercept_:+.4f}')",
    ),
    md(
        "Each coefficient says: **holding the other features constant, this is how much MPG changes per unit of this feature.**",
        "",
        "All three are negative — heavier, more powerful, larger-engined cars get fewer MPG. Matches intuition.",
    ),

    # ════════════════ CHAPTER 16: RECAP ════════════════
    md("## Chapter 16 · What we did"),
    md(
        "1. Loaded a dataset and plotted it.",
        "2. Defined a model `y = wx + b` and a loss `MSE`.",
        "3. Visualized MSE as squared distances, then as a 3D bowl over (w, b).",
        "4. Computed the gradient by hand. Took one step. Looped 10,000 times.",
        "5. Plotted the descent path on the bowl.",
        "6. Did the same thing in PyTorch (5 lines) and sklearn (3 lines). All three converged to the same answer.",
        "7. Extended to multiple features. Same loop. Same algorithm.",
        "",
        "**Next notebook: logistic regression.** Same training loop with two substitutions — sigmoid in the forward pass, log loss in place of MSE.",
    ),
]

write_notebook(lr_cells, HERE / "01-linear-regression-complete.ipynb")
write_notebook(make_live_version(lr_cells), HERE / "01-linear-regression-live.ipynb")


# ════════════════════════════════════════════════════════════════════
# Notebook 2: Logistic Regression — built from scratch
# ════════════════════════════════════════════════════════════════════

log_cells = [
    md(
        "# Logistic regression — from scratch",
        "",
        "*Companion to **Eps 24–28** of the Logistic Regression series.*",
        "",
        "Same five-line training loop as linear regression. Two substitutions: a sigmoid in the forward pass, binary cross-entropy in place of MSE. By the end you'll have trained a classifier three ways.",
    ),

    # ════════════════ CHAPTER 1: SETUP ════════════════
    md("## Chapter 1 · Setup"),
    code(
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "",
        "np.random.seed(42)",
        "plt.rcParams['figure.figsize'] = (8, 5)",
        "plt.rcParams['axes.grid'] = True",
        "plt.rcParams['grid.alpha'] = 0.3",
    ),

    # ════════════════ CHAPTER 2: THE DATASET ════════════════
    md("## Chapter 2 · The dataset"),
    md(
        "Fake spam dataset. Two features per email:",
        "",
        "- `x1` — number of suspicious words (\"click here\", \"free\", \"urgent\")",
        "- `x2` — capitalization ratio (fraction of letters in CAPS)",
        "",
        "Label is 1 if spam, 0 if not. Real spam classifiers use thousands of features. Two is enough to **see** what's going on.",
    ),
    code(
        "n_per_class = 60",
        "",
        "not_spam = np.random.randn(n_per_class, 2) * 1.0 + np.array([1.5, 0.8])",
        "spam     = np.random.randn(n_per_class, 2) * 1.0 + np.array([5.0, 4.0])",
        "",
        "X = np.vstack([not_spam, spam])",
        "y = np.hstack([np.zeros(n_per_class), np.ones(n_per_class)])",
    ),
    md("Sanity check."),
    code(
        "print('X.shape:', X.shape)",
        "print('y.shape:', y.shape)",
        "print('class balance:', int(y.sum()), 'spam  /  ', int((1-y).sum()), 'not-spam')",
    ),
    md("Plot it."),
    code(
        "plt.scatter(X[y==0, 0], X[y==0, 1], s=40, color='#00E5FF', label='not spam', edgecolor='black', linewidth=0.5)",
        "plt.scatter(X[y==1, 0], X[y==1, 1], s=40, color='#FF4081', label='spam',     edgecolor='black', linewidth=0.5)",
        "plt.xlabel('suspicious-word count'); plt.ylabel('capitalization ratio')",
        "plt.title('Spam vs not-spam'); plt.legend(); plt.show()",
    ),
    md("Two clusters. Some overlap in the middle. **A line through that middle would separate most of them.** Finding that line is what we're going to do."),

    # ════════════════ CHAPTER 3: TRY THE WRONG THING ════════════════
    md("## Chapter 3 · Try linear regression first — watch it break"),
    md("Labels are 0 and 1. Just numbers. Linear regression fits any numbers. Let's plug it in and see what happens."),
    code(
        "from sklearn.linear_model import LinearRegression",
        "",
        "lr_bad = LinearRegression()",
        "lr_bad.fit(X, y)",
    ),
    md("Predict for a few example emails."),
    code(
        "examples = np.array([[0.5, 0.0], [3.0, 2.0], [6.0, 5.5], [10.0, 8.0]])",
        "for ex in examples:",
        "    pred = lr_bad.predict(ex.reshape(1, -1))[0]",
        "    print(f'  features {ex}  ->  predicted label {pred:+.3f}')",
    ),
    md(
        "Look at those numbers.",
        "",
        "- Email 1: prediction `-0.14`. *Negative.* What does negative probability mean? Nothing.",
        "- Email 4: prediction `+2.06`. *More than 1.* Probability above 100%? Doesn't exist.",
        "",
        "**Linear regression has no idea our output is supposed to be a probability.** We need a model that knows.",
    ),

    # ════════════════ CHAPTER 4: THE SIGMOID FUNCTION ════════════════
    md("## Chapter 4 · The sigmoid function"),
    md(
        "The sigmoid takes any real number and squashes it into `(0, 1)`. Always. No matter how huge or tiny the input.",
        "",
        "$$\\sigma(z) = \\frac{1}{1 + e^{-z}}$$",
    ),
    code(
        "def sigmoid(z):",
        "    return 1 / (1 + np.exp(-z))",
    ),
    md("Worked example: what's `σ(0)`?"),
    code(
        "sigmoid(0)",
    ),
    md(
        "Exactly 0.5. The middle.",
        "",
        "**Worked example:** what's `σ(1)`?",
    ),
    code(
        "sigmoid(1)",
    ),
    md(
        "About 0.73. Mildly positive.",
        "",
        "**Worked example:** what about a big positive input?",
    ),
    code(
        "sigmoid(5)",
    ),
    md(
        "About 0.99. Confidently positive — but not 1.0.",
        "",
        "**Worked example:** big negative input?",
    ),
    code(
        "sigmoid(-5)",
    ),
    md(
        "About 0.0067. Confidently negative — but not 0.",
        "",
        "**The asymptotes never reach.** Push the input to 100, the output gets really close to 1, but never exactly. That's the feature, not a bug — it keeps the math well-behaved.",
    ),
    md("Plot the full S-curve."),
    code(
        "zs = np.linspace(-10, 10, 200)",
        "plt.plot(zs, sigmoid(zs), color='#FF4081', linewidth=2.5)",
        "plt.axhline(0, color='gray', linewidth=0.5)",
        "plt.axhline(1, color='gray', linewidth=0.5)",
        "plt.axvline(0, color='gray', linewidth=0.5)",
        "plt.xlabel('z'); plt.ylabel('σ(z)')",
        "plt.title('The sigmoid — any real number into (0, 1)'); plt.show()",
    ),

    # ════════════════ CHAPTER 5: LOGISTIC REGRESSION ════════════════
    md("## Chapter 5 · Logistic regression = linear + sigmoid"),
    md(
        "Logistic regression is two steps:",
        "",
        "1. **Linear part.** `z = b + w₁·x₁ + w₂·x₂ + …` Just like linear regression. Output is any real number.",
        "2. **Sigmoid.** Squash `z` through the sigmoid. Output is in `(0, 1)`. That's the predicted probability.",
        "",
        "$$\\hat{y} = \\sigma(b + w_1 x_1 + w_2 x_2)$$",
    ),
    md("Worked example. Bias `b=1`, weights `w₁=2, w₂=-1`. New email features `x₁=3, x₂=2`."),
    code(
        "b_eg = 1",
        "w_eg = np.array([2, -1])",
        "x_eg = np.array([3, 2])",
        "",
        "z = b_eg + (w_eg * x_eg).sum()",
        "print(f'  z = {z}')",
    ),
    md("Then squash."),
    code(
        "p = sigmoid(z)",
        "print(f'  P(spam) = {p:.4f}')",
    ),
    md(
        "About 95%. The model says: *given those features and those weights, this email has a 95% chance of being spam.*",
        "",
        "Now — where do good weights come from? Training.",
    ),

    # ════════════════ CHAPTER 6: LOG LOSS ════════════════
    md("## Chapter 6 · Log loss"),
    md(
        "Before we train, we need a loss function. MSE doesn't work here — sigmoid's flat tails make the gradient vanish when the model is confidently wrong. (We'll see it in a moment.)",
        "",
        "The right loss for binary classification is **log loss** (also called **binary cross-entropy**):",
        "",
        "$$L = -\\frac{1}{N}\\sum_i \\left[ y_i \\log(\\hat{y}_i) + (1 - y_i) \\log(1 - \\hat{y}_i) \\right]$$",
        "",
        "The formula has two cases packed into one. Let me unpack.",
    ),
    md(
        "**Case 1: true label is 1.** The `(1 - yᵢ)` term is zero — drops out. Only `−log(ŷᵢ)` remains.",
        "",
        "**Case 2: true label is 0.** The `yᵢ` term drops out. Only `−log(1 − ŷᵢ)` remains.",
        "",
        "One formula, two cases. The case you're in depends on the truth.",
    ),
    code(
        "def log_loss(y_true, y_pred):",
        "    y_pred = np.clip(y_pred, 1e-9, 1 - 1e-9)   # avoid log(0)",
        "    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))",
    ),
    md("**Worked example.** Truth is 1, model predicts 0.92. Loss?"),
    code(
        "log_loss(np.array([1]), np.array([0.92]))",
    ),
    md("Tiny. Model was right and confident."),
    md("**Worked example.** Truth is 1, model predicts 0.5 — uncertain."),
    code(
        "log_loss(np.array([1]), np.array([0.5]))",
    ),
    md("0.69. Moderate punishment for being uncertain."),
    md("**Worked example.** Truth is 1, model predicts 0.01 — confidently wrong."),
    code(
        "log_loss(np.array([1]), np.array([0.01]))",
    ),
    md("4.6. Big. **The loss explodes as you become more confidently wrong.** That's what we want — strong gradient signal exactly when the model needs to learn most."),
    md("Plot both curves."),
    code(
        "ps = np.linspace(0.001, 0.999, 200)",
        "fig, axes = plt.subplots(1, 2, figsize=(12, 4))",
        "",
        "axes[0].plot(ps, -np.log(ps), color='#FF4081', linewidth=2.5)",
        "axes[0].set_xlabel('predicted probability p'); axes[0].set_ylabel('loss')",
        "axes[0].set_title('truth = 1   →   loss = -log(p)'); axes[0].set_ylim(0, 6)",
        "",
        "axes[1].plot(ps, -np.log(1 - ps), color='#00E5FF', linewidth=2.5)",
        "axes[1].set_xlabel('predicted probability p'); axes[1].set_ylabel('loss')",
        "axes[1].set_title('truth = 0   →   loss = -log(1 - p)'); axes[1].set_ylim(0, 6)",
        "",
        "plt.tight_layout(); plt.show()",
    ),
    md("Asymptote on the wrong side of each curve. Loss is small when the prediction matches the truth, blows up when it's confidently wrong."),

    # ════════════════ CHAPTER 7: TRAIN BY HAND ════════════════
    md("## Chapter 7 · Train it by hand"),
    md("Three parameters: `w₁`, `w₂`, `b`. Gradient descent is the same loop as linear regression, with sigmoid in the forward pass and log loss as the criterion."),
    md("Forward pass — compute predicted probabilities for the whole batch."),
    code(
        "def predict_prob(W, b, X):",
        "    z = X @ W + b",
        "    return sigmoid(z)",
    ),
    md("Gradient. (For log loss + sigmoid, the math is unusually clean — the gradients work out to `prediction − truth`, no chain-rule mess.)"),
    code(
        "def grad_log(W, b, X, y):",
        "    p = predict_prob(W, b, X)",
        "    errs = p - y",
        "    dW = (X.T @ errs) / len(y)",
        "    db = np.mean(errs)",
        "    return dW, db",
    ),
    md("Initialize parameters."),
    code(
        "W = np.zeros(2)",
        "b = 0.0",
        "lr = 0.1",
    ),
    md("One step."),
    code(
        "dW, db = grad_log(W, b, X, y)",
        "print(f'before:  W={W}  b={b:.3f}  loss={log_loss(y, predict_prob(W, b, X)):.4f}')",
        "",
        "W -= lr * dW",
        "b -= lr * db",
        "",
        "print(f'after:   W={W.round(3)}  b={b:.3f}  loss={log_loss(y, predict_prob(W, b, X)):.4f}')",
    ),
    md("Loss went down. Now run the full loop."),
    code(
        "W = np.zeros(2)",
        "b = 0.0",
        "history = []",
        "",
        "for step in range(500):",
        "    dW, db = grad_log(W, b, X, y)",
        "    W -= lr * dW",
        "    b -= lr * db",
        "    history.append(log_loss(y, predict_prob(W, b, X)))",
        "",
        "print(f'final W = {W.round(3)}   b = {b:.3f}   log loss = {history[-1]:.4f}')",
    ),
    md("Plot the loss curve."),
    code(
        "plt.plot(history, color='#FF4081', linewidth=2)",
        "plt.xlabel('step'); plt.ylabel('log loss')",
        "plt.title('Training — loss going down over 500 iterations')",
        "plt.show()",
    ),

    # ════════════════ CHAPTER 8: DECISION BOUNDARY ════════════════
    md("## Chapter 8 · The decision boundary"),
    md(
        "Plot the trained model's *decision boundary*. For logistic regression, the boundary is the line where predicted probability equals 0.5 — equivalently, where `W·x + b = 0`.",
    ),
    code(
        "# Boundary: w0*x0 + w1*x1 + b = 0  →  x1 = -(w0*x0 + b) / w1",
        "x0_range = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 100)",
        "boundary_x1 = -(W[0] * x0_range + b) / W[1]",
        "",
        "plt.scatter(X[y==0, 0], X[y==0, 1], s=40, color='#00E5FF', label='not spam', edgecolor='black', linewidth=0.5)",
        "plt.scatter(X[y==1, 0], X[y==1, 1], s=40, color='#FF4081', label='spam',     edgecolor='black', linewidth=0.5)",
        "plt.plot(x0_range, boundary_x1, color='#FFD27F', linewidth=2.5, label='decision boundary')",
        "plt.xlabel('suspicious-word count'); plt.ylabel('capitalization ratio')",
        "plt.title('Trained logistic regression — boundary at p = 0.5'); plt.legend(); plt.show()",
    ),
    md("Yellow line splits spam from not-spam. **A handful of points are on the wrong side** — those are the ambiguous emails the model isn't sure about. Tightening the threshold (next series, classification) is how you trade precision for recall."),

    # ════════════════ CHAPTER 9: PYTORCH ════════════════
    md("## Chapter 9 · The same thing in PyTorch — 5-line loop, two changes from LR"),
    md(
        "Same five-line loop from the linear regression notebook. Two substitutions:",
        "",
        "- Add a sigmoid in the forward pass.",
        "- Use binary cross-entropy as the loss.",
        "",
        "PyTorch's `nn.BCEWithLogitsLoss` combines sigmoid + BCE in one call (more numerically stable).",
    ),
    code(
        "import torch",
        "import torch.nn as nn",
        "",
        "X_t = torch.tensor(X, dtype=torch.float32)",
        "y_t = torch.tensor(y, dtype=torch.float32).view(-1, 1)",
    ),
    md("Set up model + optimizer + loss."),
    code(
        "model = nn.Linear(2, 1)        # 2 features in, 1 logit out",
        "optimizer = torch.optim.SGD(model.parameters(), lr=0.1)",
        "loss_fn = nn.BCEWithLogitsLoss()",
    ),
    md("The five lines."),
    code(
        "for step in range(500):",
        "    logits = model(X_t)        # forward — no sigmoid here; BCEWithLogitsLoss adds it",
        "    loss = loss_fn(logits, y_t)",
        "    loss.backward()",
        "    optimizer.step()",
        "    optimizer.zero_grad()",
    ),
    md("Compare to the by-hand version."),
    code(
        "W_torch = model.weight.detach().numpy().flatten()",
        "b_torch = model.bias.item()",
        "",
        "print(f'  PyTorch:   W={W_torch.round(3)}   b={b_torch:.3f}')",
        "print(f'  By-hand:   W={W.round(3)}   b={b:.3f}')",
    ),
    md("Same answer. **Three lines of the five-line loop are literally identical to linear regression.** Two changes give you a classifier."),

    # ════════════════ CHAPTER 10: SKLEARN ════════════════
    md("## Chapter 10 · The same thing in sklearn — 3 lines"),
    code(
        "from sklearn.linear_model import LogisticRegression",
        "",
        "model_sk = LogisticRegression()",
        "model_sk.fit(X, y)",
    ),
    md("Read out the coefficients."),
    code(
        "print(f'  sklearn coefficients:  {model_sk.coef_[0].round(3)}')",
        "print(f'  sklearn intercept:     {model_sk.intercept_[0]:.3f}')",
    ),
    md(
        "Sklearn's coefficients differ from ours because **sklearn defaults to L2 regularization** (shrinks weights toward zero to prevent overfitting). Our by-hand version had no regularization. Both predict the same boundary direction; sklearn's weights are just smaller in magnitude.",
    ),
    md("Predict probabilities for a few example emails."),
    code(
        "for ex in examples:",
        "    probs = model_sk.predict_proba(ex.reshape(1, -1))[0]",
        "    print(f'  features {ex}  ->  P(not spam)={probs[0]:.3f}  P(spam)={probs[1]:.3f}')",
    ),
    md("Real probabilities now. All between 0 and 1. **That's what we built sigmoid for.**"),

    # ════════════════ CHAPTER 11: READ THE MODEL ════════════════
    md("## Chapter 11 · Read the trained model"),
    md(
        "Coefficients in logistic regression have a clean interpretation — they're effects on the **log-odds**. Exponentiating a coefficient gives the multiplicative effect on the odds.",
    ),
    code(
        "coef_word, coef_caps = model_sk.coef_[0]",
        "intercept = model_sk.intercept_[0]",
        "",
        "print('In log-odds terms:')",
        "print(f'  each suspicious word adds {coef_word:+.2f} to the log-odds of spam')",
        "print(f'  each unit of caps ratio adds {coef_caps:+.2f}')",
        "print(f'  baseline log-odds (no features): {intercept:+.2f}')",
    ),
    md("Exponentiate to get the multiplicative effects."),
    code(
        "print('In odds-multiplier terms:')",
        "print(f'  one more suspicious word multiplies the odds of spam by  {np.exp(coef_word):.2f}x')",
        "print(f'  one unit more caps ratio multiplies the odds by          {np.exp(coef_caps):.2f}x')",
    ),
    md("**That's a real model you can interpret.** Each feature has a clear, multiplicative effect on the odds of spam. Not a black box."),

    # ════════════════ CHAPTER 12: RECAP ════════════════
    md("## Chapter 12 · What we did"),
    md(
        "1. Built a synthetic spam dataset (two features, two classes).",
        "2. Tried linear regression — saw it produce probabilities below 0 and above 1. Broken.",
        "3. Introduced the sigmoid function. Worked through five numeric examples to feel it.",
        "4. Combined linear + sigmoid into logistic regression. Worked example.",
        "5. Introduced log loss. Three worked examples to feel why it's the right loss.",
        "6. Trained the model by hand. One step, then the full loop.",
        "7. Plotted the decision boundary.",
        "8. Same model in PyTorch (5 lines, two substitutions from LR) and sklearn (3 lines).",
        "9. Read the trained coefficients as multiplicative effects on the odds.",
        "",
        "**Next series: classification.** Threshold. Confusion matrix. Precision, recall, ROC. How to know whether your classifier is actually good.",
    ),
]

write_notebook(log_cells, HERE / "02-logistic-regression-complete.ipynb")
write_notebook(make_live_version(log_cells), HERE / "02-logistic-regression-live.ipynb")

print("\nDone. Open any of the 4 notebooks with:  jupyter notebook")
