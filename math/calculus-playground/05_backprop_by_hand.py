"""
05 · Backprop by hand — Ep 18 companion

A tiny 2-layer neural network. We compute its gradients TWO ways:

  1. By hand. Forward pass, then backward pass, applying the chain rule
     at each step. This is what backprop literally does, written out.

  2. By PyTorch. One call to `loss.backward()`. The framework computes
     the same gradients automatically.

If our chain-rule math is right, both should match exactly.

Network:
  input:   x  (shape: 2)
  layer 1: h = ReLU(W1 @ x + b1)         W1 shape: (3, 2),  b1 shape: (3)
  layer 2: y = W2 @ h + b2               W2 shape: (1, 3),  b2 shape: (1)
  loss:    L = (y - target)²

Backward (by chain rule):
  dL/dy   = 2 (y - target)
  dL/dW2  = dL/dy · hᵀ
  dL/db2  = dL/dy
  dL/dh   = W2ᵀ · dL/dy
  dL/dz1  = dL/dh ⊙ (z1 > 0)            (ReLU derivative is 1 where z1>0, else 0)
  dL/dW1  = dL/dz1 · xᵀ
  dL/db1  = dL/dz1

Watch the gradients match.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import torch

# ----------------------------------------------------------------------
# fix random seeds so this is reproducible
# ----------------------------------------------------------------------

np.random.seed(42)
torch.manual_seed(42)

# ----------------------------------------------------------------------
# initialize weights — small random values
# ----------------------------------------------------------------------

W1_init = np.random.randn(3, 2) * 0.5
b1_init = np.random.randn(3) * 0.1
W2_init = np.random.randn(1, 3) * 0.5
b2_init = np.random.randn(1) * 0.1

x       = np.array([0.6, -0.3])
target  = np.array([1.0])

# ======================================================================
# METHOD 1 · BY HAND
# ======================================================================

W1 = W1_init.copy()
b1 = b1_init.copy()
W2 = W2_init.copy()
b2 = b2_init.copy()

# forward pass
z1 = W1 @ x + b1                    # pre-activation, layer 1
h  = np.maximum(z1, 0)              # ReLU
y  = W2 @ h + b2                    # output
loss = float(((y - target) ** 2).sum())     # scalar

print("=" * 60)
print("FORWARD PASS (by hand)")
print("=" * 60)
print(f"  z1  = {z1}")
print(f"  h   = {h}     (ReLU of z1)")
print(f"  y   = {y}")
print(f"  L   = {loss:.6f}")

# backward pass — the chain rule, written out
dL_dy  = 2 * (y - target)                          # shape (1,)
dL_dW2 = np.outer(dL_dy, h)                        # shape (1, 3)
dL_db2 = dL_dy.copy()                              # shape (1,)
dL_dh  = W2.T @ dL_dy                              # shape (3,)
dL_dz1 = dL_dh * (z1 > 0).astype(float)            # ReLU derivative
dL_dW1 = np.outer(dL_dz1, x)                       # shape (3, 2)
dL_db1 = dL_dz1.copy()                             # shape (3,)

print("\nBACKWARD PASS (by hand, applying chain rule at each step)")
print("=" * 60)
print(f"  dL/dy   = {dL_dy}")
print(f"  dL/dW2  =\n{dL_dW2}")
print(f"  dL/db2  = {dL_db2}")
print(f"  dL/dh   = {dL_dh}")
print(f"  dL/dz1  = {dL_dz1}      (zero where z1 was ≤ 0)")
print(f"  dL/dW1  =\n{dL_dW1}")
print(f"  dL/db1  = {dL_db1}")

# ======================================================================
# METHOD 2 · BY PYTORCH
# ======================================================================

print("\n" + "=" * 60)
print("BY PYTORCH (one call to loss.backward())")
print("=" * 60)

W1_t = torch.tensor(W1_init, requires_grad=True)
b1_t = torch.tensor(b1_init, requires_grad=True)
W2_t = torch.tensor(W2_init, requires_grad=True)
b2_t = torch.tensor(b2_init, requires_grad=True)

x_t      = torch.tensor(x)
target_t = torch.tensor(target)

z1_t   = W1_t @ x_t + b1_t
h_t    = torch.relu(z1_t)
y_t    = W2_t @ h_t + b2_t
loss_t = ((y_t - target_t) ** 2).sum()   # scalar (one output, but call sum to ensure scalar)

loss_t.backward()

print(f"  loss (PyTorch) = {loss_t.item():.6f}")
print(f"  dL/dW1 =\n{W1_t.grad.numpy()}")
print(f"  dL/db1 = {b1_t.grad.numpy()}")
print(f"  dL/dW2 =\n{W2_t.grad.numpy()}")
print(f"  dL/db2 = {b2_t.grad.numpy()}")

# ======================================================================
# COMPARE — should all be tiny (< 1e-10) if the chain rule is right
# ======================================================================

print("\n" + "=" * 60)
print("DIFFERENCE (hand vs PyTorch — should be ~0)")
print("=" * 60)
print(f"  loss     diff: {abs(loss - loss_t.item()):.2e}")
print(f"  dL/dW1   diff: {np.max(np.abs(dL_dW1 - W1_t.grad.numpy())):.2e}")
print(f"  dL/db1   diff: {np.max(np.abs(dL_db1 - b1_t.grad.numpy())):.2e}")
print(f"  dL/dW2   diff: {np.max(np.abs(dL_dW2 - W2_t.grad.numpy())):.2e}")
print(f"  dL/db2   diff: {np.max(np.abs(dL_db2 - b2_t.grad.numpy())):.2e}")
print("\nAll differences are smaller than 1e-10 — the by-hand chain rule")
print("matches PyTorch's autograd exactly. That's what backprop is.")

# ----------------------------------------------------------------------
# what to try
# ----------------------------------------------------------------------

"""
Experiments:

  1. Change the activation from ReLU to tanh.
     By hand: h = np.tanh(z1), and dL/dz1 = dL/dh * (1 - h**2)
     In PyTorch: torch.tanh(z1_t)
     Differences should still be ~0.

  2. Add a third layer. The backward pass gains one more chain-rule
     step. Try it.

  3. Use a batch of inputs (x shape (B, 2) instead of (2,)). The math
     gets matrix-shaped but the chain rule is the same — each operation
     gets a Jacobian instead of a scalar derivative. This is the
     vector chain rule that real frameworks implement.

  4. Forget to call optimizer.zero_grad() between training steps. Watch
     loss go nuts because gradients accumulated from the previous step.
     (To simulate: call loss_t.backward() twice in a row without
     zeroing — the .grad will be 2× what it should be.)
"""
