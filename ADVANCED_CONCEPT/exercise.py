import math

# Faktorial dari 1 hingga 5
factorial = [math.factorial(x) for x in range(1, 6)]
print(f"Faktorial dari 1 hingga 5: {factorial}")

# Angka ganjil dari 1 hingga 20
odd = [i for i in range(1, 21) if i % 2 != 0]
print(f"Angka ganjil dari 1 hingga 20: {odd}")

# Matriks 3 × 3
matriks = [[j for j in range(1, 4)] for _ in range(3)]
print("Matriks 3 × 3:")
for row in matriks:
    print(row)

# Cara 1: Menggunakan range langsung
matriks1 = [[j for j in range(i, i + 3)] for i in range(1, 10, 3)]
print(f"Matriks Cara 1: {matriks1}")

# Cara 2: Menggunakan slicing
angka = list(range(1, 10))
print(angka)
print(angka[3:])
matriks2 = [angka[i:i + 3] for i in range(0, len(angka), 3)]
print(f"Matriks Cara 2: {matriks2}")