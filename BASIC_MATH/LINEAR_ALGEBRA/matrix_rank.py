import numpy as np


def gaussian_elimination(matrix, tol=1e-12):
    """
    Melakukan eliminasi Gauss pada matriks dan mengembalikan bentuk row echelon serta rank.

    Parameters:
        matrix : list of lists
            Matriks input sebagai list baris.
        tol : float
            Toleransi untuk menganggap nilai sebagai nol (default: 1e-12).

    Returns:
        A : list of lists
            Matriks dalam bentuk row echelon.
        rank : int
            Jumlah baris non-nol (rank matriks).
    """
    # Salin matriks untuk menghindari modifikasi matriks asli
    A = [row[:] for row in matrix]
    m = len(A)        # jumlah baris
    if m == 0:
        return A, 0
    n = len(A[0])     # jumlah kolom
    rank = 0          # inisialisasi rank

    for col in range(n):
        # Temukan baris pivot: cari baris dengan elemen tak nol di kolom 'col'
        pivot_row = None
        for row in range(rank, m):
            if abs(A[row][col]) > tol:
                pivot_row = row
                break
        # Jika tidak ada baris dengan elemen tak nol di kolom ini, lanjut ke kolom berikutnya
        if pivot_row is None:
            continue

        # Tukar baris pivot dengan baris 'rank' (jika berbeda)
        A[rank], A[pivot_row] = A[pivot_row], A[rank]

        # Normalisasi baris pivot sehingga elemen pivot menjadi 1
        pivot_val = A[rank][col]
        A[rank] = [x / pivot_val for x in A[rank]]

        # Eliminasi elemen di bawah pivot (jadikan nol)
        for r in range(rank + 1, m):
            factor = A[r][col]
            A[r] = [a - factor * b for a, b in zip(A[r], A[rank])]

        rank += 1  # naikkan jumlah baris non-nol (pivot)
        if rank == m:
            break

    return A, rank


matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [1, 0, 1]
]

row_echelon, rank = gaussian_elimination(matrix)

print("Bentuk Row Echelon:")
for row in row_echelon:
    print(row)
print("Rank =", rank)

A = np.array([[1, 2, 3],
              [2, 4, 6],
              [1, 0, 1]])

rank_A = np.linalg.matrix_rank(A)
print("Rank Matriks A:", rank_A)
