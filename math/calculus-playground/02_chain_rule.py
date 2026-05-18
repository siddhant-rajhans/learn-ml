"""
02 · Chain rule — Ep 15 companion

f(x) = sin(x²) is a stack: inner function is x², outer is sin.

The chain rule says:
    d/dx sin(x²) = cos(x²) · 2x

Outer slope (cos at x²) times inner slope (2x). That's it.

This script does two things:
  1. Plots f and its analytical derivative side by side.
  2. Verifies the chain rule against a finite-difference approximation
     — if our hand-computed derivative is right, both should match.

If the numbers don't match within a tiny tolerance, the chain rule is
wrong. Spoiler: they match.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt

# %% the stacked function: f(x) = sin(x²)
def f(x):
    return np.sin(x**2)

# %% the derivative by chain rule: f'(x) = cos(x²) · 2x
def fp_chain(x):
    return np.cos(x**2) * (2 * x)

# %% the derivative by finite difference (the "what's the slope of a
# secant line between two very close points" definition)
def fp_finite(x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

# %% sanity check at a few specific x
print("Chain-rule vs finite-difference (should match to many digits):")
for x in [-2.0, -0.5, 0.5, 1.0, 1.5, 2.5]:
    a = fp_chain(x)
    b = fp_finite(x)
    print(f"  x = {x:+.2f}   chain: {a:+.6f}   finite: {b:+.6f}   diff: {abs(a-b):.2e}")

# %% plot f and its derivative
xs = np.linspace(-2.5, 2.5, 1000)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
ax1.plot(xs, f(xs), color='#00E5FF', linewidth=2, label=r'$f(x) = \sin(x^2)$')
ax1.axhline(0, color='gray', linewidth=0.5); ax1.grid(alpha=0.2); ax1.legend()
ax1.set_title("the stacked function")

ax2.plot(xs, fp_chain(xs), color='#FF4081', linewidth=2,
         label=r"$f'(x) = \cos(x^2) \cdot 2x$ (by chain rule)")
ax2.axhline(0, color='gray', linewidth=0.5); ax2.grid(alpha=0.2); ax2.legend()
ax2.set_title("its derivative — outer slope × inner slope")
ax2.set_xlabel("x")

plt.tight_layout()
plt.show()

# %% bump propagation — what the Ep 15 animation shows
"""
A tiny `dx` at x=1.5 propagates through both functions.

  step 1 (inner):  du ≈ dx · 2x        = dx · 3.0
  step 2 (outer):  dy ≈ du · cos(x²)   = du · cos(2.25) ≈ du · (-0.628)
  combined:        dy ≈ dx · (-1.88)
"""
x = 1.5
dx = 0.01
inner_slope = 2 * x                # f_inner'(x) = 2x
outer_slope = np.cos(x**2)         # f_outer'(u) = cos(u), evaluated at u=x²

du = dx * inner_slope
dy = du * outer_slope
direct_dy = (f(x + dx) - f(x)) / 1  # actual change in f when x moves by dx

print("\nBump propagation at x = 1.5:")
print(f"  dx                  = {dx:+.4f}")
print(f"  du (after x²)       = {du:+.4f}     (scaled by inner slope 2x = {inner_slope})")
print(f"  dy (after sin)      = {dy:+.6f}   (scaled by outer slope cos(x²) = {outer_slope:+.4f})")
print(f"  measured df         = {direct_dy:+.6f}   (~= matches dy from chain rule)")

# %% what to try
"""
Experiments:
  1. Change `x = 1.5` to `x = 0`. The chain-rule derivative is 0 there
     (since 2x = 0). Bump in: nothing propagates out. Visualized.

  2. Stack a third function: f(x) = e^(sin(x²)).
     Derivative: e^(sin(x²)) · cos(x²) · 2x.
     Three slopes multiplied. Write your own fp_chain and check it
     against fp_finite.

  3. In a neural net, this same idea runs through 60 layers. That's all
     backprop is: this chain-rule multiplication, applied 60 times in
     reverse, by the framework.
"""
