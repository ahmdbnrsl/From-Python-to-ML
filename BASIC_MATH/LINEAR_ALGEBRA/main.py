
"""
MATRIKS
perkalian matriks 3x3
A = [4 5 6]
    [5 6 4]
    [6 4 5]

B = [4]
    [5]
    [6]

A * B

RESULT = [77]
         [74]
         [74]

hitung panjang vektor (magnitudo) dan normalisasi
V = [3]
    [4]
    [5]

magnitudo (panjang vektor)
||V|| = √3^2 + 4^2 + 5^2 = 7.071
normalisasi
Vnorm = V / ||V|| = [3/7.071] [0.424]
                    [4/7.071] [0.565]
                    [5/7.071] [0.707]

penjumlahan matriks 2x2
C = [7, 5]
    [3, 1]

D = [1, 4]
    [3, 9]

RESULT = [8, 9]
         [6, 10]
"""

import numpy as np

# Matriks
A = np.array([[4,5,6], [5,6,4], [6,4,5]])
B = np.array([[4], [5], [6]])
C = np.array([[7,5], [3,1]])
D = np.array([[1, 4], [3,9]])

# Perkalian Matriks
print("Hasil Perkalian Matriks A * B:\n", A @ B)

# Transformasi (Transpose)
print("Transpose Matriks A:\n", A.T)

# Penjumlahan Matriks C + D
print("Hasil Penjumlahan Matriks C + D:\n", C + D)

# Vektor
V = np.array([3,4,5])

# Menghitung Magnitudo (Panjang Vektor)
magnitudo = np.linalg.norm(V)
print("Magnitudo Vektor V:", magnitudo)

# Normalisasi Vektor
normalisasi = V / magnitudo
print("Normalisasi Vektor V:\n", normalisasi)