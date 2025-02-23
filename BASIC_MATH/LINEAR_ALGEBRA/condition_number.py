import numpy as np


def compute_condition_number(A):
    """
    Menghitung condition number matriks A menggunakan norma 2.
    Jika A tidak dapat dibalik, condition number dianggap sebagai infinity.
    """
    # Hitung nilai singular dari A menggunakan SVD
    U, s, Vt = np.linalg.svd(A)
    # s adalah array nilai singular, pastikan tidak ada nilai singular yang terlalu kecil
    if np.min(s) < 1e-12:
        return np.inf  # Matriks hampir singular atau singular
    cond_number = np.max(s) / np.min(s)
    return cond_number


# Contoh penggunaan:
# Definisikan sebuah matriks A
A = np.array([
    [1, 2, 1],
    [-2, -3, 1],
    [3, 5, 0]
], dtype=float)

# Hitung condition number matriks A
cond_A = compute_condition_number(A)
print("Condition number (norma 2) dari matriks A adalah:", cond_A)

# Alternatif: NumPy sudah menyediakan fungsi untuk ini
cond_np = np.linalg.cond(A)
print("Condition number (np.linalg.cond) =", cond_np)


"""
        Matriks A
             │
             ▼
         Hitung AᵀA
             │
             ▼
    AᵀA = [10  14; 14  20]
             │
             ▼
   Hitung Eigenvalue λ dari AᵀA
             │
    λ₁ = 15 + √221,   λ₂ = 15 − √221
             │
             ▼
   Hitung Nilai Singular: σ = √λ
             │
    σ_max ≈ √(29.866) ≈ 5.465
    σ_min ≈ √(0.134)  ≈ 0.366
             │
             ▼
   Condition Number: κ(A) = σ_max/σ_min ≈ 14.93
"""
