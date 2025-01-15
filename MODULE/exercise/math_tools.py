def penjumlahan(angka_1, angka_2):
    return angka_1 + angka_2
    
def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        raise ValueError("Pembagi tidak boleh nol.")
    return a / b

def pangkat(a, b):
    return a ** b

def faktorial(n):
    if n < 0:
        raise ValueError("Angka harus positif.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result