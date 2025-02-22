import numpy as np


def cholesky_decomposition(A):
    """
    Menghitung dekomposisi Cholesky dari matriks A (simetris positif-definit)
    sehingga A = L * L^T.

    Parameters:
      A (np.ndarray): Matriks simetris positif-definit berukuran n x n.

    Returns:
      L (np.ndarray): Matriks segitiga bawah yang memenuhi A = L * L^T.
    """
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                # Elemen diagonal: L[i,i] = sqrt(A[i,i] - sum_{k=0}^{i-1} L[i,k]^2)
                L[i, i] = np.sqrt(A[i, i] - np.sum(L[i, :i] ** 2))
            else:
                # Elemen non-diagonal: L[i,j] = (A[i,j] - sum_{k=0}^{j-1} L[i,k]*L[j,k]) / L[j,j]
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L


# Contoh Matriks A
A = np.array([[4, 2],
              [2, 3]], dtype=float)

L = cholesky_decomposition(A)
print("Matriks A:")
print(A)
print("\nMatriks L (hasil Cholesky):")
print(L)
print("\nVerifikasi: L * L^T")
print(L @ L.T)

L_2 = np.linalg.cholesky(A)

print("Matriks A:")
print(A)
print("\nMatriks L (hasil Cholesky):")
print(L_2)
print("\nVerifikasi (L * L^T):")
print(np.dot(L_2, L_2.T))


# Matriks A (simetris positif-definit) dan vektor b
A = np.array([[4, 2],
              [2, 3]], dtype=float)
b = np.array([2, 5], dtype=float)

# Hitung dekomposisi Cholesky: A = L * L^T
L = cholesky_decomposition(A)

# Selesaikan L * y = b untuk y (forward substitution)
y = np.linalg.solve(L, b)

# Selesaikan L^T * x = y untuk x (back substitution)
x = np.linalg.solve(L.T, y)

print("Solusi x dari Ax = b:")
print(x)
