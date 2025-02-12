import numpy as np

A = np.array([[1, 1],
              [1, -1],
              [1, 2]])

Q, R = np.linalg.qr(A)

print("Matriks A:")
print(A)
print("\nMatriks Q (ortonormal):")
print(Q)
print("\nMatriks R (segitiga atas):")
print(R)

A_reconstructed = Q @ R
print("\nRekonstruksi A (Q * R):")
print(A_reconstructed)
