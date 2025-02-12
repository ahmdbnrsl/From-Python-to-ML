import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, -28])

X = np.column_stack((x, np.ones(x.shape[0])))

Q, R = np.linalg.qr(X)

beta = np.linalg.inv(R) @ Q.T @ y
print("Parameter garis (m, c):", beta)

plt.scatter(x, y, label="Data")
plt.plot(x, X @ beta, color='red', label="Garis Regresi")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Least Squares dengan QR Decomposition")
plt.show()
