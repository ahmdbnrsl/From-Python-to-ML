import numpy as np
import math

V = np.array([1, -2, 3, -4, -5, -6, 7, -8, -9, -10])


def l0_norm(v):
    if len(v) == 0:
        return 0
    else:
        return sum([1 for i in v if i != 0])


def l1_norm(v):
    if len(v) == 0:
        return 0
    else:
        return sum([abs(i) for i in v])


def l2_norm(v):
    if len(v) == 0:
        return 0
    else:
        return math.sqrt(sum([i**2 for i in v]))


def l_inf_norm(v):
    if len(v) == 0:
        return 0
    else:
        return max([abs(i) for i in v])


v_2 = np.array([0, 10, -2])
l0 = l0_norm(v_2)
print("L0 norm:", l0)

l1 = l1_norm(V)
print("L1 norm:", l1)

l2 = l2_norm(V)
print("L2 norm:", l2)

l_inf = l_inf_norm(V)
print("L infinity norm:", l_inf)
