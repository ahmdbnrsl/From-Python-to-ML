
"""
MATRIKS
perkalian matriks 3x3
A = [4 5 6]
    [5 6 4]
    [6 4 5]

B = [4] 16 25 36
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

# EIGENVALUES AND EIGENVEKTOR

"""
example_matriks = [[8 7],
                  [-6 1]]

Λ = lambda atau nilai skalar
I = matriks identitas dimana matriks yang jika dijadikan pengali untuk matriks lain maka hasilnya matriks yang sama

contoh matriks identitas

[1 0] * [8 7] = [8 7]
[0 1]   [-6 1]  [-6 1]

(1⋅8)+(0⋅ -6)=8+0=8
(1⋅7)+(0⋅1)=7+0=7
(0⋅8)+(1⋅-6)=0+(-6)=-6
(0⋅7)+(1⋅1)=0+1=1

eigenvalues
det(A - ΛI) = 0

selesaikan A - ΛI
A - ΛI = [8 7]  -  [Λ  0]
         [-6 1]    [0  Λ]

[8-Λ 7]
[-6 1-Λ]

det[a b] = (a.d) - (b.c)
   [c d]

(8-Λ)(1-Λ)-(7.(-6)) = 0
(8-Λ)(1-Λ)+42
8-8Λ-Λ+Λ^2+42 = 0
Λ^2-9Λ+50 = 0

selsesaikan dengan rumus kuadratik

Λ = -(-9)±√(-9)^2-4(1)(50)/2(1) = 9±i√119/2

"""

A = np.array([[8,7], [-6, 1]])
I = np.array([[1, 0], [0, 1]])

print(I @ A)

A = np.array([[8, 7], [-6, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)


# import matplotlib.pyplot as plt

# # Matriks A
# A = np.array([[4, -2], [1, 3]])

# # Hitung eigenvalues dan eigenvectors
# eigenvalues, eigenvectors = np.linalg.eig(A)

# # Ambil eigenvector pertama dan kedua
# v1 = eigenvectors[:, 0]  # Eigenvector untuk λ = 5
# v2 = eigenvectors[:, 1]  # Eigenvector untuk λ = 0

# # Gambar sumbu x dan y
# plt.axhline(0, color='black', linewidth=1)
# plt.axvline(0, color='black', linewidth=1)

# # Plotkan eigenvectors sebelum transformasi
# plt.quiver(0, 0, v1[0], v1[1], color='r', angles='xy', scale_units='xy', scale=1, label="Eigenvector 1 (λ=5)")
# plt.quiver(0, 0, v2[0], v2[1], color='b', angles='xy', scale_units='xy', scale=1, label="Eigenvector 2 (λ=0)")

# # Transformasikan eigenvectors dengan matriks A
# Av1 = A @ v1
# Av2 = A @ v2

# # Plot hasil transformasi
# plt.quiver(0, 0, Av1[0], Av1[1], color='r', angles='xy', scale_units='xy', scale=1, linestyle='dashed', label="A*v1")
# plt.quiver(0, 0, Av2[0], Av2[1], color='b', angles='xy', scale_units='xy', scale=1, linestyle='dashed', label="A*v2")

# # Atur batas sumbu
# plt.xlim(-3, 5)
# plt.ylim(-3, 5)
# plt.legend()
# plt.grid()
# plt.title("Visualisasi Eigenvectors dan Transformasinya")
# plt.show()