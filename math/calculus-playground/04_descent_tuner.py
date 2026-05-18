"""
04 · Descent tuner — Ep 17 companion · FULLY BUILT

The single most important number in training a neural network is the
learning rate. Too small: training takes forever. Too big: training
explodes. Just right: it converges.

This script runs three descents on the same loss surface, each with a
different learning rate, and plots all three paths side by side.

  LEARNING_RATES = [0.01, 0.30, 1.5]
                    ↑     ↑      ↑
                   too   just   too
                   small right  large

It also plots the loss-over-time curve for each, so you can SEE the
difference between "crawling," "converging," and "exploding."

Then — the interesting part — change LEARNING_RATES to any list of
values you want. Find the smallest one that converges in under 50 steps.
Find the largest one that doesn't explode. Notice that the boundary is
narrower than you'd think.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# the loss surface — same one as the Ep 17 deck
# ----------------------------------------------------------------------

def loss(x, y):
    return 0.5 * x**2 + 1.4 * y**2 + 0.3 * np.sin(2 * x) * np.cos(2 * y)

def gradient(x, y):
    # ∂L/∂x = x + 0.6·cos(2x)·cos(2y)
    # ∂L/∂y = 2.8y - 0.6·sin(2x)·sin(2y)
    dLdx = x + 0.6 * np.cos(2 * x) * np.cos(2 * y)
    dLdy = 2.8 * y - 0.6 * np.sin(2 * x) * np.sin(2 * y)
    return np.array([dLdx, dLdy])

# ----------------------------------------------------------------------
# the descent algorithm — three lines, just like Ep 17 said
# ----------------------------------------------------------------------

def descend(start, lr, steps=50, max_norm=20):
    """Run gradient descent. Returns the path and the loss history.

    max_norm: if any coordinate blows past this magnitude we stop early
              and label the run as 'EXPLODED'. Prevents the plot from
              going to infinity when lr is too aggressive.
    """
    path = [np.array(start, dtype=float)]
    losses = [float(loss(*start))]
    exploded = False
    for _ in range(steps):
        pos = path[-1]
        g = gradient(*pos)
        new_pos = pos - lr * g
        if np.max(np.abs(new_pos)) > max_norm:
            exploded = True
            break
        path.append(new_pos)
        losses.append(float(loss(*new_pos)))
    return np.array(path), np.array(losses), exploded

# ----------------------------------------------------------------------
# experiment config — CHANGE THIS
# ----------------------------------------------------------------------

START_POINT    = (-2.0, 1.8)
LEARNING_RATES = [0.01, 0.30, 1.5]
STEPS          = 50

# ----------------------------------------------------------------------
# run all three
# ----------------------------------------------------------------------

runs = []
for lr in LEARNING_RATES:
    path, losses, exploded = descend(START_POINT, lr, STEPS)
    runs.append({
        'lr': lr,
        'path': path,
        'losses': losses,
        'exploded': exploded,
        'final_loss': losses[-1],
        'steps_taken': len(losses) - 1,
    })

# ----------------------------------------------------------------------
# print summary
# ----------------------------------------------------------------------

print(f"\nStarting point: {START_POINT}")
print(f"Initial loss:   {loss(*START_POINT):.4f}\n")
print(f"{'lr':>8} | {'final loss':>12} | {'steps':>6} | status")
print("-" * 55)
for r in runs:
    status = "EXPLODED" if r['exploded'] else "converged" if r['final_loss'] < 0.1 else "crawling"
    print(f"{r['lr']:>8.4f} | {r['final_loss']:>12.4f} | {r['steps_taken']:>6} | {status}")

# ----------------------------------------------------------------------
# plot — paths on a contour map + loss curves
# ----------------------------------------------------------------------

fig, (ax_map, ax_loss) = plt.subplots(1, 2, figsize=(14, 6))

# left: contour map with all paths overlaid
X, Y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))
Z = loss(X, Y)
ax_map.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.7)
ax_map.contour(X, Y, Z, levels=10, colors='white', linewidths=0.4, alpha=0.4)

colors = ['#7C4DFF', '#00E676', '#FF4081']  # purple / green / pink
for r, color in zip(runs, colors):
    label = f"lr = {r['lr']:.2f}"
    if r['exploded']:
        label += " (exploded)"
    ax_map.plot(r['path'][:, 0], r['path'][:, 1], '-o',
                color=color, markersize=4, linewidth=1.5, label=label)
    ax_map.scatter([r['path'][0, 0]], [r['path'][0, 1]], color=color,
                   s=120, edgecolors='white', linewidths=2, zorder=5)

ax_map.set_title(f"three learning rates · same starting point · same loss surface")
ax_map.set_xlabel("x"); ax_map.set_ylabel("y")
ax_map.legend(loc='upper right')
ax_map.set_aspect('equal')
ax_map.set_xlim(-3, 3); ax_map.set_ylim(-3, 3)

# right: loss over time
for r, color in zip(runs, colors):
    label = f"lr = {r['lr']:.2f}"
    if r['exploded']:
        label += " ↑ exploded"
    ax_loss.plot(r['losses'], '-', color=color, linewidth=2, label=label)
ax_loss.set_title("loss over time")
ax_loss.set_xlabel("step"); ax_loss.set_ylabel("loss")
ax_loss.set_yscale('log')
ax_loss.grid(alpha=0.3)
ax_loss.legend(loc='upper right')

plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------
# what to try
# ----------------------------------------------------------------------

"""
Suggested experiments:

  1. Replace LEARNING_RATES with a finer sweep:
        LEARNING_RATES = [0.01, 0.05, 0.1, 0.3, 0.6, 1.0, 1.5]
     Watch the trajectories diverge. There's a "Goldilocks zone"
     somewhere between 0.1 and 0.6 where convergence is fastest.

  2. Find the largest LR that still converges. Binary search:
     start with lr=0.8, try lr=1.0, try lr=1.2... You'll find the cliff
     somewhere around lr ≈ 0.9-1.1 for this surface. Beyond that, it
     bounces and never settles.

  3. Find the smallest LR that converges in 50 steps. Try 0.001, 0.005,
     0.01, 0.05... Anything below ~0.05 will still be very far from the
     minimum after 50 steps.

  4. Change START_POINT to (0.5, 0.5). Some learning rates that worked
     from far away now overshoot easily. The "right" LR depends on
     where you start.

  5. Modify the loss function. Make it sharper:
        return 5 * x**2 + 14 * y**2 + ...
     Now the same lr that worked before is too big. The "right" LR
     depends on the curvature of the loss. This is why Adam exists —
     it adapts the LR per-parameter using past gradients.

  6. Hard mode: implement momentum. Change the descend loop:
        v = np.zeros(2)
        for _ in range(steps):
            g = gradient(*path[-1])
            v = 0.9 * v + g           # running average of gradients
            new_pos = path[-1] - lr * v
     Try lr=0.30 with momentum. Notice it accelerates through flat
     regions and overshoots less. That's the second biggest
     optimizer improvement after just having a sane LR.
"""
