"""
01 · Tangent line — Ep 14 companion

Pick any point on a curve. The tangent line is the straight line that
best approximates the curve right there. The slope of the tangent IS
the derivative.

For f(x) = (1/2)x², the derivative is f'(x) = x.
So at x = 3, the slope of the tangent is 3.
At x = -2, the slope is -2.
At x = 0, the slope is 0 — the curve is flat right there.

Run this, then change X_POINT and rerun. Watch the tangent snap to
each new point.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt

# %% the function and its derivative
def f(x):  return 0.5 * x**2
def fp(x): return x          # derivative of (1/2)x² is x

# %% pick a point — change this and rerun
X_POINT = 1.5

# %% set up the curve
xs = np.linspace(-3, 3, 400)
ys = f(xs)

# %% the tangent line at X_POINT
# y - f(X_POINT) = f'(X_POINT) · (x - X_POINT)
slope = fp(X_POINT)
y_at_point = f(X_POINT)
tangent_xs = np.linspace(X_POINT - 1.5, X_POINT + 1.5, 50)
tangent_ys = y_at_point + slope * (tangent_xs - X_POINT)

# %% plot
plt.figure(figsize=(9, 6))
plt.plot(xs, ys, color='#00E5FF', linewidth=2.5, label=r'$f(x) = \frac{1}{2}x^2$')
plt.plot(tangent_xs, tangent_ys, color='#FF4081', linewidth=2,
         label=f'tangent at x={X_POINT}, slope={slope:.2f}')
plt.scatter([X_POINT], [y_at_point], color='#FF4081', s=80, zorder=5)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(alpha=0.2)
plt.title(f'Derivative at x = {X_POINT}: f\'(x) = {slope:.2f}', fontsize=13)
plt.xlabel('x'); plt.ylabel('f(x)')
plt.legend(loc='upper center')
plt.tight_layout()
plt.show()

# %% what to try
"""
Experiments:
  1. X_POINT = 0      → slope is exactly 0 (curve is flat at the minimum)
  2. X_POINT = -2     → slope is -2 (curve descending to the left of 0)
  3. X_POINT = 2.5    → slope is 2.5

  4. Change f to f(x) = x³.
     Update fp to:  def fp(x): return 3 * x**2
     Now the derivative at x=0 is also 0 — but the curve isn't at a
     minimum! It's at an inflection point. Slope-zero doesn't always
     mean minimum.

  5. Change f to f(x) = np.sin(x). Then fp is np.cos(x).
     Pick X_POINT at the peaks and valleys of sin — slope should be 0.
     Pick X_POINT halfway up — slope should be ±1.
"""
