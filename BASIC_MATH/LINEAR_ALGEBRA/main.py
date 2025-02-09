from sklearn.cluster import KMeans
import pandas as pd
import json
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np


class Console:
    def __init__(self):
        pass

    def log(self, *args):
        print(*args)


console = Console()
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


# Matriks
A = np.array([[4, 5, 6], [5, 6, 4], [6, 4, 5]])
B = np.array([[4], [5], [6]])
C = np.array([[7, 5], [3, 1]])
D = np.array([[1, 4], [3, 9]])

# Perkalian Matriks
print("Hasil Perkalian Matriks A * B:\n", A @ B)

# Transformasi (Transpose)
print("Transpose Matriks A:\n", A.T)

# Penjumlahan Matriks C + D
print("Hasil Penjumlahan Matriks C + D:\n", C + D)

# Vektor
V = np.array([3, 4, 5])

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

A = [5 4]
    [2 3]

det(A - ΛI)
[5 4] - [Λ 0]
[2 3]   [0 Λ]

[5-Λ  4]
[2    3-Λ]

(5-Λ)(3-Λ) - 2.4 = 0
(5-Λ)(3-Λ) - 8 = 0
15-5Λ-3Λ+Λ^2-8 =0
Λ^2-8Λ+7 = 0

(-7) * (-1) = 7
(-7) + (-1) = -8

eigen values = [7, 1]

(A-ΛI)V = 0

[5-7 4]
[2 3-7]

[-2 4]  [x] = [0]
[2 -4]  [y]   [0]

-2x +4y = 0
4y = 2x 
y = x/2


"""

A = np.array([[8, 7], [-6, 1]])
I = np.array([[1, 0], [0, 1]])

print(I @ A)

A = np.array([[8, 7], [-6, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)

A = np.array([[5, 4], [2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues, eigenvectors)

A = np.array([[6, 2, 0], [1, 5, -1], [0, 2, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues, '\n', eigenvectors)

B = np.array([[3, 0], [8, -1]])
eigenvalues, eigenvectors = np.linalg.eig(B)
print(eigenvalues, '\n', eigenvectors)

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

# impelement on python

# import numpy as np

# X = np.array([
#     [2.5, 2.4, 0.5],
#     [0.5, 0.7, -1.2],
#     [2.2, 2.9, 0.3],
#     [1.9, 2.2, 0.1],
#     [3.1, 3.0, 1.2],
#     [2.3, 2.7, 0.4],
#     [2, 1.6, -0.5],
#     [1, 1.1, -1.0],
#     [1.5, 1.6, -0.8],
#     [1.1, 0.9, -1.3]
# ])

# pca = PCA(n_components=2)
# X_reduced = pca.fit_transform(X)
# console.log(X_reduced)

# console.log("Eigenvectors (komponen utama):")
# console.log(pca.components_)

# console.log("Eigenvalues (variansi per komponen):")
# console.log(pca.explained_variance_)

# plt.scatter(X_reduced[:, 0], X_reduced[:, 1])
# plt.title("Data setelah PCA")
# plt.xlabel("Komponen 1")
# plt.ylabel("Komponen 2")
# plt.show()

# import numpy as np

# np.random.seed(42)
# n_samples = 100

# square_footage = np.random.normal(2000, 300, n_samples)
# num_rooms = np.random.normal(1, 4, n_samples)
# price = square_footage * 150 + num_rooms * 10000 + np.random.normal(0, 20000, n_samples)


# X = np.column_stack((square_footage, num_rooms, price))

# pca = PCA(n_components=2)
# data_reduced = pca.fit_transform(X)

# console.log("Eigenvectors (komponen utama):\n", pca.components_)
# console.log("\nExplained Variance (variansi yang dijelaskan):\n", pca.explained_variance_)


# plt.figure(figsize=(8, 6))
# plt.scatter(data_reduced[:, 0], data_reduced[:, 1], alpha=0.7)
# plt.xlabel("Komponen Utama 1")
# plt.ylabel("Komponen Utama 2")
# plt.title("Visualisasi Data Rumah setelah PCA\n(Mengurangi 3 Fitur Menjadi 2 Komponen)")
# plt.grid(True)
# plt.show()


# Contoh data JSON sebagai string
json_data = """
{
  "students": [
    {"name": "Alice", "age": 20, "gpa": 3.8, "credits": 120, "score": 85},
    {"name": "Bob", "age": 22, "gpa": 3.2, "credits": 110, "score": 78},
    {"name": "Charlie", "age": 21, "gpa": 3.5, "credits": 130, "score": 82},
    {"name": "David", "age": 23, "gpa": 3.0, "credits": 100, "score": 75},
    {"name": "Eva", "age": 20, "gpa": 3.9, "credits": 125, "score": 88}
  ]
}
"""

# 1. Muat data JSON dan ubah menjadi DataFrame
# data = json.loads(json_data)
# students = data["students"]
# df = pd.DataFrame(students)

# console.log(df)

# # 2. Ekstrak fitur numerik (kita buang kolom 'name' agar hanya ada fitur angka)
# df_numeric = df.drop(columns=["name"])

# # 3. Terapkan PCA untuk mereduksi dari 4 fitur menjadi 2 komponen utama
# pca = PCA(n_components=2)
# principal_components = pca.fit_transform(df_numeric)

# # Buat DataFrame baru untuk komponen utama
# df_pca = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
# # Simpan nama mahasiswa untuk keperluan anotasi
# df_pca['name'] = df['name']

# json_result = df_pca.to_json(orient='records', indent=4)
# with open('result_pca.json', 'w') as file:
#     file.write(json_result)

# # 4. Tampilkan hasil komponen utama
# print("Hasil Principal Components:")
# print(df_pca)

# # 5. Visualisasikan hasil PCA
# plt.figure(figsize=(8, 6))
# plt.scatter(df_pca['PC1'], df_pca['PC2'], alpha=0.8)

# # Tambahkan label nama untuk setiap titik data
# for i, txt in enumerate(df_pca['name']):
#     plt.annotate(txt, (df_pca['PC1'][i], df_pca['PC2'][i]))

# plt.title("Visualisasi Data Mahasiswa setelah PCA")
# plt.xlabel("Komponen Utama 1")
# plt.ylabel("Komponen Utama 2")
# plt.grid(True)
# plt.show()


# Misalkan A adalah matriks persegi yang invertible
A = np.array([[4, 7],
              [2, 6]])

# Hitung inversnya
A_inv = np.linalg.inv(A)

# Verifikasi: A * A_inv harus menghasilkan matriks identitas
I = A @ A_inv
print("Matriks A:")
print(A)
print("\nInvers Matriks A:")
print(A_inv)
print("\nA dikalikan dengan A_inv (harus identitas):")
print(I)
print(A @ I)

B = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Hitung pseudoinversnya
B_pinv = np.linalg.pinv(B)

# Verifikasi: B * B_pinv * B harus mendekati B
B_reconstructed = B @ B_pinv @ B
print("\nMatriks B:")
print(B)
print("\nPseudoinvers Matriks B:")
print(B_pinv)
print("\nRekonstruksi B (B * B_pinv * B):")
print(B_reconstructed)

A = np.array([[3, 2],
              [2, 3]])

U, S, Vt = np.linalg.svd(A)

print("Matriks U:")
print(U)
print("\nSingular Values (S):")
print(S)
print("\nMatriks V^T:")
print(Vt)

# implement norm of vector in data clustering

data = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 100],
    [65, 70, 75],
    [88, 87, 90]
])

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)
labels = kmeans.labels_

print("Label klaster untuk tiap mahasiswa:", labels)

plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=100)
plt.xlabel("Nilai Ujian")
plt.ylabel("Rata-rata Tugas")
plt.title("Pengelompokan Mahasiswa Berdasarkan Performanya")
plt.show()
