import numpy as np

V1 = np.array([8, -2, 9, -7, -5, 0, 2, -9, -9, -3])
V2 = np.array([10, -7, 3, -3, -2, -6, 1, -9, -9, -4])


def euclidian_distance(V1, V2):
    return np.sqrt(np.sum((V1 - V2) ** 2))


print((V1 - V2) ** 2)
print(euclidian_distance(V1, V2))


def manhattan_distance(V1, V2):
    return np.sum(np.abs(V1 - V2))


print(np.abs(V1 - V2))
print(manhattan_distance(V1, V2))
