import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float

# Muat gambar contoh (grayscale) dari skimage
img = img_as_float(data.camera())

# Lakukan SVD pada gambar
U, S, Vt = np.linalg.svd(img, full_matrices=False)

# Pilih hanya k singular values teratas (misalnya, k = 50)
k = 50
S_k = np.diag(S[:k])
img_compressed = U[:, :k] @ S_k @ Vt[:k, :]

# Visualisasikan gambar asli dan terkompresi
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(img, cmap='gray')
axes[0].set_title("Gambar Asli")
axes[0].axis('on')

axes[1].imshow(img_compressed, cmap='gray')
axes[1].set_title(f"Gambar Terkompresi (k = {k})")
axes[1].axis('on')

plt.show()
