"""
03 · Gradient field — Ep 16 companion

A 2D function — height varies across the map. At every point, the
gradient is a vector pointing in the steepest uphill direction. It's
perpendicular to the contour line through that point. Always.

This script plots the contour map and overlays the gradient field. You
should be able to see, by eye, that every arrow is at 90° to its
contour.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt

# %% the function (same shape as the Ep 16 deck)
def f(x, y):
    return -(x**2 + y**2) * 0.3 + np.sin(1.5 * x) * np.cos(1.5 * y) * 1.2

# %% the gradient — partial derivatives, by hand
def grad(x, y):
    # ∂f/∂x = -0.6x + 1.5·cos(1.5x)·cos(1.5y) · 1.2
    # ∂f/∂y = -0.6y - 1.5·sin(1.5x)·sin(1.5y) · 1.2
    dfdx = -0.6 * x + 1.5 * np.cos(1.5 * x) * np.cos(1.5 * y) * 1.2
    dfdy = -0.6 * y - 1.5 * np.sin(1.5 * x) * np.sin(1.5 * y) * 1.2
    return dfdx, dfdy

# %% grid of points
X, Y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))
Z = f(X, Y)

# %% sparse grid for the gradient arrows (full grid would be too dense)
xs = np.linspace(-3, 3, 18)
ys = np.linspace(-3, 3, 18)
Xs, Ys = np.meshgrid(xs, ys)
U, V = grad(Xs, Ys)

# %% plot
fig, ax = plt.subplots(figsize=(9, 8))
contour = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)
ax.contour(X, Y, Z, levels=12, colors='white', linewidths=0.6, alpha=0.5)

# normalize arrow lengths so they're all visible
magnitudes = np.sqrt(U**2 + V**2)
U_norm = U / (magnitudes + 1e-9)
V_norm = V / (magnitudes + 1e-9)

ax.quiver(Xs, Ys, U_norm, V_norm, color='#FF4081',
          scale=30, width=0.004, headwidth=4)

ax.set_title("the gradient field — every arrow is perpendicular to its contour", fontsize=12)
ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_aspect('equal')
plt.colorbar(contour, ax=ax, label='f(x, y)')
plt.tight_layout()
plt.show()

# %% verify perpendicularity at a sample point
"""
At any point, the gradient should be perpendicular to the tangent of
the contour line through that point.

The contour tangent at (x, y) is itself a vector that's perpendicular
to the gradient — so if we rotate the gradient by 90°, we get the
contour direction.

Quick numerical sanity check: pick a point, walk a tiny step in the
direction perpendicular to the gradient. The function value should
change by ~zero (because we stayed on the contour).
"""
px, py = 1.0, 0.5
gx, gy = grad(px, py)
# perpendicular direction: rotate (gx, gy) by 90° → (-gy, gx)
perp_x, perp_y = -gy, gx
norm = np.sqrt(perp_x**2 + perp_y**2)
perp_x /= norm; perp_y /= norm
step = 0.001
new_x, new_y = px + step * perp_x, py + step * perp_y

print(f"At point ({px}, {py}):")
print(f"  f         = {f(px, py):+.6f}")
print(f"  gradient  = ({gx:+.4f}, {gy:+.4f})")
print(f"  walking perpendicular to gradient by step {step}:")
print(f"  f at new  = {f(new_x, new_y):+.6f}")
print(f"  df        = {f(new_x, new_y) - f(px, py):+.2e}   <- ~= 0, we stayed on the contour")

# %% what to try
"""
Experiments:
  1. Change the function to f(x, y) = x² + y² (a perfect bowl).
     Update grad to return (2x, 2y).
     The contours become perfect circles. Arrows all point outward
     from the origin. Beautifully symmetric.

  2. Change to f(x, y) = x² - y² (a saddle).
     Update grad to return (2x, -2y).
     Now there's a saddle point at the origin. Gradient there is zero,
     but it's not a minimum or maximum.

  3. Verify the perpendicularity check at a few different points by
     editing (px, py). The df should always be tiny (limited by step
     size, not by error in the math).
"""
