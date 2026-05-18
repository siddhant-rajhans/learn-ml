# calculus-playground

Five tiny Python scripts that go with the five-episode calculus series on the YouTube channel.

Each one lets you change a number, re-run, and *see what happens*. The math stops being abstract the moment you can break it.

## What's here

| Script | Maps to | What you do with it |
|--------|---------|---------------------|
| `01_tangent_line.py` | Ep 14 — Derivative | Pick any x. See the tangent line snap to it. Watch the slope go positive, negative, zero. |
| `02_chain_rule.py` | Ep 15 — Chain rule | A tiny bump in x propagates through `sin(x²)`. Watch each layer scale it. |
| `03_gradient_field.py` | Ep 16 — Gradient | Contour map of a 2D function with the gradient field overlaid. See gradients always point uphill, perpendicular to contours. |
| `04_descent_tuner.py` | Ep 17 — Gradient descent | **Fully built.** Change the learning rate. Watch convergence, watch it explode, watch it crawl. |
| `05_backprop_by_hand.py` | Ep 18 — Backprop | Compute gradients on a 2-layer net the manual way, then compare to PyTorch's `loss.backward()`. They match. |

## Run it

```bash
git clone https://github.com/siddhant-rajhans/learn-ml.git
cd learn-ml/math/calculus-playground
pip install -r requirements.txt
python 04_descent_tuner.py
```

The plots open in a window. Close the window, edit a number in the script, run again. That's the whole loop.

## Why scripts and not notebooks

Scripts run with one command. No Jupyter setup, no kernel mismatch, no "I'll get to it later." If you prefer notebooks, every script is structured with `# %%` cell markers — VSCode and PyCharm convert them automatically.

## Where the experiments lead

The point of each script is the *thing you can break*. Start with the suggested experiments at the bottom of each file. Then change anything else you want.

Episode 17 includes the line "nobody fully knows why gradient descent works as well as it does." Run `04_descent_tuner.py` for fifteen minutes and you'll have a much more visceral relationship with that statement.

## Questions, broken things, suggestions

Open an issue on the [learn-ml repo](https://github.com/siddhant-rajhans/learn-ml). The calculus series will keep evolving.
