#!/usr/bin/env python3
import math

print("Pure Python float division:")
for a in (1.0, -1.0, 0.0):
    try:
        res = a / -0.0
    except Exception as e:
        print(f"{a} / -0.0 -> Exception: {e!r}")
    else:
        print(f"{a} / -0.0 -> {res!r}")

print("\nUsing math.copysign and checking -0.0 representation:")
neg_zero = -0.0
print("neg_zero == 0.0:", neg_zero == 0.0)
print("math.copysign(1.0, neg_zero):", math.copysign(1.0, neg_zero))
print("repr(neg_zero):", repr(neg_zero))

try:
    import numpy as np
except Exception as e:
    print("\nNumPy not available:", e)
else:
    print("\nNumPy division:")
    for a in (1.0, -1.0, 0.0):
        res = np.divide(a, np.float64(-0.0))
        print(f"{a} / -0.0 -> {res}, isinf: {np.isinf(res)}, isnan: {np.isnan(res)}")
