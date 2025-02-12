import numpy as np


def gram_schmidt(V):
    (m, n) = V.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    print("Q:", Q)
    print("R:", R)
    print('M: ', m)
    print('N: ', n)

    for j in range(n):
        v = V[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], v)
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    return Q, R


A_manual = np.array([[1, 1],
                     [1, -1],
                     [1, 2]], dtype=float)

Q_manual, R_manual = gram_schmidt(A_manual)
print("Matriks Q (manual Gram-Schmidt):")
print(Q_manual)
print("\nMatriks R (manual Gram-Schmidt):")
print(R_manual)
