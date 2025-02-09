import math
import numpy as np


class SVD:
    def __init__(self, A):
        self.A = A
        self.m = len(A)
        self.n = len(A[0])
        self.U = None
        self.S = None
        self.V = None
        self.compute_svd()

    def compute_svd(self):
        At = self.transpose(self.A)
        AtA = self.mat_mult(At, self.A)

        eigenvalues, eigenvectors = self.jacobi(AtA)

        indices = sorted(range(len(eigenvalues)),
                         key=lambda i: eigenvalues[i], reverse=True)
        eigenvalues = [eigenvalues[i] for i in indices]
        eigenvectors = [eigenvectors[i] for i in indices]

        self.S = [math.sqrt(ev) if ev > 0 else 0 for ev in eigenvalues]

        self.V = []
        for i in range(self.n):
            col = [eigenvectors[j][i] for j in range(self.n)]
            self.V.append(col)

        U_cols = []
        for i in range(self.n):
            sigma = self.S[i]
            v_i = [self.V[j][i] for j in range(self.n)]
            if sigma > 1e-10:
                Av = self.mat_vec_mult(self.A, v_i)
                u_i = [x / sigma for x in Av]
            else:
                u_i = [0 for _ in range(self.m)]
            U_cols.append(u_i)
        self.U = self.transpose(U_cols)

    def transpose(self, M):
        return [list(row) for row in zip(*M)]

    def mat_mult(self, A, B):
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                s = 0
                for k in range(len(A[0])):
                    s += A[i][k] * B[k][j]
                row.append(s)
            result.append(row)
        return result

    def mat_vec_mult(self, A, v):
        result = []
        for row in A:
            s = 0
            for i in range(len(v)):
                s += row[i] * v[i]
            result.append(s)
        return result

    def identity(self, n):
        I = [[0] * n for _ in range(n)]
        for i in range(n):
            I[i][i] = 1
        return I

    def jacobi(self, A, tol=1e-10, max_iter=100):
        n = len(A)
        A = [row[:] for row in A]
        V = self.identity(n)
        for _ in range(max_iter):
            max_val = 0
            p, q = 0, 1
            for i in range(n):
                for j in range(i+1, n):
                    if abs(A[i][j]) > max_val:
                        max_val = abs(A[i][j])
                        p, q = i, j
            if max_val < tol:
                break
            if abs(A[p][p] - A[q][q]) < tol:
                theta = math.pi / 4
            else:
                theta = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
            cos = math.cos(theta)
            sin = math.sin(theta)
            app = A[p][p]
            aqq = A[q][q]
            apq = A[p][q]
            A[p][p] = cos * cos * app - 2 * sin * cos * apq + sin * sin * aqq
            A[q][q] = sin * sin * app + 2 * sin * cos * apq + cos * cos * aqq
            A[p][q] = 0
            A[q][p] = 0
            for i in range(n):
                if i != p and i != q:
                    aip = A[i][p]
                    aiq = A[i][q]
                    A[i][p] = cos * aip - sin * aiq
                    A[p][i] = A[i][p]
                    A[i][q] = sin * aip + cos * aiq
                    A[q][i] = A[i][q]
            for i in range(n):
                vip = V[i][p]
                viq = V[i][q]
                V[i][p] = cos * vip - sin * viq
                V[i][q] = sin * vip + cos * viq
        eigenvalues = [A[i][i] for i in range(n)]
        eigenvectors = []
        for j in range(n):
            vec = [V[i][j] for i in range(n)]
            eigenvectors.append(vec)
        return eigenvalues, eigenvectors


if __name__ == '__main__':
    A = [
        [3, 1],
        [2, 2],
        [1, 3]
    ]
    svd = SVD(A)
    u, s, vt = np.linalg.svd(np.array(A))

    print("Matriks A:")
    print(np.array(A))

    print("\nMatriks U (ukuran m x n):")
    print(u)
    print(np.array(svd.U))

    print("\nNilai Singular:")
    print(s)
    print(np.array(svd.S))

    print("\nMatriks V (setiap baris merupakan elemen dari kolom eigenvector):")
    print(vt)
    print(np.array(svd.V))
