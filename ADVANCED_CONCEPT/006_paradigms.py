# Imperative paradigm
angka = [1, 2, 3, 4, 5]
hasil = []
for i in angka:
    hasil.append(i * 2)
print(hasil)  # Output: [2, 4, 6, 8, 10]

# Procedural paradigm 
def hitung_dobel(angka):
    hasil = []
    for i in angka:
        hasil.append(i * 2)
    return hasil

print(hitung_dobel([1, 2, 3, 4, 5]))  # Output: [2, 4, 6, 8, 10]

# OOP paradigm
class Pengolah:
    def __init__(self, angka):
        self.angka = angka

    def hitung_dobel(self):
        return [i * 2 for i in self.angka]

objek = Pengolah([1, 2, 3, 4, 5])
print(objek.hitung_dobel())  # Output: [2, 4, 6, 8, 10]

# Functional paradigm
angka = [1, 2, 3, 4, 5]

# Menggunakan map untuk menghitung dobel
hasil = list(map(lambda x: x * 2, angka))
print(hasil)  # Output: [2, 4, 6, 8, 10]

# Declarative paradigm
# Mencari angka genap menggunakan list comprehension
angka = [1, 2, 3, 4, 5]
genap = [i for i in angka if i % 2 == 0]
print(genap)  # Output: [2, 4]