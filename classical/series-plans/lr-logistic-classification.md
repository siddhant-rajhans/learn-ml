# Series plan — Linear Regression · Logistic Regression · Classification

> 15 episodes (3 series × 5 each) that take a viewer from "train your first real model" to "decide what counts as a good prediction." Cross-mapped to Google's ML Crash Course (which covers the same ground in ~185 minutes of static-ish content), with notes on where our format already wins and where it needs to.

---

## The spine: one training loop, three flavors

The calculus series ended on the five-line PyTorch training step. Every model in these three series uses *that exact loop* — what changes is small and visible.

```
pred = model(x)               #   ← swap in the model class for this series
loss = loss_fn(pred, y)       #   ← swap in the loss function for this series
loss.backward()               #   chain rule (Ep 15)
optimizer.step()              #   gradient descent (Ep 17)
optimizer.zero_grad()         #   bookkeeping (Ep 18)
```

| Series | New piece slotted in | Where everything else came from |
|---|---|---|
| Linear regression | `model = nn.Linear(d, 1)`; loss = MSE | gradient descent (Ep 17), chain rule (Ep 15), forward+backward (Ep 18) |
| Logistic regression | Add sigmoid; loss = binary cross-entropy | the LR scaffolding, plus a one-function activation swap |
| Classification | The loss-and-training stays. The new layer is **how we measure** the trained model — threshold, confusion matrix, precision/recall, ROC | the trained logistic regressor from the previous series |

Visual callback in every series-1 slide: a faded version of the 5-line loop from Ep 18, with the relevant lines highlighted in this series' color.

That's the spine. Three series, one loop, compounds.

---

## Series 1 — Linear regression (5 episodes)

The first real model. Single dataset throughout (Google uses car-weight → MPG; we can keep it). By the end, the viewer trains a linear regression in five lines and knows what every line is doing.

| Ep | Title | Beat (what they leave with) | Showpiece visual |
|----|-------|------------------------------|-------------------|
| 19 | **What's a model, really?** | A model is a function from inputs to outputs that we *choose* by minimizing how wrong it is. | Scatter of MPG vs car weight. A line you can drag with a slider. Live MSE counter. The viewer can find the best fit by eye, then we tell them the math does it automatically. |
| 20 | **Loss — measuring 'wrong'** | MSE squared-distance intuition. MAE for outliers. Why we square: gradients are smooth. | Same scatter. Now the squared distances render as gray squares between each point and the line. Drag the line → watch the squares grow/shrink. The sum of square areas = MSE, animated as a counter. |
| 21 | **The loss surface, again** | Two knobs (w, b) → 3D bowl. Reuse calculus Ep 17's descent animation, but the surface is the *real* MSE for *real* data. | The bowl, the ball, the descent path. Live overlay: the line on the scatter updates in sync with the ball's position. **This is the moment calculus becomes ML.** |
| 22 | **More features = higher-dimensional bowl** | `y = b + Σwᵢxᵢ`. Same descent loop, longer w vector. Can't see the bowl in d>3, but the math doesn't care. | Side-by-side: 1D fit (one slider), 2D fit (two sliders, a plane), then a "we lose the picture but keep the math" beat — a rotating high-dimensional bowl as a stylized metaphor. |
| 23 | **You can read this** | Show `LinearRegression().fit(X, y)` from sklearn and the equivalent PyTorch 5-line loop. Every line gets a callback to where it came from. | The 5-line loop slide from Ep 18, recolored for LR. Annotation: "this is what `sklearn.fit()` is doing under the hood." Then a live demo: the trained model predicts a new car's MPG, with a confidence wobble. |

### What we improve over Google's images

| Google has | We have |
|---|---|
| Static scatter with annotated best-fit line | Draggable line on the scatter, live MSE counter, the equation updating |
| Static 3D bowl render | Animated descent ball traversing the bowl, with the scatter-plot line synced to ball position |
| "Multi-feature" handwave | A visual progression: 1D line → 2D plane → "you can't see 5D but here's a stylized rotation" |
| External programming exercise | An in-deck playground reference — the viewer can clone the repo and run the same training loop locally |

---

## Series 2 — Logistic regression (5 episodes)

The first model that predicts a *probability*. Bridge from "the answer is a number" to "the answer is a yes/no." Iris (or spam, like Google) as the throughline dataset.

| Ep | Title | Beat (what they leave with) | Showpiece visual |
|----|-------|------------------------------|-------------------|
| 24 | **When the answer isn't a number** | Try to use linear regression for "is this spam?" Labels are 0 and 1. Linear gives `-2.3` and `+14.7`. Comically wrong. We need outputs in `[0, 1]`. | Scatter of spam (1) vs not-spam (0) on a feature axis. Try to fit a line through it. The line goes out of bounds in both directions. Visual breakdown. |
| 25 | **The sigmoid function** | `σ(z) = 1/(1+e⁻ᶻ)`. The S-curve. Squashes any real number into `(0, 1)`. The asymptotes never reach. **The log-odds derivation** as the punchline: `z = ln(y/(1-y))`. | The S-curve, but as an *interactive animation*: a slider for z, output dot traces the S in real time. Push z to 10 and see σ=0.99995 (but never 1). The "z and y" two-way arrow showing the inverse relationship. |
| 26 | **Log loss — why squared error breaks here** | Sigmoid's flat tails mean MSE has tiny gradients near the wrong answer. Log loss explodes when the model is confidently wrong. Derivation: `-[y log p + (1-y) log(1-p)]`. | Two curves side by side: `-log(p)` for true=1 (asymptote on the left, gentle on the right) and `-log(1-p)` for true=0. Drag p along each — feel the loss explode as confidence in the wrong direction grows. |
| 27 | **Training a logistic regression** | Same training loop. Only difference: the model now has sigmoid at the end, and we use BCE loss. Watch the decision boundary move during training. | Iris scatter (sepal length vs petal length, one species vs rest). A boundary line animates across the plane as training progresses. The line is `wx + b = 0` shown explicitly. |
| 28 | **You can read this** | `LogisticRegression().fit()` in sklearn. The same five-line PyTorch loop with two substitutions. | The 5-line loop slide again — now with sigmoid + BCE highlighted as the two changes vs LR. **Two episodes in, the viewer sees the pattern.** |

### What we improve over Google's images

| Google has | We have |
|---|---|
| Static sigmoid S-curve with a value table | Interactive z-slider: drag input, see output trace the S, watch asymptotes never reach |
| One static linear-to-sigmoid figure | Animated squashing — a moving dot on the linear `wx+b` line, mirrored onto the sigmoid output |
| Verbal explanation of why squared error fails | Side-by-side log-loss curves with draggable p, showing the gradient-vanishing problem viscerally |
| Decision boundary as a static line | Boundary animation: line moves across the scatter as training progresses, gradient descent visible in 2D |

---

## Series 3 — Classification (5 episodes)

Take a trained probabilistic model and turn it into a decision-making system. This is where the calculus series's "predicting things" arc lands.

| Ep | Title | Beat (what they leave with) | Showpiece visual |
|----|-------|------------------------------|-------------------|
| 29 | **From probability to decision** | Threshold. The spam classifier gives 0.92, 0.51, 0.03 — we pick a cutoff. Why 0.5 isn't always right. The cost-asymmetry beat (false positive vs false negative). | A row of email cards, each with a spam-probability score. A threshold slider above the row. Slide it → cards flip between spam/not-spam color. The "always-predict-negative" classifier at threshold=1.01 shown as obviously broken. |
| 30 | **The confusion matrix** | TP, FP, TN, FN. Not just a table — a way of seeing model behavior. | Scatter of predictions on the iris dataset, color-coded by quadrant: TP green, FP yellow, FN orange, TN gray. Change threshold → dots re-color in real time. The 2×2 grid updates alongside. |
| 31 | **Precision and recall** | Two numbers that say different things. Precision = "of what I said yes, how often was I right?" Recall = "of what was actually yes, how much did I catch?" The 99/1 imbalanced-dataset killer line. | The same confusion-matrix scatter, but now precision and recall display as two animated bars. Slide the threshold → watch precision rise as recall drops. The trade-off is *visceral*, not abstract. |
| 32 | **The ROC curve, drawn** | Sweep the threshold from 1.0 down to 0.0, plot (FPR, TPR) at each point. The curve. AUC = ranking accuracy. | Split screen: left side is the confusion-matrix scatter (animating as threshold sweeps), right side is the ROC curve being *drawn* dot-by-dot in sync. Area under the curve fills in as it traces. |
| 33 | **One model, many classes** | Softmax. One-vs-all. Cross-entropy generalizes. Iris is actually a 3-class problem — show all three. | Bar chart of three class probabilities responding to changing input. Slide the input — bars update, the prediction (argmax) changes. Decision boundaries on the 2D iris plot show three regions. |

### What we improve over Google's images

| Google has | We have |
|---|---|
| Static spam-threshold example | Live threshold slider with cards flipping in real time, the always-negative classifier as a visible failure mode |
| Static confusion matrix table | Scatter of points color-coded by quadrant, threshold updates colors live, table syncs |
| Verbal precision-vs-recall explanation | Animated bars showing the trade-off as you move the threshold |
| Static ROC curve | The ROC curve drawing itself as you sweep the threshold, AUC area filling in |
| Two-page multi-class section | Animated softmax bars + decision-region map for iris |

---

## The visual playbook (cross-cutting)

Patterns we should use consistently across all 15 episodes:

### 1. Slider-driven scatter plots
The bread-and-butter visualization. Any time we're showing the effect of a parameter (line slope, threshold, learning rate), it's a slider with a live-updating scatter and a live-updating metric counter. Google has interactive widgets but they're flat. Ours are richer because we control the canvas.

### 2. The 5-line loop, recolored
The Ep 18 victory-lap slide reappears in every series-1 episode (Eps 19, 24, 29 conceptually) with the relevant lines highlighted in the series color (LR green, Logistic pink, Classification gold). This is the spine made visible.

### 3. Side-by-side "before / after the swap"
For Eps 24, 28, 33 — showing the LR loop next to the new loop with the single difference circled. This makes "what's actually new" tiny and obvious.

### 4. The bowl, with the model overlaid
Ep 21's signature shot: the loss-surface bowl on one side, the linear-regression line moving on a scatter on the other side, synced. The viewer sees the *abstract* (descent on a loss surface) and the *concrete* (the actual line getting fit) happening together. Calculus Ep 17 had only the abstract.

### 5. Asymptotes you can feel
Sigmoid, log-loss, ROC — all have asymptotic behavior. Animations should *try to reach* the asymptote and visibly fail. Static figures can't do this. We can.

### 6. The decision boundary, animated during training
Iris is the canonical example, but the principle generalizes. A model's "decision boundary" moves through the data as training progresses. Showing this animated turns "the model is learning" from a slogan into a thing you can watch.

### 7. Confusion-matrix scatter (the Ep 30 invention)
Instead of a 2×2 grid in abstraction, color every datapoint in the scatter plot by its TP/FP/TN/FN status. Now precision/recall/ROC are all variations on "look at the colors in the scatter." This is the most underused visualization in beginner ML content and would be a signature for our channel.

---

## How this maps back to Google

| Google sub-page | Maps to our episode(s) |
|---|---|
| Linear regression (intro) | Ep 19 |
| Loss | Ep 20 |
| Gradient descent | Ep 21 (with stronger ties to calculus Ep 17) |
| Hyperparameters | folded into Ep 21 + Ep 22 + Ep 28 (we cover lr in Ep 17, batch size + epochs in Ep 28 as "the loop's other knobs") |
| Interactive: Parameters | Eps 19, 20 (built-in, not standalone) |
| Interactive: Gradient descent | Ep 21 (built-in) |
| Logistic regression (intro) | Ep 24 |
| Calculating a probability (sigmoid) | Ep 25 |
| Loss and regularization | Ep 26 (regularization gets one slide; deserves a future episode of its own) |
| Classification (intro) | Ep 29 |
| Thresholds + confusion matrix | Eps 29 + 30 |
| Accuracy, precision, recall | Ep 31 |
| ROC + AUC | Ep 32 |
| Prediction bias | Future (it's a deployment concern more than a classification fundamental) |
| Multi-class | Ep 33 |

15 of our episodes ≈ 100 minutes of video. Google's modules total ~185 minutes of reading. Our format is *denser per minute* because the visuals do the explanatory work the prose has to do for Google.

---

## Production order

Two reasonable paths:

**Path A — concept-first.** Series 1 → 2 → 3 in chronological order. Each episode released a week apart. Total: 15 weeks of weekly releases.

**Path B — anchor-first.** Build Ep 21 (the descent animation, the calculus-to-ML bridge) first as a "this is what we're doing" anchor. Then go back and build Eps 19-20 to set it up, then forward through 22-33. Lets you demo the strongest moment early to build interest.

I'd recommend **Path A** for the channel's flow but **Path B** for one-shot proofs to test ideas.

---

## Open questions to resolve before recording

1. **Dataset throughline.** Google uses MPG for LR and spam for everything else. We could keep that, or switch to iris-as-spine since it works for both regression-ish framing (sepal length predicting petal length) and the classification framing (which species). My vote: iris throughout — one dataset, three series, deeper familiarity.

2. **Sklearn vs PyTorch demos.** Google's programming exercises are TensorFlow-based. For us: sklearn is faster to read but PyTorch ties cleanly to the calculus series' 5-line loop. My vote: show sklearn in the "you can read this" episodes for brevity, with the PyTorch 5-line loop alongside as the "under the hood" version.

3. **Where does regularization live?** Google folds it into the logistic regression module. We could do the same (one slide in Ep 26) or carve out a standalone episode after this arc. My vote: standalone, in a future "training in practice" series.

4. **Probability series — before or after?** Calculus series finale teased probability next. Probability is needed for things like "where does the loss come from?" and "what does 0.7 actually mean?" But you can teach LR/Logistic/Classification without it, just by deferring those questions. My vote: probability first (matches the original arc), then this 15-episode model trio.

---

## Companion playground content

For each series, add a `learn-ml/classical/playground/` extension to the python-and-dsa playground:

- **lr-playground**: train an LR on synthetic data with adjustable noise, lr, epochs. Show the live descent path.
- **logistic-playground**: train a logistic regressor on a 2D dataset. Drag the decision boundary by hand vs let SGD do it.
- **classification-playground**: confusion-matrix scatter that responds to a threshold slider. Live precision/recall/ROC.

These would mirror the `math/calculus-playground/` pattern: clone the repo, run the script, change a number, see what happens.

---

## What to do next

Pick one of these:

1. **Build Ep 19's deck + script** as a proof of concept. We'd see the slider-driven scatter and the LR-recolored 5-line slide working together. ~3 hours of focused work.
2. **Build Ep 21's deck + script** (the loss-surface-as-real-data bridge from calculus to ML). This is the strongest single episode — most likely to validate the format. ~4 hours.
3. **Build all 3 series' Episode 1 decks + scripts** as a pilot trio (Eps 19, 24, 29). Shows the through-line at small scale. ~10 hours.
4. **Pause this and ship the probability series first** per the calculus finale's tease. Come back to this plan after probability + statistics are done.

My vote: option 2. Ep 21 is the single deck that proves the whole format works — calculus-to-ML bridge, animated bowl, real data overlay, the 5-line callback. If that lands, the rest of the 15 episodes follow the same playbook.
